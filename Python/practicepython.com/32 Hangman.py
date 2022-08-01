# In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses
# (head, body, 2 legs, and 2 arms) before they lose the game.
#
# In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for guessing the
# letter and displaying that information to the user. In this exercise, we have to put it all together and add logic
# for handling guesses.
#
# Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:
#
# Only let the user guess 6 times, and tell the user how many guesses they have left.
# Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize
# them - let them guess again.

import random


def random_sowpods_word():
    with open('sowpods.txt', 'r') as file_name:
        line = file_name.readline()
        sowpods_words = []
        while line:
            sowpods_words.append(line.strip())
            line = file_name.readline()

    random_word = sowpods_words[random.randint(0, len(sowpods_words)-1)]
    return random_word


def show_progress(clue_word, letters_guessed):
    out_string = [letters for letters in clue_word]

    for index in range(0, len(out_string)):
        if out_string[index] not in letters_guessed:
            out_string[index] = "_"

    letters_remaining = out_string.count("_")
    return {"progress": " ".join(out_string), "letters_remaining": letters_remaining}


def guess_letters(clue_word='EVAPORATE'):
    clue_word = clue_word.upper()
    word_solved = False
    misses = 0
    letters_guessed = []

    while not word_solved:
        if misses == 6:
            print(f"Too many guesses! you lose\nThe correct word was {clue_word}")

            break

        current_guess = input(f"{6 - misses} incorrect guesses remaining\nGuess a letter: ").upper()

        if current_guess not in [letters for letters in clue_word] + letters_guessed:
            misses += 1

        if current_guess not in letters_guessed:
            letters_guessed.append(current_guess)
        else:
            print(f'{current_guess} has already been guessed. Try again')

        progress = show_progress(clue_word, letters_guessed)

        if progress["letters_remaining"] == 0:
            print("You solved the puzzle!")
            print(progress["progress"])
            word_solved = True
        else:
            print(progress["progress"])


def play_hangman():
    print("Welcome to Hangman. Guess letters to solve the word.\n")
    cont_playing = True

    while cont_playing:
        clue_word = random_sowpods_word()
        guess_letters(clue_word)
        if input("Would you like to play again? Y/N: ").upper() == "N":
            cont_playing = False

play_hangman()
