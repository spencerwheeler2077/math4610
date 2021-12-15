def __reduceRow(row):
    pivot = None
    for item in range(len(row)):

        if row[item] != 0 and pivot is None:
            pivot = row[item]
        if pivot is not None:
            row[item] = row[item]/pivot


def __subtract(row1, row2, position):
    multiplier = row2[position]
    for i in range(len(row1)):
        row2[i] = row2[i] - (multiplier*row1[i])


def __exchangeRows(matrix, pos):
    max = matrix[pos][pos]
    bestPos = pos
    for i in range(pos, len(matrix)):
        if abs(matrix[i][pos]) > max:
            max = abs(matrix[i][pos])
            bestPos = i

    bestRow = matrix.pop(bestPos)
    matrix.insert(pos, bestRow)



def elimination(matrix):
    numRows = len(matrix)
    for row in range(numRows):
        currentRow = matrix[row]
        __reduceRow(currentRow)
        if row < numRows:
            for nextRow in matrix[row+1:]:
                __subtract(currentRow, nextRow, row)


def scaledPartialPivoting(matrix):
    numRows = len(matrix)
    for row in range(numRows):
        __exchangeRows(matrix, row)
        currentRow = matrix[row]
        __reduceRow(currentRow)
        if row < numRows:
            for nextRow in matrix[row + 1:]:
                __subtract(currentRow, nextRow, row)


if __name__ == "__main__":
    import PracticeMatrix
    Matrix = PracticeMatrix.squareMatrix(3, -5, 5)
    for line in Matrix:
        print(line)
    print()
    scaledPartialPivoting(Matrix)
    for line in Matrix:
        print(line)
