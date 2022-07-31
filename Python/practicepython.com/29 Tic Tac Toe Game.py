# The next step is to put all these three components together to make a two-player Tic Tac Toe game!
# Your challenge in this exercise is to use the functions from those previous exercises all together in the same
# program to make a two-player game that you can play with a friend. There are a lot of choices you will have to
# make when completing this exercise, so you can go as far or as little as you want with it.
#
# Here are a few things to keep in mind:
#
# You should keep track of who won - if there is a winner, show a congratulatory message on the screen.
# If there are no more moves left, don’t ask for the next player’s move!
# As a bonus, you can ask the players if they want to play again and keep a running tally of who won
# more - Player 1 or Player 2.
def get_symbol(player_number):
	if int(player_number) == 0:
		sym = " "
	elif int(player_number) == 1:
		sym = "X"
	else:
		sym = "O"
	return sym


def draw_game_board(game):
	for row in range(0, 3):
		print(" ---" * 3)
		print(f"| {get_symbol(game[row][0])} | {get_symbol(game[row][1])} | {get_symbol(game[row][2])} |  ")
	print(" ---" * 3)


def horizontal_winner(board):
	found_winner = "No"
	for row in range(0, 3):
		if board[row][0] == board[row][1] == board[row][2] and board[row][0] != 0:
			found_winner = "Yes"
			break
	return {"win": found_winner, "player": board[row][0]}


def vertical_winner(board):
	found_winner = "No"
	for col in range(0, 3):
		if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
			found_winner = "Yes"
			break
	return {"win": found_winner, "player": board[0][col]}


def diagonal_winner(board):
	found_winner = "No"
	if (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]) and board[1][1] != 0:
		found_winner = "Yes"
	return {"win": found_winner, "player": board[1][1]}


def game_winner(board):
	if 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
		return {"win": "draw", "player": 0}
	else:
		diagonal_check = diagonal_winner(board)
		horizontal_check = horizontal_winner(board)
		vert_check = vertical_winner(board)

		if diagonal_check["win"] == "Yes":
			return diagonal_check
		elif horizontal_check["win"] == "Yes":
			return horizontal_check
		elif vert_check["win"] == "Yes":
			return vert_check
		else:
			return {"win": False, "player": 0}


def print_game(game):
	for row in range(0, 3):
		print(game[row])


def get_player_move(game, player_number):
	draw_game_board(game)
	player_symbol = "X" if player_number == 1 else "O"
	legal_move = False

	while not legal_move:
		move = input(f"Player {player_number} where would you like to play (r,c)? ")
		move = move.strip().split(sep=",")
		row = int(move[0])
		col = int(move[1])

		print(f"{row} {col}")
		if (row in [1, 2, 3]) and (col in [1, 2, 3]) and (game[row - 1][col - 1] == 0):
			legal_move = True
			game[int(move[0]) - 1][int(move[1]) - 1] = player_number
		else:
			print("Not a legal move. Select another move")


def play_tic_tac_toe():
	playing = True
	keep_playing = "y"
	player1_wins = 0
	player2_wins = 0
	game = [
		[0, 0, 0],
		[0, 0, 0],
		[0, 0, 0]]

	while playing:

		for player_number in [1, 2]:
			print(game)
			get_player_move(game, player_number)
			if game_winner(game)["win"] == "Yes":
				print_game(game)
				print(f"Player {player_number} Wins!")
				keep_playing = input("Would you like to play again (Y/N)?").lower()
			elif game_winner(game)["win"] == "draw":
				print(f"Player {player_number} Wins!")
				keep_playing = input("Would you like to play again (Y/N)?").lower()

			if keep_playing == "n":
				break
			else:
				game = [
				[0, 0, 0],
				[0, 0, 0],
				[0, 0, 0]]


play_tic_tac_toe()


