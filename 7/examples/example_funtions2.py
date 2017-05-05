#Schreibt eine Funktion
#Eingabe ist eine Zahl
#Ausgabe ist eine Liste mit allen Zahlen von 0 bis zur Eingabe

def listx(a):
    b = 0
    while b < a:
        print b
        b += 1
    return b

def listy(a):
    l1 = []
    while 0 <= a:
        l1.append(a)
        a -= 1
    l1.reverse()
    return l1

def listz(a):
    return range(a) + [a]
#Range erstellt eine Liste
# das [a] erstellt ebenfalls eine Liste wo a drinsteht

if __name__ == '__main__':
    print "Bitte geben Sie eine Zahl ein"
    ZAHL= int(raw_input())
    print listz(ZAHL)