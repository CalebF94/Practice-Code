# If a game of Tic Tac Toe is represented as a list of lists, like so:
#
# game = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]
# where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2
# put their token in that space.
#
# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone
# has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or
# a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be
# one winner.

winner_is_2 = [
	[2, 2, 2],
	[2, 1, 0],
	[0, 1, 1]]


winner_is_1 = [
	[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [
	[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [
	[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [
	[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]


def horizontal_winner(board):
	found_winner = False
	for row in range(0, 3):
		if board[row][0] == board[row][1] == board[row][2] and board[row][0] != 0:
			found_winner = True
			break
	return {"win": found_winner, "player": board[row][0]}


def vertical_winner(board):
	found_winner = False
	for col in range(0, 3):
		if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
			found_winner = True
			break
	return {"win": found_winner, "player": board[0][col]}


def diagonal_winner(board):
	found_winner = False
	if (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]) and board[1][1] != 0:
		found_winner = True
	return {"win": found_winner, "player": board[1][1]}


def game_winner(board):
	diagonal_check = diagonal_winner(board)
	horizontal_check = horizontal_winner(board)
	vert_check = vertical_winner(board)

	if diagonal_check["win"]:
		print(f"Player {diagonal_check['player']} wins")
	elif horizontal_check["win"]:
		print(f"Player {horizontal_check['player']} wins")
	elif vert_check["win"]:
		print(f"Player {vert_check['player']} wins")
	else:
		print("nobody wins")


game_winner(winner_is_1)
game_winner(winner_is_2)
game_winner(winner_is_also_1)
game_winner(no_winner)
game_winner(also_no_winner)