import UpperTriangular
def LTfindSolution(matrix, bVector):

    numColumns = len(matrix[0])
    solution = []
    for i in range(numColumns):
        solution.append(0)

    j = 0
    for row in matrix:
        index = 0
        sum = 0
        for item in row:
            sum += solution[index]*item
            index += 1

        solution[j] = (bVector[j] - sum)/row[j]
        j += 1

    return solution


if __name__ == "__main__":
    from PracticeMatrix import generateMatrix
    import Transpose
    matrix = Transpose.transpose(generateMatrix())
    vector = [1, 1, 1]
    print(LTfindSolution(matrix, vector))

