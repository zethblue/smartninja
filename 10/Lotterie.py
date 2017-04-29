import random

def Lotto(R,ANZAHL):
    while ANZAHL > 0:
        print random.randint(1, R)
        ANZAHL -= 1
    return None

if __name__ == '__main__':
    print "Welcome to LOTTO - This Program generates Numbers which can be defined by the user"
    print "Please state how much numbers you want to have/n"
    ANZAHL = int(raw_input())

    while True:
        print "Please state the range:"
        print "A for Austrian Lotto"  # Austrian Lotto has a Range of 43
        print "G for German Lotto"    # German Lotto has a Range of 49
        print "Q to Quit the Program"
        RANGE = raw_input()

        if RANGE == "A":
            print "You chose Austrian Lotto"
            R = 43
            break
        elif RANGE == "G":
            print "You chose German Lotto"
            R = 49
            break
        if RANGE == "Q":
            quit()
        else:
            print "Please enter A or G for Austrian or German Lotto"
            print "Enter Q to Quit"

    Lotto(R,ANZAHL)










