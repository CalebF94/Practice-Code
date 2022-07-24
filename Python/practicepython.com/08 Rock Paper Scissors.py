# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
#
#     Rock beats scissors
#     Scissors beats paper
#     Paper beats rock
import os


def rock_paper_scissors(play = 'yes'):
    while play == 'yes':
        player1_choice = input("Player 1: Enter Rock, Paper, or Scissors: ").lower()
        player2_choice = input("Player 2: Enter Rock, Paper, or Scissors: ").lower()

        if player1_choice == player2_choice:
            print("You Tied")
        elif player1_choice == 'rock' and player2_choice == 'scissors':
            print('Player 1 Wins!')
        elif player1_choice == 'scissors' and player2_choice == 'paper':
            print('Player 1 Wins!')
        elif player1_choice == 'paper' and player2_choice == 'rock':
            print('Player 1 Wins!')
        else:
            print('Player 2 Wins!')

        print("\nWould you like to play again?")
        print("Enter 'yes' to play again")
        print("Enter anything else to quit")
        play = input("Selection: ").lower()
        print(100 * "\n")


rock_paper_scissors()
