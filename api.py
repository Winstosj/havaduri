<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Okul Bitme Sayacı</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
<style>
  :root{
    --bg-1:#05060a;
    --bg-2:#0b1120;
    --navy:#0f172a;
    --slate:#111827;
    --glass:rgba(255,255,255,0.05);
    --glass-border:rgba(255,255,255,0.08);
    --neon:#38bdf8;
    --neon-2:#818cf8;
    --neon-glow:rgba(56,189,248,0.45);
    --text:#e5e9f0;
    --text-dim:#8b93a7;
    --text-faint:#4b5364;
    --danger:#f87171;
    --ok:#34d399;
    --font-display:'Space Grotesk', system-ui, sans-serif;
    --font-body:'Manrope', system-ui, sans-serif;
    --font-mono:'JetBrains Mono', 'Consolas', monospace;
  }
  *{box-sizing:border-box;margin:0;padding:0;}
  html,body{height:100%;}
  @media (prefers-reduced-motion: reduce){
    *{animation-duration:0.001ms !important; animation-iteration-count:1 !important; transition-duration:0.001ms !important;}
  }
  body{
    font-family:var(--font-body);
    background:
      radial-gradient(circle at 15% 10%, rgba(56,189,248,0.10), transparent 40%),
      radial-gradient(circle at 85% 90%, rgba(129,140,248,0.12), transparent 45%),
      linear-gradient(160deg, var(--bg-1), var(--bg-2) 60%, #060a14);
    color:var(--text);
    min-height:100vh;
    padding:24px 16px 60px;
  }
  .wrap{max-width:1180px;margin:0 auto;}

  /* ===== Header & Real Time Clock ===== */
  header.top{
    display:flex;
    flex-direction:column;
    align-items:center;
    text-align:center;
    margin-bottom:32px;
    animation:fadeDown 0.7s ease both;
  }
  .real-clock{
    font-family:var(--font-mono);
    font-size:2.4rem;
    font-weight:700;
    color:#fff;
    text-shadow:0 0 22px var(--neon-glow);
    background:linear-gradient(160deg, rgba(255,255,255,0.05), rgba(255,255,255,0.01));
    border:1px solid var(--glass-border);
    padding:12px 28px;
    border-radius:40px;
    margin-bottom:18px;
    font-variant-numeric:tabular-nums;
    box-shadow:0 8px 32px rgba(0,0,0,0.2), inset 0 1px 0 rgba(255,255,255,0.04);
    display:inline-block;
  }
  header.top h1{
    font-family:var(--font-display);
    font-size:1.9rem;
    font-weight:700;
    letter-spacing:0.3px;
    background:linear-gradient(90deg,#fff 10%, var(--neon) 55%, var(--neon-2) 100%);
    -webkit-background-clip:text;
    background-clip:text;
    color:transparent;
  }
  header.top p{
    color:var(--text-dim);
    font-size:0.85rem;
    margin-top:6px;
    font-weight:500;
  }

  @keyframes fadeDown{
    from{opacity:0; transform:translateY(-14px);}
    to{opacity:1; transform:translateY(0);}
  }

  .glass{
    background:var(--glass);
    border:1px solid var(--glass-border);
    backdrop-filter:blur(18px);
    -webkit-backdrop-filter:blur(18px);
    border-radius:20px;
    box-shadow:0 8px 32px rgba(0,0,0,0.35), inset 0 1px 0 rgba(255,255,255,0.04);
  }

  /* ===== Countdown Hero ===== */
  .hero{
    padding:32px 20px 28px;
    margin-bottom:22px;
    text-align:center;
    position:relative;
    overflow:hidden;
    animation:riseIn 0.6s cubic-bezier(.2,.8,.2,1) 0.05s both;
  }
  .hero::before{
    content:"";
    position:absolute;
    inset:0;
    background:radial-gradient(circle at 50% 0%, rgba(56,189,248,0.15), transparent 60%);
    pointer-events:none;
  }
  .hero .label{
    color:var(--text-dim);
    font-size:0.8rem;
    text-transform:uppercase;
    letter-spacing:2px;
    margin-bottom:14px;
    font-weight:600;
  }
  .countdown-grid{
    display:flex;
    justify-content:center;
    gap:14px;
    flex-wrap:wrap;
  }
  .count-box{
    background:linear-gradient(160deg, rgba(255,255,255,0.06), rgba(255,255,255,0.01));
    border:1px solid var(--glass-border);
    border-radius:16px;
    padding:16px 14px;
    min-width:88px;
    flex:1 1 88px;
    max-width:150px;
    position:relative;
    transition:transform 0.35s cubic-bezier(.2,.8,.2,1), border-color 0.35s ease, box-shadow 0.35s ease;
  }
  .count-box:hover{
    transform:translateY(-3px);
    border-color:rgba(56,189,248,0.35);
    box-shadow:0 10px 26px rgba(56,189,248,0.12);
  }
  .count-box .num{
    font-family:var(--font-mono);
    font-size:2.3rem;
    font-weight:700;
    color:var(--neon);
    text-shadow:0 0 18px var(--neon-glow);
    font-variant-numeric:tabular-nums;
    line-height:1;
    display:inline-block;
  }
  .count-box .num.tick{
    animation:tickPop 0.4s cubic-bezier(.2,.9,.3,1.3);
  }
  @keyframes tickPop{
    0%{transform:translateY(-6px); opacity:0.3;}
    60%{transform:translateY(1px); opacity:1;}
    100%{transform:translateY(0); opacity:1;}
  }
  .count-box .unit{
    margin-top:8px;
    font-size:0.7rem;
    color:var(--text-dim);
    text-transform:uppercase;
    letter-spacing:1.5px;
    font-weight:600;
  }
  .count-box.days .num{color:#fff;text-shadow:0 0 22px var(--neon-glow);}

  .hero .sub-status{
    margin-top:18px;
    font-size:0.85rem;
    color:var(--text-dim);
    transition:opacity 0.4s ease;
  }
  .hero .sub-status span{
    color:var(--neon);
    font-weight:600; 
    font-family:var(--font-mono);
    font-variant-numeric: tabular-nums;
  }

  /* ===== Progress bar ===== */
  .progress-card{
    padding:22px 22px 20px;
    margin-bottom:22px;
    animation:riseIn 0.6s cubic-bezier(.2,.8,.2,1) 0.15s both;
  }
  .progress-card .row{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:14px;
    flex-wrap:wrap;
    gap:6px;
  }
  .progress-card h3{
    font-family:var(--font-display);
    font-size:0.95rem;
    color:var(--text);
    font-weight:600;
    display:flex;
    align-items:center;
    gap:8px;
  }
  .progress-card .pct{
    font-family:var(--font-mono);
    font-size:1.1rem;
    font-weight:700;
    color:var(--neon);
  }
  .bar-track{
    width:100%;
    height:14px;
    border-radius:20px;
    background:rgba(255,255,255,0.06);
    overflow:hidden;
    border:1px solid var(--glass-border);
    position:relative;
  }
  .bar-fill{
    height:100%;
    border-radius:20px;
    background:linear-gradient(90deg, var(--neon-2), var(--neon));
    box-shadow:0 0 14px var(--neon-glow);
    transition:width 1.2s cubic-bezier(.2,.8,.2,1);
    position:relative;
    width:0%;
  }
  .bar-fill::after{
    content:"";
    position:absolute;
    inset:0;
    background:linear-gradient(110deg, transparent 30%, rgba(255,255,255,0.35) 45%, transparent 60%);
    animation:shine 3.5s infinite;
  }
  @keyframes shine{
    0%{transform:translateX(-100%);}
    100%{transform:translateX(220%);}
  }
  .progress-card .foot{
    display:flex;
    justify-content:space-between;
    margin-top:8px;
    font-size:0.72rem;
    color:var(--text-faint);
    font-family:var(--font-mono);
  }

  /* ===== Weather card ===== */
  .weather-card{
    padding:0;
    margin-bottom:22px;
    overflow:hidden;
    animation:riseIn 0.6s cubic-bezier(.2,.8,.2,1) 0.2s both;
  }
  .weather-head{
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:14px;
    padding:16px 20px;
    cursor:pointer;
    flex-wrap:wrap;
    transition:background 0.25s ease;
  }
  .weather-head:hover{background:rgba(255,255,255,0.02);}
  .weather-now{
    display:flex;
    align-items:center;
    gap:12px;
  }
  .w-icon{
    line-height:1;
    filter:drop-shadow(0 0 8px rgba(56,189,248,0.3));
    display:flex;
    align-items:center;
    justify-content:center;
  }
  .w-svg{
    display:inline-flex;
    align-items:center;
    justify-content:center;
    user-select:none;
    -webkit-user-select:none;
    -webkit-touch-callout:none;
    pointer-events:none;
  }
  .w-svg svg{width:100%; height:100%; display:block; -webkit-user-drag:none;}
  .w-temp{
    font-family:var(--font-mono);
    font-size:1.6rem;
    font-weight:700;
    color:#fff;
    line-height:1.1;
  }
  .w-desc{
    font-size:0.75rem;
    color:var(--text-dim);
    margin-top:2px;
  }
  .weather-extra{
    display:flex;
    gap:14px;
    flex-wrap:wrap;
    font-size:0.72rem;
    color:var(--text-dim);
    font-family:var(--font-mono);
  }
  .w-chevron{
    color:var(--neon);
    font-size:0.75rem;
    transition:transform 0.3s ease;
  }
  .weather-card.open .w-chevron{transform:rotate(90deg);}
  .weather-detail{
    max-height:0;
    overflow:hidden;
    transition:max-height 0.4s cubic-bezier(.2,.8,.2,1), padding 0.4s ease;
    padding:0 20px;
    border-top:1px solid transparent;
  }
  .weather-card.open .weather-detail{
    max-height:340px;
    padding:4px 20px 18px;
    border-top:1px solid var(--glass-border);
  }
  .w-section-title{
    font-size:0.68rem;
    text-transform:uppercase;
    letter-spacing:1.5px;
    color:var(--text-faint);
    margin:12px 0 8px;
    font-weight:600;
  }
  .hourly-row, .daily-row{
    display:flex;
    gap:10px;
    overflow-x:auto;
    padding-bottom:4px;
  }
  .hourly-row::-webkit-scrollbar, .daily-row::-webkit-scrollbar{height:4px;}
  .hourly-row::-webkit-scrollbar-thumb, .daily-row::-webkit-scrollbar-thumb{background:rgba(255,255,255,0.12);border-radius:10px;}
  .hour-chip, .day-chip{
    flex:0 0 auto;
    background:rgba(255,255,255,0.03);
    border:1px solid var(--glass-border);
    border-radius:12px;
    padding:10px 12px;
    text-align:center;
    min-width:62px;
  }
  .hour-chip .h-time, .day-chip .d-day{
    font-size:0.65rem;
    color:var(--text-dim);
    font-family:var(--font-mono);
  }
  .hour-chip .h-icon, .day-chip .d-icon{
    margin:5px 0;
    display:flex;
    align-items:center;
    justify-content:center;
  }
  .hour-chip .h-temp{
    font-size:0.8rem;
    font-weight:700;
    color:var(--neon);
    font-family:var(--font-mono);
  }
  .day-chip .d-temp{
    font-size:0.72rem;
    font-family:var(--font-mono);
    color:var(--text);
  }
  .day-chip .d-temp .d-max{color:#fff; font-weight:700;}
  .day-chip .d-temp .d-min{color:var(--text-dim);}
  .w-loc{
    margin-top:12px;
    font-size:0.68rem;
    color:var(--text-faint);
    text-align:right;
  }
  .w-error{
    font-size:0.75rem;
    color:var(--text-dim);
    padding:4px 0;
  }

  /* ===== Grid layout ===== */
  .grid{
    display:grid;
    grid-template-columns:1.4fr 1fr;
    gap:20px;
  }
  @media(max-width:860px){
    .grid{grid-template-columns:1fr;}
  }
  .grid > div .card:first-child{ animation-delay:0.32s; }

  @keyframes riseIn{
    from{opacity:0; transform:translateY(16px);}
    to{opacity:1; transform:translateY(0);}
  }

  .card{padding:20px 20px 22px; transition:border-color 0.35s ease, box-shadow 0.35s ease; animation:riseIn 0.6s cubic-bezier(.2,.8,.2,1) 0.25s both;}
  .card:hover{
    border-color:rgba(56,189,248,0.18);
  }
  .card h3{
    font-family:var(--font-display);
    font-size:0.95rem;
    font-weight:600;
    margin-bottom:14px;
    display:flex;
    align-items:center;
    gap:8px;
  }
  .card h3 .dot{
    width:8px;height:8px;border-radius:50%;
    background:var(--neon);
    box-shadow:0 0 8px var(--neon-glow);
  }

  /* Calendar strike-through log */
  .day-log{
    display:grid;
    grid-template-columns:repeat(7,1fr);
    gap:5px;
    max-height:230px;
    overflow-y:auto;
    padding-right:4px;
  }
  .day-log::-webkit-scrollbar{width:5px;}
  .day-log::-webkit-scrollbar-thumb{background:rgba(255,255,255,0.12);border-radius:10px;}
  .day-cell{
    aspect-ratio:1;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:0.62rem;
    font-family:var(--font-mono);
    border-radius:6px;
    position:relative;
    background:rgba(255,255,255,0.02);
    border:1px solid rgba(255,255,255,0.04);
    color:var(--text-faint);
    transition:transform 0.2s ease, border-color 0.2s ease;
  }
  .day-cell:hover{
    transform:scale(1.15);
    border-color:rgba(56,189,248,0.4);
    z-index:2;
  }
  .day-cell.past{
    color:rgba(139,147,167,0.35);
    text-decoration:line-through;
    text-decoration-color:rgba(248,113,113,0.4);
  }
  .day-cell.weekend.past{ text-decoration-color:rgba(139,147,167,0.25); }
  .day-cell.holiday.past{ text-decoration-color:rgba(52,211,153,0.35); }
  .day-cell.today{
    background:linear-gradient(160deg, var(--neon-2), var(--neon));
    color:#fff;
    font-weight:700;
    box-shadow:0 0 12px var(--neon-glow);
    text-decoration:none;
  }
  .day-cell.future{
    color:var(--text);
    border-color:rgba(255,255,255,0.07);
  }
  .day-cell.weekend.future{ color:var(--neon-2); }
  .day-cell.holiday.future{ color:var(--ok); }

  .legend{
    display:flex;
    gap:14px;
    flex-wrap:wrap;
    margin-top:12px;
    font-size:0.68rem;
    color:var(--text-dim);
  }
  .legend span{display:flex;align-items:center;gap:5px;}
  .legend i{width:9px;height:9px;border-radius:3px;display:inline-block;}

  /* Stat boxes */
  .stat-row{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:12px;
    margin-bottom:18px;
  }
  .stat-box{
    background:rgba(255,255,255,0.03);
    border:1px solid var(--glass-border);
    border-radius:14px;
    padding:14px;
    text-align:center;
    transition:transform 0.3s ease, border-color 0.3s ease;
  }
  .stat-box:hover{
    transform:translateY(-2px);
    border-color:rgba(56,189,248,0.3);
  }
  .stat-box .val{
    font-family:var(--font-mono);
    font-size:1.5rem;
    font-weight:700;
  }
  .stat-box.school .val{color:var(--neon);}
  .stat-box.holiday .val{color:var(--ok);}
  .stat-box .lbl{
    font-size:0.65rem;
    color:var(--text-dim);
    text-transform:uppercase;
    letter-spacing:1px;
    margin-top:4px;
  }

  /* Holiday list */
  .holiday-list{
    max-height:280px;
    overflow-y:auto;
    display:flex;
    flex-direction:column;
    gap:8px;
    padding-right:4px;
  }
  .holiday-list::-webkit-scrollbar{width:5px;}
  .holiday-list::-webkit-scrollbar-thumb{background:rgba(255,255,255,0.12);border-radius:10px;}
  .holiday-wrap{
    border-radius:10px;
    overflow:hidden;
    flex-shrink: 0;
  }
  .holiday-item{
    display:flex;
    justify-content:space-between;
    align-items:center;
    background:rgba(255,255,255,0.03);
    border:1px solid var(--glass-border);
    border-radius:10px;
    transition:border-color 0.25s ease, transform 0.25s ease, background 0.25s ease;
    padding:12px 14px; 
    font-size:0.78rem;
    cursor:pointer;
    user-select:none;
    min-height:44px;
    line-height: 1.4;
  }
  .holiday-item .name{color:var(--text); display:flex; align-items:center; gap:6px;}
  .holiday-item .name::before{
    content:"▸";
    font-size:0.65rem;
    color:var(--neon);
    transition:transform 0.3s ease;
    display:inline-block;
  }
  .holiday-wrap.open .holiday-item .name::before{
    transform:rotate(90deg);
  }
  .holiday-item:hover{border-color:rgba(56,189,248,0.25); transform:translateX(2px);}
  .holiday-wrap.open .holiday-item{
    border-color:rgba(56,189,248,0.35);
    background:rgba(56,189,248,0.06);
    border-bottom-left-radius:0;
    border-bottom-right-radius:0;
  }
  .holiday-item .date{color:var(--text-dim);font-size:0.7rem;white-space:nowrap;margin-left:10px; font-family:var(--font-mono);}
  .holiday-item.passed{opacity:0.55;}
  .holiday-item.passed .name{text-decoration:line-through; opacity:0.6;}

  .holiday-detail{
    max-height:0;
    overflow:hidden;
    background:rgba(56,189,248,0.04);
    border:1px solid var(--glass-border);
    border-top:none;
    border-bottom-left-radius:10px;
    border-bottom-right-radius:10px;
    transition:max-height 0.35s cubic-bezier(.2,.8,.2,1), padding 0.35s ease;
    padding:0 12px;
    font-size:0.72rem;
  }
  .holiday-wrap.open .holiday-detail{
    max-height:120px;
    padding:10px 12px 12px;
    border-color:rgba(56,189,248,0.35);
  }
  .hd-row{
    display:flex;
    justify-content:space-between;
    padding:3px 0;
    color:var(--text-dim);
  }
  .hd-row .hd-val{
    color:var(--neon);
    font-family:var(--font-mono);
    font-weight:600;
  }
  .hd-note{
    margin-top:6px;
    padding-top:6px;
    border-top:1px dashed var(--glass-border);
    color:var(--text-faint);
    font-style:italic;
    line-height:1.4;
  }


  footer{
    text-align:center;
    margin-top:30px;
    color:var(--text-faint);
    font-size:0.72rem;
  }

  @media(max-width:480px){
    .count-box .num{font-size:1.7rem;}
    .count-box{min-width:70px;padding:12px 8px;}
    header.top h1{font-size:1.3rem;}
    .real-clock { font-size: 1.8rem; padding: 10px 22px; }
  }
</style>
</head>
<body>
<div class="wrap">

  <header class="top">
    <!-- YENİ GERÇEK SAAT BURADA -->
    <div class="real-clock" id="top-clock">--:--:--</div>
    <h1>Okul Sayacı</h1>
    <p>2026 – 2027 Eğitim Öğretim Yılı</p>
  </header>

  <!-- START COUNTDOWN (sadece okul başlamadan önce görünür) -->
  <section class="hero glass" id="start-hero" style="display:none;">
    <div class="label">Okulun Başlamasına Kalan Süre</div>
    <div class="countdown-grid">
      <div class="count-box days"><div class="num" id="sd-days">--</div><div class="unit">Gün</div></div>
      <div class="count-box"><div class="num" id="sd-hours">--</div><div class="unit">Saat</div></div>
      <div class="count-box"><div class="num" id="sd-mins">--</div><div class="unit">Dakika</div></div>
      <div class="count-box"><div class="num" id="sd-secs">--</div><div class="unit">Saniye</div></div>
    </div>
    <div class="sub-status">14 Eylül 2026 Pazartesi'yi bekliyoruz 🎒</div>
  </section>

  <!-- HERO COUNTDOWN (okulun bitişine) -->
  <section class="hero glass" id="end-hero">
    <div class="label">Okulun Bitmesine Kalan Süre</div>
    <div class="countdown-grid">
      <div class="count-box days"><div class="num" id="cd-days">--</div><div class="unit">Gün</div></div>
      <div class="count-box"><div class="num" id="cd-hours">--</div><div class="unit">Saat</div></div>
      <div class="count-box"><div class="num" id="cd-mins">--</div><div class="unit">Dakika</div></div>
      <div class="count-box"><div class="num" id="cd-secs">--</div><div class="unit">Saniye</div></div>
    </div>
    <div class="sub-status" id="sub-status">Yükleniyor...</div>
  </section>

  <!-- PROGRESS -->
  <section class="progress-card glass">
    <div class="row">
      <h3>
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="var(--neon)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="filter: drop-shadow(0 0 6px var(--neon-glow));">
          <line x1="18" y1="20" x2="18" y2="10"></line>
          <line x1="12" y1="20" x2="12" y2="4"></line>
          <line x1="6" y1="20" x2="6" y2="14"></line>
        </svg>
        Eğitim Öğretim Yılı İlerlemesi
      </h3>
      <div class="pct" id="progress-pct">0%</div>
    </div>
    <div class="bar-track">
      <div class="bar-fill" id="progress-fill" style="width:0%"></div>
    </div>
    <div class="foot">
      <span id="progress-start">14 Eylül 2026</span>
      <span id="progress-end">25 Haziran 2027</span>
    </div>
  </section>

  <!-- WEATHER -->
  <section class="card glass weather-card" id="weather-card">
    <div class="weather-head" id="weather-toggle" role="button" tabindex="0" aria-expanded="false">
      <div class="weather-now">
        <span class="w-icon" id="w-icon">⛅</span>
        <div class="w-main">
          <div class="w-temp" id="w-temp">--°</div>
          <div class="w-desc" id="w-desc">Yükleniyor...</div>
        </div>
      </div>
      <div class="weather-extra">
        <span id="w-feels">His: --°</span>
        <span id="w-hum">Nem: --%</span>
        <span id="w-wind">Rüzgar: -- km/s</span>
      </div>
      <span class="w-chevron">▸</span>
    </div>
    <div class="weather-detail" id="weather-detail">
      <div class="w-section-title">Bugün Saatlik</div>
      <div class="hourly-row" id="hourly-row"></div>
      <div class="w-section-title">6 Günlük</div>
      <div class="daily-row" id="daily-row"></div>
      <div class="w-loc">📍 Kepez, Antalya</div>
    </div>
  </section>

  <div class="grid">
    <!-- CALENDAR STRIKE LOG -->
    <section class="card glass">
      <h3><span class="dot"></span> Gün Geçmişi (Çizgili Takvim)</h3>
      <div class="day-log" id="day-log"></div>
      <div class="legend">
        <span><i style="background:rgba(139,147,167,0.4)"></i> Geçen gün</span>
        <span><i style="background:var(--neon)"></i> Bugün</span>
        <span><i style="background:var(--text)"></i> Gelecek (ders)</span>
        <span><i style="background:var(--neon-2)"></i> Hafta sonu</span>
        <span><i style="background:var(--ok)"></i> Resmi/Sömestr tatili</span>
      </div>
    </section>

    <!-- SIDEBAR -->
    <div>
      <section class="card glass">
        <h3><span class="dot"></span> İstatistikler</h3>
        <div class="stat-row">
          <div class="stat-box school">
            <div class="val" id="stat-school">--</div>
            <div class="lbl">Kalan Ders Günü</div>
          </div>
          <div class="stat-box holiday">
            <div class="val" id="stat-holiday">--</div>
            <div class="lbl">Kalan Tatil Günü</div>
          </div>
        </div>
        <h3 style="margin-top:4px;"><span class="dot"></span> Tatil / Ara Tatil Listesi</h3>
        <div class="holiday-list" id="holiday-list"></div>
      </section>
    </div>
  </div>


  <footer>Okul 14 Eylül 08:00'da başlar, 25 Haziran 16:00'da biter · Gün sayacı her gün 10:00'da güncellenir (TR saati) · MEB 2026-2027 Takvimi baz alınmıştır</footer>
</div>

<script>
/* ============ CONFIG ============ */
const SCHOOL_START = new Date('2026-09-14T08:00:00+03:00'); 
const SCHOOL_END   = new Date('2027-06-25T16:00:00+03:00'); 

const HOLIDAYS = [
  { name: "Cumhuriyet Bayramı Arifesi", start: "2026-10-28", end: "2026-10-28", note: "Öğleden sonra tatil" },
  { name: "Cumhuriyet Bayramı", start: "2026-10-29", end: "2026-10-29", note: "Resmi tatil" },
  { name: "1. Dönem Ara Tatili", start: "2026-11-16", end: "2026-11-20", note: "Ara tatil (hafta sonlarıyla birlikte 9 gün)" },
  { name: "Yılbaşı Tatili", start: "2027-01-01", end: "2027-01-01", note: "Resmi tatil" },
  { name: "Yarıyıl (Sömestr) Tatili", start: "2027-01-25", end: "2027-02-05", note: "2 haftalık dönem arası tatili" },
  { name: "2. Dönem Ara Tatili", start: "2027-03-08", end: "2027-03-12", note: "Ramazan Bayramı ile birleşik ara tatil" },
  { name: "Ulusal Egemenlik ve Çocuk Bayramı", start: "2027-04-23", end: "2027-04-23", note: "Resmi tatil" },
  { name: "İşçi Bayramı", start: "2027-05-01", end: "2027-05-01", note: "Resmi tatil (Cumartesi)" },
  { name: "Kurban Bayramı Arifesi", start: "2027-05-15", end: "2027-05-15", note: "Öğleden sonra tatil (Cumartesi)" },
  { name: "Kurban Bayramı", start: "2027-05-16", end: "2027-05-19", note: "4 gün, son günü 19 Mayıs'a denk geliyor" },
  { name: "Atatürk'ü Anma, Gençlik ve Spor Bayramı", start: "2027-05-19", end: "2027-05-19", note: "Kurban Bayramı'nın 4. günüyle aynı tarihte" },
];

/* ============ HELPERS ============ */
function toTRDateOnly(d){
  const trStr = d.toLocaleString('en-CA', { timeZone: 'Europe/Istanbul', year:'numeric', month:'2-digit', day:'2-digit' });
  return trStr; 
}
function dateFromYMD(ymd){
  const [y,m,d] = ymd.split('-').map(Number);
  return new Date(Date.UTC(y, m-1, d));
}
function addDays(date, n){
  const d = new Date(date);
  d.setUTCDate(d.getUTCDate()+n);
  return d;
}
function isWeekend(date){
  const day = date.getUTCDay();
  return day === 0 || day === 6;
}
function isHoliday(ymd){
  return HOLIDAYS.find(h => ymd >= h.start && ymd <= h.end);
}

/* ============ REAL-TIME CLOCK ============ */
function updateTopClock() {
  const now = new Date();
  const trNowStr = now.toLocaleString('en-US', { timeZone:'Europe/Istanbul', hour12:false });
  const trNow = new Date(trNowStr);
  
  const hh = String(trNow.getHours()).padStart(2, '0');
  const mm = String(trNow.getMinutes()).padStart(2, '0');
  const ss = String(trNow.getSeconds()).padStart(2, '0');
  
  const clockEl = document.getElementById('top-clock');
  if(clockEl) {
    clockEl.textContent = `${hh}:${mm}:${ss}`;
  }
}

/* ============ COUNTDOWN logic ============ */
function getEffectiveTargetDiff(){
  const now = new Date();
  const trNowStr = now.toLocaleString('en-US', { timeZone:'Europe/Istanbul', hour12:false });
  const trNow = new Date(trNowStr);

  const diffMs = SCHOOL_END.getTime() - now.getTime();
  if (diffMs <= 0) return null;

  let totalSeconds = Math.floor(diffMs/1000);
  let days = Math.floor(totalSeconds / 86400);
  let remainder = totalSeconds % 86400;

  const shiftMs = 10*3600*1000; 
  const shiftedNow = now.getTime() + shiftMs; 
  const shiftedDiff = SCHOOL_END.getTime() - shiftedNow;
  if (shiftedDiff <= 0){
    days = 0;
  } else {
    days = Math.floor(shiftedDiff/(1000*3600*24));
  }

  const h = Math.floor(remainder/3600);
  const m = Math.floor((remainder%3600)/60);
  const s = remainder%60;

  return { days, hours:h, minutes:m, seconds:s, totalMs: diffMs };
}

function setNumWithTick(id, value){
  const el = document.getElementById(id);
  if (!el) return;
  const newText = String(value);
  if (el.textContent !== newText){
    el.textContent = newText;
    el.classList.remove('tick');
    void el.offsetWidth; 
    el.classList.add('tick');
  }
}

function updateStartCountdown(){
  const now = new Date();
  const diffMs = SCHOOL_START.getTime() - now.getTime();
  if (diffMs <= 0) return;
  let totalSeconds = Math.floor(diffMs/1000);
  const days = Math.floor(totalSeconds/86400);
  const h = Math.floor((totalSeconds%86400)/3600);
  const m = Math.floor((totalSeconds%3600)/60);
  const s = totalSeconds%60;
  setNumWithTick('sd-days', days);
  setNumWithTick('sd-hours', String(h).padStart(2,'0'));
  setNumWithTick('sd-mins', String(m).padStart(2,'0'));
  setNumWithTick('sd-secs', String(s).padStart(2,'0'));
}

function updateCountdown(){
  const now = new Date();
  const started = now >= SCHOOL_START;

  const startHero = document.getElementById('start-hero');
  const endHero = document.getElementById('end-hero');
  if (!started){
    startHero.style.display = 'block';
    endHero.style.display = 'none';
    updateStartCountdown();
    return;
  } else {
    startHero.style.display = 'none';
    endHero.style.display = 'block';
  }

  const result = getEffectiveTargetDiff();

  if (result === null){
    document.getElementById('cd-days').textContent = "0";
    document.getElementById('cd-hours').textContent = "00";
    document.getElementById('cd-mins').textContent = "00";
    document.getElementById('cd-secs').textContent = "00";
    document.getElementById('sub-status').textContent = "🎉 Okul bitti! 25 Haziran saat 16:00'da tatil başladı — iyi tatiller!";
    return;
  }

  document.getElementById('cd-days').textContent = result.days;
  setNumWithTick('cd-hours', String(result.hours).padStart(2,'0'));
  setNumWithTick('cd-mins', String(result.minutes).padStart(2,'0'));
  setNumWithTick('cd-secs', String(result.seconds).padStart(2,'0'));

  if (started){
    const trNowStr = now.toLocaleString('en-US', { timeZone:'Europe/Istanbul', hour12:false });
    const trNow = new Date(trNowStr);
    const hh = String(trNow.getHours()).padStart(2,'0');
    const mm = String(trNow.getMinutes()).padStart(2,'0');
    const ss = String(trNow.getSeconds()).padStart(2,'0'); 
    document.getElementById('sub-status').innerHTML = `Türkiye saati: <span>${hh}:${mm}:${ss}</span> · Gün sayacı her gün 10:00'da güncellenir`;
  }
}

// Ortak Interval başlatıcı
updateTopClock();
updateCountdown();
setInterval(() => {
  updateTopClock();
  updateCountdown();
}, 1000);

/* ============ PROGRESS BAR ============ */
function updateProgress(){
  const now = new Date();
  const total = SCHOOL_END - SCHOOL_START;
  const elapsed = now - SCHOOL_START;
  let pct = (elapsed/total)*100;
  pct = Math.max(0, Math.min(100, pct));
  document.getElementById('progress-fill').style.width = pct.toFixed(2)+'%';
  document.getElementById('progress-pct').textContent = pct.toFixed(1)+'%';
}
requestAnimationFrame(()=> requestAnimationFrame(updateProgress));
setInterval(updateProgress, 60000);

/* ============ CALENDAR STRIKE LOG ============ */
function buildDayLog(){
  const container = document.getElementById('day-log');
  container.innerHTML = '';
  const start = dateFromYMD(toTRDateOnly(SCHOOL_START));
  const end = dateFromYMD(toTRDateOnly(SCHOOL_END));
  const todayYMD = toTRDateOnly(new Date());

  let d = new Date(start);
  const frag = document.createDocumentFragment();
  while (d <= end){
    const ymd = d.toISOString().slice(0,10);
    const cell = document.createElement('div');
    cell.className = 'day-cell';
    const weekend = isWeekend(d);
    const hol = isHoliday(ymd);

    if (weekend) cell.classList.add('weekend');
    if (hol) cell.classList.add('holiday');

    if (ymd < todayYMD) cell.classList.add('past');
    else if (ymd === todayYMD) cell.classList.add('today');
    else cell.classList.add('future');

    cell.textContent = d.getUTCDate();
    cell.title = ymd + (hol ? ` — ${hol.name}` : weekend ? ' — Hafta sonu' : '');
    frag.appendChild(cell);
    d = addDays(d,1);
  }
  container.appendChild(frag);
}
buildDayLog();

/* ============ STATS ============ */
function updateStats(){
  const now = new Date();
  const todayYMD = toTRDateOnly(now);
  const end = dateFromYMD(toTRDateOnly(SCHOOL_END));
  let d = dateFromYMD(todayYMD);
  let schoolDays = 0, holidayDays = 0;
  while (d <= end){
    const ymd = d.toISOString().slice(0,10);
    if (isWeekend(d) || isHoliday(ymd)) holidayDays++;
    else schoolDays++;
    d = addDays(d,1);
  }
  document.getElementById('stat-school').textContent = schoolDays;
  document.getElementById('stat-holiday').textContent = holidayDays;
}
updateStats();

/* ============ HOLIDAY LIST ============ */
function daysUntil(ymd){
  const now = new Date();
  const todayYMD = toTRDateOnly(now);
  const target = dateFromYMD(ymd);
  const today = dateFromYMD(todayYMD);
  const diff = Math.round((target - today) / (1000*3600*24));
  return diff;
}

function buildHolidayList(){
  const list = document.getElementById('holiday-list');
  list.innerHTML = '';
  const todayYMD = toTRDateOnly(new Date());
  const monthsTR = ["Oca","Şub","Mar","Nis","May","Haz","Tem","Ağu","Eyl","Eki","Kas","Ara"];

  HOLIDAYS.forEach((h, idx)=>{
    const wrap = document.createElement('div');
    wrap.className = 'holiday-wrap';

    const item = document.createElement('div');
    item.className = 'holiday-item';
    const isPassed = h.end < todayYMD;
    if (isPassed) item.classList.add('passed');
    item.setAttribute('role','button');
    item.setAttribute('tabindex','0');
    item.setAttribute('aria-expanded','false');

    const sName = document.createElement('span');
    sName.className = 'name';
    sName.textContent = h.name;

    const sDate = document.createElement('span');
    sDate.className = 'date';
    const [sy,sm,sd] = h.start.split('-');
    const [ey,em,ed] = h.end.split('-');
    if (h.start === h.end){
      sDate.textContent = `${parseInt(sd)} ${monthsTR[parseInt(sm)-1]}`;
    } else {
      sDate.textContent = `${parseInt(sd)} ${monthsTR[parseInt(sm)-1]} – ${parseInt(ed)} ${monthsTR[parseInt(em)-1]}`;
    }

    item.appendChild(sName);
    item.appendChild(sDate);

    // Detay paneli
    const detail = document.createElement('div');
    detail.className = 'holiday-detail';
    const daysLeft = daysUntil(h.start);
    let daysText;
    if (isPassed){
      daysText = `Bu tatil geçti.`;
    } else if (daysLeft === 0){
      daysText = `Bugün başlıyor! 🎉`;
    } else if (daysLeft < 0){
      daysText = `Şu an devam ediyor.`;
    } else {
      daysText = `Başlamasına ${daysLeft} gün kaldı.`;
    }
    const totalDays = Math.round((dateFromYMD(h.end) - dateFromYMD(h.start))/(1000*3600*24)) + 1;
    detail.innerHTML = `
      <div class="hd-row"><span class="hd-lbl">Süre</span><span class="hd-val">${totalDays} gün</span></div>
      <div class="hd-row"><span class="hd-lbl">Durum</span><span class="hd-val">${daysText}</span></div>
      ${h.note ? `<div class="hd-note">${h.note}</div>` : ''}
    `;

    item.addEventListener('click', ()=>{
      const isOpen = wrap.classList.toggle('open');
      item.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
    item.addEventListener('keydown', (e)=>{
      if (e.key === 'Enter' || e.key === ' '){
        e.preventDefault();
        item.click();
      }
    });

    wrap.appendChild(item);
    wrap.appendChild(detail);
    list.appendChild(wrap);
  });
}
buildHolidayList();

/* ============ WEATHER ============ */
const WEATHER_BASE = 'https://havadurumuapi-fni3.onrender.com';
const WEATHER_CACHE_PREFIX = 'okulSayaci_weather_';
const WEATHER_REFRESH_MS = 10*60*1000; 

const WEATHER_SVG = {
  sun: `<svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="4.6" fill="#fbbf24"/><g stroke="#fbbf24" stroke-width="1.8" stroke-linecap="round"><path d="M12 2v2.6"/><path d="M12 19.4V22"/><path d="M4.2 4.2l1.8 1.8"/><path d="M18 18l1.8 1.8"/><path d="M2 12h2.6"/><path d="M19.4 12H22"/><path d="M4.2 19.8l1.8-1.8"/><path d="M18 6l1.8-1.8"/></g></svg>`,
  partly: `<svg viewBox="0 0 24 24" fill="none"><circle cx="9" cy="9" r="3.6" fill="#fbbf24"/><path d="M6 18a4.5 4.5 0 01.7-8.94A5.5 5.5 0 0117 11.2 4 4 0 0116.5 18H6z" fill="#94a3b8"/></svg>`,
  cloud: `<svg viewBox="0 0 24 24" fill="none"><path d="M6.5 18a4.5 4.5 0 01.4-8.98A6 6 0 0118.6 11 4.2 4.2 0 0118 19H6.7A4.5 4.5 0 016.5 18z" fill="#94a3b8"/></svg>`,
  rain: `<svg viewBox="0 0 24 24" fill="none"><path d="M6.5 15a4.5 4.5 0 01.4-8.98A6 6 0 0118.6 8 4.2 4.2 0 0118 16H6.7A4.5 4.5 0 016.5 15z" fill="#94a3b8"/><g stroke="#38bdf8" stroke-width="1.8" stroke-linecap="round"><path d="M8 18.5l-1 2.5"/><path d="M12.5 18.5l-1 2.5"/><path d="M17 18.5l-1 2.5"/></g></svg>`,
  snow: `<svg viewBox="0 0 24 24" fill="none"><path d="M6.5 15a4.5 4.5 0 01.4-8.98A6 6 0 0118.6 8 4.2 4.2 0 0118 16H6.7A4.5 4.5 0 016.5 15z" fill="#94a3b8"/><g stroke="#e5e9f0" stroke-width="1.6" stroke-linecap="round"><path d="M8 18v4"/><path d="M6.3 19l3.4 2"/><path d="M9.7 19l-3.4 2"/><path d="M16 18v4"/><path d="M14.3 19l3.4 2"/><path d="M17.7 19l-3.4 2"/></g></svg>`,
  fog: `<svg viewBox="0 0 24 24" fill="none"><g stroke="#94a3b8" stroke-width="1.8" stroke-linecap="round"><path d="M4 9h16"/><path d="M3 13h18"/><path d="M5 17h14"/></g></svg>`,
  storm: `<svg viewBox="0 0 24 24" fill="none"><path d="M6.5 13a4.5 4.5 0 01.4-8.98A6 6 0 0118.6 6 4.2 4.2 0 0118 14H6.7A4.5 4.5 0 016.5 13z" fill="#94a3b8"/><path d="M13 13l-3 5h2.4L11 22l4.5-6h-2.6L13 13z" fill="#fbbf24"/></svg>`,
  hot: `<svg viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="5.6" fill="#f87171"/><g stroke="#f87171" stroke-width="1.8" stroke-linecap="round"><path d="M12 1.6v2.6"/><path d="M12 19.8v2.6"/><path d="M3.8 4l1.8 1.8"/><path d="M18.4 18.2l1.8 1.8"/><path d="M1.6 12h2.6"/><path d="M19.8 12h2.6"/><path d="M3.8 20l1.8-1.8"/><path d="M18.4 5.8l1.8-1.8"/></g></svg>`,
  warn: `<svg viewBox="0 0 24 24" fill="none"><path d="M12 3.5 22 20H2z" fill="none" stroke="#f87171" stroke-width="1.8" stroke-linejoin="round"/><path d="M12 9.5v5" stroke="#f87171" stroke-width="1.8" stroke-linecap="round"/><circle cx="12" cy="17.4" r="1" fill="#f87171"/></svg>`
};
function weatherIconKey(code, desc){
  const d = (desc || '').toLowerCase();
  if (code === 'SCK' || d.includes('sıcak')) return 'hot';
  if (code === 'A' || d.includes('açık')) return 'sun';
  if (code === 'AZ' || code === 'PB' || d.includes('parçalı') || d.includes('az bulutlu')) return 'partly';
  if (code === 'CB' || code === 'B' || d.includes('bulut') || d.includes('kapalı')) return 'cloud';
  if (['HY','HSY','RY'].includes(code) || d.includes('yağmur') || d.includes('sağanak')) return 'rain';
  if (['KY','KKY','SGK'].includes(code) || d.includes('kar')) return 'snow';
  if (code === 'SIS' || code === 'PUS' || d.includes('sis') || d.includes('pus')) return 'fog';
  if (code === 'GK' || d.includes('fırtına') || d.includes('gökgürültü')) return 'storm';
  return 'partly';
}
function weatherIconHTML(code, desc, size){
  const key = weatherIconKey(code, desc);
  const svg = WEATHER_SVG[key] || WEATHER_SVG.partly;
  const s = size || 22;
  return `<span class="w-svg" style="width:${s}px;height:${s}px" draggable="false">${svg}</span>`;
}
function weatherErrorIconHTML(size){
  const s = size || 22;
  return `<span class="w-svg" style="width:${s}px;height:${s}px" draggable="false">${WEATHER_SVG.warn}</span>`;
}

function weatherCacheGet(key){
  try{
    const raw = localStorage.getItem(WEATHER_CACHE_PREFIX + key);
    if (!raw) return null;
    return JSON.parse(raw);
  } catch(e){ return null; }
}
function weatherCacheSet(key, value){
  try{
    localStorage.setItem(WEATHER_CACHE_PREFIX + key, JSON.stringify({ data: value, savedAt: Date.now() }));
  } catch(e){ }
}

async function fetchJSON(url) {
  const res = await fetch(url, {
    method: 'GET',
    headers: {
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
      'accept-language': 'tr-TR,tr;q=0.9',
      'cache-control': 'no-cache',
      'pragma': 'no-cache'
    }
  });
  if (!res.ok) throw new Error('HTTP ' + res.status);
  const json = await res.json();
  if (!json.success || !json.data || !json.data.length) throw new Error('Boş veri');
  return json.data;
}

function renderWeatherNow(d){
  document.getElementById('w-icon').innerHTML = weatherIconHTML(d.hadiseKodu, d.hadiseAciklama, 34);
  document.getElementById('w-temp').textContent = Math.round(d.sicaklik) + '°';
  document.getElementById('w-desc').textContent = d.hadiseAciklama || '—';
  document.getElementById('w-feels').textContent = `His: ${Math.round(d.hissedilenSicaklik)}°`;
  document.getElementById('w-hum').textContent = `Nem: ${d.nem >= 0 ? d.nem : '--'}%`;
  document.getElementById('w-wind').textContent = `Rüzgar: ${d.ruzgarHiz >= 0 ? d.ruzgarHiz : '--'} km/s`;
}
function renderWeatherNowError(){
  document.getElementById('w-desc').textContent = 'Hava durumu alınamadı';
  document.getElementById('w-icon').innerHTML = weatherErrorIconHTML(34);
}

function renderWeatherHourly(tahmin){
  const row = document.getElementById('hourly-row');
  row.innerHTML = '';
  tahmin.forEach(t=>{
    const dt = new Date(t.tarih);
    const trHour = dt.toLocaleString('tr-TR', { timeZone:'Europe/Istanbul', hour:'2-digit', minute:'2-digit', hour12:false });
    const chip = document.createElement('div');
    chip.className = 'hour-chip';
    chip.innerHTML = `
      <div class="h-time">${trHour}</div>
      <div class="h-icon">${weatherIconHTML(t.hadise, t.hadiseAciklama, 22)}</div>
      <div class="h-temp">${Math.round(t.sicaklik)}°</div>
    `;
    row.appendChild(chip);
  });
}
function renderWeatherHourlyError(){
  document.getElementById('hourly-row').innerHTML = '<div class="w-error">Saatlik tahmin alınamadı</div>';
}

function renderWeatherDaily(d){
  const row = document.getElementById('daily-row');
  const dayNamesTR = ['Paz','Pzt','Sal','Çar','Per','Cum','Cmt'];
  row.innerHTML = '';
  for (let i=0; i<=5; i++){
    const tarih = d[`tarihGun${i}`];
    const max = d[`enYuksekGun${i}`];
    const min = d[`enDusukGun${i}`];
    const hadiseKodu = d[`hadiseGun${i}`];
    const hadiseAciklama = d[`hadiseAciklamaGun${i}`];
    if (tarih === undefined) continue;
    const dt = new Date(tarih);
    const trDayName = dayNamesTR[ new Date(dt.toLocaleString('en-US', {timeZone:'Europe/Istanbul'})).getDay() ];
    const chip = document.createElement('div');
    chip.className = 'day-chip';
    chip.innerHTML = `
      <div class="d-day">${i===0 ? 'Bugün' : trDayName}</div>
      <div class="d-icon">${weatherIconHTML(hadiseKodu, hadiseAciklama, 20)}</div>
      <div class="d-temp"><span class="d-max">${max}°</span> / <span class="d-min">${min}°</span></div>
    `;
    row.appendChild(chip);
  }
}
function renderWeatherDailyError(){
  document.getElementById('daily-row').innerHTML = '<div class="w-error">6 günlük tahmin alınamadı</div>';
}

async function loadWeatherNow(){
  const cached = weatherCacheGet('anlik');
  if (cached && cached.data){
    try{ renderWeatherNow(cached.data); } catch(e){}
  }
  try{
    const data = await fetchJSON(WEATHER_BASE + '/anlik');
    const d = data[0];
    renderWeatherNow(d);
    weatherCacheSet('anlik', d);
  } catch(err){
    if (!cached) renderWeatherNowError();
  }
}

async function loadWeatherHourly(){
  const cached = weatherCacheGet('saatlik');
  if (cached && cached.data){
    try{ renderWeatherHourly(cached.data); } catch(e){}
  }
  try{
    const data = await fetchJSON(WEATHER_BASE + '/saatlik');
    const tahmin = data[0].tahmin || [];
    renderWeatherHourly(tahmin);
    weatherCacheSet('saatlik', tahmin);
  } catch(err){
    if (!cached) renderWeatherHourlyError();
  }
}

async function loadWeatherDaily(){
  const cached = weatherCacheGet('gunluk');
  if (cached && cached.data){
    try{ renderWeatherDaily(cached.data); } catch(e){}
  }
  try{
    const data = await fetchJSON(WEATHER_BASE + '/gunluk');
    const d = data[0];
    renderWeatherDaily(d);
    weatherCacheSet('gunluk', d);
  } catch(err){
    if (!cached) renderWeatherDailyError();
  }
}

function initWeather(){
  loadWeatherNow();
  const card = document.getElementById('weather-card');
  const toggle = document.getElementById('weather-toggle');
  let detailLoaded = false;

  card.addEventListener('contextmenu', (e)=>{
    if (e.target.closest('.w-svg')) e.preventDefault();
  });

  function openWeather(){
    const isOpen = card.classList.toggle('open');
    toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    if (isOpen && !detailLoaded){
      detailLoaded = true;
      loadWeatherHourly();
      loadWeatherDaily();
    }
  }
  toggle.addEventListener('click', openWeather);
  toggle.addEventListener('keydown', (e)=>{
    if (e.key === 'Enter' || e.key === ' '){
      e.preventDefault();
      openWeather();
    }
  });

  setInterval(()=>{
    loadWeatherNow();
    if (card.classList.contains('open')){
      loadWeatherHourly();
      loadWeatherDaily();
    }
  }, WEATHER_REFRESH_MS);
}
initWeather();

setInterval(()=>{
  buildDayLog();
  updateStats();
  updateProgress();
}, 60000);
</script>
</body>
</html>
