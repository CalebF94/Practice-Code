# This exercise is Part 2 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 3.
#
# Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the player has to
# guess, letter by letter. The player guesses one letter at a time until the entire word has been guessed. (In the
# actual game, the player can only guess 6 letters incorrectly before losing).
#
# Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player to
# guess a letter and displays letters in the clue word that were guessed correctly. For now, let the player guess an
# infinite number of times until they get the entire word. As a bonus, keep track of the letters the player guessed and
# display a different message if the player tries to guess that letter again. Remember to stop the game when all the
# letters have been guessed correctly! Don’t worry about choosing a word randomly or keeping track of the number of
# guesses the player has remaining - we will deal with those in a future exercise.
def show_progress(clue_word, letters_guessed):
    out_string = [letters for letters in clue_word]

    for index in range(0, len(out_string)):
        if out_string[index] not in letters_guessed:
            out_string[index] = "_"

    letters_remaining = out_string.count("_")
    return {"progress": " ".join(out_string), "letters_remaining": letters_remaining}


def guess_letters(clue_word='EVAPORATE'):
    word_solved = False

    letters_guessed = []

    while not word_solved:
        current_guess = input('Guess a letter: ').upper()

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


guess_letters()