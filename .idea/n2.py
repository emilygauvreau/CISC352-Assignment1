import sys
from random import choice

class NQueens:

    # gameboard[row][column]
    def __init__(self, fileName):
        # Values of current iteration for `n` Queens in current row of text file
        self.gameBoard = None
        self.queensPositions = None
        self.nQueens = 0

        self.createGame(fileName)

        # Initialize game from input values
        # solutions is a matrix of Queen position. Each row is for size n, and each index in a row holds the row of the Queen
        # Format:
        #           solutions= [                                                            index = column, value = row
        #                       [1, 3, 0, 2],                           n = 4               Q1 = (0, 1), Q2 = (1, 3), Q3 = (0, 0)...
        #                       [1, 3, 0, 2, 4, 5, 6],                  n = 7               Q1 = (0, 1), Q2 = (1, 3), Q3 = (0, 0)...
        #                       [1, 3, 0, 2, 5, 6, 7....],              n = 7...            Q1 = (0, 1), Q2 = (1, 3), Q3 = (0, 0)...
        #                       [1, 3, 0, 2, 5, 6, 7, 8....],           n = 8...            Q1 = (0, 1), Q2 = (1, 3), Q3 = (0, 0)...
        #                       [1, 3, 0, 2, 5, 6, 7, 8, 9, 10....],    n = 10...           Q1 = (0, 1), Q2 = (1, 3), Q3 = (0, 0)...
        #                       ...                                     n = ...
        #                       ]
        #
        # initializeGame runs runOneGame on the current n value in gameSizes[i]

    def createGame(self, fileName):
        nArray = self.readFile(fileName)

        for n in nArray:
            self.gameBoard, self.queenPositions = self.createBoard(n)
            self.nQueens = n


    def createBoard(self, n):
        board = []
        positions = []

        board = [[0]*n for j in range(n)]

        print(board)
        return board, positions

    # takes a text file containing multiple n values for the nxn queens game
    # returns an array that contains each n as an int at a new index
    def readFile(self, fileName):
        # open file
        file = open(fileName, 'r')
        nArray = []  # array to hold the integers once the txt is stripped

        for line in file:
            line = line.strip()
            nArray.append(line)

        return nArray


if __name__ == '__main__':
    game = NQueens("nqueens.txt")
