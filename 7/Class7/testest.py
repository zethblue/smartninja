# coding=utf-8
# Guess a number game with random number

import random
secret = random.randint(1, 20)  # To generate a random number


if __name__ == '__main__':                 # von python def um zu verhindern, dass fremde Dateien importiert werden; da Name nie Main, wird verwendet wenn man files importiert

    print "Hello!  What is your name?"

    user = raw_input("Please enter your Name:\n")
    print "Welcome to my Secret Number Game, " + user+'!'
    print "Well, I am thinking of a number between 1 and 20! \nGuess the number " + user, "you have 5 tries!"

    life = 0
    while life < 5:

        guess = raw_input("Please enter a number:\n")

        try:
            guess = int(guess)

            if guess < secret:
                print "My number is greater than your guessed number!"
                life += 1       # life = life + 1 / Alt + Enter ist Tastenkombination für Aenderung
            elif not guess > secret:
                print "My number is less than your guessed number!"
                life += 1
            elif guess == secret:
                print "Congratulations, you did it!"
                break
        except Exception as e:                                           #except Exception as e: Text über Fehlermeldung
            print e

    else:
        print "Sorry you lost the game!!"
