#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Patch: Tab-Umbenennung, Kino-Bereich, neue Ueberschriften, Button-Fix, Alle-Chips."""
import pathlib

p = pathlib.Path("build.py")
s = p.read_text(encoding="utf-8")


def rep(old, new, n=1):
    global s
    assert s.count(old) == n, f"Anker {old[:70]!r}: {s.count(old)}x statt {n}"
    s = s.replace(old, new)


# ---- 1) Tab umbenennen: Mediathek -> Streaming & Kino ----------------------
rep('    ("mediathek", "mediathek-kinder.html", "Mediathek",',
    '    ("mediathek", "mediathek-kinder.html", "Streaming & Kino",')
rep('  nav_live:"Heute", nav_med:"Mediathek",',
    '  nav_live:"Heute", nav_med:"Streaming & Kino",')
rep('  nav_live:"Today", nav_med:"Library",',
    '  nav_live:"Today", nav_med:"Streaming & cinema",')

# ---- 2) Ueberschriften umbenennen (Woerterbuch DE/EN) ----------------------
rep('  tipps_h2:"Tipps von Eltern f\u00fcr Eltern", mehr5:"5 weitere zeigen",',
    '  tipps_h2:"Mediathek-Tipps", mehr5:"5 weitere zeigen",')
rep('  tipps_h2:"Tips from parents, for parents", mehr5:"Show 5 more",',
    '  tipps_h2:"Library tips", mehr5:"Show 5 more",')
rep('  kat_h2:"Der ganze Katalog", titel_n:"Titel",',
    '  kat_h2:"Kostenfreie Mediathek-Inhalte", titel_n:"Titel",')
rep('  kat_h2:"The full catalogue", titel_n:"titles",',
    '  kat_h2:"Free library content", titel_n:"titles",')

# ---- 3) Neue Woerterbuch-Eintraege (Kino + Alle-Chip) ----------------------
rep('  anbieter_h:"Die Anbieter", anbieter_s:"Kinderbereich im Vergleich",',
    '  anbieter_h:"Die Anbieter", anbieter_s:"Kinderbereich im Vergleich",\n'
    '  kino_h2:"Aktuell im Kino", kino_s:"Kinderfilme auf der gro\u00dfen Leinwand",\n'
    '  kino_zeigen:"Filme anzeigen", kino_trailer:"Trailer ansehen",\n'
    '  kino_ab:"Kinostart", kino_offen:"FSK folgt", alter_alle:"Alle",')
rep('  anbieter_h:"The providers", anbieter_s:"kids sections compared",',
    '  anbieter_h:"The providers", anbieter_s:"kids sections compared",\n'
    '  kino_h2:"Now in cinemas", kino_s:"kids films on the big screen",\n'
    '  kino_zeigen:"Show films", kino_trailer:"Watch trailer",\n'
    '  kino_ab:"In cinemas from", kino_offen:"rating pending", alter_alle:"All",')

# ---- 4) Intro der Mediathek-Seite erwaehnt das Kino ------------------------
ALT_INTRO_DE = ('intro_med:"<b>Kostenlose Kinderserien und Kinderfilme</b> aus den '
                'Mediatheken von KiKA, ARD, ZDF & Co.: mit Altersempfehlung, '
                'Eltern-Check und Tipps von Eltern f\u00fcr Eltern.",')
NEU_INTRO_DE = ('intro_med:"<b>Kostenlose Kinderserien und Kinderfilme</b> aus den '
                'Mediatheken von KiKA, ARD, ZDF & Co.: mit Altersempfehlung und '
                'Eltern-Check. Dazu: die aktuellen Kinderfilme im Kino.",')
rep(ALT_INTRO_DE, NEU_INTRO_DE)
rep('intro_med:"<b>Free children\'s series and films</b> from the German public '
    'media libraries (KiKA, ARD, ZDF and more): with age recommendations, a '
    'parent check and tips from parents for parents.",',
    'intro_med:"<b>Free children\'s series and films</b> from the German public '
    'media libraries (KiKA, ARD, ZDF and more): with age recommendations and a '
    'parent check. Plus: kids films now showing in cinemas.",')
rep('<p class="intro" data-i18n="intro_med"><b>Kostenlose Kinderserien und '
    'Kinderfilme</b> aus den Mediatheken von KiKA, ARD, ZDF &amp; Co.: mit '
    'Altersempfehlung, Eltern-Check und Tipps von Eltern f\u00fcr Eltern.</p>',
    '<p class="intro" data-i18n="intro_med"><b>Kostenlose Kinderserien und '
    'Kinderfilme</b> aus den Mediatheken von KiKA, ARD, ZDF &amp; Co.: mit '
    'Altersempfehlung und Eltern-Check. Dazu: die aktuellen Kinderfilme im Kino.</p>')

