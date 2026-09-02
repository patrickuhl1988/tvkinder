# -*- coding: utf-8 -*-
"""Kindersendungen der Vollprogramme.

Erzeugt von scan_kinder.py aus tv.de am 02.09.2026. Auswahl nach Kategorie,
bekannten Titeln und Beschreibung; Alterswerte heuristisch.
"""

TAGE = [
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
    ("Mittwoch, 02.09.2026", "BR", [
        ('23:50', 'Böse Spiele - Rimini Sparta', '', 'Serie', 25, 10, 'a10', 55, 'Der Tod der Mutter bringt zwei Brüder noch einmal kurz zusammen - im leer stehenden Elternhaus, wo a'),
    ]),
    ("Mittwoch, 02.09.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Die Erdmännchen Jan und Henry sind beunruhigt. Hat sich da etwa ein Krokodil in ihre Küche geschlich'),
    ]),
    ("Mittwoch, 02.09.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Jan & Henry: Das weinende Krokodil'),
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
        ('04:38', 'Athleticus', 'Kite Skating', 'Zeichentrick', 32, 3, 'a3', 55, 'Im Kurzprogramm messen sich vielerlei Tiere in den klassischen Sportarten. In dieser Folge: Ein Elef'),
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
    ("Freitag, 04.09.2026", "ProSieben Maxx", [
        ('16:45', 'Yashahime', 'Inuyasha seither', 'Anime', 25, 12, 'a10', 55, 'Die Halbdämonen-Prinzessin Towa Higurashi wird festgenommen und verhört. Da sie mit ihrem Wissen die'),
        ('17:10', 'Dragon Ball Super', 'Goku lässt die Götter bangen! Der neue Instinkt des Auferwachten!', 'Anime', 25, 12, 'a10', 55, 'Jiren gelingt es, die Genkidama-Attacke auf Son Goku zurückzuwerfen. Nach dem heftigen Einschlag ist'),
        ('17:35', 'Dragon Ball Super', 'Kampf in einer anderen Dimension! Mit Hit gegen Jiren!', 'Anime', 25, 12, 'a10', 55, 'Nachdem Son Goku seine neuen Kräfte wieder verloren hat, nimmt es Hit mit Jiren auf. Doch auch ihm g'),
        ('18:00', 'Detektiv Conan', 'Schüsse im Stadion (2)', 'Anime', 25, 12, 'a10', 55, 'Der Erpresser erhöht seine Forderung um eine weitere halbe Millionen, die zu Spielende bei Block 18 '),
        ('18:25', 'One Piece', 'Ein Kampf beginnt - Ruffy gegen den Mink-Stamm', 'Anime', 30, 12, 'a10', 55, 'Während Ruffy sich auf der Insel umsieht, wird der Rest der Truppe von außergewöhnlichen Mensch-Tier'),
        ('18:55', 'One Piece', 'Galchu! - Die Wiedervereinigung der Strohhüte', 'Anime', 25, 12, 'a10', 55, 'Die Insel schwebt in ständiger Gefahr zu überfluten, da der Elefant sich regelmäßig mit Wasser bespr'),
        ('20:15', 'Naruto Shippuden The Movie: Bonds', '', 'Zeichentrick', 105, 12, 'a10', 55, 'Eine Gruppe gefährlicher Himmel-Shinobi ist auf dem Weg ins Feuer-Reich, um das kleine Dorf Konoha v'),
        ('22:00', 'Gachiakuta', 'Der Abschluss', 'Anime', 30, 12, 'a10', 55, 'Rudo befindet sich noch immer im Kampf mit Jabber. Er versucht, die Auseinandersetzung an einen ande'),
        ('22:30', 'Gachiakuta', 'Ein Schritt nach vorn', 'Anime', 30, 12, 'a10', 55, 'Rudo hadert mit den Folgen des Kampfes gegen Jabber. Zu seiner Erleichterung erfährt er jedoch, dass'),
        ('23:00', 'Gachiakuta', 'Die Stadt des Graffiti', 'Anime', 25, 12, 'a10', 55, 'Der Putztrupp stellt eine Einheit für die Reise in die Verbotene Zone zusammen. Zur Vorbereitung beg'),
        ('23:50', 'Frieren - Nach dem Ende der Reise', 'Die Todesbotin Frieren', 'Anime', 25, 12, 'a10', 55, 'Frieren sitzt im Gefängnis fest. Der Dämon Draht sucht sie in ihrer Zelle auf und möchte sie umbring'),
    ]),
    ("Freitag, 04.09.2026", "NDR", [
        ('06:00', 'Sesamstraße', '', 'Vorlesen', 20, 3, 'a3', 55, 'Ernie ist Rapunzel. Prinz Bert wartet sehnsüchtig darauf, in den Turm hinaufzuklettern. Aber Rapunze'),
    ]),
    ("Freitag, 04.09.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Internationale Kinderlieder Heijanganga Eine Familie erlebt in den Weiten der amerikanischen Prärie '),
    ]),
    ("Freitag, 04.09.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Internationale Kinderlieder: Atte katte Nuwa'),
    ]),
    ("Freitag, 04.09.2026", "HR", [
        ('06:15', 'Leo da Vinci', 'Ein verdächtiger Brief', 'Zeichentrick', 10, 3, 'a3', 55, 'Leo, Bianca, Lisa und Lollo wenden sich an Alvise Tiepolo, in der Hoffnung, dass er Neuigkeiten über'),
        ('06:25', 'Leo da Vinci', 'Das Mädchen und der Stier', 'Zeichentrick', 15, 3, 'a3', 55, 'Auf dem Festland angekommen, erfahren Bianca, Lisa, Lollo und Leo von ihrer kleinen Freundin Maria, '),
    ]),
    ("Freitag, 04.09.2026", "arte", [
        ('04:40', 'Athleticus', 'Roller Show', 'Zeichentrick', 30, 3, 'a3', 55, 'Eine Robbe gibt bei einer Akrobatikvorführung ihre draufgängerischen Kunststücke zum Besten. Nilpfer'),
    ]),
    ("Freitag, 04.09.2026", "ORF 1", [
        ('06:00', 'ZIB KiDS', '', 'Serie', 10, 3, 'a3', 55, ''),
        ('06:10', 'Wickie und die starken Männer', 'Die Olympiade der Wikinger', 'Zeichentrick', 25, 3, 'a3', 55, 'Die Wikinger sitzen noch immer mit ihren erbeuteten Schätzen im Burggraben des Griechen-Königs fest.'),
        ('06:35', 'Servus Kasperl', 'Kasperl & Leopold: Das große Schnarchen', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('07:00', 'Noahs Insel', 'Sascha hier, Sascha dort', 'Zeichentrick', 25, 3, 'a3', 55, 'Noahs Insel läuft vor der afrikanischen Küste auf Grund. Während der Eisbär grübelt, wie er das Eila'),
        ('07:45', 'Mister Paper', 'Mister Paper verläuft sich', 'Zeichentrick', 5, 3, 'a3', 55, 'Mister Paper macht einen ausgiebigen Spaziergang mit seiner Katze. Unterwegs dekoriert er die Landsc'),
        ('07:50', 'ZIB KiDS', '', 'Serie', 10, 3, 'a3', 55, ''),
    ]),
    ("Freitag, 04.09.2026", "SRF 1", [
        ('17:30', 'Timmy Ziit - Baschtle', '', 'Vorlesen', 10, 6, 'a6', 55, 'Timmy ist das freche kleine Schaf aus Shauns Herde. Jeden Tag geht er in den Kindergarten, wo er gem'),
    ]),
]
