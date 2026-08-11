# -*- coding: utf-8 -*-
"""Kindersendungen der Vollprogramme.

Erzeugt von scan_kinder.py aus tv.de am 11.08.2026. Auswahl nach Kategorie,
bekannten Titeln und Beschreibung; Alterswerte heuristisch.
"""

TAGE = [
    ("Dienstag, 11.08.2026", "ProSieben Maxx", [
        ('16:45', 'Dr. STONE', 'Perseus, das Schiff der Wissenschaft', 'Anime', 25, 12, 'a10', 55, 'Die Dorfbewohner beginnen mit dem Bau des Schiffes. Doch ohne Pläne, an die sie sich halten können, '),
        ('17:10', 'Dragon Ball Super', 'Welches Universum wird siegen? Die stärksten Krieger versammeln sich!', 'Anime', 25, 12, 'a10', 55, 'Während das Team der Erde endlich feststeht, sind die anderen Universen noch damit beschäftigt, Kämp'),
        ('17:35', 'Detektiv Conan', 'Gentas Killerschuss (2)', 'Anime', 30, 12, 'a10', 55, 'Kommissar Megure und Inspektor Takagi nehmen die Ermittlungen auf, um herauszufinden, wer Herrn Hein'),
        ('18:05', 'One Piece', 'Die Erde bebt erneut! - Picas großes Überraschungsmanöver', 'Anime', 25, 12, 'a10', 55, 'Nachdem sich nun auch Kyros in seinen Weg stellt, zieht Pica das stärkste Ass aus seinem Ärmel und v'),
        ('18:30', 'One Piece', 'Ein Luftkampf, der alles entscheidet - Zorros Geheimtechnik', 'Anime', 25, 12, 'a10', 55, 'Um De Flamingos Herrschaft zu sichern, will Pica den ehemaligen König Riku töten. Die Widerstandskäm'),
        ('18:55', 'Detektiv Conan', 'Wo ist Nintaro Shinmei? (2)', 'Anime', 25, 12, 'a10', 55, 'Während Conan das Manuskript des halben Zenits in den Händen hält, unterhält er sich mit Ran. Ein un'),
    ]),
    ("Dienstag, 11.08.2026", "WDR", [
        ('07:35', 'Campsite', 'Von Aliens entführt', 'Jugendserie', 5, 3, 'a3', 55, 'William macht sich über Mattis lustig, der sich vor Horrorfilmen gruselt. Doch als er am nächsten Mo'),
        ('07:40', 'Campsite', 'Der Plastik-Sammeltag', 'Jugendserie', 5, 3, 'a3', 55, 'Der Campingplatz ruft einen Wettbewerb aus: Wer den meisten Müll am Strand einsammelt, gewinnt ein b'),
        ('07:45', 'Campsite', 'Das Quiz', 'Jugendserie', 10, 3, 'a3', 55, 'Sebbe veranstaltet ein Sonntags-Quiz für seine Freunde. Aber die Fragen haben es in sich. Während si'),
        ('07:55', 'Das Camp in der Wildnis', 'Nachts in der Wildnis', 'Vorlesen', 25, 3, 'a3', 55, 'In der norwegischen Wildnis treffen Maxi und alle anderen bei der Suche nach einem Schlafplatz eine '),
    ]),
    ("Dienstag, 11.08.2026", "NDR", [
        ('07:10', 'Die Pfefferkörner', 'Die einzige Chance', 'Serie', 30, 10, 'a10', 55, 'Amy findet einen hübschen Glitzeranhänger in einem Straßengully. Sie beschließt, ihn zu behalten, ni'),
        ('07:40', 'Die Pfefferkörner', 'Blackout', 'Serie', 35, 10, 'a10', 55, 'Ausgerechnet am Tag, an dem Leo als Pflegekind bei Familie Bruns einzieht, legt ein Stromausfall die'),
    ]),
    ("Dienstag, 11.08.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Der Fisch auf meiner Schmusedecke hat ein Problem: er hat kein Wasser mehr in seinem Becken! Werden '),
    ]),
    ("Dienstag, 11.08.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Meine Schmusedecke: Der Fisch'),
    ]),
    ("Dienstag, 11.08.2026", "HR", [
        ('11:20', 'Annas Erbe', '', 'Serie', 90, 6, 'a6', 55, 'Der überraschende Tod ihres geliebten Mannes trifft Anna Ingstrup wie ein Schlag: Plötzlich steht si'),
        ('23:15', 'Annas Erbe', '', 'Serie', 25, 10, 'a10', 55, 'Der überraschende Tod ihres geliebten Mannes trifft Anna Ingstrup wie ein Schlag: Plötzlich steht si'),
    ]),
    ("Dienstag, 11.08.2026", "arte", [
        ('15:30', 'Mord im Mittsommer', 'Vicky', 'Serie', 95, 6, 'a6', 55, 'Der berühmte Professor für Kinderpsychologie Carl-Johan Berger wird während einer Feier auf seinem A'),
    ]),
    ("Dienstag, 11.08.2026", "ORF 1", [
        ('07:38', 'Garfield', 'Miese Maschinen - Teil 3', 'Zeichentrick', 14, 3, 'a3', 55, 'Es werden immer mehr Menschen mit Robotersoldaten aus dem Weltall ausgetauscht. Ihre Mission ist es,'),
    ]),
    ("Dienstag, 11.08.2026", "SRF 1", [
        ('17:45', 'Pompon der kleine Bär', 'Nuss oder Ei?', 'Vorlesen', 15, 6, 'a6', 55, 'Pompon und Rita versuchen, die Ursprünge eines geheimnisvollen Eis (oder Nuss) zu ergründen und müss'),
    ]),
    ("Mittwoch, 12.08.2026", "ProSieben Maxx", [
        ('16:45', 'Dr. STONE', 'Treasure Box', 'Anime', 25, 12, 'a10', 55, 'Senku und seine Freunde stechen mit ihrem neu gebauten Schiff Perseus in See. Nun wollen sie die Sch'),
        ('17:10', 'Dragon Ball Super', 'Eine Krise im 7. Universum! Das Team ist nicht vollzählig!', 'Anime', 25, 12, 'a10', 55, 'Das dritte Universum überlässt bei der Auswahl seiner Kämpfer nichts dem Zufall. Mit besonderen Modi'),
        ('17:35', 'Detektiv Conan', 'Real 30 Minutes', 'Anime', 30, 12, 'a10', 55, 'Conan und Ran sind mit Kogoro in einem Einkaufszentrum unterwegs und müssen noch etwas Zeit totschla'),
        ('18:05', 'One Piece', "Mach's gut! - Bellamys Schlag zum Abschied", 'Anime', 25, 12, 'a10', 55, 'Die Lage spitzt sich so weit zu, dass die Marine sich gezwungen sieht, die Bevölkerung zu evakuieren'),
        ('18:30', 'One Piece', 'Law stirbt! - Ruffys wütender Angriff', 'Anime', 25, 12, 'a10', 55, 'Nur noch zwei von De Flamingos Schergen sind kampffähig, doch auch die Strohhutbande hat Verluste zu'),
        ('18:55', 'Detektiv Conan', 'Der Serienmörder von Osaka (1)', 'Anime', 25, 12, 'a10', 55, 'Kürzlich gab es zwei Morde in Osaka. Es gibt jedoch jeweils keine Zeugen und auch keine Verbindungen'),
    ]),
    ("Mittwoch, 12.08.2026", "WDR", [
        ('07:35', 'Campsite', 'Gekauft und Bezahlt', 'Jugendserie', 5, 3, 'a3', 55, 'Andrine verteilt in der Clique Süßigkeiten aus dem Supermarkt des Campingplatzes und ihre Freunde si'),
        ('07:40', 'Campsite', 'Duell', 'Jugendserie', 5, 3, 'a3', 55, 'Anja und Silje haben den ganzen Sommer Zugang zum Ballspielplatz. Hauptsache, sie lassen Lea nicht r'),
        ('07:45', 'Campsite', 'Ein neuer Slush-Meister', 'Jugendserie', 10, 3, 'a3', 55, 'Theo bewirbt sich um einen Job als Slushie-Verkäufer, aber bei seinen Probeschichten läuft der Verka'),
        ('07:55', 'Das Camp in der Wildnis', 'Alles nass', 'Vorlesen', 25, 3, 'a3', 55, 'Nichts für schwache Nerven! Die 9. Klässler haben im Kajak nicht nur mit strömendem Regen zu kämpfen'),
    ]),
    ("Mittwoch, 12.08.2026", "NDR", [
        ('06:00', 'Sesamstraße', '', 'Vorlesen', 20, 3, 'a3', 55, 'Bert möchte Elektrostatik erklären. Allerdings entfremdet Ernie den für die Erklärung vorgesehenen L'),
        ('06:20', 'Schloss Einstein', '1067', 'Jugendserie', 25, 10, 'a10', 55, 'Joshua hält sich für schlauer als das Schatzsuche-Team von Maxi. Er nutzt den Schulausflug ins Stasi'),
        ('06:45', 'Schloss Einstein', '1068', 'Jugendserie', 25, 10, 'a10', 55, 'Tahmina und Mikka suchen im Wald nach dem Schatz. Statt etwas zu finden, kommen beide jedoch vom Weg'),
        ('07:10', 'Die Pfefferkörner', 'Stinkbombe', 'Serie', 30, 10, 'a10', 55, 'Hakim wird morgens vor der Schule von einem mysteriösen Angreifer attackiert und verliert kurzzeitig'),
        ('07:40', 'Die Pfefferkörner', 'Plan Albatros', 'Serie', 35, 10, 'a10', 55, 'Moritz kommt auf seiner Laufrunde zwei Villeneinbrechern in die Quere. Er kann zwar geistesgegenwärt'),
    ]),
    ("Mittwoch, 12.08.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Ein mysteriöses Geräusch hält die Erdmännchen Jan & Henry vom Einschlafen ab.'),
    ]),
    ("Mittwoch, 12.08.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Jan & Henry: Das Meerschweinchen'),
    ]),
    ("Mittwoch, 12.08.2026", "HR", [
        ('06:20', 'Leo da Vinci', 'Der Fluchtversuch', 'Zeichentrick', 10, 3, 'a3', 55, 'Um Leo und seinen Freunden schnell folgen zu können, verschaffen sich die beiden Gauner Robert und J'),
        ('06:30', 'Leo da Vinci', 'Das Buch des Marco Polo', 'Zeichentrick', 15, 3, 'a3', 55, 'Bevor er auf große Abenteuerreise geht, verabschiedet sich Leo wehmütig von seinem geliebten Geheimv'),
    ]),
    ("Mittwoch, 12.08.2026", "ORF 1", [
        ('06:00', 'Mister Paper', 'Mister Paper baut ein Schloss', 'Zeichentrick', 5, 3, 'a3', 55, 'Mister Paper hat sich viel vorgenommen: Er will ein Schloss bauen! Für dieses Großprojekt braucht er'),
        ('06:05', 'Wickie und die starken Männer', 'Wickie gewinnt einen Freund', 'Zeichentrick', 25, 3, 'a3', 55, 'Auf dem Heimweg von England suchen die Wikinger an der Küste nach Wasser. Sie werden von Sverker und'),
        ('06:30', 'Servus Kasperl', 'Kasperl & Hopsi: Der hinterlistige Schlaumaier', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('06:55', 'Die Jagd nach dem Kju Wang', 'Die Zwillinge', 'Zeichentrick', 25, 3, 'a3', 55, 'Ardelia und Herzog Cirillo erhalten eine Einladung zur Hochzeit des Jahres, ein absolutes gesellscha'),
        ('07:35', 'Vegesaurier', 'Das große Brüllen', 'Zeichentrick', 5, 3, 'a3', 55, 'Ginger und die Erbs-Rexe machen einen Brüllwettbewerb. Weil alle vier gleichzeitig kräftig herumschr'),
        ('07:40', 'Garfield', 'Miese Maschinen - Teil 4', 'Zeichentrick', 15, 3, 'a3', 55, 'Einer der Widerstandskämpfer gegen die miesen Maschinen reist auf die Erde und bittet Garfield, mit '),
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
]
