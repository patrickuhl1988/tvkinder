#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kinoseite: Vorschlags-Boxen statt Tipps/Katalog, Kino-Box, Cover-Karten."""
import pathlib, re

p = pathlib.Path("build.py")
s = p.read_text(encoding="utf-8")


def rep(old, new, n=1):
    global s
    assert s.count(old) == n, f"ANKER {old[:60]!r}: {s.count(old)}x statt {n}"
    s = s.replace(old, new)


# ==== A) MARKUP =============================================================
# 1) Freitextsuche raus
blk = re.search(r'\s*<div class="fgroup">\n\s*<div class="fsearch"><span class="ic">\u2315</span><input id="medSearchTop"[^\n]*\n\s*</div>\n', s)
assert blk, "Suchgruppe fehlt"
s = s.replace(blk.group(0), "\n")

# 2) Sonstiges-Gruppe (Elterntipp + Nur kostenfrei) raus
blk = re.search(r'\s*<div class="fgroup"><span class="fglabel" data-i18n="grp_sonst">Sonstiges</span>.*?medFrei.*?</div></div>\n', s, re.S)
assert blk, "Sonstiges-Gruppe fehlt"
s = s.replace(blk.group(0), "\n")

# 3) Mediathek-Tipps-Bereich komplett raus
blk = re.search(r'    <div class="section-eyebrow tipphead sekkopf"><span class="secic lila">.*?tippZu[^\n]*</div>\n'
                r'    <div class="tippnote" id="tippNote"[^\n]*</div>\n'
                r'    <div class="board" id="tippBoard"></div>\n', s, re.S)
assert blk, "Tipps-Bereich fehlt"
s = s.replace(blk.group(0), "")

# 4) Kino-Bereich ausschneiden (kommt spaeter hinter die Vorschlags-Box)
kino_blk = re.search(r'    <div class="section-eyebrow tipphead sekkopf"><span class="secic lila2">.*?kinoStart[^\n]*</div>\n'
                     r'    <div class="klapp" id="kinoKlapp"><div class="klapp-in">\n'
                     r'    <div class="board" id="kinoBoard"></div>\n'
                     r'    </div></div>\n', s, re.S)
assert kino_blk, "Kino-Bereich fehlt"
s = s.replace(kino_blk.group(0), "")

KINO_NEU = '''    <section class="jetztbox">
    <div class="section-eyebrow tipphead sekkopf"><span class="secic lila2"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M3 9h18M7 5l2 4M12 5l2 4M17 5l2 4"/></svg></span><div class="secht"><h2>Aktuell im Kino</h2><span class="cnt">Kinderfilme, die jetzt laufen oder bald starten</span></div></div>
    <div class="board" id="kinoBoard"></div>
    <button class="allelink unten" id="kinoMehr" style="display:none">4 weitere anzeigen \u2192</button>
    </section>
'''

# 5) Katalog wird zur Vorschlags-Box, Kino-Box direkt danach
rep('''    <div class="section-eyebrow tipphead sekkopf"><span class="secic gruen"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 6h16M4 12h16M4 18h10"/></svg></span><div class="secht"><h2 data-i18n="kat_h2">Kostenfreie Mediathek-Inhalte</h2><span class="cnt" id="katCount"></span></div><button class="allelink" id="katMehrKopf">30 weitere \u2192</button><button class="allelink" id="katZu" style="display:none">Einklappen</button></div>
    <div class="board" id="medBoard">{prerender}</div>
    <button class="mehrbtn" id="katMehr" data-i18n="mehr30" style="display:none">30 weitere anzeigen</button>
''',
'''    <section class="jetztbox">
    <div class="section-eyebrow tipphead sekkopf"><span class="secic gruen"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5.5l10 6.5-10 6.5z"/></svg></span><div class="secht"><h2>Mediathek-Vorschl\u00e4ge</h2><span class="cnt" id="katCount"></span></div></div>
    <div class="board" id="medBoard">{prerender}</div>
    <button class="allelink unten" id="katMehr" style="display:none">4 weitere anzeigen \u2192</button>
    </section>
''' + KINO_NEU)

# ==== B) JS =================================================================
# Abgeloeste Hoerer entfernen (Elemente existieren nicht mehr)
rep('''document.getElementById("tippMehr").addEventListener("click", ()=>{
  if(!tippOffen){ tippOffen=true; tippsZeigen(true); }
  else tippsZeigen(false);
});
''', '')
rep('''const tippZuBtn=document.getElementById("tippZu");
document.getElementById("tippMehr").addEventListener("click", ()=>{ if(tippZuBtn) tippZuBtn.style.display=""; });
if(tippZuBtn) tippZuBtn.addEventListener("click", function(){
  tippOffen=false; document.getElementById("tippBoard").innerHTML="";
  const n=document.getElementById("tippNote"); if(n) n.textContent="";
  this.style.display="none";
});
''', '')
rep('''{ const b=document.getElementById("tippMehr"); b.title=t("tipps_start");
  if(b.classList.contains("ohnebild")) b.textContent=t("tipps_start");
  const bi=b.querySelector("img"); if(bi) bi.alt=t("tipps_start"); }
''', '')
rep('document.getElementById("medTipp").addEventListener("click", elterntippUmschalten);\n', '')

