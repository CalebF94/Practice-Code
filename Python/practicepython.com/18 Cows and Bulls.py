# Create a program that will play the “cows and bulls” game with the user. The game works like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the
# user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed
# correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows”
# and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the
# number of guesses the user makes throughout teh game and tell the user at the end.

import random


def cows_and_bulls():
    running = True
    guesses = 0
    ans = str(random.randint(1000, 10000))

    while running:
        # variables for counting correct values
        cows = 0
        bulls = 0

        # getting user input
        guess = input("Guess a 4 digit number: ")
        guesses += 1

        # checking if locations are correct
        for ind in range(0, 4):
            if ans[ind] == guess[ind]:
                cows += 1
            else:
                bulls += 1
        print(f"{cows} cows, {bulls} bulls")
        if cows == 4:
            print(f"you win! You made {guesses} guesses")
            break


cows_and_bulls()


