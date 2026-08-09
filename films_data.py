# -*- coding: utf-8 -*-
"""
Kinderfilme im TV, abgerufen 30.07.2026 (beide Ergebnisseiten).
Titel, Sender, Tag und Sendezeit sind übernommen; die Dauer ist aus der
angegebenen Von-Bis-Zeit berechnet.

`age` und `score` sind redaktionelle Einschätzungen (est=True).
`fsk` steht überall auf None — siehe Hinweis in der README: bei Filmen gibt es
eine echte FSK-Freigabe, die vor dem Livegang einmal in der offiziellen
Freigabedatenbank nachgeschlagen werden muss. Geratene Altersfreigaben haben
auf einer Elternseite nichts verloren.
"""

# (Tag, Zeit, Dauer-Min, Titel, Untertitel, Sender, Alter, Gruppe, Score, Notiz)
FILMS = [
    ("Donnerstag, 30.07.2026", "20:15", 175, "Die Chroniken von Narnia", "Prinz Kaspian von Narnia", "Disney Channel", 10, "a10", 62,
     "Zweiter Teil der Fantasy-Reihe mit großen Schlachtszenen. Für Grundschulkinder stellenweise zu düster, Ende weit nach 23 Uhr."),
    ("Freitag, 31.07.2026", "07:40", 90, "Das doppelte Lottchen", "Spielfilm, Deutschland 2017", "WDR", 6, "a6", 78,
     "Kästner-Klassiker um Zwillinge im Ferienheim. Ruhig erzählt, Trennung der Eltern als Thema."),
    ("Freitag, 31.07.2026", "18:40", 95, "Baymax", "Riesiges Robowabohu", "Disney Channel", 8, "a6", 76,
     "Oscar-prämiertes Animationsabenteuer. Der Tod des älteren Bruders wird offen behandelt — braucht bei jüngeren Kindern Begleitung."),
    ("Freitag, 31.07.2026", "20:15", 115, "Bolt", "Ein Hund für alle Fälle", "Disney Channel", 6, "a6", 74,
     "Hund hält seine Serienrolle für echt. Warmherzig, ein paar Verfolgungsszenen."),
    ("Freitag, 31.07.2026", "22:10", 180, "Die Chroniken von Narnia", "Prinz Kaspian von Narnia (Wiederholung)", "Disney Channel", 10, "a10", 55,
     "Zweite Ausstrahlung des Tages, Beginn 22:10 und Ende um 1:10 nachts. Praktisch nur zum Aufnehmen."),
    ("Samstag, 01.08.2026", "08:15", 25, "Tom Turbo", "Das Geheimnis des Pinguins", "ORF 1", 6, "a6", 72,
     "Interaktive Krimiserie: Tom Turbo stellt zwischendurch Fragen und wartet auf Antworten — Kinder rufen ins Zimmer, was sie gesehen haben. Genau 25 Minuten, klare Struktur, keine bedrohlichen Szenen. Gut für Kinder, die beim Fernsehen sonst wegdriften, weil das Format Mitdenken verlangt. Für deutsche Zuschauer nur über Satellit oder Stream erreichbar."),
    ("Samstag, 01.08.2026", "08:20", 85, "Bolt", "Ein Hund für alle Fälle", "Disney Channel", 6, "a6", 74,
     "Ein Hund glaubt, seine Serienrolle sei echt, und muss lernen, dass er ganz normal ist. Das Thema — jemand verliert seine vermeintlichen Superkräfte und ist trotzdem genug — trägt gut. Zwei Verfolgungsszenen und ein Feuer am Ende können Vierjährige kurz mitnehmen, lösen sich aber sofort auf. Warmherzig erzählt, kein Zynismus."),
    ("Samstag, 01.08.2026", "09:35", 25, "Pippi Langstrumpf", "Pippi auf großer Ballonfahrt", "ZDF", 6, "a6", 80,
     "Der Klassiker in Serienlänge, ruhig und ohne Schnittgewitter. Pippi macht, was sie will, und das ist Teil des Reizes — manche Kinder testen danach Grenzen aus. Die Kehrseite: Pippi lebt allein, ihre Mutter ist tot und der Vater weit weg. Für sensible Kinder ein Thema, über das man reden sollte."),
    ("Samstag, 01.08.2026", "10:00", 25, "Pippi Langstrumpf", "Pippi und die Flaschenpost", "ZDF", 6, "a6", 80,
     "Der Klassiker in Serienlänge, ruhig und ohne Schnittgewitter. Pippi macht, was sie will, und das ist Teil des Reizes — manche Kinder testen danach Grenzen aus. Die Kehrseite: Pippi lebt allein, ihre Mutter ist tot und der Vater weit weg. Für sensible Kinder ein Thema, über das man reden sollte."),
    ("Samstag, 01.08.2026", "10:25", 70, "Hans im Glück", "Spielfilm, Deutschland 1998", "RBB", 6, "a6", 74,
     "Märchenverfilmung von 1998, langsam erzählt und mit langen Einstellungen. Die Moral — Besitz gegen Leichtigkeit tauschen — ist für Sechsjährige nicht selbsterklärend und lohnt ein Gespräch danach. Keine Gruselszenen, kein Zeitdruck, gut geeignet für einen verregneten Samstagvormittag."),
    ("Samstag, 01.08.2026", "18:45", 90, "Findet Dorie", "", "Disney Channel", 6, "a6", 82,
     "Fortsetzung von Findet Nemo, in der eine vergesslicheit Fischdame ihre Eltern sucht. Der Film behandelt Vergesslichkeit als Behinderung sehr freundlich und ohne Häme. Zwei Stellen sind bang: Dorie verliert sich als Kind, und im Aquarium droht kurz der Abtransport. Beides löst sich glücklich auf. Ab sechs gut allein zu schauen, jüngere brauchen jemanden daneben."),
    ("Samstag, 01.08.2026", "20:15", 105, "Minions", "", "VOX", 6, "a6", 66,
     "Slapstick fast ohne Handlung, dafür mit hohem Tempo und viel Krach. Als Belohnungsfilm für einen langen Tag funktioniert er, als Vorlage für ruhiges Spielen danach eher nicht. Gewalt ist durchweg cartoonhaft, es passiert niemandem wirklich etwas. Kinder kommen aufgedreht heraus — kein Film für kurz vor dem Schlafengehen, zumal er um 20:15 startet."),
    ("Samstag, 01.08.2026", "20:15", 115, "Charlie & Louise", "", "S-RTL", 8, "a6", 72,
     "Zwillinge, die getrennt aufwachsen und sich zufällig treffen, wollen ihre Eltern wieder zusammenbringen. Die Trennung der Eltern wird ernsthaft verhandelt, nicht weggelacht — für Kinder aus Trennungsfamilien kann das sehr nah sein, im guten wie im schwierigen Sinn. Gedreht 1994, entsprechend ruhig geschnitten."),
    ("Samstag, 01.08.2026", "20:15", 100, "Arielle, die Meerjungfrau", "", "Disney Channel", 6, "a6", 75,
     "Disneys Klassiker über eine Meerjungfrau, die Mensch werden will. Die Meerhexe Ursula ist für unter Sechsjährige der kritische Punkt: große Gestalt, dunkle Szene, laute Musik. Ältere finden sie eher großartig. Erzählerisch ist der Film schnell und die Musiknummern tragen — deshalb funktioniert er auch beim fünften Mal noch."),
    ("Samstag, 01.08.2026", "22:10", 130, "Pünktchen und Anton", "", "S-RTL", 8, "a6", 76,
     "Caroline Links Kästner-Verfilmung über zwei Kinder aus sehr unterschiedlichen Verhältnissen. Soziale Ungleichheit wird ohne erhobenen Zeigefinger gezeigt, das trägt bis in die vierte Klasse hinein. Inhaltlich einer der stärksten Titel der Woche — der Sendeplatz um 22:10 ist für die Zielgruppe allerdings völlig verfehlt, das ist ein Aufnahmefilm."),
    ("Samstag, 01.08.2026", "22:35", 110, "Der Schuh des Manitu", "Extra Large", "SAT.1", 12, "a10", 34,
     "Steht in der Liste, weil die Quelle ihn als Familienfilm führt. Das ist er nicht. Westernparodie mit derbem Humor, Anspielungen für Erwachsene und einer Darstellung indigener Figuren, die heute zu Recht diskutiert wird. Sendeplatz 22:35. Für Kinder ungeeignet, für einen Elternabend auf dem Sofa dagegen genau richtig."),
    ("Sonntag, 02.08.2026", "04:00", 120, "Mary Poppins' Rückkehr", "", "ORF 1", 6, "a6", 70,
     "Fortsetzung des Klassikers mit Emily Blunt, aufwendig ausgestattet und mit vielen Musiknummern. Im Kern geht es um eine Familie nach dem Tod der Mutter — das wird warm, aber nicht ausweichend erzählt. Zwei Stunden Laufzeit sind für Sechsjährige viel. Der eigentliche Haken ist der Sendeplatz: 4 Uhr nachts, das ist reine Aufnahmeware."),
    ("Sonntag, 02.08.2026", "06:30", 100, "Ostwind (3)", "Aufbruch nach Ora", "WDR", 8, "a6", 77,
     "Dritter Teil der Pferdefilmreihe, diesmal mit einer Reise nach Andalusien. Freundschaft, Verantwortung für ein Tier und das Aushalten von Konflikten unter Jugendlichen. Es gibt eine Szene mit einem verletzten Pferd, die Tierliebhabern naheght. Wer die ersten beiden Teile nicht kennt, kommt trotzdem mit."),
    ("Sonntag, 02.08.2026", "08:35", 80, "Arielle, die Meerjungfrau", "", "Disney Channel", 6, "a6", 75,
     "Disneys Klassiker über eine Meerjungfrau, die Mensch werden will. Die Meerhexe Ursula ist für unter Sechsjährige der kritische Punkt: große Gestalt, dunkle Szene, laute Musik. Ältere finden sie eher großartig. Erzählerisch ist der Film schnell und die Musiknummern tragen — deshalb funktioniert er auch beim fünften Mal noch."),
    ("Sonntag, 02.08.2026", "09:00", 60, "Das Märchen von der silbernen Brücke", "Spielfilm, Deutschland 2024", "BR", 6, "a6", 76,
     "Neues ARD-Weihnachtsmärchen von 2024, hier als Sommerwiederholung. Klassische Struktur: Aufgabe, Prüfung, gutes Ende. Eine Stunde Laufzeit ist angenehm kurz. Wie bei allen Märchenfilmen gibt es eine bedrohliche Figur, die aber klar als Rolle erkennbar bleibt. Solide Sonntagvormittagsware."),
    ("Sonntag, 02.08.2026", "09:55", 75, "Himmel und Huhn", "", "Disney Channel", 6, "a6", 65,
     "Disneys erster CGI-Film ohne Pixar, und man merkt es. Sehr hohes Tempo, viele Gags, wenig Ruhe. Im Hintergrund läuft die Geschichte eines Vaters, der seinem Sohn nicht glaubt — das ist der wertvollste Teil, geht im Trubel aber unter. Für Kinder, die schnelle Bilder mögen; für ruhige eher nicht."),
    ("Sonntag, 02.08.2026", "10:00", 90, "Angry Birds – Der Film", "", "ORF 1", 6, "a6", 60,
     "Verfilmung der Handy-App. Der Held ist wütend und wird dafür ausgegrenzt, am Ende rettet genau diese Wut alle — eine Botschaft, die man mit dem Kind einordnen sollte. Viel Zerstörung als Running Gag, ein paar Anspielungen für Erwachsene. Erzählerisch dünn, unterhält aber verlässlich."),
    ("Sonntag, 02.08.2026", "13:00", 80, "Ritter Rost 2", "Das Schrottkomplott", "KiKA", 6, "a6", 74,
     "Deutscher Animationsfilm mit Musiknummern, gemächlich erzählt und ohne Härte. Thema ist ein Königreich in der Pleite und die Frage, woran man spart — überraschend nah an dem, was Kinder aus Familiengesprächen kennen. Läuft werbefrei bei KiKA auf einem guten Sonntagsplatz. Für Vor- und Grundschulkinder gleichermaßen brauchbar."),
    ("Sonntag, 02.08.2026", "15:20", 100, "Minions", "", "VOX", 6, "a6", 66,
     "Slapstick fast ohne Handlung, dafür mit hohem Tempo und viel Krach. Als Belohnungsfilm für einen langen Tag funktioniert er, als Vorlage für ruhiges Spielen danach eher nicht. Gewalt ist durchweg cartoonhaft, es passiert niemandem wirklich etwas. Kinder kommen aufgedreht heraus — kein Film für kurz vor dem Schlafengehen, zumal er um 20:15 startet."),
    ("Sonntag, 02.08.2026", "15:25", 60, "Dornröschen", "Spielfilm, Deutschland 2009", "MDR", 6, "a6", 76,
     "Grimm-Verfilmung aus der ARD-Märchenreihe von 2009. Eine Stunde, ruhig inszeniert, mit der bekannten Fluch-und-Erlösung-Struktur. Die böse Fee ist deutlich als Märchenfigur gezeichnet und erschreckt kaum. Weil die Handlung bekannt ist, funktioniert der Film gut zum Nebenbeischauen mit jüngeren Geschwistern."),
    ("Sonntag, 02.08.2026", "15:30", 100, "Heidi", "Spielfilm", "3sat", 6, "a6", 84,
     "Der Stoff von Johanna Spyri, hier in einer Spielfilmfassung. Heimweh, ein strenger Großvater und ein Kind, das aus seiner vertrauten Umgebung gerissen wird — inhaltlich stärker, als man erwartet, und für Kinder mit Trennungsängsten spürbar. Landschaftsbilder und Tempo sind ruhig. Hinweis: Die Quelle nennt widersprüchliche Jahresangaben, welche Fassung läuft, ist unklar."),
    ("Sonntag, 02.08.2026", "16:30", 90, "Der Zauberlehrling", "Spielfilm, Deutschland 2017", "MDR", 8, "a6", 74,
     "Märchenverfilmung von 2017 über Zauberei, Machtmissbrauch und die Frage, wem man vertraut. Etwas düsterer und erwachsener als die Standard-ARD-Märchen, mit einem Antagonisten, der wirklich bedrohlich wirkt. Ab acht gut, darunter zu dicht. Neunzig Minuten am Sonntagnachmittag."),
    ("Sonntag, 02.08.2026", "18:35", 100, "Bolt", "Ein Hund für alle Fälle", "Disney Channel", 6, "a6", 74,
     "Ein Hund glaubt, seine Serienrolle sei echt, und muss lernen, dass er ganz normal ist. Das Thema — jemand verliert seine vermeintlichen Superkräfte und ist trotzdem genug — trägt gut. Zwei Verfolgungsszenen und ein Feuer am Ende können Vierjährige kurz mitnehmen, lösen sich aber sofort auf. Warmherzig erzählt, kein Zynismus."),
    ("Sonntag, 02.08.2026", "20:15", 100, "Der König der Löwen 2", "Simbas Königreich", "Disney Channel", 6, "a6", 71,
     "Direct-to-Video-Fortsetzung um Simbas Tochter und einen Konflikt zwischen zwei Löwenrudeln. Romeo-und-Julia-Motiv, überraschend ernst geführt, mit mehreren Kampfszenen und einem Feuer. Für sensible Kinder stellenweise heftig, für Fans des ersten Teils eine willkommene Fortsetzung. Startet um 20:15, Ende gegen 22 Uhr."),
    ("Mittwoch, 05.08.2026", "20:15", 135, "Jim Knopf und Lukas der Lokomotivführer", "", "Kabel Eins", 6, "a6", 80,
     "Aufwendige Verfilmung des Michael-Ende-Klassikers mit echten Schauplätzen und viel Ausstattung. Freundschaft, Herkunft und die Frage, wo man hingehört — das trägt über zwei Stunden. Der Scheinriese und der Drache sind die zwei Stellen, an denen jüngere Kinder kurz die Hand suchen. Mit Werbepausen endet der Film gegen 22:30."),
    ("Donnerstag, 06.08.2026", "01:00", 105, "Jim Knopf und Lukas der Lokomotivführer", "", "Kabel Eins", 6, "a6", 45,
     "Aufwendige Verfilmung des Michael-Ende-Klassikers mit echten Schauplätzen und viel Ausstattung. Freundschaft, Herkunft und die Frage, wo man hingehört — das trägt über zwei Stunden. Der Scheinriese und der Drache sind die zwei Stellen, an denen jüngere Kinder kurz die Hand suchen. Mit Werbepausen endet der Film gegen 22:30."),
]