# ---- 5) Statische Ueberschriften im Markup ---------------------------------
rep('<h2 data-i18n="tipps_h2">Tipps von Eltern f\u00fcr Eltern</h2>',
    '<h2 data-i18n="tipps_h2">Mediathek-Tipps</h2>')
rep('<h2 data-i18n="kat_h2">Der ganze Katalog</h2>',
    '<h2 data-i18n="kat_h2">Kostenfreie Mediathek-Inhalte</h2>')

# ---- 6) Kino-Bereich einfuegen: unter den Tipps, zugeklappt ----------------
rep('    <div class="board" id="tippBoard"></div>\n',
    '    <div class="board" id="tippBoard"></div>\n'
    '    <div class="section-eyebrow tipphead"><h2 data-i18n="kino_h2">Aktuell im Kino</h2>'
    '<span class="cnt" data-i18n="kino_s">Kinderfilme auf der gro\u00dfen Leinwand</span>  '
    '<button class="mehrbtn klein" id="kinoStart" data-i18n="kino_zeigen">Filme anzeigen</button></div>\n'
    '    <div class="klapp" id="kinoKlapp"><div class="klapp-in">\n'
    '    <div class="board" id="kinoBoard"></div>\n'
    '    </div></div>\n')

# ---- 7) Alter-Chip "Alle" auf beiden Seiten --------------------------------
# Startseite: Sentinel "all" wird vom bestehenden Handler direkt verstanden.
rep('      <div class="chiprow" id="idxAlter" role="group" aria-label="Alter">\n'
    '        <button class="fchip tmode" data-a="a3" aria-pressed="false">3\u20135</button>',
    '      <div class="chiprow" id="idxAlter" role="group" aria-label="Alter">\n'
    '        <button class="fchip tmode" data-a="all" aria-pressed="true" data-i18n="alter_alle">Alle</button>\n'
    '        <button class="fchip tmode" data-a="a3" aria-pressed="false">3\u20135</button>',
    1)
# Mediathek: leeres data-a steht fuer "kein Altersfilter".
rep('    <div class="chiprow" id="medChips" role="group" aria-label="Alter">\n'
    '      <button class="fchip tmode" data-a="a3" aria-pressed="false">3\u20135</button>',
    '    <div class="chiprow" id="medChips" role="group" aria-label="Alter">\n'
    '      <button class="fchip tmode" data-a="" aria-pressed="true" data-i18n="alter_alle">Alle</button>\n'
    '      <button class="fchip tmode" data-a="a3" aria-pressed="false">3\u20135</button>',
    1)

# Mediathek-Logik: leeres data-a setzt den Filter zurueck ...
rep('  if(b.dataset.a) zustand.age = (zustand.age===b.dataset.a) ? null : b.dataset.a;',
    '  if(b.dataset.a!==undefined) zustand.age = (b.dataset.a==="") ? null'
    ' : ((zustand.age===b.dataset.a) ? null : b.dataset.a);')
# ... und der Alle-Chip gilt als gedrueckt, wenn kein Filter aktiv ist.
rep('    b.setAttribute("aria-pressed", String(b.dataset.a===fAge)));',
    '    b.setAttribute("aria-pressed", String((b.dataset.a||null)===fAge)));')

# ---- 8) Kino-Daten und Rendering -------------------------------------------
rep('    data=lambda: providers_js() + "\\n\\n" + D.media_js()',
    '    data=lambda: kino_js() + "\\n\\n" + providers_js() + "\\n\\n" + D.media_js()')

KINO_FN = '''

def kino_js():
    """Aktuelle Kinofilme als JS-Konstante fuer die Mediathek-Seite."""
    import json, kino_data
    return ("const KINO = "
            + json.dumps(kino_data.KINO, ensure_ascii=False, separators=(",", ":"))
            + ";\\nconst KINO_STAND = " + json.dumps(kino_data.STAND) + ";")

'''
rep("def providers_js():", KINO_FN.lstrip("\n") + "\ndef providers_js():")

