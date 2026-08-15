# -*- coding: utf-8 -*-
"""Kindersendungen der Vollprogramme.

Erzeugt von scan_kinder.py aus tv.de am 15.08.2026. Auswahl nach Kategorie,
bekannten Titeln und Beschreibung; Alterswerte heuristisch.
"""

TAGE = [
    ("Samstag, 15.08.2026", "ARD", [
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
        ('06:55', 'Die Biene Maja', 'Die Sonnenfinsternis', 'Zeichentrick', 10, 3, 'a3', 55, 'Maja erlebt eine totale Sonnenfinsternis. Bei der unerwarteten Dunkelheit verirren sich drei kleine '),
        ('07:05', 'Bibi Blocksberg', 'Wo ist Kartoffelbrei?', 'Zeichentrick', 25, 3, 'a3', 55, 'Bibi war unartig und bekommt deshalb drei Tage Hexverbot. Das ist eine schwere Strafe für sie. Vater'),
        ('07:30', 'Bibi Blocksberg', 'Das Wettfliegen', 'Zeichentrick', 30, 3, 'a3', 55, 'Es gibt einen großen Flugwettbewerb in Neustadt. Für Bibi ist es selbstverständlich, dass sie daran '),
        ('08:00', 'Robin Hood - Schlitzohr von Sherwood', 'Der Fallensteller', 'Zeichentrick', 10, 6, 'a6', 55, 'Tuck gerät im Wald in eine Falle. Er sitzt im Käfig fest, und Robin schafft es nicht, ihn zu befreie'),
        ('08:10', 'Robin Hood - Schlitzohr von Sherwood', 'Sheriff Robin', 'Zeichentrick', 15, 6, 'a6', 55, 'Der Sheriff hat sich verletzt, und König Richard bittet Robin, ihn zu vertreten. Natürlich passt das'),
    ]),
    ("Samstag, 15.08.2026", "ProSieben Maxx", [
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
        ('23:50', 'Dragon Ball Super', 'Überschreite alle Grenzen! Goku gegen Gohan!', 'Anime', 25, 12, 'a10', 55, 'Durch Piccolos Training strotzt Son Gohan geradezu vor Selbstvertrauen. Siegessicher fordert er sein'),
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
    ("Samstag, 15.08.2026", "ORF 1", [
        ('06:46', 'Der gestiefelte Kater - Abenteuer in San Lorenzo', 'Der große Zauber', 'Serie', 23, 3, 'a3', 55, 'Mit Hut und Degen zieht der gestiefelte Kater durchs Land, immer auf der Suche nach einem neuen Aben'),
        ('07:09', 'Der gestiefelte Kater - Abenteuer in San Lorenzo', 'Der Schatz von San Losano', 'Serie', 22, 3, 'a3', 55, 'Mit Hut und Degen zieht der gestiefelte Kater durchs Land, immer auf der Suche nach einem neuen Aben'),
        ('07:31', 'Grizzy und die Lemminge', 'Die Eisparty', 'Zeichentrick', 8, 3, 'a3', 55, 'Es ist Hochsommer und brütend heiß. Im Fernsehen sieht Grizzy eine appetitanregende Werbung für Eisc'),
        ('07:39', 'Servus Kasperl', 'Kasperl & Strolchi: Die Zauberrose', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('08:04', 'Paw Patrol - Der Kinofilm', '', 'Zeichentrick', 76, 6, 'a6', 55, "Temporeiches, erstes Kinoabenteuer der beliebten Hunde-Stars der 'Paw Patrol'. Als Bürgermeister dro"),
    ]),
    ("Sonntag, 16.08.2026", "ARD", [
        ('05:30', 'HipHorses - Du und Dein Pferd', 'Zoe und ihre Voltigier-Crew', 'Vorlesen', 25, 3, 'a3', 55, 'Handstand und Spagat-Sprung auf dem Rücken eines Pferdes? Das ist für Zoe aus Delitzsch kein Problem'),
        ('05:55', '#WIR - Freundschaft grenzenlos', 'Showtanz: Mehr als Karneval', 'Vorlesen', 10, 3, 'a3', 55, 'Vorhang auf für die Showgirls Larissa und Jana. Die beiden besten Freundinnen aus Rheinland-Pfalz ke'),
        ('06:05', 'Tigerenten Club', 'Der Club zum Mitmachen - Spiele, Spaß und spannendes Wissen', 'Vorlesen', 60, 3, 'a3', 55, 'Kickboxen mit Jugend-Europameisterin Theresa Schnelle Kicks und klare Regeln! Jugend-Europameisterin'),
        ('07:05', 'Ein Sommer in Sommerby', '', 'Serie', 75, 3, 'a3', 55, 'Seit vielen Jahren lebt Inge allein in ihrem reetgedeckten Haus an der Schlei. Hier gibt es weder ei'),
        ('08:20', 'Die Sendung mit der Maus', '', 'Vorlesen', 30, 6, 'a6', 55, 'Lach- und Sachgeschichten, heute mit Stadtschafen beim Scheren, einem Lied von einem besonderen Cowb'),
    ]),
    ("Sonntag, 16.08.2026", "ZDF", [
        ('06:00', 'Die Werkel-Ferkel', 'Nacht der Sternschnuppen', 'Zeichentrick', 10, 3, 'a3', 55, 'Die Füchsin Fiona hat sich am Bein verletzt. Wie soll sie so auf den Berg wandern, um von dort in de'),
        ('06:10', 'Die Werkel-Ferkel', 'Treppe zum Mond', 'Zeichentrick', 15, 3, 'a3', 55, 'Der Wolf Wilf hätte gerne den Vollmond ganz nahe bei sich - und deshalb heult er ohrenbetäubend laut'),
        ('06:25', 'Sam & Julia im Mäusehaus', 'Mit Pauken und Trompeten', 'Zeichentrick', 5, 3, 'a3', 55, 'Die Mäuseband plant ein Konzert im Mäusehaus und ruft alle zum Mitspielen auf. Mitmachen kann jeder,'),
        ('06:30', 'Sam & Julia im Mäusehaus', 'Julia ist hingefallen', 'Zeichentrick', 10, 3, 'a3', 55, 'Julia rutscht aus und fällt hin. Sie verletzt sich nicht, aber weil sie über Schmerzen klagt, bekomm'),
        ('06:40', 'Sam & Julia im Mäusehaus', 'Der Vatertag', 'Zeichentrick', 5, 3, 'a3', 55, 'Alle Mäusekinder sind dabei, Vatertags-Geschenke für ihre Väter zu basteln. Nur Tonio, der gleich zw'),
        ('06:45', 'Pettersson und Findus', 'Armer Pettersson', 'Zeichentrick', 15, 3, 'a3', 55, 'Einen solch verregneten Tag hat es auf dem Hof schon lange nicht mehr gegeben. Pettersson möchte am '),
        ('07:00', 'Wickie und die starken Männer', 'Ylvi in Not', 'Zeichentrick', 10, 3, 'a3', 55, 'Wickie hat Geburtstag. Ylvi und Ylva wollen über den Klippen von Flake Beeren für einen leckeren Geb'),
        ('07:10', 'Wickie und die starken Männer', 'Olympische Spiele', 'Zeichentrick', 15, 3, 'a3', 55, 'Die Wikinger bringen das Olympische Feuer nach Spanien, wo sich Vertreter vieler Nationen treffen, u'),
        ('07:25', 'Bibi Blocksberg', 'Der Kobold aus dem Briefkasten', 'Zeichentrick', 25, 3, 'a3', 55, 'Bibi und ihr Vater Bernhard sind allein zu Hause. Als Bibi sich beim Frühstück verhext, landet statt'),
        ('07:50', 'Bibi und Tina', 'Der Hufschmied', 'Zeichentrick', 25, 3, 'a3', 55, 'Graf Falko von Falkenstein lässt sich zu einer riskanten Wette hinreißen. Dadurch stehen seine beste'),
        ('08:15', 'Löwenzahn', 'Detektive - Spurensuche in Bärstadt', 'Serie', 25, 6, 'a6', 55, 'Fritz Fuchs und David Paschulke nehmen die Ermittlungen auf: Millies größter Schatz, ihr Skizzenbuch'),
        ('08:40', 'Michel aus Lönneberga', 'Als Michel einen Freund gewann', 'Serie', 23, 6, 'a6', 55, 'Die neu gekaufte Sau wirft mitten in der Nacht ein Ferkel. Michel, der zufällig in den Stall kommt, '),
        ('15:30', 'plan b', 'Clever reisen - Trips vor der Haustür', 'Serie', 45, 6, 'a6', 55, 'Sommerzeit - Ferienzeit! Ob Surfen oder Städtetrip: Urlaub muss kein Vermögen kosten - dank innovati'),
    ]),
    ("Sonntag, 16.08.2026", "ProSieben Maxx", [
        ('04:10', 'One Piece', 'Unangreifbar! - Trebols schockierendes Geheimnis', 'Anime', 20, 12, 'a10', 55, 'Mit seiner Klebeschleuder gelingt es Trébol, Ruffy lahmzulegen. Um De Flamingos Sieg zu garantieren,'),
        ('04:30', 'One Piece', 'Der Ärger bricht aus - Ich werde alles auf mich nehmen!', 'Anime', 25, 12, 'a10', 55, 'Ruffy übergibt Law an seine Verbündeten, doch der lässt sich nicht auf den Handel ein. Außerdem wird'),
        ('04:55', 'Detektiv Conan', 'Wo ist Nintaro Shinmei? (1)', 'Anime', 20, 12, 'a10', 55, 'Fünf Personen stehen um einen in der Mitte liegenden toten Körper herum, als plötzlich ein Unbekannt'),
    ]),
    ("Sonntag, 16.08.2026", "NDR", [
        ('06:45', 'Edgar, das Super-Karibu', 'Bernhard lernt Rad fahren', 'Zeichentrick', 10, 3, 'a3', 55, 'Bernhard, das ungeschickte Eichhörnchen, träumt davon, Radfahren zu lernen, damit er mit Katja, der '),
        ('06:55', 'Edgar, das Super-Karibu', 'Der große Streit', 'Zeichentrick', 15, 3, 'a3', 55, 'Im Dorfcafé streiten sich die beiden Unzertrennlichen Bosse, der Igel, und Piet, der Esel, ohne Ende'),
    ]),
    ("Sonntag, 16.08.2026", "SWR", [
        ('11:00', 'Das doppelte Lottchen', '', 'Serie', 90, 6, 'a6', 55, 'Sonne, Wasser, Surfen - für die meisten Kinder ist das Ferienheim am Wolfgangsee ein Paradies, doch '),
    ]),
    ("Sonntag, 16.08.2026", "MDR", [
        ('15:50', 'Der Meisterdieb', '', 'Serie', 60, 6, 'a6', 55, 'Das Märchen der Brüder Grimm erzählt von einem jungen Mann, der als Junge von Zuhause weggelaufen wa'),
        ('16:50', 'Rotkäppchen', '', 'Serie', 70, 6, 'a6', 55, 'Rotkäppchen wird von der Mutter in den Wald geschickt zur Großmutter, die krank im Bett liegt. "Aber'),
        ('18:52', 'Unser Sandmännchen', '', 'Serie', 8, 3, 'a3', 55, 'Pitti schießt den Fußball in Schnatterinchens Primelbeet. Moppi meint: "Das gibt Ärger!", aber Pitti'),
    ]),
    ("Sonntag, 16.08.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Kallis Gute-Nacht-Geschichten: Kalli - Schnecke'),
    ]),
    ("Sonntag, 16.08.2026", "ORF 1", [
        ('06:00', 'Tom - Ein echter Freund', 'Tom in Istanbul', 'Zeichentrick', 24, 3, 'a3', 55, 'Rupert hat sich auf der Sightseeingtour durch Istanbul verletzt. Bösewicht Carter wittert seine groß'),
        ('06:24', 'Vegesaurier', 'Erbse in der Mitte', 'Zeichentrick', 6, 3, 'a3', 55, 'Ginger und die Erbs-Rex-Babys freuen sich auf ihr Lecker-Drops-Frühstück. Doch die Früchte wurden vo'),
        ('06:30', 'Servus Kasperl', 'Kasperl & Buffi: Buffikopf und Blumentopf', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('06:55', 'Vegesaurier', 'Blütenfest', 'Zeichentrick', 5, 3, 'a3', 55, 'Im Frühling werden die Broccolisaurier von ganz besonderen Blüten auf einem Baum angelockt. Doch ein'),
        ('07:00', 'Vegesaurier', 'Rennen ohne Regeln', 'Zeichentrick', 5, 3, 'a3', 55, 'Die jungen Vegesaurier machen regelmäßig Wettrennen und Ginger ruft ein Rennen ohne Regeln aus. Bald'),
        ('07:05', 'Bakabu', 'Aufräum-Lied', 'Vorlesen', 5, 3, 'a3', 55, "Hey, was ist da los? Ui, wie schaut's da aus? Wenn Dinge einfach herumliegen, herrscht meistens ein "),
        ('07:10', 'Knall genial', '', 'Wissen', 16, 3, 'a3', 55, 'Originelle Tipps und Tricks von Thomas Brezina und den Kids! Auch dieses Mal ist wieder für jeden Ge'),
        ('07:26', 'Der gestiefelte Kater - Abenteuer in San Lorenzo', 'Skelette in der Stadt', 'Serie', 24, 3, 'a3', 55, 'Mit Hut und Degen zieht der gestiefelte Kater durchs Land, immer auf der Suche nach einem neuen Aben'),
        ('07:50', 'Drunter & drüber mit Christoph Hirschler', 'Lachattacke mit Isabell Pannagl', 'Vorlesen', 16, 3, 'a3', 55, 'Heute wird es richtig lustig. Christoph Hirschler begrüßt die Kabarettistin Isabell Pannagl in seine'),
        ('08:06', 'Campsite', 'Ich kann nicht schwimmen', 'Jugendserie', 5, 10, 'a10', 55, 'Silje möchte mit ihrem Schlauchboot eine runde Paddeln gehen und lädt Thea ein, mitzukommen. Diese s'),
        ('08:11', 'Campsite', 'Ein zu heißer Sommertag', 'Jugendserie', 14, 10, 'a10', 55, 'An einem viel zu heißen Sommertag will Andrine ihren Schwarm Sebbe, Theo und Nura mit einer Bootsfah'),
        ('12:29', 'Der König der Löwen', '', 'Zeichentrick', 106, 6, 'a6', 55, "Herzerwärmende Neuverfilmung eines der erfolgreichsten Disney-Klassikers. Jon Favreau ('The Jungle B"),
    ]),
    ("Montag, 17.08.2026", "ZDF", [
        ('22:15', 'Memory - Sein letzter Auftrag', '', 'Serie', 25, 10, 'a10', 55, 'Schnell, leise, unauffällig und professionell: Alex Lewis ist ein Auftragskiller, der keine Spuren h'),
    ]),
    ("Montag, 17.08.2026", "RTLzwei", [
        ('17:08', 'Hartz Rot Gold', 'Einfach machen!', 'Serie', 61, 6, 'a6', 55, 'In Gelsenkirchen macht sich Rentnerin Elke (69) heute auf den Weg in den Stadtteil Bulmke-Hüllen. Do'),
    ]),
    ("Montag, 17.08.2026", "ProSieben Maxx", [
        ('16:40', 'Dr. STONE', 'Schöne Wissenschaft', 'Anime', 25, 12, 'a10', 55, 'Ginro und Suika versuchen heimlich, das mobile Labor von Bord des Schiffes zu schmuggeln, um es Senk'),
        ('17:05', 'Dragon Ball Super', 'Eine Tat des Grauens! Freezer verliert die Kontrolle!', 'Anime', 25, 12, 'a10', 55, 'Prompt ist Freezer von den Toten zurückgekehrt, wird er schon von Feinden umzingelt. Unzählige Auftr'),
        ('17:30', 'Detektiv Conan', 'Drei Tage mit Hattori Heiji (3)', 'Anime', 30, 12, 'a10', 55, 'Heiji nimmt Conan mit zu einer Versammlung der Oberschülerdetektive. Die jungen Ermittler sollen für'),
        ('18:00', 'One Piece', 'Gear 4 - Der phänomenale Boundman!', 'Anime', 25, 12, 'a10', 55, 'Ruffy aktiviert Gear 4, dessen Faustschlag De Flamingo aus der Stadt hinausbefördert. De Flamingo su'),
        ('18:25', 'One Piece', 'Ein massiver Gegenangriff - De Flamingos Erwachen!', 'Anime', 30, 12, 'a10', 55, 'Ruffy greift De Flamingo an, doch der Shichibukai blockiert die Attacke und reagiert mit einer verst'),
        ('18:55', 'Detektiv Conan', 'Angriff der Killerwespen', 'Anime', 25, 12, 'a10', 55, 'Conan, Ran und Kogoro werden in die Yamazaki-Residenz eingeladen. Als Conan dort ein Modell für eine'),
    ]),
    ("Montag, 17.08.2026", "WDR", [
        ('07:05', 'Wissen macht Ah!', 'Pännnnng', 'Vorlesen', 25, 3, 'a3', 55, 'Jeder Wurf ein Treffer! Über die fünf Fragen der heutigen Sendung entscheiden diesmal der Zufall und'),
        ('07:30', 'POV - Deine Geschichte zählt', '', 'Vorlesen', 10, 3, 'a3', 55, 'Leonie (16) fühlt sich in der Schule oft ausgeschlossen. Halt findet sie in Musik, Konzerten und Onl'),
        ('07:40', 'Campsite', 'Der Trampolin-Streit', 'Jugendserie', 5, 3, 'a3', 55, 'Nura, Thea und Theo wollen auf das begehrte Campingplatz-Trampolin, aber Andrine beansprucht es exkl'),
        ('07:45', 'Campsite', 'Es gibt Krieg', 'Jugendserie', 10, 3, 'a3', 55, 'Der Kampf um das Trampolin geht weiter. Die beiden gegnerischen Gruppen bekämpfen sich mit Wasserpis'),
        ('07:55', 'Campsite', 'Olsok', 'Jugendserie', 5, 3, 'a3', 55, 'Ronja und Anja bereiten am Feiertag zu Ehren des Heiligen Olav eine kleine Zeremonie vor. Ronja nimm'),
        ('08:00', 'Neue Geschichten vom Franz', '', 'Film', 70, 6, 'a6', 55, 'Franz steckt in der Zwickmühle: Seine beste Freundin Gabi und sein bester Freund Eberhard streiten s'),
    ]),
    ("Montag, 17.08.2026", "NDR", [
        ('04:15', 'Ostwind', '', 'Film', 100, 3, 'a3', 55, 'Kurz vor Schulferienbeginn steht bei Familie Schwarz die Polizei vor der Tür. Nicht nur, dass die Ve'),
    ]),
    ("Montag, 17.08.2026", "MDR", [
        ('07:05', 'Unterwegs in Sachsen-Anhalt', 'Urlaub auf dem Bauernhof', 'Serie', 30, 3, 'a3', 55, 'Zwischen Erholung und echter Hofarbeit: Urlaub auf dem Bauernhof kann vielfältig sein. Aber was habe'),
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'MiWaus Napf mit Katzenmilch ist leer und ihr Durst ist groß. Moppi schickt MiWau zum Milchregal, sch'),
    ]),
    ("Montag, 17.08.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Moppi und MiWau: Die Katzenmilch'),
    ]),
    ("Montag, 17.08.2026", "HR", [
        ('05:15', 'Schau in meine Welt', 'Cocos Welt. YouTuberin in London', 'Vorlesen', 25, 3, 'a3', 55, 'Coco (12) lebt in London und ist ein YouTube-Star. 100.000 Follower aus der ganzen Welt schauen ihre'),
        ('06:30', 'Leo da Vinci', 'Bianca die Furchtlose', 'Zeichentrick', 10, 3, 'a3', 55, 'Robert und Jack wollen Lisa erst freilassen, wenn Leo ihnen mehr über den Verbleib des legendären Ru'),
        ('06:40', 'Leo da Vinci', 'Die Panzerkutsche', 'Zeichentrick', 15, 3, 'a3', 55, 'Statt schnell nach Venedig zu reisen, um nach dem Rubin des Marco Polo zu suchen, beschließt Leo, se'),
    ]),
    ("Montag, 17.08.2026", "3sat", [
        ('13:15', 'Borkum ... mit Judith Rakers', '', 'Serie', 45, 6, 'a6', 55, 'Judith Rakers entdeckt die größte der Ostfriesischen Inseln durch die Menschen, die dort entweder le'),
    ]),
    ("Montag, 17.08.2026", "ORF 1", [
        ('06:00', 'Mister Paper', 'Mister Paper hat Geburtstag', 'Zeichentrick', 5, 3, 'a3', 55, 'Mister Paper hat Geburtstag! Zur Feier des Tages möchte er ein großes Fest geben. Dekoration und Tor'),
        ('06:05', 'Wickie und die starken Männer', 'Die Wasserleitung', 'Zeichentrick', 25, 3, 'a3', 55, 'Der Steuereintreiber kommt mit seinem schwerbewaffneten Gefolge nach Flake. Seine Übermacht ist so g'),
        ('06:30', 'Servus Kasperl', 'Kasperl & Leopold: Das große Durcheinander', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('06:55', 'Die Jagd nach dem Kju Wang', 'Notlandung im Schnee', 'Zeichentrick', 25, 3, 'a3', 55, 'Der Herzog muss zu einer internationalen Konferenz nach Wien. Ardelia will ihn mit mehreren Schrankk'),
        ('07:40', 'Garfield', 'Die Glitzer-Schlucht - Teil 2', 'Zeichentrick', 10, 3, 'a3', 55, 'Sheriff Jon macht sich auf die Suche nach der Schnurrbartbande, die ihr Unheil in der Stadt treibt. '),
        ('07:50', 'Garfield', 'Die Glitzer-Schlucht - Teil 3', 'Zeichentrick', 10, 3, 'a3', 55, 'Die Dreharbeiten des Westernfilms gehen fleißig weiter und Garfield findet sich bei einem Duell mit '),
    ]),
    ("Montag, 17.08.2026", "SRF 1", [
        ('17:30', 'BooSnoo! - Redli', '', 'Zeichentrick', 10, 6, 'a6', 55, 'BooSnoo, der rote Ball, geht auf Reisen. Fliessende Bewegungen, sanfte Rhythmen - BooSnoo beruhigt, '),
    ]),
]
