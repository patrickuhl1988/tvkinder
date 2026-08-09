# -*- coding: utf-8 -*-
"""
detail_data.py — ausführliche Eltern-Einschätzungen

Gilt für alle Sendungen ab dem 01.08.2026. Für heute und morgen bleibt die
kurze Fassung: Wer in zwei Stunden eine Entscheidung braucht, liest keinen
Fließtext. Wer für Samstag plant, schon.

Je Titel:
    lang   — was passiert, was daran anstrengend oder anrührend ist,
             für wen es wirklich passt
    flags  — kurze Schlagworte für das, was auffallen könnte
    reden  — eine konkrete Frage oder ein Thema fürs Gespräch danach

Die Einschätzungen sind redaktionell und ersetzen kein eigenes Ansehen.
"""

DETAIL = {
    "Tom Turbo": dict(
        lang="Interaktive Krimiserie: Das Fahrrad Tom Turbo löst mit den Zuschauerkindern "
             "einen Fall, zwischendurch wird direkt in die Kamera gefragt und zum Mitraten "
             "aufgefordert. Kein Tempo, keine Bedrohung, die Fälle lösen sich immer "
             "freundlich auf. Für Kinder, die gerne mitdenken und sich trauen zu rufen, "
             "ist das ideal — wer lieber passiv schaut, langweilt sich womöglich.",
        flags=["ruhig", "zum Mitraten", "keine Gefahr"],
        reden="Welche Spur hättet ihr selbst zuerst verfolgt?"),

    "Bolt": dict(
        lang="Ein Serienhund hält seine Fernsehrolle für echt und macht sich quer durch "
             "die USA auf den Weg zu seiner Besitzerin. Der Kern ist eine Trennungs- und "
             "Heimkehrgeschichte, und die trifft manche Kinder stärker als erwartet: Bolt "
             "glaubt zwischenzeitlich, Penny habe ihn aufgegeben. Am Ende gibt es einen "
             "Brand im Studio mit echter Gefahr für beide. Ab sechs gut zu verkraften, "
             "darunter lieber gemeinsam schauen.",
        flags=["Trennung", "Brandszene am Ende", "warmherzig"],
        reden="Woran hat Bolt gemerkt, dass er auch ohne Superkräfte etwas wert ist?"),

    "Pippi Langstrumpf": dict(
        lang="Die schwedische Verfilmung von 1969, in Serienlänge geschnitten. Erzähltempo "
             "und Bildsprache sind langsam, das ist für heutige Sehgewohnheiten "
             "gewöhnungsbedürftig und genau deshalb erholsam. Pippi lebt allein, hat Geld "
             "und macht sich über Erwachsene lustig — manche Kinder probieren das danach "
             "aus. Inhaltlich harmlos, aber ein paar Szenen und Begriffe stammen erkennbar "
             "aus ihrer Zeit.",
        flags=["langsam", "Vorbild mit Widerhaken", "Klassiker"],
        reden="Was findet ihr gut daran, dass Pippi keine Regeln befolgt — und was nicht?"),

    "Hans im Glück": dict(
        lang="Grimm-Märchen als Realverfilmung: Hans tauscht sich Schritt für Schritt vom "
             "Goldklumpen bis zum Nichts herunter und ist am Ende der Glücklichste. Sehr "
             "ruhig erzählt, keine bedrohlichen Figuren, klarer Ablauf. Die Moral ist "
             "sperrig — jüngere Kinder verstehen sie oft als „Hans ist dumm\", worüber sich "
             "gut reden lässt.",
        flags=["sehr ruhig", "Märchenmoral", "keine Gruselszenen"],
        reden="War Hans am Ende wirklich glücklich oder hat er sich nur überreden lassen?"),

    "Findet Dorie": dict(
        lang="Dorie sucht ihre Eltern und kämpft dabei mit ihrer Vergesslichkeit. Der Film "
             "ist warmherzig und witzig, hat aber einen ernsten Kern: In Rückblenden sieht "
             "man die kleine Dorie ihre Eltern verlieren, und ihre Panik, wenn sie den Faden "
             "verliert, ist glaubwürdig gespielt. Für Kinder mit Trennungsangst kann das viel "
             "sein. Ab sechs meist gut, sensible Vierjährige besser in Begleitung.",
        flags=["Elternsuche", "Rückblenden traurig", "Behinderung als Thema"],
        reden="Dorie kann sich nichts merken und schafft es trotzdem. Wie hat sie das gemacht?"),

    "Minions": dict(
        lang="Slapstick am laufenden Band, Handlung nur als Vorwand. Die Minions suchen "
             "einen neuen Bösewicht und landen bei Scarlet Overkill. Sehr laut, sehr schnell, "
             "praktisch ohne ruhige Momente — als Abendprogramm vor dem Schlafengehen "
             "ungünstig. Inhaltlich harmlos, die Gewalt ist durchgehend Cartoon-Gewalt ohne "
             "Folgen. Kinder lieben es, Eltern finden es oft anstrengend.",
        flags=["sehr laut", "hohes Tempo", "wenig Handlung"],
        reden="Braucht es nach dem Film noch etwas Ruhiges, bevor es ins Bett geht?"),

    "Charlie & Louise": dict(
        lang="Zwillinge, die getrennt bei Mutter und Vater aufwachsen, treffen sich zufällig "
             "im Ferienlager und tauschen die Rollen, um die Eltern wieder zusammenzubringen. "
             "Das Thema Trennung wird ernst genommen und nicht wegerzählt. Für Kinder aus "
             "getrennten Familien kann das sehr nah kommen — im guten wie im schwierigen "
             "Sinn. Der Ton ist warm, das Ende versöhnlich.",
        flags=["Trennung der Eltern", "Rollentausch", "ruhig erzählt"],
        reden="Warum haben die beiden es den Eltern nicht einfach gesagt?"),

    "Arielle, die Meerjungfrau": dict(
        lang="Disney-Klassiker von 1989 mit starken Bildern und Ohrwürmern. Die Meerhexe "
             "Ursula ist für kleinere Kinder der Knackpunkt: Sie wird am Ende riesig, die "
             "Szene ist dunkel und laut und hat schon manches Kind aus dem Sessel geholt. "
             "Dazu kommt der Stoff selbst — Arielle gibt ihre Stimme auf, um bei einem "
             "Mann zu sein. Das lässt sich mit älteren Kindern gut auseinandernehmen.",
        flags=["Ursula erschreckt", "dunkles Finale", "Streit mit dem Vater"],
        reden="Hätte Arielle einen anderen Weg gehabt, als ihre Stimme herzugeben?"),

    "Pünktchen und Anton": dict(
        lang="Caroline Links Kästner-Verfilmung über zwei Kinder aus sehr verschiedenen "
             "Verhältnissen. Anton pflegt seine kranke Mutter und arbeitet nachts, während "
             "Pünktchens Eltern kaum zu Hause sind — beides wird ohne Beschönigung gezeigt. "
             "Inhaltlich stark und für Grundschulkinder gut zugänglich, emotional aber "
             "fordernder als eine Zeichentrickfolge. Der Sendeplatz um 22:10 spricht ohnehin "
             "fürs Aufnehmen.",
        flags=["soziale Ungleichheit", "krankes Elternteil", "später Sendeplatz"],
        reden="Was hat Anton, das Pünktchen nicht hat — und umgekehrt?"),

    "Der Schuh des Manitu": dict(
        lang="Kein Kinderfilm, auch wenn die Quelle ihn unter Familienfilm führt. "
             "Westernparodie mit Anspielungen, die auf Erwachsene zielen, dazu ein "
             "Humor über Herkunft und Sexualität, der heute streckenweise unangenehm "
             "wirkt. Läuft um 22:35 und gehört auf dieser Seite eigentlich nur der "
             "Vollständigkeit halber.",
        flags=["kein Kinderfilm", "Anspielungen", "22:35 Uhr"],
        reden="Für gemeinsames Schauen mit Kindern nicht geeignet."),

    "Mary Poppins' Rückkehr": dict(
        lang="Die Fortsetzung setzt nach dem Tod der Mutter an: Die Familie Banks trauert "
             "und droht ihr Haus zu verlieren. Das ist der Rahmen, in dem die Musik- und "
             "Trickfilmnummern stattfinden, und es wird nicht weggewischt. Für Kinder, die "
             "selbst einen Verlust erlebt haben, kann der Film sehr nah gehen. Ansonsten "
             "ein warmer, sehr schön ausgestatteter Film — der Sendeplatz um 4 Uhr nachts "
             "macht ihn allerdings zur reinen Aufnahmesache.",
        flags=["Tod der Mutter", "Trauer", "4 Uhr nachts"],
        reden="Was hilft der Familie im Film dabei, wieder fröhlich zu werden?"),

    "Ostwind (3)": dict(
        lang="Dritter Teil der Pferdefilmreihe. Mika bricht mit Ostwind nach Andalusien auf, "
             "es geht um Verantwortung, Loslassen und darum, dass gut gemeint nicht gut "
             "gemacht ist. Ein paar Szenen mit Gefahr für die Pferde, aber ohne drastische "
             "Bilder. Wer die ersten beiden Teile nicht kennt, kommt trotzdem mit. Gute "
             "Wahl für den Sonntagvormittag.",
        flags=["Tiere in Gefahr", "Freundschaft", "ohne Vorkenntnisse verständlich"],
        reden="Wann muss man ein Tier gehen lassen, auch wenn man es liebt?"),

    "Das Märchen von der silbernen Brücke": dict(
        lang="Neues ARD-Märchen von 2024, hier als Sommerwiederholung. Klassischer Aufbau "
             "mit Prüfung, Widersacher und gutem Ende, aufwendig ausgestattet und in "
             "gemächlichem Tempo erzählt. Keine Schreckmomente, die über das übliche "
             "Märchenmaß hinausgehen. Eine Stunde Länge macht es auch für Sechsjährige "
             "gut überschaubar.",
        flags=["klassisches Märchen", "eine Stunde", "keine Schrecksekunden"],
        reden="Welche Prüfung war die schwierigste — und hättet ihr sie geschafft?"),

    "Himmel und Huhn": dict(
        lang="Ein kleines Huhn wird nach einer Falschmeldung zum Gespött des ganzen Ortes "
             "und muss dann die Erde vor Außerirdischen retten. Unter dem Trubel liegt eine "
             "Vater-Sohn-Geschichte: Der Vater glaubt seinem Kind lange nicht, und das ist "
             "ehrlich unangenehm zu sehen. Das Tempo ist hoch, die Gagdichte ebenso. Für "
             "Kinder, die selbst gerade um Anerkennung ringen, überraschend berührend.",
        flags=["Vater glaubt nicht", "hohes Tempo", "Ausgelachtwerden"],
        reden="Wie fühlt es sich an, wenn einem niemand glaubt?"),

    "Angry Birds – Der Film": dict(
        lang="Verfilmung der Spiele-App. Der Held ist ein Vogel mit Wutproblem, und der Film "
             "erzählt Wut über weite Strecken als Pointe statt als Thema — am Ende ist sie "
             "sogar die Rettung. Dazu einige derbe Gags und viel Zerstörung. Unterhaltsam, "
             "aber erzählerisch dünn, und für Kinder, die gerade selbst an Wutausbrüchen "
             "arbeiten, ein zwiespältiges Vorbild.",
        flags=["Wut als Gag", "viel Zerstörung", "derbe Sprüche"],
        reden="Wann hilft Wut wirklich weiter, und wann macht sie es schlimmer?"),

    "Ritter Rost 2": dict(
        lang="Deutscher Animationsfilm mit vielen Liedern, gebaut wie ein Musical. "
             "Schrottland ist pleite, Ritter Rost soll sparen — die Geschichte bleibt "
             "durchgehend freundlich, die Konflikte lösen sich singend. Werbefreier "
             "Sendeplatz am Sonntagmittag auf KiKA. Für Kinder, die Musik mögen, eine "
             "der entspanntesten Möglichkeiten, achtzig Minuten zu füllen.",
        flags=["viel Musik", "werbefrei", "keine Bedrohung"],
        reden="Welches Lied ist hängengeblieben?"),

    "Dornröschen": dict(
        lang="Grimm-Verfilmung aus der ARD-Märchenreihe, eine Stunde lang und ruhig "
             "inszeniert. Der Fluch der dreizehnten Fee und der hundertjährige Schlaf sind "
             "die einzigen düsteren Momente und bleiben bildlich zurückhaltend. Solide "
             "Märchenkost für Sechsjährige, ohne Überraschungen in beide Richtungen.",
        flags=["Fluch", "ruhig inszeniert", "kurz"],
        reden="Warum hat die dreizehnte Fee sich so geärgert?"),

    "Heidi": dict(
        lang="Heidi wird von der Alm nach Frankfurt gebracht und leidet dort massiv unter "
             "Heimweh — das ist der emotionale Kern und wird nicht abgekürzt. Dazu kommt "
             "Klara, die im Rollstuhl sitzt, und Fräulein Rottenmeier als strenge "
             "Erzieherin. Bildstark und ruhig erzählt, aber die Trennung vom Großvater "
             "trifft besonders jüngere Kinder. Achtung: Die Quelle nennt widersprüchliche "
             "Jahresangaben, es dürfte die neuere Verfilmung sein.",
        flags=["Heimweh", "Trennung", "Behinderung als Thema"],
        reden="Was hätte Heidi in Frankfurt geholfen, damit es ihr besser geht?"),

    "Der Zauberlehrling": dict(
        lang="Märchenverfilmung um einen Jungen, der beim falschen Meister landet und in "
             "einen Machtkampf gerät. Deutlich düsterer als die üblichen ARD-Märchen: "
             "Der Apotheker Zacharias ist eine echte Bedrohung, und es geht um Gier und "
             "Verrat. Für Achtjährige gut, für Sechsjährige je nach Kind zu viel.",
        flags=["düsterer als üblich", "bedrohlicher Gegenspieler", "Machtkampf"],
        reden="Woran hätte Valentin früher merken können, dass etwas nicht stimmt?"),

    "Der König der Löwen 2": dict(
        lang="Die Fortsetzung dreht sich um Kiara und Kovu, dessen Mutter Zira auf Rache "
             "aus ist. Der Ton ist ernster als beim ersten Teil: Es gibt einen Steppenbrand, "
             "einen Kampf zwischen zwei Rudeln und einen Tod. Kovu trägt eine Narbe und "
             "wird als Ausgestoßener behandelt — das Thema Vorurteil ist gut angelegt. "
             "Für sensible Kinder sind die Kampfszenen der Knackpunkt.",
        flags=["Kämpfe", "Steppenbrand", "Ausgrenzung", "ein Tod"],
        reden="Warum haben alle Kovu misstraut, obwohl er nichts getan hatte?"),

    "Jim Knopf und Lukas der Lokomotivführer": dict(
        lang="Aufwendige Verfilmung des Michael-Ende-Klassikers mit echten Schauplätzen. "
             "Der Knackpunkt ist Frau Mahlzahn: Der Drache ist groß, laut und für "
             "Vorschulkinder ernsthaft angsteinflößend, auch wenn er am Ende gezähmt wird. "
             "Dazu die Frage nach Jims Herkunft, die feinfühlig erzählt ist. Ab sechs "
             "gut, mit über zwei Stunden plus Werbepausen aber ein langer Abend — die "
             "Ausstrahlung um 20:15 endet gegen 22:30.",
        flags=["Drache macht Angst", "über zwei Stunden", "Herkunft als Thema"],
        reden="Wie hat Jim herausgefunden, wo er hingehört?"),
}


def lookup(title):
    return DETAIL.get(title)
