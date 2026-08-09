#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Datenbestand für TVKinderprogramm.de

SENDUNGEN  – abgerufen am 30.07.2026, Sender KiKA, ab 14:35 Uhr.
             Titel, Startzeit und Genre stammen aus dem öffentlichen
             Programm des Senders. Die Dauer ist aus der Differenz zur
             Folgesendung berechnet.
             `age` (Altersempfehlung) und `score` (Eltern-Check) sind
             redaktionelle Einschätzungen — im Datensatz mit est=True
             markiert, analog zum `imp`-Flag im Transfer-Center.
             `fsk` ist bewusst None: eine FSK-Freigabe existiert nur für
             Kinofilme und Bildträger, nicht für Serienfolgen.
"""

import datetime
import re

import films_data
import programm_data
import zusatz_data
import retro_data
import imdb_data

# Kanal-Slugs bei der Quelle (für import_epg.py)
CHANNELS = {
    "kika":        "KiKA",
    "super-rtl":   "Super RTL",
    "toggo-plus":  "Toggo plus",
    "disney-channel": "Disney Channel",
    "nickelodeon": "Nickelodeon",
    "ric":         "RiC",
}

DAY = "Donnerstag, 30.07.2026"

# (Zeit, Titel, Untertitel, Genre, Dauer-Min, Alter, Gruppe, Score, Notiz)
KIKA_3007 = [
    ("14:35", "Schloss Einstein", "Erfurt · Freundschaft ist harte Arbeit", "Jugendserie", 25, 10, "a10", 68,
     "Internatsserie mit Beziehungsthemen und leichten Konflikten. Läuft seit Jahren, Einstieg mitten in der Staffel ist möglich."),
    ("15:00", "H2O – Plötzlich Meerjungfrau", "Rikko, der Clown", "Fantasyserie", 25, 10, "a10", 62,
     "Ruhige Fantasyserie ohne Schreckmomente. Thema Freundschaft und Geheimnisse."),
    ("15:25", "H2O – Plötzlich Meerjungfrau", "Blüten an Bord", "Fantasyserie", 20, 10, "a10", 62,
     "Eine Figur wird kurzzeitig festgehalten — für sehr sensible Kinder eventuell zu spannend."),
    ("15:45", "Mia and Me", "Abenteuer in Centopia · Tanzende Lichter", "Zeichentrick", 25, 6, "a6", 74,
     "Freundliche Fantasywelt, klare Gut-Böse-Struktur, keine harten Konflikte."),
    ("16:10", "Mia and Me", "Abenteuer in Centopia · Verborgene Schätze", "Zeichentrick", 20, 6, "a6", 74,
     "Suchgeschichte um ein verschwundenes Tier, löst sich freundlich auf."),
    ("16:30", "Sherlock Yack – Der Zoodetektiv", "Wer hat Sherlock umgehauen?", "Zeichentrick", 15, 6, "a6", 71,
     "Kurze Rätselgeschichten zum Mitraten. Gut geeignet, um Kinder aktiv einzubinden."),
    ("16:45", "Sherlock Yack – Der Zoodetektiv", "Wer hat beim Tapir eingesackt?", "Zeichentrick", 10, 6, "a6", 71,
     "Kurzfolge, Rätselstruktur wie zuvor. Auch einzeln verständlich."),
    ("16:55", "Garfield", "Der neue Autor", "Zeichentrick", 15, 6, "a6", 58,
     "Slapstick-Humor, hohes Tempo. Wenig Bildungsanteil, dafür kurz."),
    ("17:10", "Garfield", "Katzenwelten", "Zeichentrick", 10, 6, "a6", 58,
     "Paralleluniversum-Folge, für jüngere Kinder erzählerisch etwas verschachtelt."),
    ("17:20", "Die Schlümpfe", "Ein unwiderschlumpfliches Lächeln", "Zeichentrick", 15, 6, "a6", 66,
     "Klassiker mit ruhigem Erzähltempo. Eine Figur bricht sich ein Bein — wird harmlos aufgelöst."),
    ("17:35", "Die Schlümpfe", "Das Fliegerass", "Zeichentrick", 10, 6, "a6", 66,
     "Flugzeug gerät außer Kontrolle, endet ohne Schaden."),
    ("17:45", "Die Schlümpfe", "Ein schlumpfiger Kindergarten", "Zeichentrick", 10, 6, "a6", 66,
     "Verwandlungsgeschichte, komödiantisch und ohne Bedrohung."),
    ("17:55", "Der kleine Nick und die Ferien", "Der Papagei", "Zeichentrick", 10, 6, "a6", 72,
     "Alltagskomik im Ferienhotel. Thema: zu Unrecht beschuldigt werden — gut zum Nachbesprechen."),
    ("18:05", "Der kleine Nick und die Ferien", "Otto hat Schluckauf", "Zeichentrick", 10, 6, "a6", 72,
     "Harmlose Ferienepisode, kurze Gruselszene in einem Schiffswrack."),
    ("18:15", "Feuerwehrmann Sam", "Panik beim Picknick", "Zeichentrick", 10, 3, "a3", 79,
     "Vorschulklassiker mit vorhersehbarer Struktur: Problem, Einsatz, Lösung. Keine echte Gefahr."),
    ("18:25", "Feuerwehrmann Sam", "Die gruselige Kutschfahrt", "Zeichentrick", 10, 3, "a3", 77,
     "Ein durchgehendes Pferd sorgt für kurze Aufregung, wird schnell aufgelöst."),
    ("18:35", "Zacki und die Zoobande", "Das Geburtstagslied", "Zeichentrick", 12, 3, "a3", 78,
     "Sehr ruhig, viel Musik, Thema Zusammenarbeit. Gut für Vorschulkinder."),
    ("18:47", "Baumhaus", "An Geburtstage denken mit dem Wochenplan", "Vorlesen", 3, 3, "a3", 85,
     "Dreiminütige Übergangssendung vor dem Sandmännchen. Ruhig, mit einer Alltagsidee zum Nachmachen."),
    ("18:50", "Unser Sandmännchen", "Dr. Brumm backt Pfannkuchen", "Vorlesen", 10, 3, "a3", 88,
     "Der klassische Einschlaf-Anker. Langsames Tempo, leise Musik, feste Struktur."),
    ("19:00", "Arthur und die Freunde der Tafelrunde", "Das Fest der Kobolde", "Zeichentrick", 15, 6, "a6", 64,
     "Ritterabenteuer mit Zaubereien. Streiche statt Bedrohung, aber lauter als das Vorabendprogramm."),
    ("19:15", "Arthur und die Freunde der Tafelrunde", "Der Brunnen von Barenton", "Zeichentrick", 10, 6, "a6", 64,
     "Eine böse Fee wird befreit — leicht bedrohlicher Ton als in der Vorfolge."),
    ("19:25", "Löwenzahn", "Physik – Ein Spielplatz für Bärstadt", "Wissen", 25, 6, "a6", 89,
     "Erklärt Feder-, Flieh- und Anziehungskraft an einem Spielplatz. Hoher Sachanteil, gut zum Mitschauen."),
    ("19:50", "logo!", "Kindernachrichten", "Wissen", 10, 8, "a6", 86,
     "Deutschlands einzige tägliche Nachrichtensendung für Kinder. Je nach Weltlage können belastende Themen vorkommen — mitschauen lohnt."),
    ("20:00", "KiKA LIVE", "Kochen ohne Plan / Teil 2", "Musik & Tanz", 10, 10, "a10", 70,
     "Moderationsformat mit Koch-Challenge. Hohes Tempo, laut, aber ohne Konfliktthemen."),
    ("20:10", "Crazy Fun Park", "Vergiss mich nicht", "Jugendserie", 25, 12, "a10", 55,
     "Mystery-Serie mit Geistern und dem Thema Tod und Vergessenwerden. Für jüngere Kinder ungeeignet, ab etwa 12 gut."),
    ("20:35", "Die Regeln von Floor", "Pool", "Serie", 10, 10, "a10", 63,
     "Niederländische Comedyserie. Thema: Freundschaft aus falschen Motiven."),
    ("20:45", "Die Regeln von Floor", "Gras", "Serie", 10, 10, "a10", 52,
     "Ein Nebencharakter versucht, Drogen auf dem Schulhof zu verkaufen. Braucht ein Gespräch danach."),
    ("20:55", "Die Regeln von Floor", "Papagei", "Serie", 5, 10, "a10", 60,
     "Komödiantische Schlussfolge des Abends, Kraftausdruck als Running Gag."),
]


# --------------------------------------------------------------------------
# Toggo plus (Zeitversatz-Kanal von Super RTL), 30.07.2026, ab 14:30 Uhr.
# Werbefinanziert — fließt in den Eltern-Check ein.
TOGGO_3007 = [
    ("14:30", "Voll zu spät!", "Der Kampf der Götter", "Zeichentrick", 20, 6, "a6", 60,
     "Kurze Schulweg-Geschichten mit Mythologie-Bezug. Tempo hoch, Konflikte harmlos."),
    ("14:50", "Ninjago – Aufstieg der Drachen", "Zane und die Kapsel", "Anime", 25, 8, "a6", 52,
     "Actionlastige Ninja-Serie mit dauerhaften Kampfszenen. Für jüngere Kinder oft zu hektisch."),
    ("15:15", "ALVINNN!!! und die Chipmunks", "Endlich frei", "Zeichentrick", 10, 6, "a6", 57,
     "Slapstick-Folge um Regeln und Freiheit. Kurz, laut, ohne Tiefgang."),
    ("15:25", "ALVINNN!!! und die Chipmunks", "Gegensätze ziehen sich an", "Zeichentrick", 11, 6, "a6", 57,
     "Erfindung geht schief, Brüder bleiben aneinander hängen. Rein komödiantisch."),
    ("15:36", "ALVINNN!!! und die Chipmunks", "Das verlassene Haus", "Zeichentrick", 9, 6, "a6", 50,
     "Alvin erschreckt die anderen in einem verlassenen Haus. Kurze Gruselmomente."),
    ("15:45", "Jade Armor", "Die Sache mit dem Knöchel", "Anime", 25, 8, "a6", 55,
     "Superheldinnen-Serie im Anime-Stil mit Kampfszenen. Klare Gut-Böse-Struktur."),
    ("16:10", "Die Nektons – Abenteurer der Tiefe", "Meerjungfrauen", "Zeichentrick", 30, 6, "a6", 66,
     "Tiefsee-Abenteuer mit Familienteam. Piraten als Gegner, aber ohne echte Bedrohung."),
    ("16:40", "Willkommen bei den echten Louds", "Schöne Überraschung", "Serie", 30, 8, "a6", 58,
     "Realverfilmung der Zeichentrickserie. Thema Doppel-Date, eher für ältere Grundschulkinder."),
    ("17:10", "Pokémon Horizonte: Die Serie", "Der Plan, Rayquaza zu fangen!", "Anime", 25, 6, "a6", 61,
     "Aktuelle Pokémon-Staffel. Kämpfe sind stilisiert und ohne Verletzungen."),
    ("17:35", "Willkommen bei den Louds", "Eiskalte Lernmethoden", "Zeichentrick", 10, 6, "a6", 59,
     "Großfamilien-Comedy, hohes Tempo, viele Figuren gleichzeitig."),
    ("17:45", "Willkommen bei den Louds", "Gefährlicher Ersatz", "Zeichentrick", 10, 6, "a6", 59,
     "Band sucht Ersatz nach einer Verletzung. Freundschaftsthema, harmlos."),
    ("17:55", "Willkommen bei den Louds", "Mr. Grouse zieht aus", "Zeichentrick", 10, 6, "a6", 59,
     "Nachbar zieht wegen des Lärms weg. Ruhigste Folge des Blocks."),
    ("18:05", "Voll zu spät!", "Der verliebte Frosch", "Zeichentrick", 10, 6, "a6", 60,
     "Märchenmotiv im Schulalltag, freundlich erzählt."),
    ("18:15", "Voll zu spät!", "Der Junge aus der Zukunft", "Zeichentrick", 10, 6, "a6", 60,
     "Zeitreise-Folge. Erzählerisch etwas verschachtelt für Sechsjährige."),
    ("18:25", "Voll zu spät!", "Das Müllmonster", "Zeichentrick", 20, 6, "a6", 71,
     "Umweltthema: Was Plastik im Wasser anrichtet. Gut zum Nachbesprechen."),
    ("18:45", "Monster Loving Maniacs", "Zeitschleim", "Zeichentrick", 10, 6, "a6", 56,
     "Monster-Comedy, überzeichnet und laut, aber ohne Gruselabsicht."),
    ("18:55", "Monster Loving Maniacs", "Der Glarbergastling", "Zeichentrick", 15, 6, "a6", 56,
     "Weitere Monster-Folge im gleichen Ton."),
    ("19:10", "ALVINNN!!! und die Chipmunks", "Das Schneckenfest", "Zeichentrick", 10, 6, "a6", 57,
     "Alvin drückt sich vor Pflichten. Wiederkehrendes Muster der Serie."),
    ("19:20", "ALVINNN!!! und die Chipmunks", "Die Pizza-Drohne", "Zeichentrick", 11, 6, "a6", 57,
     "Erfindung sorgt für Chaos. Rein komödiantisch."),
    ("19:31", "ALVINNN!!! und die Chipmunks", "Die Rückkehr von Dornbertold", "Zeichentrick", 9, 6, "a6", 55,
     "Gaming-Thema, Konkurrenz zwischen den Brüdern."),
    ("19:40", "ALVINNN!!! und die Chipmunks", "Die schreienden Raupen", "Zeichentrick", 10, 6, "a6", 58,
     "Die Kinder erfahren etwas über die Vergangenheit ihres Ziehvaters."),
    ("19:50", "ALVINNN!!! und die Chipmunks", "Die verdeckte Operation", "Zeichentrick", 10, 6, "a6", 53,
     "Verwechslung mit einem Dieb und gestohlenem Geld. Braucht kurz Einordnung."),
    ("20:00", "ALVINNN!!! und die Chipmunks", "Der Zeitungsjunge", "Zeichentrick", 20, 6, "a6", 47,
     "Alvin verkauft geklaute Zeitungen weiter. Spät am Abend, Thema unehrliches Verhalten."),
    ("20:20", "Willkommen bei den echten Louds", "Epische Reinfälle", "Serie", 25, 8, "a6", 44,
     "Ein Freund bricht sich bei einem Stunt den Arm, der Unfall wird vertuscht. Später Sendeplatz."),
    ("20:45", "Woozle Goozle", "Holz", "Wissen", 30, 6, "a6", 82,
     "Wissensmagazin mit Experimenten rund um den Werkstoff Holz. Bester Sachanteil im Toggo-Programm."),
    ("21:15", "Pokémon", "Kampf um Platz acht!", "Anime", 20, 6, "a6", 50,
     "Klassische Pokémon-Folge. Um 21:15 aber weit außerhalb der üblichen Kinder-Sendezeit."),
    ("21:35", "Mr. Magoo", "Ritter Magoo / Rockstar aus dem All / Doktor Magoo", "Anime", 10, 6, "a6", 51,
     "Drei Kurzgeschichten mit Sehschwäche-Slapstick. Sehr spät im Programm."),
]

# Farbe pro Genre für die Kachel links (analog zu den Vereinsfarben)
GENRE_COLOR = {
    "Jugendserie": "#7C3AED",
    "Fantasyserie": "#0891B2",
    "Zeichentrick": "#E30613",
    "Wissen": "#15A554",
    "Vorlesen": "#2563EB",
    "Musik & Tanz": "#DB2777",
    "Serie": "#B7791F",
    "Film": "#EA580C",
    "Anime": "#0F766E",
}


CHANNEL_META = {
    "KiKA":           dict(free=True, url="https://www.kika.de/",           ads=False),
    "Super RTL":      dict(free=True, url="https://www.toggo.de/",          ads=True),
    "Toggo plus":     dict(free=True, url="https://www.toggo.de/",          ads=True),
    "Disney Channel": dict(free=True, url="https://www.disneychannel.de/",  ads=True),
    "Nickelodeon":    dict(free=True, url="https://www.nick.de/",           ads=True),
    "RiC":            dict(free=True, url="https://www.ric.tv/",            ads=True),
}


def _rows(block, channel, day=None):
    meta = CHANNEL_META.get(channel, dict(free=True, url="", ads=True))
    out = []
    for t, title, sub, genre, dur, age, grp, score, note in block:
        out.append(
            '{{day:"{day}",time:"{t}",dur:"{dur} Min",title:"{title}",sub:"{sub}",'
            'age:{age},grp:"{grp}",genres:{gs},fsk:null,genre:"{genre}",channel:"{ch}",'
            'color:"{col}",est:true,ads:{ads},'
            'ch:[{{n:"{ch}",free:{free}}}],'
            'imdb:{imdb},year:null,spaeter:{sp},retro:{retro},score:{score},note:"{note}"}}'.format(
                day=day or DAY, t=t, dur=dur,
                title=title.replace('"', '\\"'), sub=sub.replace('"', '\\"'),
                age=age, grp=grp, genre=genre, ch=channel,
                col=GENRE_COLOR.get(genre, "#2563EB"),
                ads="true" if meta["ads"] else "false",
                free="true" if films_data.ACCESS.get(channel, (True, ""))[0] else "false",
                gs=genres_js(genre),
                sp=spaeter_js(title, channel),
                imdb=(lambda v: '{r:%s,id:"%s",v:%d}' % (v[0], v[1], v[2]) if v else "null")(imdb_data.lookup(title)),
                retro=(lambda r: '{y:%d,n:"%s"}' % (r[0], r[1].replace('"', '\\"')) if r else "null")(retro_data.lookup(title)),
                score=score, note=note.replace('"', '\\"')))
    return out


def _mins(t):
    h, m = t.split(":")
    return int(h) * 60 + int(m)


# Oberkategorien: Anime ist auch Zeichentrick, Jugend- und Fantasyserie sind
# auch Serien. So laufen die Filter nicht ins Leere.
GENRE_BREIT = {
    "Anime": ["Zeichentrick"],
    "Jugendserie": ["Serie"],
    "Fantasyserie": ["Serie"],
}


def genres_js(haupt):
    alle = [haupt] + [g for g in GENRE_BREIT.get(haupt, []) if g != haupt]
    return "[" + ",".join('"%s"' % g for g in alle) + "]"


def _alle_tage():
    """Alle Tage aus programm_data plus der laufende Tag aus KIKA_3007/TOGGO_3007."""
    neu = {(l, sn) for l, sn, _ in programm_data.TAGE}
    tage = [(DAY, sn, li) for sn, li in (("KiKA", KIKA_3007), ("Toggo plus", TOGGO_3007))
            if (DAY, sn) not in neu]          # handgeschriebene Liste nur, wenn nicht importiert
    tage += list(programm_data.TAGE)
    # Kindersendungen der Vollprogramme; was schon als Film gepflegt ist, fliegt raus
    film_schluessel = {(d, t, ti) for d, t, _du, ti, *_r in films_data.FILMS}
    for label, sender, liste in zusatz_data.TAGE:
        rest = [r for r in liste if (label, r[0], r[1]) not in film_schluessel]
        if rest:
            tage.append((label, sender, rest))
    return tage


def _sortkey(label):
    m = re.search(r"(\d{2})\.(\d{2})\.(\d{4})", label)
    return datetime.date(int(m.group(3)), int(m.group(2)), int(m.group(1))) if m else datetime.date(2100, 1, 1)


DAY_ORDER = sorted({l for l, _, _ in _alle_tage()} |
                   {d for d, *_ in [(f[0],) for f in films_data.FILMS]}, key=_sortkey)


def shows_js():
    """Serien aller geladenen Tage plus Kinderfilme, chronologisch gemischt."""
    rows = []
    for label, sender, liste in _alle_tage():
        for r in liste:
            rows.append((label, _mins(r[0]), _rows([r], sender, label)[0]))
    for js, (day, t, *_rest) in zip(films_data.films_js_rows(), films_data.FILMS):
        rows.append((day, _mins(t), js))
    rows.sort(key=lambda x: (DAY_ORDER.index(x[0]) if x[0] in DAY_ORDER else 99, x[1]))
    return ("const SHOWS = [\n  " + ",\n  ".join(r[2] for r in rows) + "\n];\n"
            + "const DAY_ORDER = " + repr(DAY_ORDER).replace("'", '"') + ";")



# ---------------------------------------------------------------- Mediathek
# Standard-Streaminganbieter mit Kinderbereich. Inhalte (einzelne Titel)
# folgen später — hier steht nur, was der Anbieter für Kinder mitbringt.
MEDIA_PROVIDERS = [
    dict(name="Netflix", short="N", type="abo", price="ab 4,99 €/Mon.",
         kids="Eigener Kinderbereich mit Profilen, Altersstufen und PIN-Sperre",
         age="0–12", profiles=True, offline=True, u="https://www.netflix.com/kids"),
    dict(name="Prime Video", short="PV", type="abo", price="ab 8,99 €/Mon.",
         kids="Kinderprofile mit Altersfilter, Amazon Kids+ als Zusatzabo",
         age="3–12", profiles=True, offline=True, u="https://www.primevideo.com/"),
    dict(name="Disney+", short="D+", type="abo", price="ab 5,99 €/Mon.",
         kids="Junior-Modus für Vorschulkinder, Profil-PIN, Inhaltsstufen",
         age="0–12", profiles=True, offline=True, u="https://www.disneyplus.com/"),
    dict(name="WOW / Sky", short="SKY", type="abo", price="ab 9,99 €/Mon.",
         kids="Kids-Bereich mit Nickelodeon- und Cartoon-Network-Inhalten",
         age="3–12", profiles=True, offline=False, u="https://www.wowtv.de/"),
    dict(name="YouTube Kids", short="YT", type="frei", price="kostenlos",
         kids="Eigene App mit Altersstufen und Timer; Inhalte teils automatisch kuratiert",
         age="0–12", profiles=True, offline=False, u="https://www.youtubekids.com/"),
    dict(name="KiKA-Player", short="KiKA", type="frei", price="kostenlos",
         kids="Werbefrei, sortiert nach 3, 6 und 10 Jahren",
         age="3–13", profiles=False, offline=True, u="https://www.kika.de/"),
    dict(name="ARD Mediathek", short="ARD", type="frei", price="kostenlos",
         kids="Kinderbereich mit Sendungen aus KiKA und den Dritten",
         age="3–13", profiles=False, offline=True, u="https://www.ardmediathek.de/kinder"),
    dict(name="ZDFtivi", short="ZDF", type="frei", price="kostenlos",
         kids="Kinderangebot des ZDF, werbefrei, mit Elternbereich",
         age="3–13", profiles=False, offline=True, u="https://www.zdf.de/kinder"),
]

# ---------------------------------------------------------------------------
# Mediathek-Katalog: alle Titel aus dem Programm, entdoppelt, mit dem Ort,
# an dem sie nach der Ausstrahlung zu finden sind.
#   sure=True  → feste Regel (Öffentlich-Rechtliche stellen ihr Programm ein)
#   sure=False → in der Regel dort, aber ohne Garantie
# ---------------------------------------------------------------------------

# Markenfarben der Mediatheken und Streamer — angenähert an die Logos.
# Vor dem Livegang gegen die offiziellen Styleguides prüfen; hier steht eine
# Annäherung aus dem Gedächtnis, keine abgemessenen Werte.
PROV_COLOR = {
    "KiKA-Player":    "#5FB030",   # KiKA-Grün
    "ARD Mediathek":  "#123A8F",   # ARD-Blau
    "ZDFtivi":        "#FA7D19",   # ZDF-Orange
    "3sat":           "#E9500E",   # 3sat-Orangerot
    "Disney+":        "#0C2A6B",   # Disney+ Marineblau
    "RTL+":           "#E0004D",   # RTL+ Rotpink
    "TOGGO App":      "#F5333F",   # TOGGO-Rot
    "Joyn":           "#7B2FF7",   # Joyn-Violett
    "ORF ON":         "#E2001A",   # ORF-Rot
    # Streaming — kommen über import_tmdb.py dazu
    "Netflix":        "#E50914",   # sicher
    "Prime Video":    "#00A8E1",   # sicher
    "WOW":            "#C5008A",   # angenähert, prüfen
    "Apple TV+":      "#1C1C1E",   # angenähert
    "Paramount+":     "#0064FF",   # angenähert
    "YouTube Kids":   "#FF0000",   # sicher
}

# Welche Anbieter haben wir wirklich angebunden?
#   True  = eigene Quelle vorhanden (MediathekViewWeb)
#   False = noch keine Quelle, Einträge werden ausgeblendet
# Kostenfrei nutzbar ohne Abo?
FREI = {"KiKA-Player": True, "ARD Mediathek": True, "ZDFtivi": True, "3sat": True,
        "ORF ON": True, "YouTube Kids": True,
        "Netflix": False, "Prime Video": False, "Disney+": False, "WOW": False,
        "Apple TV+": False, "Paramount+": False, "RTL+": False, "Joyn": False,
        "TOGGO App": False}

QUELLE_DA = {
    "KiKA-Player": True, "ARD Mediathek": True, "ZDFtivi": True,
    "3sat": True, "ORF ON": True,
    "Disney+": False, "RTL+": False, "TOGGO App": False, "Joyn": False,
    "Netflix": False, "Prime Video": False, "WOW": False,
    "Apple TV+": False, "Paramount+": False, "YouTube Kids": False,
}

MEDIATHEK = {
    "KiKA":           [("KiKA-Player", True), ("ARD Mediathek", True)],
    "ZDF":            [("ZDFtivi", True)],
    "WDR":            [("ARD Mediathek", True)],
    "BR":             [("ARD Mediathek", True)],
    "MDR":            [("ARD Mediathek", True)],
    "RBB":            [("ARD Mediathek", True)],
    "3sat":           [("3sat", True)],
    "Disney Channel": [("Disney+", False)],
    "VOX":            [("RTL+", False)],
    "S-RTL":          [("RTL+", False), ("TOGGO App", False)],
    "Toggo plus":     [("RTL+", False), ("TOGGO App", False)],
    "SAT.1":          [("Joyn", False)],
    "Kabel Eins":     [("Joyn", False)],
    "ORF 1":          [("ORF ON", False)],
    "Super RTL":      [("RTL+", False), ("TOGGO App", False)],
    "Nickelodeon":    [("Paramount+", False)],
    "RiC":            [("RiC Mediathek", False)],
}


def mediathek_map_js():
    """Titel -> Mediatheken, in denen es die Sendung später gibt."""
    import json as _j
    import mediathek_data
    m = {}
    for r in mediathek_data.MVW:
        prov = [p for p in r["prov"] if QUELLE_DA.get(p, False)]
        if prov:
            m[r["title"]] = {"p": prov, "f": r["folgen"], "u": r["url"]}
    return "const NACHSEHEN = " + _j.dumps(m, ensure_ascii=False) + ";"



# ---------------------------------------------------------------------------
# "Später noch mal ansehen?" — drei Sicherheitsstufen:
#   sicher   Titel steht nachweislich in der Mediathek (aus MediathekViewWeb)
#   regel    öffentlich-rechtlicher Sender, stellt sein Programm dort ein
#   unsicher privater Sender, meist beim eigenen Dienst, ohne Garantie
# ---------------------------------------------------------------------------
OERR_SENDER = {"KiKA", "ZDF", "WDR", "RBB", "BR", "MDR", "3sat", "ORF 1"}


def spaeter(title, channel):
    import mediathek_data
    treffer = next((m for m in mediathek_data.MVW if m["title"] == title), None)
    ziele = [n for n, _ in MEDIATHEK.get(channel, []) if QUELLE_DA.get(n)]
    if treffer:
        wo = ", ".join(treffer["prov"])
        return dict(stufe="sicher", url=treffer.get("url", ""),
                    text="Ja — aktuell {0} {1} in der Mediathek ({2}).".format(
                        treffer["folgen"], "Folge" if treffer["folgen"] == 1 else "Folgen", wo))
    if channel in OERR_SENDER and ziele:
        return dict(stufe="regel", url="",
                    text="Voraussichtlich ja: {0} stellt sein Programm nach der "
                         "Ausstrahlung in die {1}, meist für 7 bis 30 Tage.".format(
                             channel, ziele[0]))
    if channel == "ORF 1":
        return dict(stufe="unsicher", url="",
                    text="In der ORF-Mediathek, aus Deutschland aber nicht abrufbar.")
    andere = [n for n, _ in MEDIATHEK.get(channel, [])]
    if andere:
        return dict(stufe="unsicher", url="",
                    text="Meist bei {0}, ohne Garantie — private Sender stellen nicht "
                         "alles ein und oft nur befristet.".format(" oder ".join(andere)))
    return dict(stufe="unsicher", url="", text="Keine Angabe zur Mediathek.")


def spaeter_js(title, channel):
    d = spaeter(title, channel)
    q = lambda x: (x or "").replace('"', '\\"')
    if d["stufe"] == "sicher":
        return '{{stufe:"sicher",text:"{0}",url:"{1}"}}'.format(q(d["text"]), q(d["url"]))
    return '{stufe:"%s"}' % d["stufe"]


def kanaele_js():
    """Empfangsangaben je Sender — einmal statt auf jeder Zeile."""
    import json as _j
    d = {}
    for n, (frei, hinweis) in films_data.ACCESS.items():
        d[n] = {"free": bool(frei), "note": hinweis,
                "u": CHANNEL_META.get(n, {}).get("url", "")}
    return "const CH_INFO = " + _j.dumps(d, ensure_ascii=False) + ";"


def en_js():
    """Englische Fassungen: Titel/Kurzbeschreibungen (Wikidata, IMDb) und
    die redaktionellen Texte aus en_texts.py."""
    import json as _j
    import en_texts
    import tipps_data
    wd = {}
    import os
    pf = os.path.join(os.path.dirname(__file__), "wikidata_en.json")
    if os.path.exists(pf):
        with open(pf, encoding="utf-8") as f:
            wd = _j.load(f)
    tips_en = []
    for de, en in zip(tipps_data.TIPPS, en_texts.TIPPS_EN):
        tips_en.append({"titel": en["titel"], "quelle": de["quelle"],
                        "text": en["text"], "haken": en["haken"],
                        "von": en["von"], "dauer": en["dauer"],
                        "alter": de["alter"], "kostenlos": de["kostenlos"],
                        "url": de.get("url", ""), "seite": de.get("seite", "beide")})
    return "const EN = " + _j.dumps({
        "t": wd.get("t", {}), "k": wd.get("k", {}),
        "n": en_texts.FILM_NOTES_EN,
        "d": en_texts.DETAILS_EN,
        "tips": tips_en}, ensure_ascii=False) + ";"


def tipps_js():
    """Elterntipps als JS-Array."""
    import json as _j
    import tipps_data
    return "const TIPPS = " + _j.dumps(tipps_data.TIPPS, ensure_ascii=False) + ";"



# ---------------------------------------------------------------------------
# Interessen-Kategorien für die Tipps-Mechanik der Mediathek.
# Codes: ab = Abenteuer & Action, ti = Tiere & Natur, ma = Magie & Fantasie,
#        la = Lachen & Quatsch,  wi = Wissen & Entdecken.
# Zuordnung über Stichworte in Titel und Beschreibung; Mehrfachnennung
# erwünscht. Genre dient als Rückfallebene, damit kein Titel leer ausgeht.
INT_WORTE = {
    "ti": ["tier", "hund", "katze", "pferd", "pony", "bär", "baer", "biene", "maja",
           "vogel", "dino", "fisch", "delfin", "pinguin", "elefant", "löwe", "affe",
           "panda", "zoo", "wald", "natur", "bauernhof", "schaf", "shaun", "koala",
           "wombat", "blinky", "dschungel", "hase", "kaninchen", "igel", "fuchs",
           "wolf", "eule", "ente", "frosch", "grizzy", "lemming", "mascha", "yakari",
           "wilde", "wildnis", "ozean", "octonaut", "paw patrol", "findus", "heidi",
           "flipper", "lassie", "käfer", "raupe", "schnecke"],
    "ma": ["hexe", "zauber", "magi", "fee", "einhorn", "vampir", "geist", "drache",
           "märchen", "prinzess", "meerjungfrau", "elfen", "troll", "dragons",
           "narnia", "fabel", "wunschpunsch", "bibi", "sabrina", "merlin", "grusel",
           "monster", "mumin", "wolkenkinder", "sterntaler", "rübezahl"],
    "ab": ["ninja", "agent", "detektiv", "pirat", "ritter", "superheld", "raumschiff",
           "weltraum", "space", "rennen", "racer", "mission", "rettung", "feuerwehr",
           "polizei", "abenteuer", "expedition", "turbo", "beyblade", "pokémon",
           "pokemon", "alarm", "ranger", "patrol", "spion", "geheim", "schatz",
           "drachenzähmen", "hot wheels", "transformers", "knight", "castle"],
    "la": ["quatsch", "spaß", "witz", "comedy", "sponge", "minions", "schlümpfe",
           "schluempfe", "tom und jerry", "tom & jerry", "angry", "oddbods",
           "chaos", "verrückt", "woozle", "bugs", "looney", "lustig", "streiche",
           "grizzy", "talking tom", "peppa", "olchis", "pumuckl"],
    "wi": ["wissen", "entdeck", "checker", "logo!", "sendung mit der maus",
           "löwenzahn", "pur+", "wow die", "forscher", "experiment", "quiz",
           "1, 2 oder 3", "erde", "weltall", "anna und die", "tigerenten",
           "schmecksplosion", "erklär", "nachrichten", "reportage", "doku"],
}
INT_GENRE = {"Wissen": "wi", "Vorlesen": "ma", "Musik & Tanz": "la",
             "Zeichentrick": "la", "Anime": "ab", "Serie": "ab",
             "Jugendserie": "ab", "Fantasyserie": "ma", "Film": "ab"}


def interessen(title, genre, *texte):
    blob = (title + " " + " ".join(x or "" for x in texte)).lower()
    treffer = [code for code, worte in INT_WORTE.items()
               if any(w in blob for w in worte)]
    if genre == "Wissen" and "wi" not in treffer:
        treffer.append("wi")
    if genre == "Fantasyserie" and "ma" not in treffer:
        treffer.append("ma")
    if not treffer:
        treffer = [INT_GENRE.get(genre, "ab")]
    return "[" + ",".join('"%s"' % c for c in treffer) + "]"


def media_js():
    """Katalog für mediathek-kinder.html — ein Eintrag je Titel."""
    import films_data, retro_data
    seen, out = {}, []

    def add(title, sub, genre, age, grp, channel, year, note):
        key = title
        if key in seen:
            for pv in MEDIATHEK.get(channel, []):
                if pv not in seen[key]["prov"]:
                    seen[key]["prov"].append(pv)
            return
        seen[key] = dict(title=title, sub=sub, genre=genre, age=age, grp=grp,
                         year=year, note=note,
                         prov=list(MEDIATHEK.get(channel, [])),
                         retro=retro_data.lookup(title))
        out.append(seen[key])

    for label, sender, liste in _alle_tage():
        for r in liste:
            add(r[1], r[2], r[3], r[5], r[6], sender, None, r[8])
    for day, t, dur, title, sub, ch, age, grp, score, note in films_data.FILMS:
        add(title, sub, "Film", age, grp, ch, films_data.YEARS.get(title), note)

    # Abo-Katalog aus TMDB, falls import_tmdb.py schon gelaufen ist
    try:
        import streaming_data
        for m in streaming_data.STREAMING:
            t = m["title"]
            neu = [(p, True) for p in m.get("prov", [])]
            if t in seen:
                for pv in neu:
                    if pv not in seen[t]["prov"]:
                        seen[t]["prov"].append(pv)
                if not seen[t].get("year"):
                    seen[t]["year"] = m.get("year")
                continue
            e = dict(title=t, sub=m.get("sub", ""), genre=m.get("genre", "Serie"),
                     age=m.get("age", 6), grp=m.get("grp", "a6"), year=m.get("year"),
                     note=m.get("note", ""), prov=neu,
                     retro=retro_data.lookup(t), src="tmdb")
            seen[t] = e
            out.append(e)
    except ImportError:
        pass

    # Mediathek-Bestand aus MediathekViewWeb dazu
    import mediathek_data
    for m in mediathek_data.MVW:
        if m["title"] in seen:
            for pv in [(n, True) for n in m["prov"]]:
                if pv not in seen[m["title"]]["prov"]:
                    seen[m["title"]]["prov"].append(pv)
            if not seen[m["title"]].get("year"):
                seen[m["title"]]["year"] = m.get("jahr")
            seen[m["title"]]["kurz"] = m.get("kurz", "")
            seen[m["title"]]["folgen"] = m["folgen"]
            seen[m["title"]]["url"] = m["url"]
            continue
        e = dict(title=m["title"], sub="", genre=m["genre"], age=m["age"], grp=m["grp"],
                 year=m.get("jahr"), note=m["note"], prov=[(n, True) for n in m["prov"]],
                 retro=retro_data.lookup(m["title"]), folgen=m["folgen"], kurz=m.get("kurz",""),
                 dauer=m["dauer"], neu=m["neu"], url=m["url"])
        seen[m["title"]] = e
        out.append(e)

    rows = []
    for e in out:
        src = e.get("src", "")
        prov = ",".join('{{n:"{0}",sure:{1},c:"{2}"{3}}}'.format(
                            n, "true" if sr else "false", PROV_COLOR.get(n, "#7A6153"),
                            (',src:"tmdb"' if src == "tmdb" else "")
                            + (",ok:true" if QUELLE_DA.get(n, False) else ",ok:false")
                            + (",frei:true" if FREI.get(n, False) else ",frei:false"))
                        for n, sr in e["prov"])
        retro = ('{{y:{0},n:"{1}"}}'.format(e["retro"][0], e["retro"][1].replace('"', '\\"'))
                 if e["retro"] else "null")
        rows.append(
            '{{title:"{t}",sub:"{s}",genre:"{g}",genres:{gs},ints:{ii},age:{a},grp:"{gr}",year:{y},'
'imdb:{im},retro:{r},prov:[{p}],folgen:{fo},dauer:{du},neu:"{ne}",url:"{ur}",kurz:"{ku}",note:"{n}"}}'.format(
                t=e["title"].replace('"', '\\"'), s=(e["sub"] or "").replace('"', '\\"'),
                g=e["genre"], gs=genres_js(e["genre"]),
                ii=interessen(e["title"], e["genre"], e.get("kurz"), e.get("note")),
                a=e["age"], gr=e["grp"], y=e["year"] or "null",
                im=(lambda v: '{{r:{0},id:"{1}",v:{2}}}'.format(*v) if v else "null")(imdb_data.lookup(e["title"])),
                fo=e.get("folgen") or "null", du=e.get("dauer") or "null",
                ku=(e.get("kurz") or "").replace('"', '\\"'),
                ne=e.get("neu",""), ur=(e.get("url") or "").replace('"', "%22"),
                r=retro, p=prov, n=(e["note"] or "").replace('"', '\\"')))
    return "const MEDIA = [\n  " + ",\n  ".join(rows) + "\n];"
