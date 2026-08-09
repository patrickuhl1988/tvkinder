# -*- coding: utf-8 -*-
"""
tipps_data.py — Elterntipps

Bewusst nur Dinge, die NICHT aus unseren automatischen Quellen stammen.
MediathekViewWeb sieht die öffentlich-rechtlichen Mediatheken, TMDB die
Abo-Anbieter — was beide nicht sehen, sind kostenlose YouTube-Kanäle,
Podcasts und Einstellungen. Genau da setzen die Tipps an.

WICHTIG FÜR DIE ABNAHME
-----------------------
Diese zehn Einträge sind redaktionelle Startbefüllung, keine echten
Nutzereinsendungen. Solange die Nutzerverwaltung in der Testphase ist, steht
das auch so über der Liste. Sobald echte Einsendungen kommen, wandern diese
hier raus oder werden als Redaktionstipps gekennzeichnet.

Jeder Tipp nennt auch, was dagegen spricht. Ein Elterntipp, der nur schwärmt,
ist für die Auswahl wertlos.
"""

TIPPS = [
    dict(seite="beide",
        titel="Peppa Wutz — offizieller YouTube-Kanal",
        quelle="YouTube", kostenlos=True, alter=3, dauer="5 Min pro Folge",
        von="Sandra, 2 Kinder (4 und 6)",
        text="Ganze Folgen, offiziell vom Rechteinhaber, kostenlos und ohne Abo. "
             "Für Vorschulkinder das Verlässlichste, was es umsonst gibt: kurze Folgen, "
             "ruhiges Tempo, immer gutes Ende.",
        haken="Werbefinanziert, also Vorrollwerbung. Und Autoplay schiebt danach "
               "beliebige Kanäle nach — vorher abschalten.",
        url="https://www.youtube.com/@PeppaPigDeutsch"),

    dict(seite="beide",
        titel="Nicoles Spielzeug-Welt und Baby Puppen",
        quelle="YouTube", kostenlos=True, alter=3, dauer="5–20 Min",
        von="Kerstin, Tochter 4",
        text="Nicole spielt mit Puppen ganz normale Alltagsszenen durch: einkaufen, "
             "Arzt, Frühstück machen. Meine Tochter spielt danach oft dieselben "
             "Szenen mit ihren eigenen Puppen nach.",
        haken="Das ist über weite Strecken Spielzeugwerbung. Die Marken stehen im "
               "Bild und im Titel. Wer das nicht will, lässt es besser.",
        url="https://www.youtube.com/channel/UCcnvyqZkcV7nz3W8g5B7Cig"),

    dict(seite="beide",
        titel="PAW Patrol — offizieller deutscher Kanal",
        quelle="YouTube", kostenlos=True, alter=3, dauer="10–20 Min",
        von="Micha, Sohn 5",
        text="Ganze Folgen und Zusammenschnitte, kostenlos. Praktisch, wenn Toggo "
             "gerade nicht läuft und man trotzdem eine Folge braucht.",
        haken="Hohes Tempo, laute Musik, sehr viel Merchandise drumherum. Als "
               "Dauerlösung nicht ideal.",
        url="https://www.youtube.com/@PAWPatrolDeutschland"),

    dict(seite="beide",
        titel="Ohrenbär — Hörgeschichten vom rbb",
        quelle="ARD Audiothek", kostenlos=True, alter=3, dauer="10 Min",
        von="Anne, 3 Kinder",
        text="Werbefreie Vorlesegeschichten, jeden Tag eine neue, das Archiv ist "
             "riesig. Unsere Rettung für Autofahrten und für die halbe Stunde vor "
             "dem Einschlafen — ganz ohne Bildschirm.",
        haken="Kein Bild heißt: Manche Kinder brauchen ein paar Anläufe, bis sie "
               "sich darauf einlassen.",
        url="https://www.ardaudiothek.de/sendung/ohrenbaer/"),

    dict(seite="beide",
        titel="Die Maus zum Hören",
        quelle="ARD Audiothek", kostenlos=True, alter=6, dauer="20–30 Min",
        von="Tobias, Sohn 7",
        text="Die Sachgeschichten als Podcast. Erklärt genauso gut wie im "
             "Fernsehen, funktioniert aber beim Malen, Bauen oder im Zug.",
        haken="Ohne Bild fehlt bei manchen Themen die Anschauung — bei "
               "Technikfolgen lohnt sich hinterher das Video.",
        url="https://www.ardaudiothek.de/sendung/die-maus-zum-hoeren/"),

    dict(seite="beide",
        titel="Kakadu — Kinderpodcast von Deutschlandfunk Kultur",
        quelle="ARD Audiothek", kostenlos=True, alter=8, dauer="25 Min",
        von="Julia, Tochter 9",
        text="Nimmt Kinderfragen ernst und beantwortet sie ausführlich, ohne "
             "albern zu werden. Gut für die Altersgruppe, der KiKA langsam zu "
             "kindlich wird.",
        haken="Braucht Aufmerksamkeit. Nebenbei laufen lassen funktioniert nicht.",
        url="https://www.deutschlandfunkkultur.de/kakadu-100.html"),

    dict(seite="beide",
        titel="Cocomelon auf Deutsch",
        quelle="YouTube", kostenlos=True, alter=3, dauer="2–60 Min",
        von="Nadine, Sohn 2",
        text="Kinderlieder mit gewaltiger Reichweite, und ja, es funktioniert — "
             "die Kleinen sind sofort gefesselt.",
        haken="Genau das ist das Problem. Sehr hohe Schnittfrequenz und Dauerreiz; "
               "Medienpädagogen raten von langen Zusammenschnitten ab. Wir nehmen "
               "einzelne Lieder statt der Stundenvideos.",
        url="https://www.youtube.com/@Cocomelon-Deutsch"),

    dict(seite="beide",
        titel="YouTube Kids auf freigegebene Inhalte umstellen",
        quelle="Einstellung", kostenlos=True, alter=3, dauer="5 Min Aufwand",
        von="Stefan, 2 Kinder",
        text="In der YouTube-Kids-App gibt es unter „Inhaltseinstellungen\" den "
             "Modus, in dem nur Kanäle laufen, die man selbst freigegeben hat. "
             "Damit ist Schluss mit merkwürdigen Empfehlungen.",
        haken="Man muss jeden Kanal einzeln freischalten. Einmal eine halbe Stunde "
               "Arbeit, danach Ruhe.",
        url="https://support.google.com/youtubekids/answer/6172308"),

    dict(seite="beide",
        titel="Flimmo — Programmberatung für Eltern",
        quelle="Ratgeber", kostenlos=True, alter=3, dauer="—",
        von="Redaktion",
        text="Kostenlose Einschätzung zu einzelnen Sendungen von Medienpädagogen: "
             "Was ängstigt, was überfordert, was passt zu welchem Alter. Wenn man "
             "bei einem Titel unsicher ist, steht dort meist etwas Fundiertes.",
        haken="Nicht jeder neue Titel ist erfasst, gerade bei Streaming-Serien "
               "gibt es Lücken.",
        url="https://www.flimmo.de/"),

    dict(seite="beide",
        titel="Augsburger Puppenkiste in der ARD Mediathek",
        quelle="ARD Mediathek", kostenlos=True, alter=5, dauer="25 Min",
        von="Bernd, Enkelkinder 5 und 8",
        text="Jim Knopf, Urmel, Räuber Hotzenplotz — die alten Marionettenfassungen "
             "sind schubweise verfügbar und kosten nichts. Langsam erzählt, kein "
             "Schnittgewitter, und die Kinder gucken erstaunlich gebannt.",
        haken="Bild und Ton sind alt, manche Kinder finden es erst mal „komisch\". "
               "Und die Verfügbarkeit wechselt, es lohnt sich, danach zu suchen.",
        url="https://www.ardmediathek.de/suche/Augsburger%20Puppenkiste"),

    # ---------------- nur Startseite: Tipps fürs Wochenende ab 01.08. -------
    dict(seite="index",
        titel="Die guten Filme laufen nachts — aufnehmen",
        quelle="Programmhinweis", kostenlos=True, alter=6, dauer="—",
        von="Katrin, 2 Kinder (7 und 10)",
        text="Am Wochenende liegen gleich vier sehenswerte Filme außerhalb jeder "
             "Kinderzeit: Pünktchen und Anton um 22:10, Narnia um 22:10, Mary Poppins' "
             "Rückkehr um 4 Uhr früh und Jim Knopf um 1 Uhr nachts. Wir programmieren "
             "sonntags einmal den Rekorder durch und haben dann zwei Wochen Vorrat.",
        haken="Wer keinen Rekorder hat, schaut in der Mediathek nach — bei den "
               "öffentlich-rechtlichen Sendern stehen die Filme meist ein paar Tage online, "
               "bei den privaten oft gar nicht.",
        url=""),

    dict(seite="index",
        titel="Samstag 20:15 laufen drei Kinderfilme gleichzeitig",
        quelle="Programmhinweis", kostenlos=True, alter=6, dauer="—",
        von="Ole, Sohn 8",
        text="Minions auf VOX, Charlie & Louise auf Super RTL und Arielle im Disney "
             "Channel — alle drei zur selben Minute. Wir suchen inzwischen schon "
             "nachmittags gemeinsam einen aus. Das erspart die Diskussion, wenn es "
             "losgeht, und die Kinder fühlen sich beteiligt.",
        haken="Funktioniert nur, wenn die Entscheidung wirklich gilt. Einmal "
               "umgeschwenkt und das Ritual ist hin.",
        url=""),

    dict(seite="index",
        titel="Untertitel anschalten, auch für hörende Kinder",
        quelle="Einstellung", kostenlos=True, alter=6, dauer="5 Min Aufwand",
        von="Franziska, Tochter 7",
        text="Bei ARD, ZDF und KiKA lassen sich Untertitel per Fernbedienung "
             "zuschalten. Unsere Große liest seit einem halben Jahr mit und ist "
             "spürbar flüssiger geworden — nebenbei, ohne dass es nach Üben aussieht.",
        haken="Bei schnellen Zeichentrickserien kommen die Untertitel kaum hinterher, "
               "das lenkt eher ab. Bei ruhigen Filmen und Märchen funktioniert es gut.",
        url=""),

    dict(seite="index",
        titel="Die Zwei-Folgen-Regel",
        quelle="Ritual", kostenlos=True, alter=3, dauer="—",
        von="Mehmet, 3 Kinder",
        text="Vorher abmachen, wie viele Folgen — nicht wie viele Minuten. Kinder "
             "können Folgen zählen, Minuten nicht. Bei uns endet der Streit seitdem, "
             "weil das Ende schon vor dem Anfang feststeht.",
        haken="Bei Filmen greift die Regel nicht. Da hilft nur, vorher auf die "
               "Laufzeit zu schauen — die steht hier bei jeder Sendung.",
        url=""),

    dict(seite="index",
        titel="KiRaKa — der Kinderradiokanal des WDR",
        quelle="Radio", kostenlos=True, alter=6, dauer="durchgehend",
        von="Bettina, Sohn 6",
        text="Werbefreies Kinderradio rund um die Uhr, mit Hörspielen, Nachrichten "
             "und Musik. Für Samstagvormittag, wenn die Kinder früh wach sind und man "
             "selbst noch nicht: läuft nebenbei, ohne dass jemand auf einen Bildschirm "
             "starrt.",
        haken="Nicht alles ist für die Kleinsten gedacht, gegen Mittag wird es älter.",
        url="https://kiraka.de/"),

    # ---------------- nur Mediathek: kostenlose Angebote im Netz ------------
    dict(seite="mediathek",
        titel="Planet Schule von SWR und WDR",
        quelle="Mediathek", kostenlos=True, alter=8, dauer="15–45 Min",
        von="Daniel, Tochter 9",
        text="Filme und Erklärstücke, die eigentlich für den Unterricht gemacht sind: "
             "Naturwissenschaft, Geschichte, Sprachen. Werbefrei, ohne Konto, und die "
             "Sachen sind dauerhaft abrufbar statt nur ein paar Tage.",
        haken="Der Ton ist schulisch. Wer gerade Ferien hat, muss dafür in Stimmung "
               "sein.",
        url="https://www.planet-schule.de/"),

    dict(seite="mediathek",
        titel="fragFINN und Blinde Kuh als Startseite",
        quelle="Einstellung", kostenlos=True, alter=6, dauer="10 Min Aufwand",
        von="Sabine, 2 Kinder",
        text="Zwei Kindersuchmaschinen, die nur redaktionell geprüfte Seiten "
             "ausliefern. Wir haben fragFINN als Startseite im Kinderprofil des "
             "Browsers gesetzt — seitdem landet niemand mehr per Zufall auf "
             "Erwachsenenseiten.",
        haken="Der Index ist kleiner als bei Google. Für Hausaufgaben zu speziellen "
               "Themen reicht er manchmal nicht.",
        url="https://www.fragfinn.de/"),

    dict(seite="mediathek",
        titel="HanisauLand von der Bundeszentrale für politische Bildung",
        quelle="Mediathek", kostenlos=True, alter=8, dauer="5–20 Min",
        von="Jonas, Sohn 10",
        text="Politik für Kinder erklärt, mit Comics, Lexikon und kurzen Filmen. "
             "Wenn in den Nachrichten etwas läuft, das Fragen aufwirft, finden wir "
             "hier meist eine Erklärung, die unser Sohn versteht.",
        haken="Kein Unterhaltungsangebot. Das funktioniert nur, wenn eine Frage "
               "schon da ist.",
        url="https://www.hanisauland.de/"),

    dict(seite="mediathek",
        titel="ANTON — Lern-App für die Grundschule",
        quelle="App", kostenlos=True, alter=6, dauer="10–20 Min",
        von="Christine, Tochter 8",
        text="Deutsch, Mathe, Sachunterricht nach Lehrplan, kostenlos und ohne "
             "Werbung. Wird von vielen Schulen selbst eingesetzt. Bei uns ersetzt eine "
             "Runde ANTON regelmäßig eine Folge Fernsehen, ohne dass es nach Strafe "
             "aussieht.",
        haken="Es ist und bleibt Üben. Als Belohnung verkaufen funktioniert nicht "
               "lange.",
        url="https://anton.app/"),

    dict(seite="mediathek",
        titel="Kindersache vom Deutschen Kinderhilfswerk",
        quelle="Mediathek", kostenlos=True, alter=8, dauer="5–15 Min",
        von="Redaktion",
        text="Nachrichten, Filmtipps und Erklärstücke, geschrieben für Kinder und ohne "
             "kommerzielles Interesse. Dazu ein Bereich über Kinderrechte, den es so "
             "sonst kaum gibt.",
        haken="Die Seite wirkt gestalterisch etwas altbacken, das schreckt manche "
               "Kinder erst mal ab.",
        url="https://www.kindersache.de/"),
]
