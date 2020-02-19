from random import choice

nValue = 8

rows, cols = nValue, nValue
gameboard = [[i for i in range(cols)] for j in range(rows)]


excludedRows = []
excludedColumns = []

for row in range(nValue):
    for col in range(nValue):
        print(gameboard[row][col], end=" ")
    print("\n")  # adds a new line between each row
print("\n")  # adds a new line between each gameboard


for x in range(0, nValue):
    column = choice([i for i in range(0, nValue) if i not in excludedColumns])
    row = choice([i for i in range(0, nValue) if i not in excludedRows])

    excludedColumns.append(column)
    excludedRows.append(row)

    gameboard[row][column] = 'Q'

for row in range(nValue):
    for col in range(nValue):
        print(gameboard[row][col], end=" ")
    print("\n")  # adds a new line between each row
print("\n")  # adds a new line between each gameboard


queensPositions = []

for col in range(nValue):
    for row in range(nValue):
        if gameboard[row][col] == 'Q':
            queensPositions.append(row + 1)

queensPairs = tuple(enumerate(queensPositions))

print(queensPairs)

for pair in queensPairs:
    print(pair)

# def verifyQueen(row, col):
# loop through row + ... and col + ... to check if there are other queens
# def checkRow(gameboard):
#     numQueens = 0
#
#     for row in gameboard:
#         for element in row:
#             if element == 'Q':
#                 numQueens += 1
#             if numQueens == 2:
#                 return 1
#     return 0
#
# def checkColumn(gameboard, nValues):
#     numQueens = 0
#
#     for column in gameboard:
#         for element in range(0, nValues):
#             if gameboard[element][column] == 'Q':
#                 numQueens += 1
#             if numQueens == 2:
#                 return 1
#     return 0

