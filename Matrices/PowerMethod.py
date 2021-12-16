import Matrices.MatrixOperations as MO
import Matrices.VectorMagnitudes as VM
import Matrices.VectorOperations as VO
import Matrices.Inverse


def powerMethod(matrix, x0, numIter): # x_(k+1) = Ax/|Ax|
    x_k = x0
    for i in range(numIter):
        Ax = MO.matrixTimesVector(matrix, x_k)
        magOfAx = VM.L2(Ax)
        x_k = VO.scalar(Ax, 1/magOfAx)

    return VO.dotProduct(Ax, x_k)/ VO.dotProduct(x_k, x_k)


def invPowerMethod(matrix, x0, maxIter):
    invMatrix = Matrices.Inverse.inverse(matrix)
    return 1/powerMethod(invMatrix, x0, maxIter)




if __name__ == "__main__":
    print(powerMethod([[1, 0], [0, 1]], [6, 4], 1000))
    print(invPowerMethod([[1, 0], [0, 1]], [6, 4], 1000))
