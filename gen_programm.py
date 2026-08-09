#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Erzeugt programm_data.py aus tv.de für mehrere Tage und Sender."""
import datetime, re, sys
from fetch_tvde import hole

SENDER = [("kika", "KiKA"), ("super-rtl", "Super RTL"), ("toggo-plus", "Toggo plus"),
          ("disney-channel", "Disney Channel"), ("nickelodeon", "Nickelodeon"), ("ric", "RiC")]
WT = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

GENRE = {
    "Animationsserie": "Zeichentrick", "Zeichentrickserie": "Zeichentrick",
    "Trickfilm": "Zeichentrick", "Animationsfilm": "Zeichentrick",
    "Anime": "Anime", "Animeserie": "Anime",
    "Kinderserie": "Serie", "Serie": "Serie", "Jugendserie": "Jugendserie",
    "Kindersendung": "Vorlesen", "Vorschulserie": "Vorlesen",
    "Kindermagazin": "Wissen", "Magazin": "Wissen", "Nachrichten": "Wissen",
    "Dokumentation": "Wissen", "Wissensmagazin": "Wissen", "Reportage": "Wissen",
    "Spielfilm": "Film", "Kinderfilm": "Film", "Familienfilm": "Film",
    "Musiksendung": "Musik & Tanz", "Fantasyserie": "Fantasyserie",
}
VORSCHUL = ("Kikaninchen", "Sandmänn", "Baumhaus", "ENE MENE", "Nö-Nö", "Bobo",
            "Conni", "Rabe Socke", "Elefanten", "Shaun", "Gabby", "Hello Kitty",
            "Billy", "Peppa", "Pettersson", "Lieselotte", "Odo")
AELTER = ("Schloss Einstein", "H2O", "logo", "Pfefferkörner", "lausige Hexe",
          "Timster", "Crazy Fun Park", "Surviving", "Chi Rho", "Dance Academy")


# Läuft auf Kindersendern, ist aber keins: 80er-Krimiserie, Teleshopping
SPERRE = re.compile(r"^T&T$|^T & T$|infomercial|teleshopping|dauerwerbesendung", re.I)


def minuten(z):
    return int(z[:2]) * 60 + int(z[3:])


def alter(titel, genre, zeit):
    if any(v.lower() in titel.lower() for v in VORSCHUL):
        return 3, "a3"
    if any(v.lower() in titel.lower() for v in AELTER):
        return 10, "a10"
    if minuten(zeit) < 8 * 60:
        return 3, "a3"
    if minuten(zeit) >= 20 * 60 or genre in ("Jugendserie",):
        return 10, "a10"
    return 6, "a6"


def score(genre, sender, zeit, dauer):
    s = 60
    if genre == "Wissen": s += 25
    if genre == "Vorlesen": s += 12
    if sender in ("KiKA",): s += 8
    elif sender in ("Super RTL", "Toggo plus", "Nickelodeon", "RiC"): s -= 6
    else: s -= 2
    if minuten(zeit) >= 20 * 60: s -= 10
    if dauer and dauer <= 12: s += 4
    return max(20, min(95, s))


def tag_label(d):
    return "%s, %s" % (WT[d.weekday()], d.strftime("%d.%m.%Y"))


def baue(datum):
    d = datetime.datetime.strptime(datum, "%d.%m.%Y").date()
    label = tag_label(d)
    raus = []
    for slug, name in SENDER:
        eintraege = hole(slug, datum)
        if not eintraege:
            print("  ! nichts für", name, datum); continue
        tupel = []
        eintraege = [e for e in eintraege
                     if not (SPERRE.search(e["titel"]) or SPERRE.search(e["kat"]))]
        for i, e in enumerate(eintraege):
            if i + 1 < len(eintraege):
                dauer = minuten(eintraege[i + 1]["zeit"]) - minuten(e["zeit"])
                if dauer <= 0: dauer += 24 * 60
            else:
                dauer = 25
            g = GENRE.get(e["kat"], "Serie")
            a, grp = alter(e["titel"], g, e["zeit"])
            txt = re.sub(r"\s+", " ", e["text"]).strip()
            if txt.startswith(e["sub"]): txt = txt[len(e["sub"]):].strip(" :–—")
            tupel.append((e["zeit"], e["titel"], e["sub"][:70], g, dauer, a, grp,
                          score(g, name, e["zeit"], dauer), txt[:100]))
        raus.append((label, name, tupel))
        print(f"  {label} · {name}: {len(tupel)} Sendungen")
    return raus


if __name__ == "__main__":
    alle = []
    for datum in sys.argv[1:]:
        alle += baue(datum)
    with open("programm_data.py", "w", encoding="utf-8") as f:
        f.write('# -*- coding: utf-8 -*-\n"""\n'
                'programm_data.py — Sendungen von KiKA und Toggo plus\n\n'
                'Erzeugt von gen_programm.py aus tv.de. Abgerufen am %s.\n'
                'Altersempfehlung und Eltern-Check sind heuristisch gesetzt\n'
                '(Sendeplatz, Genre, Sender) und redaktionell zu prüfen.\n"""\n\n'
                % datetime.date.today().strftime("%d.%m.%Y"))
        f.write("TAGE = [\n")
        for label, sender, tup in alle:
            f.write('    ("%s", "%s", [\n' % (label, sender))
            for t in tup:
                f.write("        %r,\n" % (t,))
            f.write("    ]),\n")
        f.write("]\n")
    print(f"\nprogramm_data.py: {sum(len(t) for _,_,t in alle)} Sendungen aus {len(alle)} Blöcken")
