# -*- coding: utf-8 -*-
"""Kindersendungen der Vollprogramme.

Erzeugt von scan_kinder.py aus tv.de am 01.09.2026. Auswahl nach Kategorie,
bekannten Titeln und Beschreibung; Alterswerte heuristisch.
"""

TAGE = [
    ("Dienstag, 01.09.2026", "ZDF", [
        ('20:15', 'besseresser: Die Tricks in Bärchenwurst, Pizzateig & Co.', 'Sebastian Lege deckt auf', 'Serie', 45, 10, 'a10', 55, 'Ob überraschende Zusatzstoffe, cleveres Kindermarketing oder irreführendes Verpackungsdesign: Sebast'),
    ]),
    ("Dienstag, 01.09.2026", "RTLzwei", [
        ('18:05', 'Hartz und herzlich - Tag für Tag Benz-Baracken', 'Pommes-Party', 'Serie', 60, 6, 'a6', 55, 'Wegen häufiger Kopfschmerzen und anderer Beschwerden hat Andy beim Arzt abchecken lassen, ob er viel'),
    ]),
    ("Dienstag, 01.09.2026", "ProSieben Maxx", [
        ('16:45', 'Dr. STONE', 'First Dream', 'Anime', 25, 12, 'a10', 55, 'Senku hat den Kampf gegen Ibara gewonnen und kann seine Freunde nun nach und nach wiederbeleben. Zue'),
        ('17:10', 'Dragon Ball Super', 'Gefährliche Reflexion! Attacke des unsichtbaren Angreifers!', 'Anime', 25, 12, 'a10', 55, 'Noch verbleiben 35 Minuten, um das Turnier der Universen zu gewinnen. Mit der schwindenden Zeit nimm'),
        ('17:35', 'Detektiv Conan', 'Der Teufel im Fernsehstudio (1)', 'Anime', 25, 12, 'a10', 55, 'Yoko lädt die Detective Boys und Professor Agasa in ein Fernsehstudio ein. Dort treffen die Kinder a'),
        ('18:00', 'One Piece', 'Tief in der Mine - Ruffy gegen den menschlichen Zug!', 'Anime', 25, 12, 'a10', 55, 'Bartolomeo und Ruffy sitzen in den Schächten der Silver Mine fest und leisten damit ehemaligen Pirat'),
        ('18:25', 'One Piece', 'In der Hitze des Gefechts - Law und Zorro eilen zur Hilfe!', 'Anime', 30, 12, 'a10', 55, 'Ruffy, Bartolomeo und Desire befinden sich weiterhin unter Tage, als sie von Avelon angegriffen werd'),
        ('18:55', 'Detektiv Conan', 'Den Männern in Schwarz auf der Spur (3)', 'Anime', 30, 12, 'a10', 55, 'Die vorübergehend wieder zu ihrer eigentlichen Größe zurückgekehrte Sherry kann durch den Kamin aufs'),
    ]),
    ("Dienstag, 01.09.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Der Löwe auf meiner Schmusedecke hat ein Problem: Er kann nicht mehr brüllen! Werden seine Freunde e'),
    ]),
    ("Dienstag, 01.09.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Meine Schmusedecke: Der Löwe'),
    ]),
    ("Dienstag, 01.09.2026", "SRF 1", [
        ('17:30', 'Timmy Ziit - Baby', '', 'Vorlesen', 10, 6, 'a6', 55, 'Timmy ist das freche kleine Schaf aus Shauns Herde. Jeden Tag geht er in den Kindergarten, wo er gem'),
        ('23:55', 'Les hirondelles de Kaboul', '', 'Zeichentrick', 25, 10, 'a10', 55, 'Im Sommer 1998 wird die afghanische Hauptstadt Kabul von den Taliban beherrscht. Die Stadt liegt in '),
    ]),
    ("Mittwoch, 02.09.2026", "RTLzwei", [
        ('16:05', 'Hartz und herzlich - Tag für Tag Benz-Baracken', 'Pommes-Party', 'Serie', 60, 6, 'a6', 55, 'Wegen häufiger Kopfschmerzen und anderer Beschwerden hat Andy beim Arzt abchecken lassen, ob er viel'),
        ('22:15', 'Zuhause im Glück - Unser Einzug in ein neues Leben', 'Zwischen Hoffnung, Trauer und Neubeginn', 'Serie', 25, 10, 'a10', 55, 'Mathias (31) und Julia (†29) verlieben sich 2002 ineinander. Sie sind drei Jahre zusammen, dann komm'),
    ]),
    ("Mittwoch, 02.09.2026", "ProSieben Maxx", [
        ('16:40', 'Dr. STONE', 'Die Schatzinsel', 'Anime', 25, 12, 'a10', 55, 'Nachdem das Abenteuer auf der Schatzinsel bestanden ist, haben die Wissenschaftler direkt die nächst'),
        ('17:05', 'Dragon Ball Super', 'F will Rache! Eine überaus tückische Falle!', 'Anime', 25, 12, 'a10', 55, 'Mittlerweile ringen noch 36 Kämpfer um den Sieg und letztlich auch um die Existenz ihres jeweiligen '),
        ('17:30', 'Detektiv Conan', 'Der Teufel im Fernsehstudio (2)', 'Anime', 35, 12, 'a10', 55, 'Inspektor Megure rückt an, um den Mord an Tenji Urushihara, dem Direktor einer Produktionsfirma, auf'),
        ('18:05', 'One Piece', 'Eine auswegslose Situation! - Der heiße Kampf auf Silver Mine', 'Anime', 25, 12, 'a10', 55, 'Nachdem Bill immer wieder mit Provokationen um sich wirft, kommt es zwischen ihm und Ruffy zum Kampf'),
        ('18:30', 'One Piece', 'Ein neues Abenteuer beginnt! - Ankunft auf der Phantominsel Zou', 'Anime', 25, 12, 'a10', 55, 'An Bord des Schiffes erzählt Bartolomeo der Crew bewegende Geschichten und bittet auch Ganbia, sich '),
        ('18:55', 'Detektiv Conan', 'Den Männern in Schwarz auf der Spur (4)', 'Anime', 25, 12, 'a10', 55, 'Kann Conan endlich den Mörder von Hirota finden? Ai liefert ihm schließlich den entscheidenden Hinwe'),
    ]),
    ("Mittwoch, 02.09.2026", "NDR", [
        ('06:00', 'Sesamstraße', '', 'Vorlesen', 20, 3, 'a3', 55, 'Bert freut sich auf eine entspannte Lektüre, als Ernie vorbeikommt und ein "Fantasieschlagzeug" aufb'),
    ]),
    ("Mittwoch, 02.09.2026", "BR", [
        ('23:50', 'Böse Spiele - Rimini Sparta', '', 'Serie', 25, 10, 'a10', 55, 'Der Tod der Mutter bringt zwei Brüder noch einmal kurz zusammen - im leer stehenden Elternhaus, wo a'),
    ]),
    ("Mittwoch, 02.09.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Die Erdmännchen Jan und Henry sind beunruhigt. Hat sich da etwa ein Krokodil in ihre Küche geschlich'),
    ]),
    ("Mittwoch, 02.09.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Jan & Henry: Das weinende Krokodil'),
    ]),
    ("Mittwoch, 02.09.2026", "HR", [
        ('06:15', 'Leo da Vinci', 'Das Wappentier', 'Zeichentrick', 10, 3, 'a3', 55, 'Nachdem sie die geheimnisvolle Botschaft gelesen haben, sind die Freunde etwas ratlos. Lollo spionie'),
        ('06:25', 'Leo da Vinci', 'Die Augen des Löwen', 'Zeichentrick', 15, 3, 'a3', 55, 'Lisa und Bianca werden von dem jungen Alvise Tiepolo in den Palazzo zu einem Maskenball eingeladen. '),
    ]),
    ("Mittwoch, 02.09.2026", "arte", [
        ('04:34', 'Athleticus', 'Kellner-Wettlauf', 'Zeichentrick', 31, 3, 'a3', 55, 'Die dritte Staffel des Kurzprogramms wirft in 30 neuen Folgen einen humorvollen Blick auf unsere Ges'),
    ]),
    ("Mittwoch, 02.09.2026", "ORF 1", [
        ('06:05', 'Wickie und die starken Männer', 'Immer Ärger mit den Möwen', 'Zeichentrick', 25, 3, 'a3', 55, 'An Bord des Wikinger-Schiffes gibt es nichts mehr zu essen. Noch hat die Mannschaft Flake nicht erre'),
        ('06:30', 'Servus Kasperl', 'Kasperl & Strolchi: Rettungsaktion Blumeninsel', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('06:55', 'Noahs Insel', 'Streit um die Insel', 'Zeichentrick', 25, 3, 'a3', 55, 'Noah ist verzweifelt: Seine Experimente mit der Steuerung der Insel durch die Energie des Feuerballs'),
        ('07:40', 'Garfield', 'Der Lasagne-Baum - Teil 5', 'Zeichentrick', 10, 3, 'a3', 55, "Die Forscher in Mama Meaney's Fabrik stellen fest, dass der Lasagne-Baum eine Fälschung ist, und die"),
        ('07:50', 'Garfield', 'Trautes Heim, Glück allein', 'Zeichentrick', 10, 3, 'a3', 55, 'Garfield und Jon stellen sich einer neuen Herausforderung. Sie nehmen an einer Realityserie teil, be'),
    ]),
    ("Mittwoch, 02.09.2026", "SRF 1", [
        ('17:30', 'Timmy Ziit - Verchäuferlis', '', 'Vorlesen', 10, 6, 'a6', 55, 'Timmy ist das freche kleine Schaf aus Shauns Herde. Jeden Tag geht er in den Kindergarten, wo er gem'),
    ]),
    ("Donnerstag, 03.09.2026", "ProSieben Maxx", [
        ('16:45', 'Dr. STONE', 'Beyond the New World', 'Anime', 25, 12, 'a10', 55, 'Senku und seine Freunde sind wieder zu Hause angekommen. Nun wollen sie Tsukasa endlich wiederbelebe'),
        ('17:10', 'Dragon Ball Super', 'Freezer und Frost! In Boshaftigkeit verbunden!', 'Anime', 25, 12, 'a10', 55, 'Als Son Gohan fast von Jimmies aus dem zweiten Universum besiegt wird, bekommt er Unterstützung von '),
        ('17:35', 'Dragon Ball Super', 'Zusammenstoß mit dem ultimativen Gegner! Zeit für die alles entscheide', 'Anime', 25, 12, 'a10', 55, 'Auf diesen Moment hat Son Goku das ganze Turnier über gewartet: Endlich kann er Jiren, den unheimlic'),
        ('18:00', 'Detektiv Conan', 'Schüsse im Stadion (1)', 'Anime', 30, 12, 'a10', 55, 'Conan, Ai und die Detective Boys gucken sich am Neujahrstag im Nationalstadion das Pokalfinale an. W'),
        ('18:30', 'One Piece', 'Der neue Samurai der Meere! - Der Sohn des berüchtigten Whitebeard!', 'Anime', 25, 12, 'a10', 55, 'Das Schiff nimmt weiterhin Kurs auf das Königreich Zou, als Ruffy eine erfreuliche Entdeckung macht.'),
        ('18:55', 'One Piece', 'Ein gefährlicher Aufstieg! - Das Abenteuer auf dem Rücken des Elefante', 'Anime', 25, 12, 'a10', 55, 'Mithilfe eines Drachens versucht die Crew weiterhin, das Königreich Zou zu erklimmen. Doch das Vorha'),
    ]),
    ("Donnerstag, 03.09.2026", "NDR", [
        ('06:00', 'Sesamstraße', '', 'Vorlesen', 20, 3, 'a3', 55, 'Ernie macht zusammen mit Bert ein paar Bewegungsübungen. Allerdings muss Bert dabei einen riesigen K'),
    ]),
    ("Donnerstag, 03.09.2026", "MDR", [
        ('12:30', 'Lilly unter den Linden', '', 'Film', 88, 6, 'a6', 55, 'Das Mädchen Lilly aus Hamburg lernt 1988 bei der Beerdigung der Mutter ihre Tante Lena aus Jena kenn'),
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Dr. Brumm macht das, was er immer macht, wenn er ein Abenteuer erleben will: Er fragt Bibi, ob sie I'),
    ]),
    ("Donnerstag, 03.09.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Dr. Brumm: Dr. Brumm geht zelten'),
    ]),
    ("Donnerstag, 03.09.2026", "HR", [
        ('06:15', 'Leo da Vinci', 'Der goldene Hirsch', 'Zeichentrick', 10, 3, 'a3', 55, 'Durch die zweite Nachricht entdecken Leo und seine Freunde, dass der Doge Lorenzo Tiepolo zwei Jahrh'),
        ('06:25', 'Leo da Vinci', 'Ein kostbares Paket', 'Zeichentrick', 15, 3, 'a3', 55, 'Nach dem Hinweis von Fabrizio begeben sich die Freunde zum "Fondaco dei Tedeschi", aber von ihrem Fr'),
    ]),
    ("Donnerstag, 03.09.2026", "arte", [
        ('04:30', 'Athleticus', 'Kite Skating', 'Zeichentrick', 40, 3, 'a3', 55, 'Im Kurzprogramm messen sich vielerlei Tiere in den klassischen Sportarten. In dieser Folge: Ein Elef'),
    ]),
    ("Donnerstag, 03.09.2026", "ORF 1", [
        ('06:05', 'Wickie und die starken Männer', 'Abenteuer in Griechenland', 'Zeichentrick', 25, 3, 'a3', 55, 'Wieder einmal gehen die Wikinger auf große Fahrt. Als sie unterwegs ein griechisches Schiff treffen,'),
        ('06:30', 'Servus Kasperl', 'Kasperl & Buffi: Ein sensationeller Freund', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('06:55', 'Noahs Insel', 'Der Neue', 'Zeichentrick', 25, 3, 'a3', 55, 'Die Atlantikströmung treibt die Insel weiter in Richtung Süden. Noahs Experimente mit dem Feuerball '),
        ('07:40', 'Garfield', 'Abenteuer Wildnis - Teil 1', 'Zeichentrick', 10, 3, 'a3', 55, 'Heute haben Garfield, Odie und Jon einen Ausflug in die Wildnis vor. Sie gehen Campen. Als wäre das '),
        ('07:50', 'Garfield', 'Abenteuer Wildnis - Teil 2', 'Zeichentrick', 10, 3, 'a3', 55, 'Garfield, Odie und Nermal finden sich in einer brenzligen Situation wieder. Denn Jon ist ohne die dr'),
    ]),
    ("Donnerstag, 03.09.2026", "SRF 1", [
        ('17:05', 'SRF Kids News', '', 'Serie', 15, 6, 'a6', 55, ''),
        ('17:20', 'SRF Kids Inside', 'IG Seifenkisten Derby Schweiz - Verrückte Fahrzeuge selber bauen', 'Vorlesen', 10, 6, 'a6', 55, '1 Verein, 3 Kids und noch mehr Storys: «SRF Kids Inside» erzählt Geschichten mitten aus dem Leben - '),
        ('17:30', 'Timmy Ziit - Mittagsschlaf', '', 'Vorlesen', 10, 6, 'a6', 55, 'Timmy ist das freche kleine Schaf aus Shauns Herde. Jeden Tag geht er in den Kindergarten, wo er gem'),
    ]),
]
