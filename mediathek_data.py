# -*- coding: utf-8 -*-
"""
mediathek_data.py — Katalog der Kindersendungen in den Mediatheken

Quelle: MediathekViewWeb (mediathekviewweb.de), offene API ohne Schlüssel.
Das Projekt indexiert die öffentlich-rechtlichen Mediatheken und stellt die
Abfrage ausdrücklich frei zur Verfügung. Abgerufen am 30.07.2026.

Geerntet: 6.259 eindeutige Beiträge aus 12 Sendern, verdichtet auf 152 Reihen.
Drei Treffer ohne Kinderbezug wurden entfernt (Fuzzy-Suche der API).
Folgenzahl, mittlere Laufzeit, Anbieter, neueste Ausstrahlung und Link stammen
aus der API. Altersempfehlung und Genre sind redaktionell — für die bekannten
Reihen einzeln gesetzt, sonst "ab 6" und "Zeichentrick" als Vorbelegung.

Das Feld "jahr" stammt aus Wikidata (SPARQL, ohne Schlüssel, CC0) und meint
den Start der Reihe, nicht das Produktionsjahr der einzelnen Folge. Bei
Stoffen mit langer Geschichte zeigt es die Wurzel: "Das Dschungelbuch" 1942,
"Belle und Sebastian" 1965 — gesendet werden jeweils neuere Fassungen.
Jahre vor 1955 sind verworfen: dort datiert Wikidata die literarische Vorlage.

"kurz" ist die Kurzbeschreibung der Reihe aus Wikidata. "note" ist dagegen die
Beschreibung der zuletzt eingestellten Folge aus MediathekViewWeb — deshalb wird
sie in der Oberfläche als "Aktuelle Folge" gekennzeichnet.
"""

