from Matrices.Solve import LUMatrix as LU
from Matrices.PracticeMatrix import hilbertMatrix
from Matrices.VectorOperations import dotProduct
from Matrices.Solve import partialPivotingGaussian as parcialPivoting

solution = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
errorlist = []
errorlist2 = []

#  this part below is doing task 3
for i in range(4, 10):
    matrix = hilbertMatrix(i)
    bvector = dotProduct(matrix, solution[:i])
    LUfactor = LU(matrix)
    solution2 = LUfactor.solve(bvector)
    print(solution[:i], solution2)

    # this is calculating the error between the found solution and the original vector.
    totalerror = 0
    for i in solution2:
        totalerror += abs(1 - i)
    print(totalerror)
    errorlist.append(totalerror)

print('hi')

#  this part below is doing task 5
for i in range(4, 10):
    matrix = hilbertMatrix(i)
    bvector = dotProduct(matrix, solution[:i])

    solution2 = parcialPivoting(matrix, bvector)
    print(solution[:i], solution2)

    # this is calculating the error between the found solution and the original vector.
    totalerror = 0
    for i in solution2:
        totalerror += abs(1 - i)
    errorlist2.append(totalerror)

print(errorlist)
print(errorlist2)


