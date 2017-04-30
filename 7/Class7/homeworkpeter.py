# Guess a number game with random number

import random
secret = random.randint(1, 20)  # To generate a random number


if __name__ == '__main__':

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
                life += 1
            elif guess > secret:
                print "My number is less than your guessed number!"
                life += 1
            elif guess == secret:
                print "Congratulations, you did it!"
                break
        except Exception as e:
            print e

    else:
         print "Sorry you lost the game!!"
