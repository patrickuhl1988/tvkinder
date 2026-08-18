# -*- coding: utf-8 -*-
"""Kindersendungen der Vollprogramme.

Erzeugt von scan_kinder.py aus tv.de am 18.08.2026. Auswahl nach Kategorie,
bekannten Titeln und Beschreibung; Alterswerte heuristisch.
"""

TAGE = [
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
    ("Dienstag, 18.08.2026", "ORF 1", [
        ('06:54', 'Die Jagd nach dem Kju Wang', 'Die Uhr', 'Zeichentrick', 23, 3, 'a3', 55, 'Yagor macht sich die Dankbarkeit des Volkes von Zinzania zunutze und schickt dem Herzog in des Volke'),
        ('07:34', 'Garfield', 'Die Glitzer-Schlucht - Teil 4', 'Zeichentrick', 14, 3, 'a3', 55, 'Garfields Frau wird vom Oberhaupt der Schnurrbartbande entführt. Als Star des Western-Films und Hilf'),
        ('07:48', 'Garfield', 'Die Glitzer-Schlucht - Teil 5', 'Zeichentrick', 14, 3, 'a3', 55, 'Der Regisseur Nermal beschließt kurzfristig, sich selbst mit einer Hauptrolle in den Film reinzuschr'),
    ]),
    ("Dienstag, 18.08.2026", "SRF 1", [
        ('17:30', 'BooSnoo! - Musig', '', 'Zeichentrick', 10, 6, 'a6', 55, 'BooSnoo, der rote Ball, geht auf Reisen. Fliessende Bewegungen, sanfte Rhythmen - BooSnoo beruhigt, '),
        ('21:10', 'Kassensturz', 'Risiko Online-Rezept - Medikamente ohne Arztbesuch', 'Serie', 40, 10, 'a10', 55, 'Risiko Online-Rezept - Medikamente ohne Arztbesuch Keine Lust aufs Wartezimmer, auf einen Arztbesuch'),
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
        ('11:30', 'Kassensturz', 'Risiko Online-Rezept - Medikamente ohne Arztbesuch', 'Serie', 40, 6, 'a6', 55, 'Risiko Online-Rezept - Medikamente ohne Arztbesuch Keine Lust aufs Wartezimmer, auf einen Arztbesuch'),
        ('17:30', 'BooSnoo! - Minigolf', '', 'Zeichentrick', 10, 6, 'a6', 55, 'BooSnoo, der rote Ball, geht auf Reisen. Fliessende Bewegungen, sanfte Rhythmen - BooSnoo beruhigt, '),
    ]),
    ("Donnerstag, 20.08.2026", "ZDF", [
        ('04:15', 'plan b', 'Clever reisen - Trips vor der Haustür', 'Serie', 45, 3, 'a3', 55, 'Sommerzeit - Ferienzeit! Ob Surfen oder Städtetrip: Urlaub muss kein Vermögen kosten - dank innovati'),
    ]),
    ("Donnerstag, 20.08.2026", "ProSieben Maxx", [
        ('16:45', 'Dr. STONE', 'Die Gegenoffensive des Wissenschafts-Königreichs', 'Anime', 25, 12, 'a10', 55, 'Senku und seine Freunde haben es geschafft, das Platin in ihren Besitz zu bringen. Nun können sie me'),
        ('17:10', 'Dragon Ball Super', 'Ach Vergänglichkeit! Ein Universum verzweifelt!', 'Anime', 25, 12, 'a10', 55, 'Die Kämpfer des neunten Universums haben es auf Son Goku abgesehen. Gemeinsam versuchen sie, den Sai'),
        ('17:35', 'Detektiv Conan', 'Das Messer der Waldhexe (1)', 'Anime', 25, 12, 'a10', 55, 'Professor Agasa will mit den Kindern campen gehen, doch die Gruppe verirrt sich im Wald. In einem ab'),
        ('18:00', 'One Piece', 'Tot oder lebendig! - Ein schicksalshafter Countdown', 'Anime', 30, 12, 'a10', 55, 'Gatz verkündet, dass Ruffy zurückkehren und De Flamingo endgültig besiegen wird. Dieser ist außer si'),
        ('18:30', 'One Piece', 'Himmelskampf - Ruffys rasende King Kong Gun!', 'Anime', 25, 12, 'a10', 55, 'De Flamingo und Ruffy nehmen ihren Kampf wieder auf: Ruffy gelingt der Befreiungsschlag auf den Fäng'),
        ('18:55', 'Detektiv Conan', 'Zahlenspiele', 'Anime', 25, 12, 'a10', 55, 'Als Conan mit seinen Jungs nach Hause kommt, bemerkt er eine noch nicht abgehörte Nachricht auf sein'),
    ]),
    ("Donnerstag, 20.08.2026", "WDR", [
        ('07:30', 'Campsite', 'Putzaktion am Klo', 'Jugendserie', 10, 3, 'a3', 55, 'Theo will Nura endlich sagen, dass er in sie verknallt ist. Doch bevor er die Gelegenheit findet, ta'),
        ('07:40', 'Campsite', 'Zeit für Rache', 'Jugendserie', 5, 3, 'a3', 55, 'Andrine hat ihre Freunde reingelegt: Obwohl Nura, Theo und Anja die ganzen Sanitäranlagen geputzt ha'),
        ('07:45', 'Campsite', 'Wahrheit oder Pflicht', 'Jugendserie', 10, 3, 'a3', 55, 'Die Campingplatz-Clique spielt "Wahrheit oder Pflicht". Natürlich geht es oft um die Frage, wer in w'),
        ('07:55', 'Das Camp in der Wildnis', 'Chaos bricht aus', 'Vorlesen', 25, 3, 'a3', 55, 'Auf diese Liste haben alle gespannt gewartet! Die Neuaufteilung der Zimmer ist entschieden und ausge'),
        ('08:20', 'Das Camp in der Wildnis', 'Schräge Töne', 'Vorlesen', 25, 6, 'a6', 55, 'Es ist Winterzeit in Norwegen und das Camp in der Wildnis versinkt im tiefen Schnee. Während Hinnerk'),
    ]),
    ("Donnerstag, 20.08.2026", "NDR", [
        ('06:00', 'Sesamstraße', '', 'Vorlesen', 20, 3, 'a3', 55, 'Yolan (8) und Martha (8) sind beeindruckt, wie detailliert der Künstler Ludwig (Louis) Sussmann-Hell'),
        ('06:20', 'Schloss Einstein - Erfurt', 'Bittere Enttäuschung', 'Jugendserie', 25, 10, 'a10', 55, 'Der Schatz scheint endlich gefunden, doch die Enttäuschung ist groß. In der Schatzkiste befindet sic'),
        ('06:45', 'Schloss Einstein - Erfurt', 'Das Kintsugi-Abenteuer', 'Jugendserie', 25, 10, 'a10', 55, 'Der Share Space soll mit einer weiteren kreativen Aktion gerettet werden. Tahmina sorgt für die eins'),
        ('07:10', 'Die Pfefferkörner', 'Muskeln um jeden Preis', 'Serie', 30, 10, 'a10', 55, 'Hakim ist in Alina, ein Mädchen aus der Parallelklasse, verliebt und zweifelt zum ersten Mal an sein'),
        ('07:40', 'Die Pfefferkörner', 'Leos Vater', 'Serie', 35, 10, 'a10', 55, 'Leos Vater Mark taucht zufällig und offenbar aus geschäftlichen Gründen in Hamburg auf. Jasina hat s'),
    ]),
    ("Donnerstag, 20.08.2026", "SWR", [
        ('05:30', "Erklär's mir", 'Alltagsdinge, die im alten Ägypten erfunden wurden', 'Vorlesen', 3, 3, 'a3', 55, 'Der Film beleuchtet den Einfluss des Alten Ägyptens auf den heutigen Alltag. Anhand ausgewählter Bei'),
        ('05:33', "Erklär's mir", 'Sicherheitsregeln beim Experimentieren', 'Vorlesen', 4, 3, 'a3', 55, 'Sicher experimentieren im Fachraum: Experimente in der Schule sind besonders spannend, wenn es leuch'),
        ('05:37', "Erklär's mir", 'Einfache Vorlesetipps', 'Vorlesen', 3, 3, 'a3', 55, 'Mit den Vorlesetipps in diesem Video wird Vorlesen ganz einfach. Vorlesetipp Nummer eins: Wörter in '),
        ('05:40', "Erklär's mir", 'Präsentation steht an: So bleibst du entspannt', 'Vorlesen', 5, 3, 'a3', 55, 'Eine Präsentation steht bevor und man ist super aufgeregt? Kein Wunder, immerhin geht es hier um die'),
        ('12:55', 'Meine liebe Familie - Der Erbe', '', 'Serie', 90, 6, 'a6', 55, 'Barbara Herzog ist die Chefin der familieneigenen Papierfabrik Maibach, in der ihre Mutter und ihr B'),
    ]),
    ("Donnerstag, 20.08.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Dr. Brumm macht das, was er immer macht, wenn er mit Bibi verabredet ist: Er fragt sich, was sie woh'),
    ]),
    ("Donnerstag, 20.08.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Dr. Brumm: Dr. Brumm fährt Kanu'),
    ]),
    ("Donnerstag, 20.08.2026", "HR", [
        ('04:00', 'Der Kommissar und die Alpen', 'Schnee am Dienstag', 'Serie', 90, 3, 'a3', 55, 'Vice-Questore Rocco Schiavones Geduldsfaden ist am Reißen - unfähige Mitarbeiter und ein frustrieren'),
        ('06:20', 'Leo da Vinci', 'Leo der Magier', 'Zeichentrick', 10, 3, 'a3', 55, 'Gauner Robert hat aus Leos Gefährt die zwei fehlenden Seiten der "Reisen des Marco Polo" gestohlen. '),
        ('06:30', 'Leo da Vinci', 'Die Räuberbande', 'Zeichentrick', 15, 3, 'a3', 55, 'Ausgerechnet sein bester Freund Lollo hat Leos Plan vereitelt, die Gauner in die falsche Richtung zu'),
        ('11:20', 'Bezaubernde Marie', '', 'Serie', 90, 6, 'a6', 55, 'Die liebenswürdige Marie Meyer hat stets ein offenes Ohr für die Sorgen anderer. Als sie den asthmak'),
    ]),
    ("Donnerstag, 20.08.2026", "arte", [
        ('04:25', 'Verdammte Katze!', 'Geiler Stoff', 'Zeichentrick', 5, 3, 'a3', 55, 'Während Moustique sich wieder an einer seiner Lieblingsbeschäftigungen, dem Sofazerkratzen auslässt,'),
    ]),
    ("Donnerstag, 20.08.2026", "ORF 1", [
        ('06:05', 'Wickie und die starken Männer', 'Das fliegende Schiff', 'Zeichentrick', 25, 3, 'a3', 55, 'Halvars Männer haben eine Taube nach Flake geschickt. So erfährt Wickie, dass die Wikinger in Schwie'),
        ('06:30', 'Servus Kasperl', 'Kasperl & Pezi: Die Geburtstagsüberraschung', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('06:55', 'Die Jagd nach dem Kju Wang', 'Besuch vom Mars', 'Zeichentrick', 25, 3, 'a3', 55, 'Yagor belauscht zufällig ein Gespräch zwischen dem Herzog Cirillo und seiner Schwester Ardelia. Dadu'),
        ('07:40', 'Garfield', 'Garfield, der Pirat - Teil 3', 'Zeichentrick', 10, 3, 'a3', 55, 'Auf dem gekaperten Schiff von Captain Garfield und seiner Bande befindet sich bereits eine Piratin. '),
        ('07:50', 'Garfield', 'Garfield, der Pirat - Teil 4', 'Zeichentrick', 10, 3, 'a3', 55, 'Garfield und seine Freunde finden sich in einer brenzligen Situation wieder. Sie stürzen von einer B'),
    ]),
    ("Donnerstag, 20.08.2026", "SRF 1", [
        ('17:00', 'SRF Kids Inside', 'Ein bisschen gefährlicher als singen: Ab ins Kanu!', 'Vorlesen', 10, 6, 'a6', 55, 'Ein Verein, vier Kids und noch mehr Storys: «SRF Kids Inside» erzählt Geschichten mitten aus dem Leb'),
        ('17:10', 'SRF Kids Inside', 'Aufnahmeprüfung Musicalschule - Next stop: Broadway New York?', 'Vorlesen', 15, 6, 'a6', 55, 'Ein Verein, vier Kids und noch mehr Storys: «SRF Kids Inside» erzählt Geschichten mitten aus dem Leb'),
        ('17:25', 'SRF Kids', '#SayHi 2026 - Zu Besuch bei den Songaufnahmen von «Alli zäme» ?', 'Vorlesen', 5, 6, 'a6', 55, 'Was ist #SayHi? Jedes Jahr folgen Tausende Kinder dem Aufruf von SRF Kids, zum #SayHi-Song gegen Mob'),
        ('17:30', 'BooSnoo! - Rägeboge', '', 'Zeichentrick', 10, 6, 'a6', 55, 'BooSnoo, der rote Ball, geht auf Reisen. Fliessende Bewegungen, sanfte Rhythmen - BooSnoo beruhigt, '),
    ]),
]
