import random


def generateMatrix(numRows=3, numCols=3):
    matrix = []
    for i in range(numRows):
        matrix.append([])
        for j in range(numCols):
            matrix[i].append(0)
            if j < i:
                matrix[i][j] = 0
            else:
                matrix[i][j] = i + j - 1

    return matrix


def squareMatrix(numRows, lowerBound=-10, upperBound=10):
    matrix = []
    for i in range(numRows):
        matrix.append([])
        for j in range(numRows):
            matrix[i].append(random.randint(lowerBound, upperBound))

    return matrix


def LTMatrix(numRows, lowerBound=-10, upperBound=10):
    matrix = []
    for i in range(numRows):
        matrix.append([])
        for j in range(numRows):
            if j <= i:
                matrix[i].append(random.randint(lowerBound, upperBound))
            else:
                matrix[i].append(0)

    return matrix


def UTMatrix(numRows, lowerBound=-10, upperBound=10):
    matrix = []
    for i in range(numRows):
        matrix.append([])
        for j in range(numRows):
            if j >= i:
                matrix[i].append(random.randint(lowerBound, upperBound))
            else:
                matrix[i].append(0)

    return matrix


def diagonalMatrix(numRows, lowerBound=-10, upperBound=10):
    matrix = []
    for i in range(numRows):
        matrix.append([])
        for j in range(numRows):
            if j == i:
                num = random.randint(lowerBound, upperBound)
                while num == 0:
                    num = random.randint(lowerBound, upperBound)
                matrix[i].append(num)

            else:
                matrix[i].append(0)

    return matrix


def hilbertMatrix(numRows):
    matrix = []
    for row in range(numRows):
        matrix.append([])
        for col in range(numRows):
            matrix[row].append(1/(row + col + 1))
    return matrix


def diagonallyDom(numRows):
    sizeOfMatrix = 100
    matrix = []
    for i in range(sizeOfMatrix):
        row = []
        for j in range(sizeOfMatrix):
            if i == j:
                row.append(sizeOfMatrix)
            else:
                row.append(random.randint(-1, 1))

        matrix.append(row)
    return matrix




if __name__ == "__main__":
    print("3X3 Square Matrix")
    myMatrix = squareMatrix(3)
    for line in myMatrix:
        print(line)
    print()
    print("3x3 Lower Triangular Matrix")
    myMatrix = LTMatrix(3)
    for line in myMatrix:
        print(line)
    print()
    print("3X3 Upper Triangular Matrix")
    myMatrix = UTMatrix(3)
    for line in myMatrix:
        print(line)
    print()
    print("5X5 Diagonal Matrix")
    myMatrix = diagonalMatrix(5)
    for line in myMatrix:
        print(line)

    hilbertMatrix(4)



