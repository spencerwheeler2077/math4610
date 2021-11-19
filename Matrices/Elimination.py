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


def elimination(matrix):
    numRows = len(matrix)
    for row in range(numRows-1):
        currentRow = matrix[row]
        __reduceRow(currentRow)
        for nextRow in matrix[row+1:]:
            __subtract(currentRow, nextRow, row)




if __name__ == "__main__":
    import PracticeMatrix
    Matrix = PracticeMatrix.squareMatrix(10, 1, 2)
    elimination(Matrix)
    for line in Matrix:
        print(line)