# ---------------------------------------------------------------------------
# Empfangbarkeit je Sender — geprüft am 30.07.2026.
#   free = aus Deutschland ohne Zusatzkosten empfangbar
# ---------------------------------------------------------------------------
OERR = "Öffentlich-rechtlich. Frei über Kabel, Satellit, DVB-T2 und Mediathek."
PRIV = ("SD frei empfangbar. HD über Satellit nur mit HD+, über DVB-T2 nur mit freenet TV.")
DISNEY = ("Seit 17.01.2014 im Free-TV. Frei über Kabel, Satellit und IPTV; "
          "über DVB-T2 HD nur mit freenet-TV-Karte. Wird Ende 2026 in Disney TV umbenannt.")
ORF = ("Nur in Österreich frei empfangbar (ORF-Karte). Aus Deutschland nicht regulär zu empfangen.")

ACCESS = {
    "ARD":            (False, OERR),
    "ProSieben":      (True,  PRIV),
    "ProSieben Maxx": (True,  PRIV + " Anime-Schiene am Nachmittag, meist ab 12."),
    "RTL":            (True,  PRIV),
    "RTLzwei":        (True,  PRIV),
    "Nitro":          (True,  PRIV),
    "ZDFneo":         (False, OERR),
    "ONE":            (False, OERR),
    "NDR":            (False, OERR),
    "HR":             (False, OERR),
    "SWR":            (False, OERR),
    "SRF 1":          (False, "Schweizer Fernsehen, in Grenznähe und über Satellit."),
    "KiKA":           (True,  OERR + " Einziger Kindersender ohne Werbung."),
    "ZDF":            (True,  OERR),
    "WDR":            (True,  OERR),
    "RBB":            (True,  OERR),
    "BR":             (True,  OERR),
    "MDR":            (True,  OERR),
    "3sat":           (True,  OERR),
    "Disney Channel": (True,  DISNEY),
    "VOX":            (True,  PRIV),
    "SAT.1":          (True,  PRIV),
    "Kabel Eins":     (True,  PRIV),
    "S-RTL":          (True,  PRIV),
    "Toggo plus":     (True,  PRIV + " Zeitversetzte Ausgabe von Super RTL."),
    "ORF 1":          (False, ORF),
}

