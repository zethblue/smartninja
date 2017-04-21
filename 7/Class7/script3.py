"""
script3.py: Usereingabe Beispiele, Kopie mit Zahlen abgewandelt
"""

if __name__ == '__main__':
    # Eingabe Zahl
    try:

        zahl = raw_input("Nenne eine Zahl bitte")
        # Zahl wird von TextString in eine Zahl umgewandelt mit int/float
        zahl = float(zahl)
        # Berechnung der Haelfte
        msg = zahl / 2.
        # Ausgabe der Haelfte
        print msg
    except:
        print "Sorry, your entry could not be interpreted"
        print "Please enter a valid number"