suchblk = re.search(r'const suchOben=document\.getElementById\("medSearchTop"\);.*?initSearch\(suchOben, mBoard\);\n', s, re.S)
assert suchblk, "suchOben-Block fehlt"
s = s.replace(suchblk.group(0), "")

rep('''document.getElementById("kinoStart").addEventListener("click", function(){
  const auf=document.getElementById("kinoKlapp").classList.toggle("auf");
  if(auf) kinoZeigen();
  this.textContent=auf ? "Ausblenden" : "Alle Kinofilme \\u2192";
});''',
'''document.getElementById("kinoMehr").addEventListener("click", ()=>{ kinoLimit+=4; kinoZeigen(); });
kinoZeigen();''')

rep('  if(document.getElementById("kinoKlapp").classList.contains("auf")) kinoZeigen();\n', '  kinoZeigen();\n')

# Chips wirken auf beide Boxen; Tipps-Aufruf entfaellt
rep('    if(tippOffen) tippsZeigen(true); katalogZeigen(); })));',
    '    katalogZeigen(); kinoZeigen(); })));')

# Vorschlags-Box: 4er-Schritte
rep('let katOffen=true, katLimit=10;', 'let katOffen=true, katLimit=4;')
rep('document.getElementById("katMehr").addEventListener("click", ()=>{ katLimit+=30; katalogZeigen(); }',
    'document.getElementById("katMehr").addEventListener("click", ()=>{ katLimit+=4; katalogZeigen(); }')
rep('  if(rest>0) mehrBtn.textContent = t("mehr30").replace("%s", Math.min(30,rest));',
    '  if(rest>0) mehrBtn.textContent = Math.min(4,rest)+" weitere anzeigen \\u2192";')
# Einklappen-Reste stilllegen (Knoepfe existieren nicht mehr; Hoerer sind gepuffert)
rep('if(kzu) kzu.addEventListener("click", function(){ katLimit=10; katalogZeigen(); this.style.display="none";',
    'if(kzu) kzu.addEventListener("click", function(){ katLimit=4; katalogZeigen(); this.style.display="none";')

# Kino: 4er-Box, Altersfilter nur sekundaer, Platzhalter-Poster
alt_kino = re.search(r"function kinoZeigen\(\)\{.*?\n\}\n", s, re.S)
assert alt_kino
s = s.replace(alt_kino.group(0), '''let kinoLimit=4;
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
        (zukunft?'<span class="ribbon">Demn\\u00e4chst</span>':(neu?'<span class="ribbon neu">Neu</span>':""))+
        '<span class="fskcircle">'+(f.fsk!==""?f.fsk:"?")+'</span>'+
        '<img src="kino-platzhalter.jpg" alt="" loading="lazy" decoding="async" onerror="this.remove()">'+
      '</div>'+
      '<h3>'+f.t+'</h3>'+
      '<p class="kmeta">'+(f.dauer?f.dauer+" Min \\u00b7 ":"")+(zukunft?("Kinostart "+f.start.slice(0,6)):"jetzt im Kino")+'</p>'+
      '<a class="trailerbtn" target="_blank" rel="noopener" href="'+trailerUrl(f.t)+'">'+
      '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5.5l10 6.5-10 6.5z"/></svg>Trailer</a>'+
      '</article>';
  }).join("")+"</div>";
  const km=document.getElementById("kinoMehr"), rest=pool.length-seite.length;
  if(km){ km.style.display = rest>0 ? "" : "none";
    km.textContent = Math.min(4,rest)+" weitere anzeigen \\u2192"; }
}
''')

# Cover-Kachel statt Folgenzelle in den Katalogkarten
rep('    <div class="time"><span class="t-start">${zc1}</span><span class="t-dur">${zc2}</span></div>\n'
    '    <div class="teams">\n'
    '      <div class="t">${sticker',
    '    <div class="mthumb"><img src="cover-${({ti:"tiere",ma:"magie",ab:"abenteuer",la:"lachen",wi:"wissen"})[(e.ints||[])[0]]||"musik"}.jpg" alt="" loading="lazy" decoding="async"><span class="mfolgen">${zc1}${zc2?" "+zc2:""}</span></div>\n'
    '    <div class="teams">\n'
    '      <div class="t">${sticker')

# ==== C) CSS ================================================================
CSS = '''
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

'''
rep("  /* ---- Kompakt-Kacheln: alles sichtbar, kein Aufklappen ---- */",
    CSS + "  /* ---- Kompakt-Kacheln: alles sichtbar, kein Aufklappen ---- */")

p.write_text(s, encoding="utf-8")
print("Kinoseiten-Umbau gepatcht:", len(s), "Zeichen")