MVW = [
 {
  "title": "Die Biene Maja",
  "folgen": 300,
  "dauer": 12,
  "age": 3,
  "grp": "a3",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player",
   "ZDFtivi"
  ],
  "neu": "2026-06-14",
  "url": "https://www.kika.de/die-biene-maja/videos/acht-knacks-im-schneckenhaus-102",
  "note": "Die Schnecke Rufus ist buchstäblich aus dem Häuschen: Das Schneckenhaus hat beim Spielen mit Maja einen Knacks abbekommen.",
  "jahr": 1975,
  "land": "Japan",
  "kurz": "deutsch-japanische Zeichentrickserie (1975–1980)"
 },
 {
  "title": "Wissen macht Ah!",
  "folgen": 300,
  "dauer": 24,
  "age": 8,
  "grp": "a6",
  "genre": "Wissen",
  "prov": [
   "ARD Mediathek",
   "KiKA-Player"
  ],
  "neu": "2026-07-25",
  "url": "https://www.ardmediathek.de/video/Y3JpZDovL3dkci5kZS9CZWl0cmFnLXNvcGhvcmEtOTFlOWU3ODItNjI1Mi00ZDcwLWFhZTMtYzY1ZjBlYzdmYjdh",
  "note": "Diese Folge von \"Wissen macht Ah!\" kümmert sich um Menschen und Maschinen. Wie zum Beispiel bei Clarissa, die einen neuen Kollegen im Studio begrüßt. Was ist das denn? Die Sendung "
 },
 {
  "title": "Unser Sandmännchen",
  "folgen": 300,
  "dauer": 4,
  "age": 3,
  "grp": "a3",
  "genre": "Vorlesen",
  "prov": [
   "ARD Mediathek",
   "KiKA-Player"
  ],
  "neu": "2026-07-29",
  "url": "https://www.ardmediathek.de/video/Y3JpZDovL3JiYl84ZWUwODU5OC0yZDc3LTQ0NzUtYjEyMi05ODU2ZDc1ZjViMmNfcHVibGljYXRpb24",
  "note": "Unser Sandmännchen kommt heute mit der Flugkapsel und bringt Euch eine Geschichte von Jan & Henry mit: Die Erdmännchen Jan und Henry wollen ein Nashorn vor einer schweren Kopfverle",
  "jahr": 1959,
  "land": "Deutsche Demokratische Republik",
  "kurz": "Kindersendung seit 1959, zunächst im Fernsehen der DDR, seit 1990 in der Bundesrepublik"
 },
 {
  "title": "Die Sendung mit der Maus",
  "folgen": 299,
  "dauer": 28,
  "age": 6,
  "grp": "a6",
  "genre": "Wissen",
  "prov": [
   "ARD Mediathek",
   "KiKA-Player"
  ],
  "neu": "2026-08-29",
  "url": "https://www.ardmediathek.de/video/Y3JpZDovL3dkci5kZS9CZWl0cmFnLXNvcGhvcmEtNGMyZmRjMWMtN2VhYi00Nzc3LTliYTAtZDMxMGU2MDA5ZWFj",
  "note": "Wie wird eine Brücke gebaut? Armin hat mit dem Maus-Team über viele Jahre den Bau der neuen Leverkusener Autobahnbrücke begleitet. In diesem XXL Maus Spezial werden die Meilenstein",
  "jahr": 1971,
  "land": "Deutschland",
  "kurz": "Kindersendung im deutschen Fernsehen"
 },
 {
  "title": "Die Pfefferkörner",
  "folgen": 296,
  "dauer": 28,
  "age": 12,
  "grp": "a10",
  "genre": "Serie",
  "prov": [
   "ARD Mediathek",
   "KiKA-Player"
  ],
  "neu": "2026-08-08",
  "url": "https://www.ardmediathek.de/video/Y3JpZDovL2Rhc2Vyc3RlLm5kci5kZS80NzUzXzIwMjItMDEtMjktMDktMjA",
  "note": "(Folge 224) Pippa engagiert sich in der Bienen-AG – und ist entsetzt, als nach einem brutalen Brandanschlag elf Bienenvölker ausgerottet sind.",
  "jahr": 1999,
  "land": "Deutschland",
  "kurz": "Deutsche Fernsehserie"
 },
 {
  "title": "PUR+",
  "folgen": 266,
  "dauer": 24,
  "age": 8,
  "grp": "a6",
  "genre": "Wissen",
  "prov": [
   "KiKA-Player",
   "ZDFtivi"
  ],
  "neu": "2026-07-10",
  "url": "https://www.zdf.de/video/reportagen/purplus-100/meine-stadt-fit-fuers-klima-100",
  "note": "Unsere Städte werden immer heißer, und auf Starkregen sind sie schlecht vorbereitet. Kann man sie in eine Art Schwamm verwandeln? Wie kühlen wir die Straßen und Häuser? Eric findet"
 },
 {
  "title": "Checker Reportagen",
  "folgen": 265,
  "dauer": 24,
  "age": 8,
  "grp": "a6",
  "genre": "Wissen",
  "prov": [
   "ARD Mediathek",
   "KiKA-Player"
  ],
  "neu": "2026-07-29",
  "url": "https://www.ardmediathek.de/video/Y3JpZDovL2JyLmRlL3ZpZGVvLzlhNjBhNDZmLWI1ZWYtNGIwMy1iYjA0LTQ2NzY0ZjBmY2NkYg",
  "note": "Internate sind Orte, an denen Kinder zur Schule gehen und auch wohnen. In Deutschland gibt es etwa 250 Internate. Wie das Leben dort so ist und warum man sich für einen Internatsbe"
 },
 {
  "title": "Löwenzahn",
  "folgen": 249,
  "dauer": 24,
  "age": 6,
  "grp": "a6",
  "genre": "Wissen",
  "prov": [
   "KiKA-Player",
   "ZDFtivi"
  ],
  "neu": "2026-06-14",
  "url": "https://www.kika.de/loewenzahn/videos/audiodeskription/kranich-als-hoerfilm-100",
  "note": "Faszinierend, diese Kraniche, die laut trompetend über Fritz' Bauwagen ziehen. Ausgerechnet jetzt soll der Kranich-Ausguck geschlossen werden.",
  "jahr": 1981,
  "land": "Deutschland",
  "kurz": "deutsche Fernsehserie"
 },
 {
  "title": "Wickie und die starken Männer",
  "folgen": 195,
  "dauer": 12,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player",
   "ZDFtivi"
  ],
  "neu": "2026-06-14",
  "url": "https://www.kika.de/wickie-und-die-starken-maenner/videos/neununddreissig-kampf-mit-dem-stier-100",
  "note": "Eigentlich wollen die Wikinger bloß schauen, was sie sich denn im fernen Spanien an Reichtümern unter den Nagel reißen können. Doch dann kommt alles anders.",
  "jahr": 1974,
  "land": "Japan",
  "kurz": "deutsch-österreichisch-französische 3D-Animationsserie (2013–2014)"
 },
 {
  "title": "Rudis Siebenstein",
  "folgen": 173,
  "dauer": 24,
  "age": 6,
  "grp": "a6",
  "genre": "Wissen",
  "prov": [
   "KiKA-Player",
   "ZDFtivi"
  ],
  "neu": "2026-05-24",
  "url": "https://www.kika.de/rudi/rudis-siebenstein/videos/der-tanzzauber-102",
  "note": "Eine magische Spieluhr verzaubert Siebenstein und zwingt sie, Polka zu tanzen!"
 },
 {
  "title": "Bibi Blocksberg",
  "folgen": 168,
  "dauer": 25,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player",
   "ZDFtivi"
  ],
  "neu": "2026-06-14",
  "url": "https://www.kika.de/bibi-blocksberg/videos/sieben-das-diamantendiadem-100",
  "note": "Bibi und Karla Kolumna freuen sich auf die Ausstellung des Diadems im Museum. Doch während der Rede zur Ausstellungseröffnung, geht das Licht aus.",
  "jahr": 1997,
  "land": "Deutschland",
  "kurz": "Film von Hermine Huntgeburth (2002)"
 },
 {
  "title": "logo!",
  "folgen": 142,
  "dauer": 10,
  "age": 8,
  "grp": "a6",
  "genre": "Wissen",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-16",
  "url": "https://www.kika.de/logo/videos/logo-vom-dienstag-sechzehn-juni-zweitausendsechsundzwanzig-100",
  "note": "Die Themen: Wasserqualität / Schiefer Turm von Pisa - einfach erklärt / Abseits / Videobeweis / Katze crasht Theater / Moderation: Teresa"
 },
 {
  "title": "Das Magazin",
  "folgen": 128,
  "dauer": 21,
  "age": 8,
  "grp": "a6",
  "genre": "Wissen",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-16",
  "url": "https://www.kika.de/sesamstrasse/videos/audiodeskription/eins-zwei-drei-vier-jahreszeiten-hoerfassung-100",
  "note": "Außerdem möchte Ernie erklären, was Gegensätze sind und fragt, ob Bert mitmachen möchte. Hätte Bert mal lieber \"Nein\" gesagt..."
 },
 {
  "title": "Kikaninchen Schnipselwelt",
  "folgen": 128,
  "dauer": 2,
  "age": 3,
  "grp": "a3",
  "genre": "Vorlesen",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-16",
  "url": "https://www.kika.de/kikaninchen-schnipselwelt/videos/das-pferd-hat-geburtstag-100",
  "note": "Anni erzählt Kikaninchen eine Geschichte von einem orangefarbenen Schnipsel, der zu einer Möhre wird. Über die sich das Pferd sehr freut."
 },
 {
  "title": "Siebenstein",
  "folgen": 127,
  "dauer": 25,
  "age": 6,
  "grp": "a6",
  "genre": "Wissen",
  "prov": [
   "KiKA-Player",
   "ZDFtivi"
  ],
  "neu": "2025-09-07",
  "url": "https://www.zdf.de/video/serien/siebenstein-110/spielen-verboten-102",
  "note": "Der Koffer hat eine kleine Dampflok gebaut, auf die er sehr stolz ist. Rudi kann gar nicht verstehen, warum die tolle Lok nur zum Anschauen da ist und er nicht damit spielen darf."
 },
 {
  "title": "Zoom - Der weiße Delfin",
  "folgen": 108,
  "dauer": 12,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-16",
  "url": "https://www.kika.de/zoom-der-weisse-delfin/videos/vierundvierzig-tag-der-streiche-100",
  "note": "Auf der Insel Maotou wird das Fest des Spaßvogels Tupapau gefeiert. Zu diesem Anlass werden traditionell Streiche gespielt."
 },
 {
  "title": "H2O - Plötzlich Meerjungfrau",
  "folgen": 103,
  "dauer": 24,
  "age": 12,
  "grp": "a10",
  "genre": "Serie",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-04",
  "url": "https://www.kika.de/h2o-ploetzlich-meerjungfrau/videos/sechsundzwanzig-komet-im-anflug-100",
  "note": "Cleo, Rikki und Bella sind verzweifelt, denn ein Komet rast auf Mako zu und wird ein Werk der Zerstörung anrichten.",
  "jahr": 2006,
  "land": "Australien",
  "kurz": "australische Fernsehserie (2006–2010)"
 },
 {
  "title": "Schloss Einstein",
  "folgen": 101,
  "dauer": 25,
  "age": 12,
  "grp": "a10",
  "genre": "Serie",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-16",
  "url": "https://www.kika.de/schloss-einstein/schloss-einstein/videos/schloss-einstein-neunhundertsechsundfuenfzig-108",
  "note": "Seit Till wieder auf dem Einstein ist, verhält er sich komisch - wird jemand sein Geheimnis knacken?",
  "jahr": 1998,
  "land": "Deutschland",
  "kurz": "deutsche Fernsehserie für Kinder und Jugendliche"
 },
 {
  "title": "Heidi",
  "folgen": 94,
  "dauer": 22,
  "age": 6,
  "grp": "a6",
  "genre": "Serie",
  "prov": [
   "KiKA-Player",
   "ZDFtivi"
  ],
  "neu": "2026-01-07",
  "url": "https://www.kika.de/heidi/videos/neununddreissig-die-versoehnung-100",
  "note": "Zur Einweihung der Teufelsbrücke reisen auch Dete und Sebastian an. Die Stimmung ist ausgelassen, nur zwischen Großvater und Dete herrscht dicke Luft.",
  "land": "Japan",
  "kurz": "Film von Albert Hanan Kaminski und Alan Simpson (2005)"
 },
 {
  "title": "Lilys Strandschatz Eiland",
  "folgen": 82,
  "dauer": 7,
  "age": 3,
  "grp": "a3",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-16",
  "url": "https://www.kika.de/lilys-strandschatz-eiland/videos/einhundert-costa-del-hirsch-100",
  "note": "Lord von Hirsch will aus der Insel einen Touristenmagneten machen. Alles soll abgerissen und zubetoniert werden. Die Inselbewohner sind schockiert."
 },
 {
  "title": "Der kleine Drache Kokosnuss",
  "folgen": 75,
  "dauer": 12,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-16",
  "url": "https://www.kika.de/der-kleine-drache-kokosnuss/videos/vierundzwanzig-das-buch-der-weisheit-100",
  "note": "Ein Buch der Weisheit, das die Antworten auf alle Fragen kennt. Das wär ein Ding!",
  "land": "Deutschland",
  "kurz": "deutsche Fernsehserie"
 },
 {
  "title": "Die Sendung mit dem Elefanten",
  "folgen": 71,
  "dauer": 4,
  "age": 3,
  "grp": "a3",
  "genre": "Wissen",
  "prov": [
   "ARD Mediathek",
   "KiKA-Player"
  ],
  "neu": "2026-07-25",
  "url": "https://www.ardmediathek.de/video/Y3JpZDovL3dkci5kZS9CZWl0cmFnLTI3NjllMGEzLTg2YTMtNDU2NS05YTQ3LTQ2OTE2MmYyNGM4OQ",
  "note": "Ein Experiment mit Wasser · Elefant und Hase überqueren den Fluss · David und Red haben Durst · Priesemut bringt Nulli Schwimmen bei · Mit Papa im Schwimmbad · Elefant, Hase und da",
  "jahr": 2007,
  "land": "Deutschland",
  "kurz": "deutsche Fernsehserie"
 },
 {
  "title": "Saïd und Anna",
  "folgen": 65,
  "dauer": 7,
  "age": 6,
  "grp": "a6",
  "genre": "Serie",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-13",
  "url": "https://www.kika.de/said-und-anna/videos/discokugel-folge-sechzehn-100",
  "note": "Saïd ist wütend, weil Anna seinen Ball kaputt gemacht hat und will nicht mehr mit ihr spielen. Anna braucht einen Plan, Saïd wieder fröhlich zu kriegen."
 },
 {
  "title": "Shaun das Schaf",
  "folgen": 59,
  "dauer": 7,
  "age": 3,
  "grp": "a3",
  "genre": "Zeichentrick",
  "prov": [
   "ARD Mediathek",
   "KiKA-Player"
  ],
  "neu": "2026-07-30",
  "url": "https://www.ardmediathek.de/video/Y3JpZDovL3dkci5kZS9CZWl0cmFnLXNvcGhvcmEtMmE5YjNhYzMtNTA3Mi00NTgyLWIyZDctODM1ZGRkMWQyZmE5",
  "note": "Weiter im Shirleyversum gefangen, kommt Shaun auf einer leeren Farm an und findet Bitzers verlassene Pfeife. Zum Glück bringt ihn das Shirley-Portal wieder nach Hause - Shaun war n",
  "jahr": 2007,
  "land": "Vereinigtes Königreich",
  "kurz": "britische Fernsehserie von Richard Goleszowski und Christopher Sadler"
 },
 {
  "title": "Wir sind die Dorfbande",
  "folgen": 52,
  "dauer": 12,
  "age": 6,
  "grp": "a6",
  "genre": "Serie",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-16",
  "url": "https://www.kika.de/wir-sind-die-dorfbande/videos/rettet-martin-102",
  "note": "Bohnenstange und Kleiner Fuß bemerken, dass Martin, der Gartenzwerg, weg ist. Der Verdacht fällt auf Marie.",
  "jahr": 2024,
  "land": "Frankreich",
  "kurz": "französische Animationsserie"
 },
 {
  "title": "Dylans Spielkiste",
  "folgen": 52,
  "dauer": 11,
  "age": 3,
  "grp": "a3",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-16",
  "url": "https://www.kika.de/dylans-spielkiste/videos/astronaut-102",
  "note": "Dylan startet als Astronaut eine Mission zum Mond. Zusammen mit Ozzy und Bitsy begegnet er Daisy, der Sternschnuppe, die vor einem schwarzen Loch warnt."
 },
 {
  "title": "Kleine lustige Krabbler",
  "folgen": 51,
  "dauer": 12,
  "age": 3,
  "grp": "a3",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-16",
  "url": "https://www.kika.de/kleine-lustige-krabbler/videos/zwei-die-heimkehr-zwei-100",
  "note": "Nachdem es Wendy mit einem Trick gelungen ist, Marylin, Klaus und Josefine aus dem Garten wegzulocken, hat sie freie Bahn."
 },
 {
  "title": "Robin Hood",
  "folgen": 48,
  "dauer": 12,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-13",
  "url": "https://www.kika.de/robin-hood/videos/neununddreissig-der-muerrische-drache-100",
  "note": "Derke hat sein Hamsterdasein satt und bittet Marian erneut um einen Zauber.",
  "land": "Japan",
  "kurz": "Film von Étienne Arnaud und Herbert Blaché (1912)"
 },
 {
  "title": "Baumhaus",
  "folgen": 47,
  "dauer": 4,
  "age": 3,
  "grp": "a3",
  "genre": "Vorlesen",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-16",
  "url": "https://www.kika.de/baumhaus/videos/einhundertsiebenundsechzig-unterwasser-woche-fidi-spielt-tauchen-100",
  "note": "Es ist Unterwasser-Woche: Fidi und Singa spielen Tauchen im Meer. Mit der Taucherbrille auf der Nase begegnet Fidi dabei sogar einem Fisch im Baumhaus."
 },
 {
  "title": "Die drei Musketiere",
  "folgen": 47,
  "dauer": 12,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-25",
  "url": "https://www.kika.de/die-drei-musketiere/videos/der-entdecker-koenig-102",
  "note": "Der König ist allein und langweilt sich im Louvre. Als er sieht, dass die Pforte eines Seiteneingangs offensteht, betritt er neugierig Paris.",
  "land": "Kanada",
  "kurz": "Film von Masakazu Higuchi und Chinami Namba (1992)"
 },
 {
  "title": "Lassie",
  "folgen": 46,
  "dauer": 23,
  "age": 6,
  "grp": "a6",
  "genre": "Serie",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-14",
  "url": "https://www.kika.de/lassie/videos/sechsundzwanzig-das-seifenkistenrennen-100",
  "note": "Zoé will Mrs. Lee durch einen Sieg beim Seifenkistenrennen unterstützen, da deren Laden in letzter Zeit nicht gut läuft.",
  "land": "Kanada",
  "kurz": "US-amerikanische Fernsehserie (1954–1973)"
 },
 {
  "title": "Der kleine Rabe Socke",
  "folgen": 45,
  "dauer": 12,
  "age": 3,
  "grp": "a3",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-13",
  "url": "https://www.kika.de/der-kleine-rabe-socke/videos/die-waldpruefung-142",
  "note": "Herr Hund bildet die Kinder zu Waldläufern aus. Am Ende winkt ein richtiges Waldläufer-Abzeichen. Das hätte Socke schon auch gerne.",
  "jahr": 2012,
  "land": "Deutschland",
  "kurz": "Film von Ute von Münchow-Pohl und Sandor Jesse (2012)"
 },
 {
  "title": "Meine Freundin Conni",
  "folgen": 44,
  "dauer": 12,
  "age": 3,
  "grp": "a3",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-16",
  "url": "https://www.kika.de/meine-freundin-conni/videos/conni-und-der-hundebesuch-104",
  "note": "Conni trifft auf einen freilaufenden Hund im Park, der einfach an ihr hochspringt. Das mag Conni nicht. Soll sie wegrennen? Oder ist das zu gefährlich?",
  "jahr": 2012,
  "land": "Deutschland",
  "kurz": "deutsche Zeichentrickserie"
 },
 {
  "title": "Team Nuggets",
  "folgen": 42,
  "dauer": 7,
  "age": 6,
  "grp": "a6",
  "genre": "Serie",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-13",
  "url": "https://www.kika.de/team-nuggets/videos/ich-will-nach-hause-102",
  "note": "Karla darf bei Oggi übernachten! Doch bei ihm zu Hause ist alles ganz anders. Karla bekommt Heimweh und will nach Hause. Oggi ist traurig."
 },
 {
  "title": "ENE MENE BU",
  "folgen": 41,
  "dauer": 11,
  "age": 3,
  "grp": "a3",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-16",
  "url": "https://www.kika.de/ene-mene-bu/videos/zweitausendachthunderteinundsechzig-geburtstagsparty-feiern-basteln-und-singen-zum-geburtstag-100",
  "note": "Wir feiern eine Geburtstagsparty! Ein Kind hat Geburtstag und andere Kinder basteln und singen. Mach mit und bastle eine Steckfigur oder male ein Bild!"
 },
 {
  "title": "Pippi Langstrumpf",
  "folgen": 41,
  "dauer": 24,
  "age": 6,
  "grp": "a6",
  "genre": "Serie",
  "prov": [
   "KiKA-Player",
   "ZDFtivi"
  ],
  "neu": "2025-09-06",
  "url": "https://www.kika.de/pippi-langstrumpf/videos/pippi-auf-der-walz-vier-100",
  "note": "Pippis Flugauto verliert langsam alle Teile. Die Kinder landen am Ufer eines Sees. Während sie baden gehen, frisst eine neugierige Kuh ihre Kleider. Doch der kleine Onkel hilft!",
  "land": "Kanada",
  "kurz": "schwedischer Animationsfilm aus dem Jahr 1997"
 },
 {
  "title": "Das Dschungelbuch",
  "folgen": 40,
  "dauer": 11,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-13",
  "url": "https://www.kika.de/das-dschungelbuch/videos/achtundzwanzig-der-falsche-kranke-100",
  "note": "Um Aufmerksamkeit zu bekommen, behauptet der kleine Mungo Rikki-Tikki, er sei krank. Balu diagnostiziert tropisches Fieber.",
  "land": "Vereinigte Staaten",
  "kurz": "indisch-britische Computeranimationsserie (2010–2020)"
 },
 {
  "title": "Odo - Kleine Eule ganz groß",
  "folgen": 40,
  "dauer": 7,
  "age": 3,
  "grp": "a3",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-04",
  "url": "https://www.kika.de/odo/videos/einundfuenfzig-der-eulenblick-100",
  "note": "Als Odos Papierflieger sich in einem hohen Baum verfängt, klettert er dort hinauf. Oben stellt er fest, wie weit er mit seinem Eulenblick schauen kann."
 },
 {
  "title": "Pirate Academy - Nichts für Landratten",
  "folgen": 39,
  "dauer": 12,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-16",
  "url": "https://www.kika.de/pirate-academy/videos/die-zerreissprobe-106",
  "note": "Erika nervt die Sardinen mit ihrem \"Gesang\", ständig und mit voller Absicht. Käpt'n Raubein will nichts dagegen tun."
 },
 {
  "title": "Eine lausige Hexe",
  "folgen": 39,
  "dauer": 25,
  "age": 12,
  "grp": "a10",
  "genre": "Serie",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-16",
  "url": "https://www.kika.de/eine-lausige-hexe/videos/dreizehn-ruhm-und-rache-100",
  "note": "Gerade als alle zum Ende des Schuljahres abreisen wollen, verdüstert sich der Himmel über Graustein. Ein Sturm zieht auf und Indigo erscheint.",
  "jahr": 1998,
  "land": "Kanada",
  "kurz": "britische Fantasy-Kinderserie (2017–2020)"
 },
 {
  "title": "Löwenzahn mit Fritz Fuchs",
  "folgen": 39,
  "dauer": 24,
  "age": 6,
  "grp": "a6",
  "genre": "Wissen",
  "prov": [
   "ZDFtivi"
  ],
  "neu": "2026-06-04",
  "url": "https://www.zdf.de/video/magazine/loewenzahn-mit-fritz-fuchs-100/satellit-ufo-alarm-im-elchwinkel-100",
  "note": "Fritz staunt über die seltsamen Lichter am Bärstädter Nachthimmel. Hat Nachbarin Dani Paschulke recht und im Elchwinkel ist wirklich ein UFO abgestürzt? Fritz geht der Sache auf de"
 },
 {
  "title": "Pettersson und Findus",
  "folgen": 37,
  "dauer": 12,
  "age": 3,
  "grp": "a3",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-14",
  "url": "https://www.kika.de/pettersson-und-findus/videos/neunzehn-namenstag-fuer-alle-100",
  "note": "Es ist Mitte Dezember, als Findus beschließt, seinen \"Halb-jahresnamenstag\" zu feiern. Davon hat Pettersson zwar noch nie gehört, aber er willigt ein.",
  "jahr": 1999,
  "land": "Schweden",
  "kurz": "Film von Albert Hanan Kaminski (1999)"
 },
 {
  "title": "Weißt du eigentlich, wie lieb ich dich hab?",
  "folgen": 36,
  "dauer": 11,
  "age": 3,
  "grp": "a3",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-15",
  "url": "https://www.kika.de/weisst-du-eigentlich-wie-lieb-ich-dich-hab/videos/einundzwanzig-die-gutenacht-geschichte-100",
  "note": "In einer heißen Sommernacht kühlen sich alle am Fluss ab. Auch nach der Abkühlung ist der kleine Hase nicht müde. Hilft da eine Gutenacht-Geschichte?",
  "jahr": 2012,
  "land": "Australien",
  "kurz": "Australisch-deutsche Zeichentrickserie"
 },
 {
  "title": "Team Timster",
  "folgen": 36,
  "dauer": 3,
  "age": 12,
  "grp": "a10",
  "genre": "Wissen",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-14",
  "url": "https://www.kika.de/team-timster/videos/einhundertvierundsiebzig-pro-gamer-wie-wird-man-das-102",
  "note": "Zocken als Beruf? Tim trifft echte Pro-Gamer und lernt, was man draufhaben muss, um im E-Sport richtig gut zu sein."
 },
 {
  "title": "Paula, Anna und die wilden Tiere",
  "folgen": 36,
  "dauer": 24,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "ARD Mediathek"
  ],
  "neu": "2020-05-31",
  "url": "https://www.ardmediathek.de/video/Y3JpZDovL2JyLmRlL3ZpZGVvL2I0ZjY1YjkzLWEyODctNDI3ZC1iZTFkLTk5NDQ5ZjZjNGQxOA",
  "note": "In Indonesien macht Anna heute Bekanntschaft mit einem der süßesten Affen überhaupt: dem Plumplori. Aber Achtung! Dieses Tier ist giftig. Bei Gefahr vermischt der Plumplori ein Sek"
 },
 {
  "title": "KiKA LIVE",
  "folgen": 35,
  "dauer": 10,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-16",
  "url": "https://www.kika.de/kika-live/videos/flickzy-beim-e-sport-turnier-102",
  "note": "E-Sport-Legende Flickzy kämpft um den Einzug in die Fortnite Global Championship. Wie bereitet er sich auf den großen Wettkampf vor?"
 },
 {
  "title": "Ein Fall für die Erdmännchen",
  "folgen": 33,
  "dauer": 12,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-13",
  "url": "https://www.kika.de/ein-fall-fuer-die-erdmaennchen/videos/platte-reifen-s-e-100",
  "note": "Ein geplanter Fahrradausflug an den Badesee lässt die Erdmännchen-Detektive direkt in ihren nächsten Fall schlittern.",
  "land": "Deutschland",
  "kurz": "deutsche Kindersendung"
 },
 {
  "title": "Super Wings",
  "folgen": 33,
  "dauer": 12,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-27",
  "url": "https://www.kika.de/super-wings/videos/chaos-auf-dem-bauernhof-110",
  "note": "Jett bringt Glasschuhe zu Colette in Südfrankreich, die zu einem Kostümball geht. Da muss sich Jett eben um die Tiere auf Colettes Bauernhof kümmern.",
  "jahr": 2014,
  "land": "Vereinigte Staaten",
  "kurz": "Kinderanimationsserie"
 },
 {
  "title": "Belle und Sebastian",
  "folgen": 32,
  "dauer": 12,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-14",
  "url": "https://www.kika.de/belle-und-sebastian/videos/zwoelf-die-schoene-und-der-mops-100",
  "note": "Sebastian ist beunruhigt. Schon seit Tagen trifft er Belle zu Hause kaum noch an. Sie läuft morgens alleine in die Berge und kümmert sich kaum noch um ihn.",
  "jahr": 1965,
  "land": "Kanada",
  "kurz": "französischer Film von Nicolas Vanier (2013)"
 },
 {
  "title": "Anna, Nina, Pia und die wilden Tiere",
  "folgen": 32,
  "dauer": 24,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "ARD Mediathek"
  ],
  "neu": "2026-07-29",
  "url": "https://www.ardmediathek.de/video/Y3JpZDovL2JyLmRlL3ZpZGVvLzVjZTFhZTY3LTY0MTktNGVlMi1hNmYzLTg1ZTE3ZGYzZDkwMQ",
  "note": "In der Savanne Namibias nimmt Tierreporterin Anna heute Termiten unter die Lupe. Termiten sind hervorragende Baumeister, perfekte Straßen- und Tunnelbauer, bestens organisierte Ern"
 },
 {
  "title": "Wir Kinder aus dem Möwenweg",
  "folgen": 29,
  "dauer": 12,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-14",
  "url": "https://www.kika.de/wir-kinder-aus-dem-moewenweg/videos/wir-fangen-maeuse-104",
  "note": "Die Erwachsenen im Möwenweg haben beschlossen, mit Hilfe eines Kammerjägers die Mäuse aus den Garagen und Gärten zu vertreiben."
 },
 {
  "title": "Lieselotte",
  "folgen": 28,
  "dauer": 7,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-03",
  "url": "https://www.kika.de/lieselotte/videos/lieselotte-hat-den-dreh-raus-104",
  "note": "Lieselotte nimmt Ballett-Unterricht beim Huhn. Sie übt hart, macht jedoch keine großen Fortschritte."
 },
 {
  "title": "Schleich pur",
  "folgen": 28,
  "dauer": 5,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "ARD Mediathek"
  ],
  "neu": "2026-07-16",
  "url": "https://www.ardmediathek.de/video/Y3JpZDovL2JyLmRlL2Jyb2FkY2FzdC9GMjAyNVdPMDI1ODE4QTAvc2VjdGlvbi8xYjVmZTVkNy1lNTUwLTQ3ODItYmI4NS01ZGU3MzAyZTAyNDc",
  "note": "Demokratie ist mehr als ein Schlagwort. Andreas Rebers beschäftigt sich mit Meinungsfreiheit, Pluralismus, Vielfalt, Gleichheit, Resonanzräumen, staatlich finanzierten NGOs und der"
 },
 {
  "title": "TOM und das Erdbeermarmeladebrot mit Honig",
  "folgen": 27,
  "dauer": 5,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-13",
  "url": "https://www.kika.de/tom-und-das-erdbeermarmeladebrot-mit-honig/videos/tom-und-der-streit-130",
  "note": "Das Krokodil hat genug davon, immer herumkommandiert zu werden. Es verlässt die Erdbeermaus im Streit und zieht zu TOMs Mama."
 },
 {
  "title": "Zacki und die Zoobande",
  "folgen": 26,
  "dauer": 11,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-14",
  "url": "https://www.kika.de/zacki-und-die-zoobande/videos/bruno-muss-niesen-110",
  "note": "Bruno hat eine Erkältung und niest ununterbrochen. Frau Emily weiß Rat.",
  "land": "Belgien"
 },
 {
  "title": "Zoés Zauberschrank",
  "folgen": 26,
  "dauer": 11,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-13",
  "url": "https://www.kika.de/zoes-zauberschrank/videos/ein-drache-weiss-nicht-weiter-104",
  "note": "Zoé und Finn werden Prinzessin und Ritter, um auf dem Rücken eines Drachen „Fang-die-Flagge“ zu spielen. Sie beschließen, am großen Turnier teilzunehmen.",
  "jahr": 2009,
  "land": "Vereinigtes Königreich",
  "kurz": "britische Kinder-Animationsserie (2009–2017)"
 },
 {
  "title": "Wendy",
  "folgen": 26,
  "dauer": 24,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-10",
  "url": "https://www.kika.de/wendy/videos/sieben-erwischt-100",
  "note": "In zwei Wochen ist ein wichtiger Wettkampf, bei dem Wendy unbedingt dabei sein will.",
  "jahr": 1995,
  "land": "Vereinigte Staaten",
  "kurz": "neuseeländische Fernsehserie (1995–1996)"
 },
 {
  "title": "Lenas Hof",
  "folgen": 26,
  "dauer": 6,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-29",
  "url": "https://www.kika.de/lenas-hof/videos/zwei-maeuse-sehen-fern-102",
  "note": "Die Mäusefamilie hat es gut auf Lenas Hof. Sie dürfen bei Lena in der Stubeauf dem Kaminsims wohnen."
 },
 {
  "title": "Die Werkel-Ferkel",
  "folgen": 26,
  "dauer": 11,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-21",
  "url": "https://www.kika.de/die-werkel-ferkel/videos/der-jurticopter-102",
  "note": "Fiona will auf Abenteuerreise gehen. Die Werkel-Ferkel könnten ihr diesen Wunsch erfüllen. Aber Fiona packt so viel ein, dass es nicht in den Koffer passt."
 },
 {
  "title": "Bibi und Tina",
  "folgen": 25,
  "dauer": 25,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-14",
  "url": "https://www.kika.de/bibi-und-tina/videos/tante-paula-auf-dem-schloss-102",
  "note": "Bibi, Tina und Alex wollen Frau Martin und den Grafen mit einem Ritterfest auf Schloss Falkenstein überraschen.",
  "jahr": 2004,
  "land": "Deutschland",
  "kurz": "deutsche Fernsehserie (2004–2017)"
 },
 {
  "title": "H2O - Abenteuer Meerjungfrau",
  "folgen": 24,
  "dauer": 24,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-13",
  "url": "https://www.kika.de/h2o-abenteuer-meerjungfrau/videos/die-geheimnisvolle-alge-104",
  "note": "Emma wird von einer seltsamen Wasserpflanze angegriffen und entkommt ihr nur durch Rikkis und Cleos Hilfe."
 },
 {
  "title": "Die Checker-Webshow",
  "folgen": 24,
  "dauer": 13,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "ARD Mediathek",
   "KiKA-Player"
  ],
  "neu": "2025-04-25",
  "url": "https://www.ardmediathek.de/video/Y3JpZDovL2JyLmRlL2Jyb2FkY2FzdC8yNDI0YWVmZi1mNDlhLTRjMDItOTdiYi1iZTUwZWQ0NzRjYzBfb25saW5lYnJvYWRjYXN0",
  "note": "Wir alle müssen mal groß aufs Klo. Das ist das normalste der Welt. Doch wie wird aus einem leckeren Snack am Ende ein Haufen in der Toilette? Marina findet es heraus!"
 },
 {
  "title": "Sesamstraße",
  "folgen": 21,
  "dauer": 4,
  "age": 3,
  "grp": "a3",
  "genre": "Zeichentrick",
  "prov": [
   "ARD Mediathek",
   "KiKA-Player"
  ],
  "neu": "2025-09-17",
  "url": "https://www.ardmediathek.de/video/Y3JpZDovL25kci5kZS9kZGRmNmZhMi01NWJkLTQyNDAtYjE1Zi0wYWVmZWI2MzRlNDg",
  "note": "Graf Zahl ist im Urlaub und möchte natürlich etwas Neues zählen. So zählt er voller Freude Segelboote, Pelikane und Fische.",
  "jahr": 1969,
  "land": "Vereinigte Staaten",
  "kurz": "deutschsprachige Ausgabe der Kinderserie"
 },
 {
  "title": "Sonntagsmärchen",
  "folgen": 20,
  "dauer": 70,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-14",
  "url": "https://www.kika.de/sonntagsmaerchen/videos/die-galoschen-des-gluecks-102",
  "note": "Johann ist Diener der Großherzogin und möchte ein Prinz sein. Zum Glück gibt es Frau Sorge und Frau Glück. Die beiden Feen besitzen \"Galoschen des Glücks\".",
  "jahr": 1997,
  "land": "Deutschland",
  "kurz": "Sendereihe auf KiKA"
 },
 {
  "title": "Peter Pan",
  "folgen": 20,
  "dauer": 22,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-13",
  "url": "https://www.kika.de/peter-pan/videos/neunundvierzig-kinozauber-100",
  "note": "Die drei Geschwister sehen sich einen Film an, in dem der kleine Bösewicht Synapse von Captain Muscles gejagt wird. Peter kommt dazu und ist fasziniert.",
  "land": "Japan",
  "kurz": "Zeichentrickfilm aus dem Jahr 1953"
 },
 {
  "title": "Sam & Julia im Mäusehaus",
  "folgen": 19,
  "dauer": 7,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-14",
  "url": "https://www.kika.de/sam-julia-im-maeusehaus/videos/der-kinderladen-102",
  "note": "Tonios Eltern müssen Käse für ihren Laden besorgen und schließen ihn deshalb vorübergehend. Julia möchte gerne einmal in einem echten Laden verkaufen."
 },
 {
  "title": "Törtel",
  "folgen": 18,
  "dauer": 23,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-14",
  "url": "https://www.kika.de/toertel/videos/ach-du-lieber-schwan-102",
  "note": "Der sonst so vernünftige Schwan Hokuspokus scheint sich Hals über Kopf in eine schwimmende Artgenossin aus Plastik zu verlieben."
 },
 {
  "title": "Grisu - Der kleine Drache",
  "folgen": 18,
  "dauer": 12,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-14",
  "url": "https://www.kika.de/grisu/videos/achtzehn-der-schluessel-zum-glueck-100",
  "note": "Grisu freut sich - er darf im Feuerwehrauto mitfahren. Bis er dann erfährt, dass Feuerwehrchef David den Schlüssel vom Feuerwehrauto verloren hat."
 },
 {
  "title": "Marcus Level",
  "folgen": 18,
  "dauer": 13,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-04",
  "url": "https://www.kika.de/marcus-level/videos/zweiundvierzig-mission-jahrhundertraub-100",
  "note": "Marcus soll eine Bank ausrauben, um ihr Sicherheitssystem zu testen. Seinem Team wird ein gewisser Vipkrud zugeteilt, den aber Marcus verdächtig findet!"
 },
 {
  "title": "Rudis Rasselbande",
  "folgen": 17,
  "dauer": 11,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-14",
  "url": "https://www.kika.de/rudi/rudis-rasselbande/videos/wuermer-stinken-102",
  "note": "Wurm Lotti ist sehr unglücklich. Eule Eulalia will nicht mit ihr spielen und behauptet sogar, dass Würmer stinken! Was kann Lotti dagegen tun?"
 },
 {
  "title": "1, 2 oder 3",
  "folgen": 16,
  "dauer": 25,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-14",
  "url": "https://www.kika.de/1-2-oder-3/videos/fussball-next-level-102",
  "note": "Tooooor! Wie oft lässt die Männer Fußball-WM in diesem Jahr die Deutschland-Fans jubeln? Ex-Nationalmannschaftskapitän Philipp Lahm gibt seine Einschätzung.",
  "jahr": 1977,
  "land": "Österreich",
  "kurz": "deutsche Fernseh-Quizshow für Kinder"
 },
 {
  "title": "Super Happy Magic Forest",
  "folgen": 16,
  "dauer": 11,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-13",
  "url": "https://www.kika.de/super-happy-magic-forest/videos/die-schnecke-zorgoth-102",
  "note": "Zorgoth der Schreckliche träumt von der Weltherrschaft. Zwar ist er selbst nur eine kleine Schnecke, aber er verfügt über eine Kompressionskugel."
 },
 {
  "title": "Petronella Apfelmus",
  "folgen": 16,
  "dauer": 11,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-10",
  "url": "https://www.kika.de/petronella-apfelmus/videos/das-ueberraschungs-picknick-110",
  "note": "Lea und Luis wollen Petronella mit einem Picknick überraschen. Können sie dabei das Geheimnis des Gartens vor Malina verbergen?"
 },
 {
  "title": "Die beste Klasse Deutschlands",
  "folgen": 16,
  "dauer": 3,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-05",
  "url": "https://www.kika.de/die-beste-klasse-deutschlands/extras/maria-ziffy-in-der-prager-metro-100",
  "note": "Maria Ziffy ist für \"Die beste Klasse Deutschlands\" als Außenreporterin in Prag unterwegs und hat sich hier die Metro ganz genau angeschaut.",
  "jahr": 2008,
  "land": "Deutschland",
  "kurz": "Deutsche Quizsendung für Kinder"
 },
 {
  "title": "Ab nach Alicante",
  "folgen": 16,
  "dauer": 24,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-02",
  "url": "https://www.kika.de/die-wg/mixed-wg-alicante/videos/abschied-unter-traenen-102",
  "note": "Letzter Tag in der Villa: Die WG bereitet die Abschiedsparty vor. Das Motto: \"All White\". Voller Vorfreude erwarten sie die Gäste."
 },
 {
  "title": "Die Muskeltiere",
  "folgen": 16,
  "dauer": 12,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-04",
  "url": "https://www.kika.de/die-muskeltiere/videos/ein-heisser-tanz-102",
  "note": "Ratte Gruyère entdeckt ihre Leidenschaft fürs Tanzen. Pech allerdings, dass sie dabei die Aufmerksamkeit von Frau Fröhlich erregt.",
  "jahr": 2021,
  "land": "Deutschland"
 },
 {
  "title": "Filme",
  "folgen": 14,
  "dauer": 44,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-25",
  "url": "https://www.kika.de/filme/videos/prinzessin-emmy-102",
  "note": "Prinzessin Emmy hat eine besondere Gabe: Sie kann mit Pferden sprechen. Das ist allerdings ihr großes Geheimnis, von dem niemand etwas erfahren darf."
 },
 {
  "title": "Mumintal",
  "folgen": 14,
  "dauer": 22,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-24",
  "url": "https://www.kika.de/mumintal/videos/dreizehn-mittsommerzauber-100",
  "note": "Im Mumintal herrscht gute Stimmung, denn es ist Mittsommer. An diesem Tag scheint die Sonne rund um die Uhr. Das wird gefeiert.",
  "jahr": 2019,
  "land": "Finnland"
 },
 {
  "title": "Der kleine Nick und die Ferien",
  "folgen": 13,
  "dauer": 11,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-16",
  "url": "https://www.kika.de/der-kleine-nick-und-die-ferien/videos/die-maus-s-evierzehn-100",
  "note": "Mama hat eine Maus im Hotel entdeckt und möchte sofort abreisen. Während Papa schon das Auto packt, versuchen Nick und Otto verzweifelt, die Maus zu fangen.",
  "jahr": 2022,
  "land": "Frankreich",
  "kurz": "französisch-schweiz-belgische Animationsserie"
 },
 {
  "title": "STORY TIME",
  "folgen": 13,
  "dauer": 15,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-14",
  "url": "https://www.kika.de/story-time/videos/muay-thai-aidan-trainiert-fuer-die-wm-102",
  "note": "Aidan (10) aus Schottland tritt bei der Muay Thai WM in Italien an. Wie laufen seine Kämpfe gegen Konkurrenten aus aller Welt?"
 },
 {
  "title": "KiKA Sport",
  "folgen": 13,
  "dauer": 1,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-13",
  "url": "https://www.kika.de/kika-sport/mach-mit/kommentieren-deutschlandtour-116",
  "note": "Erzähle uns, was dich am Radsport begeistert. Mit etwas Glück bekommst du die einmalige Chance, bei einer Etappe der Deutschlandtour live zu kommentieren."
 },
 {
  "title": "stark!",
  "folgen": 13,
  "dauer": 15,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-24",
  "url": "https://www.kika.de/stark/videos/nathan-klima-schuetzen-mit-zahlen-102",
  "note": "Nathan will auf Klimakiller aufmerksam machen. Er recherchiert, fotografiert und experimentiert. Wie kann jeder einzelne das Klima schützen?"
 },
 {
  "title": "Anna, Paula, Pia und die wilden Tiere / wilde Natur",
  "folgen": 13,
  "dauer": 24,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "ARD Mediathek"
  ],
  "neu": "2020-12-27",
  "url": "https://www.ardmediathek.de/video/Y3JpZDovL2JyLmRlL3ZpZGVvLzljNGZjMmQ5LWQ4OTgtNDE4Zi04N2Y5LWRmOTY5Yzk2NzZkOA",
  "note": "Wer kennt sie nicht, die Erdhügel im Garten und auf Feldern und Weiden! Anna macht sich heute auf, den kleinen Buddler zu entdecken, der hinter - oder besser gesagt - unter diesen "
 },
 {
  "title": "Bobo Siebenschläfer",
  "folgen": 12,
  "dauer": 7,
  "age": 3,
  "grp": "a3",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-16",
  "url": "https://www.kika.de/bobo-siebenschlaefer/videos/bobo-malt-mit-fingerfarben-110",
  "note": "Bobo und Mama bemalen mit Fingerfarbe die Fenster. Bobo entdeckt, dass man nicht nur mit den Fingern malen kann.",
  "jahr": 2014,
  "land": "Deutschland",
  "kurz": "deutsche Kinder-Zeichentrickserie (2014–2020)"
 },
 {
  "title": "Vegesaurier",
  "folgen": 12,
  "dauer": 5,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-14",
  "url": "https://www.kika.de/sendungen/sendereihen/v/vegesaurier/videos/tanzparty-im-schnee-102",
  "note": "Ginger findet auf einem verschneiten Berg einen am Boden festgefrorenen Erdbeersaurier. Zum Glück bekommt Ginger Hilfe von einem Kiwi-Mammut."
 },
 {
  "title": "Josefine, Törtel und die Tiere",
  "folgen": 12,
  "dauer": 12,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-09",
  "url": "https://www.kika.de/josefine-toertel-und-die-tiere/videos/der-igelfreund-102",
  "note": "Josefine rettet einen verletzten Igel aus dem Garten von Nachbar Lüttkewitz. Zuhause kann sie ihn zusammen mit ihrer Mutter erstversorgen.",
  "jahr": 2025,
  "land": "Deutschland",
  "kurz": "deutsche Animationsserie"
 },
 {
  "title": "Löwenzahn mit Peter Lustig",
  "folgen": 12,
  "dauer": 29,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player",
   "ZDFtivi"
  ],
  "neu": "2026-06-05",
  "url": "https://www.kika.de/loewenzahn-mit-peter-lustig/videos/neun-fluss-100",
  "note": "Peter hat Urlaub nötig. Er macht keine Kreuzfahrt über das Meer, sondern paddelt mit dem Schlauchboot den Fluss hinab. Mal sehen, wo Peter ankommt."
 },
 {
  "title": "Wilde Tiere Reportagen",
  "folgen": 12,
  "dauer": 24,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-17",
  "url": "https://www.kika.de/wilde-tierwelt/die-wilden-tiere/anna-und-die-wilden-tiere/videos/sushi-der-schuhschnabel-100",
  "note": "Tierreporterin Anna ist in den Sümpfen Ugandas auf der Suche nach einem außergewöhnlichen Vogel: dem Schuhschnabel."
 },
 {
  "title": "Unsere Ferien auf Saltkrokan",
  "folgen": 12,
  "dauer": 26,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-15",
  "url": "https://www.kika.de/unsere-ferien-auf-saltkrokan/videos/das-letzte-kapitel-102",
  "note": "Die Ferien auf Saltkrokan gehen zu Ende, alle freuen sich schon aufs nächste Jahr. Doch dann erfahren sie, dass Uffe das Schreinerhäuschen verkaufen will."
 },
 {
  "title": "KiKA Award",
  "folgen": 12,
  "dauer": 3,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-04-25",
  "url": "https://www.kika.de/kika-award/videos/kika-award-highlights-rueckblick-mit-noel-102",
  "note": "Noel ordnet für euch die besten Momente der Preisverleihung ein."
 },
 {
  "title": "Spellbound - Verzaubert in Paris",
  "folgen": 11,
  "dauer": 23,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-23",
  "url": "https://www.kika.de/spellbound-verzaubert-in-paris/videos/magische-machtprobe-102",
  "note": "Obwohl Cece und Bash eine Verbindung als Mystic-Paar eingegangen sind, sind sie immer noch in der Krypta gefangen.",
  "land": "Deutschland",
  "kurz": "Fernsehserie"
 },
 {
  "title": "Taylors Welt der Tiere",
  "folgen": 10,
  "dauer": 11,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-16",
  "url": "https://www.kika.de/taylors-welt-der-tiere/videos/ein-flaeschchen-fuer-lucy-102",
  "note": "Das Riesenflughund-Weibchen Mina ist verletzt und wird von Hector behandelt. Taylor und Tommy sollen Minas Junges \"Lucy\" mit dem Fläschchen zu füttern.",
  "land": "Kanada",
  "kurz": "französische Animationsserie aus dem Jahr 2024"
 },
 {
  "title": "SingAlarm",
  "folgen": 10,
  "dauer": 13,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-13",
  "url": "https://www.kika.de/singalarm/videos/sechs-dino-songs-100",
  "note": "Rawrrr - die Dinos sind los! Singa und SingDing sind total fasziniert. Am liebsten wäre SingDing selbst ein \"Flugsaurier\" wie aus dem Lied von Heavysaurus."
 },
 {
  "title": "Tanoshii",
  "folgen": 10,
  "dauer": 23,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-11",
  "url": "https://www.kika.de/tanoshii/videos/knockout-justnero-und-imahairyoldman-vs-harut-und-anigents-102",
  "note": "Vier starten, nur eine Person bleibt am Ende stehen - Harut, Anigents, JustNero und Anni liefern sich den Tanoshii Knockout. Wer holt sich den Titel?"
 },
 {
  "title": "Dein Song 2026",
  "folgen": 10,
  "dauer": 0,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-02",
  "url": "https://www.kika.de/dein-song/mach-mit/voting-constantin-flugmodus-an-100",
  "note": "Jeannie und Luca sind von euren Songs begeistert. Ein riesiges Dankeschön an alle Talente, die sich beworben haben."
 },
 {
  "title": "Sommer.Sonne.Elternfrei.",
  "folgen": 10,
  "dauer": 24,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-16",
  "url": "https://www.kika.de/die-wg/jungs-gardasee/videos/zwanzig-die-jungs-wg-in-italien-102",
  "note": "Der letzte Tag in der Jungs-WG! Leroy, Luc, Nils, Ole und Robin wollen mit einer großen Party den Abschied etwas leichter machen."
 },
 {
  "title": "Ritter Rost",
  "folgen": 10,
  "dauer": 12,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-10",
  "url": "https://www.kika.de/ritter-rost/videos/sechsundzwanzig-die-abschlusspruefung-100",
  "note": "Wenn Ritter Rost eines hasst, dann das Büffeln für die Prüfung, um seine Ritterlizenz zu verlängern.",
  "jahr": 2013,
  "land": "Deutschland",
  "kurz": "3D-Animationsserie"
 },
 {
  "title": "Die Abenteuer-Checker Staffel 1",
  "folgen": 10,
  "dauer": 12,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "ORF ON"
  ],
  "neu": "2025-03-16",
  "url": "https://on.orf.at/video/14266244/die-abenteuerchecker-survival-camp",
  "note": "Die \"Abenteuer-Checker\" Benni und Gucki gehen auf eine aufregende Entdeckungsreise in die Wildnis. Gemeinsam mit den Outdoor-Experten Benedikt und Jonathan entdecken sie, wie man o"
 },
 {
  "title": "TickTack Zeitreise mit Lisa & Lena",
  "folgen": 9,
  "dauer": 24,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-14",
  "url": "https://www.kika.de/ticktack-zeitreise-mit-lisa-und-lena/videos/radiogeschichte-102",
  "note": "Eine Zeitreise durch die Radiogeschichte. Lisa und Lena sind in einer Ausstellung zum 100. Geburtstag des Radios und live beim SWR-Jugendsender DASDING."
 },
 {
  "title": "Tigerenten Club",
  "folgen": 9,
  "dauer": 58,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-06",
  "url": "https://www.kika.de/tigerenten-club/tigerenten-club/videos/roboter-action-die-bohlebots-im-tigerenten-cub-100",
  "note": "Robos auf die 1! Die deutschen Meisterinnen im Robocup Soccer - also Roboter-Fußball - zeigen ihre Roboter, mit denen sie den WM-Titel holen wollen."
 },
 {
  "title": "Schau in meine Welt!",
  "folgen": 9,
  "dauer": 25,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-03",
  "url": "https://www.kika.de/schau-in-meine-welt/videos/lisa-und-die-schimpansen-106",
  "note": "Lisa ist 13 Jahre alt und hat ungewöhnliche Freunde: Schimpansen!"
 },
 {
  "title": "ICH bin ICH",
  "folgen": 8,
  "dauer": 7,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-16",
  "url": "https://www.kika.de/ich-bin-ich/videos/einundfuenfzig-pelle-rasmus-und-leo-bauen-einen-staudamm-100",
  "note": "Pelle und Rasmus sind Zwillingsbrüder. Durch den kleinen Ort, in dem Pelle und Rasmus zu Hause sind, schlängelt sich ein Bach. Dort spielen sie am liebsten."
 },
 {
  "title": "Animanimals",
  "folgen": 8,
  "dauer": 4,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-14",
  "url": "https://www.kika.de/animanimals/videos/fuenfunddreissig-marienkaefer-100",
  "note": "Der Marienkäfer mag seinen Nachbarn nicht. Oder?",
  "jahr": 2013,
  "land": "Deutschland",
  "kurz": "Kinder-Zeichentrickserie (2013–2018)"
 },
 {
  "title": "Urlaub ohne Eltern",
  "folgen": 8,
  "dauer": 25,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-13",
  "url": "https://www.kika.de/die-wg/maedchen-mallorca/videos/acht-die-maedchen-wg-urlaub-ohne-eltern-100",
  "note": "Mehr als eine Woche WG-Leben hat Spuren hinterlassen: In der Traumvilla der fünf Mädchen sieht es wüst aus."
 },
 {
  "title": "Checkpoint",
  "folgen": 8,
  "dauer": 25,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-11",
  "url": "https://www.kika.de/checkpoint/videos/-auf-dem-bau-falschspieler-und-riesenflummi-100",
  "note": "Falschspielen, ohne dass der Schwindel auffliegt? Checkpoint testet Täuschungen!",
  "jahr": 2003,
  "land": "Niederlande",
  "kurz": "niederländische Fernsehserie"
 },
 {
  "title": "Zum ersten Mal",
  "folgen": 8,
  "dauer": 14,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-21",
  "url": "https://www.kika.de/zum-ersten-mal/videos/sturmfrei-132",
  "note": "Kajs Mütter gehen essen und ermahnen ihren Sohn, niemandem die Tür zu öffnen. Benjamin freut sich über einen Abend ohne seine Mutter."
 },
 {
  "title": "Goat Girl",
  "folgen": 8,
  "dauer": 11,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-16",
  "url": "https://www.kika.de/goat-girl/videos/dreiundzwanzig-kyles-berufung-100",
  "note": "Berufstest-Schock: Kyle erhält keine Empfehlung! Während Kallista tobt, wollen Gigi und Saige ihm helfen, seine echte Berufung zu entdecken."
 },
 {
  "title": "TanzAlarm",
  "folgen": 7,
  "dauer": 12,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-13",
  "url": "https://www.kika.de/tanzalarm/videos/kochloeffelkonzert-108",
  "note": "Tom muss sich als singenden Spaghetti-Koch ausgeben, um die Vermietern zu besänftigen. Die TanzAlarm-Kids entspannen mit Sukini und singen ihre Songs."
 },
 {
  "title": "Sesamstraße Magazin",
  "folgen": 7,
  "dauer": 2,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "ARD Mediathek"
  ],
  "neu": "2023-06-27",
  "url": "https://www.ardmediathek.de/video/Y3JpZDovL25kci5kZS9kZGRmNmZhMi01NWJkLTQyNDAtYjE1Zi0wYWVmZWI2MzRlNDg",
  "note": "Natürlich möchte Graf Zahl im Urlaub etwas Neues zählen. So zählt er voller Freude Segelboote, Pelikane und Fische."
 },
 {
  "title": "FC Internat - Fußball ist unser Leben",
  "folgen": 6,
  "dauer": 0,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-04",
  "url": "https://www.kika.de/fc-internat-fussball-ist-unser-leben/kennenlernen/leonie-steckbrief-100",
  "note": "Lerne Nachwuchs-Fußballerin Leonie besser kennen!"
 },
 {
  "title": "Minus Drei und die wilde Lucy",
  "folgen": 6,
  "dauer": 11,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-04-19",
  "url": "https://www.kika.de/minus-drei-und-die-wilde-lucy/videos/meso-weiss-es-102",
  "note": "Der coole Kioskbesitzer Meso übergibt für einen Tag das Geschäft an Minus Drei und Lucy."
 },
 {
  "title": "Rudis Rabenteuer",
  "folgen": 5,
  "dauer": 12,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-14",
  "url": "https://www.kika.de/rudi/rudis-rabenteuer/videos/die-maeusefantenfeuerwehr-102",
  "note": "Rudis Kiste zeigt ihm und Lotti die Geschichte von Mäuschen Emma. Sie feiert ihren vierten Geburtstag!"
 },
 {
  "title": "Surviving Summer",
  "folgen": 5,
  "dauer": 25,
  "age": 12,
  "grp": "a10",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-13",
  "url": "https://www.kika.de/surviving-summer/videos/kein-druck-102",
  "note": "Das Team aus Shorehaven kommt zu den Subtropix 360-Wettkämpfen, wo Ari und Bodhi viel Aufmerksamkeit bekommen.",
  "jahr": 2022,
  "land": "Australien"
 },
 {
  "title": "Anna, Nina, Pia und die Haustiere",
  "folgen": 5,
  "dauer": 14,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-16",
  "url": "https://www.kika.de/wilde-tierwelt/die-haustiere/nina-und-die-haustiere/videos/zwerggarnelen-102",
  "note": "Nina schaut sich die bunte Welt der Zwerggarnelen an. Die winzigen Krebstiere sind zwar klein, können aber überraschend faszinierende Haustiere sein."
 },
 {
  "title": "Löwenzähnchen",
  "folgen": 5,
  "dauer": 8,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-04-17",
  "url": "https://www.kika.de/loewenzaehnchen/videos/strauss-102",
  "note": "Keks trifft bei seinem Streifzug auf den größten Vogel der Welt. Sabo Strauß erzählt Keks aufgeregt, dass ein Ei verschwunden sei und zeigt ihm sein Nest."
 },
 {
  "title": "Anna, Paula, Pia und die wilden Tiere",
  "folgen": 5,
  "dauer": 24,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "ARD Mediathek"
  ],
  "neu": "2023-09-24",
  "url": "https://www.ardmediathek.de/video/Y3JpZDovL2JyLmRlL3ZpZGVvLzE2ZTI2YTFhLTY3ZWMtNGIwMy1hYWRiLTRlMGVmMTAzNjUzYg",
  "note": "Pia geht ganz nah ran an die Kreuzotter und hat riesen Respekt, denn der Biss dieser Giftschlange ist nicht ganz ungefährlich. Sie darf sogar eine Baby-Kreuzotter in die Hand nehme"
 },
 {
  "title": "Sommer.Son­ne.Elternfrei.",
  "folgen": 4,
  "dauer": 24,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-16",
  "url": "https://www.kika.de/die-wg/maedchen-gardasee/videos/vier-die-maedchen-wg-sommer-sonne-elternfrei-100",
  "note": "Der WG-Morgen beginnt mit einem verrückten Frisuren-Contest: Jolina, Kaya, Luna, Natalie und Serena sind von den haarsträubenden Ergebnissen begeistert."
 },
 {
  "title": "starting point",
  "folgen": 4,
  "dauer": 2,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-12",
  "url": "https://www.kika.de/kinderredaktionsrat/mach-mit/bewirb-dich-152",
  "note": "Du hast Ideen, eine Meinung und Lust auf Medien? Werde Teil des Kinderredaktionsrates! Hier darfst du mitreden, mitgestalten und mitentscheiden. Bewirb dich!"
 },
 {
  "title": "Maulwurf Moley",
  "folgen": 4,
  "dauer": 11,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-12",
  "url": "https://www.kika.de/maulwurf-moley/videos/dem-geheimnis-auf-der-spur-104",
  "note": "Moley und Dotty beobachten zufällig den Alten Kauz, der sich abends heimlich davonschleicht."
 },
 {
  "title": "Feuerwehrmann Sam",
  "folgen": 4,
  "dauer": 10,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-12",
  "url": "https://www.kika.de/feuerwehrmann-sam/videos/ein-wirklich-scharfer-snack-102",
  "note": "Polizeimeister Malcolm wird beim Tag der offenen Tür vorgestellt. Er wird die Feuerwehr unterstützen. Der erste Einsatz lässt nicht lange auf sich warten.",
  "jahr": 1987,
  "land": "Vereinigtes Königreich",
  "kurz": "Kinderfernsehserie"
 },
 {
  "title": "First Day",
  "folgen": 4,
  "dauer": 22,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-01",
  "url": "https://www.kika.de/first-day-ich-bin-hannah/videos/alles-ist-moeglich-folge-vier-100",
  "note": "Bei der Schulversammlung versucht Hannah Schüler*innen und Eltern davon zu überzeugen, eine Änderung der Uniformvorschriften zu unterstützen.",
  "jahr": 2020,
  "land": "Australien"
 },
 {
  "title": "Simon Superhase",
  "folgen": 4,
  "dauer": 5,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-03",
  "url": "https://www.kika.de/simon-superhase/videos/rettet-den-ozean-102",
  "note": "Simon Ferdinand, Lou und Franz verbringen den Tag mit Opa am Strand. Beim Drachenfliegen entdecken sie große Mengen Müll im Meer."
 },
 {
  "title": "4 1/2 Freunde",
  "folgen": 4,
  "dauer": 24,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-04-25",
  "url": "https://www.kika.de/4-12-freunde/videos/hausmeister-des-grauens-104",
  "note": "Das Armband von Freds Lehrerin ist verschwunden! Fred will diesen Fall unbedingt allein lösen, um ihr zu imponieren."
 },
 {
  "title": "Ein Fall für TKKG",
  "folgen": 4,
  "dauer": 24,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-04-18",
  "url": "https://www.kika.de/ein-fall-fuer-tkkg/videos/fuenfundzwanzig-wer-raubte-das-millionenpferd-100",
  "note": "Tim, Karl und Klößchen holen Gabi vom Reiterhof ab. In dem Gestüt steht auch \"Ringo\". Ein Millionenpferd, sagt Karl.",
  "jahr": 1985,
  "land": "Deutschland",
  "kurz": "deutsche Fernsehserie (1985–1987)"
 },
 {
  "title": "Anna und die wilden Tiere",
  "folgen": 4,
  "dauer": 24,
  "age": 6,
  "grp": "a6",
  "genre": "Wissen",
  "prov": [
   "3sat"
  ],
  "neu": "2023-01-03",
  "url": "https://www.3sat.de/dokumentation/anna-und-die-wilden-tiere/anna-und-die-wilden-tiere-im-revier-der-tiger-100.html",
  "note": "Anna ist diesmal auf der Suche nach einer der größten Raubkatzen der Erde, dem Tiger. Genauer gesagt, dem Sumatra-Tiger. Der Regenwald der indonesischen Insel Sumatra ist sein Zuha",
  "jahr": 2014,
  "land": "Deutschland",
  "kurz": "Tier-Doku-Fernsehserie"
 },
 {
  "title": "Schloss Einstein und die Pfefferkörner auf Gangsterjagd",
  "folgen": 4,
  "dauer": 8,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-03-03",
  "url": "https://www.kika.de/schloss-einstein/schloss-einstein-und-die-pfefferkoerner-auf-gangsterjagd/videos/folge-zwei-auf-gangsterjagd-s-ezwei-102",
  "note": "Io und Joyce stehen vor einem Rätsel: Warum bricht jemand ins Internat ein? Währendessen haben die Pfefferkörner am Museum bereits einen ersten Verdacht."
 },
 {
  "title": "Meister Eder und sein Pumuckl",
  "folgen": 4,
  "dauer": 23,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "ARD Mediathek"
  ],
  "neu": "2026-07-25",
  "url": "https://www.ardmediathek.de/video/Y3JpZDovL2JyLmRlL3ZpZGVvLzVhZTUxYzEwLTA2NzgtNGU5ZC04ZmYyLTg4MmVlYzMxYTE1ZC9icm9hZGNhc3Q",
  "note": "Meister Eders Schwester ist zu Besuch, um mal wieder für ihn zu kochen. Zum Nachtisch gibt es Schokoladenpudding. Pumuckl ist begeistert und beschließt, dass es nun jeden Tag Puddi",
  "jahr": 1982,
  "land": "Ungarn",
  "kurz": "deutsche Kinderfernsehserie (1982–1989)"
 },
 {
  "title": "Augsburger Puppenkiste",
  "folgen": 4,
  "dauer": 27,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "3sat"
  ],
  "neu": "2022-12-28",
  "url": "https://www.3sat.de/film/augsburger-puppenkiste/kleiner-koenig-kalle-wirsch-3-die-falle-100.html",
  "note": "Der kleine König und seine Freunde Max und Jenny sind auf dem Weg zur Kampfstätte für den Zweikampf mit Zoppo. Vor dem Rubinberg muss Kalle Wirsch drei Rätsel lösen, damit sie pass"
 },
 {
  "title": "Shaun, das Schaf",
  "folgen": 4,
  "dauer": 7,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "ARD Mediathek"
  ],
  "neu": "2023-01-01",
  "url": "https://www.ardmediathek.de/video/Y3JpZDovL2Rhc2Vyc3RlLmRlL3NoYXVuLWRhcy1zY2hhZi8zNmUyOTYxZC04NjMzLTRkOTEtYTIwOC0zN2NkNGY4M2M0MjA",
  "note": "Der erste Schnee ist da, Shaun und seine Freunde sind begeistert! Während die Schafe sich mit Curling und Eislaufen vergnügen, erweist sich Bitzer als hervorragender Snowboarder.",
  "jahr": 2007,
  "land": "Vereinigtes Königreich",
  "kurz": "britische Fernsehserie von Richard Goleszowski und Christopher Sadler"
 },
 {
  "title": "Tom Sawyer",
  "folgen": 3,
  "dauer": 22,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-12",
  "url": "https://www.kika.de/tom-sawyer/videos/wie-tom-zu-indianer-joes-komplizen-wurde-106",
  "note": "Tom lässt sich von Bandit Joe reinlegen. Ohne es zu ahnen, wird er zum Komplizen und schleust einen Schlüssel ins Gefängnis, mit dem Muff ausbrechen kann.",
  "land": "Vereinigte Staaten",
  "kurz": "deutscher Kinder-Spielfilm von Hermine Huntgeburth (2011)"
 },
 {
  "title": "Glücksbärchis - Willkommen im Wolkenland",
  "folgen": 3,
  "dauer": 21,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-11",
  "url": "https://www.kika.de/gluecksbaerchis-willkommen-im-wolkenland/videos/fuenfzehn-teilen-macht-spass-100",
  "note": "Die Zwillingsschwestern Heidi und Josi benötigen dringend eine Lektion im Teilen. Teile-Gern-Bärchi löst versehentlich einen heiklen Verdopplungszauber aus."
 },
 {
  "title": "Trio - Die Kepler Diamanten",
  "folgen": 3,
  "dauer": 24,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-07",
  "url": "https://www.kika.de/trio-die-kepler-diamanten/videos/der-einbruch-110",
  "note": "Nora beharrt weiterhin darauf, dass sie Hinweise gefunden hätten, dass ihr Vater noch am Leben ist."
 },
 {
  "title": "Stark mit Fidi",
  "folgen": 3,
  "dauer": 8,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-23",
  "url": "https://www.kika.de/stark-mit-fidi/videos/gabriel-will-was-erzaehlen-102",
  "note": "Gabriel will von seinem Fußballtraining erzählen. Doch Mama hört nur der Schwester zu und sagt: nicht reinquatschen. Wütend geht Gabriel zu Fidi."
 },
 {
  "title": "Nö-Nö Schnabeltier",
  "folgen": 2,
  "dauer": 7,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-15",
  "url": "https://www.kika.de/noe-noe-schnabeltier/videos/ich-will-heute-gefeiert-werden-132",
  "note": "Nö-Nö hat Geburtstag. Doch seine Freunde scheinen das vergessen zu haben. Enttäuscht will Nö-Nö Bad Unterholz verlassen.",
  "jahr": 2017,
  "land": "Frankreich",
  "kurz": "französische animierte Zeichentrickserie (2017–2019)"
 },
 {
  "title": "Die Kinder von Bullerbü",
  "folgen": 2,
  "dauer": 23,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-24",
  "url": "https://www.kika.de/die-kinder-von-bullerbue/videos/die-kinder-von-bullerbue-spinat-und-schwarze-schuhcreme-100",
  "note": "Inga und Lisa sollen auf Kerstin aufpassen. Erst will Kerstin nicht essen, dann schreit sie wie am Spieß. Und zum Schluss bemalt sie noch die ganze Küche.",
  "jahr": 1961,
  "land": "Schweden",
  "kurz": "Film von Lasse Hallström (1986)"
 },
 {
  "title": "Zeig mir Feiertage!",
  "folgen": 2,
  "dauer": 11,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-22",
  "url": "https://www.kika.de/zeig-mir-feiertage/videos/zeig-mir-pfingsten-100",
  "note": "Pfingsten wird jedes Jahr von vielen Menschen gefeiert? Aber was wird da genau gefeiert? Feiertagsreporterin Elisabeth findet die Antworten."
 },
 {
  "title": "Blinky Bill",
  "folgen": 2,
  "dauer": 76,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-14",
  "url": "https://www.kika.de/blinky-bill/videos/blinky-bill-das-meer-der-weissen-drachen-106",
  "note": "Als Blinkys Vater William nicht wie versprochen von seiner gefährlichen Expedition aus dem Outback zurückkommt, beschließt der junge Koala ihn zu suchen.",
  "jahr": 1992,
  "land": "Australien",
  "kurz": "australische Animationsserie (1993–2004)"
 },
 {
  "title": "Kicken wie ein Mädchen",
  "folgen": 2,
  "dauer": 24,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-04-29",
  "url": "https://www.kika.de/kicken-wie-ein-maedchen/videos/leidenschaft-102",
  "note": "Zum Fußball gehört die Liebe zur Mannschaft: Die U15-Spielerinnen der SGS Essen fragen sich, wie sie als Team zusammenwachsen und erfolgreich sein können."
 },
 {
  "title": "Magic Pranks - Ausgetrickst mit den Ehrlich Brothers",
  "folgen": 2,
  "dauer": 24,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-04-24",
  "url": "https://www.kika.de/magic-pranks-102/videos/zwillingsprank-und-sushi-kochkurs-102",
  "note": "Doppelt witzig: Die Zwillinge Vin und Lex starten ein verrücktes Prank-Spiel im Einkaufszentrum. Mit Komplizin Jeannie sorgen sie für erstaunte Gesichter."
 },
 {
  "title": "Tib und Tumtum",
  "folgen": 2,
  "dauer": 12,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-04-12",
  "url": "https://www.kika.de/tib-tumtum/videos/sechsundzwanzig-das-grosse-rote-biest-100",
  "note": "Nach einem Streit mit den Bären verschwinden plötzlich Sachen. Kori meint, ein \"rotes Biest\" gesehen zu haben. Ist Tumtum der Dieb?"
 },
 {
  "title": "Sesamstraße präsentiert: Eine Möhre für Zwei",
  "folgen": 2,
  "dauer": 12,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "ARD Mediathek"
  ],
  "neu": "2019-01-06",
  "url": "https://www.ndr.de/fernsehen/sendungen/Der-perfekte-Freund,sendung309118.html",
  "note": "Pferd hat einfach zu nichts Lust. Wenn Pferd nicht mit ihm spielt, dann baut Wolle sich eben einen neuen Freund. Und wirklich: Wolles neuer Freund kann viele tolle Sachen machen."
 },
 {
  "title": "Die Schlümpfe",
  "folgen": 1,
  "dauer": 12,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-06-11",
  "url": "https://www.kika.de/die-schluempfe/videos/einhundertsechsunddreissig-diskomania-100",
  "note": "Meteorit entdeckt einen Tanzpalast und fordert die Schlümpfe auf, tanzen zu gehen. Zu spät merkt sie, dass sie in eine Falle von Gargamel getappt ist.",
  "jahr": 1981,
  "land": "Vereinigte Staaten",
  "kurz": "US-amerikanische Fernsehserie (1981–1989)"
 },
 {
  "title": "Mascha und der Bär",
  "folgen": 1,
  "dauer": 7,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-29",
  "url": "https://www.kika.de/mascha-und-der-baer/mascha-und-der-baer/videos/sechsundsechzig-baelle-fuer-alle-faelle-102",
  "note": "Um zur Ruhe zu kommen, empfehlen die Wölfe dem Bären das Golfspiel. Doch dann wird der Bär von Mascha und dem Panda auf dem Grün begleitet.",
  "jahr": 2009,
  "land": "Russland",
  "kurz": "russische 3D-Animationsserie"
 },
 {
  "title": "Abgetaucht! - Meine falschen Ferien",
  "folgen": 1,
  "dauer": 43,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-22",
  "url": "https://www.kika.de/abgetaucht-meine-falschen-ferien/videos/abgetaucht-meine-falschen-ferien-114",
  "note": "Seit Wochen prahlt Aaron mit seinem Tauchurlaub. Als dieser platzt, beschließt Aaron, den Urlaub mit Hilfe seiner Freundin Nina über seinen Kanal zu faken."
 },
 {
  "title": "Kikaninchen und Freunde",
  "folgen": 1,
  "dauer": 26,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-16",
  "url": "https://www.kika.de/kikaninchen-und-freunde/videos/vom-ballspielen-skaten-und-seilspringen-102",
  "note": "Fin nimmt am Krabbenkrabbeln teil. Kikaninchen erzählt vom Tintenfisch. T-Rex ist schlecht im Basketball. Aylins Rolli ist mehr als ein Gefährt."
 },
 {
  "title": "Astrobrot",
  "folgen": 1,
  "dauer": 2,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-05-12",
  "url": "https://www.kika.de/bernd-das-brot/musik/bergmelodielied-100",
  "note": "Durch Täler und über Gipfel hallen Stimmen und Blechbläser. Die Bergmelodie ist einfach da – in der Natur, in den Häusern und direkt in Bernds Ohren."
 },
 {
  "title": "CHECK IN - Marinas Rätsel-Abenteuer",
  "folgen": 1,
  "dauer": 15,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-04-25",
  "url": "https://www.kika.de/checker-welt/check-in-marinas-raetsel-abenteuer/videos/schreckgespenst-im-gruselhaus-102",
  "note": "Dieses Rätsel-Abenteuer ist erschreckend gruselig. Im Geisterhaus lernt Marina, warum wir uns manchmal gerne gruseln."
 },
 {
  "title": "Leo da Vinci",
  "folgen": 1,
  "dauer": 13,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-04-22",
  "url": "https://www.kika.de/leo-da-vinci/videos/das-maedchen-und-der-stier-108",
  "note": "Auf dem Festland erfahren die Freunde von Maria, dass zwei Männer versucht haben, in ihre Raupe einzudringen. Ist die Gefahr näher als sie denken?",
  "jahr": 2019,
  "land": "Italien",
  "kurz": "Animationsserie"
 },
 {
  "title": "Edmund und Luzie",
  "folgen": 1,
  "dauer": 11,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "KiKA-Player"
  ],
  "neu": "2026-04-14",
  "url": "https://www.kika.de/edmund-und-luzie/videos/die-geschichtensteine-112",
  "note": "Edmund und Luzie langweilen sich schrecklich. Da kommt Georg Eule auf die Idee ihnen eine Aufgabe zu geben."
 },
 {
  "title": "Die Abenteuer-Checker Staffel 2",
  "folgen": 1,
  "dauer": 12,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "ORF ON"
  ],
  "neu": "2026-06-14",
  "url": "https://on.orf.at/video/14327167/die-abenteuerchecker-fussball",
  "note": "Benni und Gucki sind diesmal in der aufregenden Welt des Fußballs unterwegs, um die wichtigsten Fakten rund um die beliebte Sportart unter die Lupe nehmen. Ein besonderes Highlight"
 },
 {
  "title": "Vom kleinen Maulwurf, der wissen wollte, wer ihm auf den Kopf gemacht hat",
  "folgen": 1,
  "dauer": 56,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "ORF ON"
  ],
  "neu": "2026-03-29",
  "url": "https://on.orf.at/video/14316467/vom-kleinen-maulwurf-der-wissen-wollte-wer-ihm-auf-den-kopf-gemacht-hat",
  "note": "Wie klingt eigentlich ein frischer Pferdeapfel oder ein herabplatschender Kuhfladen? Noch viel wichtiger für den kleinen kurzsichtigen Maulwurf ist es, herauszufinden, wie der Kot "
 },
 {
  "title": "Shaun, das Schaf - Rettet den Baum",
  "folgen": 1,
  "dauer": 7,
  "age": 6,
  "grp": "a6",
  "genre": "Zeichentrick",
  "prov": [
   "ARD Mediathek"
  ],
  "neu": "2020-12-27",
  "url": "https://www.ardmediathek.de/video/Y3JpZDovL2Rhc2Vyc3RlLmRlL3NoYXVuLCBkYXMgc2NoYWYvMzFiMjJmYzMtZGJhMC00OWYxLWJiMWYtOTM2Y2ZlNGMyNTY4",
  "note": "Es ist so kalt, dass der Bauer schon wieder neues Brennholz braucht. Als er im Wald kein Glück hat, nimmt er ausgerechnet den Lieblingsbaum der Schafe ins Visier!"
 }
]
