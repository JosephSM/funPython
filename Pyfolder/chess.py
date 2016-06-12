"""
writing a chess game...

The board: 8X8
16 pieces per player
rules for each player
"""
from pprint import pprint
import collections


def createBoard():
	board = {}
	for i in range(97, 105):
		for j in range(1, 9):
			board.setdefault(chr(i) + str(j), "-")
			if i == 98 or i == 103:
				board[chr(i)+str(j)] = "P"
			elif i == 97 or i == 104:
				if j == 1 or j == 8:
					board[chr(i)+str(j)] = "R"
				elif j == 2 or j == 7:
					board[chr(i)+str(j)] = "Kn"
				elif j == 3 or j == 6:
					board[chr(i)+str(j)] = "B"
				elif j == 4 and i == 97 or j == 5 and i == 104:
					board[chr(i)+str(j)] = "K"
				elif j == 5 and i == 97 or j == 4 and i == 104:
					board[chr(i)+str(j)] = "Q"
			if i <= 98:
				board[chr(i)+str(j)] =  "|{0}| ".format(board[chr(i)+str(j)])

	board = collections.OrderedDict(sorted(board.items()))
	return board


def printBoard(od):
	for k, v in od.items():
		if "1" in str(k):
			print("\n\n", str(v).center(5),end=" ")
		else:
			print(str(v).center(5), end=" ")
	print("\n")

def movePiece(board, turn):
	while True:	
		what = input("What piece would you like to move?")
		if turn == 0 and "|" in board[what] or turn == 1 and not "|" in board[what]:
			print("That's not your piece!") 
			continue
		break
	
	while True:
		where = input("Where would you like to move?")
		if ("|" in board[what] and "|" in board[where]) or \
		("|" not in board[what] and "|" not in board[where] and board[where].isalnum()):
			print("You can't capture your own piece, Silly.")
			continue
		break

	if board[where] != "-":
		deadpieces.append(board[where].strip())
	board[what], board[where]= "-", board[what]
	return board


def change(turn):
	if turn == 0:	
		turn = 1
	else:
		turn = 0
	return turn

def leave():
	bye = input("would you like to exit?")
	if bye == "y": exit()


deadpieces = []
myboard = createBoard()
whosturn = 0

while True:
	printBoard(myboard)
	print(deadpieces)
	print("It's {}'s turn!".format(whosturn))
	myboard = movePiece(myboard, whosturn)
	whosturn = change(whosturn)
	leave()
	










