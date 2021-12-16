import Matrices.PowerMethod as PM
from Matrices.PracticeMatrix import diagonallyDom as matrixGen


def condition(matrix, x0=None):
    if x0 is None:
        x0 = []
        for i in range(len(matrix[0])):
            x0.append(1)
    maxLambda = PM.powerMethod(matrix, x0, 1000)
    minLambda = PM.invPowerMethod(matrix, x0, 1000)
    return abs(maxLambda)/abs(minLambda)


if __name__ == "__main__":
    matrix = matrixGen(100)
    print(condition(matrix))
