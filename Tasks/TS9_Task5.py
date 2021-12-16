import random
from Matrices import MatrixOperations, VectorMagnitudes, Solve, JacobiIteration


def main():


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

    solution = []
    guess = []
    for i in range(sizeOfMatrix):
        solution.append(1)
        guess.append(random.randint(-1, 2))

    bVector = MatrixOperations.matrixTimesVector(matrix, solution)

    jacSolution = JacobiIteration.jacobi(matrix, bVector, guess, .001, 10)
    jacSolution2 = JacobiIteration.jacobi(matrix, bVector, guess, .0000000000001, 1000)
    gaussSolution = Solve.gaussian(matrix, bVector)

    jacL2error = VectorMagnitudes.L2error(solution, jacSolution)
    jacL2error2 = VectorMagnitudes.L2error(solution, jacSolution2)
    gaussL2error = VectorMagnitudes.L2error(solution, gaussSolution)
    print("The error from jacobi iterations was: ", jacL2error)
    print("The error from jacobi iterations with higher precision was: ", jacL2error2)
    print("The error from gaussian elimination was: ", gaussL2error)




if __name__ == "__main__":
    main()
