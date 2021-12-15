from Matrices.Elimination import elimination as elim
from Matrices.UpperTriangular import UTfindSolution
from Matrices.LowerTriangular import LTfindSolution
from Matrices.Elimination import scaledPartialPivoting as ParPivot


class LUMatrix():
    def __init__(self, matrix):
        self.matrix = matrix
        self.__multipliers = []
        self.__L = []

        for i in range(len(self.matrix)):
            self.__L.append([])
            for j in range(len(self.matrix[i])):
                if i == j:
                    self.__L[i].append(1)
                else:
                    self.__L[i].append(0)

        self.__elimination(self.matrix)




    def solve(self, bVector):
        c = LTfindSolution(self.__L, bVector)
        solution = UTfindSolution(self.matrix, c)
        return solution

    def print(self):
        for line in self.matrix:
            print(line)


    def __subtract(self, row1, row2, position):
        multiplier = row2[position]/row1[position]
        for i in range(len(row1)):
            row2[i] = row2[i] - (multiplier*row1[i])
        self.__multipliers.append(multiplier)


    def __elimination(self, matrix):
        numRows = len(matrix)
        for row in range(numRows-1):
            currentRow = matrix[row]
            for nextRow in matrix[row+1:]:
                self.__subtract(currentRow, nextRow, row)

        for cols in range(len(matrix[0])):
            for rows in range(len(matrix)):
                if rows > cols:
                    multi = self.__multipliers.pop(0)
                    self.__L[rows][cols] = multi
                    #self.matrix[rows][cols] = multi




def gaussian(matrix, vector):
    for i in range(len(vector)):
        matrix[i].append(vector[i])
    elim(matrix)
    bVector = []   # this is supposed to be the bvector after elimination.
    for row in matrix:
        bVector.append(row.pop(-1))
    return UTfindSolution(matrix, bVector)


def partialPivotingGaussian(matrix, vector):
    """
    This method is the exact same as the guassian method except it uses a scaled partial pivoting method to do
    elimination.
    """

    for i in range(len(vector)):
        matrix[i].append(vector[i])
    ParPivot(matrix) # this line is what makes the difference between guassian method and this method.
    bVector = []
    for row in matrix:
        bVector.append(row.pop(-1))
    return UTfindSolution(matrix, bVector)




if __name__ == "__main__":
    import PracticeMatrix
    matrix = PracticeMatrix.diagonalMatrix(4)
    for line in matrix:
        print(line)
    print(gaussian(matrix, [1, 1, 1, 1]))
    print()

    matrix = LUMatrix([[2, 2, 2, 1], [2, 5, 5, 3], [3, 6, 7, 4], [4, 8, 9, 6]])
    matrix.print()
    print()
    print(matrix.solve([1, 1, 1, 1]))

    print()
