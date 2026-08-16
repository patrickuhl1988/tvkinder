# -*- coding: utf-8 -*-
"""Kindersendungen der Vollprogramme.

Erzeugt von scan_kinder.py aus tv.de am 16.08.2026. Auswahl nach Kategorie,
bekannten Titeln und Beschreibung; Alterswerte heuristisch.
"""

TAGE = [
    ("Sonntag, 16.08.2026", "ARD", [
        ('06:05', 'Tigerenten Club', 'Der Club zum Mitmachen - Spiele, Spaß und spannendes Wissen', 'Vorlesen', 60, 3, 'a3', 55, 'Kickboxen mit Jugend-Europameisterin Theresa Schnelle Kicks und klare Regeln! Jugend-Europameisterin'),
        ('07:05', 'Ein Sommer in Sommerby', '', 'Serie', 75, 3, 'a3', 55, 'Seit vielen Jahren lebt Inge allein in ihrem reetgedeckten Haus an der Schlei. Hier gibt es weder ei'),
        ('08:20', 'Die Sendung mit der Maus', '', 'Vorlesen', 30, 6, 'a6', 55, 'Lach- und Sachgeschichten, heute mit Stadtschafen beim Scheren, einem Lied von einem besonderen Cowb'),
    ]),
    ("Sonntag, 16.08.2026", "ZDF", [
        ('07:00', 'Wickie und die starken Männer', 'Ylvi in Not', 'Zeichentrick', 10, 3, 'a3', 55, 'Wickie hat Geburtstag. Ylvi und Ylva wollen über den Klippen von Flake Beeren für einen leckeren Geb'),
        ('07:10', 'Wickie und die starken Männer', 'Olympische Spiele', 'Zeichentrick', 15, 3, 'a3', 55, 'Die Wikinger bringen das Olympische Feuer nach Spanien, wo sich Vertreter vieler Nationen treffen, u'),
        ('07:25', 'Bibi Blocksberg', 'Der Kobold aus dem Briefkasten', 'Zeichentrick', 25, 3, 'a3', 55, 'Bibi und ihr Vater Bernhard sind allein zu Hause. Als Bibi sich beim Frühstück verhext, landet statt'),
        ('07:50', 'Bibi und Tina', 'Der Hufschmied', 'Zeichentrick', 25, 3, 'a3', 55, 'Graf Falko von Falkenstein lässt sich zu einer riskanten Wette hinreißen. Dadurch stehen seine beste'),
        ('08:15', 'Löwenzahn', 'Detektive - Spurensuche in Bärstadt', 'Serie', 25, 6, 'a6', 55, 'Fritz Fuchs und David Paschulke nehmen die Ermittlungen auf: Millies größter Schatz, ihr Skizzenbuch'),
        ('08:40', 'Michel aus Lönneberga', 'Als Michel einen Freund gewann', 'Serie', 23, 6, 'a6', 55, 'Die neu gekaufte Sau wirft mitten in der Nacht ein Ferkel. Michel, der zufällig in den Stall kommt, '),
        ('15:30', 'plan b', 'Clever reisen - Trips vor der Haustür', 'Wissen', 45, 6, 'a6', 55, 'Sommerzeit - Ferienzeit! Ob Surfen oder Städtetrip: Urlaub muss kein Vermögen kosten - dank innovati'),
    ]),
    ("Sonntag, 16.08.2026", "NDR", [
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
    ("Dienstag, 18.08.2026", "ProSieben Maxx", [
        ('16:45', 'Dr. STONE', 'Science Wars', 'Anime', 25, 12, 'a10', 55, 'Senku stellt einen Ohrring her, den er nutzt, um mit Kohaku zu kommunizieren. Diese schleicht sich m'),
        ('17:10', 'Dragon Ball Super', 'Die Zeit ist gekommen! Das Schicksal der Universen steht auf dem Spiel', 'Anime', 25, 12, 'a10', 55, 'Endlich ist es so weit: Das große Turnier beginnt. Die Kämpfer der acht teilnehmenden Universen vers'),
        ('17:35', 'Detektiv Conan', 'Drei Tage mit Hattori Heiji (4)', 'Anime', 30, 12, 'a10', 55, 'Conan, Heiji und Saguru müssen den Mord an dem Oberschülerdetektiv Junya Tokitsu aufklären. Die jung'),
        ('18:05', 'One Piece', 'Ruffys Trumpf - Die Leo-Bazooka!', 'Anime', 25, 12, 'a10', 55, 'De Flamingo hat die Oberhand im Kampf gegen Ruffy, doch dieser holt zu einem massiven Gegenschlag au'),
        ('18:30', 'One Piece', 'Der König des Drachenfeuers - Beschützt Ruffys Leben!', 'Anime', 25, 12, 'a10', 55, 'Gatz rückt mit weiteren Gladiatoren an, um Ruffys Leben zu beschützen und De Flamingo abzulenken. In'),
        ('18:55', 'Detektiv Conan', 'Das versiegelte Badezimmer (1)', 'Anime', 25, 12, 'a10', 55, 'Mina hilft ihrer Schwester Masayo beim Einkaufen, da diese gerade ihren Auszug vorbereitet und schon'),
    ]),
    ("Dienstag, 18.08.2026", "WDR", [
        ('07:35', 'Campsite', 'Siljes Spiel', 'Jugendserie', 5, 3, 'a3', 55, 'Silje ist stolz auf ihre weibliche Figur. In der Hoffnung, bei den Jungs Eindruck zu machen, schlägt'),
        ('07:40', 'Campsite', 'Ein großer Fremder', 'Jugendserie', 5, 3, 'a3', 55, 'Andrine ist eifersüchtig, weil Sebbe sich lieber mit Silje als mit ihr trifft. Um Silje von ihm wegz'),
        ('07:45', 'Campsite', 'Psychopath?', 'Jugendserie', 10, 3, 'a3', 55, 'Emmi ist empört, als Anja ihr erzählt, dass Max sie "süß" genannt hat. Für Emmi ist das sexistische '),
        ('07:55', 'Das Camp in der Wildnis', 'Viel Gegenwind', 'Vorlesen', 25, 3, 'a3', 55, 'Nach einer anstrengenden Nacht im Zelt mitten in der norwegischen Wildnis verlassen Niklas beim Kaja'),
        ('08:20', 'Das Camp in der Wildnis', 'Erste Liebe', 'Vorlesen', 25, 6, 'a6', 55, 'Kaja ist frisch verliebt und bringt ihren neuen Freund beim Tanzkurs zum Schwitzen. Der hat für Nach'),
    ]),
    ("Dienstag, 18.08.2026", "NDR", [
        ('06:00', 'Sesamstraße', '', 'Vorlesen', 20, 3, 'a3', 55, 'Bert mischt Farben: aus Rot und Blau wird Violett, aus Gelb und Rot wird Orange. Ernie soll herausfi'),
        ('06:20', 'Schloss Einstein - Erfurt', 'Verfolgungsjagd', 'Jugendserie', 25, 10, 'a10', 55, 'Plötzlich taucht das letzte Kartenstück auf! Es zu bekommen, endet in einer wilden Verfolgungsjagd. '),
        ('06:45', 'Schloss Einstein - Erfurt', 'Alle für Einstein', 'Jugendserie', 25, 10, 'a10', 55, 'Reena versucht, Charlotte in Sachen Share Space mit einem Coaching zu helfen. Ihre Methode führt jed'),
        ('07:10', 'Die Pfefferkörner', 'Fakt oder Fake', 'Serie', 30, 10, 'a10', 55, 'Moritz hilft geistesgegenwärtig und mit viel Zivilcourage einem Obdachlosen, der von zwei jungen Män'),
        ('07:40', 'Die Pfefferkörner', 'Entführt', 'Serie', 35, 10, 'a10', 55, 'Eine Entführung am helllichten Tag mitten in der Stadt? Amy behauptet, gesehen zu haben, wie ein ält'),
    ]),
    ("Dienstag, 18.08.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Die Biene auf meiner Schmusedecke hat ein Problem: Ihr Flügel hat ein Riss und sie kann nicht mehr f'),
    ]),
    ("Dienstag, 18.08.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Meine Schmusedecke: Die Biene'),
    ]),
    ("Dienstag, 18.08.2026", "HR", [
        ('06:25', 'Leo da Vinci', 'Zwei entscheidende Seiten', 'Zeichentrick', 10, 3, 'a3', 55, 'Auf dem Weg nach Venedig kommen Leo und seine Freunde an einem Bauernhof vorbei. Die beiden Kinder F'),
        ('06:35', 'Leo da Vinci', 'Die Wahrsagerin', 'Zeichentrick', 15, 3, 'a3', 55, 'Leo muss dringend eine Nachricht nach Venedig schicken. Er entdeckt Brieftauben der Medici, die sich'),
    ]),
    ("Dienstag, 18.08.2026", "ORF 1", [
        ('06:00', 'Mister Paper', 'Mister Paper lernt fliegen', 'Zeichentrick', 5, 3, 'a3', 55, 'Mister Paper hat eine neue Leidenschaft für sich entdeckt: das Fliegen! Er möchte am liebsten schwer'),
        ('06:05', 'Wickie und die starken Männer', 'Die freiwillige Feuerwehr', 'Zeichentrick', 25, 3, 'a3', 55, 'In Flake ist ein großer Brand ausgebrochen, das ganze Dorf ist in Gefahr. Die Wikinger wissen keinen'),
        ('06:30', 'Servus Kasperl', 'Kasperl & Hopsi: Das hinterlistige Pumpelstilzchen', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('06:55', 'Die Jagd nach dem Kju Wang', 'Die Uhr', 'Zeichentrick', 25, 3, 'a3', 55, 'Yagor macht sich die Dankbarkeit des Volkes von Zinzania zunutze und schickt dem Herzog in des Volke'),
        ('07:40', 'Garfield', 'Die Glitzer-Schlucht - Teil 4', 'Zeichentrick', 10, 3, 'a3', 55, 'Garfields Frau wird vom Oberhaupt der Schnurrbartbande entführt. Als Star des Western-Films und Hilf'),
        ('07:50', 'Garfield', 'Die Glitzer-Schlucht - Teil 5', 'Zeichentrick', 10, 3, 'a3', 55, 'Der Regisseur Nermal beschließt kurzfristig, sich selbst mit einer Hauptrolle in den Film reinzuschr'),
    ]),
    ("Dienstag, 18.08.2026", "SRF 1", [
        ('17:30', 'BooSnoo! - Musig', '', 'Zeichentrick', 10, 6, 'a6', 55, 'BooSnoo, der rote Ball, geht auf Reisen. Fliessende Bewegungen, sanfte Rhythmen - BooSnoo beruhigt, '),
    ]),
]
