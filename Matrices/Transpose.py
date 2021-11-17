def transpose(matrix):
    matrixT = []
    for i in range(len(matrix[0])):
        matrixT.append([])
        for j in range(len(matrix)):
            matrixT[i].append(matrix[j][i])

    return matrixT


if __name__ == "__main__":
    transpose([[1, 0, 1], [1, 1, 2]])
