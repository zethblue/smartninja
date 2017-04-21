"""
script6.py: Usereingabe Beispiele, Kopie mit Zahlen abgewandelt
ist Script3 mit Schleife zum Fortsetzen bei Falscheingabe
"""
if __name__ == '__main__':
    # Eingabe Zahl
    X = 1

    while X == 1:
        try:

            zahl = raw_input("Nenne eine Zahl bitte")
            # Zahl wird von TextString in eine Zahl umgewandelt mit int/float
            zahl = float(zahl)
            # Berechnung der Haelfte
            msg = zahl / 2.
            # Ausgabe der Haelfte
            print msg
            X = X + 1

        except:
            print "Sorry, your entry could not be interpreted"
            print "Please enter a valid number"
            continue
       