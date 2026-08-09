# -*- coding: utf-8 -*-
"""Aktuelle Kinderfilme im Kino. Manuell gepflegt; Stand siehe STAND.
Felder: t = Titel, fsk = Freigabe ("0", "6" oder "" wenn noch offen),
dauer = Minuten (0 wenn unbekannt), start = Kinostart TT.MM.JJJJ,
kurz/kurz_en = Kurzbeschreibung DE/EN."""

STAND = "09.08.2026"

KINO = [
    dict(t="Paw Patrol 3: Der Dino-Film", fsk="0", dauer=88, start="06.08.2026",
         kurz="Marshall, Chase und die anderen Fellfreunde stranden auf einer "
              "Insel voller Dinosaurier. Mit dem Dino-Experten Rex an ihrer "
              "Seite müssen sie die Insel und ihre Urzeit-Bewohner retten.",
         kurz_en="Marshall, Chase and the pups get stranded on an island full "
                 "of dinosaurs. With dino expert Rex at their side they must "
                 "save the island and its prehistoric inhabitants."),
    dict(t="Toy Story 5", fsk="0", dauer=102, start="23.07.2026",
         kurz="Woody, Buzz und Jessie stehen vor ihrer bisher größten "
              "Aufgabe: Ihre Besitzerin Bonnie ist das letzte Kind, das noch "
              "mit analogem Spielzeug spielt.",
         kurz_en="Woody, Buzz and Jessie face their biggest challenge yet: "
                 "their owner Bonnie is the last kid still playing with "
                 "analogue toys."),
    dict(t="Minions & Monster", fsk="6", dauer=89, start="01.07.2026",
         kurz="Die Minions wollen ihren eigenen Monsterfilm drehen und "
              "beschwören dafür echte Monster herbei. Als die zur Gefahr "
              "werden, müssen die gelben Chaoten sie wieder stoppen.",
         kurz_en="The Minions set out to shoot their own monster movie and "
                 "summon real monsters to help. When those become a threat, "
                 "the little yellow troublemakers must stop them."),
    dict(t="Vaiana", fsk="6", dauer=0, start="09.07.2026",
         kurz="Realverfilmung des Disney-Abenteuers: Vaiana folgt dem Ruf "
              "des Ozeans, um ihre Heimatinsel zu retten. Mit Dwayne Johnson "
              "als Halbgott Maui.",
         kurz_en="Live-action remake of the Disney adventure: Moana follows "
                 "the call of the ocean to save her home island, with Dwayne "
                 "Johnson as demigod Maui."),
    dict(t="Chihiros Reise ins Zauberland", fsk="0", dauer=125, start="13.08.2026",
         kurz="Miyazakis Meisterwerk zurück auf der großen Leinwand: Die "
              "zehnjährige Chihiro gerät in eine Welt der Geister und "
              "Götter und muss dort ihre Eltern befreien. Für geübte "
              "Kinokinder ab etwa 8.",
         kurz_en="Miyazaki's masterpiece back on the big screen: ten-year-old "
                 "Chihiro stumbles into a world of spirits and gods and must "
                 "free her parents. Best for seasoned young viewers around 8+."),
    dict(t="Die Wilden Kerle 4", fsk="6", dauer=0, start="13.08.2026",
         kurz="Die Fußball-Bande kehrt ins Kino zurück: Die Wilden Kerle "
              "treten gegen die unheimlichen Silberlichten an.",
         kurz_en="The football gang returns to cinemas: the Wild Soccer "
                 "Bunch face off against the eerie Silverlights."),
    dict(t="Marsupilami", fsk="6", dauer=99, start="20.08.2026",
         kurz="Abenteuerfilm nach den beliebten Comics: Das quirlige "
              "Fabelwesen mit dem endlosen Schwanz wirbelt durch den "
              "Dschungel und hält alle auf Trab.",
         kurz_en="Adventure film based on the beloved comics: the whirlwind "
                 "creature with the endless tail races through the jungle "
                 "and keeps everyone on their toes."),
    dict(t="Tad Stones und die Wunderlampe", fsk="", dauer=0, start="27.08.2026",
         kurz="Der tollpatschige Abenteurer Tad ist zurück: Als sein Kumpel, "
              "die Mumie, eine magische Wunderlampe findet, beginnt eine "
              "turbulente Schatzjagd.",
         kurz_en="Clumsy adventurer Tad is back: when his mummy buddy finds "
                 "a magical wonder lamp, a turbulent treasure hunt begins."),
]
