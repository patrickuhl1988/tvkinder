#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Baut TVKinderprogramm.de — drei Seiten, je eine einzelne HTML-Datei
mit inline <style> und <script>.

Das Stylesheet ist unverändert von TVFussball.de übernommen (orig.css).
Inhalte kommen aus epg_data.py.
"""
import pathlib
import epg_data as D

HERE = pathlib.Path(__file__).parent
BASE_CSS = (HERE / "orig.css").read_text(encoding="utf-8")

BRAND = "TVKinderprogramm.de"
DOMAIN = "https://tvkinderprogramm.de"

ADD_CSS = """
  /* Optionen als Chips: gleiche Familie wie die Filter darüber */
  .opt{border:1px solid var(--line2); background:var(--surface); color:var(--ink);
    border-radius:var(--r-ctl); padding:7px 12px; font-size:12.5px; font-weight:650;
    display:inline-flex; align-items:center; gap:7px; cursor:pointer; user-select:none;
    transition:background .15s, border-color .15s, color .15s}
  .opts .opt, .opt{background:var(--surface)}
  .opt:hover{border-color:#F1571A; color:#C94108}
  html[data-theme="dark"] .opt:hover{color:#FF9A5C; border-color:rgba(255,122,61,.5)}
  .opt input{appearance:none; -webkit-appearance:none; margin:0; width:15px; height:15px;
    flex:0 0 auto; border:1.5px solid var(--line2); border-radius:2px; background:var(--surface);
    display:grid; place-items:center; cursor:pointer; transition:background .12s, border-color .12s}
  .opt input:checked{background:#FFF3E8; border-color:#FFF3E8}
  .opt input:checked::after{content:""; width:8px; height:4.5px; margin-top:-1.5px;
    border-left:2px solid #D8430C; border-bottom:2px solid #D8430C; transform:rotate(-45deg)}
  .opts .opt:has(input:checked), .opt:has(input:checked){
    background:linear-gradient(135deg,#FF7A3D,#F1571A 55%,#D8430C) !important;
    border-color:#D8430C; color:#FFF3E8}
  .opt input:focus-visible{outline:2px solid #F1571A; outline-offset:2px}
  .opts{background:none; border:none; box-shadow:none; padding:2px 0 0}

  /* Altersfilter: keine Sonderfarben, gleiche Familie wie alle Chips */
  .fchip.tmode{color:var(--ink); border-color:var(--line2); background:var(--surface); font-weight:650}
  .fchip.tmode[aria-pressed="true"]{
    background:linear-gradient(135deg,#FF7A3D,#F1571A 55%,#D8430C); border-color:#D8430C; color:#FFF3E8}
  html[data-theme="dark"] .freebest.tv{color:#3A2606}

  /* Sonderfilter-Reihe, Elterntipp als Empfehlung hervorgehoben */
  .opts.specialrow{padding-top:0; margin-top:-2px}
  .fchip.tippchip{background:var(--surface); border-color:var(--line2); color:var(--ink);
    font-weight:650; box-shadow:none}
  .fchip.tippchip[aria-pressed="true"]{
    background:linear-gradient(135deg,#FF7A3D,#F1571A 55%,#D8430C); border-color:#D8430C; color:#FFF3E8}
  html[data-theme="dark"] .fchip.tippchip{background:var(--surface);
    border-color:var(--line2); color:var(--ink)}
  html[data-theme="dark"] .fchip.tippchip[aria-pressed="true"]{color:#FFF3E8}

  /* Markenbanner im Kopf: läuft über die volle verfügbare Breite,
     die Schalter rechts stehen fest, das Banner gibt nach. */
  .logo .logobanner{display:block; height:54px; width:auto; max-width:100%;
    object-fit:contain; object-position:left center; border-radius:10px}
  @media (min-width:700px){ .logo .logobanner{height:66px} }
  @media (max-width:400px){ .logo .logobanner{height:46px} }
  @media (max-width:345px){ .logo .logobanner{height:40px} }
  html[data-theme="dark"] .logo .logobanner{filter:drop-shadow(0 1px 4px rgba(0,0,0,.45))}

  /* Kopfzeile: eine Reihe, eine Höhe, ein Raster.
     Alle Bedienelemente exakt 32px hoch, das Maskottchen läuft mit der
     Versalhöhe des Schriftzugs (24px zu 17px Schrift), damit Bild und Text
     wie EIN Logo wirken statt wie zwei Nachbarn. */
  .hbar{display:flex; align-items:center; gap:10px; min-height:56px}
  .logo{display:flex; align-items:center; gap:7px; min-width:0; flex:1 1 auto}
  .logotv{width:24px; height:24px; display:block; flex:0 0 auto;
    transform:translateY(-1px);            /* optischer Ausgleich zur x-Höhe */
    filter:drop-shadow(0 1px 1.5px rgba(58,42,32,.16))}
  .logo .wordmark{font-family:"Archivo",sans-serif; font-weight:800; font-size:17px;
    letter-spacing:-.015em; line-height:1; color:var(--ink);
    overflow:hidden; text-overflow:ellipsis; white-space:nowrap}
  .switches{display:flex; align-items:center; gap:6px; flex:0 0 auto}
  .switches .seg.lang{height:32px; box-sizing:border-box; padding:2px;
    display:flex; align-items:stretch; border-radius:var(--r-ctl)}
  .switches .seg.lang button{height:auto; padding:0 9px; font-size:11.5px;
    border-radius:calc(var(--r-ctl) - 1px)}
  .switches .mktbtn, .switches .themebtn{width:32px; height:32px;
    box-sizing:border-box; border-radius:var(--r-ctl);
    display:grid; place-items:center; padding:0}
  .switches .mktbtn-flag{font-size:16px; line-height:1}
  .switches .themebtn svg{width:17px; height:17px}
  @media (max-width:374px){
    .logotv{width:21px; height:21px}
    .logo .wordmark{font-size:14.5px}
    .switches{gap:4px}
    .switches .seg.lang button{padding:0 7px} }

  .section-eyebrow.tipphead{display:flex; align-items:center; gap:10px; flex-wrap:wrap; row-gap:8px}
  .section-eyebrow.tipphead h2{flex:1 1 auto; min-width:0}
  .mehrbtn.klein{width:auto; margin:0; padding:8px 12px; font-size:12px; flex:0 0 auto}
  .intro{font-size:13px; color:var(--muted); line-height:1.65; margin:14px 2px 4px}
  .intro b{color:var(--ink); font-weight:750}






  /* ---- Vorschlags-Boxen: Cover-Kacheln + Kino-Raster ---- */
  .mthumb{position:relative; width:76px; flex:0 0 auto; border-radius:11px; overflow:hidden;
    align-self:stretch; min-height:76px; background:var(--bg2)}
  .mthumb img{position:absolute; inset:0; width:100%; height:100%; object-fit:cover}
  .mfolgen{position:absolute; left:4px; bottom:4px; right:4px; text-align:center;
    background:rgba(32,37,49,.72); color:#fff; border-radius:7px; padding:2px 4px;
    font:700 8.5px "JetBrains Mono",monospace; letter-spacing:.02em; white-space:nowrap;
    overflow:hidden; text-overflow:ellipsis}
  #medBoard .rowhead{display:flex; gap:12px}
  .kinogrid{display:grid; grid-template-columns:1fr 1fr; gap:10px}
  @media (min-width:760px){ .kinogrid{grid-template-columns:repeat(4,1fr)} }
  .kinogrid .kinoart{height:150px}
  .jetztbox + .jetztbox{margin-top:16px}

  /* ---- Kompakt-Kacheln: alles sichtbar, kein Aufklappen ---- */
  .kompaktrow .rowhead{cursor:default; padding-bottom:9px}
  .rowfuss{display:flex; align-items:center; gap:10px; padding:9px 14px 12px;
    border-top:1px solid var(--line)}
  .pcheck{flex:1 1 auto; min-width:0; display:flex; align-items:center; gap:6px}
  .pclbl{font:700 9.5px "JetBrains Mono",monospace; letter-spacing:.07em;
    text-transform:uppercase; color:var(--muted); white-space:nowrap}
  .pcval{font:850 14px "Archivo",sans-serif}
  .pcmax{font-size:10px; color:var(--faint); margin-right:2px}
  .pcbar{flex:1 1 auto; min-width:34px; height:5px; border-radius:999px;
    background:var(--bg2); overflow:hidden}
  .pcbar span{display:block; height:100%; border-radius:999px}
  .pcleer{flex:1 1 auto}
  .rowact{display:flex; align-items:center; gap:7px; flex:0 0 auto}
  .minibtn{width:34px; height:34px; border-radius:10px; border:1px solid var(--line2);
    background:var(--surface); color:var(--muted); display:grid; place-items:center; cursor:pointer}
  .minibtn svg{width:16px; height:16px}
  .minibtn:hover{color:#F2673A; border-color:#F2673A}
  .schaubtn{display:inline-flex; align-items:center; gap:6px; padding:8px 12px;
    border-radius:10px; background:linear-gradient(135deg,#F2673A,#FF8B5F); color:#fff;
    font:700 11.5px "Inter",sans-serif; text-decoration:none; white-space:nowrap}
  .schaubtn svg{width:12px; height:12px}
  .durtag.adfrei{color:#1D7A4B; background:rgba(35,154,104,.1); border-color:rgba(35,154,104,.35)}

  /* ---- Mediathek-Redesign: Hero, Filterkarte, Bereichskoepfe, Kino-Karten ---- */
  .heromed{background:linear-gradient(180deg, rgba(123,97,209,.12), rgba(123,97,209,0) 82%);
    border-radius:24px; padding:18px 16px 6px; margin:6px 0 14px}
  .heromed-grid{display:grid; grid-template-columns:1fr; gap:6px; align-items:center}
  .heromed .kicker{color:#7B61D1}
  .heromed .heroh1{font-size:clamp(26px,6vw,44px)}
  .heromask{width:min(240px,62%); height:auto; justify-self:center; margin-top:4px}
  @media (min-width:720px){
    .heromed-grid{grid-template-columns:1.35fr .65fr; gap:18px}
    .heromask{width:100%; max-width:290px; margin-top:0}
  }
  .filtercard{background:var(--surface); border:1px solid var(--line); border-radius:20px;
    box-shadow:var(--shadow); padding:14px 14px 6px; margin:0 0 16px}

  .section-eyebrow.tipphead.sekkopf{display:flex; align-items:center; gap:11px;
    flex-wrap:nowrap; row-gap:0; margin:20px 2px 10px}
  .sekkopf .secht h2{font-size:15px}
  @media (max-width:420px){ .sekkopf .secht h2{font-size:13.5px} .sekkopf .cnt{display:none} }
  .secic{flex:0 0 auto; width:38px; height:38px; border-radius:12px; display:grid; place-items:center; color:#fff}
  .secic svg{width:19px; height:19px}
  .secic.lila{background:linear-gradient(145deg,#8E77DC,#7B61D1)}
  .secic.lila2{background:linear-gradient(145deg,#6550A5,#493B73)}
  .secic.gruen{background:linear-gradient(145deg,#2FB077,#239A68)}
  .secic.blau{background:linear-gradient(145deg,#54A0E0,#3988D6)}
  .secht{flex:1 1 auto; min-width:0}
  .secht h2{margin:0}
  .secht .cnt{display:block; margin:1px 0 0}
  .sekkopf .allelink{padding:8px 0}

  .hscroll{display:grid; grid-auto-flow:column; grid-auto-columns:170px; gap:10px;
    overflow-x:auto; padding:2px 2px 8px; scroll-snap-type:x proximity;
    -webkit-overflow-scrolling:touch}
  .kinocard{scroll-snap-align:start; background:var(--surface); border:1px solid var(--line);
    border-radius:16px; box-shadow:var(--shadow); padding:9px 9px 11px}
  .kinoart{position:relative; height:120px; border-radius:11px; overflow:hidden;
    background:linear-gradient(150deg,var(--k1),var(--k2)); display:grid; place-items:center}
  .kinoart img{width:100%; height:100%; object-fit:cover}
  .ribbon{position:absolute; left:-26px; top:12px; transform:rotate(-38deg); z-index:2;
    background:linear-gradient(90deg,#F2673A,#FF8B5F); color:#fff; padding:3px 28px;
    font:800 9px "JetBrains Mono",monospace; letter-spacing:.09em; text-transform:uppercase}
  .ribbon.neu{background:linear-gradient(90deg,#239A68,#2FB077)}
  .fskcircle{position:absolute; right:7px; top:7px; z-index:2; width:26px; height:26px;
    border-radius:50%; background:rgba(255,255,255,.94); color:#202531; display:grid;
    place-items:center; font:800 11.5px "Archivo",sans-serif; box-shadow:0 2px 6px rgba(0,0,0,.25)}
  .kinocard h3{font:800 13px "Archivo",sans-serif; letter-spacing:-.01em; color:var(--ink);
    margin:9px 1px 3px; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical;
    overflow:hidden; min-height:33px}
  .kinocard .kmeta{font-size:10.5px; color:var(--muted); margin:0 1px 9px}
  .kinocard .trailerbtn{padding:7px 11px; font-size:11.5px}

  /* ---- Sendungs-Kacheln 2.0 ---- */
  .row{position:relative; padding-left:0; background:var(--surface); border:1px solid var(--line);
    border-radius:16px; box-shadow:var(--shadow); margin:0 0 10px; overflow:hidden}
  .row.free{box-shadow:var(--shadow)}
  .row.playing{border-color:rgba(229,72,77,.38)}
  .row.past{opacity:.55}
  .rowhead{display:flex; grid-template-columns:none; gap:12px; padding:13px 14px;
    align-items:flex-start; width:100%; text-align:left}
  .chtile{width:46px; height:46px; flex:0 0 auto; border-radius:14px; display:grid; place-items:center;
    color:#fff; font:850 19px "Archivo",sans-serif; letter-spacing:0;
    background:linear-gradient(145deg, color-mix(in srgb, var(--chc) 78%, #fff), var(--chc));
    text-shadow:0 1px 2px rgba(0,0,0,.22)}
  .teams{flex:1 1 auto; min-width:0}
  .topline{display:flex; align-items:center; gap:8px; margin:1px 0 5px;
    font:700 10px "JetBrains Mono",monospace; letter-spacing:.09em; text-transform:uppercase;
    color:var(--muted)}
  .chname{white-space:nowrap; overflow:hidden; text-overflow:ellipsis}
  .livebadge{display:inline-flex; align-items:center; gap:5px; color:#E5484D; flex:0 0 auto}
  .livedot{width:7px; height:7px; border-radius:50%; background:#E5484D;
    box-shadow:0 0 0 0 rgba(229,72,77,.45); animation:tvkpuls 1.7s infinite}
  @keyframes tvkpuls{70%{box-shadow:0 0 0 6px rgba(229,72,77,0)}100%{box-shadow:0 0 0 0 rgba(229,72,77,0)}}
  .topzeit{margin-left:auto; flex:0 0 auto; font:800 13.5px "Archivo",sans-serif;
    letter-spacing:-.01em; color:var(--ink); text-transform:none}
  .rowhead .t{font-family:"Archivo",sans-serif; font-weight:800; font-size:15px; letter-spacing:-.015em}
  .rowhead .t.subline{font:600 12px "Inter",sans-serif; color:var(--muted); letter-spacing:0; margin-top:1px}
  .rowhead .meta{margin-top:7px; display:flex; flex-wrap:wrap; gap:5px 6px; align-items:center}
  .durtag{font-family:"JetBrains Mono",monospace; font-size:9.5px; font-weight:700;
    padding:2.5px 7px; border-radius:6px; white-space:nowrap;
    background:var(--bg2); color:var(--muted); border:1px solid var(--line2)}
  .liveprog{margin-top:10px; height:5px; border-radius:999px; background:var(--bg2); overflow:hidden}
  .liveprog span{display:block; height:100%; border-radius:999px;
    background:linear-gradient(90deg,#F2673A,#FF8B5F)}

  /* ---- Jetzt-Box mit kleinem Alle-Link ---- */
  .jetztbox{display:block; background:var(--bg2); border:1px solid var(--line);
    border-radius:20px; padding:13px 12px 4px; margin:16px 0 0}
  .jetztbox .daybar{background:var(--bg2)}
  .jetztbox.offen{background:none; border:0; border-radius:0; padding:0; margin:0}
  .jetztbox.offen .daybar{background:var(--bg)}
  .allelink{margin-left:auto; flex:0 0 auto; border:0; background:none; cursor:pointer;
    color:#F2673A; font:800 12.5px "Inter",sans-serif; padding:6px 0; white-space:nowrap}
  .allelink:hover{text-decoration:underline}
  .allelink.unten{display:flex; justify-content:center; width:100%; margin:0 auto 6px;
    padding:10px 0; min-height:44px; align-items:center; font-size:13px}
  .footnav{display:flex; flex-wrap:wrap; gap:8px; margin:0 0 12px; font-size:12px}
  .footnav a{color:var(--ink); font-weight:650; text-decoration:none}
  .footnav a:hover{color:#F2673A}
  .footnav span{color:var(--faint)}

  /* Feinschliff Kacheln: ruhige weisse Karten, normale Schrift, ohne Sticker */
  .row, .row.free, .row.playing, .row.retro{background:var(--surface) !important;
    background-image:none !important}
  .rowhead .teams .t{font-family:"Archivo",sans-serif !important; font-weight:800 !important;
    font-size:15px !important; letter-spacing:-.015em !important; text-transform:none !important}
  .rowhead .teams .t.subline{font-family:"Inter",sans-serif !important; font-weight:600 !important;
    font-size:12px !important; color:var(--muted) !important; text-transform:none !important;
    letter-spacing:0 !important}
  .rowhead .stick{display:none !important}
  .row.playing{border-color:var(--line)}
  .row.playing .liveprog{margin-top:10px}
  .row .rowhead, .row .rowhead:hover{background:none !important}
  .row .rowhead:hover{background:var(--hover) !important}
  .row.playing, .row.playing.free{border-color:var(--line) !important}
  .row::after{content:none !important}          /* Deko-Ring aus der Basis aus */
  .row::before{width:0 !important}              /* alter Farbbalken links aus */
  .logowort{height:44px}
  @media (max-width:430px){ .logowort{height:34px} }

  /* ---- Redesign 2026: Hero, Feature-Banner, Spiele-Teaser, Footer ---- */
  .hero{margin:8px 2px 16px}
  .filterbar{margin:6px 0 14px}
  .filterbar .chiprow{margin:0 0 9px}
  .filterbar .fsearch{margin:0}
  .kicker{font:800 11px "JetBrains Mono",monospace; letter-spacing:.14em;
    text-transform:uppercase; color:#F2673A; margin:0 0 10px}
  .heroh1{font-family:"Archivo",sans-serif; font-weight:850;
    font-size:clamp(30px,7vw,54px); line-height:1.05; letter-spacing:-.028em;
    color:var(--ink); margin:0 0 12px; max-width:820px}
  .heroh1 em{font-style:normal; color:#F2673A}
  .lead{font-size:14.5px; line-height:1.65; color:var(--muted); max-width:680px; margin:0 0 16px}
  .stats{display:grid; grid-template-columns:repeat(auto-fit,minmax(140px,1fr)); gap:9px; margin:0 0 14px}
  .stat{border:1px solid var(--line); border-radius:14px; background:var(--surface);
    box-shadow:var(--shadow); padding:11px 13px}
  .stat strong{display:block; font-family:"Archivo",sans-serif; font-size:20px;
    font-weight:850; letter-spacing:-.03em; color:var(--ink)}
  .stat span{display:block; color:var(--muted); font-size:11.5px; margin-top:2px}
  .heroslot{position:relative; display:block; text-decoration:none}
  .heroslot.klickbar{cursor:pointer}
  .heroart{display:block; width:100%; height:auto; aspect-ratio:1500/701; object-fit:cover;
    border-radius:var(--r); box-shadow:var(--shadow); border:1px solid var(--line);
    transition:opacity .38s ease}
  .herocap{position:absolute; left:12px; bottom:12px; max-width:calc(100% - 24px);
    background:rgba(32,37,49,.78); color:#fff; backdrop-filter:blur(6px);
    border-radius:999px; padding:8px 14px; font:650 12px "Inter",sans-serif; line-height:1.35}
  .allebtn{display:flex; justify-content:center; margin:14px auto 0; border:0; cursor:pointer;
    background:linear-gradient(135deg,#F2673A,#FF8B5F); color:#fff; border-radius:999px;
    padding:13px 24px; font:700 13.5px "Inter",sans-serif; min-height:44px; align-items:center;
    box-shadow:0 10px 24px -10px rgba(242,103,58,.55); transition:transform .12s, box-shadow .12s}
  .allebtn:hover{transform:translateY(-1px); box-shadow:0 13px 28px -10px rgba(242,103,58,.6)}
  .logowort{display:block; height:40px; width:auto}
  @media (max-width:430px){ .logowort{height:32px} }
  .logo{display:flex; align-items:center; gap:9px}
  html[data-theme="dark"] .heroart{opacity:.94}

  .feature{display:grid; grid-template-columns:1.25fr .75fr; gap:18px; align-items:center;
    margin:22px 0 0; padding:20px 22px; border-radius:20px; text-decoration:none;
    background:linear-gradient(135deg,#2D2942,#493B73 58%,#6550A5); color:#fff;
    box-shadow:0 18px 44px -14px rgba(73,59,115,.5)}
  .feature .kicker2{display:block; font:800 10.5px "JetBrains Mono",monospace;
    letter-spacing:.13em; text-transform:uppercase; color:#D7CAFE; margin-bottom:8px}
  .feature b{display:block; font-family:"Archivo",sans-serif; font-size:22px;
    font-weight:850; letter-spacing:-.03em; margin-bottom:7px}
  .feature .fs{display:block; color:#DDD7EE; font-size:13px; line-height:1.6; margin-bottom:13px}
  .feature .ctas{display:flex; flex-wrap:wrap; gap:8px; margin-top:13px}
  .feature .cta{display:inline-flex; background:#fff; color:#322A50; padding:10px 14px;
    border-radius:11px; font-weight:800; font-size:12.5px; text-decoration:none; min-height:40px;
    align-items:center}
  .feature .cta.cta2{background:rgba(255,255,255,.12); color:#fff;
    border:1px solid rgba(255,255,255,.45)}
  .feature .cta.cta2:hover{background:rgba(255,255,255,.2)}
  .feature img{width:100%; max-width:240px; height:auto; justify-self:center}
  .feature:hover .cta{background:#F2E9FF}
  @media(max-width:620px){ .feature{grid-template-columns:1fr; gap:10px} .feature img{max-width:180px} }

  .spielteaser{display:flex; align-items:center; gap:14px; margin:14px 0 0;
    padding:13px 16px; border:1px dashed var(--line2); border-radius:16px; background:var(--surface2);
    text-decoration:none}
  a.spielteaser:hover{border-color:#F2673A; border-style:solid}
  .spielteaser img{width:62px; height:auto; flex:0 0 auto}
  .spielteaser b{display:block; font-family:"Archivo",sans-serif; font-size:14.5px;
    font-weight:800; color:var(--ink); margin-bottom:3px}
  .spielteaser .s{display:block; font-size:12.5px; color:var(--muted); line-height:1.55}
  .spielteaser .bald{margin-left:auto; flex:0 0 auto; font:700 10px "JetBrains Mono",monospace;
    letter-spacing:.08em; text-transform:uppercase; color:#8A5A00; border:1px solid #D9A94E;
    background:rgba(217,169,78,.14); border-radius:999px; padding:4px 9px}
  html[data-theme="dark"] .spielteaser .bald{color:#F0C868; border-color:rgba(240,200,104,.5);
    background:rgba(240,200,104,.12)}

  .empty::before{content:""; display:block; width:110px; height:110px; margin:6px auto 10px;
    background:url(leer.png) center/contain no-repeat}

  footer .footlang{display:inline-flex; gap:2px; border:1px solid var(--line2);
    border-radius:999px; padding:2px; margin-right:8px; vertical-align:middle}
  footer .footlang button{border:0; background:none; color:var(--muted);
    font:700 11px "Inter",sans-serif; padding:5px 10px; border-radius:999px; cursor:pointer}
  footer .footlang button[aria-pressed="true"]{background:var(--surface); color:var(--ink);
    box-shadow:var(--shadow)}

  #medGenres .fchip[data-i]::before{content:""; display:inline-block; width:19px; height:19px;
    background:center/contain no-repeat; margin:-3px 5px -4px -2px}
  #medGenres .fchip[data-i="ab"]::before{background-image:url(interesse-abenteuer.png)}
  #medGenres .fchip[data-i="ti"]::before{background-image:url(interesse-tiere.png)}
  #medGenres .fchip[data-i="ma"]::before{background-image:url(interesse-magie.png)}
  #medGenres .fchip[data-i="la"]::before{background-image:url(interesse-lachen.png)}
  #medGenres .fchip[data-i="wi"]::before{background-image:url(interesse-wissen.png)}

  .seotext{margin:30px 2px 12px; padding-top:18px; border-top:1px solid var(--line)}
  .seotext h2{font-family:"Archivo",sans-serif; font-weight:800; font-size:15px;
    letter-spacing:-.01em; color:var(--ink); margin-bottom:8px}
  .seotext p{font-size:12.5px; color:var(--muted); line-height:1.7; margin:0 0 10px}

  .fgroup{margin:2px 0 7px}
  .fglabel{display:block; font-family:"JetBrains Mono",monospace; font-size:10px;
    letter-spacing:.09em; text-transform:uppercase; font-weight:700;
    color:var(--muted); margin:0 2px 5px}

  .kinorow{border:1px solid var(--line2); border-radius:14px; background:var(--surface);
    padding:12px 14px 13px; margin:0 0 10px}
  .kinorow h3{font-family:"Archivo",sans-serif; font-size:14.5px; font-weight:800;
    letter-spacing:-.01em; color:var(--ink); margin:0 0 7px}
  .kinometa{display:flex; flex-wrap:wrap; gap:6px; margin:0 0 8px}
  .kinobadge{font-family:"JetBrains Mono",monospace; font-size:10px; font-weight:600;
    letter-spacing:.05em; color:var(--muted); border:1px solid var(--line2);
    border-radius:var(--r-ctl); padding:3px 7px}
  .kinobadge.neu{color:#8A5A00; border-color:#D9A94E; background:rgba(217,169,78,.14)}
  .kinodesc{font-size:12.5px; color:var(--muted); line-height:1.62; margin:0 0 10px}
  .trailerbtn{display:inline-flex; align-items:center; gap:7px; padding:8px 13px;
    border:1px solid var(--line2); border-radius:var(--r-ctl); background:none;
    color:var(--ink); font-family:"Inter",sans-serif; font-size:12px; font-weight:650;
    text-decoration:none}
  .trailerbtn svg{width:13px; height:13px; color:#F1571A}
  .trailerbtn:hover{border-color:#F1571A}

  .tippnote{font-size:12.5px; color:var(--muted); margin:0 2px 8px; min-height:0}
  .tippnote:empty{display:none}

  .panelprov{display:flex; flex-wrap:wrap; gap:6px; margin:10px 0 12px}
  .panelprov:empty{display:none}

  /* Aufklappbarer Filterblock der Startseite */
  .imgbtn{flex:0 0 auto; padding:0; border:0; background:none; cursor:pointer; line-height:0}
  .imgbtn img{height:44px; width:auto; display:block; border-radius:0;
    filter:drop-shadow(0 1px 3px rgba(58,42,32,.22)); transition:transform .12s}
  .imgbtn:hover img{transform:translateY(-1px)}
  .imgbtn:disabled{opacity:.55; cursor:default}
  .imgbtn.ohnebild{padding:8px 12px; border:1px solid var(--line2); border-radius:var(--r-ctl);
    background:var(--surface); color:var(--ink); font-family:"Inter",sans-serif;
    font-size:12px; font-weight:650; line-height:1.2}

  .crosslink.muehle .cl-ic.mm{background:linear-gradient(135deg,#7A5B3A,#4C3216);
    display:grid; place-items:center}
  .crosslink.muehle .cl-ic.mm svg{width:20px; height:20px; color:#F2E4CF}
  .crosslink[hidden]{display:none}

  .filtertoggle{display:inline-flex; align-items:center; gap:7px; margin:10px 0 8px}
  .filtertoggle svg{width:14px; height:14px; transition:transform .2s}
  .filtertoggle[aria-expanded="true"] svg{transform:rotate(180deg)}
  .klapp{display:grid; grid-template-rows:0fr; transition:grid-template-rows .26s ease}
  .klapp.auf{grid-template-rows:1fr}
  .klapp-in{overflow:hidden; min-height:0}
  .klapp-pad{margin:2px 0 10px; padding:12px 12px 6px;
    border:1px solid var(--line); border-radius:12px; background:var(--surface)}
  html[data-theme="dark"] .klapp-pad{background:rgba(255,255,255,.03)}
  .klapp-pad .fsearch{margin-top:0}

  /* Ankreuz-Schalter im selben Kleid wie die Filterchips: ein Guss */
  .chiprow .opt span, .opts .opt span{overflow:visible; flex:0 0 auto; min-width:max-content}
  .chiprow .opt, .opts .opt{display:inline-flex; align-items:center; gap:0; flex:0 0 auto;
    padding:7px 12px; border:1px solid var(--line2); border-radius:3px; background:var(--surface);
    font-family:"Inter",sans-serif; font-size:12px; font-weight:650; color:var(--ink);
    cursor:pointer; user-select:none}
  .chiprow .opt input, .opts .opt input{position:absolute; opacity:0; pointer-events:none;
    width:1px; height:1px; margin:0; -webkit-appearance:none; appearance:none}
  .chiprow .opt:has(input:checked), .opts .opt:has(input:checked){color:#fff; border-color:transparent;
    background:linear-gradient(135deg,#FF7A3D,#F1571A 55%,#D8430C)}
  html[data-theme="dark"] .chiprow .opt:has(input:checked),
  html[data-theme="dark"] .opts .opt:has(input:checked){color:#FFF3EA}

  /* Chip-Zeile: einzeilig, auf dem Handy seitlich wischbar */
  .chiprow{display:flex; align-items:center; gap:7px; flex-wrap:nowrap; overflow-x:auto; padding:2px 2px 7px;
    scrollbar-width:none; -webkit-overflow-scrolling:touch}
  .chiprow::-webkit-scrollbar{display:none}
  .chiprow .fchip{flex:0 0 auto}
  .chipsep{flex:0 0 auto; width:1px; align-self:stretch; margin:4px 3px; background:var(--line2)}

  /* Mehr-Knopf und Hinweiszeile der Tipps */
  .mehrbtn{display:block; width:100%; margin:2px 0 14px; padding:11px 14px;
    border:1px solid var(--line2); border-radius:var(--r-ctl); background:var(--surface);
    color:var(--ink); font-family:"Inter",sans-serif; font-weight:650; font-size:13px; cursor:pointer}
  .mehrbtn:hover{border-color:#F1571A; color:#C94108}
  html[data-theme="dark"] .mehrbtn:hover{color:#FF9A5C; border-color:rgba(255,122,61,.5)}
  .mehrbtn:disabled{cursor:default; opacity:.75}
  .mehrbtn:disabled:hover{border-color:var(--line2); color:var(--ink)}

  /* Toast: unaufdringlich, unten mittig */
  .toast{position:fixed; left:50%; bottom:20px; transform:translate(-50%, 10px);
    background:var(--ink); color:var(--surface); font-size:13px; font-weight:600;
    padding:10px 16px; border-radius:var(--r); box-shadow:0 6px 22px -6px rgba(0,0,0,.35);
    opacity:0; pointer-events:none; transition:opacity .22s ease, transform .22s ease;
    max-width:88vw; text-align:center; z-index:60}
  .toast.an{opacity:1; transform:translate(-50%, 0)}

  /* Kopf: kleines Maskottchen + einheitlicher Schriftzug */

  /* Überschrift nur für Suchmaschinen und Screenreader */
  .srh1{position:absolute; width:1px; height:1px; padding:0; margin:-1px;
    overflow:hidden; clip:rect(0 0 0 0); clip-path:inset(50%);
    white-space:nowrap; border:0}

  /* Maskottchen im Leerzustand */
  .maskottchen.klein{width:64px; height:64px; display:block; margin:0 auto 10px;
    filter:drop-shadow(0 2px 4px rgba(58,42,32,.14))}

  /* ---- Kinder-Ergänzungen (nutzen nur bestehende Tokens) ---- */
  :root{--wm-line:rgba(183,121,31,.30)}
  html[data-theme="dark"]{--wm-line:rgba(232,196,78,.32)}
  .teams .t.subline{font-weight:500; font-size:13px; color:var(--muted); margin-top:2px}
  .agetag{font-family:"JetBrains Mono",monospace; font-size:9.5px; font-weight:700; letter-spacing:.02em;
    padding:2.5px 7px; border-radius:6px; white-space:nowrap;
    background:var(--wm-soft); color:var(--wm); border:1px solid var(--wm-line)}
  .fsktag{font-family:"JetBrains Mono",monospace; font-size:9.5px; font-weight:700;
    padding:2.5px 7px; border-radius:6px; white-space:nowrap;
    background:transparent; color:var(--muted); border:1px solid var(--line2)}
  .agebox{margin-top:10px; border-top:1px solid var(--line); padding-top:9px}
  .agebox .arow{display:flex; align-items:baseline; gap:9px; padding:5px 0; font-size:13px}
  .agebox .alb{flex:0 0 128px; font:700 10.5px "Inter",sans-serif; letter-spacing:.06em;
    text-transform:uppercase; color:var(--muted)}
  .agebox .aval{color:var(--ink); font-weight:600}
  .agebox .ahint{font-size:11.5px; color:var(--faint); line-height:1.5; margin-top:5px}
  .estmark{font:700 9px "JetBrains Mono",monospace; color:var(--faint); border:1px solid var(--line2);
    border-radius:4px; padding:1px 4px; margin-left:6px; vertical-align:middle}
  .wmsec-body p{font-size:13.5px; color:var(--muted); line-height:1.62}
  .wmsec-body p + p{margin-top:9px}
  .provrow{display:flex; align-items:center; gap:13px; padding:13px 15px}
  .provrow .plogo{flex:0 0 auto; width:44px; height:44px; display:grid; place-items:center;
    background:var(--pv-bg); color:var(--pv-tx); border:1px solid var(--pv-bd);
    font-family:"Archivo",sans-serif; font-weight:900; font-size:13px}
  html[data-theme="dark"] .provrow .plogo{background:var(--pv-bgd); color:var(--pv-txd)}
  .provcard{--c1:var(--pv); --c2:var(--pv)}
  .provcard .provrow{background:
    radial-gradient(120% 150% at 0% 0%, var(--pv-bg), transparent 60%)}
  html[data-theme="dark"] .provcard .provrow{background:
    radial-gradient(130% 165% at 0% 0%, var(--pv-bgd), transparent 64%)}
  .provcard .pprice{color:var(--pv-tx)}
  html[data-theme="dark"] .provcard .pprice{color:var(--pv-txd)}
  .provcard .feat.yes{color:var(--pv-tx); border-color:var(--pv-bd); background:var(--pv-bg)}
  html[data-theme="dark"] .provcard .feat.yes{color:var(--pv-txd); background:var(--pv-bgd)}
  .provrow .pmain{flex:1 1 auto; min-width:0}
  .provrow .pmain b{display:block; font-family:"Archivo",sans-serif; font-weight:800; font-size:15px; letter-spacing:-.01em}
  .provrow .pmain span{display:block; color:var(--muted); font-size:12.5px; margin-top:2px}
  .provrow .pprice{flex:0 0 auto; font-family:"JetBrains Mono",monospace; font-weight:700; font-size:12.5px; white-space:nowrap}
  .featrow{display:flex; flex-wrap:wrap; gap:6px; margin-top:8px}
  .feat{font:600 11px "Inter",sans-serif; padding:2px 8px; border-radius:99px;
    border:1px solid var(--line); background:var(--bg2); color:var(--muted)}
  .feat.yes{color:var(--free); border-color:var(--free-line); background:var(--free-soft)}
  /* ================= Warme Farbwelt für das Kinderprogramm =================
     Prinzip wie die Vereinsfarben bei TVFussball: jede Sendung trägt ein
     eigenes Farbpaar (--c1/--c2), das aus dem Titel abgeleitet wird und
     damit immer gleich bleibt. Daraus speisen sich Sticker, Kartenwäsche
     und der geöffnete Zustand.
     ===================================================================== */

  /* ---- Grundpalette: von kühlem Blaugrau auf warm gedreht -------------
     Struktur und Abstände bleiben identisch zu TVFussball, nur die
     Neutraltöne und der Akzent wechseln. Grün bleibt für „kostenlos".  */
  :root{
    --bg:#F7F5F0; --bg2:#F1EDE6; --surface:#FFFFFF; --surface2:#FFF8F3;
    --line:#E8E3DB; --line2:#DBD3C7;
    --ink:#202531; --muted:#6F7683; --faint:#9AA0AB;
    --green:#C24009; --green-soft:rgba(194,64,9,.10); --green-line:rgba(194,64,9,.28);
    --free:#B07408; --free-soft:rgba(176,116,8,.12); --free-line:rgba(176,116,8,.34);
    --free-grad:linear-gradient(135deg,#FFC14D,#F2A413 58%,#D98E0B);
    --on-accent:#FFFFFF;
    --header-bg:rgba(253,246,240,.86); --hover:rgba(31,21,18,.035);
    --shadow:0 1px 2px rgba(90,50,25,.05), 0 6px 20px -8px rgba(90,50,25,.14);
    --header-shadow:0 1px 0 rgba(90,50,25,.06), 0 8px 22px -14px rgba(90,50,25,.14);
    --wm:#8A5A0B; --wm-soft:#FBF1DD;
  }
  html[data-theme="dark"]{
    /* Flächen fast neutral halten. Ein brauner Grundton plus farbige Wäsche
       ergibt Matsch — die Wärme kommt hier aus Akzent, Farbbalken und Sticker,
       nicht aus dem Untergrund. Sättigung der Flächen unter 8 %. */
    --bg:#111010; --bg2:#191716; --surface:#221F1D; --surface2:#2C2825;
    --line:rgba(255,246,240,.10); --line2:rgba(255,246,240,.17);
    --ink:#F6F1EC; --muted:#B9ACA3; --faint:#8D827B;
    --green:#FF9A5C; --green-soft:rgba(255,154,92,.16); --green-line:rgba(255,154,92,.38);
    --free:#F2CE76; --free-soft:rgba(242,206,118,.14); --free-line:rgba(242,206,118,.36);
    --free-grad:linear-gradient(135deg,#FFD98A,#F2CE76 58%,#DDAE45);
    --on-accent:#2A1206;
    --header-bg:rgba(23,16,14,.86); --hover:rgba(255,255,255,.045);
    --shadow:0 1px 2px rgba(0,0,0,.42), 0 10px 30px -12px rgba(0,0,0,.62);
    --header-shadow:0 6px 24px rgba(0,0,0,.5);
    --wm:#F0C868; --wm-soft:rgba(240,200,104,.13);
  }

  /* Hintergrundschein */
  :root{--glow1:rgba(242,103,58,.10); --glow2:rgba(123,97,209,.06)}
  html[data-theme="dark"]{--glow1:rgba(242,103,58,.07); --glow2:rgba(123,97,209,.05)}

  /* Tagestrenner bekommt den warmen Verlauf */
  .daybar .dtag{background:linear-gradient(135deg,#F2673A,#FF8B5F); border:0}
  .daybar .dtag.tm{background:transparent; color:#F2673A; border:1px solid rgba(242,103,58,.45)}

  /* --- Farbbalken links auf jeder Karte -------------------------------- */
  .row{padding-left:6px}
  .row::before{content:""; position:absolute; left:0; top:0; bottom:0; width:6px; z-index:2;
    background:linear-gradient(180deg, var(--c1), var(--c2))}
  .row.free{box-shadow:var(--shadow)}          /* grüne Kante ersetzt durch Farbbalken */
  .row.open.free{box-shadow:0 0 0 1.5px var(--c1), var(--shadow)}

  /* --- Sticker statt Ball --------------------------------------------- */
  .stick{flex:0 0 auto; width:38px; height:38px; border-radius:12px; display:grid; place-items:center;
    background:linear-gradient(140deg, var(--s1), var(--s2)); color:#fff;
    box-shadow:0 3px 10px -3px var(--s1), inset 0 1px 0 rgba(255,255,255,.35);
    transform:rotate(-4deg); transition:transform .2s cubic-bezier(.34,1.5,.5,1)}
  .stick svg{width:21px; height:21px; display:block; filter:drop-shadow(0 1px 1px rgba(0,0,0,.18))}
  .rowhead:hover .stick{transform:rotate(4deg) scale(1.08)}
  .row.open .stick{transform:rotate(0deg) scale(1.05)}
  html[data-theme="dark"] .stick{box-shadow:0 3px 12px -3px var(--s1), inset 0 1px 0 rgba(255,255,255,.22)}

  /* --- Farbwäsche der Karte ------------------------------------------- */
  .row .mrow{background:
    radial-gradient(125% 150% at 0% 0%, var(--w1), transparent 58%),
    radial-gradient(125% 150% at 100% 0%, var(--w2), transparent 58%)}
  html[data-theme="dark"] .row .mrow{background:
    radial-gradient(140% 180% at 0% 0%, var(--w1d), transparent 66%),
    radial-gradient(140% 180% at 100% 0%, var(--w2d), transparent 66%)}
  .mnote{font-size:12.5px; color:var(--muted); line-height:1.5; margin:8px 0 0}
  .provmore{border:1px solid var(--line); border-radius:var(--r); background:var(--surface); margin:0 0 9px}
  .provmore>summary{list-style:none; cursor:pointer; padding:11px 13px; display:flex;
    align-items:center; gap:10px; font-size:12.5px; font-weight:700}
  .provmore>summary::-webkit-details-marker{display:none}
  .provmore .pm-cnt{margin-left:auto; font:400 11px "JetBrains Mono",monospace; color:var(--faint)}
  .provmore .wmchev{width:24px; height:24px}
  .provmore[open]>summary .wmchev{transform:rotate(180deg)}
  .provgrid.aus{border:0; border-top:1px solid var(--line); border-radius:0; margin:0; background:none}
  .row .rowhead{background:
    radial-gradient(125% 150% at 0% 0%, var(--w1), transparent 58%),
    radial-gradient(125% 150% at 100% 0%, var(--w2), transparent 58%)}
  .row .rowhead:hover{background:
    radial-gradient(125% 150% at 0% 0%, var(--w1), transparent 52%),
    radial-gradient(125% 150% at 100% 0%, var(--w2), transparent 52%),
    var(--hover)}
  .row.open{border-color:transparent; box-shadow:0 0 0 1.5px var(--c1), var(--shadow)}
  .row.open.free{box-shadow:inset 3px 0 0 var(--free), 0 0 0 1.5px var(--c1), var(--shadow)}
  .row.open .rowhead{background:
    radial-gradient(130% 165% at 0% 0%, var(--w1), transparent 62%),
    radial-gradient(130% 165% at 100% 0%, var(--w2), transparent 62%)}
  html[data-theme="dark"] .row{background:var(--surface); border-color:rgba(255,246,240,.11)}
  html[data-theme="dark"] .row .rowhead,
  html[data-theme="dark"] .row.open .rowhead{background:
    radial-gradient(140% 180% at 0% 0%, var(--w1d), transparent 66%),
    radial-gradient(140% 180% at 100% 0%, var(--w2d), transparent 66%)}
  /* Farbbalken und Sticker bleiben voll gesättigt — dort sitzt die Farbe */
  html[data-theme="dark"] .row::before{filter:saturate(1.15) brightness(1.1)}
  html[data-theme="dark"] .stick{filter:saturate(1.1) brightness(1.08)}
  html[data-theme="dark"] .row.open{border-color:transparent; box-shadow:0 0 0 1.5px var(--c1), 0 8px 30px rgba(0,0,0,.42)}

  /* Trennlinie im Panel in Sendungsfarbe statt Grau */
  .row .panel-pad{border-top:1.5px solid var(--w1)}
  html[data-theme="dark"] .row .panel-pad{border-top-color:var(--w1d)}

  /* Chevron übernimmt die Sendungsfarbe */
  .rowhead:hover .chev{color:var(--c1); border-color:var(--c1)}
  .row.open .chev{background:linear-gradient(140deg,var(--c1),var(--c2)); color:#fff; border-color:transparent}

  /* Aufklapp-Buttons und Links im Panel ebenfalls warm */
  .row .morebtn{color:var(--c1)}
  .row .chrow .nm a.streamlink{text-decoration-color:var(--c1)}
  .row .chrow .nm a.streamlink:hover{color:var(--c1)}

  /* Genre-Label bekommt einen farbigen Anstrich statt grauer Kante */
  .row .comp{border-left-color:var(--c1); color:var(--c1); opacity:.95}
  html[data-theme="dark"] .row .comp{opacity:1}

  /* Uhrzeit-Block als getönte Kachel */
  .row .time{background:linear-gradient(160deg, var(--w1), var(--w2));
    border-radius:11px; padding:7px 4px; margin-left:2px}
  html[data-theme="dark"] .row .time{background:linear-gradient(160deg, var(--w1d), var(--w2d))}

  /* Tagestrenner-Linie warm auslaufen lassen */
  .daybar .ln{background:linear-gradient(90deg, rgba(251,133,0,.45), rgba(247,37,133,.12) 60%, var(--line))}


  /* =====================================================================
     ENTRUNDUNG — zweiter Durchgang
     Die durchgehenden 14–18px-Radien, Pillen und weichen Schatten sind das,
     was ein Layout nach Baukasten aussehen lässt. Hier ersetzt durch eine
     knappe Radiusskala (4 / 3 / 2 px), Haarlinien statt Schlagschatten und
     eine Zeitspalte, die wie eine gedruckte Programmzeile liest.
     Bewusst nicht auf 0px: ganz kantig plus Haarlinien wäre das nächste
     Klischee. 4px liest sich präzise, nicht steril.
     ===================================================================== */
  :root{--r:16px; --r-ctl:11px; --r-tag:8px;
        --shadow:0 1px 2px rgba(60,45,25,.05), 0 10px 28px -12px rgba(60,45,25,.16);
        --header-shadow:0 1px 0 rgba(90,50,25,.06), 0 10px 26px -16px rgba(90,50,25,.18)}
  html[data-theme="dark"]{--r:16px;
        --shadow:0 1px 2px rgba(0,0,0,.4), 0 12px 30px -14px rgba(0,0,0,.6);
        --header-shadow:0 6px 24px rgba(0,0,0,.5)}

  /* Karten: Kontur statt Schatten */
  .row{border-radius:var(--r); box-shadow:none; padding-left:5px}
  .row::before{width:4px}
  .row.free{box-shadow:none}
  .row.open{box-shadow:none; border-color:var(--c1)}
  .row.open.free{box-shadow:none}
  html[data-theme="dark"] .row.open{box-shadow:none; border-color:var(--c1)}

  /* Bedienelemente */
  .fchip{border-radius:var(--r-ctl); padding:7px 12px; font-weight:700}
  /* #liveFilters wird in orig.css mit höherer Spezifität überschrieben */
  #liveFilters .fchip{border-radius:var(--r-ctl); box-shadow:none;
    padding:8px 13px; font-size:13px}
  #liveFilters .fchip[aria-pressed="true"]{box-shadow:none}
  .fchip .cdot{width:8px; height:8px; border-radius:2px; box-shadow:none}
  .fsearch{border-radius:var(--r); box-shadow:none}
  .seg{border-radius:var(--r-ctl)}
  .seg button{border-radius:2px}
  .mktbtn,.themebtn{border-radius:var(--r-ctl)}
  .mktpop{border-radius:var(--r); box-shadow:0 6px 24px rgba(60,35,20,.14)}
  .mktopt{border-radius:2px}
  .sharebtn{border-radius:var(--r-ctl)}
  .actrow .sharebtn{border-radius:var(--r-ctl)}
  .navitem{border-radius:var(--r-ctl)}
  .toast{border-radius:var(--r-ctl)}
  .consent{border-radius:var(--r); box-shadow:0 8px 30px rgba(60,35,20,.16)}
  .consent button{border-radius:var(--r-ctl)}
  .legal-card{border-radius:var(--r); box-shadow:none}
  .legal-x{border-radius:var(--r-ctl)}
  details.wmsec{border-radius:var(--r); box-shadow:none}
  .wmchev,.wm-secico{border-radius:var(--r-ctl)}
  .crosslink{border-radius:var(--r); box-shadow:none}
  .crosslink .cl-ic,.crosslink .cl-go{border-radius:var(--r-ctl)}
  .crosslink:hover{box-shadow:none; border-color:rgba(37,99,235,.42)}
  .provrow .plogo{border-radius:var(--r-ctl)}
  .vcard,.cardgrid .vcard{border-radius:var(--r); box-shadow:none}

  /* Chevron: Quadrat statt Kreis */
  .chev{border-radius:var(--r-ctl); width:28px; height:28px}
  .row.open .chev{border-radius:var(--r-ctl)}

  /* Marker: flache Kachel, keine schräge Sticker-Optik */
  .stick{width:32px; height:32px; border-radius:var(--r-ctl);
    background:var(--s1); box-shadow:none; transform:none}
  .stick svg{width:18px; height:18px; filter:none}
  .rowhead:hover .stick,.row.open .stick{transform:none; filter:brightness(1.08)}

  /* Badges kantiger und ruhiger */
  .agetag,.fsktag,.freebest,.chrow .tag{border-radius:var(--r-tag)}
  .freebest{font-weight:700; letter-spacing:.03em}

  /* --- Zeitspalte wie eine gedruckte Programmzeile --------------------- */
  .rowhead{grid-template-columns:66px 1fr auto; gap:13px; padding:12px 13px 12px 13px}
  .row .time{background:none; padding:0; margin:0; text-align:left; border-left:2px solid var(--c1);
    padding-left:9px}
  html[data-theme="dark"] .row .time{background:none}
  .t-start{display:block; font-family:"JetBrains Mono",monospace; font-weight:700;
    font-size:17px; letter-spacing:-.02em; color:var(--ink); line-height:1.05}
  .t-dur{display:block; font-family:"JetBrains Mono",monospace; font-size:10.5px;
    color:var(--muted); margin-top:3px; letter-spacing:.01em}
  .till{font-family:"JetBrains Mono",monospace; font-size:10px; color:var(--faint)}

  /* Zustände: läuft gerade / vorbei */
  .nowtag{font:700 9.5px "JetBrains Mono",monospace; letter-spacing:.08em; text-transform:uppercase;
    background:var(--red); color:#fff; padding:2.5px 6px; border-radius:var(--r-tag)}
  .pasttag{font:700 9.5px "JetBrains Mono",monospace; letter-spacing:.08em; text-transform:uppercase;
    border:1px solid var(--line2); color:var(--faint); padding:1.5px 5px; border-radius:var(--r-tag)}
  .row.past{opacity:.62}
  .row.past .stick{filter:grayscale(.55)}
  .row.playing{border-color:var(--red)}
  .row.playing .t-start{color:var(--red)}

  /* --- Optionen als echte Checkboxen ---------------------------------- */
  .opts{display:flex; align-items:center; gap:10px 16px; flex-wrap:wrap;
    margin:9px 0 2px; padding:11px 13px;
    border:1px solid var(--line); border-radius:var(--r); background:var(--surface)}
  .opts .fchip{flex:0 0 auto; text-decoration:none}
  .opt{display:inline-flex; align-items:center; gap:9px; cursor:pointer;
    font-size:13px; font-weight:700; color:var(--ink); user-select:none}
  .opt input{appearance:none; -webkit-appearance:none; margin:0; flex:0 0 auto;
    width:18px; height:18px; border:1.5px solid var(--line2); border-radius:var(--r-tag);
    background:var(--surface); display:grid; place-items:center; cursor:pointer;
    transition:background .12s ease, border-color .12s ease}
  .opt input:hover{border-color:var(--muted)}
  .opt input:checked{background:var(--free); border-color:var(--free)}
  .opt input:checked::after{content:""; width:9px; height:5px; margin-top:-2px;
    border-left:2px solid #fff; border-bottom:2px solid #fff; transform:rotate(-45deg)}
  .opt input:focus-visible{outline:2px solid var(--green); outline-offset:2px}
  #optPast:checked{background:var(--green); border-color:var(--green)}
  .opt-cnt{margin-left:auto; font-family:"JetBrains Mono",monospace; font-size:11px; color:var(--faint)}
  .opt span{white-space:nowrap; overflow:hidden; text-overflow:ellipsis}
  @media (max-width:460px){
    .opts{gap:11px; padding:10px 11px}
    .opt{font-size:12px; min-width:0}
    .opt-cnt{display:none}
  }
  #liveSpecial{padding-top:0}

  /* Querverweis auf das Schwesterprojekt */
  .crosslink{display:flex; align-items:center; gap:13px; margin:12px 0 10px; padding:12px 14px;
    background:var(--surface); border:1px solid var(--line); border-radius:var(--r);
    box-shadow:var(--shadow); text-decoration:none; color:inherit;
    transition:border-color .16s ease, box-shadow .16s ease, transform .1s ease}
  .crosslink:hover{border-color:rgba(37,99,235,.34); box-shadow:0 0 0 3px rgba(37,99,235,.10), var(--shadow)}
  .crosslink:active{transform:scale(.994)}
  .crosslink .cl-ic{flex:0 0 auto; width:40px; height:40px; border-radius:12px; display:grid; place-items:center;
    background:rgba(37,99,235,.10); color:#2563EB; border:1px solid rgba(37,99,235,.26)}
  html[data-theme="dark"] .crosslink .cl-ic{background:rgba(91,140,255,.16); color:#7FA8FF; border-color:rgba(91,140,255,.36)}
  .crosslink .cl-ic svg{width:22px; height:22px}
  .crosslink .cl-txt{flex:1 1 auto; min-width:0}
  .crosslink .cl-txt b{display:block; font-family:"Archivo",sans-serif; font-weight:800; font-size:14.5px;
    letter-spacing:-.01em; color:var(--ink)}
  .crosslink .cl-txt span{display:block; color:var(--muted); font-size:12.5px; margin-top:2px; line-height:1.4}
  .crosslink .cl-go{flex:0 0 auto; width:28px; height:28px; border-radius:50%; display:grid; place-items:center;
    border:1px solid var(--line); background:var(--bg2); color:var(--muted); transition:color .15s, border-color .15s}
  .crosslink .cl-go svg{width:15px; height:15px}
  .crosslink:hover .cl-go{color:#2563EB; border-color:rgba(37,99,235,.34)}
  @media (max-width:400px){ .crosslink .cl-txt span{font-size:11.5px} }
  .fchip.freechip{color:var(--free); border-color:var(--free-line); background:var(--free-soft); font-weight:800}
  .fchip.freechip[aria-pressed="true"]{background:var(--free); color:#fff; border-color:var(--free)}
  .fchip.freechip[aria-pressed="true"] .cdot{background:#fff !important}
  #freeFilter{margin-bottom:2px}
  .codechip{font-family:"JetBrains Mono",monospace; font-size:11.5px; color:var(--green);
    background:var(--bg2); border:1px solid var(--line); border-radius:5px; padding:1px 5px}
  /* Wortmarke ist länger als "TVFUSSBALL" – auf schmalen Geräten runterskalieren */

  .lh-txt.lang{font-size:13.5px; line-height:1.6}
  .lh-flags{display:flex; flex-wrap:wrap; gap:6px; margin:10px 0 0}
  .lh-flag{font-size:11px; font-weight:700; padding:3px 9px; border-radius:var(--r-tag);
    background:var(--w1); border:1px solid var(--c1); color:var(--c1)}
  html[data-theme="dark"] .lh-flag{background:var(--w1d); filter:brightness(1.3)}
  .lh-reden{margin:11px 0 0; padding:10px 12px; border-radius:var(--r-tag);
    background:var(--bg2); border:1px solid var(--line);
    font-size:12.5px; color:var(--muted); line-height:1.5}
  .lh-reden b{color:var(--ink); font-weight:700}

  /* Ampel für "Später nachsehen" */
  .spdot{display:inline-block; width:8px; height:8px; border-radius:1px;
    margin-right:8px; vertical-align:middle; background:var(--line2)}
  .arow.sp-sicher .spdot{background:var(--free)}
  .arow.sp-regel .spdot{background:var(--wm)}
  .arow.sp-unsicher .spdot{background:var(--line2)}
  .arow.sp-sicher .aval,.arow.sp-regel .aval,.arow.sp-unsicher .aval{
    font-weight:500; line-height:1.5}

  /* --- IMDb ------------------------------------------------------------ */
  .imdb{display:inline-flex; align-items:center; gap:5px; font-family:"JetBrains Mono",monospace;
    font-size:9.5px; font-weight:700; padding:2.5px 6px; border-radius:var(--r-tag);
    border:1px solid rgba(199,155,0,.45); color:#8A6A00; background:rgba(245,197,24,.16); white-space:nowrap}
  .imdb b{font-family:"Archivo",sans-serif; font-weight:900; font-size:9px; letter-spacing:.02em}
  html[data-theme="dark"] .imdb{color:#F5C518; border-color:rgba(245,197,24,.42); background:rgba(245,197,24,.12)}
  .agebox .votes{color:var(--faint); font-size:12px; font-weight:400}
  .agebox .aval a{color:var(--c1); text-decoration:underline; text-underline-offset:2px}

  /* Empfangs-Hinweis in der Senderliste */
  .chrow .chnote{display:block; font-size:11px; color:var(--faint); font-weight:400; margin-top:2px; line-height:1.4}
  .chrow{align-items:flex-start}
  .chrow .tag{margin-top:1px}

  /* --- Loader: hüpfende Bausteine -------------------------------------- */
  .hop{display:flex; align-items:flex-end; gap:9px; height:52px}
  .hop i{width:17px; height:17px; border-radius:var(--r-ctl); display:block;
    animation:hopjump .56s cubic-bezier(.32,0,.68,1) infinite alternate}
  .hop i:nth-child(1){background:#FF6B35; animation-delay:0s}
  .hop i:nth-child(2){background:#F72585; animation-delay:.10s}
  .hop i:nth-child(3){background:#FFB703; animation-delay:.20s}
  .hop i:nth-child(4){background:#00A6A6; animation-delay:.30s}
  @keyframes hopjump{0%{transform:translateY(0)}100%{transform:translateY(-24px)}}
  @media (prefers-reduced-motion:reduce){ .hop i{animation:none} }

  /* Crosslink-Marke */
  .crosslink .cl-ic{font-family:"Archivo",sans-serif; font-weight:900; font-style:italic;
    font-size:15px; letter-spacing:-.02em; background:#2563EB; color:#fff; border-color:#2563EB}
  html[data-theme="dark"] .crosslink .cl-ic{background:#5B8CFF; color:#0A0D14; border-color:#5B8CFF}

  /* --- Retro-Kennzeichnung --------------------------------------------- */
  .retro{display:inline-flex; align-items:center; font-family:"JetBrains Mono",monospace;
    font-size:9.5px; font-weight:700; padding:2.5px 6px; border-radius:var(--r-tag);
    border:1px solid rgba(122,44,191,.42); color:#6D28A8; background:rgba(122,44,191,.10); white-space:nowrap}
  html[data-theme="dark"] .retro{color:#C77DFF; border-color:rgba(199,125,255,.40); background:rgba(199,125,255,.13)}
  /* Filterchips: eine Familie, ein System.
     Grundzustand neutral, aktiv immer im Seiten-Orange. Die beiden
     Sonderfilter unterscheiden sich nur über ein kleines Zeichen davor,
     nicht über eigene Farbwelten. */
  .fchip{border-radius:var(--r-ctl) !important; background:var(--surface);
    border:1px solid var(--line2); color:var(--ink); font-weight:650}
  .fchip:hover{border-color:#F1571A; color:#C94108}
  html[data-theme="dark"] .fchip:hover{color:#FF9A5C; border-color:rgba(255,122,61,.5)}
  .fchip[aria-pressed="true"]{
    background:linear-gradient(135deg,#FF7A3D,#F1571A 55%,#D8430C) !important;
    border-color:#D8430C !important; color:#FFF3E8 !important}
  .fchip .fcount{opacity:.55}
  .fchip[aria-pressed="true"] .fcount{opacity:.8}
  .fchip.retrochip{background:var(--surface); border-color:var(--line2); color:var(--ink); font-weight:650}
  .fchip.retrochip[aria-pressed="true"]{
    background:linear-gradient(135deg,#FF7A3D,#F1571A 55%,#D8430C); border-color:#D8430C; color:#FFF3E8}
  html[data-theme="dark"] .fchip.retrochip{background:var(--surface); border-color:var(--line2); color:var(--ink)}
  html[data-theme="dark"] .fchip.retrochip[aria-pressed="true"]{color:#FFF3E8}
  .fchip.leer{opacity:.4}

  .testbanner{border:1px dashed var(--line2); border-radius:var(--r); background:var(--bg2);
    padding:12px 14px; margin-bottom:9px; font-size:12.5px; color:var(--muted); line-height:1.55}
  .testbanner b{display:block; font-family:"Archivo",sans-serif; font-size:14px;
    color:var(--ink); margin-bottom:4px}
  .tipptext{font-size:13.5px; color:var(--ink); line-height:1.55; margin:9px 0 0}
  .tipphaken{font-size:12.5px; color:var(--muted); line-height:1.5; margin:7px 0 0}
  .tipphaken b{color:var(--ink); font-weight:700}
  .tippvon{margin-top:8px; }
  .unbenutzt-tippvon{font-size:11.5px; color:var(--faint); font-style:italic}
  .tipprow .mmeta{margin-top:7px}

  /* --- Anmeldung ------------------------------------------------------- */
  .loginbtn{border:1px solid var(--line2); background:var(--bg2); color:var(--ink);
    border-radius:var(--r-ctl); padding:6px 12px; font-size:12.5px; font-weight:700}
  .loginbtn:hover{border-color:var(--green-line); color:var(--green)}
  .testnote{background:var(--wm-soft); border:1px solid var(--wm-line); border-radius:var(--r-tag);
    padding:10px 12px; font-size:12.5px; color:var(--wm) !important; line-height:1.5; margin-bottom:14px}
  .field{display:block; margin-bottom:11px}
  .field span{display:block; font-size:11.5px; font-weight:700; letter-spacing:.05em;
    text-transform:uppercase; color:var(--muted); margin-bottom:5px}
  .field input{width:100%; font:inherit; font-size:14px; color:var(--ink);
    background:var(--bg2); border:1.5px solid var(--line2); border-radius:var(--r-tag);
    padding:9px 11px}
  .field input:focus-visible{outline:2px solid var(--green); outline-offset:1px}
  .loginrow{display:flex; gap:9px; margin-top:15px}
  .loginsubmit{flex:1; border:none; background:var(--green); color:var(--on-accent);
    border-radius:var(--r-ctl); padding:10px 14px; font-size:13px; font-weight:800}
  .loginreg{flex:1; border:1px solid var(--line); background:var(--bg2); color:var(--faint);
    border-radius:var(--r-ctl); padding:10px 14px; font-size:13px; font-weight:700; cursor:not-allowed}
  .reghint{font-size:11.5px; color:var(--faint); margin-top:9px}

  /* --- letzte Rundungsreste (steht bewusst am Ende der Kaskade) -------- */
  .logo .tv{border-radius:var(--r-tag);
    background:linear-gradient(135deg,#FF7A3D,#F1571A 55%,#D8430C) !important;
    color:#FFF3E8 !important; box-shadow:none !important}
  html[data-theme="dark"] .logo .tv{
    background:linear-gradient(135deg,#FF8A50,#F1571A 60%,#C94108) !important}
  .crosslink .cl-ic,.crosslink .cl-go{border-radius:var(--r-ctl)}
  .row .time{border-radius:0}
  .row .morebtn{border-radius:var(--r-tag)}
  .stick{border-radius:var(--r-ctl)}
  .opt input{border-radius:var(--r-tag)}
  .vthumb{border-radius:0}
  .feat{border-radius:var(--r-tag)}
"""

NAV = [
    ("live", "index.html", "Heute",
     '<rect x="2.5" y="4.5" width="19" height="12.5" rx="2.6"/><path d="M8 20.5h8M12 17v3.5"/>'
     '<path d="M10.7 9.1l3.4 2-3.4 2z" fill="currentColor" stroke="none"/>'),
    ("mediathek", "mediathek-kinder.html", "Streaming & Kino",
     '<rect x="3" y="4.6" width="18" height="14.8" rx="2"/>'
     '<path d="M10.3 9.2l4.6 2.8-4.6 2.8z" fill="currentColor" stroke="none"/>'),
]

CHEV = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
        'stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>')


def nav_html(active):
    return ""                         # Bottom-Navigation komplett entfernt
    if active == "live":
        return ""
    rows = []
    for tab, href, label, icon in NAV:
        if tab == "mediathek":
            continue                  # eigener Tab wird nicht angezeigt
        rows.append(
            f'  <a class="navitem" role="tab" aria-selected="{"true" if tab == active else "false"}" '
            f'data-tab="{tab}" href="{href}">\n'
            f'    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" '
            f'stroke-linecap="round" stroke-linejoin="round">{icon}</svg>\n'
            f'    <span data-i18n="{"nav_live" if tab=="live" else "nav_med"}">{label}</span></a>')
    return ('<nav class="bottomnav" role="tablist" aria-label="Bereiche">\n'
            + "\n".join(rows) + "\n</nav>")


def seosec(icon, title, sub, paragraphs):
    ps = "\n      ".join(f"<p>{p}</p>" for p in paragraphs)
    return f"""    <details class="wmsec">
      <summary>
        <span class="wm-secico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{icon}</svg></span>
        <span class="wm-sectt"><b>{title}</b><span>{sub}</span></span>
        <span class="wmchev">{CHEV}</span>
      </summary>
      <div class="wmsec-body">
      {ps}
      </div>
    </details>"""


SHELL = """<!DOCTYPE html>
<html data-build="{build}" lang="de" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{domain}/{canon}">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<meta name="theme-color" content="#F7F5F0">
<meta property="og:url" content="{domain}/{canon}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{brand}">
<meta property="og:locale" content="de_DE">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{domain}/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{brand}: Was läuft heute für Kinder?">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{domain}/og-image.jpg">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800;900&family=Barlow+Condensed:wght@600;700&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="icon" href="favicon.ico" sizes="48x48">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
<link rel="preload" as="image" href="headerbild.png" fetchpriority="high">
{head_extra}<style>
{css}
</style>
{site_ld}
{seo_ld}
{cat_ld}
</head>
<body data-page="{page}">

<div class="loader" id="loader" aria-hidden="true">
  <div class="hop"><i></i><i></i><i></i><i></i></div>
  <div class="ltxt">LÄDT …</div>
</div>

<header>
  <div class="hbar">
    <a class="logo" href="index.html" aria-label="{brand} – zur Startseite"><img class="logowort" src="logo-schriftzug.png" alt="TVKinderprogramm" height="44" decoding="async" onerror="this.hidden=true"><img class="logobanner" src="headerbild.png" width="518" height="160" fetchpriority="high" decoding="async" alt="TVKinderprogramm.de: Kinderprogramm im Überblick"></a>
  </div>
</header>

<div class="wrap">
  <section class="tabpane active" id="pane-{page}" role="tabpanel">
{main}
  </section>

  <footer>
    <nav class="footnav" aria-label="Seiten"><a href="index.html">Kinderprogramm heute</a><span>·</span><a href="mediathek-kinder.html">Kinderserien streamen &amp; Kino</a><span>·</span><a href="memory.html">Memory online spielen</a></nav>
    <a href="#" data-legal="imprint" data-i18n="imprint">Impressum</a>
    <a href="#" data-legal="privacy" data-i18n="privacy">Datenschutz</a>
    <a href="#" data-legal="about" data-i18n="about">Über uns</a>
    <span class="lnote" id="attrib"></span>
    <span class="lnote" id="langHint"></span>
    <span class="lnote" data-i18n="tzhint">Alle Sendezeiten in deutscher Zeit.</span>
    <span class="lnote" data-i18n="fussnote">{brand} überträgt selbst keine Sendungen. Wir verweisen nur auf legale Sender und Mediatheken und betten ausschließlich offizielle, freigegebene Videos ein. Altersempfehlungen sind redaktionell und ersetzen keine FSK-Freigabe. Programmangaben ohne Gewähr — verbindlich ist das Programm des Senders.</span>
  </footer>

  <div class="legal-ov" id="loginOv" aria-hidden="true">
    <div class="legal-card" role="dialog" aria-modal="true" aria-labelledby="loginTitle">
      <div class="legal-head"><h3 id="loginTitle" data-i18n="anmelden">Anmelden</h3><button class="legal-x" id="loginClose" aria-label="Schließen">✕</button></div>
      <div class="legal-body">
        <p class="testnote" data-i18n="test_note">Die Nutzerverwaltung befindet sich in der Testphase.</p>
        <label class="field"><span data-i18n="benutzer">Benutzername</span>
          <input type="text" id="loginUser" autocomplete="username" placeholder="benutzername"></label>
        <label class="field"><span data-i18n="passwort">Passwort</span>
          <input type="password" id="loginPass" autocomplete="current-password" placeholder="••••••••"></label>
        <div class="loginrow">
          <button class="loginsubmit" id="loginGo" data-i18n="anmelden">Anmelden</button>
          <button class="loginreg" disabled data-i18n="registrieren">Registrieren</button>
        </div>
        <p class="reghint" data-i18n="reg_hint">Registrierung ist während der Testphase deaktiviert.</p>
      </div>
    </div>
  </div>

  <div class="legal-ov" id="legalOv" aria-hidden="true">
    <div class="legal-card" role="dialog" aria-modal="true" aria-labelledby="legalTitle">
      <div class="legal-head"><h3 id="legalTitle"></h3><button class="legal-x" id="legalClose" aria-label="Schließen">✕</button></div>
      <div class="legal-body" id="legalBody"></div>
    </div>
  </div>
</div>

{nav}

<div class="consent hide" id="consent">
  <p data-i18n="consent">Wir messen anonym, welche Seiten genutzt werden — cookiefrei über Cloudflare Web Analytics. Weitere Dienste laden wir erst nach deiner Einwilligung.</p>
  <div class="cbtns">
    <button id="consentNo" data-i18n="c_no">Ablehnen</button>
    <button class="ok" id="consentYes" data-i18n="c_yes">Einverstanden</button>
  </div>
</div>

<div class="toast" id="toast" role="status" aria-live="polite"></div>

<script>
{data_js}

{shell_js}

{page_js}
</script>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<!-- Cloudflare Web Analytics — cookiefrei, kein Local Storage, keine Fingerprints -->
<script defer type="module" src="https://static.cloudflareinsights.com/beacon.min.js"
  data-cf-beacon='{{"token": "60f94c580ceb4df180fd401c94267269"}}'></script>
<!-- Ende Cloudflare Web Analytics -->
</body>
</html>
"""

SHELL_JS = r"""
/* =================================================================== */
/*  SHELL — Theme, Land, Sprache, Consent, Recht, Toast, Zeilen        */
/* =================================================================== */
const $  = (s,r)=> (r||document).querySelector(s);
const $$ = (s,r)=> Array.from((r||document).querySelectorAll(s));
const LS = {
  get(k,d){ try{ const v=localStorage.getItem(k); return v===null?d:JSON.parse(v); }catch(e){ return d; } },
  set(k,v){ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(e){} }
};

const MARKETS = [{c:"DE",f:"\uD83C\uDDE9\uD83C\uDDEA",n:"Deutschland"},
                 {c:"AT",f:"\uD83C\uDDE6\uD83C\uDDF9",n:"Österreich"},
                 {c:"CH",f:"\uD83C\uDDE8\uD83C\uDDED",n:"Schweiz"}];

const GROUPS = [
  {id:"all", k:"f_alle"},
  {id:"a3",  k:"f_a3",  color:"#15A554"},
  {id:"a6",  k:"f_a6",  color:"#2563EB"},
  {id:"a10", k:"f_a10", color:"#B7791F"}
];
const GENRES = ["Zeichentrick","Anime","Serie","Jugendserie","Fantasyserie","Wissen","Vorlesen","Musik & Tanz","Film"];

/* =================================================================== */
/*  Sprachen — Bedienoberfläche zweisprachig, Inhalte bleiben deutsch   */
/*  (es geht um deutsches Fernsehen; Titel und Beschreibungen zu        */
/*   übersetzen wäre irreführend)                                       */
/* =================================================================== */
const I18N = {
 de:{
  nav_live:"Heute", nav_med:"Streaming & Kino",
  land:"Land wählen", en_hint:"Interface switched to English",
  such_live:"Sendung, Folge oder Sender suchen …",
  such_med:"Titel, Genre oder Anbieter suchen …",
  f_alle:"Alle", f_a3:"Vorschule · 3–5", f_a6:"6–9 Jahre", f_a10:"10–13 Jahre",
  f_retro:"Kennst du noch?", f_tipp:"Elterntipp",
  o_free:"Nur kostenlos", o_past:"Vergangene anzeigen", o_imdb:"Nur IMDb über 8",
  o_sort:"Sortieren", s_az:"A – Z", s_jahr_ab:"Jahr, neueste zuerst",
  s_jahr_auf:"Jahr, älteste zuerst", s_alter:"Alter, aufsteigend", s_imdb:"IMDb-Bewertung",
  von:"von", ausgeblendet:"ausgeblendet", tipps_n:"Tipps",
  laeuft:"läuft", vorbei:"vorbei", ab:"ab", kostenlos:"Kostenlos", nichtfrei:"nicht frei",
  wo:"Wo es läuft", kein_sender:"Noch kein Sender hinterlegt",
  alter:"Altersempfehlung", redaktionell:"redaktionell", jahren:"Jahren",
  laufzeit:"Laufzeit", werbung:"Werbung", werbefrei:"werbefrei",
  mit_werbung:"mit Werbeunterbrechungen", nachsehen:"Später nachsehen",
  nachsehen_ja:"ja, in der Mediathek", folgen_abrufbar:"Folgen abrufbar",
  nachsehen_wahrsch:"wahrscheinlich ja — öffentlich-rechtliche Sender stellen ihr Programm meist für 7 bis 30 Tage online",
  nachsehen_nein:"nicht bekannt — für diesen Sender haben wir noch keine Mediathek-Quelle",
  hinsehen:"hinsehen", ansehen:"ansehen", imdb_von:"von 10", imdb_stimmen:"bei %s Stimmen",
  imdb_ansehen:"bei IMDb ansehen", imdb_nach:"bei IMDb nachschlagen",
  kennst:"Kennst du noch?", passt:"Passt das zu meinem Kind?", elterncheck:"Passt das zu meinem Kind? Der Eltern-Check",
  keine_einschaetzung:"Noch keine Einschätzung hinterlegt.",
  weitere_laender:"Sender in weiteren Ländern",
  kalender:"In Kalender", teilen:"Teilen", gemerkt:"gemerkt", entfernt:"entfernt",
  link_kopiert:"Link kopiert", termin:"Termin heruntergeladen",
  heute:"HEUTE", morgen:"MORGEN", nichts:"Nichts gefunden.",
  leer_tt:"Keine Sendungen für diese Auswahl", leer_tx:"Anderen Filter wählen.",
  weitere_anb:"Weitere Anbieter", in_impl:"in Implementierung",
  prov_note:"Für diese Anbieter ist noch keine Quelle angebunden — in Implementierung. Ihre Inhalte sind bis dahin ausgeblendet.",
  anmelden:"Anmelden", benutzer:"Benutzername", passwort:"Passwort",
  registrieren:"Registrieren", reg_hint:"Registrierung ist während der Testphase deaktiviert.",
  test_note:"Die Nutzerverwaltung befindet sich in der Testphase. Anmelden können sich derzeit nur Konten, die wir manuell angelegt haben.",
  tipp_tt:"Elterntipps",
  tipp_tx:"Empfehlungen aus der Community für Dinge, die unsere automatischen Quellen nicht sehen — kostenlose YouTube-Kanäle, Podcasts, Einstellungen. Die Nutzerverwaltung ist in der Testphase; bis eigene Einsendungen freigeschaltet sind, stammen die Tipps aus der Redaktion.",
  dagegen:"Was dagegen spricht:",
  imprint:"Impressum", privacy:"Datenschutz", about:"Über uns",
  consent:"Wir messen anonym, welche Seiten genutzt werden — cookiefrei über Cloudflare Web Analytics. Weitere Dienste laden wir erst nach deiner Einwilligung.",
  c_no:"Ablehnen", c_yes:"Einverstanden",
  anbieter_h:"Die Anbieter", anbieter_s:"Kinderbereich im Vergleich",
  kino_h2:"Aktuell im Kino", kino_s:"Kinderfilme auf der großen Leinwand",
  kino_zeigen:"Filme anzeigen", kino_trailer:"Trailer ansehen",
  kino_ab:"Kinostart", kino_offen:"FSK folgt", alter_alle:"Alle",
  kino_zu:"Ausblenden", anb_zu:"Ausblenden", kat_zu:"Einklappen", tipp_zu:"Ausblenden",
  hero_kick:"Kinderprogramm heute",
  hero_h1:"Was läuft heute – <em>und passt zu meinem Kind?</em>",
  hero_lead:"Sendezeiten, Altersempfehlungen, kostenlose Mediatheken und aktuelle Kinderfilme – ruhig, übersichtlich und ohne Suchstress.",
  stat_sender:"Kindersender im Blick", stat_heute:"Sendungen heute",
  stat_frei:"Elterntipps aus der Redaktion", stat_alter:"Jahre Altersfilter",
  feat_kick:"Streaming & Kino", feat_h:"Wenn im TV gerade nichts passt.",
  feat_s:"Kostenlose Mediathek-Tipps und die aktuellen Kinderfilme im Kino – in einem eigenen Bereich.",
  feat_cta:"Jetzt entdecken",
  spiel_h:"Spiele-Ecke: Memory ist da!",
  spiel_s:"Paare finden mit Tieren, Fahrzeugen und Leckereien – kostenlos im Browser spielen.",
  spiel_bald:"Neu",
  jetzt_h2:"Jetzt & als Nächstes",
  jetzt_s:"Die wichtigsten Sendungen der nächsten Stunden",
  jetzt_alle:"%s weitere anzeigen →",
  alter_a3:"3–5 Jahre", alter_a6:"6–9 Jahre", alter_a10:"10–13 Jahre",
  slide_tvf:"Für die Großen: alle Spiele heute auf TVFussball.de",
  slide_mm:"Kurze Pause? Mühle Meister – kostenlos im Play Store",
  slide_mem:"Spiele-Ecke: Memory jetzt kostenlos spielen",
  fussnote:"TVKinderprogramm.de überträgt selbst keine Sendungen. Wir verweisen nur auf legale Sender und Mediatheken und betten ausschließlich offizielle, freigegebene Videos ein. Altersempfehlungen sind redaktionell und ersetzen keine FSK-Freigabe. Programmangaben ohne Gewähr — verbindlich ist das Programm des Senders.",
  jetzt_frei:"Gerade kostenlos",
  tzhint:"Alle Sendezeiten in deutscher Zeit (Europe/Berlin).",
  lv_jetzt:"im Browser öffnen", lv_konto:"kostenlos bei Joyn, Konto nötig", lv_abo:"über RTL+, Abo nötig",
  intro_idx:"<b>TVKinderprogramm.de</b> beantwortet eine einfache Frage: <b>Was läuft heute für Kinder im TV?</b> Alle Kindersendungen mit Altersempfehlung, Eltern-Check und kostenlosen Mediathek-Links.",
  cl_b:"Und für die Großen?",
  toast_bald:"Disney+, Netflix & Co. folgen bald",
  int_ab:"Abenteuer & Action", int_ti:"Tiere & Natur", int_ma:"Magie & Fantasie",
  int_la:"Lachen & Quatsch", int_wi:"Wissen & Entdecken",
  tipps_h2:"Mediathek-Tipps", mehr5:"5 weitere zeigen",
  wenig_tipps:"Dazu haben wir gerade nur %s Tipps: hier noch Ideen aus ähnlichen Kategorien",
  alle_gezeigt:"Das war's: schau morgen wieder vorbei!",
  grp_alter:"Alter", grp_genre:"Genre", grp_sonst:"Sonstiges", grp_suche:"Suche",
  filter_zeigen:"Filter & Suche", tipps_start:"5 Tipps anzeigen",
  mm_b:"Kurze Pause?", mm_s:"Mühle Meister: der Brettspiel-Klassiker als kostenlose App im Play Store",
  intro_med:"<b>Kostenlose Kinderserien und Kinderfilme</b> aus den Mediatheken von KiKA, ARD, ZDF & Co.: mit Altersempfehlung und Eltern-Check. Dazu: die aktuellen Kinderfilme im Kino.",
  kat_start:"Katalog anzeigen", mehr30:"%s weitere anzeigen", anb_start:"Vergleich anzeigen",
  kat_h2:"Kostenfreie Mediathek-Inhalte", titel_n:"Titel", tipp_l:"Tipp", dagegen:"Was dagegen spricht:",
  seo_med_h:"Kinderserien und Kinderfilme kostenlos in den Mediatheken",
  seo_med_1:"TVKinderprogramm.de sammelt Kinderserien und Kinderfilme, die in den kostenlosen Mediatheken der öffentlich-rechtlichen Sender abrufbar sind: im KiKA-Player, in der ARD Mediathek, bei ZDFtivi und bei 3sat. Jeder Titel trägt eine redaktionelle Altersempfehlung (ab 3, ab 6 oder ab 10 Jahren), dazu Folgenzahl, Laufzeit und, wo vorhanden, die IMDb-Bewertung mit Stimmenzahl.",
  seo_med_2:"Die Angebote der öffentlich-rechtlichen Mediatheken sind werbefrei und ohne Anmeldung nutzbar: ein Unterschied zu YouTube und den Apps der Privatsender. Über die Filter oben lassen sich Titel nach Altersgruppe und Interessen wie Tiere und Natur, Wissen und Entdecken oder Magie und Fantasie eingrenzen. Die Tipps werden bei jedem Besuch neu gemischt.",
  seo_med_3:"Verfügbarkeiten in den Mediatheken ändern sich laufend; verbindlich ist stets die Angabe des jeweiligen Anbieters. Kostenpflichtige Dienste wie Disney+, Netflix und Prime Video werden derzeit nicht gelistet, folgen aber. Das laufende Fernsehprogramm der Kindersender zeigt die Startseite.",
  cl_s:"Alle Spiele heute im TV, Stream und Radio: auf TVFussball.de",
  inhalt_de:""
 },
 en:{
  nav_live:"Today", nav_med:"Streaming & cinema",
  land:"Choose country", en_hint:"Programme details stay in German",
  such_live:"Search shows, episodes or channels …",
  such_med:"Search titles, genres or providers …",
  f_alle:"All", f_a3:"Preschool · 3–5", f_a6:"Ages 6–9", f_a10:"Ages 10–13",
  f_retro:"Remember this?", f_tipp:"Parent tip",
  o_free:"Free only", o_past:"Show past", o_imdb:"IMDb above 8",
  o_sort:"Sort", s_az:"A – Z", s_jahr_ab:"Year, newest first",
  s_jahr_auf:"Year, oldest first", s_alter:"Age, ascending", s_imdb:"IMDb rating",
  von:"of", ausgeblendet:"hidden", tipps_n:"tips",
  laeuft:"on air", vorbei:"ended", ab:"age", kostenlos:"Free", nichtfrei:"not free",
  wo:"Where to watch", kein_sender:"No channel on file yet",
  alter:"Age guidance", redaktionell:"editorial", jahren:"and up",
  laufzeit:"Running time", werbung:"Advertising", werbefrei:"ad-free",
  mit_werbung:"with commercial breaks", nachsehen:"Catch up later",
  nachsehen_ja:"yes, in the media library", folgen_abrufbar:"episodes available",
  nachsehen_wahrsch:"most likely — German public broadcasters usually keep their programmes online for 7 to 30 days",
  nachsehen_nein:"unknown — no media library source for this channel yet",
  hinsehen:"open", ansehen:"watch", imdb_von:"of 10", imdb_stimmen:"from %s votes",
  imdb_ansehen:"view on IMDb", imdb_nach:"look up on IMDb",
  kennst:"Remember this?", passt:"Is this right for my child?", elterncheck:"Is this right for my child? The parent check",
  keine_einschaetzung:"No assessment on file yet.",
  weitere_laender:"Channels in other countries",
  kalender:"Add to calendar", teilen:"Share", gemerkt:"saved", entfernt:"removed",
  link_kopiert:"Link copied", termin:"Calendar file downloaded",
  heute:"TODAY", morgen:"TOMORROW", nichts:"Nothing found.",
  leer_tt:"No programmes for this selection", leer_tx:"Try a different filter.",
  weitere_anb:"More providers", in_impl:"being implemented",
  prov_note:"No source connected for these providers yet — being implemented. Their content is hidden until then.",
  anmelden:"Sign in", benutzer:"Username", passwort:"Password",
  registrieren:"Register", reg_hint:"Registration is disabled during the test phase.",
  test_note:"User accounts are in a test phase. Only accounts we created manually can sign in at the moment.",
  tipp_tt:"Parent tips",
  tipp_tx:"Community recommendations for things our automated sources cannot see — free YouTube channels, podcasts, settings. User accounts are in a test phase; until submissions open up, the tips come from the editorial team.",
  dagegen:"What speaks against it:",
  imprint:"Imprint", privacy:"Privacy", about:"About",
  consent:"We measure anonymously which pages are used — cookie-free via Cloudflare Web Analytics. Any further services load only after your consent.",
  c_no:"Decline", c_yes:"Accept",
  anbieter_h:"The providers", anbieter_s:"kids sections compared",
  kino_h2:"Now in cinemas", kino_s:"kids films on the big screen",
  kino_zeigen:"Show films", kino_trailer:"Watch trailer",
  kino_ab:"In cinemas from", kino_offen:"rating pending", alter_alle:"All",
  kino_zu:"Hide", anb_zu:"Hide", kat_zu:"Collapse", tipp_zu:"Hide",
  hero_kick:"Kids TV today",
  hero_h1:"What's on today – <em>and what suits my child?</em>",
  hero_lead:"Air times, age recommendations, free media libraries and current kids films – calm, clear and without the search stress.",
  stat_sender:"kids channels covered", stat_heute:"shows today",
  stat_frei:"parent tips from the editors", stat_alter:"years of age filter",
  feat_kick:"Streaming & cinema", feat_h:"When nothing on TV fits right now.",
  feat_s:"Free library tips and the current kids films in cinemas – in their own section.",
  feat_cta:"Explore now",
  spiel_h:"Games corner: Memory is here!",
  spiel_s:"Find pairs with animals, vehicles and treats – free in your browser.",
  spiel_bald:"New",
  jetzt_h2:"Now & up next",
  jetzt_s:"The most important shows of the next hours",
  jetzt_alle:"%s more →",
  alter_a3:"3–5 years", alter_a6:"6–9 years", alter_a10:"10–13 years",
  slide_tvf:"For the grown-ups: all matches today on TVFussball.de",
  slide_mm:"Quick break? Mühle Meister – free on Google Play",
  slide_mem:"Games corner: play Memory for free now",
  fussnote:"TVKinderprogramm.de does not broadcast anything itself. We only point to legal channels and media libraries and embed officially released videos. Age guidance is editorial and does not replace an official rating. Schedules without guarantee — the channel's own listing is binding.",
  jetzt_frei:"Free right now",
  tzhint:"All broadcast times in German local time (Europe/Berlin).",
  lv_jetzt:"open in browser", lv_konto:"free on Joyn, account required", lv_abo:"via RTL+, subscription required",
  intro_idx:"<b>TVKinderprogramm.de</b> answers one simple question: <b>What is on TV for kids today?</b> Every children's show with an age recommendation, a parent check and free media-library links.",
  cl_b:"And for the grown-ups?",
  toast_bald:"Disney+, Netflix & Co. are coming soon",
  int_ab:"Adventure & Action", int_ti:"Animals & Nature", int_ma:"Magic & Fantasy",
  int_la:"Laughs & Silliness", int_wi:"Learning & Discovery",
  tipps_h2:"Library tips", mehr5:"Show 5 more",
  wenig_tipps:"We only have %s picks for that right now: adding ideas from similar categories",
  alle_gezeigt:"That's all: check back tomorrow!",
  grp_alter:"Age", grp_genre:"Genre", grp_sonst:"More", grp_suche:"Search",
  filter_zeigen:"Filter & search", tipps_start:"Show 5 tips",
  mm_b:"Quick break?", mm_s:"Mühle Meister: the classic mill board game, free on Google Play",
  intro_med:"<b>Free children's series and films</b> from the German public media libraries (KiKA, ARD, ZDF and more): with age recommendations and a parent check. Plus: kids films now showing in cinemas.",
  kat_start:"Show catalogue", mehr30:"Show %s more", anb_start:"Show comparison",
  kat_h2:"Free library content", titel_n:"titles", tipp_l:"Tip", dagegen:"What speaks against it:",
  seo_med_h:"Children's series and films, free in the German media libraries",
  seo_med_1:"TVKinderprogramm.de collects children's series and films available in the free media libraries of the German public broadcasters: the KiKA player, the ARD Mediathek, ZDFtivi and 3sat. Every title carries an editorial age recommendation (3+, 6+ or 10+), plus episode count, running time and, where available, the IMDb rating with vote count.",
  seo_med_2:"The public media libraries are ad-free and need no account: a real difference to YouTube and the commercial broadcasters' apps. Use the filters above to narrow titles by age group and interests such as animals and nature, learning and discovery, or magic and fantasy. The picks are reshuffled on every visit.",
  seo_med_3:"Media library availability changes constantly; the provider's own listing is always binding. Paid services such as Disney+, Netflix and Prime Video are not listed yet but will follow. For what is on children's TV right now, see the start page.",
  cl_s:"Every match on German TV, stream and radio: on TVFussball.de",
  inhalt_de:"Episode descriptions supplied by the German broadcasters remain in German."
 }
};
const G_EN = {"Zeichentrick":"Animation","Anime":"Anime","Serie":"Series",
  "Jugendserie":"Teen series","Fantasyserie":"Fantasy","Wissen":"Learning",
  "Vorlesen":"Bedtime story","Musik & Tanz":"Music & dance","Film":"Film"};
const TAG_EN = {"Montag":"Monday","Dienstag":"Tuesday","Mittwoch":"Wednesday",
  "Donnerstag":"Thursday","Freitag":"Friday","Samstag":"Saturday","Sonntag":"Sunday"};
window.gname = g => (LANG==="en" && G_EN[g]) ? G_EN[g] : (g||"");
window.dname = d => LANG==="en"
  ? String(d).replace(/^(\wontag|Dienstag|Mittwoch|Donnerstag|Freitag|Samstag|Sonntag)/,
      m=>TAG_EN[m]||m).replace(/^(\w+), (\d{2})\.(\d{2})\.(\d{4})$/, (a,w,t,mo,j)=>`${TAG_EN[w]||w}, ${t}/${mo}/${j}`)
  : d;

let LANG = "de";
window.t = function t(k){ return (I18N[LANG] && I18N[LANG][k]) || I18N.de[k] || k; };
function uebersetzeDaten(){
  if(typeof EN==="undefined") return;
  const an = LANG==="en";
  const feld=(o,f,en)=>{ if(o["_"+f]===undefined) o["_"+f]=o[f];
                         o[f] = (an && en!==undefined && en!==null) ? en : o["_"+f]; };
  if(typeof SHOWS!=="undefined") SHOWS.forEach(x=>{
    const de = x._title!==undefined ? x._title : x.title;
    feld(x,"title", EN.t[de]);
    feld(x,"note",  EN.n[de]);
    if(x.detail){
      if(x._detail===undefined) x._detail = x.detail;
      x.detail = (an && EN.d[de]) ? EN.d[de] : x._detail;
    }
  });
  if(typeof MEDIA!=="undefined") MEDIA.forEach(x=>{
    const de = x._title!==undefined ? x._title : x.title;
    feld(x,"title", EN.t[de]);
    feld(x,"kurz",  EN.k[de]);
  });
  if(typeof TIPPS!=="undefined" && EN.tips && EN.tips.length===TIPPS.length){
    TIPPS.forEach((x,i)=>{
      ["titel","text","haken","von","dauer"].forEach(f=>feld(x,f,EN.tips[i][f]));
    });
  }
}

function applyI18n(){
  uebersetzeDaten();
  document.documentElement.lang = LANG;
  $$("[data-i18n]").forEach(e=>{
    if(e.classList.contains("intro") || e.classList.contains("heroh1")) e.innerHTML = t(e.dataset.i18n);
    else e.textContent = t(e.dataset.i18n);
  });
  $$("[data-i18n-ph]").forEach(e=>{ e.placeholder = t(e.dataset.i18nPh); });
  const hw=$("#langHint"); if(hw) hw.textContent = LANG==="en" ? t("inhalt_de") : "";
}

const SUN='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.6v2.4M12 19v2.4M4.2 4.2l1.7 1.7M18.1 18.1l1.7 1.7M2.6 12h2.4M19 12h2.4M4.2 19.8l1.7-1.7M18.1 5.9l1.7-1.7"/></svg>';
const MOON='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4a8.4 8.4 0 1 0 10.2 10.2z"/></svg>';
function setTheme(t){ document.documentElement.setAttribute("data-theme",t);
  const b=$("#themeToggle"); if(b) b.innerHTML = t==="dark"?SUN:MOON; }
setTheme("light");

let _tt; function toast(m){ const t=$("#toast"); if(!t) return;
  t.textContent=m; t.classList.add("show"); clearTimeout(_tt);
  _tt=setTimeout(()=>t.classList.remove("show"),2200); }

const LEGAL_DE = {
  imprint:{t:"Impressum",h:`<h4>Angaben gemäß § 5 DDG (Digitale-Dienste-Gesetz)</h4>
    <p class="addr">Patrick Uhl<br>Im Frondel 19<br>55424 Münster-Sarmsheim<br>Deutschland</p>
    <h4>Kontakt</h4>
    <p>E-Mail: <a href="mailto:patrick.uhl1988@googlemail.com">patrick.uhl1988@googlemail.com</a></p>
    <h4>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h4>
    <p>Patrick Uhl (Anschrift wie oben)</p>
    <h4>Art des Angebots</h4>
    <p>TVKinderprogramm.de ist ein privat betriebenes, nicht-kommerzielles Informationsangebot.
    Es werden keine Umsätze erzielt; eine Umsatzsteuer-Identifikationsnummer besteht nicht.</p>
    <h4>Haftung für Inhalte</h4>
    <p>Die Inhalte wurden mit größter Sorgfalt erstellt. Für Richtigkeit, Vollständigkeit und
    Aktualität – insbesondere bei Sendeangaben, Altersempfehlungen und Verfügbarkeiten in den
    Mediatheken – kann keine Gewähr übernommen werden. Verbindlich ist stets das Programm des
    jeweiligen Senders.</p>
    <h4>Altersempfehlungen</h4>
    <p>Die Angaben „ab 3“, „ab 6“ und „ab 10“ sind redaktionelle Einschätzungen und keine
    Freigaben im Sinne des Jugendschutzgesetzes. Eine FSK-Freigabe besteht nur für Kinofilme
    und Bildträger, nicht für einzelne Serienfolgen.</p>
    <h4>Haftung für Links</h4>
    <p>Dieses Angebot enthält Links zu externen Websites Dritter (z. B. ARD, ZDF, KiKA, YouTube).
    Auf deren Inhalte haben wir keinen Einfluss; dafür ist stets der jeweilige Anbieter
    verantwortlich.</p>
    <h4>Urheberrecht</h4>
    <p>TVKinderprogramm.de überträgt selbst keine Sendungen und hostet keine Videoinhalte,
    sondern verweist ausschließlich auf die offiziellen, legalen Angebote der Rechteinhaber.
    Marken-, Sender- und Sendungsnamen sind Eigentum der jeweiligen Inhaber.</p>
    <h4>Schwesterprojekt</h4>
    <p>Vom selben Betreiber stammt <a href="https://tvfussball.de" target="_blank"
    rel="noopener">TVFussball.de</a>.</p>`},
  privacy:{t:"Datenschutz",h:`<h4>Überblick</h4>
    <p>Die Seite ist ohne Konto nutzbar. Gemerkte Sendungen, Land und Farbschema werden
    ausschließlich lokal im Browser gespeichert und nicht übertragen.</p>
    <h4>Reichweitenmessung</h4>
    <p>Wir nutzen <strong>Cloudflare Web Analytics</strong> (Cloudflare Inc., 101 Townsend St,
    San Francisco, CA 94107, USA). Der Dienst arbeitet <strong>ohne Cookies</strong>, ohne
    Local Storage und ohne Fingerprinting. Erhoben werden nur aggregierte Angaben wie
    aufgerufene Seite, Verweisquelle, ungefähre Herkunftsregion, Gerätetyp und Ladezeit.
    Es findet keine geräteübergreifende Wiedererkennung statt, es werden keine Profile
    gebildet und die Daten werden nicht an Dritte weitergegeben.</p>
    <p>Da kein Zugriff auf Informationen im Endgerät erfolgt, ist nach § 25 Abs. 1 TTDSG
    keine Einwilligung erforderlich. Rechtsgrundlage für die Verarbeitung ist unser
    berechtigtes Interesse an einer datensparsamen Reichweitenmessung
    (Art. 6 Abs. 1 lit. f DSGVO). Weitere Dienste laden wir erst nach ausdrücklicher
    Einwilligung über den Hinweis beim ersten Besuch.</p>
    <p>Datenschutzerklärung von Cloudflare:
    <a href="https://www.cloudflare.com/privacypolicy/" target="_blank" rel="noopener">cloudflare.com/privacypolicy</a></p>
    <h4>Kinder</h4><p>Das Angebot richtet sich an Eltern und Betreuungspersonen. Es werden keine
    Daten von Kindern erhoben, keine personalisierte Werbung ausgespielt und keine Profile gebildet.</p>`},
  about:{t:"Über uns",h:`<h4>Was diese Seite macht</h4>
    <p>Sie zeigt tagesaktuell, welche Kindersendungen wo laufen — im Fernsehen, in den Mediatheken
    und bei den Streaming-Anbietern. Mit Altersempfehlung, Laufzeit und dem Hinweis, was kostenlos ist.</p>
    <h4>Wie die Altersempfehlung entsteht</h4>
    <p>Die Angabe „ab 6" ist eine redaktionelle Einschätzung anhand von Tempo, Lautstärke und
    Konfliktdichte. Eine FSK-Freigabe gibt es nur für Kinofilme und Bildträger, nicht für
    einzelne Serienfolgen.</p>
    <h4>Was sie nicht macht</h4><p>Wir streamen nichts selbst und verlinken nur auf legale Quellen.</p>`}
};
const LEGAL_EN = {
  imprint:{t:"Imprint",h:`<h4>Information pursuant to § 5 DDG</h4>
    <p class="addr">Patrick Uhl<br>Im Frondel 19<br>55424 Münster-Sarmsheim<br>Germany</p>
    <h4>Contact</h4>
    <p>Email: <a href="mailto:patrick.uhl1988@googlemail.com">patrick.uhl1988@googlemail.com</a></p>
    <h4>Responsible for content under § 18 (2) MStV</h4><p>Patrick Uhl (address as above)</p>
    <h4>Nature of this service</h4>
    <p>TVKinderprogramm.de is a privately run, non-commercial information service. No revenue is
    generated and no VAT identification number exists.</p>
    <h4>Liability for content</h4>
    <p>Content is compiled with great care. No guarantee can be given for accuracy, completeness
    or timeliness — in particular for broadcast times, age guidance and media library
    availability. The channel's own listing is always binding.</p>
    <h4>Age guidance</h4>
    <p>The labels "age 3", "age 6" and "age 10" are editorial assessments, not classifications
    under German youth protection law.</p>
    <h4>Liability for links</h4>
    <p>This service links to external websites. We have no influence on their content; the
    respective provider is always responsible.</p>
    <h4>Copyright</h4>
    <p>TVKinderprogramm.de does not broadcast anything itself and hosts no video content. Brand,
    channel and programme names are the property of their respective owners.</p>
    <h4>Sister project</h4>
    <p>By the same operator: <a href="https://tvfussball.de" target="_blank" rel="noopener">TVFussball.de</a>.</p>`},
  privacy:{t:"Privacy",h:`<h4>Overview</h4>
    <p>The site works without an account. Saved shows, country and colour scheme are stored
    locally in your browser only and never transmitted.</p>
    <h4>Analytics</h4>
    <p>We use <strong>Cloudflare Web Analytics</strong> (Cloudflare Inc., San Francisco, USA).
    It works <strong>without cookies</strong>, without local storage and without fingerprinting.
    Only aggregated data is collected: page visited, referrer, approximate region, device type
    and load time. No cross-site tracking, no profiling, no sharing with third parties.</p>
    <p>Since no information is accessed on your device, no consent is required under
    § 25 (1) TTDSG. The legal basis is our legitimate interest in privacy-friendly audience
    measurement (Art. 6 (1) (f) GDPR). After your consent via the notice below we additionally use Google Analytics 4 (Google Ireland Ltd.), which sets cookies and processes usage data; the legal basis is Art. 6 (1) (a) GDPR and consent can be withdrawn at any time by clearing the site data.</p>
    <h4>Children</h4><p>This service is aimed at parents and carers. No data is collected from
    children, no personalised advertising is served and no profiles are built.</p>`},
  about:{t:"About",h:`<h4>What this site does</h4>
    <p>It shows which children's programmes are on where — on television, in the German public
    media libraries and on streaming services. With age guidance, running time and a note on
    what is free.</p>
    <h4>How the age guidance works</h4>
    <p>"Age 6" is an editorial assessment based on pace, volume and how much conflict a
    programme contains. An official FSK rating exists only for cinema films and physical media,
    not for individual episodes.</p>
    <h4>What it does not do</h4><p>We do not stream anything ourselves and link only to legal sources.</p>`}
};

/* Optionen als echte Checkboxen — Tastatur, Screenreader, Browser-Semantik */
function buildOptions(host, onChange){
  if(!host) return;
  host.addEventListener("change", ()=> onChange && onChange({
    free: !!(host.querySelector("#optFree")||{}).checked,
    past: !!(host.querySelector("#optPast")||{}).checked
  }));
}

function buildSpecial(host, onChange){
  if(!host) return;
  host.innerHTML =
    '<button class="fchip retrochip" data-s="retro" aria-pressed="false">Kennst du noch?</button>' +
    '<button class="fchip tippchip" data-s="tipps" aria-pressed="false">Elterntipp</button>';
  host.addEventListener("click", e=>{
    const b=e.target.closest(".fchip"); if(!b) return;
    const an = b.getAttribute("aria-pressed") !== "true";
    $$(".fchip",host).forEach(x=>x.setAttribute("aria-pressed","false"));
    b.setAttribute("aria-pressed", String(an));
    onChange && onChange(an ? b.dataset.s : "all");
  });
}

/* Zählt, wie viele Einträge ein Filter aktuell liefern würde. Chips ohne
   Treffer werden ausgegraut — sonst klickt man ins Leere und weiß nicht warum. */
window.chipCounts = null;
function updateChipCounts(host, basis){
  if(!host || !basis) return;
  host.querySelectorAll(".fchip").forEach(b=>{
    const g=b.dataset.g; if(!g) return;
    let n;
    if(g==="all") n = basis.length;
    else if(g.indexOf("genre:")===0) n = basis.filter(x=>(x.genres||[x.genre]).includes(g.slice(6))).length;
    else n = basis.filter(x=>x.grp===g).length;
    let c=b.querySelector(".fcount");
    if(!c){ c=document.createElement("span"); c.className="fcount"; b.appendChild(c); }
    c.textContent = n;
    b.classList.toggle("leer", n===0);
  });
}

function buildFilters(host, onChange){
  if(!host) return;
  host.innerHTML =
    GROUPS.map(g=>`<button class="fchip${g.id!=="all"?" tmode":""}" data-g="${g.id}" aria-pressed="${g.id==="all"}">`+
      (g.color?`<span class="cdot" style="background:${g.color}"></span>`:"")+t(g.k)+`</button>`).join("") +
    GENRES.map(x=>`<button class="fchip" data-g="genre:${x}" aria-pressed="false">${gname(x)}</button>`).join("");
  host.addEventListener("click", e=>{
    const b=e.target.closest(".fchip"); if(!b) return;
    $$(".fchip",host).forEach(x=>x.setAttribute("aria-pressed", String(x===b)));
    onChange && onChange(b.dataset.g);
  });
}

const MCHEV='<svg class="mchev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>';
const RCHEV='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg>';

/* ---------------------------------------------------------------------
   Farbpaare pro Sendung — das Pendant zu den Vereinsfarben bei TVFussball.
   Der Titel wird gehasht, daraus fällt immer dasselbe Paar. „Feuerwehrmann
   Sam" ist also jeden Tag rot-orange, „Löwenzahn" jeden Tag grün-gelb.
   Warme, kräftige Töne; alle tragen weiße Symbole mit genug Kontrast.
   --------------------------------------------------------------------- */
const PALETTE = [
  ["#FF6B35","#FFB703"],  // Mango
  ["#EF476F","#FF9E7D"],  // Himbeere
  ["#F72585","#FF8FA3"],  // Bubblegum
  ["#FB8500","#FFD166"],  // Sonnenblume
  ["#E76F51","#F4A261"],  // Terrakotta
  ["#D00000","#FF8800"],  // Feuer
  ["#8338EC","#FF6B9D"],  // Traube
  ["#00A6A6","#F6C177"],  // Lagune
  ["#2A9D8F","#E9C46A"],  // Salbei
  ["#7B2CBF","#C77DFF"],  // Pflaume
  ["#06A77D","#B7E4C7"],  // Minze
  ["#C1121F","#F9844A"],  // Kirsche
  ["#3A86FF","#8ECAE6"],  // Himmel
  ["#FF4D6D","#FFC09F"]   // Koralle
];

function hashStr(t){
  let h = 0;
  for(let i=0;i<t.length;i++){ h = (h*31 + t.charCodeAt(i)) | 0; }
  return Math.abs(h);
}
function pairFor(title){ return PALETTE[hashStr(title||"?") % PALETTE.length]; }

/* Markenfarbe so nachziehen, dass sie auf hellem bzw. dunklem Grund lesbar
   bleibt — die Logo-Farben selbst sind dafür teils zu hell oder zu dunkel. */
function _rgb(hex){ const n=parseInt(hex.slice(1),16); return [(n>>16)&255,(n>>8)&255,n&255]; }
function _hex(r,g,b){ return "#"+[r,g,b].map(v=>Math.max(0,Math.min(255,Math.round(v))).toString(16).padStart(2,"0")).join(""); }
function _lum(hex){ const [r,g,b]=_rgb(hex).map(v=>{v/=255; return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)});
  return .2126*r+.7152*g+.0722*b; }
function darkenTo(hex, maxLum){ let [r,g,b]=_rgb(hex), out=hex, i=0;
  while(_lum(out)>maxLum && i<40){ r*=.92; g*=.92; b*=.92; out=_hex(r,g,b); i++; } return out; }
function lightenTo(hex, minLum){ let [r,g,b]=_rgb(hex), out=hex, i=0;
  while(_lum(out)<minLum && i<40){ r=r+(255-r)*.12; g=g+(255-g)*.12; b=b+(255-b)*.12; out=_hex(r,g,b); i++; } return out; }

function hexA(hex, a){
  const n = parseInt(hex.slice(1),16);
  return `rgba(${(n>>16)&255},${(n>>8)&255},${n&255},${a})`;
}

/* Symbol je Genre — gefüllt, damit es bei 19px noch trägt */
const GLYPH = {
  "Zeichentrick": '<path d="M12 3.2l2.6 5.4 5.9.85-4.3 4.2 1.02 5.9L12 16.7l-5.22 2.85L7.8 13.65 3.5 9.45l5.9-.85z"/>',
  "Anime":        '<path d="M12 2l2.1 6.1L20 10l-5.9 1.9L12 18l-2.1-6.1L4 10l5.9-1.9z"/><circle cx="18.5" cy="17.5" r="2"/>',
  "Film":         '<path d="M3 6.4h18v12.2a1.6 1.6 0 0 1-1.6 1.6H4.6A1.6 1.6 0 0 1 3 18.6z"/><path d="M3.4 3.4h4l1.4 2.6h-4zM9.4 3.4h4l1.4 2.6h-4zM15.4 3.4h4l1.4 2.6h-4z"/>',
  "Wissen":       '<path d="M12 2.4A6.4 6.4 0 0 0 8.1 13.9c.5.4.8 1 .8 1.6v.6h6.2v-.6c0-.6.3-1.2.8-1.6A6.4 6.4 0 0 0 12 2.4z"/><path d="M9.2 17.6h5.6v1.5H9.2zM10.1 20.4h3.8v1.3h-3.8z"/>',
  "Vorlesen":     '<path d="M20.4 14.6A8.4 8.4 0 0 1 9.5 3.7a8.6 8.6 0 1 0 10.9 10.9z"/><path d="M17.4 3l.7 1.9 1.9.7-1.9.7-.7 1.9-.7-1.9-1.9-.7 1.9-.7z"/>',
  "Serie":        '<circle cx="12" cy="12" r="9.2"/><circle cx="9" cy="10" r="1.3" fill="#fff"/><circle cx="15" cy="10" r="1.3" fill="#fff"/><path d="M7.8 14c1 1.9 2.5 2.8 4.2 2.8s3.2-.9 4.2-2.8" stroke="#fff" stroke-width="1.7" fill="none" stroke-linecap="round"/>',
  "Jugendserie":  '<path d="M12 20.6l-1.5-1.36C5.3 14.5 2 11.5 2 7.9A5.6 5.6 0 0 1 7.6 2.3c1.8 0 3.5.84 4.4 2.16A5.4 5.4 0 0 1 16.4 2.3 5.6 5.6 0 0 1 22 7.9c0 3.6-3.3 6.6-8.5 11.34z"/>',
  "Fantasyserie": '<path d="M6.6 20.4l9-9 2 2-9 9z"/><path d="M17.8 3.2l.85 2.35 2.35.85-2.35.85-.85 2.35-.85-2.35-2.35-.85 2.35-.85zM8.2 2.6l.6 1.7 1.7.6-1.7.6-.6 1.7-.6-1.7-1.7-.6 1.7-.6z"/>',
  "Musik & Tanz": '<path d="M9.4 17.6V6.2l10-1.9v11.4"/><circle cx="6.8" cy="17.9" r="2.7"/><circle cx="16.8" cy="15.9" r="2.7"/>'
};
const GLYPH_DEFAULT = '<path d="M8.6 5.6l10 6.4-10 6.4z"/>';

/* --- Zeitrechnung -------------------------------------------------------
   Alle Sendezeiten sind deutsche Ortszeit (so liefern es die Sender).
   Der Vergleich "läuft gerade" / "vorbei" muss deshalb ebenfalls in
   deutscher Zeit stattfinden — sonst sieht jemand in Bangkok oder New York
   ein falsches Programm. Wir vergleichen Wanduhrzeiten, nicht Zeitstempel:
   das umgeht Sommerzeit-Rechnerei komplett.
   --------------------------------------------------------------------- */
function berlinJetzt(){
  const f = new Intl.DateTimeFormat("de-DE", {timeZone:"Europe/Berlin",
    year:"numeric", month:"2-digit", day:"2-digit",
    hour:"2-digit", minute:"2-digit", hour12:false});
  const p = {};
  f.formatToParts(new Date()).forEach(x=>{ if(x.type!=="literal") p[x.type]=x.value; });
  return { tag: +p.year*10000 + +p.month*100 + +p.day,
           min: (+p.hour%24)*60 + +p.minute };
}
function berlinMorgenTag(){
  /* Morgen als Kalendertag in Berlin: heutiges Datum nehmen, auf 12 Uhr UTC
     verankern, 24h addieren: robust auch an Monatsgrenzen und Zeitumstellung. */
  const n = berlinJetzt();
  const y = Math.floor(n.tag/10000), m = Math.floor(n.tag/100)%100, d = n.tag%100;
  const t = new Date(Date.UTC(y, m-1, d, 12) + 86400000);
  return t.getUTCFullYear()*10000 + (t.getUTCMonth()+1)*100 + t.getUTCDate();
}
function tagNr(day){
  const m = (day||"").match(/(\d{2})\.(\d{2})\.(\d{4})/);
  return m ? +m[3]*10000 + +m[2]*100 + +m[1] : 0;
}
function durMin(s){ const m=(s.dur||"").match(/(\d+)/); return m?+m[1]:0; }
function startMin(s){ return parseInt(s.time.slice(0,2),10)*60 + parseInt(s.time.slice(3),10); }
function endMin(s){ return startMin(s) + durMin(s); }
function isPast(s){
  const n = berlinJetzt(), t = tagNr(s.day);
  if(t < n.tag) return true;
  if(t > n.tag) return false;
  return endMin(s) <= n.min;
}
function isNow(s){
  const n = berlinJetzt();
  if(tagNr(s.day) !== n.tag) return false;
  return startMin(s) <= n.min && n.min < endMin(s);
}
function hhmm(min){
  const m = ((min % 1440) + 1440) % 1440;
  return String(Math.floor(m/60)).padStart(2,"0") + ":" + String(m%60).padStart(2,"0");
}

function imdbUrl(s){
  return s.imdb && s.imdb.id
    ? "https://www.imdb.com/title/" + s.imdb.id + "/"
    : "https://www.imdb.com/find/?q=" + encodeURIComponent(s.title) + "&s=tt";
}
function imdbBadge(s){
  if(!(s.imdb && s.imdb.r)) return "";
  return `<span class="imdb"><b>IMDb</b>${String(s.imdb.r).replace(".",",")}</span>`;
}

function sticker(s){
  const [c1,c2] = s.color2 ? [s.color, s.color2] : pairFor(s.title);
  const g = GLYPH[s.genre] || GLYPH_DEFAULT;
  return `<span class="stick" style="--s1:${c1};--s2:${c2}" aria-hidden="true">`+
         `<svg viewBox="0 0 24 24" fill="currentColor">${g}</svg></span>`;
}

const CH = c => (typeof CH_INFO!=="undefined" && CH_INFO[c.n]) ? CH_INFO[c.n] : {u:"",note:""};

/* Offizielle Livestreams je Sender. ard = ARD-Mediathek-Live, zdf = ZDF-Live,
   joyn = kostenlos mit Konto, rtlplus = Abo nötig. Ohne Eintrag: kein Link. */
const LIVESTREAM = (()=>{
  const ard=["https://www.ardmediathek.de/live",null],
        zdf=["https://www.zdf.de/live-tv",null],
        joyn=["https://www.joyn.de/live-tv","konto"],
        rtl=["https://plus.rtl.de","abo"];
  return {
    "KiKA":["https://www.kika.de/live",null],
    "Super RTL":["https://www.toggo.de/livestream",null],
    "S-RTL":["https://www.toggo.de/livestream",null],
    "Toggo plus":["https://www.toggo.de/livestream",null],
    "ARD":ard,"WDR":ard,"NDR":ard,"BR":ard,"SWR":ard,"MDR":ard,"RBB":ard,"HR":ard,"ONE":ard,
    "ZDF":zdf,"ZDFneo":zdf,"3sat":zdf,
    "arte":["https://www.arte.tv/de/live/",null],
    "SAT.1":joyn,"ProSieben":joyn,"Kabel Eins":joyn,"ProSieben Maxx":joyn,"sixx":joyn,
    "RTL":rtl,"VOX":rtl,"RTLzwei":rtl,"Nitro":rtl
  };
})();

function rowHTML(s){
  const free = (s.ch||[]).filter(c=>c.free);
  const best = free[0] || (s.ch||[])[0];
  const badge = best ? (best.free
      ? `<span class="freebest tv">▣ ${t("kostenlos")} · ${best.n}</span>`
      : `<span class="freebest pay">${t("nichtfrei")} · ${best.n}</span>`) : "";
  const sc = typeof s.score==="number" ? s.score : null;
  const col = sc===null ? "" : (sc>=70?"#15A554": sc>=45?"#f59e0b":"#E5484D");
  const past = isPast(s), now = isNow(s);
  const lv = (typeof LIVESTREAM!=="undefined" && LIVESTREAM[s.channel]) ? LIVESTREAM[s.channel] : null;

  return `
<div class="row kompaktrow${free.length?" free":""}${past?" past":""}${now?" playing":""}" data-k="${s.day}|${s.time}|${s.title}|${s.sub||""}|${s.genre||""}|${(s.ch||[]).map(c=>c.n).join(" ")}">
  <div class="rowhead statisch">
    <span class="chtile" style="--chc:${s.color||"#F2673A"}" aria-hidden="true">${(s.channel||"?").slice(0,1)}</span>
    <div class="teams">
      <div class="topline"><span class="chname">${s.channel||""}</span>${now?'<span class="livebadge"><span class="livedot"></span>'+t("laeuft")+'</span>':""}${past?'<span class="pasttag">'+t("vorbei")+'</span>':""}<span class="topzeit">${s.time}</span></div>
      <div class="t"><span>${s.title}</span></div>
      ${s.sub?`<div class="t subline">${s.sub}</div>`:""}
      <div class="meta">${s.age!==undefined?`<span class="agetag">${t("ab")} ${s.age}</span>`:""}${s.dur?`<span class="durtag">${s.dur}</span>`:""}${(s.fsk!==null&&s.fsk!==undefined)?`<span class="fsktag">FSK ${s.fsk}</span>`:""}${s.ads===false?`<span class="durtag adfrei">${t("werbefrei")}</span>`:""}${badge}<span class="comp">${gname(s.genre)}</span>${imdbBadge(s)}${s.retro?`<span class="retro">seit ${s.retro.y}</span>`:""}</div>
      ${now?`<div class="liveprog"><span style="width:${Math.min(99,Math.max(2,Math.round((berlinJetzt().min-startMin(s))/Math.max(1,durMin(s))*100)))}%"></span></div>`:""}
    </div>
  </div>
  <div class="rowfuss">
    ${sc!==null?`<div class="pcheck"><span class="pclbl">Eltern Check</span><b class="pcval" style="color:${col}">${sc}</b><span class="pcmax">/100</span><span class="pcbar"><span style="width:${sc}%;background:${col}"></span></span></div>`:'<span class="pcleer"></span>'}
    <div class="rowact">
      ${now&&lv?`<a class="schaubtn" href="${lv[0]}" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5.5l10 6.5-10 6.5z"/></svg>${t("lv_jetzt")}</a>`:""}
      <button class="minibtn" data-cal data-title="${s.title}" data-day="${s.day}" data-time="${s.time}" aria-label="${t("kalender")}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4.5" width="18" height="16" rx="2.5"/><path d="M3 9.5h18M8 2.5v4M16 2.5v4"/></svg></button>
      <button class="minibtn" data-share data-title="${s.title}" data-text="${s.title} · ${s.time} Uhr auf ${best?best.n:""} (BRANDNAME)" aria-label="${t("teilen")}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="2.6"/><circle cx="6" cy="12" r="2.6"/><circle cx="18" cy="19" r="2.6"/><path d="M8.3 10.7l7.4-4.3M8.3 13.3l7.4 4.3"/></svg></button>
    </div>
  </div>
</div>`;
}

function crosslinkHTML(){
  return `<a class="crosslink" href="https://tvfussball.de" target="_blank" rel="noopener">
  <span class="cl-ic" aria-hidden="true">TV</span>
  <span class="cl-txt"><b>${t("cl_b")}</b><span>${t("cl_s")}</span></span>
  <span class="cl-go"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l6 6-6 6"/></svg></span>
</a>`;
}

function renderBoard(board, list, emptyHTML){
  if(!list.length){ board.innerHTML = emptyHTML; return; }
  const order = (typeof DAY_ORDER!=="undefined") ? DAY_ORDER : [];
  /* Sicherheitsnetz: nach Tag und Uhrzeit sortieren, damit die Tagestrenner
     stimmen — unabhängig davon, in welcher Reihenfolge die Daten ankommen. */
  const mm = z => parseInt(z.slice(0,2),10)*60 + parseInt(z.slice(3),10);
  list = list.slice().sort((a,b)=>{
    const da=order.indexOf(a.day), db=order.indexOf(b.day);
    return (da<0?99:da)-(db<0?99:db) || mm(a.time)-mm(b.time);
  });
  let html="", day=null, crossGesetzt=false;
  list.forEach(s=>{
    if(s.day!==day){ day=s.day;
      const tn = tagNr(day), heute = berlinJetzt().tag, morgen = berlinMorgenTag();
      const tag = tn===heute  ? '<span class="dtag">'+t("heute")+'</span>'
                : tn===morgen ? '<span class="dtag tm">'+t("morgen")+'</span>' : '';
      html += `<div class="daybar">${tag}<span class="d">${dname(day)}</span><span class="ln"></span></div>`; }
    html += rowHTML(s);
  });
  board.innerHTML = html;
  markFavs();
}

function initSearch(input, board){
  if(!input||!board) return;
  input.addEventListener("input", ()=>{
    const q=input.value.trim().toLowerCase(); let hits=0;
    $$(".row",board).forEach(r=>{
      const on = !q || (r.dataset.k||"").toLowerCase().includes(q);
      r.style.display = on?"":"none"; if(on) hits++;
    });
    $$(".daybar",board).forEach(d=> d.style.display = q?"none":"");
    const e=$(".empty",board); if(e) e.style.display = (hits||!q)?"none":"";
  });
}

function markFavs(){
  const f=LS.get("tvk_favs",[]);
  $$(".favstar").forEach(s=>{
    if(f.includes(s.dataset.follow)){ s.classList.add("on"); s.textContent="★"; s.setAttribute("aria-pressed","true"); }
  });
}

function ics(d){
  const st=new Date().toISOString().replace(/[-:.]/g,"").slice(0,15)+"Z";
  const t=["BEGIN:VCALENDAR","VERSION:2.0","PRODID:-//BRANDNAME//DE","BEGIN:VEVENT",
    "UID:"+st+"@tvk","DTSTAMP:"+st,"SUMMARY:"+(d.title||"Sendung"),
    "DESCRIPTION:"+(d.day||"")+" "+(d.time||"")+" — BRANDNAME","END:VEVENT","END:VCALENDAR"].join("\r\n");
  const a=document.createElement("a");
  a.href="data:text/calendar;charset=utf-8,"+encodeURIComponent(t);
  a.download=(d.title||"sendung").replace(/\W+/g,"-").toLowerCase()+".ics"; a.click();
}

document.addEventListener("click", e=>{
  const head=e.target.closest(".rowhead");
  if(head && !head.classList.contains("statisch") && !e.target.closest(".favstar")){
    const row=head.closest(".row"); const open=row.classList.toggle("open");
    head.setAttribute("aria-expanded",String(open)); return;
  }
  const more=e.target.closest("[data-more]");
  if(more){ const open=more.getAttribute("aria-expanded")==="true";
    more.setAttribute("aria-expanded",String(!open));
    const w=more.nextElementSibling; if(w) w.classList.toggle("show",!open); return; }
  const st=e.target.closest(".favstar");
  if(st){ const f=LS.get("tvk_favs",[]); const i=f.indexOf(st.dataset.follow);
    if(i>=0){ f.splice(i,1); st.classList.remove("on"); st.textContent="☆"; st.setAttribute("aria-pressed","false"); toast(st.dataset.follow+" "+t("entfernt")); }
    else { f.push(st.dataset.follow); st.classList.add("on"); st.textContent="★"; st.setAttribute("aria-pressed","true"); toast(st.dataset.follow+" "+t("gemerkt")); }
    LS.set("tvk_favs",f); return; }
  const sh=e.target.closest("[data-share]");
  if(sh){ const d={title:sh.dataset.title,text:sh.dataset.text,url:location.origin};
    if(navigator.share) navigator.share(d).catch(()=>{});
    else { navigator.clipboard && navigator.clipboard.writeText(d.text+" "+d.url); toast(t("link_kopiert")); } return; }
  const cal=e.target.closest("[data-cal]");
  if(cal){ ics(cal.dataset); cal.classList.add("done"); toast(t("termin")); }
});
document.addEventListener("keydown", e=>{
  if((e.key==="Enter"||e.key===" ") && e.target.classList && e.target.classList.contains("favstar")){
    e.preventDefault(); e.target.click(); }
});

(function boot(){
  const tb=$("#themeToggle");
  if(tb) tb.addEventListener("click", ()=>{
    const n = document.documentElement.getAttribute("data-theme")==="dark"?"light":"dark";
    setTheme(n); LS.set("tvk_theme",n);
  });

  const seg=$(".seg.lang");
  if(seg){
    $$("button",seg).forEach(x=>x.setAttribute("aria-pressed", String(x.dataset.lang===LANG)));
    seg.addEventListener("click", e=>{
      const b=e.target.closest("button[data-lang]"); if(!b) return;
      LANG=b.dataset.lang; LS.set("tvk_lang",LANG);
      $$("button",seg).forEach(x=>x.setAttribute("aria-pressed",String(x===b)));
      applyI18n();
      if(typeof window.reRender==="function") window.reRender();
      if(LANG==="en") toast(t("en_hint"));
    });
  }
  applyI18n();

  /* Google Analytics (G-P0C7K19KSH): setzt Cookies, lädt deshalb erst
     nach Einwilligung — genau wie es der Hinweis verspricht. */
  function ladeGtag(){
    if(window.gtagGeladen) return; window.gtagGeladen=true;
    const sc=document.createElement("script");
    sc.async=true; sc.src="https://www.googletagmanager.com/gtag/js?id=G-P0C7K19KSH";
    document.head.appendChild(sc);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function(){ dataLayer.push(arguments); };
    gtag("js", new Date());
    gtag("config", "G-P0C7K19KSH");
  }
  if(LS.get("tvk_consent",null)===true) ladeGtag();

  const cb=$("#consent");
  if(LS.get("tvk_consent",null)===null){ cb.classList.remove("hide");
    const done=v=>{ LS.set("tvk_consent",v); cb.classList.add("hide");
      if(v===true) ladeGtag(); };
    $("#consentYes").addEventListener("click",()=>done(true));
    $("#consentNo").addEventListener("click",()=>done(false)); }

  const ov=$("#legalOv");
  $$("[data-legal]").forEach(a=>a.addEventListener("click", e=>{ e.preventDefault();
    const d=(LANG==="en"?LEGAL_EN:LEGAL_DE)[a.dataset.legal]; if(!d) return;
    $("#legalTitle").textContent=d.t; $("#legalBody").innerHTML=d.h;
    ov.classList.add("show"); ov.setAttribute("aria-hidden","false"); }));
  $("#legalClose").addEventListener("click", ()=>{ ov.classList.remove("show"); ov.setAttribute("aria-hidden","true"); });
  ov.addEventListener("click", e=>{ if(e.target===ov){ ov.classList.remove("show"); ov.setAttribute("aria-hidden","true"); } });
  document.addEventListener("keydown", e=>{ if(e.key==="Escape"){ ov.classList.remove("show"); ov.setAttribute("aria-hidden","true"); } });

  const lo=$("#loginOv"), lb=$("#loginOpen");
  if(lo && lb){
    const auf=()=>{ lo.classList.add("show"); lo.setAttribute("aria-hidden","false"); $("#loginUser").focus(); };
    const zu =()=>{ lo.classList.remove("show"); lo.setAttribute("aria-hidden","true"); };
    lb.addEventListener("click", auf);
    $("#loginClose").addEventListener("click", zu);
    lo.addEventListener("click", e=>{ if(e.target===lo) zu(); });
    $("#loginGo").addEventListener("click", ()=>{
      const u=$("#loginUser").value.trim();
      toast(u ? "Kein Konto für „"+u+"\u201c — Testphase" : "Bitte Benutzernamen eingeben");
    });
    document.addEventListener("keydown", e=>{ if(e.key==="Escape") zu(); });
  }

  const page=document.body.dataset.page;
  $$(".navitem").forEach(a=>a.setAttribute("aria-selected",String(a.dataset.tab===page)));

  const l=$("#loader");
  const hide=()=>setTimeout(()=>l.classList.add("hide"),200);
  if(document.readyState==="complete") hide(); else window.addEventListener("load",hide);
})();

function tippKarteIndex(tp){
  const [c1,c2]=pairFor(tp.titel);
  const vars=`--c1:${c1};--c2:${c2};--w1:${hexA(c1,.22)};--w2:${hexA(c2,.20)};--w1d:${hexA(c1,.15)};--w2d:${hexA(c2,.11)}`;
  return `
<div class="row tipprow free" style="${vars}" data-k="${tp.titel}|${tp.quelle}|${tp.von}">
  <button class="rowhead" aria-expanded="false">
    <div class="time"><span class="t-start">♥</span><span class="t-dur">${t("tipp_l")}</span></div>
    <div class="teams">
      <div class="t"><span class="stick" style="--s1:${c1};--s2:${c2}" aria-hidden="true"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 20.6l-1.5-1.36C5.3 14.5 2 11.5 2 7.9A5.6 5.6 0 0 1 7.6 2.3c1.8 0 3.5.84 4.4 2.16A5.4 5.4 0 0 1 16.4 2.3 5.6 5.6 0 0 1 22 7.9c0 3.6-3.3 6.6-8.5 11.34z"/></svg></span><span>${tp.titel}</span></div>
      <div class="meta"><span class="comp">${tp.quelle}</span><span class="agetag">${t("ab")} ${tp.alter}</span>${
        tp.kostenlos?`<span class="freebest tv">▣ ${t("kostenlos")}</span>`:""}${
        tp.dauer && tp.dauer!=="–" && tp.dauer!=="-" ? `<span class="folgen">${tp.dauer}</span>`:""}</div>
    </div>
    <div class="rh-right"><span class="chev">${RCHEV}</span></div>
  </button>
  <div class="panel"><div class="panel-in"><div class="panel-pad">
    <div class="lh">
      <p class="lh-txt">${tp.text}</p>
      <p class="lh-reden"><b>${t("dagegen")}</b> ${tp.haken}</p>
      <p class="tippvon">${tp.von}</p>
    </div>
    ${tp.url?`<div class="actrow"><a class="sharebtn" href="${tp.url}" target="_blank" rel="noopener"><span>${t("ansehen")}</span></a></div>`:""}
  </div></div></div>
</div>`;
}

/* Aufklappbarer Filterbereich (Startseite und Mediathek) */
const _ft=document.getElementById("filterToggle");
if(_ft) _ft.addEventListener("click", function(){
  const auf = this.getAttribute("aria-expanded")!=="true";
  this.setAttribute("aria-expanded", String(auf));
  document.getElementById("filterKlapp").classList.toggle("auf", auf);
});



"""


MONTH_FIX = {"01":"01","02":"02","03":"03","04":"04","05":"05","06":"06",
             "07":"07","08":"08","09":"09","10":"10","11":"11","12":"12"}


def _offset(dt):
    """Zeitzonenversatz für Europe/Berlin am jeweiligen Datum — nicht fest +02:00,
    sonst stimmen die strukturierten Daten im Winter nicht."""
    from zoneinfo import ZoneInfo
    o = dt.replace(tzinfo=ZoneInfo("Europe/Berlin")).utcoffset()
    h, m = divmod(int(o.total_seconds()) // 60, 60)
    return "%+03d:%02d" % (h, m)


def broadcast_ld():
    """schema.org/BroadcastEvent je Sendung — das Pendant zu den SportsEvent-
    Daten bei TVFussball. Google versteht damit Titel, Sender und Sendezeit."""
    import json, re, datetime
    import films_data, retro_data
    items = []

    def add(day, time, dur, title, sub, genre, channel, age):
        m = re.search(r"(\d{2})\.(\d{2})\.(\d{4})", day)
        if not m:
            return
        h, mi = time.split(":")
        start = datetime.datetime(int(m.group(3)), int(m.group(2)), int(m.group(1)),
                                  int(h), int(mi))
        end = start + datetime.timedelta(minutes=dur)
        work = "Movie" if genre == "Film" else "TVEpisode"
        items.append({
            "@type": "BroadcastEvent",
            "name": title + ((" – " + sub) if sub else ""),
            "startDate": start.strftime("%Y-%m-%dT%H:%M:00") + _offset(start),
            "endDate": end.strftime("%Y-%m-%dT%H:%M:00") + _offset(end),
            "isLiveBroadcast": False,
            "inLanguage": "de",
            "publishedOn": {"@type": "BroadcastService", "name": channel},
            "workPerformed": {"@type": work, "name": title,
                              "genre": genre,
                              "typicalAgeRange": str(age) + "-13"},
            "organizer": {"@type": "Organization", "name": BRAND, "url": DOMAIN + "/"},
        })

    for label, sender, liste in D._alle_tage():
        for r in liste:
            add(label, r[0], r[4], r[1], r[2], r[3], sender, r[5])
    for day, t, dur, title, sub, ch, age, grp, score, note in films_data.FILMS:
        add(day, t, dur, title, sub, "Film", ch, age)

    items.sort(key=lambda x: x["startDate"])
    items = items[:140]          # Umfang begrenzen, sonst wird die Seite unnötig schwer
    graph = {"@context": "https://schema.org", "@graph": items}
    return ('<script type="application/ld+json" id="tvkSeoData">'
            + json.dumps(graph, ensure_ascii=False, separators=(",", ":"))
            + "</script>")



import html as _html


def _esc(x):
    return _html.escape(str(x or ""), quote=True)


def prerender_shows():
    """Statisches HTML für #liveBoard — das, was ein Crawler ohne JavaScript liest.
    Beim Laden ersetzt das Skript den Inhalt durch dieselben Sendungen in
    interaktiver Form. Inhaltsgleich, also kein Cloaking."""
    import films_data, retro_data, imdb_data
    zeilen, tag = [], None
    alle = []
    for label, sender, liste in D._alle_tage():
        for r in liste:
            alle.append((label, r[0], r[1], r[2], r[3], r[4], r[5], sender, r[8]))
    for day, t, dur, title, sub, ch, age, grp, score, note in films_data.FILMS:
        alle.append((day, t, title, sub, "Film", dur, age, ch, note))
    alle.sort(key=lambda x: (D.DAY_ORDER.index(x[0]) if x[0] in D.DAY_ORDER else 99,
                             int(x[1][:2]) * 60 + int(x[1][3:])))
    import datetime as _dt, re as _re
    _h = _dt.date.today()
    def _d(label):
        m = _re.search(r"(\d{2})\.(\d{2})\.(\d{4})", label)
        return _dt.date(int(m.group(3)), int(m.group(2)), int(m.group(1))) if m else None
    erlaubt = [l for l in D.DAY_ORDER if _d(l) in (_h, _h + _dt.timedelta(days=1))]
    if not erlaubt:
        erlaubt = D.DAY_ORDER[:2]
    for day, zeit, titel, sub, genre, dur, age, sender, note in alle:
        if day not in erlaubt:
            continue
        if day != tag:
            tag = day
            import datetime as _dt
            import re as _re
            _m = _re.search(r"(\d{2})\.(\d{2})\.(\d{4})", day)
            _d = _dt.date(int(_m.group(3)), int(_m.group(2)), int(_m.group(1))) if _m else None
            _h = _dt.date.today()
            marke = "HEUTE" if _d == _h else ("MORGEN" if _d == _h + _dt.timedelta(days=1) else "")
            zeilen.append('<div class="daybar">%s<span class="d">%s</span>'
                          '<span class="ln"></span></div>' % (
                              '<span class="dtag">%s</span>' % marke if marke else "", _esc(day)))
        im = imdb_data.lookup(titel)
        zeilen.append(
            '<article class="prerow">'
            '<h3><span class="pretime">%s</span> %s%s</h3>'
            '<p class="premeta">%s · %s · ab %s · %s Min%s</p>'
            '<p class="predesc">%s</p></article>' % (
                _esc(zeit), _esc(titel),
                (" — " + _esc(sub)) if sub else "",
                _esc(sender), _esc(genre), age, dur,
                (" · IMDb %s" % str(im[0]).replace(".", ",")) if im else "",
                _esc((note or "")[:150])))
    return "\n".join(zeilen)


def prerender_media():
    """Statisches HTML für #medBoard."""
    import mediathek_data, imdb_data, epg_data
    import films_data
    zeilen = []
    gesehen = set()
    for m in mediathek_data.MVW:
        t = m["title"]
        gesehen.add(t)
        im = imdb_data.lookup(t)
        zeilen.append(
            '<article class="prerow">'
            '<h3>%s</h3>'
            '<p class="premeta">%s · ab %s%s · %s Folgen%s · %s</p>'
            '<p class="predesc">%s</p></article>' % (
                _esc(t), _esc(m["genre"]), m["age"],
                (" · %s" % m["jahr"]) if m.get("jahr") else "",
                m["folgen"],
                (" · IMDb %s" % str(im[0]).replace(".", ",")) if im else "",
                _esc(", ".join(m["prov"])),
                _esc(m.get("kurz") or m.get("note") or "")))
    for day, t, dur, title, sub, ch, age, grp, score, note in films_data.FILMS:
        if title in gesehen:
            continue
        gesehen.add(title)
        im = imdb_data.lookup(title)
        zeilen.append(
            '<article class="prerow"><h3>%s</h3>'
            '<p class="premeta">Film · ab %s%s%s · %s</p>'
            '<p class="predesc">%s</p></article>' % (
                _esc(title), age,
                (" · %s" % films_data.YEARS[title]) if films_data.YEARS.get(title) else "",
                (" · IMDb %s" % str(im[0]).replace(".", ",")) if im else "",
                _esc(ch), _esc((note or "")[:150])))
    return "\n".join(zeilen)


def media_itemlist_ld():
    """ItemList für den Katalog — maschinenlesbar für Suchmaschinen."""
    import json, mediathek_data, imdb_data
    items = []
    for i, m in enumerate(mediathek_data.MVW[:80], 1):
        im = imdb_data.lookup(m["title"])
        w = {"@type": "TVSeries", "name": m["title"], "genre": m["genre"],
             "inLanguage": "de", "typicalAgeRange": "%s-13" % m["age"]}
        if m.get("jahr"):
            w["startDate"] = str(m["jahr"])
        if m.get("kurz"):
            w["description"] = m["kurz"]
        if m.get("url"):
            w["url"] = m["url"]
        if im:
            w["aggregateRating"] = {"@type": "AggregateRating", "ratingValue": im[0],
                                    "ratingCount": im[2], "bestRating": 10}
        items.append({"@type": "ListItem", "position": i, "item": w})
    return ('<script type="application/ld+json" id="tvkCatalog">'
            + json.dumps({"@context": "https://schema.org", "@type": "ItemList",
                          "name": "Kinderserien und -filme in den Mediatheken",
                          "numberOfItems": len(items), "itemListElement": items},
                         ensure_ascii=False, separators=(",", ":"))
            + "</script>")


def kino_js():
    """Aktuelle Kinofilme als JS-Konstante fuer die Mediathek-Seite."""
    import json, kino_data
    return ("const KINO = "
            + json.dumps(kino_data.KINO, ensure_ascii=False, separators=(",", ":"))
            + ";\nconst KINO_STAND = " + json.dumps(kino_data.STAND) + ";")


def providers_js():
    rows = []
    for p in D.MEDIA_PROVIDERS:
        rows.append(
            '{{name:"{name}",short:"{short}",type:"{type}",price:"{price}",'
            'kids:"{kids}",age:"{age}",profiles:{prof},offline:{off},u:"{u}"}}'.format(
                name=p["name"], short=p["short"], type=p["type"], price=p["price"],
                kids=p["kids"], age=p["age"],
                prof=str(p["profiles"]).lower(), off=str(p["offline"]).lower(), u=p["u"]))
    return "const PROVIDERS = [\n  " + ",\n  ".join(rows) + "\n];"




def site_ld(pg):
    """WebSite + Organization + WebPage mit Tagesdatum: ein Graph pro Seite."""
    import json, datetime, zoneinfo
    heute = datetime.datetime.now(zoneinfo.ZoneInfo("Europe/Berlin")).date().isoformat()
    website = {"@type": "WebSite", "@id": DOMAIN + "/#website",
               "name": BRAND, "url": DOMAIN + "/", "inLanguage": "de-DE",
               "alternateName": ["TV Kinderprogramm", "Kinderprogramm heute"],
               "description": "Das TV-Programm für Kinder: alle Sendungen mit "
                              "Altersempfehlung, Eltern-Check und kostenlosen "
                              "Mediathek-Links, täglich aktualisiert.",
               "publisher": {"@id": DOMAIN + "/#org"}}
    org = {"@type": "Organization", "@id": DOMAIN + "/#org",
           "name": BRAND, "url": DOMAIN + "/",
           "logo": {"@type": "ImageObject", "url": DOMAIN + "/icon-512.png",
                    "width": 512, "height": 512}}
    page = {"@type": "CollectionPage" if pg["page"] == "mediathek" else "WebPage",
            "@id": DOMAIN + "/" + pg["canon"] + "#webpage",
            "url": DOMAIN + "/" + pg["canon"],
            "name": pg["title"].replace(" \u2014 ", ": "),
            "description": pg["desc"],
            "inLanguage": "de-DE", "dateModified": heute,
            "isPartOf": {"@id": DOMAIN + "/#website"},
            "primaryImageOfPage": {"@type": "ImageObject",
                                   "url": DOMAIN + "/og-image.jpg",
                                   "width": 1200, "height": 630}}
    graph = [website, org, page]
    if pg["page"] == "mediathek":
        graph.append({"@type": "BreadcrumbList",
                      "itemListElement": [
                          {"@type": "ListItem", "position": 1, "name": "Startseite",
                           "item": DOMAIN + "/"},
                          {"@type": "ListItem", "position": 2,
                           "name": "Mediatheken und Streaming",
                           "item": DOMAIN + "/mediathek-kinder.html"}]})
    return ('<script type="application/ld+json">'
            + json.dumps({"@context": "https://schema.org", "@graph": graph},
                         ensure_ascii=False, separators=(",", ":"))
            + "</script>")


def faq_ld():
    """FAQ-Schema fuer die Startseite: entspricht dem sichtbaren Text der
    aufklappbaren Info-Abschnitte und dem Intro."""
    import json
    try:
        n = sum(len(t) for _, _, t in D._alle_tage())
    except Exception:
        n = 0
    a1 = ("TVKinderprogramm.de zeigt das komplette Kinderprogramm von heute und "
          "den nächsten Tagen: alle Sendungen auf KiKA, Super RTL (Toggo und "
          "Toggolino), Nickelodeon, Disney Channel, Toggo plus und RiC, dazu "
          "Kindersendungen und Kinderfilme in den Vollprogrammen von ARD, ZDF "
          "und weiteren Sendern.")
    if n:
        a1 += " Aktuell stehen über %d Sendungen im Programmfenster." % (n // 100 * 100)
    fragen = [
        ("Was läuft heute für Kinder im TV?", a1),
        ("Welche Kindersender kann man kostenlos sehen?",
         "KiKA sendet täglich von 6 bis 21 Uhr werbefrei und komplett kostenlos. "
         "Auch Super RTL, Nickelodeon, Toggo plus und RiC sind im Free-TV "
         "empfangbar. Die grüne Kante an einer Programmzeile bedeutet: Es gibt "
         "eine kostenlose Möglichkeit, die Sendung zu sehen, im Free-TV oder in "
         "einer Mediathek wie dem KiKA-Player, der ARD- oder der ZDF-Mediathek."),
        ("Was bedeutet die Altersempfehlung, und was ist der Unterschied zur FSK?",
         "Die Angabe wie 'ab 6' ist eine redaktionelle Einschätzung anhand von "
         "Tempo, Lautstärke und Konfliktdichte der Sendung. Eine FSK-Freigabe "
         "existiert dagegen nur fuer Kinofilme und Bildträger; einzelne "
         "Serienfolgen im Fernsehen tragen keine FSK. Bei Kinderfilmen wird die "
         "FSK-Stufe zusätzlich als eigenes Feld angezeigt."),
    ]
    items = [{"@type": "Question", "name": q,
              "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in fragen]
    return ('<script type="application/ld+json" id="tvkFaq">'
            + json.dumps({"@context": "https://schema.org", "@type": "FAQPage",
                          "mainEntity": items},
                         ensure_ascii=False, separators=(",", ":"))
            + "</script>")


PAGES = {}

PAGES["live"] = dict(
    file="index.html", canon="", page="live",
    head_extra='<link rel="preload" as="image" href="hero.jpg" fetchpriority="high">\n',
    title="Kinderprogramm heute: Was läuft für Kinder im TV? | TVKinderprogramm.de",
    desc="Das TV-Programm für Kinder heute und morgen: alle Sendungen auf KiKA, Toggo, "
         "Nick und Co. mit Startzeit, Altersempfehlung und Eltern-Check. Täglich aktualisiert.",
    data=lambda: D.shows_js() + "\n\n" + D.kanaele_js() + "\n\n" + D.tipps_js() + "\n\n" + D.en_js(),
    # Sendungstexte bewusst nicht statisch ausliefern: nur Intro, h1 und
    # Beschreibung sind für Google sichtbar, die Liste kommt per JavaScript.
    # Rückweg: seo_ld=broadcast_ld, prerender=prerender_shows wieder eintragen.
    seo_ld=faq_ld,
    prerender=lambda: "",
    main="""    <section class="hero">
    <div class="kicker" data-i18n="hero_kick">Kinderprogramm heute</div>
    <h1 class="heroh1" data-i18n="hero_h1">Was läuft heute – <em>und passt zu meinem Kind?</em></h1>
    <p class="lead" data-i18n="hero_lead">Sendezeiten, Altersempfehlungen, kostenlose Mediatheken und aktuelle Kinderfilme – ruhig, übersichtlich und ohne Suchstress.</p>
    <div class="stats">
      <div class="stat"><strong id="statSender">23</strong><span data-i18n="stat_sender">Kindersender im Blick</span></div>
      <div class="stat"><strong id="statHeute">70+</strong><span data-i18n="stat_heute">Sendungen heute</span></div>
      <div class="stat"><strong id="statTipps">25+</strong><span data-i18n="stat_frei">Elterntipps aus der Redaktion</span></div>
      <div class="stat"><strong>3–13</strong><span data-i18n="stat_alter">Jahre Altersfilter</span></div>
    </div>
    <a class="heroslot" id="heroSlot">
      <img class="heroart" id="heroBild" src="hero.jpg" width="1500" height="701" fetchpriority="high" decoding="async" alt="TVKinderprogramm – Illustration">
      <span class="herocap" id="heroCap" hidden></span>
    </a>
    </section>
    <div class="fgroup filterbar">
      <div class="chiprow" id="idxAlter" role="group" aria-label="Alter">
        <button class="fchip tmode" data-a="all" aria-pressed="true" data-i18n="alter_alle">Alle</button>
        <button class="fchip tmode" data-a="a3" aria-pressed="false" data-i18n="alter_a3">3–5 Jahre</button>
        <button class="fchip tmode" data-a="a6" aria-pressed="false" data-i18n="alter_a6">6–9 Jahre</button>
        <button class="fchip tmode" data-a="a10" aria-pressed="false" data-i18n="alter_a10">10–13 Jahre</button>
      </div>
      <div class="fsearch"><span class="ic">⌕</span><input id="liveSearch" type="text" data-i18n-ph="such_live" placeholder="Sendung, Folge oder Sender suchen …"></div>
    </div>
    <section class="jetztbox" id="jetztBox">
    <div class="section-eyebrow tipphead jetzthead"><h2 data-i18n="jetzt_h2">Jetzt &amp; als Nächstes</h2></div>
    <div class="board" id="liveBoard">{prerender}</div>
    <button class="allelink unten" id="alleZeigen">Alle anzeigen</button>
    </section>
    <noscript><p class="nojs">Diese Seite zeigt das Kinderprogramm oben als Liste. Filter, Suche und die Detailangaben brauchen JavaScript.</p></noscript>
    <div class="feature">
      <span><span class="kicker2">Streaming &amp; Kino</span><b>Wenn im TV gerade nichts passt.</b>
      <span class="ctas">
        <a class="cta" href="mediathek-kinder.html">Mediathek- &amp; Kino-Tipps entdecken</a>
        <a class="cta cta2" href="memory.html">Eine Runde Memory spielen</a>
      </span></span>
      <img src="kino.png" alt="" width="640" height="580" loading="lazy" decoding="async">
    </div>

""" + seosec('<rect x="2.5" y="4.5" width="19" height="12.5" rx="2.6"/><path d="M8 20.5h8M12 17v3.5"/>',
             "Wo läuft das Kinderprogramm?",
             "KiKA, Super RTL, Nick, Disney Channel",
             ["KiKA sendet täglich von 6 bis 21 Uhr werbefrei und ist der einzige "
              "öffentlich-rechtliche Kindersender. Super RTL zeigt bis 11 Uhr unter dem Label "
              "Toggolino Vorschulprogramm und danach als Toggo Inhalte für Kinder ab etwa sechs "
              "Jahren. Dazu kommen Nickelodeon, Disney Channel, Toggo plus und RiC.",
              "Die grüne Kante links an einer Zeile bedeutet: Es gibt eine kostenlose Möglichkeit, "
              "die Sendung zu sehen — im Free-TV oder in einer Mediathek."])
    + "\n" + seosec('<circle cx="12" cy="12" r="9"/><path d="M12 8v4.5l3 1.8"/>',
                    "Altersempfehlung und FSK",
                    "Zwei verschiedene Angaben",
                    ["Die Angabe „ab 6\" ist eine redaktionelle Einschätzung anhand von Tempo, "
                     "Lautstärke und Konfliktdichte der Sendung. Sie steht bei jeder Zeile und ist "
                     "im Detail als redaktionell gekennzeichnet.",
                     "Eine FSK-Freigabe existiert dagegen nur für Kinofilme und Bildträger. Einzelne "
                     "Serienfolgen im Fernsehen tragen keine FSK — dort steht deshalb „keine Angabe\". "
                     "Bei Kinderfilmen wird die FSK-Stufe zusätzlich als eigenes Feld angezeigt."]),
    page_js="""
const board = document.getElementById("liveBoard");

(function(){
  try{
    const d=new Date(), ds=("0"+d.getDate()).slice(-2)+"."+("0"+(d.getMonth()+1)).slice(-2)+"."+d.getFullYear();
    const heute=SHOWS.filter(x=>x.day && x.day.indexOf(ds)>=0);
    if(heute.length) document.getElementById("statHeute").textContent=heute.length;
    if(typeof TIPPS!=="undefined") document.getElementById("statTipps").textContent=TIPPS.length;
    document.getElementById("statSender").textContent=Object.keys(CH_INFO).length;
  }catch(_){}
})();

function zeigeTippsIndex(){
  board.innerHTML =
    '<div class="testbanner"><b>Elterntipps</b>' +
    'Empfehlungen f\u00fcr Dinge, die unsere automatischen Quellen nicht sehen \u2014 ' +
    'kostenlose YouTube-Kan\u00e4le, Podcasts, Einstellungen. Die Nutzerverwaltung ist in der ' +
    'Testphase; bis eigene Einsendungen freigeschaltet sind, stammen die Tipps aus der Redaktion.</div>' +
    TIPPS.filter(x=>!x.seite||x.seite==="beide"||x.seite==="index").map(tippKarteIndex).join("");
  const erster=board.querySelector(".tipprow"); 
  if(erster){ erster.classList.add("open"); erster.querySelector(".rowhead").setAttribute("aria-expanded","true"); }
  const c=document.getElementById("optCount");
  if(c) c.textContent = TIPPS.length + " Tipps";
}


const EMPTY_LIVE = ()=> '<div class="soonbox"><span class="ic">\\ud83d\\udcfa</span><div>' +
  '<b style="display:block;color:var(--ink);font-family:Archivo,sans-serif;font-size:14px;margin-bottom:3px">'+t("leer_tt")+'</b>' +
  '<span style="font-size:12.5px;line-height:1.55">'+t("leer_tx")+'</span></div></div>';

let fGroup = "all", fFree = false, fPast = false, fSpecial = "all";
let kompakt = true;                        /* Startansicht: nur die nächsten Sendungen */

function apply(){
  let list = SHOWS;
  if(!fPast) list = list.filter(s=>!isPast(s));
  list = list.filter(s=>(s.age||0) < 16);   /* ab 16 wird nie angezeigt */
  if(fGroup.indexOf("genre:")===0) list = list.filter(s=>(s.genres||[s.genre]).includes(fGroup.slice(6)));
  else if(fGroup !== "all") list = list.filter(s=>s.grp===fGroup);
  const suche=(document.getElementById("liveSearch").value||"").trim();
  const teaser = kompakt && !suche;
  const jh=document.querySelector(".jetzthead"), jb=document.getElementById("alleZeigen");
  const bx=document.getElementById("jetztBox");
  if(teaser){
    if(bx) bx.classList.remove("offen");
    if(jh) jh.style.display="";
    let basis=list;
    if(fGroup==="all"){ const kinder=list.filter(x=>(x.age||0)<=6); if(kinder.length>=4) basis=kinder; }
    renderBoard(board, basis.slice(0,4), EMPTY_LIVE());
    if(jb){ const rest=Math.max(0, list.length-4);
      jb.textContent=t("jetzt_alle").replace("%s", rest);
      jb.style.display = rest>0 ? "" : "none"; }
  } else {
    if(bx) bx.classList.add("offen");
    if(jh) jh.style.display="none";
    if(jb) jb.style.display="none";
    renderBoard(board, list, EMPTY_LIVE());
  }
}

/* Minütlich nachziehen, damit gelaufene Sendungen von selbst verschwinden */
setInterval(()=>{ if(!fPast) apply(); }, 60000);

document.getElementById("idxAlter").addEventListener("click", e=>{
  const b=e.target.closest(".fchip"); if(!b) return;
  kompakt = true;
  fGroup = (fGroup===b.dataset.a) ? "all" : b.dataset.a;
  document.querySelectorAll("#idxAlter .fchip").forEach(x=>
    x.setAttribute("aria-pressed", String(x.dataset.a===fGroup)));
  apply();
});
document.getElementById("alleZeigen").addEventListener("click", ()=>{ kompakt=false; apply(); });

/* ---- Hero-Rotation: Eigenwerbung im Bildplatz ---- */
(function(){
  const KANDIDATEN=[
    {img:"hero.jpg", href:null, cap:null, alt:"Familie schaut gemeinsam Kinderprogramm – Illustration"},
    {img:"banner-tvfussball.jpg", href:"https://tvfussball.de", ext:true, cap:"slide_tvf", alt:"Fußball im Stadion: TVFussball.de für die Großen"},
    {img:"banner-muehle.jpg", href:"https://play.google.com/store/apps/details?id=app.muehle.muehle&utm_source=tvk_hero", ext:true, cap:"slide_mm", alt:"Mühle Meister: Brettspiel-App kostenlos im Play Store"},
    {img:"banner-memory.jpg", href:"memory.html", cap:"slide_mem", alt:"Memory online spielen: Paare finden für Kinder"},
    {img:"banner-abend.jpg", href:null, cap:null, alt:"Gemütlicher Fernsehabend für Kinder – Illustration"}
  ];
  const slot=document.getElementById("heroSlot"), bild=document.getElementById("heroBild"),
        cap=document.getElementById("heroCap");
  if(!slot||!bild) return;
  const da=[KANDIDATEN[0]];
  let geprueft=1;
  KANDIDATEN.slice(1).forEach(k=>{
    const i=new Image();
    i.onload=()=>{ da.push(k); fertig(); };
    i.onerror=fertig;
    i.src=k.img;
  });
  function fertig(){ geprueft++; if(geprueft===KANDIDATEN.length && da.length>1) start(); }
  let idx=0;
  function zeigen(k){
    bild.style.opacity="0";
    setTimeout(()=>{
      bild.src=k.img;
      if(k.alt) bild.alt=k.alt;
      if(k.href){ slot.setAttribute("href",k.href);
        if(k.ext){ slot.setAttribute("target","_blank"); slot.setAttribute("rel","noopener"); }
        else { slot.removeAttribute("target"); slot.removeAttribute("rel"); }
        slot.classList.add("klickbar");
      } else { slot.removeAttribute("href"); slot.removeAttribute("target"); slot.classList.remove("klickbar"); }
      if(cap){ if(k.cap){ cap.hidden=false; cap.textContent=t(k.cap); } else cap.hidden=true; }
      bild.style.opacity="1";
    }, 380);
  }
  function start(){ setInterval(()=>{ idx=(idx+1)%da.length; zeigen(da[idx]); }, 6500); }
})();
document.getElementById("liveSearch").addEventListener("input", apply);
apply();
initSearch(document.getElementById("liveSearch"), board);
window.reRender = ()=>{ apply(); };
""")

PAGES["mediathek"] = dict(
    file="mediathek-kinder.html", canon="mediathek-kinder.html", page="mediathek",
    title="Kinderserien kostenlos streamen: KiKA, Netflix, Disney+ und Co. | TVKinderprogramm.de",
    desc="Kinderserien und Kinderfilme kostenlos streamen: KiKA-Player, ARD und ZDF Mediathek "
         "im Vergleich mit Netflix, Disney+, Prime Video, WOW und YouTube Kids.",
    prerender=lambda: "",
    cat_ld=media_itemlist_ld,  # Top 80 des Katalogs als ItemList
    data=lambda: kino_js() + "\n\n" + providers_js() + "\n\n" + D.media_js() + "\n\n" + D.tipps_js() + "\n\n" + D.en_js(),
    main="""
    <section class="hero heromed">
    <div class="heromed-grid">
    <div class="heromed-txt">
    <div class="kicker">Streaming &amp; Kino</div>
    <h1 class="heroh1">Die besten Filme &amp; Serien für Kinder – <em>online &amp; im Kino</em></h1>
    <p class="lead">Altersgerechte Inhalte aus den kostenlosen Mediatheken und die aktuellen Kinderfilme im Kino – geprüft, übersichtlich und kindgerecht.</p>
    <div class="stats statsmed">
      <div class="stat"><strong id="statMed">190+</strong><span>Mediathek-Titel</span></div>
      <div class="stat"><strong id="statKino">8</strong><span>Kinofilme aktuell</span></div>
      <div class="stat"><strong>100%</strong><span>kinderfreundlich</span></div>
      <div class="stat"><strong>0 €</strong><span>kostenlos oder im Abo</span></div>
    </div>
    </div>
    <img class="heromask" src="kino.png" width="640" height="580" alt="Maskottchen mit Popcorn und 3D-Brille im Kino" fetchpriority="high" decoding="async">
    </div>
    </section>
    <div class="filtercard">
    <div class="fgroup"><span class="fglabel" data-i18n="grp_alter">Alter</span>
    <div class="chiprow" id="medChips" role="group" aria-label="Alter">
      <button class="fchip tmode" data-a="" aria-pressed="true" data-i18n="alter_alle">Alle</button>
      <button class="fchip tmode" data-a="a3" aria-pressed="false">3–5</button>
      <button class="fchip tmode" data-a="a6" aria-pressed="false">6–9</button>
      <button class="fchip tmode" data-a="a10" aria-pressed="false">10–13</button>
    </div></div>
    <div class="fgroup"><span class="fglabel" data-i18n="grp_genre">Genre</span>
    <div class="chiprow" id="medGenres" role="group" aria-label="Genre">
      <button class="fchip" data-i="ab" aria-pressed="false" data-i18n="int_ab">Abenteuer &amp; Action</button>
      <button class="fchip" data-i="ti" aria-pressed="false" data-i18n="int_ti">Tiere &amp; Natur</button>
      <button class="fchip" data-i="ma" aria-pressed="false" data-i18n="int_ma">Magie &amp; Fantasie</button>
      <button class="fchip" data-i="la" aria-pressed="false" data-i18n="int_la">Lachen &amp; Quatsch</button>
      <button class="fchip" data-i="wi" aria-pressed="false" data-i18n="int_wi">Wissen &amp; Entdecken</button>
    </div></div>
    </div>
    <section class="jetztbox">
    <div class="section-eyebrow tipphead sekkopf"><span class="secic gruen"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5.5l10 6.5-10 6.5z"/></svg></span><div class="secht"><h2>Mediathek-Vorschläge</h2><span class="cnt" id="katCount"></span></div></div>
    <div class="board" id="medBoard">{prerender}</div>
    <button class="allelink unten" id="katMehr" style="display:none">4 weitere anzeigen →</button>
    </section>
    <section class="jetztbox">
    <div class="section-eyebrow tipphead sekkopf"><span class="secic lila2"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M3 9h18M7 5l2 4M12 5l2 4M17 5l2 4"/></svg></span><div class="secht"><h2>Aktuell im Kino</h2><span class="cnt">Kinderfilme, die jetzt laufen oder bald starten</span></div></div>
    <div class="board" id="kinoBoard"></div>
    <button class="allelink unten" id="kinoMehr" style="display:none">4 weitere anzeigen →</button>
    </section>

    <noscript><p class="nojs">Der Katalog steht oben als Liste. Filter, Sortierung und Suche brauchen JavaScript.</p></noscript>

    <div class="section-eyebrow tipphead sekkopf"><span class="secic blau"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="7.5" height="16" rx="2"/><rect x="13.5" y="4" width="7.5" height="16" rx="2"/></svg></span><div class="secht"><h2 data-i18n="anbieter_h">Die Anbieter</h2><span class="cnt" data-i18n="anbieter_s">Kinderbereich im Vergleich</span></div><button class="allelink" id="anbStart">Vergleich anzeigen →</button></div>
    <div class="klapp" id="anbKlapp"><div class="klapp-in">
    <div class="board" id="medFree"></div>
    <div class="board" id="medPaid"></div>
    </div></div>

<a class="spielteaser" href="memory.html">
  <img src="leer.png" alt="" width="480" height="479" loading="lazy" decoding="async">
  <span><b data-i18n="spiel_h">Spiele-Ecke: Memory ist da!</b><span class="s" data-i18n="spiel_s">Paare finden mit Tieren, Fahrzeugen und Leckereien – kostenlos im Browser spielen.</span></span>
  <span class="bald" data-i18n="spiel_bald">Neu</span>
</a>

<section class="seotext">
  <h2 data-i18n="seo_med_h">Kinderserien und Kinderfilme kostenlos in den Mediatheken</h2>
  <p data-i18n="seo_med_1">TVKinderprogramm.de sammelt Kinderserien und Kinderfilme, die in den kostenlosen Mediatheken der öffentlich-rechtlichen Sender abrufbar sind: im KiKA-Player, in der ARD Mediathek, bei ZDFtivi und bei 3sat. Jeder Titel trägt eine redaktionelle Altersempfehlung (ab 3, ab 6 oder ab 10 Jahren), dazu Folgenzahl, Laufzeit und, wo vorhanden, die IMDb-Bewertung mit Stimmenzahl.</p>
  <p data-i18n="seo_med_2">Die Angebote der öffentlich-rechtlichen Mediatheken sind werbefrei und ohne Anmeldung nutzbar: ein Unterschied zu YouTube und den Apps der Privatsender. Über die Filter oben lassen sich Titel nach Altersgruppe und Interessen wie Tiere und Natur, Wissen und Entdecken oder Magie und Fantasie eingrenzen. Die Tipps werden bei jedem Besuch neu gemischt.</p>
  <p data-i18n="seo_med_3">Verfügbarkeiten in den Mediatheken ändern sich laufend; verbindlich ist stets die Angabe des jeweiligen Anbieters. Kostenpflichtige Dienste wie Disney+, Netflix und Prime Video werden derzeit nicht gelistet, folgen aber. Das laufende Fernsehprogramm der Kindersender zeigt die Startseite.</p>
</section>


""" + seosec('<circle cx="12" cy="12" r="9"/><path d="M10.2 8.6l4.8 3.4-4.8 3.4z" fill="currentColor" stroke="none"/>',
             "Worauf es beim Kinderprofil ankommt",
             "PIN, Autoplay, Downloads",
             ["Ein eigenes Kinderprofil begrenzt den Katalog auf altersgerechte Titel und schaltet "
              "Empfehlungen aus dem Erwachsenenkatalog ab. Wichtig sind eine PIN, die sich nicht "
              "durch das Kind zurücksetzen lässt, und eine Download-Funktion für unterwegs.",
              "Bei YouTube Kids werden Inhalte teilweise automatisch kuratiert. Wer das nicht "
              "möchte, kann in der App auf einen manuell freigegebenen Kanal-Katalog umstellen.",
              "Die Mediatheken von KiKA, ARD und ZDF sind werbefrei und kostenlos, zeigen Folgen "
              "aber nur befristet."])
    + "\n" + seosec('<path d="M12.6 3.3l7.1 7.1a2 2 0 0 1 0 2.8l-6.5 6.5a2 2 0 0 1-2.8 0l-7.1-7.1V5.3a2 2 0 0 1 2-2z"/><circle cx="8" cy="8" r="1.5"/>',
                    "Werbung im Kinderfernsehen",
                    "Der wichtigste Unterschied",
                    ["KiKA ist der einzige Kindersender ohne Werbung. Super RTL, Toggo plus, "
                     "Nickelodeon, Disney Channel und RiC finanzieren sich über Werbung, die sich "
                     "inhaltlich oft direkt an Kinder richtet.",
                     "Bei den Streaming-Anbietern hängt es vom Tarif ab: Netflix, Prime Video und "
                     "Disney+ haben günstigere Abos mit Werbung. In den Kinderprofilen ist sie meist "
                     "reduziert, aber nicht immer ganz abgeschaltet — vor dem Abschluss lohnt der "
                     "Blick ins Kleingedruckte.",
                     "Werbefrei und kostenlos sind ausschließlich die öffentlich-rechtlichen "
                     "Mediatheken: KiKA-Player, ARD Mediathek und ZDFtivi."]),
    page_js="""
/* ---------- Anbieterkarten ---------- */
const PCOL={"Netflix":"#E50914","Prime Video":"#00A8E1","Disney+":"#0C2A6B",
  "WOW / Sky":"#C5008A","YouTube Kids":"#FF0000","KiKA-Player":"#5FB030",
  "ARD Mediathek":"#123A8F","ZDFtivi":"#FA7D19"};
function pcard(p){
  const c = PCOL[p.name] || "#C24009";
  const stil = `--pv:${c};--pv-bg:${hexA(c,.11)};--pv-bd:${hexA(c,.38)};`+
               `--pv-tx:${darkenTo(c,.185)};--pv-bgd:${hexA(c,.17)};--pv-txd:${lightenTo(c,.42)}`;
  return '<div class="row provcard" style="'+stil+'"><div class="provrow">' +
    '<span class="plogo">'+p.short+'</span>' +
    '<span class="pmain"><b>'+p.name+'</b><span>'+p.kids+'</span>' +
      '<span class="featrow">' +
        '<span class="feat">Alter '+p.age+'</span>' +
        '<span class="feat'+(p.profiles?' yes':'')+'">'+(p.profiles?'Kinderprofile':'keine Profile')+'</span>' +
        '<span class="feat'+(p.offline?' yes':'')+'">'+(p.offline?'Downloads':'kein Download')+'</span>' +
      '</span></span>' +
    '<span class="pprice">'+p.price+'</span></div></div>';
}
/* Pflichtangabe, sobald Streaming-Daten aus TMDB im Katalog stehen */
(function(){
  /* nur zeigen, wenn die Angabe wirklich von dort stammt (src:"tmdb"),
     nicht bei unseren eigenen Sender-zu-Mediathek-Regeln */
  const hatStreaming = MEDIA.some(e=>e.prov.some(p=>p.src==="tmdb"));
  const el=document.getElementById("attrib");
  if(el && hatStreaming) el.innerHTML =
    'Streaming-Verf\u00fcgbarkeit: <a href="https://www.themoviedb.org/" target="_blank" rel="noopener">TMDB</a>, powered by <a href="https://www.justwatch.com/" target="_blank" rel="noopener">JustWatch</a>.';
})();

document.getElementById("medFree").innerHTML = PROVIDERS.filter(p=>p.type!=="abo").map(pcard).join("");
document.getElementById("medPaid").innerHTML = PROVIDERS.filter(p=>p.type==="abo").map(pcard).join("");

/* ---------- Katalog und Tipps ---------- */
const mBoard = document.getElementById("medBoard");

function mcard(e){
  const [c1,c2] = pairFor(e.title);
  const prov = e.prov.filter(p=>p.ok).map(p=>{
    const c = p.c || "#7A6153";
    const style = `--pv:${c};--pv-bg:${hexA(c,.11)};--pv-bd:${hexA(c,.38)};`+
                  `--pv-tx:${darkenTo(c,.185)};--pv-bgd:${hexA(c,.17)};--pv-txd:${lightenTo(c,.42)}`;
    return `<span class="pv${p.sure?" sure":""}" style="${style}"><i></i>${p.n}${p.sure?"":" *"}</span>`;
  }).join("");
  const frei1 = e.prov.find(p=>p.ok && p.frei);
  const badge = frei1 ? `<span class="freebest tv">▣ ${t("kostenlos")} · ${frei1.n}</span>` : "";
  const key = [e.title, e.sub||"", e.genre, e.year||"",
               e.prov.map(p=>p.n).join(" ")].join("|");
  const vars = `--c1:${c1};--c2:${c2};--w1:${hexA(c1,.22)};--w2:${hexA(c2,.20)};`+
               `--w1d:${hexA(c1,.14)};--w2d:${hexA(c2,.11)}`;
  const rate = (e.imdb&&e.imdb.r) ? String(e.imdb.r).replace(".",",") : null;
  /* Zeitzelle der Startseite wird hier zur Folgenzelle: großer Wert oben,
     Einheit darunter. So bleiben beide Boards im selben Raster. */
  const zc1 = e.folgen ? e.folgen : (e.year || "Film");
  const zc2 = e.folgen ? (LANG==="en"?"episodes":"Folgen")
            : (e.year ? (LANG==="en"?"since":"seit") : "");
  return `
<div class="row free" style="${vars}" data-k="${key}">
  <button class="rowhead" aria-expanded="false">
    <div class="mthumb"><img src="cover-${({ti:"tiere",ma:"magie",ab:"abenteuer",la:"lachen",wi:"wissen"})[(e.ints||[])[0]]||"musik"}.jpg" alt="" loading="lazy" decoding="async"><span class="mfolgen">${zc1}${zc2?" "+zc2:""}</span></div>
    <div class="teams">
      <div class="t">${sticker({title:e.title, genre:e.genre})}<span>${e.title}</span></div>
      ${e.sub?`<div class="t subline">${e.sub}</div>`:""}
      <div class="meta"><span class="comp">${gname(e.genre)}</span>${
        rate?`<span class="imdb"><b>IMDb</b>${rate}</span>`:""}${
        e.retro?`<span class="retro">${LANG==="en"?"since":"seit"} ${e.retro.y}</span>`:""}<span class="agetag">${t("ab")} ${e.age}</span>${badge}</div>
    </div>
    <div class="rh-right"><span class="chev">${RCHEV}</span></div>
  </button>
  <div class="panel"><div class="panel-in"><div class="panel-pad">
    <div class="lh"><div class="lh-h">${t("passt")}</div>
      ${e.kurz?`<p class="lh-txt lang">${e.kurz}</p>`:""}
      ${e.note?`<p class="lh-reden"><b>${LANG==="en"?"Latest episode:":"Aktuelle Folge:"}</b> ${e.note}</p>`:""}
    </div>
    <div class="pvrow panelprov">${prov}</div>
    <div class="agebox">
      <div class="arow"><span class="alb">${t("alter")}</span><span class="aval">${t("ab")} ${e.age} ${t("jahren")}<span class="est">${t("redaktionell")}</span></span></div>
      ${e.year?`<div class="arow"><span class="alb">${LANG==="en"?"Since":"Seit"}</span><span class="aval">${e.year}</span></div>`:""}
      ${e.folgen?`<div class="arow"><span class="alb">${LANG==="en"?"Episodes":"Folgen"}</span><span class="aval">${e.folgen}${e.dauer?` · ${LANG==="en"?"approx.":"ca."} ${e.dauer} ${LANG==="en"?"min each":"Min je Folge"}`:""}</span></div>`:""}
      <div class="arow sp-sicher"><span class="alb">${t("nachsehen")}</span><span class="aval"><span class="spdot"></span>${
        t("nachsehen_ja")}: ${e.prov.filter(p=>p.ok).map(p=>p.n).join(LANG==="en"?" and ":" und ")}</span></div>
      ${e.retro?`<div class="arow"><span class="alb">${t("kennst")}</span><span class="aval">${e.retro.n}</span></div>`:""}
      <div class="arow"><span class="alb">IMDb</span><span class="aval">${
        rate?`<b>${rate}</b> ${t("imdb_von")} <span class="votes">${t("imdb_stimmen").replace("%s",(e.imdb.v||0).toLocaleString("de-DE"))}</span> · <a href="https://www.imdb.com/title/${e.imdb.id}/" target="_blank" rel="noopener">${t("imdb_ansehen")}</a>`
            :`<a href="https://www.imdb.com/find/?q=${encodeURIComponent(e.title)}&s=tt" target="_blank" rel="noopener">${t("imdb_nach")}</a>`}</span></div>
    </div>
    ${e.url?`<div class="actrow"><a class="sharebtn" href="${e.url}" target="_blank" rel="noopener"><span>${t("ansehen")}</span></a></div>`:""}
  </div></div></div>
</div>`;
}



/* ---- Kostenfrei-Schalter: fest an, Hinweis statt Abschalten ---- */
function toast(txt){
  const el=document.getElementById("toast"); if(!el) return;
  el.textContent=txt; el.classList.add("an");
  clearTimeout(toast._t); toast._t=setTimeout(()=>el.classList.remove("an"), 3000);
}

/* ---- Filterchips: Alter (Einfachauswahl) + Interessen (Mehrfach) ---- */
let fAge=null, fInts=new Set();
const SPEICHER="tvk_med_filter";
try{
  const g=JSON.parse(localStorage.getItem(SPEICHER)||"null");
  if(g){ fAge=g.a||null; fInts=new Set(g.i||[]); }
}catch(_){}

function chipsAnzeigen(){
  document.querySelectorAll("#medChips .fchip[data-a]").forEach(b=>
    b.setAttribute("aria-pressed", String((b.dataset.a||null)===fAge)));
  document.querySelectorAll("#medGenres .fchip[data-i]").forEach(b=>
    b.setAttribute("aria-pressed", String(fInts.has(b.dataset.i))));
  const mt=document.getElementById("medTipp");
  if(mt) mt.setAttribute("aria-pressed", String(typeof fElterntipp!=="undefined"&&fElterntipp));
}
function chipsSpeichern(){
  try{ localStorage.setItem(SPEICHER, JSON.stringify({a:fAge, i:[...fInts]})); }catch(_){}
}
function chipKlick(e, zustand, danach){
  const b=e.target.closest(".fchip"); if(!b || b.id) return;
  if(b.dataset.a!==undefined) zustand.age = (b.dataset.a==="") ? null : ((zustand.age===b.dataset.a) ? null : b.dataset.a);
  if(b.dataset.i){ zustand.ints.has(b.dataset.i) ? zustand.ints.delete(b.dataset.i) : zustand.ints.add(b.dataset.i); }
  danach();
}
const topZustand={get age(){return fAge}, set age(v){fAge=v}, get ints(){return fInts}};
["medChips","medGenres"].forEach(id=>document.getElementById(id).addEventListener("click",
  e=>chipKlick(e, topZustand, ()=>{ chipsAnzeigen(); chipsSpeichern();
    katalogZeigen(); kinoZeigen(); })));

/* ---- Tipps: Treffer mischen, ohne Wiederholung in der Sitzung ---- */
const gezeigt = new Set();
let tippRest=[], tippTreffer=0, sichtbareTipps=[];
const kat = e => (e.age||0) < 16 && e.prov.some(p=>p.ok && p.frei);   /* Schalter "Nur kostenfrei" ist fest an */
const deTitel = e => e._title!==undefined ? e._title : e.title;
function passt(e){
  if(fAge && e.grp!==fAge) return false;
  if(fInts.size && !(e.ints||[]).some(c=>fInts.has(c))) return false;
  return true;
}
function mischen(a){
  for(let i=a.length-1;i>0;i--){ const j=Math.floor(Math.random()*(i+1)); [a[i],a[j]]=[a[j],a[i]]; }
  return a;
}
function tippAlter(tp){ return tp.alter<6 ? "a3" : (tp.alter<10 ? "a6" : "a10"); }
function tippPoolBauen(){
  if(typeof fElterntipp!=="undefined" && fElterntipp){
    /* Elterntipp aktiv: die Vorschläge kommen aus den Elterntipps selbst.
       Altersfilter greift, Interessen passen hier nicht und bleiben außen vor. */
    const alle = TIPPS.filter(x=>!x.seite||x.seite==="beide"||x.seite==="mediathek")
                      .filter(x=>!gezeigt.has("tipp:"+x.titel));
    const treffer = mischen(alle.filter(x=>!fAge || tippAlter(x)===fAge));
    const rest = mischen(alle.filter(x=>fAge && tippAlter(x)!==fAge));
    tippTreffer = treffer.length;
    tippRest = treffer.concat(rest);
    return;
  }
  const frisch = MEDIA.filter(e=>kat(e) && !gezeigt.has(deTitel(e)));
  const treffer = mischen(frisch.filter(passt));
  /* Auffüllreihenfolge: thematisch nächstliegend zuerst */
  const naehe = e => ((e.ints||[]).some(c=>fInts.has(c)) ? 2 : 0) + (fAge && e.grp===fAge ? 1 : 0);
  const rest = mischen(frisch.filter(e=>!passt(e))).sort((a,b)=>naehe(b)-naehe(a));
  tippTreffer = treffer.length;
  tippRest = treffer.concat(rest);
}
function ersterTippAuf(){
  const host=document.getElementById("tippBoard");
  if(host.querySelector(".row.open")) return;
  const r=host.querySelector(".row");
  if(r){ r.classList.add("open"); r.querySelector(".rowhead").setAttribute("aria-expanded","true"); }
}
function tippsZeigen(neuAufbau){
  const host=document.getElementById("tippBoard"),
        btn=document.getElementById("tippMehr"),
        note=document.getElementById("tippNote");
  if(neuAufbau){ note.textContent=""; tippPoolBauen(); }
  /* Immer genau fünf Karten: der Knopf blättert weiter statt anzuhängen */
  host.innerHTML=""; sichtbareTipps=[];
  const elternModus = (typeof fElterntipp!=="undefined" && fElterntipp);
  const naechste = tippRest.splice(0,5);
  naechste.forEach(e=>{ gezeigt.add(elternModus ? "tipp:"+e.titel : deTitel(e)); sichtbareTipps.push(e); });
  host.innerHTML = naechste.map(elternModus ? tippKarteIndex : mcard).join("");
  if(!naechste.length){
    /* Sitzung ausgeschöpft: freundlich sagen statt leer stehen lassen */
    host.innerHTML = '<div class="tippnote" style="padding:10px 2px">'+t("alle_gezeigt")+'</div>';
    note.textContent="";
  } else if(neuAufbau && (fAge||fInts.size) && tippTreffer<5 && tippTreffer>0)
    note.textContent = t("wenig_tipps").replace("%s", tippTreffer);
  const label = !tippRest.length ? t("alle_gezeigt") : t("mehr5");
  btn.disabled = !tippRest.length;
  btn.title = label;
  if(btn.classList.contains("ohnebild")) btn.textContent = label;
  const bimg=btn.querySelector("img"); if(bimg) bimg.alt = label;
  ersterTippAuf();
}
let tippOffen=false;

/* ---- Katalog: vollständig, A bis Z; die Suche ignoriert die Chips ---- */
let katOffen=true, katLimit=4;
function katalogZeigen(){
  const mehrBtn=document.getElementById("katMehr"),
        kopfBtn=document.getElementById("katMehrKopf"),
        suchtext=(document.getElementById("medSearchTop")||{}).value||"";
  if(typeof fElterntipp!=="undefined" && fElterntipp){
    mehrBtn.style.display="none"; if(kopfBtn) kopfBtn.style.display="none";
    const tipps=TIPPS.filter(x=>!x.seite||x.seite==="beide"||x.seite==="mediathek");
    mBoard.innerHTML = tipps.map(tippKarteIndex).join("") + '<div class="empty" style="display:none">'+t("nichts")+'</div>';
    const e1=mBoard.querySelector(".tipprow");
    if(e1){ e1.classList.add("open"); e1.querySelector(".rowhead").setAttribute("aria-expanded","true"); }
    document.getElementById("katCount").textContent = tipps.length + " " + t("tipps_n");
    return;
  }
  let l = MEDIA.filter(kat);
  if(fAge) l = l.filter(e=>e.grp===fAge);
  if(fInts.size) l = l.filter(e=>(e.ints||[]).some(c=>fInts.has(c)));
  l = l.slice().sort((a,b)=>a.title.localeCompare(b.title, LANG==="en"?"en":"de"));
  /* Bei aktiver Suche die volle Liste rendern, sonst seitenweise zu 30 */
  const seite = suchtext.trim() ? l : l.slice(0, katLimit);
  mBoard.innerHTML = seite.map(mcard).join("") + '<div class="empty" style="display:none">'+t("nichts")+'</div>';
  const rest = suchtext.trim() ? 0 : l.length - seite.length;
  mehrBtn.style.display = rest>0 ? "" : "none";
  if(kopfBtn) kopfBtn.style.display = rest>0 ? "" : "none";
  if(rest>0) mehrBtn.textContent = Math.min(4,rest)+" weitere anzeigen \u2192";
  document.getElementById("katCount").textContent =
    (suchtext.trim() ? l.length : Math.min(katLimit,l.length)+" / "+l.length) + " " + t("titel_n");
  const mc=document.getElementById("medCount");
  if(mc) mc.textContent = MEDIA.filter(kat).length + " " + t("titel_n");
}

document.getElementById("katMehr").addEventListener("click", ()=>{ katLimit+=4; katalogZeigen(); });
{ const kk=document.getElementById("katMehrKopf");
  if(kk) kk.addEventListener("click", ()=>{ katLimit+=4; katalogZeigen(); }); }
let fElterntipp=false;
function elterntippUmschalten(){
  fElterntipp = !fElterntipp;
  chipsAnzeigen();
  katalogZeigen();
  if(tippOffen) tippsZeigen(true);
}

chipsAnzeigen();
katalogZeigen();
(function(){ try{
  if(typeof MEDIA!=="undefined") document.getElementById("statMed").textContent=MEDIA.length;
  if(typeof KINO!=="undefined") document.getElementById("statKino").textContent=KINO.length;
}catch(_){} })();

document.getElementById("anbStart").addEventListener("click", function(){
  const auf=document.getElementById("anbKlapp").classList.toggle("auf");
  this.textContent=auf ? "Ausblenden" : "Vergleich anzeigen \u2192";
});

/* ---- Aktuell im Kino ---- */
function trailerUrl(titel){
  const w = (typeof LANG!=="undefined" && LANG==="en") ? "Trailer Englisch" : "Trailer Deutsch";
  return "https://www.youtube.com/results?search_query=" + encodeURIComponent(titel + " " + w);
}
let kinoLimit=4;
function kinoAuswahl(){
  const map={a3:["0"], a6:["0","6"], a10:["0","6","12"]};
  let pool=KINO.slice();
  if(typeof fAge!=="undefined" && fAge && map[fAge]){
    const ok=pool.filter(f=>f.fsk!=="" && map[fAge].indexOf(String(f.fsk))>=0);
    pool=ok.concat(pool.filter(f=>ok.indexOf(f)<0));   /* passend zuerst, dann auffuellen */
  }
  return pool;
}
function kinoZeigen(){
  const kb=document.getElementById("kinoBoard"); if(!kb) return;
  const heute=new Date(); heute.setHours(0,0,0,0);
  const dat = x=>{ const m=x.split("."); return new Date(+m[2], +m[1]-1, +m[0]); };
  const pool=kinoAuswahl(), seite=pool.slice(0,kinoLimit);
  kb.innerHTML = '<div class="kinogrid">'+seite.map(f=>{
    const st=dat(f.start), zukunft=st>heute;
    const neu=!zukunft && (heute-st)/864e5<=21;
    return '<article class="kinocard">'+
      '<div class="kinoart">'+
        (zukunft?'<span class="ribbon">Demn\u00e4chst</span>':(neu?'<span class="ribbon neu">Neu</span>':""))+
        '<span class="fskcircle">'+(f.fsk!==""?f.fsk:"?")+'</span>'+
        '<img src="kino-platzhalter.jpg" alt="" loading="lazy" decoding="async" onerror="this.remove()">'+
      '</div>'+
      '<h3>'+f.t+'</h3>'+
      '<p class="kmeta">'+(f.dauer?f.dauer+" Min \u00b7 ":"")+(zukunft?("Kinostart "+f.start.slice(0,6)):"jetzt im Kino")+'</p>'+
      '<a class="trailerbtn" target="_blank" rel="noopener" href="'+trailerUrl(f.t)+'">'+
      '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5.5l10 6.5-10 6.5z"/></svg>Trailer</a>'+
      '</article>';
  }).join("")+"</div>";
  const km=document.getElementById("kinoMehr"), rest=pool.length-seite.length;
  if(km){ km.style.display = rest>0 ? "" : "none";
    km.textContent = Math.min(4,rest)+" weitere anzeigen \u2192"; }
}
document.getElementById("kinoMehr").addEventListener("click", ()=>{ kinoLimit+=4; kinoZeigen(); });

/* ---- Tipps und Katalog wieder einklappen ---- */
const katZuBtn=document.getElementById("katZu");
["katMehrKopf","katMehr"].forEach(id=>{const b=document.getElementById(id);
  if(b) b.addEventListener("click", ()=>{ if(katZuBtn && katLimit>10) katZuBtn.style.display=""; });});
if(katZuBtn) katZuBtn.addEventListener("click", function(){
  katLimit=10; katalogZeigen(); this.style.display="none";
  const kopf=document.querySelector('h2[data-i18n="kat_h2"]');
  if(kopf) kopf.scrollIntoView({behavior:"smooth", block:"start"});
});
window.reRender = ()=>{
  katalogZeigen();
  kinoZeigen();
  const kk=document.getElementById("kinoKlapp"), kb=document.getElementById("kinoStart");
  const ak=document.getElementById("anbKlapp"), ab=document.getElementById("anbStart");

  /* sichtbare Tippkarten in der neuen Sprache neu zeichnen, Bestand behalten */
  const em = (typeof fElterntipp!=="undefined" && fElterntipp);
  document.getElementById("tippBoard").innerHTML = sichtbareTipps.map(em ? tippKarteIndex : mcard).join("");
  ersterTippAuf();
  chipsAnzeigen();
};
kinoZeigen();
""")

def main():
    css = BASE_CSS + ADD_CSS
    shell_js = SHELL_JS.replace("BRANDNAME", BRAND)
    for p in PAGES.values():
        html = SHELL.format(
            build="2026-07-30-v3", brand=BRAND, domain=DOMAIN,
            title=p["title"], desc=p["desc"], canon=p["canon"], page=p["page"],
            css=css, main=p["main"].replace("{prerender}", p.get("prerender", lambda: "")()),
            nav=nav_html(p["page"]),
            data_js=p["data"](), shell_js=shell_js, page_js=p["page_js"],
            site_ld=site_ld(p),
            head_extra=p.get("head_extra", ""),
            seo_ld=p.get("seo_ld", lambda: "")(),
            cat_ld=p.get("cat_ld", lambda: "")(),
        )
        # Gedankenstriche raus: liest sich generisch, Doppelpunkt oder Punkt tut es.
        html = html.replace(" — ", ": ").replace(" —", ":").replace("— ", ": ").replace("—", "-")
        (HERE / p["file"]).write_text(html, encoding="utf-8")
        print(f"geschrieben: {p['file']:16} {len(html)//1024} KB")

    for old in ("quiz.html", "neu.html"):
        f = HERE / old
        if f.exists():
            f.unlink()
            print("entfernt:    " + old)


if __name__ == "__main__":
    main()
