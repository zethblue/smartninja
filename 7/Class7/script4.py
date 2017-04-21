"""
Selfstudy Programm
2 Zahlen auswaehlen, die Rechnungsart auswaehlen und auswerten lassen
"""

if __name__ == '__main__':
    #Eingabe der ersten Zahl
    print "Willkommen beim Calculator. Hier koennen Sie Addieren, Multiplizieren, Dividieren und Subtrahieren"
    Zahl1 = raw_input("Bitte geben Sie die erste Zahl ein: " )
    try:
        Zahl1 = float(Zahl1)
    except:
        print "Bitte geben Sie eine gueltige Zahl ein"
        exit()
    #Eingabe der zweiten Zahl
    Zahl2 = raw_input("Bitte geben Sie die zweite Zahl ein: ")
    try:
        Zahl2 = float(Zahl2)
    except:
        print "Bitte geben Sie eine gueltige Zahl ein"
        exit()
    #Waehle die Vorgangsweise
    try:
        Vorgang = raw_input("bitte geben sie M zum Multiplizieren, A zum Addieren, D zum Dividieren, S zum Subtrahieren ein: ")
        if Vorgang == "M":
            Ergebnis = Zahl1 * Zahl2
        elif Vorgang == "A":
            Ergebnis = Zahl1 + Zahl2
        elif Vorgang == "D":
            Ergebis = Zahl1 / Zahl2
        elif Vorgang =="S":
            Ergebnis = Zahl1 - Zahl2

        #Ausgabe
        print Ergebnis
    except:
        print "Vorgang nicht moeglich. Bitte waehlen Sie eine der folgenden Eingaben: M A D oder S"


