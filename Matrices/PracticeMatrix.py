def generateMatrix(numRows=3, numCols=3):
    matrix = []
    for i in range(numRows):
        matrix.append([])
        for j in range(numCols):
            matrix[i].append(0)
            item = 0
            if j < i:
                matrix[i][j] = item
            else:
                matrix[i][j] = i + j - 1

    return matrix

if __name__ == "__main__":
    matrix = generateMatrix(3, 3)
    for line in matrix:
        print(line)
