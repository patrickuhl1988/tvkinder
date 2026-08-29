# -*- coding: utf-8 -*-
"""Kindersendungen der Vollprogramme.

Erzeugt von scan_kinder.py aus tv.de am 29.08.2026. Auswahl nach Kategorie,
bekannten Titeln und Beschreibung; Alterswerte heuristisch.
"""

TAGE = [
    ("Samstag, 29.08.2026", "ARD", [
        ('14:00', 'Im Fluss des Lebens', '', 'Film', 90, 6, 'a6', 55, 'Die Berliner Schriftstellerin Agnes Berg (Ruth Maria Kubitschek) erhält einen Literaturpreis für ihr'),
    ]),
    ("Samstag, 29.08.2026", "SAT.1", [
        ('20:15', 'Matilda', '', 'Film', 125, 10, 'a10', 55, 'Kaum zu glauben, dass solche Eltern eine solche Tochter haben: Die kleine Matilda ist ein telekineti'),
    ]),
    ("Samstag, 29.08.2026", "ProSieben Maxx", [
        ('13:10', 'Voltron: Legendärer Verteidiger', 'Unbekannte Regionen', 'Zeichentrick', 30, 6, 'a6', 55, 'Während Honerva ihren Plan weiter vorantreibt, spaltet sich die Voltron-Koalition, um sie aufzuhalte'),
        ('13:40', 'She-Ra und die Rebellen-Prinzessinnen', 'Eine heilige Verbindung', 'Zeichentrick', 20, 6, 'a6', 55, 'Bow und Glimmer wollen herausfinden, was mit Entrapta passiert ist. Dabei nehmen sie aus Versehen Ca'),
    ]),
    ("Samstag, 29.08.2026", "BR", [
        ('12:00', 'Dann kam Lucy', '', 'Serie', 90, 6, 'a6', 55, 'Zehn Jahre ist es her, seit die Pferdezüchterin Saskia ihre Jugendfreundin Andrea zuletzt gesehen ha'),
    ]),
    ("Samstag, 29.08.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Herr Fuchs borgt sich den Sonnenschirm der Elster. Diese ist verwundert, denn der Sommer ist vorüber'),
    ]),
    ("Samstag, 29.08.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Fuchs und Elster: Herr Fuchs borgt einen Sonnenschirm'),
    ]),
    ("Samstag, 29.08.2026", "SRF 1", [
        ('17:40', 'Minisguard', 'Wie macht man eigentlich Glace?', 'Serie', 20, 6, 'a6', 55, 'An einem heissen Sommertag gibt es kaum etwas Besseres als eine feine Glace. Aber wie wird Glace eig'),
    ]),
    ("Sonntag, 30.08.2026", "ARD", [
        ('05:30', 'HipHorses - Du und Dein Pferd', 'Annika und Spring-Pony Oh-Fiona', 'Vorlesen', 25, 3, 'a3', 55, 'Annika aus Schönebeck bereitet sich auf das große Springturnier ihres Heimatvereins Westeregeln vor.'),
        ('05:55', 'Dein Traumjob? Zimmermann!', '', 'Vorlesen', 15, 3, 'a3', 55, 'Theo ist zehn Jahre alt, spielt gern Fußball und zeichnet gern. Außerdem steht er total auf "Sägen".'),
        ('06:10', 'Tigerenten Club', 'Der Club zum Mitmachen - Spiele, Spaß und spannendes Wissen', 'Vorlesen', 55, 3, 'a3', 55, '"krass nass!" - Das ultimative Sommer-Action-Highlight ist zurück Es wird krass nass! Spektakuläre H'),
        ('08:30', 'Alina', 'Die Pferdeflüsterin', 'Jugendserie', 60, 10, 'a10', 55, 'Alina ist verzweifelt, weil Silverado kaum Fortschritte macht. Als Patrick ihr von der Pferdeflüster'),
        ('09:30', 'Die Sendung mit der Maus', '', 'Vorlesen', 30, 6, 'a6', 55, 'Lach- und Sachgeschichten, heute mit Johannes in einem sparsamen Dorf, Trudes Tier beim Fußball-Trai'),
    ]),
    ("Sonntag, 30.08.2026", "ZDF", [
        ('06:00', 'Die Werkel-Ferkel', 'Der tiefgekühlte Wilf', 'Zeichentrick', 10, 3, 'a3', 55, 'Wegen der Hitze bauen die Werkel-Ferkel eine Eismaschine für Fred und Dana. Heimlich verfolgt Wilf d'),
        ('06:10', 'Die Werkel-Ferkel', 'Der Flatter-Schnappschuss', 'Zeichentrick', 15, 3, 'a3', 55, 'Einen Schnappschuss von einem bunten Schmetterling für Cherry machen? Das sollte doch eigentlich kei'),
        ('06:25', 'Sam & Julia im Mäusehaus', 'Das große Fondue-Fest', 'Zeichentrick', 5, 3, 'a3', 55, 'Heute ist der Jahrestag der Gründung des Mäusehauses. Das wird wie jedes Jahr mit einem großen Fondu'),
        ('06:30', 'Sam & Julia im Mäusehaus', 'Die maskierte Maus', 'Zeichentrick', 10, 3, 'a3', 55, 'Sam, Tonio und Ella sind begeisterte Fans der "Maskierten Maus", einer Heldenfigur aus dem gleichnam'),
        ('06:40', 'Sam & Julia im Mäusehaus', 'Ich bin schon groß', 'Zeichentrick', 5, 3, 'a3', 55, 'Sams kleiner Bruder Ben ist frustriert, weil er noch so klein ist und vieles noch nicht kann. Zusamm'),
        ('06:45', 'Pettersson und Findus', 'Aufruhr im Gemüsebeet', 'Zeichentrick', 15, 3, 'a3', 55, 'Pettersson glaubt, es sei doch eigentlich ganz einfach, ein Gemüsebeet einzusäen. Doch da liegt er o'),
        ('07:00', 'Wickie und die starken Männer', 'Svens Schiffbruch', 'Zeichentrick', 10, 3, 'a3', 55, 'Svens Boot ist mit Reichtümern so beladen, dass das Schiff auseinanderbricht und schließlich auf den'),
        ('07:10', 'Wickie und die starken Männer', 'Pirat Gilby', 'Zeichentrick', 15, 3, 'a3', 55, 'Wegen seiner bösen Streiche haben weder Halvar noch seine Leute Lust, Gilby mit auf große Fahrt zu n'),
        ('07:25', 'Bibi Blocksberg', 'Die Jagd nach dem Goldhexstein', 'Zeichentrick', 25, 3, 'a3', 55, 'Bibi übt Lichthexereien für die Walpurgisnacht. Der Höhepunkt ist eine Goldlicht-Hexerei der Althexe'),
        ('07:50', 'Bibi und Tina', 'Sorge um Cleopatra', 'Zeichentrick', 25, 3, 'a3', 55, 'Cleopatra, das Lieblingspferd des Grafen, ist verstört und lässt keinen mehr an sich heran. Bibi und'),
        ('08:15', 'Löwenzahn', 'Wunder des Lebens - Mit Liebe gemacht', 'Serie', 25, 6, 'a6', 55, 'Wie genau entstehen eigentlich Babys? Fritz Fuchs erforscht die folgenreiche Begegnung von Spermien '),
        ('08:40', 'Michel aus Lönneberga', 'Als Michel ein Held wurde', 'Serie', 23, 6, 'a6', 55, 'Knecht Alfred verletzt sich beim Schnitzen den Finger. Seine Schmerzen werden immer stärker. Die Swe'),
    ]),
    ("Sonntag, 30.08.2026", "SAT.1", [
        ('17:00', 'Matilda', '', 'Film', 115, 6, 'a6', 55, 'Kaum zu glauben, dass solche Eltern eine solche Tochter haben: Die kleine Matilda ist ein telekineti'),
    ]),
    ("Sonntag, 30.08.2026", "ProSieben Maxx", [
        ('04:10', 'One Piece', 'Das Bündnis der Brüder! - Die Geschichte von Ruffys und Sabos Wiederse', 'Anime', 25, 12, 'a10', 55, 'Nachdem er von Aces Tod erfahren hatte, gewann Sabo sein Gehör zurück. Zwei Jahre später besuchte er'),
        ('04:35', 'One Piece', 'Die stärkste Kreatur aller Zeiten! - Kaido der hundert Bestien', 'Anime', 20, 12, 'a10', 55, 'Kaido der hundert Bestien landet aus heiterem Himmel auf der Basis und verkündet, er werde einen Kri'),
        ('04:55', 'One Piece', 'Fujitoras nächster Schritt - Die vollständige Belagerung der Strohhüte', 'Anime', 25, 12, 'a10', 55, 'Fujitora will einen Würfel über das Schicksal von Ruffy und Law entscheiden lassen. Das Mysterium um'),
    ]),
    ("Sonntag, 30.08.2026", "WDR", [
        ('17:20', 'Wuppertal und die einzigartige Schwebebahn', '', 'Wissen', 30, 6, 'a6', 55, 'Einmal im Leben durch Wuppertal schweben! Die Wuppertaler Schwebebahn feiert ihren 125. Geburtstag -'),
    ]),
    ("Sonntag, 30.08.2026", "NDR", [
        ('04:35', 'Apple Hills', 'Cousin Walters Spielpark', 'Zeichentrick', 5, 3, 'a3', 55, 'Ein Tornado hat einen Container auf das Grundstück von Cousin Walter geworfen, und er sieht darin ei'),
        ('04:40', 'Apple Hills', 'Eine Trafalgar-Pizza, bitte!', 'Zeichentrick', 10, 3, 'a3', 55, 'In Onkel Knuts Pizzeria entdeckt Trafalgar, dass jemand eine Pizza nach Frank benannt hat. Trafalgar'),
        ('04:50', 'Apple Hills', 'Der Helmfluencer', 'Zeichentrick', 5, 3, 'a3', 55, 'Die Bürgermeisterin möchte, dass die Kinder in Apple Hills sicherer sind. Deshalb zwingt sie Frank, '),
        ('04:55', 'Apple Hills', 'Schneeball', 'Zeichentrick', 5, 3, 'a3', 55, 'Trafalgar und Powder haben ein Zelt aufgestellt, in dem sie die Zukunft anderer Menschen vorhersagen'),
        ('05:00', 'Apple Hills', 'Ballon-Man', 'Zeichentrick', 10, 3, 'a3', 55, 'Trafalgar lädt sich mit statischer Elektrizität auf und verwandelt sich in den Superhelden Ballon-Ma'),
        ('05:10', 'Apple Hills', 'Ironie ist nicht witzig!', 'Zeichentrick', 5, 3, 'a3', 55, 'Trafalgar und Powder lernen etwas über Ironie und können nicht mehr aufhören, ironisch zu sein. Der '),
        ('05:15', 'Apple Hills', 'Pulvers Präsentation', 'Zeichentrick', 5, 3, 'a3', 55, 'Alle Kinder müssen in der Schule eine Präsentation halten. Bald ist Powder an der Reihe. Die anderen'),
        ('05:20', 'Apple Hills', 'Süßigkeiten-Suppe', 'Zeichentrick', 10, 3, 'a3', 55, 'Es ist Wissenschaftstag in der Schule. Anna-Lise möchte ihr großes Idol, Professor Scharfsinn, beein'),
        ('05:30', 'Apple Hills', 'Trafalgars Entenkostüm', 'Zeichentrick', 5, 3, 'a3', 55, 'Die Klasse bekommt Besuch vom Tierfreunde-Verein, der einen Kostümwettbewerb organisiert. Trafalgar '),
        ('05:35', 'Apple Hills', 'Außerirdische im Pilzwald', 'Zeichentrick', 5, 3, 'a3', 55, 'Cousin Walter hat sich im Pilzwald verirrt! Trafalgar, Powder und Lizzie suchen ihn im Wald, wo sie '),
        ('05:40', 'Apple Hills', 'Der Trafalgar-Platz', 'Zeichentrick', 5, 3, 'a3', 55, 'Herr Zement erhält den Auftrag, die neue Touristenattraktion von Apple Hills zu bauen: den Herrn-Zem'),
        ('05:45', 'Apple Hills', 'Ein Tag mit Stiefvater', 'Zeichentrick', 10, 3, 'a3', 55, 'Powders Stiefvater muss sich um Trafalgar und Powder kümmern und möchte sie beeindrucken. Er lehrt s'),
        ('05:55', 'Apple Hills', 'Die Spielzeugkrise', 'Zeichentrick', 5, 3, 'a3', 55, 'Der Spielzeugladen in Apple Hills hat einen Wasserschaden erlitten und ist geschlossen, also beginne'),
        ('06:00', 'Apple Hills', 'Der liebenswerte Herr Zement', 'Zeichentrick', 5, 3, 'a3', 55, 'Ein harter Schlag auf den Kopf verändert Herrn Zement völlig, plötzlich ist er sehr freundlich. Er b'),
        ('06:05', 'Apple Hills', 'Das Traumspiel', 'Zeichentrick', 5, 3, 'a3', 55, 'Die Kinder haben eine wunderbare Vertretungslehrerin in der Schule, Frau Lax, die ihnen den besten S'),
        ('06:10', 'Apple Hills', 'Raketenwissenschaft', 'Zeichentrick', 10, 3, 'a3', 55, 'Eva wird große Schwester und plant eine Gender-Reveal-Party. Ganz Apple Hills ist in eine hitzige Di'),
        ('06:20', 'Apple Hills', 'Der Pfadfinder-Ausflug', 'Zeichentrick', 5, 3, 'a3', 55, 'Die Kinder aus Apple Hills sind mit der Pfadfindergruppe zum Zelten gefahren und werden die Nacht un'),
        ('06:25', 'Apple Hills', 'Stiefvaters Siegerjacke', 'Zeichentrick', 5, 3, 'a3', 55, 'Powders Stiefvater glaubt, dass er in seinem Leben nichts erreicht ha. Er beschließt, am Radrennen "'),
        ('06:30', 'Apple Hills', 'Bürgermeisterwahlen', 'Zeichentrick', 10, 3, 'a3', 55, 'Der Bürgermeisterin verlässt Apple Hills und ruft eine Neuwahl aus. Herr Zement tritt schnell als Bü'),
        ('06:40', 'Apple Hills', 'Neutags-Fest', 'Zeichentrick', 5, 3, 'a3', 55, 'Trafalgar und Powder verbringen mit dem lustigen Onkel Knut den besten Silvesterabend aller Zeiten. '),
        ('06:45', 'Edgar, das Super-Karibu', 'Super-Edgar außer Atem', 'Zeichentrick', 10, 3, 'a3', 55, 'Edgar, das Super-Karibu und Katja, die Katze, die ständig herumfaucht, versuchen die Bewohner des St'),
        ('06:55', 'Edgar, das Super-Karibu', 'Das rätselhafte Küsschen-Küsschen', 'Zeichentrick', 15, 3, 'a3', 55, 'Es ist Valentinstag in Windhausen und alle Einwohner erhalten hübsche Liebeserklärungen, die mit "Kü'),
    ]),
    ("Sonntag, 30.08.2026", "BR", [
        ('09:20', 'Die Galoschen des Glücks', '', 'Serie', 60, 6, 'a6', 55, 'Großherzogin Ottilie und ihre Diener stecken mitten in den Vorbereitungen des Geburtstags von Prinze'),
    ]),
    ("Sonntag, 30.08.2026", "MDR", [
        ('15:30', 'Hans Röckle und der Teufel', '', 'Serie', 75, 6, 'a6', 55, 'Dem Puppenspieler und Erfinder Hans Röckle erscheint der Teufel und bietet ihm einen Pakt an. Röckle'),
        ('16:45', 'Das Mädchen auf dem Besenstiel', '', 'Serie', 75, 6, 'a6', 55, 'Hexenschülerin Saxana muss 300 Jahre nachsitzen und sucht nach Abwechslung. Im Zauberlexikon stößt s'),
        ('18:52', 'Unser Sandmännchen', '', 'Serie', 8, 3, 'a3', 55, 'Pitti und Moppi spielen Feuerwehr. Rasen mit dem Handwagen quer über die Gartenbeete und stoßen alle'),
    ]),
    ("Sonntag, 30.08.2026", "RBB", [
        ('09:00', 'Das blaue Licht', '', 'Serie', 80, 6, 'a6', 55, 'Der Bauer Hans ist als Soldat in den Krieg gezogen. Zurückgekehrt und von seinem König um den Sold b'),
        ('10:20', 'Der Teufel vom Mühlenberg', '', 'Serie', 80, 6, 'a6', 55, 'Eine alte Sage berichtet, dass vor vielen 100 Jahren im Harz in einer dunklen Schlucht drei Waldgeis'),
        ('11:40', 'Die Gänsemagd', '', 'Serie', 60, 6, 'a6', 55, 'Prinzessin Elisabeth ist schon seit vielen Jahren dem Prinzen Leopold versprochen. Auf den Weg zur V'),
        ('13:50', 'Der Froschkönig', '', 'Serie', 65, 6, 'a6', 55, 'Der schönen Prinzessin fällt eines Tages beim Spielen ihre Goldkugel in den Brunnen. Traurig über de'),
        ('14:55', 'Die Gänseprinzessin', '', 'Serie', 60, 6, 'a6', 55, 'Nach Motiven der Brüder Grimm erzählt das Märchen die Geschichte eines Königreiches im Ausnahmezusta'),
        ('16:55', 'König Drosselbart', '', 'Serie', 58, 6, 'a6', 55, 'Es war einmal die stolze Prinzessin Isabella von Geranien, die war schön, aber hochmütig. Als ihr Va'),
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Kallis Gute-Nacht-Geschichten: Super-Kalli'),
    ]),
    ("Sonntag, 30.08.2026", "3sat", [
        ('17:15', 'Ein Schloss am Wörthersee - Der Film', '', 'Film', 80, 6, 'a6', 55, 'Der charmante Lennie Berger hat von seinem Onkel das Schlosshotel Velden geerbt und will es auf Vord'),
    ]),
    ("Sonntag, 30.08.2026", "arte", [
        ('04:40', 'Athleticus', 'Marathonlauf', 'Zeichentrick', 35, 3, 'a3', 55, 'Die dritte Staffel des Kurzprogramms wirft einen humorvollen Blick auf unsere Gesellschaft und die R'),
    ]),
    ("Sonntag, 30.08.2026", "ORF 1", [
        ('06:00', 'Tom - Ein echter Freund', 'Tom in Südafrika', 'Zeichentrick', 24, 3, 'a3', 55, 'Rupert ist von seinem verstorbenen Onkel Rufus als Alleinerbe eingesetzt worden. Gemeinsam mit Tom u'),
        ('06:24', 'Vegesaurier', 'Was kleine Kokosnüsse brauchen', 'Zeichentrick', 5, 3, 'a3', 55, 'Ginger und die Erbs-Rexe befreien süße Kokosnussodon-Babys, die eingesperrt sind. Doch bald stellt s'),
        ('06:29', 'Servus Kasperl', 'Kasperl & Hopsi: Der kichernde Baum', 'Serie', 24, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('06:53', 'Vegesaurier', 'Keinen Schritt weiter', 'Zeichentrick', 5, 3, 'a3', 55, 'Ginger und die Erbs-Rexe toben sich in der Winterlandschaft aus, als sie plötzlich auf ein kleines K'),
        ('06:58', 'Vegesaurier', 'Erbs mit Hicks', 'Zeichentrick', 5, 3, 'a3', 55, 'Ein Erbs-Rex-Baby nach dem anderen bekommt plötzlich Schluckauf. Ginger versucht den kleinen Erbs-Re'),
        ('07:03', 'Bakabu', 'Die Weltraumrakete', 'Vorlesen', 5, 3, 'a3', 55, 'Bakabu und seine Freunde fliegen mit einer Rakete in den Weltraum, dann können sie von oben auf die '),
        ('07:08', 'Knall genial', '', 'Wissen', 18, 3, 'a3', 55, 'Originelle Tipps und Tricks von Thomas Brezina und den Kids! In dieser Folge präsentieren Thomas und'),
        ('07:26', 'Der gestiefelte Kater - Abenteuer in San Lorenzo', 'Auf der Jagd', 'Serie', 22, 3, 'a3', 55, 'Mit Hut und Degen zieht der gestiefelte Kater durchs Land, immer auf der Suche nach einem neuen Aben'),
        ('07:48', 'Drunter & drüber mit Christoph Hirschler', 'Bauchreden mit Tricky Niki', 'Vorlesen', 17, 3, 'a3', 55, 'Können Socken sprechen? Mit Christophs heutigem Gast Tricky Niki geht das. Er ist Zauberer und Bauch'),
        ('08:05', 'Campsite', 'Olsok', 'Jugendserie', 7, 10, 'a10', 55, 'Die Schwestern Ronja und Anja wollen wie jedes Jahr zum Olsok-Tag Olav dem Heiligen gedenken, indem '),
        ('08:12', 'Campsite', 'Siljes Spiel', 'Jugendserie', 6, 10, 'a10', 55, 'Siljes wird langsam erwachsen und sie ist total stolz darauf, dass ihre Figur immer weiblicher wird.'),
        ('08:18', 'Campsite', 'Ein großer Fremder', 'Jugendserie', 7, 10, 'a10', 55, 'Andrine und Silje stehen beide auf Sebbe. Als Andrine Sebbe und Silje sieht, wie sie an einem Tisch '),
        ('08:25', 'Dragons - Die Wächter von Berk', 'Die Aal-Insel', 'Zeichentrick', 22, 6, 'a6', 55, 'Auf Berk sind die Aal-Pocken ausgebrochen. Die Drachenreiter müssen losziehen und Zutaten für einen '),
        ('08:47', 'Was geht?', 'Geschichten', 'Wissen', 14, 6, 'a6', 55, 'Manche Geschichten lassen uns abtauchen bis wir Raum und Zeitgefühl verlieren. Woher kommt das und h'),
        ('09:01', 'Mini Spezial', 'Schrottplatz', 'Vorlesen', 5, 6, 'a6', 55, 'Bananenschalen kommen in den Biomüll, leere Flaschen ins Altglas - was aber passiert mit alten, kapu'),
        ('09:06', 'Garfield', 'Maus TV', 'Zeichentrick', 13, 6, 'a6', 55, 'Die zwei Mäuse, die in Jons Haus wohnen, wollen ihre Sendung spät nachts nicht verpassen. Die Nageti'),
        ('09:19', 'Hallo, was machst Du?', 'Logistik', 'Wissen', 15, 6, 'a6', 55, 'Habt ihr schonmal von Intralogistik gehört? Was kompliziert klingt, schaut sich Lena heute für euch '),
        ('09:34', 'Bibi & Tina 4 - Tohuwabohu Total', '', 'Film', 108, 6, 'a6', 55, "Viertes Kinoabenteuer und turbulentes Finale der knallbunten, schwungvollen 'Bibi & Tina'-Reihe von "),
    ]),
    ("Sonntag, 30.08.2026", "SRF 1", [
        ('17:10', 'Minisguard', 'Wie macht man eigentlich Glace?', 'Serie', 15, 6, 'a6', 55, 'An einem heissen Sommertag gibt es kaum etwas Besseres als eine feine Glace. Aber wie wird Glace eig'),
    ]),
    ("Montag, 31.08.2026", "ProSieben Maxx", [
        ('16:45', 'Dr. STONE', 'Last Man Standing', 'Anime', 25, 12, 'a10', 55, 'Der teuflische Ibara hat jede Person auf der Insel versteinert und denkt, er sei der einzige Überleb'),
        ('17:10', 'Dragon Ball Super', 'Ein erbitterter Kampf! Muten-Roshi gibt alles!', 'Anime', 25, 12, 'a10', 55, 'Drei Kämpfer des vierten Universums haben es auf Muten-Roshi abgesehen. Darunter auch Caway, die sog'),
        ('17:35', 'Detektiv Conan', 'Love-Story im Hauptquartier 8 - Der linke Ringfinger (2)', 'Anime', 25, 12, 'a10', 55, 'Sato übernimmt die Befragung der drei Verdächtigen, die an dem Interview mit dem verstorbenen Krimin'),
        ('18:00', 'One Piece', 'Kämpfer unter sich! - Die wütenden Monster der neuen Welt', 'Anime', 30, 12, 'a10', 55, 'De Flamingo schwört Rache an Ruffy. Gut, dass dieser auch in Zukunft auf die Hilfe seiner Verbündete'),
        ('18:30', 'One Piece', 'Die silberne Festung! - Ruffys und Bartolomeos großes Abenteuer', 'Anime', 25, 12, 'a10', 55, 'Nach einer ausgelassenen Party begibt sich Ruffy auf die Suche nach etwas Essbarem. Doch sein Hunger'),
        ('18:55', 'Detektiv Conan', 'Den Männern in Schwarz auf der Spur (2)', 'Anime', 25, 12, 'a10', 55, 'Conan findet heraus, dass Pisco einer von sieben Verdächtigen sein muss. Auf dem Boden findet er ein'),
    ]),
    ("Montag, 31.08.2026", "WDR", [
        ('06:50', 'Wissen macht Ah!', 'Im Ah!telier', 'Vorlesen', 25, 3, 'a3', 55, 'Das Studio von "Wissen macht Ah!" wird heute zum Maler-Atelier und Ralph vollbringt eine künstlerisc'),
        ('07:15', 'POV - Deine Geschichte zählt', 'Was tun, wenn keiner was sagt · Rechtsextremismus unter Jugendlichen', 'Vorlesen', 10, 3, 'a3', 55, 'Leonie (16) fühlt sich in der Schule oft ausgeschlossen. Halt findet sie in Musik, Konzerten und Onl'),
        ('07:25', 'Campsite', 'Die Klette', 'Jugendserie', 5, 3, 'a3', 55, 'Theo ist sehr verliebt in Nura und möchte am liebsten die ganze Zeit mit ihr verbringen. Lea ist das'),
        ('07:30', 'Campsite', 'Das Midsommar-Brüllen', 'Jugendserie', 10, 3, 'a3', 55, 'Theo leidet unter der Trennung von Nura und möchte so gern wieder mit ihr zusammen sein. Doch im Str'),
        ('07:40', 'Campsite', 'Lach-Dämonen', 'Jugendserie', 5, 3, 'a3', 55, 'Andrine, Lea, Thea und Max chillen auf dem Campingplatz, als sie merkwürdige Geräusche hören. Wer la'),
    ]),
    ("Montag, 31.08.2026", "SWR", [
        ('12:55', 'Familie für Fortgeschrittene', '', 'Serie', 90, 6, 'a6', 55, 'Der Berliner Lehrer Oliver zieht mit Tochter Holly in die bayerische Provinz zu seiner neuen Lebensp'),
    ]),
    ("Montag, 31.08.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Oh, was für ein Lampenfieber! Denn heute steht für die Turnschuhe ein großes Konzert an und Wetz dar'),
    ]),
    ("Montag, 31.08.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Geschichten aus dem Schuhregal: Wer gibt den Takt an?'),
    ]),
    ("Montag, 31.08.2026", "HR", [
        ('05:10', 'Schau in meine Welt', 'Sammys erste Filmrolle', 'Vorlesen', 25, 3, 'a3', 55, 'Samanta Lillia (13) hat ihre erste Rolle beim Film. Als Sängerin stand sie schon auf vielen Bühnen. '),
        ('06:25', 'Leo da Vinci', 'Der gierige Schneider', 'Zeichentrick', 10, 3, 'a3', 55, 'Bianca wird in der Medici-Bank für eine Betrügerin gehalten und bekommt keine Fiorini, dafür wird si'),
        ('06:35', 'Leo da Vinci', 'Die Ankunft in Venedig', 'Zeichentrick', 15, 3, 'a3', 55, 'Unterwegs treffen die Freunde das kleine Mädchen Maria und retten sie vor einem wütenden Stier. Sie '),
    ]),
    ("Montag, 31.08.2026", "3sat", [
        ('10:15', 'Ein Schloss am Wörthersee - Der Film', '', 'Film', 85, 6, 'a6', 55, 'Der charmante Lennie Berger hat von seinem Onkel das Schlosshotel Velden geerbt und will es auf Vord'),
    ]),
    ("Montag, 31.08.2026", "arte", [
        ('04:35', 'Athleticus', 'Gym Tonic', 'Zeichentrick', 25, 3, 'a3', 55, 'Die dritte Staffel des Kurzprogramms wirft in 30 Folgen einen humorvollen Blick auf unsere Gesellsch'),
    ]),
    ("Montag, 31.08.2026", "ORF 1", [
        ('06:05', 'Wickie und die starken Männer', 'Der Eskimoschatz', 'Zeichentrick', 25, 3, 'a3', 55, 'Nach einer langen Reise kommen die Wikinger in Grönland an und machen sich auf die Schatzsuche. Die '),
        ('06:30', 'Servus Kasperl', 'Kasperl & Co: Zwei wie Pech und Schwefel', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('06:55', 'Die Jagd nach dem Kju Wang', 'Der schwarze Gondoliere', 'Zeichentrick', 25, 3, 'a3', 55, 'Da der Herzog auf Reisen ist, erklärt er Talbot zu seinem Stellvertreter. Zunächst profitiert Yagor '),
        ('07:35', 'Vegesaurier', 'Flugübungen', 'Zeichentrick', 5, 3, 'a3', 55, 'Das Trikarrotops-Mädchen Ginger und die Baby-Erbs-Rexe Minzi, Wasabi und Split lernen einen kleinen '),
        ('07:40', 'Dragons - Die Wächter von Berk', 'Drachentausch', 'Zeichentrick', 20, 3, 'a3', 55, 'Dass sich Rotzbakke und Astrid nicht leiden können, weiß jeder auf Berk. Als aus heiterem Himmel abe'),
    ]),
    ("Montag, 31.08.2026", "SRF 1", [
        ('17:30', 'Timmy Ziit - Pöschtler', '', 'Vorlesen', 10, 6, 'a6', 55, ''),
    ]),
]
