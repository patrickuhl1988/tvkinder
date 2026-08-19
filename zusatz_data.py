# -*- coding: utf-8 -*-
"""Kindersendungen der Vollprogramme.

Erzeugt von scan_kinder.py aus tv.de am 19.08.2026. Auswahl nach Kategorie,
bekannten Titeln und Beschreibung; Alterswerte heuristisch.
"""

TAGE = [
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
        ('23:45', 'Der Kommissar und die Alpen', 'Schnee am Dienstag', 'Serie', 25, 10, 'a10', 55, 'Vice-Questore Rocco Schiavones Geduldsfaden ist am Reißen - unfähige Mitarbeiter und ein frustrieren'),
    ]),
    ("Mittwoch, 19.08.2026", "ORF 1", [
        ('06:52', 'Die Jagd nach dem Kju Wang', 'Sesam, öffne dich', 'Zeichentrick', 24, 3, 'a3', 55, 'Die neueste Errungenschaft des Herzogs hält im Palast Einzug: Eine Panzertür mit Spracherkennungsmod'),
        ('07:33', 'Garfield', 'Garfield, der Pirat - Teil 1', 'Zeichentrick', 14, 3, 'a3', 55, 'Garfield ist ein gefürchteter Pirat. Er und seine Mannschaft kapern andere Schiffe nach Belieben. Er'),
        ('07:47', 'Garfield', 'Garfield, der Pirat - Teil 2', 'Zeichentrick', 14, 3, 'a3', 55, 'Captain Garfield und Admiral Nermal stellen zu ihrem Erstaunen fest, dass sie auf der einsamen Insel'),
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
        ('17:35', 'Detektiv Conan', 'Das Messer der Waldhexe (1)', 'Anime', 30, 12, 'a10', 55, 'Professor Agasa will mit den Kindern campen gehen, doch die Gruppe verirrt sich im Wald. In einem ab'),
        ('18:05', 'One Piece', 'Tot oder lebendig! - Ein schicksalshafter Countdown', 'Anime', 25, 12, 'a10', 55, 'Gatz verkündet, dass Ruffy zurückkehren und De Flamingo endgültig besiegen wird. Dieser ist außer si'),
        ('18:30', 'One Piece', 'Himmelskampf - Ruffys rasende King Kong Gun!', 'Anime', 25, 12, 'a10', 55, 'De Flamingo und Ruffy nehmen ihren Kampf wieder auf: Ruffy gelingt der Befreiungsschlag auf den Fäng'),
        ('18:55', 'Detektiv Conan', 'Zahlenspiele', 'Anime', 30, 12, 'a10', 55, 'Als Conan mit seinen Jungs nach Hause kommt, bemerkt er eine noch nicht abgehörte Nachricht auf sein'),
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
    ("Freitag, 21.08.2026", "ProSieben Maxx", [
        ('16:40', 'Dr. STONE', 'Medusas wahres Gesicht', 'Anime', 25, 12, 'a10', 55, 'Mithilfe der Entsteinerungsflüssigkeit gelingt es Senku und seinen Freunden, Kaseki wiederzubeleben.'),
        ('17:05', 'Dragon Ball Super', 'Zeig sie uns! Krillins verborgene Kraft!', 'Anime', 25, 12, 'a10', 55, 'Geschockt von der Vernichtung der ersten Verlierer, wägen die Kämpfer ihre Taktiken neu ab. Umso ver'),
        ('17:30', 'Detektiv Conan', 'Das Messer der Waldhexe (2)', 'Anime', 30, 12, 'a10', 55, 'Inspektor Yamamura rückt an, um den Mord an Akane Ooba in dem einsamen Haus im Wald aufzuklären. Mit'),
        ('18:00', 'One Piece', 'Für die Freiheit! - Dressrosas Freudentränen', 'Anime', 25, 12, 'a10', 55, 'Die Einwohner von Dressrosa feiern De Flamingos Niederlage. Sie beklagen alle das Leid, dass sie unt'),
        ('18:25', 'One Piece', 'Unglaublich! - Admiral Fujitoras überraschende Entscheidung', 'Anime', 30, 12, 'a10', 55, 'Die Hafenpolizei nimmt alle Donquixote Piraten in Gewahrsam, außer Viola, Baby 5 und Bellamy. Maynar'),
        ('18:55', 'Detektiv Conan', 'Der mysteriöse Scharfschütze (1)', 'Anime', 25, 12, 'a10', 55, 'Kogoro nimmt an einer Party in der Veranstaltungshalle eines Hotels teil, bei der auch Conan und Ran'),
        ('20:15', 'Ame & Yuki - Die Wolfskinder', '', 'Serie', 135, 10, 'a10', 55, 'Die junge Studentin Hana ist über beide Ohren verliebt in einen Mann, der sich als Wolfsmensch entpu'),
        ('22:30', 'Gachiakuta', 'Der Himmel', 'Anime', 30, 12, 'a10', 55, 'Rudo lebt in einer Welt, in der die Oberschicht sich ihres Besitzes achtlos entledigt und alles sofo'),
        ('23:00', 'Gachiakuta', 'Was innewohnt', 'Anime', 20, 12, 'a10', 55, 'Rudo wird von mehreren Müllmonstern in die Enge getrieben und nimmt den Kampf mit ihnen auf. Ein mys'),
        ('23:20', 'Gachiakuta', 'Die Unterwelt', 'Anime', 30, 12, 'a10', 55, 'Enjin rekrutiert Rudo für den sogenannten Putztrupp, da seine neu erwachte Fähigkeit als Giver im Ka'),
    ]),
    ("Freitag, 21.08.2026", "WDR", [
        ('07:25', 'Campsite', 'Der geheime Club', 'Jugendserie', 5, 3, 'a3', 55, 'Nura und Silje folgen Thea heimlich zum Fundsachenraum, wo sie überraschend auf verschlossene Türen '),
        ('07:30', 'Campsite', 'Dirty Dancing', 'Jugendserie', 10, 3, 'a3', 55, 'Sebbe plant eine große romantische Aktion auf der Campingplatz-Party, inspiriert von dem Film "Dirty'),
        ('07:40', 'Campsite', 'Lost and Found', 'Jugendserie', 5, 3, 'a3', 55, 'Theo, Thea, Nura und Silja kramen sich durch merkwürdige Sachen im Fundraum des Campingplatzes, als '),
        ('07:45', 'Max und die wilde 7', '', 'Film', 85, 3, 'a3', 55, 'Eine echte Ritterburg als neues Zuhause - kann man sich etwas Cooleres vorstellen? Ja, kann man, fin'),
    ]),
    ("Freitag, 21.08.2026", "NDR", [
        ('06:00', 'Sesamstraße', '', 'Vorlesen', 20, 3, 'a3', 55, 'Bert hat ein Experiment zur Lichtbrechung aufgebaut. Er will zeigen, wie eine Münze, die unter einem'),
        ('06:20', 'Schloss Einstein', 'Der Code-Knacker', 'Jugendserie', 25, 10, 'a10', 55, 'Joshua beschließt, dem Schatzsuche-Team um Maxi zu helfen. Die Lösung des Rätsels führt jedoch nicht'),
        ('06:45', 'Schloss Einstein', 'Noahs Geständnis', 'Jugendserie', 25, 10, 'a10', 55, 'Noahs Reise nach Köln nimmt eine überraschende Wendung. Maxi erfährt Oma Maggies Geheimnis und stell'),
        ('07:10', 'Die Pfefferkörner', 'Das Geisterhaus', 'Serie', 30, 10, 'a10', 55, 'In dem alten Haus von Tante Gordy spukt es. Amy beschließt, bei Gordy zu übernachten, um der Sache n'),
        ('07:40', 'Die Pfefferkörner', 'Peking-Kracher', 'Serie', 35, 10, 'a10', 55, 'Hakim ist mit Alina und seiner Schwester im Hafenmuseum. Jasina ist davon überzeugt, dass die beiden'),
    ]),
    ("Freitag, 21.08.2026", "SWR", [
        ('12:55', 'Meine liebe Familie - Zeit für Veränderung', '', 'Serie', 90, 6, 'a6', 55, 'Ausgerechnet mit Hilfe ihres Widersachers Marius Perlinger kann Barbara Herzog den drohenden Verkauf'),
    ]),
    ("Freitag, 21.08.2026", "MDR", [
        ('18:54', 'Unser Sandmännchen', '', 'Serie', 6, 3, 'a3', 55, 'Spielerisch das ABC lernen: Von A wie Affe, bis Z wie Zebra findet in diesem Song jedes Tier seinen '),
    ]),
    ("Freitag, 21.08.2026", "RBB", [
        ('17:53', 'Unser Sandmännchen', '', 'Serie', 7, 3, 'a3', 55, 'Liedergeschichten: Tier-ABC'),
    ]),
    ("Freitag, 21.08.2026", "HR", [
        ('06:25', 'Leo da Vinci', 'Mission Brombeere', 'Zeichentrick', 10, 3, 'a3', 55, 'Dank Lollos Heilmittel werden Leo und seine Freunde von der Räuberbande des "Schäfers" freigelassen.'),
        ('06:35', 'Leo da Vinci', 'Die Da Vinci - Brücke', 'Zeichentrick', 15, 3, 'a3', 55, 'Endlich hat Leo seine Verfolger abschütteln können. Diese sind noch immer auf der Suche nach ihren P'),
        ('11:25', 'Brücke zum Herzen', '', 'Serie', 85, 6, 'a6', 55, 'Die erfolgreiche Ärztin Karen Tillner traut ihren Augen kaum, als eines Tages plötzlich ihr Vater vo'),
    ]),
    ("Freitag, 21.08.2026", "arte", [
        ('04:15', 'Verdammte Katze!', 'Mein Revier', 'Zeichentrick', 5, 3, 'a3', 55, 'Wo Moustique und Stéphane sich niemals einig werden, ist das Sofa. Moustique liebt es, Stéphanes Sof'),
    ]),
    ("Freitag, 21.08.2026", "ORF 1", [
        ('06:00', 'ZIB KiDS', '', 'Serie', 10, 3, 'a3', 55, ''),
        ('06:10', 'Wickie und die starken Männer', 'Der dicke König', 'Zeichentrick', 25, 3, 'a3', 55, 'Die Wikinger landen im Land der Bulgaren und werden von einem König, der ständig von Hunger geplagt '),
        ('06:35', 'Servus Kasperl', 'Kasperl & Strolchi: Simsis Einladung nach Afrika', 'Serie', 25, 3, 'a3', 55, 'Der Klassiker des österreichischen Kinderfernsehens mit amüsanten Kasperlstücken und vielen Möglichk'),
        ('07:00', 'Die Jagd nach dem Kju Wang', 'Eine hinterhältige Maschine', 'Zeichentrick', 25, 3, 'a3', 55, 'Ein Beben erschüttert Venedig. Kurz darauf fordert der Rattenkönig in einem Brief das sofortige Abda'),
        ('07:40', 'Galapagos X', 'Kleiner Goldfisch - große Folgen', 'Zeichentrick', 10, 3, 'a3', 55, 'Die ganze Stadt wird von Goldfischen geflutet. Irgendetwas ist da in der Vergangenheit gehörig schie'),
        ('07:50', 'ZIB KiDS', '', 'Serie', 10, 3, 'a3', 55, ''),
    ]),
    ("Freitag, 21.08.2026", "SRF 1", [
        ('17:30', 'BooSnoo! - Wältall', '', 'Zeichentrick', 10, 6, 'a6', 55, 'BooSnoo, der rote Ball, geht auf Reisen. Fliessende Bewegungen, sanfte Rhythmen - BooSnoo beruhigt, '),
    ]),
]
