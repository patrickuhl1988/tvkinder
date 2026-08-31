# -*- coding: utf-8 -*-
"""Kindersendungen der Vollprogramme.

Erzeugt von scan_kinder.py aus tv.de am 31.08.2026. Auswahl nach Kategorie,
bekannten Titeln und Beschreibung; Alterswerte heuristisch.
"""

TAGE = [
    ("Montag, 31.08.2026", "ProSieben Maxx", [
        ('16:45', 'Dr. STONE', 'Last Man Standing', 'Anime', 25, 12, 'a10', 55, 'Der teuflische Ibara hat jede Person auf der Insel versteinert und denkt, er sei der einzige Überleb'),
        ('17:10', 'Dragon Ball Super', 'Ein erbitterter Kampf! Muten-Roshi gibt alles!', 'Anime', 25, 12, 'a10', 55, 'Drei Kämpfer des vierten Universums haben es auf Muten-Roshi abgesehen. Darunter auch Caway, die sog'),
        ('17:35', 'Detektiv Conan', 'Love-Story im Hauptquartier 8 - Der linke Ringfinger (2)', 'Anime', 25, 12, 'a10', 55, 'Sato übernimmt die Befragung der drei Verdächtigen, die an dem Interview mit dem verstorbenen Krimin'),
        ('18:00', 'One Piece', 'Kämpfer unter sich! - Die wütenden Monster der neuen Welt', 'Anime', 30, 12, 'a10', 55, 'De Flamingo schwört Rache an Ruffy. Gut, dass dieser auch in Zukunft auf die Hilfe seiner Verbündete'),
        ('18:30', 'One Piece', 'Die silberne Festung! - Ruffys und Bartolomeos großes Abenteuer', 'Anime', 25, 12, 'a10', 55, 'Nach einer ausgelassenen Party begibt sich Ruffy auf die Suche nach etwas Essbarem. Doch sein Hunger'),
        ('18:55', 'Detektiv Conan', 'Den Männern in Schwarz auf der Spur (2)', 'Anime', 25, 12, 'a10', 55, 'Conan findet heraus, dass Pisco einer von sieben Verdächtigen sein muss. Auf dem Boden findet er ein'),
    ]),
    ("Montag, 31.08.2026", "SWR", [
        ('12:55', 'Familie für Fortgeschrittene', '', 'Serie', 90, 6, 'a6', 55, 'Der Berliner Lehrer Oliver zieht mit Tochter Holly in die bayerische Provinz zu seiner neuen Lebensp'),
    ]),
    ("Montag, 31.08.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Oh, was für ein Lampenfieber! Denn heute steht für die Turnschuhe ein großes Konzert an und Wetz dar'),
    ]),
    ("Montag, 31.08.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Geschichten aus dem Schuhregal: Wer gibt den Takt an?'),
    ]),
    ("Montag, 31.08.2026", "SRF 1", [
        ('17:30', 'Timmy Ziit - Pöschtler', '', 'Vorlesen', 10, 6, 'a6', 55, 'Timmy ist das freche kleine Schaf aus Shauns Herde. Jeden Tag geht er in den Kindergarten, wo er gem'),
    ]),
    ("Dienstag, 01.09.2026", "ZDF", [
        ('20:15', 'besseresser: Die Tricks in Bärchenwurst, Pizzateig & Co.', 'Sebastian Lege deckt auf', 'Serie', 45, 10, 'a10', 55, 'Ob überraschende Zusatzstoffe, cleveres Kindermarketing oder irreführendes Verpackungsdesign: Sebast'),
    ]),
    ("Dienstag, 01.09.2026", "RTLzwei", [
        ('18:05', 'Hartz und herzlich - Tag für Tag Benz-Baracken', 'Pommes-Party', 'Serie', 60, 6, 'a6', 55, 'Wegen häufiger Kopfschmerzen und anderer Beschwerden hat Andy beim Arzt abchecken lassen, ob er viel'),
    ]),
    ("Dienstag, 01.09.2026", "ProSieben Maxx", [
        ('05:10', 'One Piece', 'Kein Entkommen - Fujitoras unbarmherzige Verfolgungsjagd!', 'Anime', 20, 12, 'a10', 55, 'Fujitora hat es auf die Piratenflotte abgesehen, die am Hafen von Dress Rosa ankert. Doch die Einwoh'),
        ('16:45', 'Dr. STONE', 'First Dream', 'Anime', 25, 12, 'a10', 55, 'Senku hat den Kampf gegen Ibara gewonnen und kann seine Freunde nun nach und nach wiederbeleben. Zue'),
        ('17:10', 'Dragon Ball Super', 'Gefährliche Reflexion! Attacke des unsichtbaren Angreifers!', 'Anime', 25, 12, 'a10', 55, 'Noch verbleiben 35 Minuten, um das Turnier der Universen zu gewinnen. Mit der schwindenden Zeit nimm'),
        ('17:35', 'Detektiv Conan', 'Der Teufel im Fernsehstudio (1)', 'Anime', 25, 12, 'a10', 55, 'Yoko lädt die Detective Boys und Professor Agasa in ein Fernsehstudio ein. Dort treffen die Kinder a'),
        ('18:00', 'One Piece', 'Tief in der Mine - Ruffy gegen den menschlichen Zug!', 'Anime', 25, 12, 'a10', 55, 'Bartolomeo und Ruffy sitzen in den Schächten der Silver Mine fest und leisten damit ehemaligen Pirat'),
        ('18:25', 'One Piece', 'In der Hitze des Gefechts - Law und Zorro eilen zur Hilfe!', 'Anime', 30, 12, 'a10', 55, 'Ruffy, Bartolomeo und Desire befinden sich weiterhin unter Tage, als sie von Avelon angegriffen werd'),
        ('18:55', 'Detektiv Conan', 'Den Männern in Schwarz auf der Spur (3)', 'Anime', 30, 12, 'a10', 55, 'Die vorübergehend wieder zu ihrer eigentlichen Größe zurückgekehrte Sherry kann durch den Kamin aufs'),
    ]),
    ("Dienstag, 01.09.2026", "WDR", [
        ('07:30', 'Campsite', 'Sehnsucht', 'Jugendserie', 10, 3, 'a3', 55, 'So ein Mist: Weil Theo immer nur mit Nura zusammen war, verbringt sein bester Freund Sebbe seine Zei'),
        ('07:40', 'Campsite', 'Leos Liste', 'Jugendserie', 5, 3, 'a3', 55, 'Leo wird von seinen Freunden dabei überrascht, dass er Lea malt. Wohl oder übel muss er zugeben, das'),
        ('07:45', 'Campsite', 'Die Abschiedsparty', 'Jugendserie', 10, 3, 'a3', 55, 'Lea ist entsetzt, als sie von Theo erfährt, dass sie am nächsten Tag schon abreisen. Die Ferien sind'),
        ('07:55', 'Das Camp in der Wildnis', 'Partylaune statt Abschiedstränen', 'Vorlesen', 25, 3, 'a3', 55, 'In der letzten Woche des Schuljahres wird das Camp auf den Kopf gestellt. An allen Ecken wird gestri'),
        ('08:20', 'Das Camp in der Wildnis', 'Am Ende der Welt', 'Vorlesen', 25, 6, 'a6', 55, 'Nachdem die Türen des Wildnis-Camps verschlossen sind, geht es für die 32 Jugendlichen vor ihrer Rüc'),
    ]),
    ("Dienstag, 01.09.2026", "NDR", [
        ('06:00', 'Sesamstraße', '', 'Vorlesen', 20, 3, 'a3', 55, 'Wie bekommt Elmo nur alle seine neuen Spielsachen nach oben in sein Spielehaus? Elin, Wolle und Pfer'),
    ]),
    ("Dienstag, 01.09.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Der Löwe auf meiner Schmusedecke hat ein Problem: Er kann nicht mehr brüllen! Werden seine Freunde e'),
    ]),
    ("Dienstag, 01.09.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Meine Schmusedecke: Der Löwe'),
    ]),
    ("Dienstag, 01.09.2026", "HR", [
        ('06:15', 'Leo da Vinci', 'Die Karnevalskostüme', 'Zeichentrick', 10, 3, 'a3', 55, 'Im Glauben, Venedig ohne ihre Verfolger erreicht zu haben, schneidert Leo für alle Karnevalskostüme.'),
        ('06:25', 'Leo da Vinci', 'Durch die Gassen von Venedig', 'Zeichentrick', 15, 3, 'a3', 55, 'Die Piraten beschließen zum Palazzo di Tiepolo zurückzukehren, um nach dem zweiten Teil der Nachrich'),
    ]),
    ("Dienstag, 01.09.2026", "arte", [
        ('04:40', 'Athleticus', 'Spiele im Park', 'Zeichentrick', 20, 3, 'a3', 55, 'Die dritte Staffel des Kurzprogramms wirft in 30 Folgen einen humorvollen Blick auf unsere Gesellsch'),
    ]),
    ("Dienstag, 01.09.2026", "ORF 1", [
        ('06:05', 'Wickie und die starken Männer', 'Der kleine Wal', 'Zeichentrick', 25, 3, 'a3', 55, 'Zum ersten Mal treten die Wikinger eine Heimreise ohne Beute an. Die herrlichen Schätze, die sie in '),
        ('06:30', 'Servus Kasperl', 'Kasperl & Pezi: Ein Abenteuer mit Dagobert', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('06:55', 'Noahs Insel', 'Ein neues Zuhause', 'Zeichentrick', 25, 3, 'a3', 55, 'Ein aus dem Weltraum herabstürzender Feuerball trennt ein Stück Küste vom Festland ab. Als schwimmen'),
        ('07:30', 'Vegesaurier', 'Keine Angst!', 'Zeichentrick', 5, 3, 'a3', 55, 'Die Brokkolisaurier gehören zu den allergrößten Vegesauriern der späten Knusperzeit. Die sanften Rie'),
        ('07:35', 'Galapagos X', 'Der Glitzer-Vulkan', 'Zeichentrick', 15, 3, 'a3', 55, 'Rae ist völlig aus dem Häuschen, denn es regnet Glitzer vom Himmel! Doch das Galapagos X-Team muss s'),
    ]),
    ("Dienstag, 01.09.2026", "SRF 1", [
        ('17:30', 'Timmy Ziit - Baby', '', 'Vorlesen', 10, 6, 'a6', 55, ''),
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
        ('04:35', 'Athleticus', 'Kellner-Wettlauf', 'Zeichentrick', 30, 3, 'a3', 55, 'Die dritte Staffel des Kurzprogramms wirft in 30 neuen Folgen einen humorvollen Blick auf unsere Ges'),
    ]),
    ("Mittwoch, 02.09.2026", "ORF 1", [
        ('06:05', 'Wickie und die starken Männer', 'Immer Ärger mit den Möwen', 'Zeichentrick', 25, 3, 'a3', 55, 'An Bord des Wikinger-Schiffes gibt es nichts mehr zu essen. Noch hat die Mannschaft Flake nicht erre'),
        ('06:30', 'Servus Kasperl', 'Kasperl & Strolchi: Rettungsaktion Blumeninsel', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('06:55', 'Noahs Insel', 'Streit um die Insel', 'Zeichentrick', 25, 3, 'a3', 55, 'Noah ist verzweifelt: Seine Experimente mit der Steuerung der Insel durch die Energie des Feuerballs'),
        ('07:40', 'Garfield', 'Der Lasagne-Baum - Teil 5', 'Zeichentrick', 10, 3, 'a3', 55, "Die Forscher in Mama Meaney's Fabrik stellen fest, dass der Lasagne-Baum eine Fälschung ist, und die"),
        ('07:50', 'Garfield', 'Trautes Heim, Glück allein', 'Zeichentrick', 10, 3, 'a3', 55, 'Garfield und Jon stellen sich einer neuen Herausforderung. Sie nehmen an einer Realityserie teil, be'),
    ]),
    ("Mittwoch, 02.09.2026", "SRF 1", [
        ('17:30', 'Timmy Ziit - Verchäuferlis', '', 'Vorlesen', 10, 6, 'a6', 55, ''),
    ]),
]