# Rendering + Klick-Logik ans Ende des Mediathek-page_js haengen (vor reRender).
rep('document.getElementById("anbStart").addEventListener("click", function(){\n'
    '  document.getElementById("anbKlapp").classList.add("auf");\n'
    '  this.style.display="none";\n'
    '});',
    'document.getElementById("anbStart").addEventListener("click", function(){\n'
    '  document.getElementById("anbKlapp").classList.add("auf");\n'
    '  this.style.display="none";\n'
    '});\n'
    '\n'
    '/* ---- Aktuell im Kino ---- */\n'
    'function trailerUrl(titel){\n'
    '  const w = (typeof LANG!=="undefined" && LANG==="en") ? "Trailer Englisch" : "Trailer Deutsch";\n'
    '  return "https://www.youtube.com/results?search_query=" + encodeURIComponent(titel + " " + w);\n'
    '}\n'
    'function kinoZeigen(){\n'
    '  const kb=document.getElementById("kinoBoard"); if(!kb) return;\n'
    '  const en = (typeof LANG!=="undefined" && LANG==="en");\n'
    '  const heute=new Date(); heute.setHours(0,0,0,0);\n'
    '  const dat = s=>{ const m=s.split("."); return new Date(+m[2], +m[1]-1, +m[0]); };\n'
    '  kb.innerHTML = KINO.map(f=>{\n'
    '    const zukunft = dat(f.start) > heute;\n'
    '    const b=[];\n'
    '    b.push(\'<span class="kinobadge">\'+(f.fsk!=="" ? "FSK "+f.fsk : t("kino_offen"))+"</span>");\n'
    '    if(f.dauer) b.push(\'<span class="kinobadge">\'+f.dauer+" Min</span>");\n'
    '    if(zukunft) b.push(\'<span class="kinobadge neu">\'+t("kino_ab")+" "+f.start+"</span>");\n'
    '    return \'<article class="kinorow">\'+\n'
    '      "<h3>"+f.t+"</h3>"+\n'
    '      \'<p class="kinometa">\'+b.join("")+"</p>"+\n'
    '      \'<p class="kinodesc">\'+(en ? f.kurz_en : f.kurz)+"</p>"+\n'
    '      \'<a class="trailerbtn" target="_blank" rel="noopener" href="\'+trailerUrl(f.t)+\'">\'+\n'
    '      \'<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5.5l10 6.5-10 6.5z"/></svg>\'+\n'
    '      t("kino_trailer")+"</a></article>";\n'
    '  }).join("");\n'
    '}\n'
    'document.getElementById("kinoStart").addEventListener("click", function(){\n'
    '  kinoZeigen();\n'
    '  document.getElementById("kinoKlapp").classList.add("auf");\n'
    '  this.style.display="none";\n'
    '});')

# Sprachwechsel: offenen Kino-Bereich in der neuen Sprache neu zeichnen.
rep('window.reRender = ()=>{\n  katalogZeigen();',
    'window.reRender = ()=>{\n  katalogZeigen();\n'
    '  if(document.getElementById("kinoKlapp").classList.contains("auf")) kinoZeigen();')

# ---- 9) Button-Grafiken: weisser Kasten weg, Anordnung robuster ------------
rep('  .imgbtn img{height:40px; width:auto; display:block; border-radius:9px;\n'
    '    box-shadow:0 1px 4px rgba(58,42,32,.18); transition:transform .12s}',
    '  .imgbtn img{height:44px; width:auto; display:block; border-radius:0;\n'
    '    filter:drop-shadow(0 1px 3px rgba(58,42,32,.22)); transition:transform .12s}')
rep('  .section-eyebrow.tipphead{display:flex; align-items:center; gap:10px}',
    '  .section-eyebrow.tipphead{display:flex; align-items:center; gap:10px; flex-wrap:wrap; row-gap:8px}')

# ---- 10) Kino-Kartenstile ---------------------------------------------------
rep('  .tippnote{font-size:12.5px; color:var(--muted); margin:0 2px 8px; min-height:0}',
    '  .kinorow{border:1px solid var(--line2); border-radius:14px; background:var(--surface);\n'
    '    padding:12px 14px 13px; margin:0 0 10px}\n'
    '  .kinorow h3{font-family:"Archivo",sans-serif; font-size:14.5px; font-weight:800;\n'
    '    letter-spacing:-.01em; color:var(--ink); margin:0 0 7px}\n'
    '  .kinometa{display:flex; flex-wrap:wrap; gap:6px; margin:0 0 8px}\n'
    '  .kinobadge{font-family:"JetBrains Mono",monospace; font-size:10px; font-weight:600;\n'
    '    letter-spacing:.05em; color:var(--muted); border:1px solid var(--line2);\n'
    '    border-radius:var(--r-ctl); padding:3px 7px}\n'
    '  .kinobadge.neu{color:#8A5A00; border-color:#D9A94E; background:rgba(217,169,78,.14)}\n'
    '  .kinodesc{font-size:12.5px; color:var(--muted); line-height:1.62; margin:0 0 10px}\n'
    '  .trailerbtn{display:inline-flex; align-items:center; gap:7px; padding:8px 13px;\n'
    '    border:1px solid var(--line2); border-radius:var(--r-ctl); background:none;\n'
    '    color:var(--ink); font-family:"Inter",sans-serif; font-size:12px; font-weight:650;\n'
    '    text-decoration:none}\n'
    '  .trailerbtn svg{width:13px; height:13px; color:#F1571A}\n'
    '  .trailerbtn:hover{border-color:#F1571A}\n'
    '\n'
    '  .tippnote{font-size:12.5px; color:var(--muted); margin:0 2px 8px; min-height:0}')

p.write_text(s, encoding="utf-8")
print("build.py gepatcht:", len(s), "Zeichen")
