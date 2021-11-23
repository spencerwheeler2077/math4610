
def vectorMultiplication(matrix, vector):

    solution = []
    for row in matrix:
        i = 0
        solution.append(0)
        for entry in row:
            solution[-1] += entry * vector[i]

    return solution

if __name__ == "__main__":
    print(vectorMultiplication([[2, 1, 1], [2, 2, 1]], [1, 1, 1]))