# Senderlinks
FILM_CHANNELS = {
    "Disney Channel": "https://www.disneychannel.de/",
    "WDR":            "https://www.wdr.de/",
    "ORF 1":          "https://tv.orf.at/",
    "ZDF":            "https://www.zdf.de/kinder",
    "RBB":            "https://www.rbb-online.de/",
    "VOX":            "https://www.vox.de/",
    "S-RTL":          "https://www.toggo.de/",
    "SAT.1":          "https://www.sat1.de/",
    "BR":             "https://www.br.de/",
    "MDR":            "https://www.mdr.de/",
    "3sat":           "https://www.3sat.de/",
    "KiKA":           "https://www.kika.de/",
    "Kabel Eins":     "https://www.kabeleins.de/",
}

# Werbefrei sind nur die öffentlich-rechtlichen.
NO_ADS = {"KiKA", "ZDF", "WDR", "RBB", "BR", "MDR", "3sat", "ORF 1"}


YEARS = {'Die Chroniken von Narnia': 2008, 'Das doppelte Lottchen': 2017, 'Baymax': 2014, 'Bolt': 2008, 'Tom Turbo': 1993, 'Pippi Langstrumpf': 1969, 'Hans im Glück': 1998, 'Findet Dorie': 2016, 'Minions': 2015, 'Charlie & Louise': 1994, 'Arielle, die Meerjungfrau': 1989, 'Pünktchen und Anton': 1999, 'Der Schuh des Manitu': 2001, "Mary Poppins' Rückkehr": 2018, 'Ostwind (3)': 2017, 'Das Märchen von der silbernen Brücke': 2024, 'Himmel und Huhn': 2005, 'Angry Birds – Der Film': 2016, 'Ritter Rost 2': 2017, 'Dornröschen': 2009, 'Heidi': 1974, 'Der Zauberlehrling': 2017, 'Der König der Löwen 2': 1998, 'Jim Knopf und Lukas der Lokomotivführer': 2018}

