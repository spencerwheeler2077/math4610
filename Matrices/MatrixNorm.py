

def Norm1(matrix):
    max = None
    for cols in range(len(matrix[0])):
        colTotal = 0
        for rows in range(len(matrix)):
            colTotal += abs(matrix[rows][cols])
        if max is None:
            max = colTotal
        else:
            if max < colTotal:
                max = colTotal
    return max


def infNorm(matrix):
    max = None
    for row in matrix:
        total = 0
        for item in row:
            total += abs(item)
        if max is None:
            max = total
        if total > max:
            max = total

    return max


if __name__ == "__main__":
    import Matrices.PracticeMatrix
    print(Norm1([[1, 2],
          [1, -2],
          [1, 5]]))

    print(infNorm([[1, 2],
                 [1, -2],
                 [1, 5]]))

    matrix = Matrices.PracticeMatrix.diagonallyDom(100)

    print(Norm1(matrix))
    print(infNorm(matrix))
