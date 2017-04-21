# coding=utf-8
"""
script3.py: Usereingabe Beispiele, Zahlen
"""
import random
secret = random.randint(1,15)

if __name__ == '__main__':

    # Eingabe Zahl
    while True:
        try:
            zahl = raw_input("Errate die geheime Zahl\n")
            zahl = float(zahl)

            # Kontrolle ob Eingabe RICHTIG oder FALSCH
            if zahl == secret:
                print "Glückwunsch sie haben die richtige Zahl erraten"
                break
            elif zahl < secret:
                print "Die gesuchte Zahl ist größer"
            else:
                print "Die gesuchte Zahl ist kleiner"

        except:
            print "Sorry, your entry could not be interpreted"
            print "Please enter a valid number next time"
