#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Durchsucht das komplette deutsche Fernsehprogramm nach Kindersendungen.

Geht alle Sender auf tv.de durch und behält, was nach Kategorie, Titel oder
Beschreibung für Kinder geeignet ist. Ergebnis: zusatz_data.py im selben
Format wie programm_data.py. Die sechs Kindersender laufen weiterhin über
gen_programm.py und werden hier übersprungen.
"""
import datetime, re, sys
from fetch_tvde import hole
from gen_programm import GENRE, alter, minuten, tag_label

SENDER = [
    ("ard", "ARD"), ("zdf", "ZDF"), ("rtl", "RTL"), ("sat1", "SAT.1"),
    ("prosieben", "ProSieben"), ("vox", "VOX"), ("rtl-zwei", "RTLzwei"),
    ("kabel-eins", "Kabel Eins"), ("prosieben-maxx", "ProSieben Maxx"),
    ("zdf-neo", "ZDFneo"), ("wdr", "WDR"), ("ndr", "NDR"), ("br", "BR"),
    ("swr", "SWR"), ("mdr", "MDR"), ("rbb", "RBB"), ("hr", "HR"),
    ("3sat", "3sat"), ("arte", "arte"), ("rtl-nitro", "Nitro"),
    ("einsfestival", "ONE"), ("orf-1", "ORF 1"), ("srf1", "SRF 1"),
]

KATEGORIE_OK = re.compile(
    r"kinder|zeichentrick|animations|anime|trickfilm|puppentrick|märchen|"
    r"familienfilm|vorschul|jugendserie", re.I)

# Sendungen, die trotz passender Kategorie nichts für die Zielgruppe sind
SPERRE = re.compile(
    r"family guy|american dad|south park|rick and morty|simpsons|futurama|"
    r"bob's burgers|beavis|genial daneben|hot ?wheels lets race|infomercial|"
    r"demon slayer|attack on titan|jujutsu|chainsaw man|tokyo ghoul|death note|"
    r"solo leveling|berserk|hellsing|black butler|fire force|"
    r"teleshopping|axe cop|adult", re.I)

# Bekannte Kindertitel: aus unserem Katalog plus Klassiker der Vollprogramme
def bekannte_titel():
    import mediathek_data, films_data, imdb_data, json
    t = {m["title"].lower() for m in mediathek_data.MVW}
    t |= {k.lower() for k in films_data.YEARS}
    try:
        t |= {k.lower() for k in json.load(open("imdb_map.json"))}
    except Exception:
        pass
    t |= {"die sendung mit der maus", "löwenzahn", "wissen macht ah!",
          "checker tobi", "checker julia", "anna und die wilden tiere",
          "pur+", "logo!", "1, 2 oder 3", "tigerenten club", "sesamstraße",
          "die pfefferkörner", "schloss einstein", "willi wills wissen",
          "paula und die wilden tiere", "pia und die wilde natur"}
    return t

ANIME_12 = re.compile(r"one piece|naruto|dragon ball|pokémon|pokemon|detektiv conan|yu-gi-oh", re.I)


def kindgeeignet(e, bekannt):
    titel = e["titel"].lower()
    if SPERRE.search(e["titel"]) or SPERRE.search(e["kat"]):
        return None
    if titel in bekannt:
        return "titel"
    if KATEGORIE_OK.search(e["kat"]):
        return "kategorie"
    if ANIME_12.search(e["titel"]):
        return "anime"
    blob = (e["titel"] + " " + e["text"]).lower()
    if re.search(r"für kinder|kindgerecht|ab \d+ jahren erzählt", blob):
        return "text"
    return None


def baue(datum):
    d = datetime.datetime.strptime(datum, "%d.%m.%Y").date()
    label = tag_label(d)
    bekannt = bekannte_titel()
    raus = []
    for slug, name in SENDER:
        eintraege = hole(slug, datum)
        tupel = []
        for i, e in enumerate(eintraege):
            grund = kindgeeignet(e, bekannt)
            if not grund:
                continue
            if i + 1 < len(eintraege):
                dauer = minuten(eintraege[i + 1]["zeit"]) - minuten(e["zeit"])
                if dauer <= 0: dauer += 24 * 60
            else:
                dauer = 25
            if dauer > 200:      # Datenfehler oder Nachtstrecke
                continue
            g = GENRE.get(e["kat"], "Serie")
            if ANIME_12.search(e["titel"]) or "anime" in e["kat"].lower():
                a, grp = 12, "a10"
            else:
                a, grp = alter(e["titel"], g, e["zeit"])
            txt = re.sub(r"\s+", " ", e["text"]).strip()[:100]
            tupel.append((e["zeit"], e["titel"], e["sub"][:70], g, dauer, a, grp,
                          55, txt))
        if tupel:
            raus.append((label, name, tupel))
            print(f"  {label} · {name}: {len(tupel)}")
    return raus


if __name__ == "__main__":
    alle = []
    for datum in sys.argv[1:]:
        alle += baue(datum)
    with open("zusatz_data.py", "w", encoding="utf-8") as f:
        f.write('# -*- coding: utf-8 -*-\n"""Kindersendungen der Vollprogramme.\n\n'
                'Erzeugt von scan_kinder.py aus tv.de am %s. Auswahl nach Kategorie,\n'
                'bekannten Titeln und Beschreibung; Alterswerte heuristisch.\n"""\n\n'
                % datetime.date.today().strftime("%d.%m.%Y"))
        f.write("TAGE = [\n")
        for label, sender, tup in alle:
            f.write('    ("%s", "%s", [\n' % (label, sender))
            for t in tup:
                f.write("        %r,\n" % (t,))
            f.write("    ]),\n")
        f.write("]\n")
    print(f"\nzusatz_data.py: {sum(len(t) for _,_,t in alle)} Sendungen")
