# The next logical step is to deal with handling user input. When a player (say player 1, who is X) wants to place an X on the screen, they can’t just click on a terminal. So we are going to approximate this clicking simply by asking the user for a coordinate of where they want to place their piece.
#
# As a reminder, our tic tac toe game is really a list of lists. The game starts out with an empty game board like this:
#
# game = [[0, 0, 0],
# 	[0, 0, 0],
# 	[0, 0, 0]]
# The computer asks Player 1 (X) what their move is (in the format row,col), and say they type 1,3. Then the game
# would print out
#
# game = [[0, 0, X],
# 	[0, 0, 0],
# 	[0, 0, 0]]
# And ask Player 2 for their move, printing an O in that place.
#
# Things to note:
#
# For this exercise, assume that player 1 (the first player to move) will always be X and player 2 (the second player)
# will always be O.
#
# Notice how in the example I gave coordinates for where I want to move starting from (1, 1) instead of (0, 0).
# To people who don’t program, starting to count at 0 is a strange concept, so it is better for the user experience if
# the row counts and column counts start at 1. This is not required, but whichever way you choose to implement this,
# it should be explained to the player.
#
# Ask the user to enter coordinates in the form “row,col” - a number, then a comma, then a number. Then you can use
# your Python skills to figure out which row and column they want their piece to be in.
#
# Don’t worry about checking whether someone won the game, but if a player tries to put a piece in a game position
# where there already is another piece, do not allow the piece to go there.

game = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]


def print_game(game):
    for row in range(0, 3):
        print(game[row])


def get_player_move(game, player_num):
    print_game(game)
    player_move = input("What is your move")


get_player_move(game, 1)