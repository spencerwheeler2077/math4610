from Matrices.Solve import LUMatrix
from Matrices.MatrixOperations import transpose

def inverse(matrix):
    LU = LUMatrix(matrix)
    invMatrix = []
    for i in range(len(matrix)):
        identityCol = []
        for j in range(len(matrix)):
            if i == j:
                identityCol.append(1)
            else:
                identityCol.append(0)

        invMatrix.append(LU.solve(identityCol))  # this is adding the cols of the inverse as rows, so it needs to be transposed.

    return transpose(invMatrix)


if __name__ == "__main__":
    print(inverse([[2, 2], [1, 2]]))

