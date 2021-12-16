import Matrices.VectorOperations


def addition(matrix1, matrix2):
    newMatrix = []
    for row in range(len(matrix1)):
        newMatrix.append(Matrices.VectorOperations.addition(matrix1[row], matrix2[row]))
    return newMatrix


def subtraction(matrix1, matrix2):
    newMatrix = []
    for row in range(len(matrix1)):
        newMatrix.append(Matrices.VectorOperations.subtraction(matrix1[row], matrix2[row]))
    return newMatrix


def scalar(matrix, c):
    newMatrix = []
    for row in matrix:
        newRow = []
        for entry in row:
            newRow.append(entry*c)
        newMatrix.append(newRow)
    return newMatrix


def transpose(matrix):
    matrixT = []
    for i in range(len(matrix[0])):
        matrixT.append([])
        for j in range(len(matrix)):
            matrixT[i].append(matrix[j][i])

    return matrixT


def matrixTimesVector(matrix, vector):
    result = []
    for row in matrix:
        result.append(Matrices.VectorOperations.dotProduct(row, vector))

    return result


def matrixTimesMatrix(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return
    newMatrix = []
    for row in matrix1:
        newRow = []
        for col in range(len(matrix2[0])):
            sum = 0
            for i in range(len(row)):
                sum += row[i]*matrix2[i][col]
            newRow.append(sum)
        newMatrix.append(newRow)

    return newMatrix

if __name__ == "__main__":
    print(matrixTimesMatrix([[2, 0], [0, 2], [3, 1]], [[2, 0, 3], [1, 1, 5]]))
