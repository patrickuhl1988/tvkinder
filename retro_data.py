# -*- coding: utf-8 -*-
"""
retro_data.py — „Kennst du noch?"

Eltern von Grundschulkindern sind 2026 grob zwischen 30 und 45, haben ihre
Kindheit also zwischen Mitte der 80er und Mitte der 2000er verbracht. Aus dem
vorhandenen Programm sind das die Titel, die sie selbst gesehen haben.

Aufgenommen wurde nur, wo ich mir beim Ursprungsjahr sicher bin. Titel, bei denen
ich hätte raten müssen, fehlen bewusst — die Liste wächst mit jedem Import.

    Titel -> (Ursprungsjahr, Notiz für Eltern)
"""

RETRO = {
    # --- Serien -----------------------------------------------------------
    "Unser Sandmännchen": (1959,
        "Läuft seit 1959 und damit schon bei den Großeltern. Das Ritual vor dem Schlafengehen schlechthin."),
    "Die Schlümpfe": (1981,
        "Die Zeichentrickserie startete 1981, im deutschen Fernsehen lief sie durch die ganzen 80er."),
    "Löwenzahn": (1981,
        "Seit 1981, jahrzehntelang mit Peter Lustig im Bauwagen. Die heutige Folge stammt aus den Classics."),
    "Alvinnn!!! und die Chipmunks": (1983,
        "Die Chipmunks gibt es als Zeichentrickserie seit 1983 — die aktuelle Fassung ist eine Neuauflage."),
    "ALVINNN!!! und die Chipmunks": (1983,
        "Die Chipmunks gibt es als Zeichentrickserie seit 1983 — die aktuelle Fassung ist eine Neuauflage."),
    "Feuerwehrmann Sam": (1987,
        "Der walisische Feuerwehrmann fährt seit 1987 nach Pontypandy aus."),
    "logo!": (1989,
        "Deutschlands Kindernachrichten seit 1989 — viele Eltern haben damit selbst die Welt erklärt bekommen."),
    "Schloss Einstein": (1998,
        "Läuft seit 1998 ununterbrochen. Wer in den Nullerjahren Kind war, kennt mindestens eine Staffel."),
    "Pokémon": (1999,
        "Kam 1999 ins deutsche Fernsehen und hat eine ganze Generation durch die Grundschule begleitet."),
    "Pokémon Horizonte: Die Serie": (1999,
        "Aktuelle Staffel der Reihe, die 1999 im deutschen Fernsehen startete."),
    "H2O – Plötzlich Meerjungfrau": (2006,
        "Australische Serie von 2006 — Pflichtprogramm für alle, die um 2010 in der Grundschule waren."),
    "Mr. Magoo": (1949,
        "Die Figur stammt aus dem Jahr 1949, die Kurzfilme liefen in Deutschland über Jahrzehnte."),
    "Garfield": (1978,
        "Der Comic startete 1978, im deutschen Fernsehen lief der Kater ab den 80ern."),

    # --- Filme ------------------------------------------------------------
    "Pippi Langstrumpf": (1969,
        "Die schwedische Verfilmung von 1969 mit Inger Nilsson — bei drei Generationen im Wohnzimmer gelaufen."),
    "Heidi": (1974,
        "Die japanische Zeichentrickserie von 1974 prägte das Heidi-Bild in ganz Europa."),
    "Arielle, die Meerjungfrau": (1989,
        "Disneys Wendepunkt von 1989, der die große Zeichentrick-Renaissance einleitete."),
    "Tom Turbo": (1993,
        "Thomas Brezinas Fahrrad-Detektiv fährt seit 1993 durch den ORF."),
    "Charlie & Louise": (1994,
        "Deutsche Kästner-Adaption von 1994 mit den Zwillingen Floriane und Fritzi Eichhorn."),
    "Hans im Glück": (1998,
        "Märchenverfilmung von 1998, ein Fixpunkt im Feiertagsprogramm der Dritten."),
    "Der König der Löwen 2": (1998,
        "Die Fortsetzung von 1998 kam direkt auf Video — für viele die erste eigene Kassette."),
    "Pünktchen und Anton": (1999,
        "Caroline Links Neuverfilmung von 1999, gedreht mit Elea Geissler und Max Felder."),
    "Der Schuh des Manitu": (2001,
        "Der Kinohit von 2001. Nostalgie für die Eltern — für die Kinder aber kein Kinderfilm."),
    "Himmel und Huhn": (2005,
        "Disneys erster vollständig computeranimierter Film ohne Pixar, von 2005."),
    "Bolt": (2008,
        "Von 2008 — der Film, mit dem Disney Animation wieder Fahrt aufnahm."),
}


# ---------------------------------------------------------------------------
# Automatische Ergänzung aus Wikidata: Reihen, die 2006 oder früher gestartet
# sind, haben heutige Eltern mit hoher Wahrscheinlichkeit selbst gesehen.
# Die handgeschriebenen Notizen oben haben Vorrang; für den Rest wird ein
# neutraler Satz erzeugt und mit auto=True gekennzeichnet.
# ---------------------------------------------------------------------------
import json
import os

_WD = {}
_pfad = os.path.join(os.path.dirname(__file__), "wikidata_years.json")
if os.path.exists(_pfad):
    with open(_pfad, encoding="utf-8") as _f:
        _WD = {k: v for k, v in json.load(_f).items() if v and 1955 <= v <= 2006}

GRENZE = 2006


def lookup(title):
    """Gibt (Jahr, Notiz) oder None zurück. Handgeschriebenes zuerst."""
    if title in RETRO:
        return RETRO[title]
    j = _WD.get(title)
    if j:
        return (j, "Den Stoff gibt es seit %d — gut möglich, dass Eltern ihn aus "
                   "der eigenen Kindheit kennen. Gesendet wird eine neuere "
                   "Fassung. (Jahr aus Wikidata)" % j)
    return None


def ist_handgeprueft(title):
    return title in RETRO
