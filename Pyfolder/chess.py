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
	print(od)
	for k, v in od.items():
		if "1" in str(k):
			print("\n\n", str(v).center(5),end=" ")
		else:
			print(str(v).center(5), end=" ")
	print("\n")

def movePiece(board):
	what = input("What piece would you like to move?")
	where = input("Where would you like to move?")
	board[what], board[where] = "-", board[what]
	return board


myboard = createBoard()
while True:
	printBoard(myboard)
	myboard = movePiece(myboard)
	leave = input("would you like to exit?")
	if leave == "y":
		exit()










