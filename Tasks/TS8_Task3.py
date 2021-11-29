from Matrices.Solve import LUMatrix as LU
from Matrices.PracticeMatrix import hilbertMatrix
from Matrices.Multiplication import vectorMultiplication

solution = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(4, 11):
    matrix = hilbertMatrix(i)
    bvector = vectorMultiplication(matrix, solution[:i])
    LUfactor = LU(matrix)
    solution2 = LUfactor.solve(bvector)
    print(solution[:i], solution2)



