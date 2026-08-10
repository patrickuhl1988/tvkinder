# -*- coding: utf-8 -*-
"""Kindersendungen der Vollprogramme.

Erzeugt von scan_kinder.py aus tv.de am 10.08.2026. Auswahl nach Kategorie,
bekannten Titeln und Beschreibung; Alterswerte heuristisch.
"""

TAGE = [
    ("Montag, 10.08.2026", "ProSieben Maxx", [
        ('16:45', 'Dr. STONE', 'Auge der Wissenschaft', 'Anime', 25, 12, 'a10', 55, 'Senku und seine Freunde erhalten mysteriöse Signale einer unbekannten Person, die sie "Whyman" nenne'),
        ('17:10', 'Dragon Ball Super', 'Überschreite alle Grenzen! Goku gegen Gohan!', 'Anime', 25, 12, 'a10', 55, 'Durch Piccolos Training strotzt Son Gohan geradezu vor Selbstvertrauen. Siegessicher fordert er sein'),
        ('17:35', 'Detektiv Conan', 'Gentas Killerschuss (1)', 'Anime', 30, 12, 'a10', 55, 'Nach einem Fußballspiel fährt Professor Agasa mit den Kindern noch zum Kuchenessen. In der Tiefgarag'),
        ('18:05', 'One Piece', 'Tödlicher Sternenstaub! - Diamantes Sturm der bösartigen Angriffe', 'Anime', 25, 12, 'a10', 55, 'Auf dem Königsplateau spitzt sich der Kampf zwischen Kyros und Diamante immer weiter zu. Trotz seine'),
        ('18:30', 'One Piece', "Trueno Bastardo - Kyros' ultimative Attacke!", 'Anime', 25, 12, 'a10', 55, "Diamante verliert angesichts Kyros' Gleichgültigkeit die Fassung. Blutüberströmt nimmt der Krieger d"),
        ('18:55', 'Detektiv Conan', 'Wo ist Nintaro Shinmei? (1)', 'Anime', 25, 12, 'a10', 55, 'Fünf Personen stehen um einen in der Mitte liegenden toten Körper herum, als plötzlich ein Unbekannt'),
    ]),
    ("Montag, 10.08.2026", "WDR", [
        ('07:55', 'Geschichten vom Franz', '', 'Film', 75, 3, 'a3', 55, 'Franz ist neun Jahre alt und wird von allen gehänselt. Dabei ist er doch ein Mann - na ja, so gut wi'),
    ]),
    ("Montag, 10.08.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Auf einem nächtlichen Spaziergang im Leckerladen stößt MiWau aus Versehen an einen Becher, der auf M'),
    ]),
    ("Montag, 10.08.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Moppi und MiWau: Die kleine Nachtmusik'),
    ]),
    ("Montag, 10.08.2026", "SRF 1", [
        ('17:45', 'Pompon der kleine Bär', 'Ich wett ich wär gross', 'Vorlesen', 15, 6, 'a6', 55, 'Pompon will gross sein und geht mit seinem Papa ein Windrad flicken. Es ist anstrengender als gedach'),
    ]),
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
        ('06:00', 'Sesamstraße', '', 'Vorlesen', 20, 3, 'a3', 55, 'Bert möchte Licht und Schatten erklären. Als Ernie dann sein Quietscheentchen vor die Lampe hält, wi'),
        ('06:20', 'Schloss Einstein', '1065', 'Jugendserie', 25, 10, 'a10', 55, 'Nesrin will gemeinsam mit Marlon herausfinden, ob sie verliebt ist. Ob ein paar Fragen in einem Onli'),
        ('06:45', 'Schloss Einstein', '1066', 'Jugendserie', 25, 10, 'a10', 55, 'Die Suche nach dem geheimen DDR-Schatz nimmt mit Besuch des Zeitzeugens Udo Winkler eine neue Wendun'),
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
        ('06:15', 'Leo da Vinci', 'Der Krummsäbel', 'Zeichentrick', 10, 3, 'a3', 55, 'Bianca de Medici möchte unbedingt mit Leo und seinen Freunden nach Venedig aufbrechen, um mit ihnen '),
        ('06:25', 'Leo da Vinci', 'Der Liebestrank', 'Zeichentrick', 15, 3, 'a3', 55, 'Um zu verhindern, dass Leo zuerst Venedig erreicht, um den legendären Rubin des Marco Polo zu bekomm'),
        ('11:20', 'Annas Erbe', '', 'Serie', 90, 6, 'a6', 55, 'Der überraschende Tod ihres geliebten Mannes trifft Anna Ingstrup wie ein Schlag: Plötzlich steht si'),
        ('23:15', 'Annas Erbe', '', 'Serie', 25, 10, 'a10', 55, 'Der überraschende Tod ihres geliebten Mannes trifft Anna Ingstrup wie ein Schlag: Plötzlich steht si'),
    ]),
    ("Dienstag, 11.08.2026", "arte", [
        ('15:30', 'Mord im Mittsommer', 'Vicky', 'Serie', 95, 6, 'a6', 55, 'Der berühmte Professor für Kinderpsychologie Carl-Johan Berger wird während einer Feier auf seinem A'),
    ]),
    ("Dienstag, 11.08.2026", "ORF 1", [
        ('06:00', 'Mister Paper', 'Mister Paper lernt pfeifen', 'Zeichentrick', 5, 3, 'a3', 55, 'Mister Paper erfreut sich an dem herrlichen Vogelgezwitscher vor seinem Fenster. So schön möchte er '),
        ('06:05', 'Wickie und die starken Männer', 'Die Befreiung', 'Zeichentrick', 25, 3, 'a3', 55, 'Nachdem Wickie und Snorre in England angekommen sind, um die Wikinger zu befreien, treffen sie mit d'),
        ('06:30', 'Servus Kasperl', 'Kasperl & Leopold: Die böse Zauberuhr', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('06:55', 'Die Jagd nach dem Kju Wang', 'Ardelia als Geschäftsfrau', 'Zeichentrick', 25, 3, 'a3', 55, 'Das alljährliche Frühlingsfest steht vor der Tür und Ardelia ist schon ganz aus dem Häuschen vor Fre'),
        ('07:35', 'Vegesaurier', 'Ich bin Ginger', 'Zeichentrick', 5, 3, 'a3', 55, 'Willkommen in der späten Knusperzeit, einer magischen Ära, in der die saftigsten und frischesten Kre'),
        ('07:40', 'Garfield', 'Miese Maschinen - Teil 3', 'Zeichentrick', 10, 3, 'a3', 55, 'Es werden immer mehr Menschen mit Robotersoldaten aus dem Weltall ausgetauscht. Ihre Mission ist es,'),
    ]),
    ("Dienstag, 11.08.2026", "SRF 1", [
        ('17:45', 'Pompon der kleine Bär', 'Nuss oder Ei?', 'Vorlesen', 15, 6, 'a6', 55, 'Pompon und Rita versuchen, die Ursprünge eines geheimnisvollen Eis (oder Nuss) zu ergründen und müss'),
    ]),
    ("Mittwoch, 12.08.2026", "ProSieben Maxx", [
        ('16:45', 'Dr. STONE', 'Treasure Box', 'Anime', 25, 12, 'a10', 55, 'Senku und seine Freunde stechen mit ihrem neu gebauten Schiff Perseus in See. Nun wollen sie die Sch'),
        ('17:10', 'Dragon Ball Super', 'Eine Krise im 7. Universum! Das Team ist nicht vollzählig!', 'Anime', 25, 12, 'a10', 55, 'Das dritte Universum überlässt bei der Auswahl seiner Kämpfer nichts dem Zufall. Mit besonderen Modi'),
        ('17:35', 'Detektiv Conan', 'Real 30 Minutes', 'Anime', 25, 12, 'a10', 55, 'Conan und Ran sind mit Kogoro in einem Einkaufszentrum unterwegs und müssen noch etwas Zeit totschla'),
        ('18:00', 'One Piece', "Mach's gut! - Bellamys Schlag zum Abschied", 'Anime', 30, 12, 'a10', 55, 'Die Lage spitzt sich so weit zu, dass die Marine sich gezwungen sieht, die Bevölkerung zu evakuieren'),
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
]