import retro_data
import detail_data
import imdb_data


AB = ("01.08.2026", "02.08.2026", "05.08.2026", "06.08.2026")


def _detail_js(day, title):
    """Ausführliche Einschätzung — nur für Sendungen ab übermorgen."""
    if not any(d in day for d in AB):
        return "null"
    d = detail_data.lookup(title)
    if not d:
        return "null"
    q = lambda x: x.replace('"', '\\"')
    flags = ",".join('"%s"' % q(f) for f in d["flags"])
    return '{{lang:"{0}",flags:[{1}],reden:"{2}"}}'.format(
        q(d["lang"]), flags, q(d["reden"]))



# Ein Eintrag kann mehreren Kategorien angehören. "Film" ist die Form,
# Zeichentrick/Realfilm/Märchen/Musik die Machart — beides ist für die Suche
# relevant: Wer auf "Zeichentrick" filtert, will auch Zeichentrickfilme sehen.
GENRES_EXTRA = {
    "Baymax": ["Zeichentrick"], "Bolt": ["Zeichentrick"], "Findet Dorie": ["Zeichentrick"],
    "Minions": ["Zeichentrick"], "Arielle, die Meerjungfrau": ["Zeichentrick", "Musik & Tanz"],
    "Der König der Löwen 2": ["Zeichentrick", "Musik & Tanz"],
    "Himmel und Huhn": ["Zeichentrick"], "Angry Birds – Der Film": ["Zeichentrick"],
    "Ritter Rost 2": ["Zeichentrick", "Musik & Tanz"], "Heidi": ["Serie"],
    "Das doppelte Lottchen": ["Serie"], "Tom Turbo": ["Serie"],
    "Pippi Langstrumpf": ["Serie"], "Charlie & Louise": ["Serie"],
    "Pünktchen und Anton": ["Serie"], "Ostwind (3)": ["Serie"],
    "Jim Knopf und Lukas der Lokomotivführer": ["Fantasyserie"],
    "Die Chroniken von Narnia": ["Fantasyserie"],
    "Hans im Glück": ["Vorlesen"], "Dornröschen": ["Vorlesen"],
    "Das Märchen von der silbernen Brücke": ["Vorlesen"],
    "Der Zauberlehrling": ["Vorlesen", "Fantasyserie"],
    "Mary Poppins' Rückkehr": ["Musik & Tanz"],
    "Der Schuh des Manitu": [],
}


