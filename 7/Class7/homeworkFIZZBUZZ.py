"""FIZZBUZZ Hausuebung"""

X = 1
if __name__ == '__main__':

    print "Bitte geben Sie eine Zahl zwischen 1 und 100 ein\n"
    while X == 1:
        ZAHL1 = raw_input()
        try:
            ZAHL1 =float(ZAHL1)

        except:
            print "Ihre Eingabe ist fehlerhaft. Bitte geben Sie eine korrekte Zahl zwischen 1 und 100 ein"
            continue
        if ZAHL1 > 100:
             print "Die Zahl ist zu gross. Bitte geben Sie eine Zahl zwischen 1 und 100 ein"
             continue
        elif ZAHL1 < 1:
            print "Die Zahl ist zu klein. Bitte geben Sie eine Zahl zwischen 1 und 100 ein"
            continue
        else:
            print "BIZZFUZZ is starting"
            X = X + 1

    while ZAHL1 < 300:
        ZAHL1 = ZAHL1 + 1
        if ZAHL1 % 3 == 0 and ZAHL1 % 5 != 0:
            print "FIZZ"
        elif ZAHL1 % 5 == 0 and ZAHL1 % 3 != 0:
            print "BUZZ"
        elif ZAHL1 % 3 == 0 and ZAHL1 % 5 == 0:
            print "FIZZBUZZ"
        else:
            print ZAHL1