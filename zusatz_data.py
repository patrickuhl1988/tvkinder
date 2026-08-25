# -*- coding: utf-8 -*-
"""Kindersendungen der Vollprogramme.

Erzeugt von scan_kinder.py aus tv.de am 25.08.2026. Auswahl nach Kategorie,
bekannten Titeln und Beschreibung; Alterswerte heuristisch.
"""

TAGE = [
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
    ("Dienstag, 25.08.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Der Fuchs auf meiner Schmusedecke hat ein Problem: Keiner spielt mit ihm! Werden seine Freunde eine '),
    ]),
    ("Dienstag, 25.08.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Meine Schmusedecke: Der Fuchs'),
    ]),
    ("Dienstag, 25.08.2026", "ORF 1", [
        ('06:54', 'Die Jagd nach dem Kju Wang', 'Filmstar Ardelia', 'Zeichentrick', 23, 3, 'a3', 55, 'Getarnt als der große Regisseur Fetuccini gibt Yagor vor, in Venedig einen gigantischen Film drehen '),
        ('07:34', 'Vegesaurier', 'Essenszeit', 'Zeichentrick', 5, 3, 'a3', 55, 'Die Baby-Erbs-Rexe Minzi, Wasabi und Split haben wieder einmal großen Hunger. Split findet eine Spur'),
        ('07:39', 'Dragons - Die Wächter von Berk', 'Eingefroren', 'Zeichentrick', 21, 3, 'a3', 55, 'Als Hicks und Ohnezahn von einem Auftrag zurückkehren, finden sie zu ihrer Verwunderung Berk völlig '),
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
    ("Donnerstag, 27.08.2026", "ZDF", [
        ('09:05', 'Volle Kanne - Service täglich', '', 'Serie', 85, 6, 'a6', 55, '- Gast: Eva Umlauf Ärztin und Holocaustüberlebende - Geldanlage für Kinder Was Sie dabei beachten so'),
    ]),
    ("Donnerstag, 27.08.2026", "ProSieben Maxx", [
        ('16:45', 'Dr. STONE', 'Joker', 'Anime', 25, 12, 'a10', 55, 'Senku und seine Freunde entern das Schiff des Feindes. Durch die Vortäuschung von Magie gelingt es i'),
        ('17:10', 'Dragon Ball Super', 'Gohan, zeig keine Gnade! Showdown mit dem 10. Universum!', 'Anime', 25, 12, 'a10', 55, 'Während der Kampf zwischen dem siebten und dem zweiten Universum weitergeht, müssen sich Son Gohan u'),
        ('17:35', 'Detektiv Conan', 'Von rechts nach links: Winkekatzen', 'Anime', 25, 12, 'a10', 55, 'Ai und Conan retten ein Kätzchen aus einem Baum und bringen es zu seinem Besitzer, Tamotsu Ishigami,'),
        ('18:00', 'One Piece', 'Das Band zwischen Vater und Tochter - Kyros und Rebecca!', 'Anime', 30, 12, 'a10', 55, 'Rebecca steht nach ihrer abenteuerlichen Reise endlich ihrem Vater Kyros gegenüber und offenbart die'),
        ('18:30', 'One Piece', 'Der Stolz eines Mannes - Ruffys Kopf-an-Kopf-Kampf gegen Fujitora!', 'Anime', 25, 12, 'a10', 55, 'Während Sengoku ein ernstes Wörtchen mit Law wechselt, will Fujitora seinen teuflischen Pan in die T'),
        ('18:55', 'Detektiv Conan', 'Der Milliardenraub', 'Anime', 25, 12, 'a10', 55, 'Conan wird Zeuge eines Überfalls auf einen Geldtransporter. Kurze Zeit später findet man den Fluchtw'),
    ]),
    ("Donnerstag, 27.08.2026", "WDR", [
        ('07:35', 'Campsite', 'Freundinnen', 'Jugendserie', 5, 3, 'a3', 55, 'Lea freut sich über den Einzug ins Volleyball-Halbfinale und wird von der Gruppe als Naturtalent gef'),
        ('07:40', 'Campsite', 'Die Todesklippe', 'Jugendserie', 5, 3, 'a3', 55, 'Der traditionelle "Todesklippen-Sprungtag" steht an - doch wie im Vorjahr verpasst Mattis ihn im let'),
        ('07:45', 'Campsite', 'Das Doppeldate', 'Jugendserie', 10, 3, 'a3', 55, 'Als Klaus Anja erzählt, Max sei in sie verliebt, beschließt sie, mit Sebbe Schluss zu machen. Max fa'),
        ('07:55', 'Das Camp in der Wildnis', 'Eisiges Bad', 'Vorlesen', 25, 3, 'a3', 55, 'Obwohl nächtliches Husky Geheul und das Porridge-Frühstück den Start in den Tag erschweren, kommt di'),
        ('08:20', 'Das Camp in der Wildnis', 'Frühjahrsputz für Fortgeschrittene', 'Vorlesen', 25, 6, 'a6', 55, 'Der Winter geht, der Frühling kommt! Das Thermometer zeigt endlich die ersten Plusgrade an und schon'),
    ]),
    ("Donnerstag, 27.08.2026", "NDR", [
        ('06:00', 'Sesamstraße', '', 'Vorlesen', 20, 3, 'a3', 55, 'Elmo hat ein neues Wort gelernt: Überraschung. Was das Wort bedeutet, erklärt er gleich mal in einem'),
    ]),
    ("Donnerstag, 27.08.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Dr. Brumm macht das, was er immer macht, wenn er nichts zu tun hat: Er puzzelt. Mit einem Hammer klo'),
    ]),
    ("Donnerstag, 27.08.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Dr. Brumm: Dr. Brumm puzzelt'),
    ]),
    ("Donnerstag, 27.08.2026", "HR", [
        ('06:25', 'Leo da Vinci', 'Der falsche Apotheker', 'Zeichentrick', 10, 3, 'a3', 55, 'Bianca wurde von den Soldaten Montefeltros gekidnappt und ihre Freunde tun alles, um sie zu befreien'),
        ('06:35', 'Leo da Vinci', 'Zwei glückliche Enden', 'Zeichentrick', 15, 3, 'a3', 55, 'Nach Lollos Scheitern gelingt es den Freunden, dank Leos genialem Plan, Bianca zu befreien. Durch ei'),
        ('12:10', 'Ein Drilling kommt selten allein', '', 'Serie', 90, 6, 'a6', 55, 'Die Journalistin Linda Rosenau lebt nur für ihren Beruf: Als Chefredakteurin eines erfolgreichen Fra'),
    ]),
    ("Donnerstag, 27.08.2026", "arte", [
        ('04:40', 'Athleticus', 'Straßenfußball', 'Zeichentrick', 30, 3, 'a3', 55, 'Ein Giraffenkind und ein Elefantenbaby spielen vergnügt Fußball, bis sie von Straußen und Nilpferden'),
    ]),
    ("Donnerstag, 27.08.2026", "ORF 1", [
        ('06:05', 'Wickie und die starken Männer', 'Faxe hat eine Braut', 'Zeichentrick', 25, 3, 'a3', 55, 'Die Wikinger versuchen, Faxe zu verheiraten - Halvar hat die Braut bereits ausgesucht. Leider aber i'),
        ('06:30', 'Servus Kasperl', 'Kasperl & Strolchi: Das Lügengespenst', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('06:55', 'Die Jagd nach dem Kju Wang', 'Das Palastgespenst', 'Zeichentrick', 25, 3, 'a3', 55, 'Im Palast des Herzogs spukt es. Zumindest verbreitet Murky dieses Gerücht, der ja nicht weiß, dass e'),
        ('07:40', 'Garfield', 'Der Lasagne-Baum - Teil 2', 'Zeichentrick', 10, 3, 'a3', 55, 'Seine Widersacher arbeiten weiter hart daran, Vito und sein Restaurant zu sabotieren. Sie bearbeiten'),
        ('07:50', 'Garfield', 'Der Lasagne-Baum - Teil 3', 'Zeichentrick', 10, 3, 'a3', 55, 'Es verschlägt Garfield, Jon, Odie und Vitos Freundin nach Italien. Sie suchen nach Vito, der spurlos'),
    ]),
    ("Donnerstag, 27.08.2026", "SRF 1", [
        ('17:05', 'SRF Kids News', '', 'Serie', 10, 6, 'a6', 55, ''),
        ('17:15', 'SRF Kids Inside', 'IG Seifenkisten Derby Schweiz - Schnelligkeit ohne Motor', 'Vorlesen', 15, 6, 'a6', 55, ''),
        ('17:30', 'Kiri und Lou', 'E schöni Erfrischig', 'Zeichentrick', 10, 6, 'a6', 55, 'Kiri und Lou, zwei junge Dinosaurier, leben in einem wunderschönen Wald. Die beiden ungleichen Freun'),
    ]),
]
