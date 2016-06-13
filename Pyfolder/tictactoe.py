"""
Tic tac toe
"""

gameBoard = {"tl": " ", "tm": " ", "tr": " ",
			"ml": " ", "mm": " ", "mr": " ",
			"ll": " ", "lm": " ", "lr": " "}

def printBoard(board):
	print("\n")
	print(board["tl"] + "|" + board["tm"] + "|" + board["tr"])
	print("- + -")
	print(board["ml"] + "|" + board["mm"] + "|" + board["mr"])
	print("- + -")
	print(board["ll"] + "|" + board["lm"] + "|" + board["lr"])
	print("\n")


def changeturn(turn):
	if turn == 'x':
		turn = "o"
	else:
		turn = "x"
	return turn

def move(board):
	what = input("what's your move?").lower()
	board[what] = whosturn



whosturn = "x"
while True:
	printBoard(gameBoard)
	print("It's {}'s' turn".format(whosturn))
	move(gameBoard)
	whosturn = changeturn(whosturn)


