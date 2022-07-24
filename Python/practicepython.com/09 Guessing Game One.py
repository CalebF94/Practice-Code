# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they
# guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)
#
# Extras:
#
#     Keep the game going until the user types “exit”
#     Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random


def guessing_game_1():
    print("Welcome to the Guessing Game. Enter 'quit' to stop playing")
    solution = random.randint(1, 9)
    keep_playing = True
    guesses = 0
    guess = 0

    while keep_playing:
        try:
            guess = int(input("Guess a number: "))
        except ValueError:
            break

        guesses += 1

        if guess == solution:
            print("You Win!")
            print(f"Number of Guesses: {guesses}")

            play_again = input("Enter 'yes' to keep playing: ").lower()
            if play_again != 'yes':
                keep_playing = False
            else:
                guesses = 0
                solution = random.randint(1, 9)
        elif guess < solution:
            print("Too low.")
        elif guess > solution:
            print("Too high. ")
        elif guess == 'quit':
            keep_playing = False
        else:
            "Invalid input: Please enter a valid number"


guessing_game_1()