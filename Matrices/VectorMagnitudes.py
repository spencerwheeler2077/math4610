import math
from Matrices.VectorOperations import subtraction as subtract


def L1(vector):
    total = 0
    for i in vector:
        total += abs(i)
    return total


def L2(vector):
    total = 0
    for i in vector:
        total += i*i
    return math.sqrt(total)


def inf(vector):
    max = vector[0]
    for i in vector[1:]:
        if i > max:
            max = i

    return max


def L1error(vector1, vector2):
    errorVector = subtract(vector1, vector2)
    return L1(errorVector)

    
def L2error(vector1, vector2):
    errorVector = subtract(vector1, vector2)
    return L2(errorVector)


def infError(vector1, vector2):
    errorVector = subtract(vector1, vector2)
    return inf(errorVector)

if __name__ == "__main__":
    print()
