import sys
#import random
from random import choice

class NQueens:

    # gameboard[row][column]
    def __init__(self, fileName):
        self.currentN = 0
        # Array of n values read from file
        gameSizes = self.readFile(fileName)

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
        solutions = self.initializeGame(gameSizes)

        self.output(solutions)


    #takes a text file containing multiple n values for the nxn queens game
    #returns an array that contains each n as an int at a new index
    def readFile(self, fileName):
        # open file
        file = open(fileName, 'r')
        nArray = [] # array to hold the integers once the txt is stripped

        for line in file:
            line = line.strip()
            nArray.append(line)

        return nArray


    #initializes the game by taking the array of ints & finding a solution for each int
    #returns an array of arrays where each element is a solution in matrix form
    def initializeGame(self, nArray):

        solutionMatrix = []

        for nValue in nArray:
            self.currentN = int(nValue)
            solution = self.runOneGame()  #returns an array that holds the values
            solutionMatrix.append(solution) #array of arrays

        return solutionMatrix


    #takes the value in the original n array and sets up a nxn board
    #performs the 8 queens algorithm where no two queens can be in the same
    #row, column or diagonal.
    def runOneGame(self):
        #run n queens

        solution = []
        # [1,3,0,2] is column 0 row 1, column 1, row 3
        # index positions are columns, row indexes are the value held at each spot

        gameboard = self.createBoard()
        if self.verifyBoard(gameboard):
            solution = self.getQueensPositions(gameboard)

        print(solution)
        self.displayBoard(gameboard)

        return solution


    #creates a nxn size board with all values initialized to 0
    #for every queen in range of 0-n a random value is selected for the x and y coordinates
    #and that (x,y) is updated in the board to hold Q this creates a random game board
    def createBoard(self):

        rows, cols = self.currentN, self.currentN
        gameboard = [[0 for i in range(cols)] for j in range(rows)]

            # [[0,0], [0,0], [0,0]]
            # [row 1 column 1,2 ... row 2 column 1,2 ...]

        # y = 0 #ensures that each queen appears in a different column to start
        # for x in range(0,nValue):
        #     xcoordinate = random.randint(0, nValue-1)
        #     ycoordinate = y
        #     gameboard[xcoordinate][ycoordinate] = 'Q'
        #     y += 1

        excludedRows = []
        excludedColumns = []

        for x in range(0, self.currentN):
            column = choice([i for i in range(0, self.currentN) if i not in excludedColumns])
            row = choice([i for i in range(0, self.currentN) if i not in excludedRows])

            excludedColumns.append(column)
            excludedRows.append(row)

            gameboard[row][column] = 'Q'

        return gameboard


    #function depicts the current gameboard as an nxn grid
    def displayBoard(self, gameboard):
        for row in range(self.currentN):
            for col in range(self.currentN):
                print(gameboard[row][col], end=" ")
            print("\n")  # adds a new line between each row
        print("\n")  # adds a new line between each gameboard


    def verifyBoard(self, gameboard, queensPositions):

        #queenspositions is giving us an array where the index is a column so i = column
        # and the value stored at the index is a row so queenspositions[i] = row

        queensPairs = tuple(enumerate(queensPositions))

        print("starting")
        for pair in queensPairs:
            self.verifyQueen(gameboard, pair)

        row1, col1 = 0, 0
        row2, col2 = 0, 0

        #for every pair of queens we have to check if they exists on the same diagonal
        if (row1 != row2) and (col1 != col2) and (row1 - col1 != row2 - col2) and (row1 + col1 != row2 + col2):
            #verifyBoard() == True this is a solution that can be returned
            return True

        else:
            if row1 - col1 == row2 - col2:
                return False
                # in the same left diagonal and must be moved
            elif row1 + col1 == row2 + col2:
                return False
                # in the same right diagonal and must be moved
        # iterate over rows and colums and see if there r probs
        #
        # 1) find queen in column x when x starts as 0
        # 2) check if the queen has any conflicts
        #     - same row, same column, left diagonal, right diagonal
        # 3) if conflict exists find the spot in the SAME column with the smallest amount of conflict
        # 4) if no conflict then hurray x += 1
        return True


    def getQueensPositions(self, gameboard):

        queensPositions = []

        for col in range(self.currentN):
            for row in range(self.currentN):
                if gameboard[row][col] == 'Q':
                    queensPositions.append(row + 1)

        return queensPositions


    def output(self, solutionMatrix):

        sys.stdout = open("nqueens_out.txt", "w")

        for value in solutionMatrix:
            print(value, '\n')

        sys.stdout.close()

if __name__ == '__main__':
    game = NQueens("nqueens.txt")
