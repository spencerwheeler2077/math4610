from Matrices.Solve import LUMatrix as LU
from Matrices.PracticeMatrix import hilbertMatrix
from Matrices.Multiplication import vectorMultiplication
from Matrices.Solve import parcialPivotingGuassian as parcialPivoting

solution = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

#  this part below is doing task 3
for i in range(4, 15):
    matrix = hilbertMatrix(i)
    bvector = vectorMultiplication(matrix, solution[:i])
    LUfactor = LU(matrix)
    solution2 = LUfactor.solve(bvector)
    print(solution[:i], solution2)

    # this is calculating the error between the found solution and the original vector.
    print(abs(solution2[0]-1))

print('hi')

#  this part below is doing task 5
for i in range(4, 15):
    matrix = hilbertMatrix(i)
    bvector = vectorMultiplication(matrix, solution[:i])

    solution2 = parcialPivoting(matrix, bvector)
    print(solution[:i], solution2)

    # this is calculating the error between the found solution and the original vector.
    print(abs(solution2[0] - 1))




