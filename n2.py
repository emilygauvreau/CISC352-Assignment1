import sys
from random import choice, randint
from math import sqrt

class NQueens:
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

    # gameboard[row][column] i think these should be swapped [col][row]
    def __init__(self, fileName):
        # Values of current iteration for `n` Queens in current row of text file
        self.gameBoard = None
        self.queensPositions = None
        self.nQueens = 0
        self.createGame(fileName)

    # Reads the file in and runs the game for each N in the file
    def createGame(self, fileName):
        nArray = self.readFile(fileName)
        qPositionMatrix = []
        # for as many Ns as available
        for n in nArray:
            # Create game board and load current queen positons
            self.gameBoard, self.queensPositions = self.createBoard(n)
            self.nQueens = n
            # Try to change positions of queens in the board to satisfy the criteria (CSP)
            self.verifyBoard()
            # Display the board and verify position results
            solution = self.makeQueenPositions()
            print(solution)
            self.displayBoard()
            qPositionMatrix.append(solution)
            # quick row test
            temp = {}
            for i in solution:
                if i in temp:
                    print("Row issue: ", i)
                else:
                    temp[i] = True
            # Output total results
            self.output(qPositionMatrix)

    # Create list of row positions of queens in board at correct columns
    def makeQueenPositions(self):
        queensPositions = []
        for col in range(self.nQueens):
            for row in range(self.nQueens):
                if self.gameBoard[col][row] == 'Q':
                    queensPositions.append(row + 1)
        return queensPositions

    # Function depicts the current gameboard as an nxn grid
    def displayBoard(self):
        for row in range(self.nQueens):
            for col in range(self.nQueens):
                print(self.gameBoard[col][row], end="   ")
            print("\n")  # adds a new line between each row
        print("\n")  # adds a new line between each gameboard


    # Initialize board with 0s and loads 'Q' into each column at a random row position, avoiding repeated rows
    def createBoard(self, n):
        board = [[0 for i in range(n)] for j in range(n)]
        qPositions = []
        excludedRows = []
        for x in range(0, n):
            # Idea is to generate best possible start state to reduce computations
            # Excludes already used rows
            row = choice([i for i in range(0, n) if i not in excludedRows])
            excludedRows.append(row)
            # Update board and save queen (col, row) position
            board[x][row] = 'Q'
            qPositions.append((x, row))
        # Sort positions by columns
        qPositions = sorted(qPositions, key=lambda x: x[0])
        return board, qPositions

    def shuffleBoard(self, n): # resets board - helps with local minima problem
        self.gameBoard, self.queensPositions = self.createBoard(n)

    def verifyBoard(self):
        # Iterates over Queens at their initial positions
        swapWillOccur = True # Represents if swap will occur with different row
        swapCounter = 0 # Counts number of swaps - helps detect local minima
        while swapWillOccur: # While rows are still being swapped
            swapWillOccur = False
            swapCounter+=1
            if swapCounter == self.nQueens: # solution is not being found we need to reshuffle
                self.shuffleBoard(self.nQueens) # should be great than self.nqueens for all possible situations
                swapCounter = 0
            for queen in self.queensPositions:
                # determine positions of minimum conflict
                # if more than 1 row has same min conflict then
                # next step determines
                # "random" position to switch to
                possibleRows, minConflicts = self.conflictsInColumn(queen) # queen is tuple (col, row)
                # Only one position available so yeehaw
                if len(possibleRows) == 1:
                    minConflictRow = possibleRows[0]
                else:
                    # Determine first "random" available position to switch to that ISN'T the same as the original
                    while True:
                        minConflictRow = choice(possibleRows)
                        if minConflictRow == queen[1]:
                            possibleRows.remove(minConflictRow)
                        else:
                            break

                # swap queens yeehaw
                if minConflictRow != queen[1] or minConflicts > 0: # new row - so new conflict could occur
                    swapWillOccur = True
                newPosition = (queen[0], minConflictRow)
                queen = self.moveQueen(queen, newPosition)

    # Given new and current position, swap the Queen position in the board
    def moveQueen(self, currentPosition, newPosition):
        curCol, curRow = currentPosition[0], currentPosition[1]
        newRow = newPosition[1]
        # note: col is same for both currentPosition and newPosition
        # self.displayBoard()
        # print("Swap: ({}, {}) for ({}, {})".format(curCol, curRow, newCol, newRow))
        self.gameBoard[curCol][curRow], self.gameBoard[curCol][newRow] = self.gameBoard[curCol][newRow], self.gameBoard[curCol][curRow]
        self.queensPositions[curCol] = (curCol, newRow)
        return self.queensPositions[curCol] # Returning new queen location

    # Determine the rows with minimum conflicts in the same column as the current queen
    def conflictsInColumn(self, position):
        col, row = position[0], position[1]
        minConflicts = self.conflictsAtPosition(position)
        lowestConflictIndex = position[1]
        minConflictIndices = []
        # for as many rows there are
        for i in range(self.nQueens):
            # if not the same row as current queen position
            if i != position[1]:
                # determine conflicts at that position
                newConflict = self.conflictsAtPosition((col, i))
                # if smaller than previously determined min conflict position, switch
                if newConflict < minConflicts:
                    minConflicts = newConflict
                    lowestConflictIndex = i
                    minConflictIndices.clear()
                elif newConflict == minConflicts: # if value already exists then add to available min positions
                    minConflictIndices.append(lowestConflictIndex)
                    minConflictIndices.append(i)
        if len(minConflictIndices) != 0:
           return minConflictIndices, minConflicts
        # Return lowest swap position
        return [lowestConflictIndex], minConflicts

    # position = (column, row)
    # Determine the total conflicts where queen is at the current position (row, column and diagonals)
    def conflictsAtPosition(self, position):
        conflicts = 0
        for queen in self.queensPositions:
            # same pos
            if position[0] == queen[0] and position[1] == queen[1]:
                pass
            # same column
            elif position[0] == queen[0]:
                conflicts += 1

            # same row
            elif position[1] == queen[1]:
                conflicts += 1

            # on left/right diagonal
            elif abs(position[0] - queen[0]) == abs(position[1] - queen[1]):
                conflicts += 1

        return conflicts

    # takes a text file containing multiple n values for the nxn queens game
    # returns an array that contains each n as an int at a new index
    def readFile(self, fileName):
        file = open(fileName, 'r') # open file
        nArray = []  # array to hold the integers once the txt is stripped
        for line in file:
            line = line.strip()
            nArray.append(int(line))
        return nArray

    # Output the queen position results into the output txt file
    def output(self, solutionMatrix):
        sys.stdout = open("nqueens_out.txt", "w")
        for value in solutionMatrix:
            print(value, '\n')
        sys.stdout.close()

if __name__ == '__main__':
    game = NQueens("nqueens.txt")