def genres_js(title, haupt):
    alle = [haupt] + [g for g in GENRES_EXTRA.get(title, []) if g != haupt]
    return "[" + ",".join('"%s"' % g for g in alle) + "]"


def films_js_rows():
    rows = []
    for day, t, dur, title, sub, ch, age, grp, score, note in FILMS:
        rows.append(
            '{{day:"{day}",time:"{t}",dur:"{dur} Min",title:"{title}",sub:"{sub}",'
            'age:{age},grp:"{grp}",genres:{gs},fsk:null,fskTodo:true,genre:"Film",channel:"{ch}",'
            'color:"#EA580C",est:true,ads:{ads},'
            'ch:[{{n:"{ch}",free:{free},u:"{u}",note:"{cnote}"}}],'
            'imdb:{imdb},year:{year},spaeter:{sp},detail:{detail},retro:{retro},score:{score},note:"{note}"}}'.format(
                day=day, t=t, dur=dur,
                title=title.replace('"', '\\"'), sub=sub.replace('"', '\\"'),
                age=age, grp=grp, ch=ch, gs=genres_js(title, "Film"),
                ads="false" if ch in NO_ADS else "true",
                u=FILM_CHANNELS.get(ch, ""),
                free="true" if ACCESS.get(ch, (True, ""))[0] else "false",
                cnote=ACCESS.get(ch, (True, ""))[1].replace('"', '\\"'),
                sp=__import__("epg_data").spaeter_js(title, ch),
                detail=_detail_js(day, title),
                imdb=(lambda v: '{r:%s,id:"%s",v:%d}' % (v[0], v[1], v[2]) if v else "null")(imdb_data.lookup(title)),
                year=YEARS.get(title, "null"),
                retro=(lambda r: '{y:%d,n:"%s"}' % (r[0], r[1].replace('"', '\\"')) if r else "null")(retro_data.lookup(title)),
                score=score, note=note.replace('"', '\\"')))
    return rows
