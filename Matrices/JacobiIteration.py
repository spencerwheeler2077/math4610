from Matrices import MatrixOperations
from Matrices import VectorOperations
from Matrices import VectorMagnitudes


def jacobi(matrix, b, x_k, tolerance, maxIter):  # x_k1 = x_k + D^-1(r_k)

    resid = VectorOperations.subtraction(b, MatrixOperations.matrixTimesVector(matrix, x_k))

    for i in range(maxIter):
        if VectorMagnitudes.L2(resid) < tolerance:
            return x_k
        DinvResid = []
        for entry in range(len(resid)):
            DinvResid.append((1/matrix[entry][entry])*resid[entry])

        x_k = VectorOperations.addition(x_k, DinvResid)
        resid = VectorOperations.subtraction(b, MatrixOperations.matrixTimesVector(matrix, x_k))

    return x_k


if __name__ == "__main__":
    import PracticeMatrix
    matrix = [[3, 1, 1, 0],
              [0, 2, 1, 0],
              [0, 0, 2, 1],
              [0, 0, 0, 1]]
    b = [5, 3, 3, 1]
    tolerance = .001
    maxIter = 1000
    x0 = [5, 10, 6, 20]

    print(jacobi(matrix, b, x0, tolerance, maxIter))
