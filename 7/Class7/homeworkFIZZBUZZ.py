"""FIZZBUZZ Hausuebung"""

X = 1
if __name__ == '__main__':

    print "Bitte geben Sie eine Zahl zwischen 1 und 100 ein\n"
    while X == 1:
        ZAHL1 = raw_input()
        try:
            ZAHL1 =float(ZAHL1)

        #keine Zahl eingegeben
        except:
            print "Ihre Eingabe ist fehlerhaft. Bitte geben Sie eine korrekte Zahl zwischen 1 und 100 ein"
            continue
        #Zahl zu gross
        if ZAHL1 > 100:
             print "Die Zahl ist zu gross. Bitte geben Sie eine Zahl zwischen 1 und 100 ein"
             continue
        #Zahl zu klein
        elif ZAHL1 < 1:
            print "Die Zahl ist zu klein. Bitte geben Sie eine Zahl zwischen 1 und 100 ein"
            continue
        #Alles roger. Schleifen Ende
        else:
            print "BIZZFUZZ is starting"
            X = X + 1

    while ZAHL1 < 300:
        #Zahlen raufzaehlen
        ZAHL1 = ZAHL1 + 1
        #Zahl ist durch 3 aber nicht durch 5 teilbar gibt FIZZ
        if ZAHL1 % 3 == 0 and ZAHL1 % 5 != 0:
            print "FIZZ"
        #Zahl ist durch 5 aber nicht durch 4 teilbar gibt BUZZ
        elif ZAHL1 % 5 == 0 and ZAHL1 % 3 != 0:
            print "BUZZ"
        #Zahl ist durch 5 und durch 3 teilbar gibt FIZZBUZZ
        elif ZAHL1 % 3 == 0 and ZAHL1 % 5 == 0:
            print "FIZZBUZZ"
        #Zahl ist weder das eine noch das andere gibt normale Zahlenausgabe
        else:
            print ZAHL1