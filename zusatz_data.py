# -*- coding: utf-8 -*-
"""Kindersendungen der Vollprogramme.

Erzeugt von scan_kinder.py aus tv.de am 05.09.2026. Auswahl nach Kategorie,
bekannten Titeln und Beschreibung; Alterswerte heuristisch.
"""

TAGE = [
    ("Samstag, 05.09.2026", "ProSieben Maxx", [
        ('10:15', 'Voltron: Legendärer Verteidiger', 'Unbekannte Regionen', 'Zeichentrick', 25, 6, 'a6', 55, 'Während Honerva ihren Plan weiter vorantreibt, spaltet sich die Voltron-Koalition, um sie aufzuhalte'),
        ('10:40', 'She-Ra und die Rebellen-Prinzessinnen', 'Eine heilige Verbindung', 'Zeichentrick', 25, 6, 'a6', 55, 'Bow und Glimmer wollen herausfinden, was mit Entrapta passiert ist. Dabei nehmen sie aus Versehen Ca'),
        ('11:05', 'Die neuen Abenteuer des He-Man', 'Kampfspiele', 'Zeichentrick', 20, 6, 'a6', 55, 'Prinz Adam muss auf dem Planeten Primus gegen gefährliche Mutanten kämpfen.'),
        ('11:25', 'Die neuen Abenteuer des He-Man', 'Hilfe von der Zauberin', 'Zeichentrick', 25, 6, 'a6', 55, 'Prinz Adam muss auf dem Planeten Primus gegen gefährliche Mutanten kämpfen.'),
        ('11:50', 'Die neuen Abenteuer des He-Man', 'Ein neuer galaktischer Wächter', 'Zeichentrick', 25, 6, 'a6', 55, 'Prinz Adam muss auf dem Planeten Primus gegen gefährliche Mutanten kämpfen.'),
        ('12:15', 'She-Ra', 'Glimmers Geschichte', 'Zeichentrick', 25, 6, 'a6', 55, 'Auf dem Weg nach Schloss Bright Moon gerät Prinz Haycliff in einen Hinterhalt von Hordaks Schergen. '),
        ('12:40', 'She-Ra', 'Das Ebenbild', 'Zeichentrick', 20, 6, 'a6', 55, 'Shadow Weaver erschafft eine abscheuliche Kreatur aus Schlamm, mit der Fähigkeit, jedem Lebewesen be'),
        ('13:00', 'Voltron: Legendärer Verteidiger', 'Der Zenit', 'Zeichentrick', 25, 6, 'a6', 55, 'Das gesamte Universum steht am Abgrund: Die Paladine bündeln nun all ihre Macht und setzen auf ihre '),
        ('13:25', 'Voltron: Legendärer Verteidiger', 'Das Ende ist der Anfang', 'Zeichentrick', 30, 6, 'a6', 55, 'Voltron und Honerva stehen sich im alles entscheidenden Kampf zwischen Gut und Böse gegenüber. Wer w'),
        ('13:55', 'She-Ra und die Rebellen-Prinzessinnen', 'Signale', 'Zeichentrick', 20, 6, 'a6', 55, 'Adora und ihre Freunde begeben sich an einen Ort, an dem es spuken soll. Währenddessen macht Entrapt'),
    ]),
    ("Samstag, 05.09.2026", "MDR", [
        ('09:45', 'Lilly unter den Linden', '', 'Film', 90, 6, 'a6', 55, 'Das Mädchen Lilly aus Hamburg lernt 1988 bei der Beerdigung der Mutter ihre Tante Lena aus Jena kenn'),
        ('14:00', 'Die kluge Bauerntochter', '', 'Serie', 60, 6, 'a6', 55, 'Ein Garten auf dem Dach ihrer ärmlichen Hütte! Mit dieser Idee verblüfft die kluge Bauerntochter den'),
        ('15:00', 'Wer reißt denn gleich vorm Teufel aus?', '', 'Serie', 90, 6, 'a6', 55, 'Der arme Bursche Jakob ist vom Missgeschick verfolgt. Und nun hat es auch noch der König auf sein Le'),
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Hinter einem Busch taucht ein Blumenstrauß auf, der hin und her geschwenkt wird. Schnattchen glaubt,'),
    ]),
    ("Samstag, 05.09.2026", "RBB", [
        ('10:30', 'Max und die Wilde 7 - Die Geisteroma', '', 'Film', 90, 6, 'a6', 55, 'In der Seniorenresidenz Burg Geroldseck hat der 10-jährige Max endlich richtige, aber alles andere a'),
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Pittiplatsch: Der Blumenstraußwinker'),
    ]),
    ("Samstag, 05.09.2026", "ORF 1", [
        ('10:29', '1000 Tricks', '', 'Vorlesen', 15, 6, 'a6', 55, 'Ist es tatsächlich möglich seine Gedanken zu funken? Melly verblüfft Christoph und zeigt euch, wie d'),
        ('10:44', 'Ganz Ohr', 'Film', 'Vorlesen', 15, 6, 'a6', 55, 'Wie entsteht ein Film oder eine Serie? Um das rauszufinden besucht Esther das Set von "Tage, die es '),
        ('10:59', 'Mini Spezial', 'Gebärdensprache', 'Vorlesen', 7, 6, 'a6', 55, 'In dieser Mini Spezial schaut sich Julia die Gebärdensprache genauer an. Sie trifft Babs und Milana,'),
        ('11:06', 'Galapagos X', 'Zeph, der Vampirjäger', 'Zeichentrick', 12, 6, 'a6', 55, 'In der Gegenwart wird die Ruhe durch nervige Staubsauger gestört, die die verpestete Luft in der Sta'),
    ]),
    ("Samstag, 05.09.2026", "SRF 1", [
        ('17:25', 'Minisguard', 'Wie bereitet man sich auf die Jagd vor?', 'Serie', 35, 6, 'a6', 55, 'Wie bereitet man sich auf die Jagd vor? Um das herauszufinden, hat Gian-Carlo Niculin und seinen Bru'),
    ]),
    ("Sonntag, 06.09.2026", "ARD", [
        ('05:30', 'HipHorses - Du und Dein Pferd', 'Finnja und Showpferd Missy', 'Vorlesen', 25, 3, 'a3', 55, 'Finnja lebt in der Nähe von Bremen, ist 13 Jahre alt und liebt Pferde und Shows. Deshalb ist das Sho'),
        ('05:55', '#WIR - Freundschaft grenzenlos', 'Eiskunstlaufen: Tanz auf dem Eis', 'Vorlesen', 10, 3, 'a3', 55, 'Laura und Diana sind richtige Eisprinzessinnen. Beide stehen schon von Kindesbeinen an auf dem Eis u'),
        ('06:05', 'Tigerenten Club', 'Der Club zum Mitmachen - Spiele, Spaß und spannendes Wissen', 'Vorlesen', 60, 3, 'a3', 55, 'Haie: Faszinierend und bedroht! Sie taucht da, wo keiner hinwill: zu Haien! Die Unterwasserkamerafra'),
        ('08:30', 'Alina', 'Das Turnier', 'Jugendserie', 60, 10, 'a10', 55, 'Alina darf Silverado trainieren, bis ein Käufer gefunden ist, und ihn sogar auf dem bevorstehenden S'),
        ('09:30', 'Die Sendung mit der Maus', '', 'Vorlesen', 30, 6, 'a6', 55, 'Lach- und Sachgeschichten, heute mit dem Geheimnis der Hafermilch, Nulli in Priesemuts Schwimmschule'),
        ('15:30', 'Ein Ferienhaus auf Ibiza', '', 'Serie', 90, 6, 'a6', 55, 'Man kann nicht gerade behaupten, dass die Geschwister Karla (Tina Ruland), Henriette (Suzan Anbeh) u'),
    ]),
    ("Sonntag, 06.09.2026", "ZDF", [
        ('06:00', 'Die Biene Maja', 'Majas Geburt', 'Zeichentrick', 10, 3, 'a3', 55, 'Im Bienenstock auf der Klatschmohnwiese wird eine besondere Biene geboren: Maja. Sie will nicht im S'),
        ('06:10', 'Die Biene Maja', 'Die große, weite Wiesenwelt', 'Zeichentrick', 10, 3, 'a3', 55, 'In der ersten Nacht ihres Bienenlebens schleicht sich Maja zusammen mit Willi aus dem Bienenstock. M'),
        ('06:20', 'Die Biene Maja', 'Der Buschwindbote', 'Zeichentrick', 15, 3, 'a3', 55, 'Eine Stelle, an der es Nektar zu holen gibt, ist für Bienen Gold wert. Vor allem, wenn den Platz vor'),
        ('06:35', 'Die Biene Maja', 'Richter Bienenwachs', 'Zeichentrick', 15, 3, 'a3', 55, 'Die Klatschmohnwiese ohne Maja? Für Richter Bienenwachs eine schöne Vorstellung, müsste er sich dann'),
        ('06:50', 'Die Biene Maja - Ihre schönsten Abenteuer', '', 'Serie', 80, 3, 'a3', 55, 'Maja erlebt unglaubliche Abenteuer mit ihrem liebsten Freund, dem faulen Willi. Schon als Maja auf d'),
        ('08:10', 'Löwenzahn', 'Bienen - Der Raub der Honigmacher', 'Serie', 25, 6, 'a6', 55, 'Ein Bienenwagen verschwindet über Nacht. Fritz nimmt die Ermittlungen auf und macht sich auf die Suc'),
        ('08:35', '1, 2 oder 3', 'Bienen - Helden der Natur', 'Serie', 28, 6, 'a6', 55, 'Welches Insekt ist für unser Ökosystem unverzichtbar? Ganz klar: die Biene! Autorin und Biologin Dr.'),
    ]),
    ("Sonntag, 06.09.2026", "SAT.1", [
        ('14:55', 'Ice Age – Die Abenteuer von Buck Wild', '', 'Zeichentrick', 105, 6, 'a6', 55, 'Crash und sein Bruder Eddie verlassen ihre Heimat und stürzen sich in ein aufregendes Abenteuer. In '),
    ]),
    ("Sonntag, 06.09.2026", "ProSieben Maxx", [
        ('04:05', 'One Piece', 'Eine auswegslose Situation! - Der heiße Kampf auf Silver Mine', 'Anime', 20, 12, 'a10', 55, 'Nachdem Bill immer wieder mit Provokationen um sich wirft, kommt es zwischen ihm und Ruffy zum Kampf'),
        ('04:25', 'One Piece', 'Ein neues Abenteuer beginnt! - Ankunft auf der Phantominsel Zou', 'Anime', 25, 12, 'a10', 55, 'An Bord des Schiffes erzählt Bartolomeo der Crew bewegende Geschichten und bittet auch Ganbia, sich '),
        ('04:50', 'Dr. STONE', 'Beyond the New World', 'Anime', 20, 12, 'a10', 55, 'Senku und seine Freunde sind wieder zu Hause angekommen. Nun wollen sie Tsukasa endlich wiederbelebe'),
        ('05:10', 'Yashahime', 'Inuyasha seither', 'Anime', 25, 12, 'a10', 55, 'Die Halbdämonen-Prinzessin Towa Higurashi wird festgenommen und verhört. Da sie mit ihrem Wissen die'),
    ]),
    ("Sonntag, 06.09.2026", "NDR", [
        ('06:45', 'Edgar, das Super-Karibu', 'Das schreckliche Gurgeln', 'Zeichentrick', 10, 3, 'a3', 55, 'Edgar, das Super-Karibu putzt sich die Zähne und singt dabei furchtbar schlecht. Im Wald hört Marion'),
        ('06:55', 'Edgar, das Super-Karibu', 'Der verliebte Hase', 'Zeichentrick', 15, 3, 'a3', 55, 'Um Birgit zu imponieren, in die er heimlich verliebt ist, steigert Rudi, der Hase seine Heldentaten '),
    ]),
    ("Sonntag, 06.09.2026", "BR", [
        ('09:00', 'Hans im Glück', '', 'Serie', 60, 6, 'a6', 55, 'Sieben Jahre arbeitet Hans im Haus eines reichen Gewürzhändlers. Doch eines Morgens wacht er auf und'),
    ]),
    ("Sonntag, 06.09.2026", "MDR", [
        ('15:20', 'Till Eulenspiegel', '', 'Serie', 115, 6, 'a6', 55, 'Der größten Herausforderung seines Leben stellt sich Till Eulenspiegel, als er gegen den Lübecker Bü'),
        ('17:35', 'Unser Sandmännchen', '', 'Serie', 5, 3, 'a3', 55, 'Frau Elster drängt den Fuchs etwas zu tun, damit man ihre Anwesenheit auf der Insel bemerkt. Als Her'),
    ]),
    ("Sonntag, 06.09.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Kallis Gute-Nacht-Geschichten: Kalli-Saurier'),
    ]),
    ("Sonntag, 06.09.2026", "HR", [
        ('12:20', 'Dann kam Lucy', '', 'Serie', 90, 6, 'a6', 55, 'Die passionierte Pferdezüchterin Saskia lebt zurückgezogen auf ihrem idyllischen Gestüt im Rheinland'),
    ]),
    ("Sonntag, 06.09.2026", "arte", [
        ('04:35', 'Athleticus', 'Jogging', 'Zeichentrick', 45, 3, 'a3', 55, 'Die dritte Staffel des Kurzprogramms wirft in 30 Folgen einen humorvollen Blick auf unsere Gesellsch'),
    ]),
    ("Sonntag, 06.09.2026", "ORF 1", [
        ('04:22', 'Chaos im Netz', '', 'Zeichentrick', 98, 3, 'a3', 55, "Überaus witzige Fortsetzung des Animationshits 'Ralph reicht's'. Vanellope und Ralph stürzen sich wa"),
        ('06:00', 'Tom - Ein echter Freund', 'Tom in Japan', 'Zeichentrick', 23, 3, 'a3', 55, 'An der Küste Japans rettet Saurier Tom den Perlentaucher Miko gerade noch vor einer geheimnisvollen '),
        ('06:23', 'Vegesaurier', 'Blubberbad', 'Zeichentrick', 5, 3, 'a3', 55, 'Zur Freude von Ginger und den Erbs-Rex-Babys gibt es beim Vulkan plötzlich ein warmes Blubberbad. Ab'),
        ('06:28', 'Servus Kasperl', 'Kasperl & Co: Bfrt - Brft - bfrrrt!', 'Serie', 26, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('06:54', 'Mister Paper', 'Mister Paper geht spazieren', 'Zeichentrick', 5, 3, 'a3', 55, 'In einer Welt aus Papier und Pappe lebt der eigensinnige Mister Paper mit seiner Katze ein heiteres '),
        ('06:59', 'Mister Paper', 'Mister Paper geht schlafen', 'Zeichentrick', 5, 3, 'a3', 55, 'Als Mister Paper in der Nacht von einer vorwitzigen Fledermaus geweckt wird, hat er Probleme, wieder'),
        ('07:04', 'Bakabu', 'Beste Freunde', 'Vorlesen', 5, 3, 'a3', 55, 'Mit wem macht dir das Spielen am meisten Spaß? Na klar, mit einer Freundin oder einem Freund. Auch B'),
        ('07:09', 'Knall genial', '', 'Wissen', 18, 3, 'a3', 55, 'Originelle Tipps und Tricks von Thomas Brezina und den Kids! Theater einmal anders. Im Kameltheater '),
        ('07:27', 'Der gestiefelte Kater - Abenteuer in San Lorenzo', 'Die Weisheit des Buches', 'Serie', 22, 3, 'a3', 55, 'Mit Hut und Degen zieht der gestiefelte Kater durchs Land, immer auf der Suche nach einem neuen Aben'),
        ('07:49', 'Drunter & drüber mit Christoph Hirschler', '"Hits im Ohr" mit Christina Stürmer', 'Vorlesen', 19, 3, 'a3', 55, 'Christoph Hirschler begrüßt heute die erfolgreichste Musikerin Österreichs: Christina Stürmer! Sie e'),
        ('08:08', 'Campsite', 'Psychopath?', 'Jugendserie', 8, 10, 'a10', 55, 'Anja schwebt auf Wolke Sieben wegen Max, denn er hat ihr gesagt, dass er sie süß findet. Sie erzählt'),
        ('08:16', 'Campsite', 'Ein neuer König', 'Jugendserie', 6, 10, 'a10', 55, 'An der Tischtennisplatte ist Sebbe der ungeschlagene König. Keins der anderen Kinder kann ihm beim S'),
        ('08:22', 'Campsite', 'Erdbeereis', 'Jugendserie', 7, 10, 'a10', 55, 'Anja möchte sich unbedingt ein Erdbeereis bei Tonis Kiosk holen, doch der gibt ihr fälschlicherweise'),
        ('08:29', 'Dragons - Die Wächter von Berk', 'Bing! Bamm! Bumm!', 'Zeichentrick', 22, 6, 'a6', 55, 'Die Drachenreiter stöbern ein Trio kleiner Donnertrommler auf. Ohne es zu wollen, folgen ihnen die d'),
        ('08:51', 'Was geht?', 'Coole Schule', 'Wissen', 15, 6, 'a6', 55, 'Kann Schule Spaß machen? Tiara (10), Konstantin (11) und Amelie (12) berichten von ihren lustigsten '),
        ('09:06', 'Mini Spezial', 'Elektroauto', 'Vorlesen', 4, 6, 'a6', 55, 'Gibt es in deiner Familie ein Auto? Und wenn ja, womit fährt es - mit Benzin, Diesel oder mit Strom?'),
        ('09:10', 'Garfield', 'Detektiv  Squeak', 'Zeichentrick', 13, 6, 'a6', 55, 'Jon muss sparen und setzt den gefräßigen Garfield deswegen auf Diät. Die Ernährung des Katers wird n'),
        ('09:23', 'Hallo, was machst Du?', 'Friseurin', 'Wissen', 17, 6, 'a6', 55, 'Schnipp, schnapp, Haare ab! Lena besucht Friseurin Claudia und lernt dort nicht nur, wie ein Fischgr'),
        ('09:50', 'Galapagos X', 'Der Klimaanlagen-Kollaps', 'Zeichentrick', 13, 6, 'a6', 55, 'Zeph ist entsetzt! Der Popstar Barney Pluto sagt seine Tournee ab und möchte vor der Hitzewelle, die'),
        ('10:03', 'Mumien - Ein total verwickeltes Abenteuer', '', 'Zeichentrick', 81, 6, 'a6', 55, 'Vergnügliches Animationsabenteuer. Eine junge ägyptische Prinzessin, ihr Bräutigam wider Willen, des'),
    ]),
    ("Sonntag, 06.09.2026", "SRF 1", [
        ('17:10', 'Minisguard', 'Wie bereitet man sich auf die Jagd vor?', 'Serie', 15, 6, 'a6', 55, 'Wie bereitet man sich auf die Jagd vor? Um das herauszufinden, hat Gian-Carlo Niculin und seinen Bru'),
        ('23:45', 'One Minute Movies - Selection I', '', 'Zeichentrick', 10, 10, 'a10', 55, 'Der kurzen Aufmerksamkeitsspanne des modernen Menschen Rechnung tragend, ist keine Folge länger als '),
    ]),
    ("Montag, 07.09.2026", "WDR", [
        ('08:35', 'Wissen macht Ah!', 'Das wird jetzt ein bisschen wehtun', 'Vorlesen', 25, 6, 'a6', 55, 'Heute sendet "Wissen macht Ah!" direkt aus dem Krankenhaus. Aber keine Panik: Bei Doktor Clarissa Co'),
        ('09:00', 'POV - Deine Geschichte zählt', 'Faszination Techno · Mehr als nur Party', 'Vorlesen', 10, 6, 'a6', 55, 'Leonie (16) fühlt sich in der Schule oft ausgeschlossen. Halt findet sie in Musik, Konzerten und Onl'),
    ]),
    ("Montag, 07.09.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Als die Gummistiefel Torf und Buddel im Schuhladen auftauchen, ist es vorbei mit der Langeweile: End'),
    ]),
    ("Montag, 07.09.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Geschichten aus dem Schuhregal: Die Neuen'),
    ]),
    ("Montag, 07.09.2026", "HR", [
        ('05:10', 'Schau in meine Welt', 'Ginevra - Ein Mädchen unter Cowboys', 'Vorlesen', 25, 3, 'a3', 55, 'Ginevra (12) will eine Buttera werden, eine Rinderhirtin, die vom Rücken ihres Pferds die Herden tre'),
        ('06:25', 'Leo da Vinci', 'Berg-Piraten', 'Zeichentrick', 10, 3, 'a3', 55, 'Eine Bärenmutter hindert die Freunde daran weiterzufahren, ihr Junges ist in eine Schlucht gefallen '),
        ('06:35', 'Leo da Vinci', 'Meister Albrecht Dürer', 'Zeichentrick', 15, 3, 'a3', 55, 'Nach ihrer Alpenüberquerung schicken die Freunde eine Taube nach Venedig, um Alvise auf den neuesten'),
    ]),
    ("Montag, 07.09.2026", "arte", [
        ('04:35', 'Athleticus', 'Skateboard', 'Zeichentrick', 30, 3, 'a3', 55, 'Die dritte Staffel des Kurzprogramms wirft in 30 Folgen einen humorvollen Blick auf unsere Gesellsch'),
    ]),
    ("Montag, 07.09.2026", "ORF 1", [
        ('06:00', 'ZIB KiDS', '', 'Serie', 5, 3, 'a3', 55, ''),
        ('06:05', 'Wickie und die starken Männer', 'Eine böse Überraschung', 'Zeichentrick', 25, 3, 'a3', 55, 'Wickie, einziger Sohn des furchtlosen Wikingerhäuptlings Halvar, ist für sein Alter ein wenig klein '),
        ('06:30', 'Servus Kasperl', 'Kasperl & Pezi: Superkaspi und Peziman', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('06:55', 'Noahs Insel', 'Die Elefantensorgen', 'Zeichentrick', 25, 3, 'a3', 55, 'Noahs Insel schwimmt dicht an der Küste Afrikas entlang. Die Gefahr, von Menschen entdeckt zu werden'),
        ('07:20', 'Bakabu', 'Beste Freunde', 'Vorlesen', 5, 3, 'a3', 55, 'Mit wem macht dir das Spielen am meisten Spaß? Na klar, mit einer Freundin oder einem Freund. Auch B'),
        ('07:35', 'Vegesaurier', 'Bauchschmerzen', 'Zeichentrick', 5, 3, 'a3', 55, 'Nach dem Genuss einer unreifen Frucht leidet Ginger unter Bauchschmerzen. Die möchte sie mit Pfeffer'),
        ('07:40', 'Garfield', 'Abenteuer Wildnis - Teil 3', 'Zeichentrick', 15, 3, 'a3', 55, 'Die drei Waschbären machen es sich in Garfields Haus gemütlich, und der arme Jon, noch immer krank v'),
        ('07:55', 'ZIB KiDS', '', 'Serie', 5, 3, 'a3', 55, ''),
    ]),
    ("Montag, 07.09.2026", "SRF 1", [
        ('17:30', 'Giggelibug', 'En schöne Glungge', 'Zeichentrick', 10, 6, 'a6', 55, 'Claude macht Giggeli und Poppy mit seinen Riesensprüngen die Pfützen kaputt, bis sie eine bauen, die'),
    ]),
]
