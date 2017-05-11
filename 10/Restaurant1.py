# coding=utf-8

tagesmenus = []


if __name__ == '__main__':

    while True:
        answer = raw_input("Was ,möchtest du machen?\n"
                           "(1) Alle Gerichte anzeigen\n"
                           "(2) Set (Vorspeise, Hauptspeise, Nachspeise) hinzufügen\n"
                           "(3) Schreibe Menü in ein File\n"
                           "(4) Set löschen\n"
                           "(q) Programm verlassen\n")
        if answer.lower() == "q": ##.lower heißt dass kleincshreibung/grossscheibung egal ist
            break
        elif answer == "1":
            print "Gerichte werden angezeigt"
            print "*"*30

            for xxy in tagesmenus:
                for speise, info in xxy.iteritems():
                    print speise, info
                    # Es gibt .iteritems(), .keys(), values(). Values gibt eine Liste der Werte, keys gibt die Keys der Liste, iteritems ist keys+werte
                    # for k, v in a.iteritems() - print k gibt nur das 1. tuple zurück, print v gibt nur das 2. tuple zurück

        elif answer == "2":
            print
            print "Set hinzufügen"
            print "*"*30
            speisentypen = ("Vorspeise", "Hauptspeise", "Nachspeise")
            menuset = dict()
            for xxx in speisentypen:
                name = raw_input("Was ist Name der {}?\n".format(xxx))
                preis = raw_input("Was ist der Preis der {}?\n".format(xxx))
                # menuset[SCHLÜSSEL] = (ADDME1, ADDME2)
                menuset[xxx] = (name, preis)
            tagesmenus.append(menuset)

        elif answer == "3":
            print "Schreibe Menü in ein File"
            content = ""
            for xxy in tagesmenus:
                for speise, info in xxy.iteritems():
                    content += str(speise) + " " + str(info) + "\n"
            with open("menukarte.txt","w") as f:
                # with open heißt in ein File schreiben/lesen. option r ist read only, option w ist überschreiben, option a ist append
                f.write(content)

        elif answer == "4":
            # todo: set löschen
            print "Set löschen"
        else:
            print "unknown input"

    print "Exit Restaurant Program"


