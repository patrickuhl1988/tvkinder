# -*- coding: utf-8 -*-
"""Kindersendungen der Vollprogramme.

Erzeugt von scan_kinder.py aus tv.de am 26.08.2026. Auswahl nach Kategorie,
bekannten Titeln und Beschreibung; Alterswerte heuristisch.
"""

TAGE = [
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
        ('12:10', 'Die Liebe kommt selten allein', '', 'Serie', 85, 6, 'a6', 55, 'Die alleinstehende Berlinerin Eva Beckstedt ist das, was man eine echte "Zicke" nennt. Kein Wunder a'),
    ]),
    ("Mittwoch, 26.08.2026", "ORF 1", [
        ('06:52', 'Die Jagd nach dem Kju Wang', 'Der Besuch des Sultans', 'Zeichentrick', 24, 3, 'a3', 55, 'Der Sultan will mit dem Herzog einen Vertrag über Frieden und künftige Zusammenarbeit unterschreiben'),
        ('07:34', 'Garfield', 'Garfield, der Pirat - Teil 5', 'Zeichentrick', 14, 3, 'a3', 55, 'Mit dem letzten Puzzlestück der Schatzkarte finden Garfield und seine Crew endlich den Weg zum kostb'),
        ('07:48', 'Garfield', 'Der Lasagne-Baum - Teil 1', 'Zeichentrick', 14, 3, 'a3', 55, 'Garfields guter Freund Vito steckt in großen Schwierigkeiten. Seit Wochen steht sein Restaurant leer'),
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
        ('17:35', 'Detektiv Conan', 'Von rechts nach links: Winkekatzen', 'Anime', 30, 12, 'a10', 55, 'Ai und Conan retten ein Kätzchen aus einem Baum und bringen es zu seinem Besitzer, Tamotsu Ishigami,'),
        ('18:05', 'One Piece', 'Das Band zwischen Vater und Tochter - Kyros und Rebecca!', 'Anime', 25, 12, 'a10', 55, 'Rebecca steht nach ihrer abenteuerlichen Reise endlich ihrem Vater Kyros gegenüber und offenbart die'),
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
        ('04:34', 'Athleticus', 'Straßenfußball', 'Zeichentrick', 36, 3, 'a3', 55, 'Ein Giraffenkind und ein Elefantenbaby spielen vergnügt Fußball, bis sie von Straußen und Nilpferden'),
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
        ('17:15', 'SRF Kids Inside', 'IG Seifenkisten Derby Schweiz - Schnelligkeit ohne Motor', 'Vorlesen', 15, 6, 'a6', 55, '1 Verein, 3 Kids und noch mehr Storys: «SRF Kids Inside» erzählt Geschichten mitten aus dem Leben.'),
        ('17:30', 'Kiri und Lou', 'E schöni Erfrischig', 'Zeichentrick', 10, 6, 'a6', 55, 'Kiri und Lou, zwei junge Dinosaurier, leben in einem wunderschönen Wald. Die beiden ungleichen Freun'),
    ]),
    ("Freitag, 28.08.2026", "ProSieben Maxx", [
        ('16:40', 'Dr. STONE', 'Das Funkeln des Untergangs', 'Anime', 25, 12, 'a10', 55, 'Yo gelingt es, die Versteinerungswaffe zu beschlagnahmen, doch sein Triumph ist nur von kurzer Dauer'),
        ('17:05', 'Dragon Ball Super', 'Ein Kampf in Überlichtgeschwindigkeit! Goku und Hit an gemeinsamer Fro', 'Anime', 25, 12, 'a10', 55, 'Hit wird von Dyspo, einem rasend schnellen Kämpfer aus dem elften Universum, herausgefordert. Trotz '),
        ('17:30', 'Detektiv Conan', 'Love-Story im Hauptquartier 8 - Der linke Ringfinger (1)', 'Anime', 30, 12, 'a10', 55, 'Sato erscheint mit einem Ring am linken Ringfinger zur Arbeit und versetzt ihre Kollegen in Erstaune'),
        ('18:00', 'One Piece', 'Kein Entkommen - Fujitoras unbarmherzige Verfolgungsjagd!', 'Anime', 25, 12, 'a10', 55, 'Fujitora hat es auf die Piratenflotte abgesehen, die am Hafen von Dress Rosa ankert. Doch die Einwoh'),
        ('18:25', 'One Piece', 'Sakeschalen der Gefolgschaft - Die Entstehung der Strohhut-Großflotte!', 'Anime', 30, 12, 'a10', 55, 'Im Kampf gegen de Flamingo schließen sich Ruffys Anhänger zu einer mächtigen Truppe zusammen. Kann d'),
        ('18:55', 'Detektiv Conan', 'Den Männern in Schwarz auf der Spur (1)', 'Anime', 25, 12, 'a10', 55, 'In der Klasse 1B der Teitan Grundschule wird eine neue Schülerin erwartet: Ai Haibara. Die Lehrerin '),
        ('20:15', 'Naruto Shippuden the Movie', '', 'Zeichentrick', 105, 12, 'a10', 55, 'Als ein mächtiger Dämon ins Reich der Lebenden zurückkommt, beschließt Naruto, die Schamanin Shion z'),
        ('22:00', 'Gachiakuta', 'Das Hauptquartier des Putztrupps', 'Anime', 30, 12, 'a10', 55, 'Enjin und die anderen bringen Rudo in das Hauptquartier des Putztrupps. Dort angekommen, erhält er e'),
        ('22:30', 'Gachiakuta', 'Die Vandalen', 'Anime', 30, 12, 'a10', 55, 'Der Putztrupp veranstaltet eine Willkommensfeier für Rudo. Der Junge ist jedoch gar nicht in Partyst'),
        ('23:00', 'Gachiakuta', 'Die volle Breitseite!', 'Anime', 25, 12, 'a10', 55, 'Rudo und zwei seiner Kollegen vom Putztrupp treffen auf den Vandalen Jabber, der ihnen den Weg versp'),
        ('23:50', 'Frieren - Nach dem Ende der Reise', 'Der Held des Dorfes', 'Anime', 25, 12, 'a10', 55, 'Fern bittet Stark, ihr und Frieren beim Kampf gegen den Drachen zu helfen. Der Junge hat zwar Angst '),
    ]),
    ("Freitag, 28.08.2026", "WDR", [
        ('07:30', 'Campsite', 'Heute ist mein Geburtstag', 'Jugendserie', 10, 3, 'a3', 55, 'Lea ist enttäuscht: Sie hat Geburtstag, aber Nura und Thea verschwinden nach einem kurzen Glückwunsc'),
        ('21:15', 'Wuppertal und die einzigartige Schwebebahn', '', 'Wissen', 30, 10, 'a10', 55, 'Einmal im Leben durch Wuppertal schweben! Die Wuppertaler Schwebebahn feiert ihren 125. Geburtstag -'),
    ]),
    ("Freitag, 28.08.2026", "NDR", [
        ('06:00', 'Sesamstraße', '', 'Vorlesen', 20, 3, 'a3', 55, 'Ein am Ast hängender Apfel hat es Ernie angetan. Doch leider hängt der Apfel zu hoch für Ernie. Zum '),
    ]),
    ("Freitag, 28.08.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'In diesem traditionellen chinesischen Wiegenlied wird das Bett im Traum zu einem Schiff, mit dem das'),
    ]),
    ("Freitag, 28.08.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Internationale Kinderlieder: Yao lan qu'),
    ]),
    ("Freitag, 28.08.2026", "HR", [
        ('06:20', 'Leo da Vinci', 'Das verlassene Schloss', 'Zeichentrick', 10, 3, 'a3', 55, 'Bei einem Zwischenstopp in Bologna besucht Bianca ihren Freund Ildebrando, den sie bittet, eine Nach'),
        ('06:30', 'Leo da Vinci', 'Bianca die Hochstaplerin', 'Zeichentrick', 15, 3, 'a3', 55, 'Die Zwillinge Jack und Robert verkleiden sich als Boten der Herrscherin von Kastilien und versuchen,'),
    ]),
    ("Freitag, 28.08.2026", "arte", [
        ('04:45', 'Athleticus', 'Jonglieren', 'Zeichentrick', 15, 3, 'a3', 55, 'Eine Schildkröte auf Sightseeingtour: Fasziniert von einem Flamingo, der eine Glaskugel kunstvoll au'),
    ]),
    ("Freitag, 28.08.2026", "ORF 1", [
        ('06:00', 'ZIB KiDS', '', 'Serie', 10, 3, 'a3', 55, ''),
        ('06:10', 'Wickie und die starken Männer', 'Das Geisterschiff', 'Zeichentrick', 25, 3, 'a3', 55, 'Eines Tages entdeckt Faxe im Morgengrauen vor Flake ein Geisterschiff. Unter den Wikingern herrscht '),
        ('06:35', 'Servus Kasperl', 'Kasperl & Buffi: Ein Fest! Ein Superfest!', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('07:00', 'Die Jagd nach dem Kju Wang', 'Zirkus Royal', 'Zeichentrick', 25, 3, 'a3', 55, 'Yagor gibt diesmal vor, der "Große Bambino" zu sein. Sgarry gibt er als Clown aus. Um an den Kju Wan'),
        ('07:40', 'Garfield', 'Der Lasagne-Baum - Teil 4', 'Zeichentrick', 10, 3, 'a3', 55, 'Garfield und seine Freunde haben den sagenumwobenen Lasagne-Baum gefunden. Wie sich herausstellt ste'),
        ('07:50', 'ZIB KiDS', '', 'Serie', 10, 3, 'a3', 55, ''),
    ]),
    ("Freitag, 28.08.2026", "SRF 1", [
        ('17:30', 'Kiri und Lou', 'En unsichtbare Fründ', 'Zeichentrick', 10, 6, 'a6', 55, 'Kiri und Lou, zwei junge Dinosaurier, leben in einem wunderschönen Wald. Die beiden ungleichen Freun'),
    ]),
]
