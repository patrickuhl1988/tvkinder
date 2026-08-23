# -*- coding: utf-8 -*-
"""Kindersendungen der Vollprogramme.

Erzeugt von scan_kinder.py aus tv.de am 23.08.2026. Auswahl nach Kategorie,
bekannten Titeln und Beschreibung; Alterswerte heuristisch.
"""

TAGE = [
    ("Sonntag, 23.08.2026", "ARD", [
        ('06:10', 'Tigerenten Club', 'Der Club zum Mitmachen - Spiele, Spaß und spannendes Wissen', 'Vorlesen', 55, 3, 'a3', 55, 'Als Astronautin ins All! Anschnallen - es geht ins Weltall! Amelie wird zur Astronautin ausgebildet.'),
        ('08:30', 'Alina', 'Silverado in Gefahr', 'Jugendserie', 60, 10, 'a10', 55, 'Alina heißt das 13-jährige Mädchen, das im Mittelpunkt des Dreiteilers steht. Die Schülerin lebt mit'),
        ('09:30', 'Die Sendung mit der Maus', '', 'Vorlesen', 30, 6, 'a6', 55, 'Lach- und Sachgeschichten, heute mit einer Gottesanbeterin auf der Lauer, einem großen Monster im Wa'),
    ]),
    ("Sonntag, 23.08.2026", "ZDF", [
        ('07:00', 'Wickie und die starken Männer', 'Die verflixte Kuh', 'Zeichentrick', 10, 3, 'a3', 55, 'Was tun, wenn eine Kuh Halvars Hochzeitsgeschenk für Ylva aufgefressen hat? Die Zeit wird knapp, abe'),
        ('07:10', 'Wickie und die starken Männer', 'Pilzesammeln', 'Zeichentrick', 15, 3, 'a3', 55, 'Wickie geht mit Ylvi Pilze sammeln, und da Gilby den gleichen Auftrag von seiner Mutter hat, geht er'),
        ('07:25', 'Bibi Blocksberg', 'Kreuzfahrt mit Oma Grete', 'Zeichentrick', 25, 3, 'a3', 55, 'Oma Grete und Bibi machen eine Kreuzfahrt. Auch eine Gräfin und deren Enkel Karl-Friedrich gehen an '),
        ('07:50', 'Bibi und Tina', 'Das Schlossfest', 'Zeichentrick', 25, 3, 'a3', 55, 'Der Graf hat zu einem Familientreffen auf Schloss Falkenstein eingeladen. Dort sollen die Familienmi'),
        ('08:15', 'Löwenzahn', 'Haut - Empfindlich auf die Pelle gerückt', 'Serie', 25, 6, 'a6', 55, 'Fritz Fuchs testet teures Haarwuchsmittel. Seine Schwester Suse hat es bei einem Straßenhändler geka'),
        ('08:40', 'Michel aus Lönneberga', 'Als Michel die Tiere mit Kirschen fütterte', 'Serie', 23, 6, 'a6', 55, 'Michels Mutter setzt Kirschwasser an, und Michel verfüttert die Kirschen an die Tiere. Schon bald la'),
    ]),
    ("Sonntag, 23.08.2026", "NDR", [
        ('07:00', 'Edgar, das Super-Karibu', 'Der Gemüse-Tag', 'Zeichentrick', 10, 3, 'a3', 55, 'Edgar, das Super-Karibu und Katja, die Katze, die ständig herumfaucht, versuchen die Bewohner des St'),
    ]),
    ("Sonntag, 23.08.2026", "BR", [
        ('08:35', 'Helene, die wahre Braut', '', 'Serie', 60, 6, 'a6', 55, 'Helene wird von ihrer bösen Stiefmutter Gertrud zu Arbeiten gezwungen, die nicht zu schaffen sind. A'),
    ]),
    ("Sonntag, 23.08.2026", "SWR", [
        ('11:00', 'Ostwind', '', 'Film', 95, 6, 'a6', 55, 'Die vierzehnjährige Mika muss ausgerechnet auf dem Reiterhof ihrer strengen Großmutter den Sommer üb'),
    ]),
    ("Sonntag, 23.08.2026", "MDR", [
        ('15:50', 'Der Schweinehirt', '', 'Serie', 60, 6, 'a6', 55, 'Das kleine Königreich Lichterwald steht vor dem finanziellen Ruin. Einzig und allein eine reiche Hoc'),
        ('18:52', 'Unser Sandmännchen', '', 'Serie', 8, 3, 'a3', 55, 'Herr Fuchs findet auf einem Abendspaziergang eine Kindergeldbörse, die er gern für sich behalten möc'),
    ]),
    ("Sonntag, 23.08.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Kallis Gute-Nacht-Geschichten: Kalli - Kalli'),
    ]),
    ("Sonntag, 23.08.2026", "ORF 1", [
        ('07:00', 'Vegesaurier', 'Reingefallen!', 'Zeichentrick', 5, 3, 'a3', 55, 'Ginger und ihre Erbs-Rex-Babys fliehen vor zwei Bananaraptoren. Als diese in eine Grube fallen, besc'),
        ('07:05', 'Bakabu', 'Ich nicht', 'Vorlesen', 4, 3, 'a3', 55, 'Hast du schon einmal ein Eis gegessen, das nach Ketchup schmeckt oder im Schokokuchen eine Kuh entde'),
        ('07:09', 'Knall genial', '', 'Wissen', 19, 3, 'a3', 55, "Originelle Tipps und Tricks von Thomas Brezina und den Kids! Thomas' Kuriositätenladen ist wieder ge"),
        ('07:28', 'Der gestiefelte Kater - Abenteuer in San Lorenzo', 'Nur geträumt!', 'Serie', 22, 3, 'a3', 55, 'Mit Hut und Degen zieht der gestiefelte Kater durchs Land, immer auf der Suche nach einem neuen Aben'),
        ('07:50', 'Drunter & drüber mit Christoph Hirschler', 'NOA und der Dinosaurier in der Achterbahn', 'Vorlesen', 16, 3, 'a3', 55, 'Heute wird es bei "Drunter & Drüber" musikalisch! Christoph Hirschler und seine Band begrüßen den ju'),
        ('08:06', 'Campsite', 'Silje in der Patsche', 'Jugendserie', 10, 10, 'a10', 55, 'Silje erzählt ihren Freunden, dass sie den bekannten Influencer Kattekryp kennt und gut mit ihm befr'),
        ('08:16', 'Campsite', 'Der Trampolin-Streit', 'Jugendserie', 7, 10, 'a10', 55, 'Thea, Theo und Nura wollen Trampolin springen. Als sie beim Trampolin ankommen, sind sie verwundert,'),
        ('08:23', 'Campsite', 'Es gibt Krieg', 'Jugendserie', 8, 10, 'a10', 55, 'Der erbitterte Krieg ums Trampolin geht in die nächste Runde. Die beiden Lager um Nura und Andrine w'),
        ('08:31', 'Dragons - Die Wächter von Berk', 'Eingefroren', 'Zeichentrick', 22, 6, 'a6', 55, 'Als Hicks und Ohnezahn von einem Auftrag zurückkehren, finden sie zu ihrer Verwunderung Berk völlig '),
        ('08:53', 'Was geht?', 'Zusammen stark', 'Wissen', 13, 6, 'a6', 55, 'Eine starke Gemeinschaft - wie geht das? Tiara (10), Raffael (10) und Lou (10) sprechen mit Pädagogi'),
        ('09:06', 'Mini Spezial', 'Autodesigner', 'Vorlesen', 4, 6, 'a6', 55, 'Hast du schon mal ein Auto aus Plastilin gesehen, das gleich groß ist, wie Autos, die auf der Straße'),
        ('09:10', 'Garfield', 'Garfield im Land der Träume', 'Zeichentrick', 13, 6, 'a6', 55, 'Der Nachbarsjunge ist sehr erfinderisch und talentiert im Bau von wissenschaftlichen Maschinen. So h'),
        ('09:23', 'Hallo, was machst Du?', 'Gärtner', 'Wissen', 12, 6, 'a6', 55, 'Blumen pflanzen und Rasenmähen - das sind die Aufgaben von Gärtnerinnen und Gärtner, an die wahrsche'),
    ]),
    ("Sonntag, 23.08.2026", "SRF 1", [
        ('17:10', 'Minisguard', 'Wie bleiben Lebensmittel länger frisch?', 'Serie', 15, 6, 'a6', 55, 'Auf der Suche nach Antworten besucht Élin Ana, Expertin für Lebensmittellagerung bei Valentin Gastro'),
    ]),
    ("Montag, 24.08.2026", "ProSieben Maxx", [
        ('16:40', 'Dr. STONE', 'Kampf mit Köpfchen', 'Anime', 25, 12, 'a10', 55, 'Senku und seinen Kameraden gelingt es, immer mehr ihrer Freunde wiederzubeleben. Doch die Freude im '),
        ('17:05', 'Dragon Ball Super', 'Total außer Kontrolle! Eine wilde Berserkerin erwacht!', 'Anime', 25, 12, 'a10', 55, 'Son Goku trifft auf Caulifla und Kale, zwei Kämpferinnen aus dem sechsten Universum. Als Kale in ihr'),
        ('17:30', 'Detektiv Conan', 'Der verschwundene Polizist', 'Anime', 30, 12, 'a10', 55, 'Die Detective Boys treffen auf Ayumis ehemalige Nachbarin. Die Frau berichtet den Kindern von einem '),
        ('18:00', 'One Piece', 'Ausbreitende Schockwelle - Die schlimmste Generation tritt in Aktion!', 'Anime', 25, 12, 'a10', 55, 'Nach dem Kampf auf Dressrosa löst Kyros die Tontatta- Armee auf. Sakazuki trifft in Mary Geoise die '),
        ('18:25', 'One Piece', 'Die Geburt einer Legende! - Die Abenteuer des Revolutionskämpfers Sabo', 'Anime', 30, 12, 'a10', 55, "Die tapferen Kämpfer ruhen sich in Kyros' Haus aus. Bald stößt auch Sabo dazu, der etwas zu offenbar"),
        ('18:55', 'Detektiv Conan', 'Der mysteriöse Scharfschütze (2)', 'Anime', 25, 12, 'a10', 55, 'Yukiko, die Sekretärin von Direktor Ishimoto, hat einen Liebhaber namens Shibata, auf den Kogoro eif'),
    ]),
    ("Montag, 24.08.2026", "WDR", [
        ('06:45', 'Wissen macht Ah!', 'Wissen macht anziehend', 'Vorlesen', 25, 3, 'a3', 55, 'Farben und Muster - darum geht es in der heutigen Sendung. Denn Farben und Muster sind anziehend. Be'),
        ('07:10', 'POV - Deine Geschichte zählt', 'Hauptsache Crash vermeiden · Mein Leben mit ME/CFS', 'Vorlesen', 10, 3, 'a3', 55, 'Leonie (16) fühlt sich in der Schule oft ausgeschlossen. Halt findet sie in Musik, Konzerten und Onl'),
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
    ("Montag, 24.08.2026", "HR", [
        ('05:20', 'Schau in meine Welt', 'Lina die Boxerin aus der Wüste', 'Vorlesen', 25, 3, 'a3', 55, 'Lina (12) aus Jordanien trainiert seit einem Jahr im Boxring und ist bereits so erfolgreich, dass es'),
        ('06:35', 'Leo da Vinci', 'Die Fossilien-Höhle', 'Zeichentrick', 10, 3, 'a3', 55, 'Durch die holprige Straße hat sich die Bremse in Leos Gefährt gelöst. In der Nähe des nächsten Dorfe'),
        ('06:45', 'Leo da Vinci', 'Zwei Löwen', 'Zeichentrick', 15, 3, 'a3', 55, 'Die Gauner Robert und Jack sind verzweifelt. Die Karte, die sie nach Venedig und auf die Spur Leos z'),
    ]),
    ("Montag, 24.08.2026", "arte", [
        ('04:30', 'Athleticus', 'Fitness-Coach', 'Zeichentrick', 40, 3, 'a3', 55, 'Im Park coacht ein hartnäckiger Vogel Strauß einen behäbigen Elefanten beim Sport. Es gibt Lauftrain'),
    ]),
    ("Montag, 24.08.2026", "ORF 1", [
        ('06:05', 'Wickie und die starken Männer', 'Das böse Weib', 'Zeichentrick', 25, 3, 'a3', 55, 'Auf dem Heimweg nach Flake bekommen die Wikinger die Rache der Magyaren zu spüren: Ein starker Gegen'),
        ('06:30', 'Servus Kasperl', 'Kasperl & Hopsi: Der goldene Kerzenleuchter', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('06:55', 'Die Jagd nach dem Kju Wang', 'Ardelias Foto-Termin', 'Zeichentrick', 25, 3, 'a3', 55, 'Yagor hat wiedereinmal einen Plan. Unter dem Decknamen Knipsi Bertolini, seines Zeichens berühmter P'),
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
]
