# -*- coding: utf-8 -*-
"""Kindersendungen der Vollprogramme.

Erzeugt von scan_kinder.py aus tv.de am 13.08.2026. Auswahl nach Kategorie,
bekannten Titeln und Beschreibung; Alterswerte heuristisch.
"""

TAGE = [
    ("Donnerstag, 13.08.2026", "ProSieben Maxx", [
        ('16:40', 'Dr. STONE', 'Das Licht der Hoffnung und Verzweiflung', 'Anime', 25, 12, 'a10', 55, 'Die Crew der Perseus kommt an der Schatzinsel an. Senku, Soyuz, Kohaku und Gen gehen an Land, um das'),
        ('17:05', 'Dragon Ball Super', 'Der zehnte Kämpfer bist du! Goku besucht Freezer!', 'Anime', 25, 12, 'a10', 55, 'Son Goku will Freezer bitten, als Ersatz für Boo mit Team Erde am Turnier der Universen teilzunehmen'),
        ('17:30', 'Detektiv Conan', 'Drei Tage mit Hattori Heiji (1)', 'Anime', 30, 12, 'a10', 55, 'Conan und die anderen sind auf einem Kirschblütenfest. Der junge Detektiv hat Heiji dorthin bestellt'),
        ('18:00', 'One Piece', 'Die Klinge des eisernen Willens - Der Gamma Knife Gegenangriff!', 'Anime', 25, 12, 'a10', 55, 'De Flamingo unterbreitet Law ein Angebot: Wenn dieser ihm mit Hilfe seiner Teufelskräfte Unsterblich'),
        ('18:25', 'One Piece', 'Zusammenprall der Haki! - Ruffy gegen De Flamingo', 'Anime', 25, 12, 'a10', 55, 'Laws Angriff setzt De Flamingo ordentlich zu. Der Samurai aber verfügt über außergewöhnliche Selbsth'),
        ('18:50', 'Detektiv Conan', 'Der Serienmörder von Osaka (2)', 'Anime', 30, 12, 'a10', 55, 'Die Todesursache von Sumie Okazaki steht fest: Strangulation mit einem Seil. Conan, Hejii und Yusuke'),
    ]),
    ("Donnerstag, 13.08.2026", "WDR", [
        ('07:55', 'Das Camp in der Wildnis', 'Krise im Kajak', 'Vorlesen', 25, 3, 'a3', 55, 'Emilia ergründet auf der Huskyfarm das Wesen ihres Patenhundes Skare und sie darf das erste Mal eine'),
    ]),
    ("Donnerstag, 13.08.2026", "NDR", [
        ('07:40', 'Die Pfefferkörner', 'Der Einbruch', 'Serie', 35, 10, 'a10', 55, 'Ein Nachbar bittet Mira, eine wertvolle Skulptur zu verwahren, während er für einen Tag verreist ist'),
    ]),
    ("Donnerstag, 13.08.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Dr. Brumm macht das, was er immer macht, wenn Pottwal sich die Flossen vertreten will: Er radelt mit'),
    ]),
    ("Donnerstag, 13.08.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Dr. Brumm: Dr. Brumm will helfen'),
    ]),
    ("Donnerstag, 13.08.2026", "SRF 1", [
        ('17:45', 'Pompon der kleine Bär', 'Es Waldmonschter', 'Vorlesen', 15, 6, 'a6', 55, 'Pompon und Rita auf Spuren des Waldmonsters Zerbidul, das letztlich doch keins ist.'),
    ]),
    ("Freitag, 14.08.2026", "ProSieben Maxx", [
        ('16:40', 'Dr. STONE', 'Das Ass im Ärmel auf dem Schiff der Wissenschaft', 'Anime', 30, 12, 'a10', 55, 'Die Besatzung der Perseus wurde versteinert. Senku, Soyuz, Kohaku und Gen, die sich auf der Schatzin'),
        ('17:10', 'Dragon Ball Super', 'Die Auferstehung des bösen Imperators! Die rätselhafen Attentäter!', 'Anime', 25, 12, 'a10', 55, 'Nachdem Quitela, der Gott der Zerstörung aus dem vierten Universum, von Freezers geplanter Wiederbel'),
        ('17:35', 'Detektiv Conan', 'Drei Tage mit Hattori Heiji (2)', 'Anime', 25, 12, 'a10', 55, 'Kogoro ist überzeugt, das Rätsel um die verschwundene Frauenleiche im Tempel gelöst zu haben. Doch C'),
        ('18:00', 'One Piece', 'Unangreifbar! - Trebols schockierendes Geheimnis', 'Anime', 30, 12, 'a10', 55, 'Mit seiner Klebeschleuder gelingt es Trébol, Ruffy lahmzulegen. Um De Flamingos Sieg zu garantieren,'),
        ('18:30', 'One Piece', 'Der Ärger bricht aus - Ich werde alles auf mich nehmen!', 'Anime', 25, 12, 'a10', 55, 'Ruffy übergibt Law an seine Verbündeten, doch der lässt sich nicht auf den Handel ein. Außerdem wird'),
        ('18:55', 'Detektiv Conan', 'Im falschen Film', 'Anime', 25, 12, 'a10', 55, 'Conan und die Detective Boys warten auf Kogoro und dessen Tochter Ran. Sie planen gemeinsam ein neue'),
    ]),
    ("Freitag, 14.08.2026", "WDR", [
        ('07:25', 'Campsite', 'Ich kann nicht schwimmen', 'Jugendserie', 5, 3, 'a3', 55, 'Silje freut sich über ein neues Schlauchboot, das sie von ihrem Vater geschenkt bekommen hat. Begeis'),
        ('07:30', 'Campsite', 'Ein zu heißer Sommertag', 'Jugendserie', 10, 3, 'a3', 55, 'Ohne ihre Eltern zu fragen, lädt Andrine Nura, Sebbe, Theodor und Ronja zu einem Bootsausflug ein. A'),
        ('07:40', 'Campsite', 'Silje in der Patsche', 'Jugendserie', 10, 3, 'a3', 55, 'Der Influencer Kattekryp kommt auf den Campingplatz und Silje prahlt damit, dass sie eng befreundet '),
    ]),
    ("Freitag, 14.08.2026", "NDR", [
        ('06:00', 'Sesamstraße', '', 'Vorlesen', 20, 3, 'a3', 55, 'Bert will mithilfe eines Ventilators Windkraft erklären. Aber als Ernie den Ventilator auf die höchs'),
        ('06:20', 'Grüße vom Mars', '', 'Film', 80, 3, 'a3', 55, 'Tom ist zehn und anders als die anderen Kinder. Er mag keine Veränderungen, keine Dinge, die rot sin'),
    ]),
    ("Freitag, 14.08.2026", "BR", [
        ('20:15', 'Hubert ohne Staller', 'Pony am Stock', 'Serie', 45, 10, 'a10', 55, 'Riedls Dienstfahrrad wurde gestohlen. Der Sohn des Gestütbesitzers Georg Dausinger wurde von Riedls '),
    ]),
    ("Freitag, 14.08.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Ähnlich wie beim bekannten "Drei Chinesen mit nem Kontrabass"-Song, wird beim Kitzelkanon mit Vokale'),
    ]),
    ("Freitag, 14.08.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Liedergeschichten: Kitzelkanon'),
    ]),
    ("Freitag, 14.08.2026", "HR", [
        ('06:20', 'Leo da Vinci', 'Die zwei Bären', 'Zeichentrick', 10, 3, 'a3', 55, 'Leo und seinen Freunden gelingt es, ihr Gefährt zu verstecken, bevor die Gauner um Jack und Robert e'),
        ('06:30', 'Leo da Vinci', 'Lisas Entführung', 'Zeichentrick', 15, 3, 'a3', 55, 'Die beiden gerissenen Kaufleute Jack und Robert überwältigen Lisa in der Annahme, Bianca de Medici v'),
        ('07:00', 'Young Reporter', 'Zwischen Wald, Wahl und Wirklichkeit\nWas Schülerinnen und Schüler der ', 'Wissen', 15, 3, 'a3', 55, 'Wie blicken Jugendliche auf die großen Fragen unserer Zeit? Schülerinnen und Schüler der Dreieichsch'),
    ]),
    ("Freitag, 14.08.2026", "arte", [
        ('04:05', 'Verdammte Katze!', 'Großer Bruder', 'Zeichentrick', 5, 3, 'a3', 55, 'Stéphane passt auf das Nachbarskätzchen Grisbi auf - niedlich, aber leider ein Problem. Denn Moustiq'),
    ]),
    ("Freitag, 14.08.2026", "ORF 1", [
        ('06:00', 'ZIB KiDS', '', 'Serie', 10, 3, 'a3', 55, ''),
        ('06:10', 'Wickie und die starken Männer', 'Nochmals davongekommen', 'Zeichentrick', 25, 3, 'a3', 55, 'Wickie tritt als Küchenjunge in die Dienste der Franken. Die Vorbereitungen für das große Fest sind '),
        ('06:35', 'Servus Kasperl', 'Kasperl & Pezi: Räuber in der Märchenstadt', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('07:00', 'Die Jagd nach dem Kju Wang', 'Ardelias neue Leidenschaft', 'Zeichentrick', 25, 3, 'a3', 55, 'Graf Yagor gelingt es, seine Nichte Alma unter einem Vorwand in Cirillos Palast einzuschleusen. Arde'),
        ('07:40', 'Galapagos X', 'Das perfekte Spielzeug', 'Zeichentrick', 5, 3, 'a3', 55, 'Die Welt wird von nicht recycelbaren Einweg-Spielsachen überflutet, sodass es beinahe kein Durchkomm'),
        ('07:45', 'Garfield', 'Die Glitzer-Schlucht - Teil 1', 'Zeichentrick', 15, 3, 'a3', 55, 'Garfield hat eine Rolle in einem Western Film! Er spielt den Hilfssheriff von Jon, der den Hauptsher'),
        ('08:00', 'ZIB KiDS', '', 'Serie', 15, 6, 'a6', 55, ''),
    ]),
    ("Freitag, 14.08.2026", "SRF 1", [
        ('17:45', 'Pompon der kleine Bär', 'Es Geburtstagsgheimnis', 'Vorlesen', 15, 6, 'a6', 55, 'Pompon macht seinem Papa eine Überraschung in einer Kiste, die dieser prompt findet. Mit List und Ri'),
    ]),
    ("Samstag, 15.08.2026", "ARD", [
        ('05:30', 'Arthur und die Freunde der Tafelrunde', 'Der Umkehrtrunk', 'Zeichentrick', 10, 3, 'a3', 55, 'König Uther empfängt den Gesandten des Königs von Orkanien, um den Frieden zu feiern. Doch das Banke'),
        ('05:40', 'Arthur und die Freunde der Tafelrunde', 'Das Monster auf Camelot', 'Zeichentrick', 15, 3, 'a3', 55, 'Normalerweise ist Guineveres Werwolfkatze Migarou ein liebes Tier. Doch an diesem Morgen verhält sie'),
        ('05:55', 'HobbyMania - Tausch mit mir dein Hobby!', 'Gardetanz vs. Kegeln', 'Vorlesen', 25, 3, 'a3', 55, 'Elisabeth macht ordentlich Ballett: Sie hüpft und springt zur Musik, wirbelt dabei übers Parkett. Di'),
        ('07:05', 'Shaun das Schaf', 'Abgehoben', 'Zeichentrick', 10, 3, 'a3', 55, 'Ein Heißluftballon auf der Weide - das weckt die Neugier der Schafe! Im Nu entern sie den Korb. Als '),
        ('07:15', 'Anna im Land der tausend Seen', 'Die Riesen des Waldes', 'Vorlesen', 25, 3, 'a3', 55, 'Anna erfährt von ihrem Rangerkollegen Thomas, dass der größte Landschaftsgärtner Deutschlands, der W'),
        ('07:40', 'Pia und die Haustiere', 'Ein Tag in der Reptilienauffangstation', 'Vorlesen', 15, 3, 'a3', 55, 'Die Auffangstation für Reptilien in München ist Deutschlands größtes Tierheim für exotische Haustier'),
        ('07:55', 'Checker Tobi', 'Der Ich-Check', 'Wissen', 25, 3, 'a3', 55, 'Wir Menschen sind alle ziemlich unterschiedlich. Wir unterscheiden uns im Aussehen oder im Charakter'),
        ('08:20', 'Wissen macht Ah!', 'Dangerzone', 'Vorlesen', 25, 6, 'a6', 55, 'Sie fürchten weder Tod noch Teufel - Clarissa und Ralph füllen die heutige Sendung mit halsbrecheris'),
        ('08:45', 'POV - Deine Geschichte zählt', 'Musik machen - Nur was für Reiche?', 'Vorlesen', 10, 6, 'a6', 55, 'José spielt Posaune in einem Orchester in Dresden-Prohlis - der Unterricht ist kostenlos, damit alle'),
        ('08:55', 'Die Pfefferkörner', 'Miese Nummer', 'Serie', 25, 10, 'a10', 55, 'Katastrophe! Das teure Rad, das sich Jet schon so lange wünscht und das sie zu ihrem Geburtstag am n'),
        ('09:20', 'Die Pfefferkörner', 'Helden lügen nicht', 'Serie', 30, 10, 'a10', 55, 'Rafa soll ein Referat über Alltagshelden halten - und hat sich für seinen Vater entschieden. Der Pol'),
    ]),
    ("Samstag, 15.08.2026", "ZDF", [
        ('06:20', 'Dylans Spielkiste', 'Flughafenmitarbeiter', 'Zeichentrick', 10, 3, 'a3', 55, "Heute ist Dylan Flughafenmitarbeiter. Doch statt Routine gibt's Chaos: Ozzy hat kein Ticket, ein ver"),
        ('06:30', 'Dylans Spielkiste', 'Detektiv', 'Zeichentrick', 10, 3, 'a3', 55, 'Dylan ist Detektiv und sucht Bitsys verschwundenen Pinsel. Er entdeckt Farbspritzer, Fußabdrücke und'),
        ('06:40', 'Meine Freundin Conni', 'Conni spielt Fußball', 'Zeichentrick', 15, 3, 'a3', 55, 'Mit Papa und Onkel Günther im Garten zu bolzen, macht Spaß, aber richtig dribbeln und kicken zu könn'),
        ('06:55', 'Die Biene Maja', 'Die Sonnenfinsternis', 'Zeichentrick', 10, 3, 'a3', 55, 'Maja erlebt eine totale Sonnenfinsternis. Bei der unerwarteten Dunkelheit verirren sich drei kleine '),
        ('07:05', 'Bibi Blocksberg', 'Wo ist Kartoffelbrei?', 'Zeichentrick', 25, 3, 'a3', 55, 'Bibi war unartig und bekommt deshalb drei Tage Hexverbot. Das ist eine schwere Strafe für sie. Vater'),
        ('07:30', 'Bibi Blocksberg', 'Das Wettfliegen', 'Zeichentrick', 30, 3, 'a3', 55, 'Es gibt einen großen Flugwettbewerb in Neustadt. Für Bibi ist es selbstverständlich, dass sie daran '),
        ('08:00', 'Robin Hood - Schlitzohr von Sherwood', 'Der Fallensteller', 'Zeichentrick', 10, 6, 'a6', 55, 'Tuck gerät im Wald in eine Falle. Er sitzt im Käfig fest, und Robin schafft es nicht, ihn zu befreie'),
        ('08:10', 'Robin Hood - Schlitzohr von Sherwood', 'Sheriff Robin', 'Zeichentrick', 15, 6, 'a6', 55, 'Der Sheriff hat sich verletzt, und König Richard bittet Robin, ihn zu vertreten. Natürlich passt das'),
    ]),
    ("Samstag, 15.08.2026", "ProSieben Maxx", [
        ('04:15', 'Frieren - Nach dem Ende der Reise', 'Es hätte nicht unbedingt Magie sein müssen ...', 'Anime', 25, 12, 'a10', 55, 'Frieren unterrichtet Fern in den Grundlagen der Magie. Zeitgleich versucht sie, das Buch zu entschlü'),
        ('04:40', 'Frieren - Nach dem Ende der Reise', 'Tötungszauber', 'Anime', 25, 12, 'a10', 55, 'Fern und Frieren kommen in der Handelsstadt Warm an. Die Frauen wollen dort ihre Vorräte für die wei'),
        ('05:05', 'One Piece', 'Tödlicher Sternenstaub! - Diamantes Sturm der bösartigen Angriffe', 'Anime', 20, 12, 'a10', 55, 'Auf dem Königsplateau spitzt sich der Kampf zwischen Kyros und Diamante immer weiter zu. Trotz seine'),
        ('05:25', 'One Piece', "Trueno Bastardo - Kyros' ultimative Attacke!", 'Anime', 35, 12, 'a10', 55, "Diamante verliert angesichts Kyros' Gleichgültigkeit die Fassung. Blutüberströmt nimmt der Krieger d"),
        ('06:00', 'Eyeshield 21', 'Das teuflische Sportfest der Deimon-Oberschule', 'Anime', 25, 12, 'a10', 55, 'An der Deimon-Oberschule findet das traditionelle Sportfest statt. Die Mitglieder der Devil Bats lan'),
        ('06:25', 'Eyeshield 21', 'Sena ist ein Sprinter', 'Anime', 25, 12, 'a10', 55, 'Es bleiben nur noch fünf Tage bis zum nächsten Spiel der Devil Bats. Die Konkurrenz ist sehr stark, '),
        ('06:50', 'Eyeshield 21', 'Das Versprechen der Drei', 'Anime', 25, 12, 'a10', 55, 'Riku taucht beim Training der Devil Bats und will herausfinden, wer sich hinter Eyeshield wirklich v'),
        ('07:15', 'Eyeshield 21', 'Beweis wahrer Schnelligkeit', 'Anime', 25, 12, 'a10', 55, 'Im Halbfinale treffen die Devil Bats auf die Seibu Wild Gunmen - und somit stehen sich auch Riku und'),
        ('07:40', 'Die neuen Abenteuer des He-Man', 'Mutantenhochzeit', 'Zeichentrick', 25, 3, 'a3', 55, 'Prinz Adam muss auf dem Planeten Primus gegen gefährliche Mutanten kämpfen.'),
        ('08:05', 'Die neuen Abenteuer des He-Man', 'Pflanzenkrieg', 'Zeichentrick', 25, 6, 'a6', 55, 'Prinz Adam muss auf dem Planeten Primus gegen gefährliche Mutanten kämpfen.'),
        ('08:30', 'Die neuen Abenteuer des He-Man', 'Gepples Sprengstoff', 'Zeichentrick', 25, 6, 'a6', 55, 'Prinz Adam muss auf dem Planeten Primus gegen gefährliche Mutanten kämpfen.'),
        ('08:55', 'She-Ra', 'Nichts als Ärger', 'Zeichentrick', 25, 6, 'a6', 55, 'She-Ra kämpft gegen den finsteren Hordak und die Böse Horde.'),
        ('09:20', 'She-Ra', 'Der König der Trolle', 'Zeichentrick', 20, 6, 'a6', 55, 'She-Ra kämpft gegen den finsteren Hordak und die Böse Horde.'),
        ('09:40', 'Voltron: Legendärer Verteidiger', 'Kampfwunden', 'Zeichentrick', 25, 6, 'a6', 55, 'Um Honervas durchtriebene Pläne aufzudecken, treiben die Paladine durch das Universum und beschließe'),
        ('10:05', 'Voltron: Legendärer Verteidiger', 'Der Groll', 'Zeichentrick', 25, 6, 'a6', 55, 'Das Ziel der Paladine, sich wieder mit der Atlas zu vereinen, wird jäh unterbrochen, als die Löwen v'),
        ('10:30', 'She-Ra und die Rebellen-Prinzessinnen', 'Light Hope', 'Zeichentrick', 25, 6, 'a6', 55, 'Die Kriegerin She-Ra will ihren Planeten aus den Fängen der Horde befreien.'),
        ('10:55', 'Die neuen Abenteuer des He-Man', 'Rockfieber', 'Zeichentrick', 20, 6, 'a6', 55, 'Prinz Adam muss auf dem Planeten Primus gegen gefährliche Mutanten kämpfen.'),
        ('11:15', 'Die neuen Abenteuer des He-Man', 'Dreadator, der Gefürchtete', 'Zeichentrick', 25, 6, 'a6', 55, 'Prinz Adam muss auf dem Planeten Primus gegen gefährliche Mutanten kämpfen.'),
        ('11:40', 'Die neuen Abenteuer des He-Man', 'Gefangen im Ionensturm', 'Zeichentrick', 25, 6, 'a6', 55, 'Prinz Adam muss auf dem Planeten Primus gegen gefährliche Mutanten kämpfen.'),
        ('12:05', 'She-Ra', 'Das Schicksalstor', 'Zeichentrick', 25, 6, 'a6', 55, 'She-Ra kämpft gegen den finsteren Hordak und die Böse Horde.'),
        ('12:30', 'She-Ra', 'Die Einhörner in Gefahr', 'Zeichentrick', 20, 6, 'a6', 55, 'She-Ra kämpft gegen den finsteren Hordak und die Böse Horde.'),
        ('12:50', 'Voltron: Legendärer Verteidiger', 'Ursprung', 'Zeichentrick', 30, 6, 'a6', 55, 'In höchster Eile bricht Voltron nach Oriande auf, um Honervas durchtriebene Pläne zu durchkreuzen. M'),
        ('13:20', 'Voltron: Legendärer Verteidiger', 'Tag 47', 'Zeichentrick', 25, 6, 'a6', 55, 'In ihrem Vlog gewähren die Piloten Kinkade und Rizavi einen Einblick in den Alltag an Bord der Atlas'),
        ('13:45', 'She-Ra und die Rebellen-Prinzessinnen', 'Die Schlacht von Bright Moon', 'Zeichentrick', 20, 6, 'a6', 55, 'Die Kriegerin She-Ra will ihren Planeten aus den Fängen der Horde befreien.'),
        ('23:55', 'Dragon Ball Super', 'Überschreite alle Grenzen! Goku gegen Gohan!', 'Anime', 25, 12, 'a10', 55, 'Durch Piccolos Training strotzt Son Gohan geradezu vor Selbstvertrauen. Siegessicher fordert er sein'),
    ]),
    ("Samstag, 15.08.2026", "WDR", [
        ('08:10', 'Die Sendung mit dem Elefanten', 'Wie funktioniert ein Pfandflaschenautomat?', 'Serie', 25, 3, 'a3', 55, 'In der Sendung mit dem Elefanten macht sich Knolle auf Entdeckungsreise zum Supermarkt. Er will wiss'),
        ('08:35', 'Die Sendung mit der Maus', '', 'Vorlesen', 30, 6, 'a6', 55, 'Lach- und Sachgeschichten'),
    ]),
    ("Samstag, 15.08.2026", "NDR", [
        ('07:00', 'Die Sendung mit der Maus', '', 'Vorlesen', 30, 3, 'a3', 55, 'Lach- und Sachgeschichten, heute mit Clarissa und einem Haufen Haaren, Trudes Tier und dem Traum vom'),
    ]),
    ("Samstag, 15.08.2026", "BR", [
        ('20:15', 'Die drei Musketiere', '', 'Serie', 100, 10, 'a10', 55, 'Im Paris des 17. Jahrhunderts dienen die Musketiere König Louis XIII. Zur gleichen Zeit verlässt der'),
    ]),
    ("Samstag, 15.08.2026", "MDR", [
        ('07:00', 'Meister Eder und sein Pumuckl', 'Die abergläubische Putzfrau', 'Serie', 25, 3, 'a3', 55, 'Meister Eder liegt krank im Bett und kann sich nicht um den Haushalt kümmern. Er ruft Frau Eichinger'),
        ('07:25', 'Meister Eder und sein Pumuckl', 'Eder bekommt Besuch', 'Serie', 25, 3, 'a3', 55, 'Eder bekommt Besuch von seiner Schwester und deren Tochter Bärbel. Das Mädchen spielt mit Pumuckls B'),
        ('18:15', 'Unterwegs in Sachsen-Anhalt', 'Urlaub auf dem Bauernhof', 'Serie', 30, 6, 'a6', 55, 'Zwischen Erholung und echter Hofarbeit: Urlaub auf dem Bauernhof kann vielfältig sein. Aber was habe'),
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Herr Fuchs hat wieder einmal eine Erfindung gemacht. Sie soll verhindern, dass man das Zähneputzen v'),
    ]),
    ("Samstag, 15.08.2026", "RBB", [
        ('05:45', 'Schloss Einstein', '', 'Jugendserie', 25, 10, 'a10', 55, 'Während eines Fußballspiels im Sportunterricht, rastet Tommy aus, beleidigt Herrn Krassnick und wirf'),
        ('06:10', 'Schloss Einstein', '', 'Jugendserie', 25, 10, 'a10', 55, 'Weil Tochter Leonie auf Klassenfahrt fährt, muss Herr Berger für einige Tage Karlchen, Leonies Kanin'),
        ('06:35', 'Samuel - Graffiti-Sprayer aus Berlin', '', 'Vorlesen', 25, 3, 'a3', 55, 'Der 13-jährige Samuel aus Berlin ist ein begeisterter Sprayer. Diese Leidenschaft teilt er mit viele'),
        ('07:00', 'Die Wrack-Taucherin in der Ostsee', '', 'Vorlesen', 25, 3, 'a3', 55, 'Antonia ist 12 Jahre alt und das Wasser ist ihr zweites Zuhause. Sie schwimmt und taucht am liebsten'),
        ('10:25', 'Die sieben Raben', '', 'Zeichentrick', 95, 6, 'a6', 55, 'Bohdanka ist ein glückliches Mädchen. Wenn nur nicht ihre Mutter immer so traurig wäre und um die Tr'),
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Fuchs und Elster: Herr Fuchs als Erfinder'),
    ]),
    ("Samstag, 15.08.2026", "HR", [
        ('08:35', 'Schau in meine Welt', 'Cocos Welt. YouTuberin in London', 'Vorlesen', 25, 6, 'a6', 55, 'Coco (12) lebt in London und ist ein YouTube-Star. 100.000 Follower aus der ganzen Welt schauen ihre'),
    ]),
    ("Samstag, 15.08.2026", "3sat", [
        ('12:15', "Liebesg'schichten und Heiratssachen", '', 'Serie', 45, 6, 'a6', 55, 'In der Halbzeitausgabe der Jubiläumsstaffel von "Liebesg\'schichten und Heiratssachen" besucht Nina H'),
    ]),
    ("Samstag, 15.08.2026", "arte", [
        ('04:40', 'Verdammte Katze!', 'Puma oder nicht Puma', 'Zeichentrick', 35, 3, 'a3', 55, 'Moustique ist frustriert: Irgendwie fühlt er sich nicht mehr wie der wilde, unbesiegbare Jäger von e'),
    ]),
    ("Samstag, 15.08.2026", "ORF 1", [
        ('06:00', 'Die Jagd nach dem Kju Wang', 'Ardelias neue Leidenschaft', 'Zeichentrick', 25, 3, 'a3', 55, 'Graf Yagor gelingt es, seine Nichte Alma unter einem Vorwand in Cirillos Palast einzuschleusen. Arde'),
        ('06:25', 'Kung Fu Panda: Die Tatzen des Schicksals', 'Auf dünnem Eis', 'Zeichentrick', 25, 3, 'a3', 55, 'Po ist fest entschlossen, sein Chi wiederzubekommen. Außerdem muss er seine Schüler wiederfinden. Di'),
        ('06:50', 'Der gestiefelte Kater - Abenteuer in San Lorenzo', 'Der große Zauber', 'Serie', 20, 3, 'a3', 55, 'Mit Hut und Degen zieht der gestiefelte Kater durchs Land, immer auf der Suche nach einem neuen Aben'),
        ('07:10', 'Der gestiefelte Kater - Abenteuer in San Lorenzo', 'Der Schatz von San Losano', 'Serie', 20, 3, 'a3', 55, 'Mit Hut und Degen zieht der gestiefelte Kater durchs Land, immer auf der Suche nach einem neuen Aben'),
        ('07:30', 'Grizzy und die Lemminge', 'Die Eisparty', 'Zeichentrick', 10, 3, 'a3', 55, 'Es ist Hochsommer und brütend heiß. Im Fernsehen sieht Grizzy eine appetitanregende Werbung für Eisc'),
        ('07:40', 'Servus Kasperl', 'Kasperl & Strolchi: Die Zauberrose', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('08:05', 'Paw Patrol - Der Kinofilm', '', 'Zeichentrick', 75, 6, 'a6', 55, "Temporeiches, erstes Kinoabenteuer der beliebten Hunde-Stars der 'Paw Patrol'. Als Bürgermeister dro"),
    ]),
]
