# -*- encoding: utf-8 -*-
import random

number = random.randint(1,10)
counter = 0

if __name__ == '__main__':

    while counter < 3:

        if counter == 0:
            print "\nGuess the Secret Number between 1 and 10 You have 3 tries!\n"
            variable = int(raw_input())
        else:
            print "Try again!\n"
            variable = int(raw_input())


        if variable == number:
            print "\n You did it. Congratulations!\n"
            quit()

        else:
            if variable > number:
                print "Your Guess is higher than the number\n"
                counter = counter + 1

            else:
                print "Your Guess is lower than the number\n"
                counter = counter + 1

    print "You lost. Thank you for playing"