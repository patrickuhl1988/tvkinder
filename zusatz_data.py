# -*- coding: utf-8 -*-
"""Kindersendungen der Vollprogramme.

Erzeugt von scan_kinder.py aus tv.de am 24.08.2026. Auswahl nach Kategorie,
bekannten Titeln und Beschreibung; Alterswerte heuristisch.
"""

TAGE = [
    ("Montag, 24.08.2026", "ProSieben Maxx", [
        ('16:40', 'Dr. STONE', 'Kampf mit Köpfchen', 'Anime', 25, 12, 'a10', 55, 'Senku und seinen Kameraden gelingt es, immer mehr ihrer Freunde wiederzubeleben. Doch die Freude im '),
        ('17:05', 'Dragon Ball Super', 'Total außer Kontrolle! Eine wilde Berserkerin erwacht!', 'Anime', 25, 12, 'a10', 55, 'Son Goku trifft auf Caulifla und Kale, zwei Kämpferinnen aus dem sechsten Universum. Als Kale in ihr'),
        ('17:30', 'Detektiv Conan', 'Der verschwundene Polizist', 'Anime', 30, 12, 'a10', 55, 'Die Detective Boys treffen auf Ayumis ehemalige Nachbarin. Die Frau berichtet den Kindern von einem '),
        ('18:00', 'One Piece', 'Ausbreitende Schockwelle - Die schlimmste Generation tritt in Aktion!', 'Anime', 25, 12, 'a10', 55, 'Nach dem Kampf auf Dressrosa löst Kyros die Tontatta- Armee auf. Sakazuki trifft in Mary Geoise die '),
        ('18:25', 'One Piece', 'Die Geburt einer Legende! - Die Abenteuer des Revolutionskämpfers Sabo', 'Anime', 30, 12, 'a10', 55, "Die tapferen Kämpfer ruhen sich in Kyros' Haus aus. Bald stößt auch Sabo dazu, der etwas zu offenbar"),
        ('18:55', 'Detektiv Conan', 'Der mysteriöse Scharfschütze (2)', 'Anime', 25, 12, 'a10', 55, 'Yukiko, die Sekretärin von Direktor Ishimoto, hat einen Liebhaber namens Shibata, auf den Kogoro eif'),
    ]),
    ("Montag, 24.08.2026", "WDR", [
        ('07:20', 'Campsite', 'Wollen wir wetten?', 'Jugendserie', 10, 3, 'a3', 55, 'Klaus überredet William zu einer Runde Finger-Klatschen: Der Verlierer muss EINE Sache für den ander'),
        ('07:30', 'Campsite', 'Der Lottoschein', 'Jugendserie', 5, 3, 'a3', 55, 'Klaus, Max und Silje wollen eigentlich baden gehen, als Anja sie aufgeregt zu Ruth ruft - einer skur'),
        ('07:35', 'Campsite', 'Mafia', 'Jugendserie', 10, 3, 'a3', 55, 'William ist plötzlich ein Star auf dem Campingplatz. Der Grund: Er besitzt ein mysteriöses Foto, das'),
        ('07:45', 'Hauptsache Bären!', '', 'Serie', 85, 3, 'a3', 55, 'Jips großer Traum wird wahr, als ihre Eltern beschließen, in einem Wohnmobil durch Amerika zu reisen'),
    ]),
    ("Montag, 24.08.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'MiWau hört im Leckerladen ein mysteriöses Brummen. Moppi soll helfen, das unbekannte Geräusch zu erk'),
    ]),
    ("Montag, 24.08.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Moppi und MiWau: Der mutige Wachhund'),
    ]),
    ("Montag, 24.08.2026", "ORF 1", [
        ('07:35', 'Vegesaurier', 'Im Nest', 'Zeichentrick', 5, 3, 'a3', 55, 'Gingers größter Wunsch wäre es, fliegen zu können. Obwohl sie gar keine Flügel hat, unternimmt das T'),
        ('07:40', 'Vegesaurier', 'Frische Kartoffelchips', 'Zeichentrick', 5, 3, 'a3', 55, 'Sonntags baden die Kartofflodons in den mineralreichen Quellen und aalen sich daraufhin in der Sonne'),
        ('07:45', 'Dragons - Die Wächter von Berk', 'Raffnuss, die Drachenzähmerin', 'Zeichentrick', 20, 3, 'a3', 55, 'Hicks und seine Freunde entdecken auf einer Insel einen verletzten Wasserdrachen. Er kann nicht zurü'),
    ]),
    ("Montag, 24.08.2026", "SRF 1", [
        ('17:30', 'Kiri und Lou', 'Immer wider Versteckis', 'Zeichentrick', 10, 6, 'a6', 55, 'Kiri und Lou, zwei junge Dinosaurier, leben in einem wunderschönen Wald. Die beiden ungleichen Freun'),
    ]),
    ("Dienstag, 25.08.2026", "ProSieben Maxx", [
        ('16:40', 'Dr. STONE', 'Schlacht der dritten Dimension', 'Anime', 25, 12, 'a10', 55, 'Senku und seine Freunde bereiten sich auf die finale Schlacht gegen Ibara und seine Untertanen vor. '),
        ('17:05', 'Dragon Ball Super', 'Die Krieger der Gerechtigkeit kommen! Der Kampf gegen die stolze Briga', 'Anime', 25, 12, 'a10', 55, 'Im Eifer des Gefechts hat sich Team Erde aus den Augen verloren: Tenshinhan, Muten-Roshi und Son Goh'),
        ('17:30', 'Detektiv Conan', 'Wo das schwarze Foto ist (1)', 'Anime', 30, 12, 'a10', 55, 'Heiji liefert Conan neue Informationen über die Vergangenheit von Eisuke Hondou und dessen Vater, de'),
        ('18:00', 'One Piece', 'Das Bündnis der Brüder! - Die Geschichte von Ruffys und Sabos Wiederse', 'Anime', 25, 12, 'a10', 55, 'Nachdem er von Aces Tod erfahren hatte, gewann Sabo sein Gehör zurück. Zwei Jahre später besuchte er'),
        ('18:25', 'One Piece', 'Die stärkste Kreatur aller Zeiten! - Kaido der hundert Bestien', 'Anime', 30, 12, 'a10', 55, 'Kaido der hundert Bestien landet aus heiterem Himmel auf der Basis und verkündet, er werde einen Kri'),
        ('18:55', 'Detektiv Conan', 'Mord im Theater (1)', 'Anime', 25, 12, 'a10', 55, 'Eine Wandertheatergruppe ist in Beika zu Besuch. Tamanosuke, der Anführer, lädt Conan, die Detective'),
    ]),
    ("Dienstag, 25.08.2026", "WDR", [
        ('07:35', 'Campsite', 'Romeo und Andrine', 'Jugendserie', 5, 3, 'a3', 55, 'Ein neuer Junge - Romeo - kommt mit seiner Familie auf den Campingplatz, und Andrine zeigt ihnen all'),
        ('07:40', 'Campsite', 'Liebeskummer und Feuerquallen', 'Jugendserie', 5, 3, 'a3', 55, 'Andrine hat Liebeskummer: Romeo ist mit seiner Familie abgereist, ohne sich von ihr zu verabschieden'),
        ('07:45', 'Campsite', 'Intimsphäre', 'Jugendserie', 10, 3, 'a3', 55, 'Klaus ist genervt: Seine Freunde rücken ihm ständig auf die Pelle. Ob beim Trampolinspringen oder be'),
        ('07:55', 'Das Camp in der Wildnis', 'Explosiver Eintopf', 'Vorlesen', 25, 3, 'a3', 55, 'Nach den Weihnachtsferien in der Heimat herrscht schlechte Stimmung im Wildnis-Camp. Kein Ausschlafe'),
        ('08:20', 'Das Camp in der Wildnis', 'Ganz schön rutschig', 'Vorlesen', 25, 6, 'a6', 55, 'Nach den ersten Versuchen auf Langlaufskiern steht für die Wildnis-Klasse die nächste Etappe der Tou'),
    ]),
    ("Dienstag, 25.08.2026", "NDR", [
        ('06:00', 'Sesamstraße', '', 'Vorlesen', 20, 3, 'a3', 55, 'Ernie versucht herauszufinden, wie sich sein Quietscheentchen fühlt. Bert meint, dass das nicht geht'),
    ]),
    ("Dienstag, 25.08.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Der Fuchs auf meiner Schmusedecke hat ein Problem: Keiner spielt mit ihm! Werden seine Freunde eine '),
    ]),
    ("Dienstag, 25.08.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Meine Schmusedecke: Der Fuchs'),
    ]),
    ("Dienstag, 25.08.2026", "HR", [
        ('06:20', 'Leo da Vinci', 'Das Geheimnis der Zahlen', 'Zeichentrick', 10, 3, 'a3', 55, 'Leo und seine Freunde erreichen die Stadt Mirandola, wo sie Antonio, einen Freund Leos zu finden erh'),
        ('06:30', 'Leo da Vinci', 'Bernardo, der Abenteurer', 'Zeichentrick', 15, 3, 'a3', 55, 'Die Gauner Robert und Jack haben sich Giovanni geschnappt. Von ihm wollen sie wissen, was er Leo und'),
    ]),
    ("Dienstag, 25.08.2026", "arte", [
        ('04:35', 'Athleticus', 'Capoeira', 'Zeichentrick', 35, 3, 'a3', 55, 'Ein Giraffenjunges überwindet seine Ängste durch einen Capoeira-Kurs. Seine Freunde stehen ihm unter'),
    ]),
    ("Dienstag, 25.08.2026", "ORF 1", [
        ('06:05', 'Wickie und die starken Männer', 'Die Schatztruhe', 'Zeichentrick', 25, 3, 'a3', 55, 'Als die Wikinger von ihren Abenteuern nach Flake zurückkommen, finden sie Sven und seine Männer vor,'),
        ('06:30', 'Servus Kasperl', 'Kasperl & Co: Der Liebesbrief', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('06:55', 'Die Jagd nach dem Kju Wang', 'Filmstar Ardelia', 'Zeichentrick', 25, 3, 'a3', 55, 'Getarnt als der große Regisseur Fetuccini gibt Yagor vor, in Venedig einen gigantischen Film drehen '),
        ('07:35', 'Vegesaurier', 'Essenszeit', 'Zeichentrick', 5, 3, 'a3', 55, 'Die Baby-Erbs-Rexe Minzi, Wasabi und Split haben wieder einmal großen Hunger. Split findet eine Spur'),
        ('07:40', 'Dragons - Die Wächter von Berk', 'Eingefroren', 'Zeichentrick', 20, 3, 'a3', 55, 'Als Hicks und Ohnezahn von einem Auftrag zurückkehren, finden sie zu ihrer Verwunderung Berk völlig '),
    ]),
    ("Dienstag, 25.08.2026", "SRF 1", [
        ('17:30', 'Kiri und Lou', 'Wunderblueme', 'Zeichentrick', 10, 6, 'a6', 55, 'Kiri und Lou, zwei junge Dinosaurier, leben in einem wunderschönen Wald. Die beiden ungleichen Freun'),
    ]),
    ("Mittwoch, 26.08.2026", "ProSieben Maxx", [
        ('16:40', 'Dr. STONE', 'Battle Royale', 'Anime', 25, 12, 'a10', 55, 'Die Schlacht gegen Ibara und seine Untertanen hat begonnen. Mithilfe von Moz soll Kirisame dazu gebr'),
        ('17:05', 'Dragon Ball Super', 'Eine Explosion der Liebe! Die Kriegerhexen des 2. Universums greifen a', 'Anime', 25, 12, 'a10', 55, 'Von den acht teilnehmenden Universen sind nur noch drei in voller Besetzung im Turnier, unter andere'),
        ('17:30', 'Detektiv Conan', 'Wo das schwarze Foto ist (2)', 'Anime', 30, 12, 'a10', 55, 'Conan muss herausfinden, wer in Nishiguns Wohnung eingedrungen ist und das Foto von Eisukes Vater en'),
        ('18:00', 'One Piece', 'Fujitoras nächster Schritt - Die vollständige Belagerung der Strohhüte', 'Anime', 25, 12, 'a10', 55, 'Fujitora will einen Würfel über das Schicksal von Ruffy und Law entscheiden lassen. Das Mysterium um'),
        ('18:25', 'One Piece', 'Ein Notfall - Rebecca wird entführt!', 'Anime', 30, 12, 'a10', 55, 'Bei einem Angriff auf die Strohhüte gelingt es Ruffy, Rebecca zu entführen. Der Pirat hat den Plan, '),
        ('18:55', 'Detektiv Conan', 'Mord im Theater (2)', 'Anime', 25, 12, 'a10', 55, 'Frau Itoe stürzt die Bühnenvertiefung herunter und stirbt. In ihrer Hand findet Conan einen Zettel, '),
    ]),
    ("Mittwoch, 26.08.2026", "WDR", [
        ('07:35', 'Campsite', 'Wir langweilen uns', 'Jugendserie', 5, 3, 'a3', 55, 'Regen auf dem Campingplatz: Lea, Nura, Leo und Theo liegen gelangweilt herum und streiten sich über '),
        ('07:40', 'Campsite', 'Er ist zurück', 'Jugendserie', 5, 3, 'a3', 55, 'Andrine ist gestresst: Auf dem Campingplatz hat eine Familie eingecheckt, die schon im Vorjahr da wa'),
        ('07:45', 'Campsite', '15 Minutes of Fame', 'Jugendserie', 10, 3, 'a3', 55, 'Sebbe will mit einer Dance-Performance das vorbeifahrende "Sommermobil" eines Fernsehsenders auf sic'),
        ('07:55', 'Das Camp in der Wildnis', 'Lust auf Lava', 'Vorlesen', 25, 3, 'a3', 55, 'Die Wildnis-Klasse nutzt die Pause zwischen den Wintertouren im Camp für Kreativarbeit: Niklas und X'),
        ('08:20', 'Das Camp in der Wildnis', 'Auf Husky-Tour', 'Vorlesen', 25, 6, 'a6', 55, 'Ein Traum geht für die Wildnis-Klasse in Erfüllung! Sich auf dem Schlitten von einem Huskygespann du'),
    ]),
    ("Mittwoch, 26.08.2026", "NDR", [
        ('06:00', 'Sesamstraße', '', 'Vorlesen', 20, 3, 'a3', 55, 'Ernie möchte erklären, was Gegensätze sind und fragt Bert, ob er mitmachen möchte. Hätte Bert mal li'),
    ]),
    ("Mittwoch, 26.08.2026", "SWR", [
        ('21:00', 'Die Ernährungs-Docs', 'Rheuma, Schuppenflechte', 'Wissen', 45, 10, 'a10', 55, 'Yvonne und Stephan W.(48) von der Insel Sylt leiden an chronischem Rheuma. Yvonne hat Schmerzen in d'),
    ]),
    ("Mittwoch, 26.08.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Die Erdmännchen Jan und Henry sind sich sicher, dass bei ihnen vor der Tür eine Schildkröte im Renna'),
    ]),
    ("Mittwoch, 26.08.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Jan & Henry: Die Schildkröte im Rennauto'),
    ]),
    ("Mittwoch, 26.08.2026", "HR", [
        ('06:25', 'Leo da Vinci', 'Ein Parfum aus Dreck', 'Zeichentrick', 10, 3, 'a3', 55, 'Lollo hält den jungen Abenteurer Bernardo noch immer für einen Aufschneider und Lügner. Doch Bianca '),
        ('06:35', 'Leo da Vinci', 'Die Puppenspieler von Bologna', 'Zeichentrick', 15, 3, 'a3', 55, 'Leo und seine Freunde machen auf ihrer Reise einen Zwischenstopp in Bologna. Hier soll eine Gruppe m'),
        ('12:10', 'Die Liebe kommt selten allein', '', 'Serie', 85, 6, 'a6', 55, 'Die alleinstehende Berlinerin Eva Beckstedt ist das, was man eine echte "Zicke" nennt. Kein Wunder a'),
    ]),
    ("Mittwoch, 26.08.2026", "arte", [
        ('04:35', 'Athleticus', 'Kung Fu', 'Zeichentrick', 30, 3, 'a3', 55, 'Ein Giraffenkind und ein Elefantenbaby gehen bei einer Schildkröte in die Lehre, um die Kampfkunst K'),
    ]),
    ("Mittwoch, 26.08.2026", "ORF 1", [
        ('06:05', 'Wickie und die starken Männer', 'Die Rache der Sägefische', 'Zeichentrick', 25, 3, 'a3', 55, 'Das Boot der Wikinger ist gesunken. Unter Leitung des Zimmermanns Tjure soll ein neues, schönes Schi'),
        ('06:30', 'Servus Kasperl', 'Kasperl & Pezi: Gefährliche Süßigkeiten', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('06:55', 'Die Jagd nach dem Kju Wang', 'Der Besuch des Sultans', 'Zeichentrick', 25, 3, 'a3', 55, 'Der Sultan will mit dem Herzog einen Vertrag über Frieden und künftige Zusammenarbeit unterschreiben'),
        ('07:40', 'Garfield', 'Garfield, der Pirat - Teil 5', 'Zeichentrick', 10, 3, 'a3', 55, 'Mit dem letzten Puzzlestück der Schatzkarte finden Garfield und seine Crew endlich den Weg zum kostb'),
        ('07:50', 'Garfield', 'Der Lasagne-Baum - Teil 1', 'Zeichentrick', 10, 3, 'a3', 55, 'Garfields guter Freund Vito steckt in großen Schwierigkeiten. Seit Wochen steht sein Restaurant leer'),
    ]),
    ("Mittwoch, 26.08.2026", "SRF 1", [
        ('17:30', 'Kiri und Lou', 'Njam-njam-Boronies', 'Zeichentrick', 10, 6, 'a6', 55, 'Kiri und Lou, zwei junge Dinosaurier, leben in einem wunderschönen Wald. Die beiden ungleichen Freun'),
        ('23:00', 'Robot Dreams', '', 'Zeichentrick', 25, 10, 'a10', 55, 'Nachdem der Roboter (mit der Stimme von Ivan Labanda) während eines Ausflugs an den Strand am Tag de'),
    ]),
]
