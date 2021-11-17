def UTfindSolution(matrix, bVector):

    matrix.reverse()
    numColumns = len(matrix[0])
    solution = []
    for i in range(numColumns):
        solution.append(0)


    j = numColumns - 1
    for row in matrix:
        index = 0
        sum = 0
        for item in row:
            sum += solution[index]*item
            index += 1

        solution[j] = (bVector[j] - sum)/row[j]
        j -= 1

    return solution

if __name__ == "__main__":
    from PracticeMatrix import generateMatrix
    matrix = generateMatrix()
    print(matrix)
    print(UTfindSolution(matrix, [1, 1, 1]))
