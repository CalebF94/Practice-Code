# Given this solution to Exercise 9, modify it to have one level of user feedback: if the user does not enter a number
# between 1 and 9, tell them. Don’t count this guess against the user when counting the number of guesses they used.

import random


def guessing_game():
    num_to_guess = random.randint(1, 9)
    number_of_guesses = 0

    while True:

        while True:
            try:
                guess = int(input('Guess a number between 1 and 9: '))
            except ValueError:
                print("You need to enter a digit between 1 and 9")
            else:
                break
        if guess in [x for x in range(1, 10)]:
            number_of_guesses += 1
            if guess == num_to_guess:
                print(f"You guessed the number in {number_of_guesses} guesses")
                break
        else:
            print("Your guess needs to be a number between 1 and 9")


guessing_game()
