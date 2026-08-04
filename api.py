import os
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "tr-TR,tr;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Origin": "https://mgm.gov.tr",
    "Pragma": "no-cache",
    "Referer": "https://mgm.gov.tr/",
    "User-Agent": (
        "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like"
        " Gecko) Chrome/139.0.0.0 Mobile Safari/537.36"
    ),
}


# GÜVENLİ İSTEK ATICI (MGM Çökerse Kod Patlamaz)
def safe_mgm_request(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=8)

        # MGM 200 dönmediyse veya yanıt boşsa
        if response.status_code != 200:
            return None, f"MGM Servis Hatası (HTTP {response.status_code})"

        # JSON Parse kontrolü (MGM Bazen HTML hata sayfası döndürür)
        try:
            data = response.json()
            return data, None
        except ValueError:
            return None, "MGM yanıtı geçersiz JSON formatında."

    except requests.exceptions.Timeout:
        return None, "MGM sunucusundan yanıt zaman aşımına uğradı (Timeout)."
    except requests.exceptions.RequestException as e:
        return None, f"Baglanti hatasi: {str(e)}"


# MERKEZ ID ÇEKİCİ
def get_merkez_ids(il="Antalya", ilce="Kepez"):
    url = f"https://servis.mgm.gov.tr/web/merkezler?il={il}&ilce={ilce}"
    data, err = safe_mgm_request(url)

    if err or not isinstance(data, list) or len(data) == 0:
        return None

    return {
        "merkezId": data[0].get("merkezId"),
        "saatlikTahminIstNo": data[0].get("saatlikTahminIstNo"),
        "gunlukTahminIstNo": data[0].get("gunlukTahminIstNo"),
    }


# ==========================================
# ENDPOINT'LER
# ==========================================


@app.route("/ping")
def ping():
    return jsonify({"status": "pong", "message": "Sistem zehir gibi ayakta!"}), 200


@app.route("/anlik")
def anlik():
    il = request.args.get("il", "Antalya")
    ilce = request.args.get("ilce", "Kepez")

    ids = get_merkez_ids(il, ilce)
    if not ids or not ids.get("merkezId"):
        return (
            jsonify({
                "success": False,
                "error": f"'{il}/{ilce}' için merkez bilgisi çekilemedi.",
            }),
            404,
        )

    url = (
        "https://servis.mgm.gov.tr/web/sondurumlar?merkezid="
        + str(ids["merkezId"])
    )
    data, err = safe_mgm_request(url)

    if err:
        return jsonify({"success": False, "error": err}), 500

    return jsonify({"success": True, "data": data})


@app.route("/saatlik")
def saatlik():
    il = request.args.get("il", "Antalya")
    ilce = request.args.get("ilce", "Kepez")

    ids = get_merkez_ids(il, ilce)
    if not ids or not ids.get("saatlikTahminIstNo"):
        return (
            jsonify({
                "success": False,
                "error": f"'{il}/{ilce}' için saatlik istasyon bulunamadı.",
            }),
            404,
        )

    url = (
        "https://servis.mgm.gov.tr/web/tahminler/saatlik?istno="
        + str(ids["saatlikTahminIstNo"])
    )
    data, err = safe_mgm_request(url)

    if err:
        return jsonify({"success": False, "error": err}), 500

    return jsonify({"success": True, "data": data})


@app.route("/gunluk")
def gunluk():
    il = request.args.get("il", "Antalya")
    ilce = request.args.get("ilce", "Kepez")

    ids = get_merkez_ids(il, ilce)
    if not ids or not ids.get("gunlukTahminIstNo"):
        return (
            jsonify({
                "success": False,
                "error": f"'{il}/{ilce}' için günlük istasyon bulunamadı.",
            }),
            404,
        )

    url = (
        "https://servis.mgm.gov.tr/web/tahminler/gunluk?istno="
        + str(ids["gunlukTahminIstNo"])
    )
    data, err = safe_mgm_request(url)

    if err:
        return jsonify({"success": False, "error": err}), 500

    return jsonify({"success": True, "data": data})


# BEKLENMEYEN GLOBAL HATA YAKALAYICI (Sunucunun Çökmesini Engeller)
@app.errorhandler(Exception)
def handle_global_exception(e):
    return (
        jsonify({
            "success": False,
            "error": "Sunucu içi beklenmeyen bir hata oluştu.",
            "detail": str(e),
        }),
        500,
    )


if __name__ == "__main__":
    # Render ortam portunu otomatik alır, yoksa 10000 açar
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
