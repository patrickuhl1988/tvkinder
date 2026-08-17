# -*- coding: utf-8 -*-
"""Kindersendungen der Vollprogramme.

Erzeugt von scan_kinder.py aus tv.de am 17.08.2026. Auswahl nach Kategorie,
bekannten Titeln und Beschreibung; Alterswerte heuristisch.
"""

TAGE = [
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
    ("Montag, 17.08.2026", "MDR", [
        ('07:05', 'Unterwegs in Sachsen-Anhalt', 'Urlaub auf dem Bauernhof', 'Serie', 30, 3, 'a3', 55, 'Zwischen Erholung und echter Hofarbeit: Urlaub auf dem Bauernhof kann vielfältig sein. Aber was habe'),
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'MiWaus Napf mit Katzenmilch ist leer und ihr Durst ist groß. Moppi schickt MiWau zum Milchregal, sch'),
    ]),
    ("Montag, 17.08.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Moppi und MiWau: Die Katzenmilch'),
    ]),
    ("Montag, 17.08.2026", "3sat", [
        ('13:15', 'Borkum ... mit Judith Rakers', '', 'Serie', 45, 6, 'a6', 55, 'Judith Rakers entdeckt die größte der Ostfriesischen Inseln durch die Menschen, die dort entweder le'),
    ]),
    ("Montag, 17.08.2026", "ORF 1", [
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
    ("Mittwoch, 19.08.2026", "ProSieben Maxx", [
        ('16:45', 'Dr. STONE', 'Das Wunder mit dieser Faust', 'Anime', 25, 12, 'a10', 55, 'Kohaku gelingt es, die Schatztruhe ausfindig zu machen. Doch diese befindet sich in einem massiven B'),
        ('17:10', 'Dragon Ball Super', 'Der Kampf ums Überleben beginnt! Vorhang auf für das Turnier der Kraft', 'Anime', 25, 12, 'a10', 55, 'Bevor sich die 80 Kämpfer gleichzeitig aufeinander stürzen, erklärt der Hohepriester die Regeln des '),
        ('17:35', 'Detektiv Conan', 'Gelbes Alibi', 'Anime', 25, 12, 'a10', 55, 'Die Barbetreiberin Hiroko Inoue wird ermordet in ihrer Wohnung aufgefunden. Da Kogoro das Opfer kann'),
        ('18:00', 'One Piece', 'Die Wundertränen - Mansherrys Kampf!', 'Anime', 30, 12, 'a10', 55, 'Mansherrys leistet wertvolle Arbeit, indem er den Verletzten und den Gladiatoren Hilfe leistet. Law '),
        ('18:30', 'One Piece', 'Solange wir am Leben sind - Haltet den Vogelkäfig auf!', 'Anime', 25, 12, 'a10', 55, 'Die Inselbewohner und Seemänner auf Dressrosa arbeiten gemeinsam daran, den Vogelkäfig aufzuhalten. '),
        ('18:55', 'Detektiv Conan', 'Das versiegelte Badezimmer (2)', 'Anime', 25, 12, 'a10', 55, 'Masayos Fingerabdrücke werden auf dem Klebeband entdeckt, das zur Verriegelung der Badezimmertür gen'),
    ]),
    ("Mittwoch, 19.08.2026", "WDR", [
        ('07:35', 'Campsite', 'Ein neuer König', 'Jugendserie', 5, 3, 'a3', 55, 'Sebbe ist der ungeschlagene Tischtennis-König auf dem Campingplatz - keiner schafft es, ihn zu besie'),
        ('07:40', 'Campsite', 'Erdbeereis', 'Jugendserie', 5, 3, 'a3', 55, 'Anja will sich am Kiosk ein Erdbeereis holen, bekommt aber versehentlich Schoko und traut sich nicht'),
        ('07:45', 'Campsite', 'Du wurdest reingelegt', 'Jugendserie', 10, 3, 'a3', 55, 'Auf dem Campingplatz findet eine Übernachtungsparty statt. Silje, Lea, Leo und Klaus sind dabei. Die'),
        ('07:55', 'Das Camp in der Wildnis', 'Unfaires Spiel', 'Vorlesen', 25, 3, 'a3', 55, 'Sechs Tage bei Minusgraden mitten in der wilden Natur: Es ist Herbst in Norwegen und das Wetter erwe'),
        ('08:20', 'Das Camp in der Wildnis', 'Spurlos verschwunden', 'Vorlesen', 25, 6, 'a6', 55, 'Pirschen, Verbergen, Aufspüren: Der Endspurt um den Sieg bei der Foto-Challenge geht für die Teams i'),
    ]),
    ("Mittwoch, 19.08.2026", "NDR", [
        ('06:00', 'Sesamstraße', '', 'Vorlesen', 20, 3, 'a3', 55, 'Bert hat ein Dosentelefon gebaut, um damit das Phänomen der Schallübertragung zu erklären. Als das K'),
        ('06:20', 'Schloss Einstein', 'Die Suche nach der Wahrheit', 'Jugendserie', 25, 10, 'a10', 55, 'Noah hat eine wichtige Mission: Für einen Bewerbungsfilm will er die Schatzsuche dokumentieren. Nur '),
        ('06:45', 'Schloss Einstein', 'Die Schatzkarte', 'Jugendserie', 25, 10, 'a10', 55, 'Der Schatz ist zum Greifen nah, bis Karl einen entscheidenden Fehler macht. Maxi ist sauer, doch Kar'),
        ('07:10', 'Die Pfefferkörner', 'Leinen los!', 'Serie', 30, 10, 'a10', 55, 'Als Jasina für ein Fotoprojekt der Schule eine Hafenrundfahrt mit ihrer Lieblingskapitänin Anja mach'),
        ('07:40', 'Die Pfefferkörner', 'Die falsche Vermieterin', 'Serie', 35, 10, 'a10', 55, 'Leos Mutter Kim will nach der Rückkehr aus der Therapie alles richtig machen und sucht nach einer gr'),
    ]),
    ("Mittwoch, 19.08.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Erdmännchen Jan kann aufgrund eines unheimlichen Geräuschs nicht einschlafen. Seltsamerweise kann se'),
    ]),
    ("Mittwoch, 19.08.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Jan & Henry: Das Känguru mit dem Wecker'),
    ]),
    ("Mittwoch, 19.08.2026", "HR", [
        ('05:55', 'Leo da Vinci', 'Brieftauben', 'Zeichentrick', 10, 3, 'a3', 55, 'Leo will seinem Freund Fabrizio eine Brieftaube nach Venedig schicken. Doch dazu muss er erst einmal'),
        ('06:05', 'Leo da Vinci', 'Der Bühnenmaler', 'Zeichentrick', 15, 3, 'a3', 55, 'Auf dem Weg nach Venedig treffen Leo und seine Freunde auf eine Truppe, deren Kutsche feststeckt. Al'),
        ('23:45', 'Der Kommissar und die Alpen', 'Schnee am Dienstag', 'Serie', 25, 10, 'a10', 55, 'Vice-Questore Rocco Schiavones Geduldsfaden ist am Reißen - unfähige Mitarbeiter und ein frustrieren'),
    ]),
    ("Mittwoch, 19.08.2026", "ORF 1", [
        ('06:05', 'Wickie und die starken Männer', 'Brieftaube', 'Zeichentrick', 25, 3, 'a3', 55, 'Wickie und Ylvi gehen einer neuen Beschäftigung nach: sie dressieren Tauben. Halvar hält nicht viel '),
        ('06:30', 'Servus Kasperl', 'Kasperl & Co: Eine Kragenweite zu groß', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('06:55', 'Die Jagd nach dem Kju Wang', 'Sesam, öffne dich', 'Zeichentrick', 25, 3, 'a3', 55, 'Die neueste Errungenschaft des Herzogs hält im Palast Einzug: Eine Panzertür mit Spracherkennungsmod'),
        ('07:40', 'Garfield', 'Garfield, der Pirat - Teil 1', 'Zeichentrick', 10, 3, 'a3', 55, 'Garfield ist ein gefürchteter Pirat. Er und seine Mannschaft kapern andere Schiffe nach Belieben. Er'),
        ('07:50', 'Garfield', 'Garfield, der Pirat - Teil 2', 'Zeichentrick', 10, 3, 'a3', 55, 'Captain Garfield und Admiral Nermal stellen zu ihrem Erstaunen fest, dass sie auf der einsamen Insel'),
    ]),
    ("Mittwoch, 19.08.2026", "SRF 1", [
        ('17:30', 'BooSnoo! - Minigolf', '', 'Zeichentrick', 10, 6, 'a6', 55, 'BooSnoo, der rote Ball, geht auf Reisen. Fliessende Bewegungen, sanfte Rhythmen - BooSnoo beruhigt, '),
    ]),
]
