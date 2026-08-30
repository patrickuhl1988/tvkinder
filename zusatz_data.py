# -*- coding: utf-8 -*-
"""Kindersendungen der Vollprogramme.

Erzeugt von scan_kinder.py aus tv.de am 30.08.2026. Auswahl nach Kategorie,
bekannten Titeln und Beschreibung; Alterswerte heuristisch.
"""

TAGE = [
    ("Sonntag, 30.08.2026", "SAT.1", [
        ('17:00', 'Matilda', '', 'Film', 115, 6, 'a6', 55, 'Kaum zu glauben, dass solche Eltern eine solche Tochter haben: Die kleine Matilda ist ein telekineti'),
    ]),
    ("Sonntag, 30.08.2026", "WDR", [
        ('17:20', 'Wuppertal und die einzigartige Schwebebahn', '', 'Wissen', 30, 6, 'a6', 55, 'Einmal im Leben durch Wuppertal schweben! Die Wuppertaler Schwebebahn feiert ihren 125. Geburtstag -'),
    ]),
    ("Sonntag, 30.08.2026", "MDR", [
        ('15:30', 'Hans Röckle und der Teufel', '', 'Serie', 75, 6, 'a6', 55, 'Dem Puppenspieler und Erfinder Hans Röckle erscheint der Teufel und bietet ihm einen Pakt an. Röckle'),
        ('16:45', 'Das Mädchen auf dem Besenstiel', '', 'Serie', 75, 6, 'a6', 55, 'Hexenschülerin Saxana muss 300 Jahre nachsitzen und sucht nach Abwechslung. Im Zauberlexikon stößt s'),
        ('18:52', 'Unser Sandmännchen', '', 'Serie', 8, 3, 'a3', 55, 'Pitti und Moppi spielen Feuerwehr. Rasen mit dem Handwagen quer über die Gartenbeete und stoßen alle'),
    ]),
    ("Sonntag, 30.08.2026", "RBB", [
        ('11:40', 'Die Gänsemagd', '', 'Serie', 60, 6, 'a6', 55, 'Prinzessin Elisabeth ist schon seit vielen Jahren dem Prinzen Leopold versprochen. Auf den Weg zur V'),
        ('13:50', 'Der Froschkönig', '', 'Serie', 65, 6, 'a6', 55, 'Der schönen Prinzessin fällt eines Tages beim Spielen ihre Goldkugel in den Brunnen. Traurig über de'),
        ('14:55', 'Die Gänseprinzessin', '', 'Serie', 60, 6, 'a6', 55, 'Nach Motiven der Brüder Grimm erzählt das Märchen die Geschichte eines Königreiches im Ausnahmezusta'),
        ('16:55', 'König Drosselbart', '', 'Serie', 58, 6, 'a6', 55, 'Es war einmal die stolze Prinzessin Isabella von Geranien, die war schön, aber hochmütig. Als ihr Va'),
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Kallis Gute-Nacht-Geschichten: Super-Kalli'),
    ]),
    ("Sonntag, 30.08.2026", "3sat", [
        ('17:15', 'Ein Schloss am Wörthersee - Der Film', '', 'Film', 80, 6, 'a6', 55, 'Der charmante Lennie Berger hat von seinem Onkel das Schlosshotel Velden geerbt und will es auf Vord'),
    ]),
    ("Sonntag, 30.08.2026", "SRF 1", [
        ('17:10', 'Minisguard', 'Wie macht man eigentlich Glace?', 'Serie', 15, 6, 'a6', 55, 'An einem heissen Sommertag gibt es kaum etwas Besseres als eine feine Glace. Aber wie wird Glace eig'),
    ]),
    ("Montag, 31.08.2026", "ProSieben Maxx", [
        ('16:45', 'Dr. STONE', 'Last Man Standing', 'Anime', 25, 12, 'a10', 55, 'Der teuflische Ibara hat jede Person auf der Insel versteinert und denkt, er sei der einzige Überleb'),
        ('17:10', 'Dragon Ball Super', 'Ein erbitterter Kampf! Muten-Roshi gibt alles!', 'Anime', 25, 12, 'a10', 55, 'Drei Kämpfer des vierten Universums haben es auf Muten-Roshi abgesehen. Darunter auch Caway, die sog'),
        ('17:35', 'Detektiv Conan', 'Love-Story im Hauptquartier 8 - Der linke Ringfinger (2)', 'Anime', 25, 12, 'a10', 55, 'Sato übernimmt die Befragung der drei Verdächtigen, die an dem Interview mit dem verstorbenen Krimin'),
        ('18:00', 'One Piece', 'Kämpfer unter sich! - Die wütenden Monster der neuen Welt', 'Anime', 30, 12, 'a10', 55, 'De Flamingo schwört Rache an Ruffy. Gut, dass dieser auch in Zukunft auf die Hilfe seiner Verbündete'),
        ('18:30', 'One Piece', 'Die silberne Festung! - Ruffys und Bartolomeos großes Abenteuer', 'Anime', 25, 12, 'a10', 55, 'Nach einer ausgelassenen Party begibt sich Ruffy auf die Suche nach etwas Essbarem. Doch sein Hunger'),
        ('18:55', 'Detektiv Conan', 'Den Männern in Schwarz auf der Spur (2)', 'Anime', 25, 12, 'a10', 55, 'Conan findet heraus, dass Pisco einer von sieben Verdächtigen sein muss. Auf dem Boden findet er ein'),
    ]),
    ("Montag, 31.08.2026", "WDR", [
        ('06:50', 'Wissen macht Ah!', 'Im Ah!telier', 'Vorlesen', 25, 3, 'a3', 55, 'Das Studio von "Wissen macht Ah!" wird heute zum Maler-Atelier und Ralph vollbringt eine künstlerisc'),
        ('07:15', 'POV - Deine Geschichte zählt', 'Was tun, wenn keiner was sagt · Rechtsextremismus unter Jugendlichen', 'Vorlesen', 10, 3, 'a3', 55, 'Leonie (16) fühlt sich in der Schule oft ausgeschlossen. Halt findet sie in Musik, Konzerten und Onl'),
        ('07:25', 'Campsite', 'Die Klette', 'Jugendserie', 5, 3, 'a3', 55, 'Theo ist sehr verliebt in Nura und möchte am liebsten die ganze Zeit mit ihr verbringen. Lea ist das'),
        ('07:30', 'Campsite', 'Das Midsommar-Brüllen', 'Jugendserie', 10, 3, 'a3', 55, 'Theo leidet unter der Trennung von Nura und möchte so gern wieder mit ihr zusammen sein. Doch im Str'),
        ('07:40', 'Campsite', 'Lach-Dämonen', 'Jugendserie', 5, 3, 'a3', 55, 'Andrine, Lea, Thea und Max chillen auf dem Campingplatz, als sie merkwürdige Geräusche hören. Wer la'),
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
    ("Montag, 31.08.2026", "HR", [
        ('05:10', 'Schau in meine Welt', 'Sammys erste Filmrolle', 'Vorlesen', 25, 3, 'a3', 55, 'Samanta Lillia (13) hat ihre erste Rolle beim Film. Als Sängerin stand sie schon auf vielen Bühnen. '),
        ('06:25', 'Leo da Vinci', 'Der gierige Schneider', 'Zeichentrick', 10, 3, 'a3', 55, 'Bianca wird in der Medici-Bank für eine Betrügerin gehalten und bekommt keine Fiorini, dafür wird si'),
        ('06:35', 'Leo da Vinci', 'Die Ankunft in Venedig', 'Zeichentrick', 15, 3, 'a3', 55, 'Unterwegs treffen die Freunde das kleine Mädchen Maria und retten sie vor einem wütenden Stier. Sie '),
    ]),
    ("Montag, 31.08.2026", "3sat", [
        ('10:15', 'Ein Schloss am Wörthersee - Der Film', '', 'Film', 85, 6, 'a6', 55, 'Der charmante Lennie Berger hat von seinem Onkel das Schlosshotel Velden geerbt und will es auf Vord'),
    ]),
    ("Montag, 31.08.2026", "arte", [
        ('04:35', 'Athleticus', 'Gym Tonic', 'Zeichentrick', 25, 3, 'a3', 55, 'Die dritte Staffel des Kurzprogramms wirft in 30 Folgen einen humorvollen Blick auf unsere Gesellsch'),
    ]),
    ("Montag, 31.08.2026", "ORF 1", [
        ('06:05', 'Wickie und die starken Männer', 'Der Eskimoschatz', 'Zeichentrick', 25, 3, 'a3', 55, 'Nach einer langen Reise kommen die Wikinger in Grönland an und machen sich auf die Schatzsuche. Die '),
        ('06:30', 'Servus Kasperl', 'Kasperl & Co: Zwei wie Pech und Schwefel', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('06:55', 'Die Jagd nach dem Kju Wang', 'Der schwarze Gondoliere', 'Zeichentrick', 25, 3, 'a3', 55, 'Da der Herzog auf Reisen ist, erklärt er Talbot zu seinem Stellvertreter. Zunächst profitiert Yagor '),
        ('07:35', 'Vegesaurier', 'Flugübungen', 'Zeichentrick', 5, 3, 'a3', 55, 'Das Trikarrotops-Mädchen Ginger und die Baby-Erbs-Rexe Minzi, Wasabi und Split lernen einen kleinen '),
        ('07:40', 'Dragons - Die Wächter von Berk', 'Drachentausch', 'Zeichentrick', 20, 3, 'a3', 55, 'Dass sich Rotzbakke und Astrid nicht leiden können, weiß jeder auf Berk. Als aus heiterem Himmel abe'),
    ]),
    ("Montag, 31.08.2026", "SRF 1", [
        ('17:30', 'Timmy Ziit - Pöschtler', '', 'Vorlesen', 10, 6, 'a6', 55, ''),
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
]
