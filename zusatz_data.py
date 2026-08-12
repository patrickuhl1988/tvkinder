# -*- coding: utf-8 -*-
"""Kindersendungen der Vollprogramme.

Erzeugt von scan_kinder.py aus tv.de am 12.08.2026. Auswahl nach Kategorie,
bekannten Titeln und Beschreibung; Alterswerte heuristisch.
"""

TAGE = [
    ("Mittwoch, 12.08.2026", "ProSieben Maxx", [
        ('16:45', 'Dr. STONE', 'Treasure Box', 'Anime', 25, 12, 'a10', 55, 'Senku und seine Freunde stechen mit ihrem neu gebauten Schiff Perseus in See. Nun wollen sie die Sch'),
        ('17:10', 'Dragon Ball Super', 'Eine Krise im 7. Universum! Das Team ist nicht vollzählig!', 'Anime', 25, 12, 'a10', 55, 'Das dritte Universum überlässt bei der Auswahl seiner Kämpfer nichts dem Zufall. Mit besonderen Modi'),
        ('17:35', 'Detektiv Conan', 'Real 30 Minutes', 'Anime', 30, 12, 'a10', 55, 'Conan und Ran sind mit Kogoro in einem Einkaufszentrum unterwegs und müssen noch etwas Zeit totschla'),
        ('18:05', 'One Piece', "Mach's gut! - Bellamys Schlag zum Abschied", 'Anime', 25, 12, 'a10', 55, 'Die Lage spitzt sich so weit zu, dass die Marine sich gezwungen sieht, die Bevölkerung zu evakuieren'),
        ('18:30', 'One Piece', 'Law stirbt! - Ruffys wütender Angriff', 'Anime', 25, 12, 'a10', 55, 'Nur noch zwei von De Flamingos Schergen sind kampffähig, doch auch die Strohhutbande hat Verluste zu'),
        ('18:55', 'Detektiv Conan', 'Der Serienmörder von Osaka (1)', 'Anime', 25, 12, 'a10', 55, 'Kürzlich gab es zwei Morde in Osaka. Es gibt jedoch jeweils keine Zeugen und auch keine Verbindungen'),
    ]),
    ("Mittwoch, 12.08.2026", "WDR", [
        ('07:55', 'Das Camp in der Wildnis', 'Alles nass', 'Vorlesen', 25, 3, 'a3', 55, 'Nichts für schwache Nerven! Die 9. Klässler haben im Kajak nicht nur mit strömendem Regen zu kämpfen'),
    ]),
    ("Mittwoch, 12.08.2026", "NDR", [
        ('07:40', 'Die Pfefferkörner', 'Plan Albatros', 'Serie', 35, 10, 'a10', 55, 'Moritz kommt auf seiner Laufrunde zwei Villeneinbrechern in die Quere. Er kann zwar geistesgegenwärt'),
    ]),
    ("Mittwoch, 12.08.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Ein mysteriöses Geräusch hält die Erdmännchen Jan & Henry vom Einschlafen ab.'),
    ]),
    ("Mittwoch, 12.08.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Jan & Henry: Das Meerschweinchen'),
    ]),
    ("Mittwoch, 12.08.2026", "SRF 1", [
        ('17:45', 'Pompon der kleine Bär', 'De gröschti Goldschatz', 'Vorlesen', 15, 6, 'a6', 55, 'Pompon und Linette suchen nach einem Goldschatz und finden ihn bei sich selbst. Mama ist die Beste!'),
    ]),
    ("Donnerstag, 13.08.2026", "ProSieben Maxx", [
        ('16:40', 'Dr. STONE', 'Das Licht der Hoffnung und Verzweiflung', 'Anime', 25, 12, 'a10', 55, 'Die Crew der Perseus kommt an der Schatzinsel an. Senku, Soyuz, Kohaku und Gen gehen an Land, um das'),
        ('17:05', 'Dragon Ball Super', 'Der zehnte Kämpfer bist du! Goku besucht Freezer!', 'Anime', 25, 12, 'a10', 55, 'Son Goku will Freezer bitten, als Ersatz für Boo mit Team Erde am Turnier der Universen teilzunehmen'),
        ('17:30', 'Detektiv Conan', 'Drei Tage mit Hattori Heiji (1)', 'Anime', 30, 12, 'a10', 55, 'Conan und die anderen sind auf einem Kirschblütenfest. Der junge Detektiv hat Heiji dorthin bestellt'),
        ('18:00', 'One Piece', 'Die Klinge des eisernen Willens - Der Gamma Knife Gegenangriff!', 'Anime', 25, 12, 'a10', 55, 'De Flamingo unterbreitet Law ein Angebot: Wenn dieser ihm mit Hilfe seiner Teufelskräfte Unsterblich'),
        ('18:25', 'One Piece', 'Zusammenprall der Haki! - Ruffy gegen De Flamingo', 'Anime', 25, 12, 'a10', 55, 'Laws Angriff setzt De Flamingo ordentlich zu. Der Samurai aber verfügt über außergewöhnliche Selbsth'),
        ('18:50', 'Detektiv Conan', 'Der Serienmörder von Osaka (2)', 'Anime', 30, 12, 'a10', 55, 'Die Todesursache von Sumie Okazaki steht fest: Strangulation mit einem Seil. Conan, Hejii und Yusuke'),
    ]),
    ("Donnerstag, 13.08.2026", "WDR", [
        ('07:35', 'Campsite', 'Der beste Platz', 'Jugendserie', 5, 3, 'a3', 55, 'Wo ist der schönste Platz am Strand? Silje lotst die Clique zu den hohen Felsen mit Blick aufs Wasse'),
        ('07:40', 'Campsite', 'Endlich alleine', 'Jugendserie', 5, 3, 'a3', 55, 'Siljes Schwester Emmi möchte allein im Wald zelten. Dass sie im Rollstuhl sitzt, ist für sie kein Hi'),
        ('07:45', 'Campsite', 'Der Revolver ist weg', 'Jugendserie', 10, 3, 'a3', 55, 'Sebbe und seine Freunde spielen ein Brettspiel, als sie erfahren, dass am Strand ein großes Segelsch'),
        ('07:55', 'Das Camp in der Wildnis', 'Krise im Kajak', 'Vorlesen', 25, 3, 'a3', 55, 'Emilia ergründet auf der Huskyfarm das Wesen ihres Patenhundes Skare und sie darf das erste Mal eine'),
    ]),
    ("Donnerstag, 13.08.2026", "NDR", [
        ('06:00', 'Sesamstraße', '', 'Vorlesen', 20, 3, 'a3', 55, 'Krümelmonster ist Jean Bonbon in "Leckereien für alle", der "Sesamstraßen"-Parodie von "Les Misérabl'),
        ('06:20', 'Schloss Einstein', '1069', 'Jugendserie', 25, 10, 'a10', 55, 'Ava und Patrick sind das perfekte Tanzteam. Ihr gemeinsames Castingvideo ist ein voller Erfolg. Doch'),
        ('06:45', 'Schloss Einstein', '1070', 'Jugendserie', 25, 10, 'a10', 55, 'Massuda entscheidet sich nach der intensiven Lernphase fürs Chillen. Als Herr Hauser sie jedoch zu d'),
        ('07:10', 'Die Pfefferkörner', 'Giftige Angelegenheit', 'Serie', 30, 10, 'a10', 55, 'Bei einem Waldspaziergang mit Amy reißt Pepper sich plötzlich los und kommt mit einem toten Eichhörn'),
        ('07:40', 'Die Pfefferkörner', 'Der Einbruch', 'Serie', 35, 10, 'a10', 55, 'Ein Nachbar bittet Mira, eine wertvolle Skulptur zu verwahren, während er für einen Tag verreist ist'),
    ]),
    ("Donnerstag, 13.08.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Dr. Brumm macht das, was er immer macht, wenn Pottwal sich die Flossen vertreten will: Er radelt mit'),
    ]),
    ("Donnerstag, 13.08.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Dr. Brumm: Dr. Brumm will helfen'),
    ]),
    ("Donnerstag, 13.08.2026", "HR", [
        ('06:20', 'Leo da Vinci', 'Der Traum vom Fliegen', 'Zeichentrick', 10, 3, 'a3', 55, 'Um Leo und seine Freunde aufzuhalten, wollen ihm die Gauner Jack und Robert eine Falle stellen und L'),
        ('06:30', 'Leo da Vinci', 'Der falsche Abt', 'Zeichentrick', 15, 3, 'a3', 55, 'Lollo freut sich, dass Bianca de Medici ihn, Leo und Lisa auf ihrer Reise nach Venedig begleiten wir'),
    ]),
    ("Donnerstag, 13.08.2026", "ORF 1", [
        ('06:00', 'Mister Paper', 'Mister Paper sehnt sich nach Regen', 'Zeichentrick', 5, 3, 'a3', 55, 'Im Papier-Land hat es schon lange nicht mehr geregnet. Die Bäume in Mister Papers Vorgarten sind des'),
        ('06:05', 'Wickie und die starken Männer', 'Sturm auf die Festung', 'Zeichentrick', 25, 3, 'a3', 55, 'Die Wikinger wollen unbedingt ein Schloss in Franken angreifen. Trozt aller Warnungen von Wickie las'),
        ('06:30', 'Servus Kasperl', 'Kasperl & Co: Das Drachenschwänzchen', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('06:55', 'Die Jagd nach dem Kju Wang', 'Der große Sänger', 'Zeichentrick', 25, 3, 'a3', 55, 'Der große Startenor Ugolotti kommt zu einem Benefizkonzert in Cirillos Palast. Berto, der selber ger'),
        ('07:35', 'Vegesaurier', 'Wackelzahn', 'Zeichentrick', 5, 3, 'a3', 55, 'Als ein Vulkan ausbricht, landet eine Lava-Nuss mit verlockendem Inhalt vor Gingers Füßchen. Ihre ne'),
        ('07:40', 'Garfield', 'Miese Maschinen - Teil 5', 'Zeichentrick', 15, 3, 'a3', 55, 'Garfield und die Rebellen sehen ihre letzte Chance, Master Control von der Weltherrschaft abzuhalten'),
    ]),
    ("Donnerstag, 13.08.2026", "SRF 1", [
        ('17:45', 'Pompon der kleine Bär', 'Es Waldmonschter', 'Vorlesen', 15, 6, 'a6', 55, 'Pompon und Rita auf Spuren des Waldmonsters Zerbidul, das letztlich doch keins ist.'),
    ]),
    ("Freitag, 14.08.2026", "ProSieben Maxx", [
        ('16:45', 'Dr. STONE', 'Das Ass im Ärmel auf dem Schiff der Wissenschaft', 'Anime', 25, 12, 'a10', 55, 'Die Besatzung der Perseus wurde versteinert. Senku, Soyuz, Kohaku und Gen, die sich auf der Schatzin'),
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
]
