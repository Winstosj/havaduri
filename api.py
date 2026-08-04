import os
import requests
from flask import Flask, jsonify, request
from flask_cors import CORS # CORS kütüphanesini içe aktarıyoruz

app = Flask(__name__)

# CORS AYARI: Bu satır sayesinde tarayıcılardan gelen tüm OPTIONS istekleri 
# otomatik onaylanır ve engelleme ortadan kalkar.
CORS(app) 

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

# MGM HADİSE KODLARI SÖZLÜĞÜ (Kod -> Türkçe Açıklama)
HADİSE_SOZLUGU = {
    "A": "Açık", "AB": "Az Bulutlu", "PB": "Parçalı Bulutlu", "CB": "Çok Bulutlu",
    "HY": "Hafif Yağmurlu", "Y": "Yağmurlu", "KY": "Kuvvetli Yağmurlu",
    "MSY": "Mevzi Sağanak Yağışlı", "DY": "Dolu", "KKY": "Karla Karışık Yağmur",
    "HKY": "Hafif Kar Yağışlı", "K": "Kar Yağışlı", "SK": "Yoğun Kar Yağışlı",
    "TSY": "Gökgürültülü Sağanak Yağışlı", "SIS": "Sisli", "PUS": "Puslu",
    "DMN": "Dumanlı", "KF": "Toz veya Kum Taşınımı", "R": "Rüzgarlı",
    "SCK": "Sıcak", "SOG": "Soğuk",
}

# GÜVENLİ İSTEK ATICI
def safe_mgm_request(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=8)
        if response.status_code != 200:
            return None, f"MGM Servis Hatası (HTTP {response.status_code})"
        try:
            data = response.json()
            return data, None
        except ValueError:
            return None, "MGM yanıtı geçersiz JSON formatında."
    except requests.exceptions.Timeout:
        return None, "MGM sunucusundan yanıt zaman aşımına uğradı (Timeout)."
    except requests.exceptions.RequestException as e:
        return None, f"Bağlantı hatası: {str(e)}"

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
@app.route("/")
def home():
    return jsonify({
        "status": "pong",
        "message": "Hava Durumu API aktif ve çalışıyor!",
        "endpoints": ["/ping", "/anlik", "/saatlik", "/gunluk"],
    }), 200

@app.route("/ping")
def ping():
    return jsonify({"status": "pong", "message": "Sistem zehir gibi ayakta!"}), 200

@app.route("/anlik")
def anlik():
    il = request.args.get("il", "Antalya")
    ilce = request.args.get("ilce", "Kepez")
    ids = get_merkez_ids(il, ilce)
    if not ids or not ids.get("merkezId"):
        return jsonify({"success": False, "error": f"'{il}/{ilce}' için merkez bilgisi çekilemedi."}), 404
        
    url = f"https://servis.mgm.gov.tr/web/sondurumlar?merkezid={ids['merkezId']}"
    data, err = safe_mgm_request(url)
    if err:
        return jsonify({"success": False, "error": err}), 500
        
    if isinstance(data, list) and len(data) > 0:
        kod = data[0].get("hadiseKodu")
        if kod:
            data[0]["hadiseAciklama"] = HADİSE_SOZLUGU.get(kod, kod)
        return jsonify({"success": True, "data": data})

@app.route("/saatlik")
def saatlik():
    il = request.args.get("il", "Antalya")
    ilce = request.args.get("ilce", "Kepez")
    ids = get_merkez_ids(il, ilce)
    if not ids or not ids.get("saatlikTahminIstNo"):
        return jsonify({"success": False, "error": f"'{il}/{ilce}' için saatlik istasyon bulunamadı."}), 404
        
    url = f"https://servis.mgm.gov.tr/web/tahminler/saatlik?istno={ids['saatlikTahminIstNo']}"
    data, err = safe_mgm_request(url)
    if err:
        return jsonify({"success": False, "error": err}), 500
        
    if isinstance(data, list) and len(data) > 0:
        tahminler = data[0].get("tahmin", [])
        for item in tahminler:
            kod = item.get("hadise")
            if kod:
                item["hadiseAciklama"] = HADİSE_SOZLUGU.get(kod, kod)
        return jsonify({"success": True, "data": data})

@app.route("/gunluk")
def gunluk():
    il = request.args.get("il", "Antalya")
    ilce = request.args.get("ilce", "Kepez")
    ids = get_merkez_ids(il, ilce)
    if not ids or not ids.get("gunlukTahminIstNo"):
        return jsonify({"success": False, "error": f"'{il}/{ilce}' için günlük istasyon bulunamadı."}), 404
        
    url = f"https://servis.mgm.gov.tr/web/tahminler/gunluk?istno={ids['gunlukTahminIstNo']}"
    data, err = safe_mgm_request(url)
    if err:
        return jsonify({"success": False, "error": err}), 500
        
    if isinstance(data, list) and len(data) > 0:
        for i in range(6):
            hadise_key = f"hadiseGun{i}"
            if hadise_key in data[0]:
                kod = data[0][hadise_key]
                data[0][f"hadiseAciklamaGun{i}"] = HADİSE_SOZLUGU.get(kod, kod)
        return jsonify({"success": True, "data": data})

# BEKLENMEYEN GLOBAL HATA YAKALAYICI
@app.errorhandler(Exception)
def handle_global_exception(e):
    return jsonify({
        "success": False,
        "error": "Sunucu içi beklenmeyen bir hata oluştu.",
        "detail": str(e),
    }), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
