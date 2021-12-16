def addition(vector1, vector2):

    sumVector = []
    for i in range(len(vector1)):
        sumVector.append(vector1[i] + vector2[i])

    return sumVector


def subtraction(vector1, vector2):
    sumVector = []
    for i in range(len(vector1)):
        sumVector.append(vector1[i] - vector2[i])

    return sumVector


def scalar(vector, number):
    newVector = []
    for i in vector:
        newVector.append(i*number)

    return newVector


def dotProduct(vector1, vector2):
    total = 0
    for i in range(len(vector1)):
        total += vector1[i] * vector2[i]

    return total


def outerProduct(vector1,vector2):
    matrix = []

    for i in vector1:
        row = []
        for j in vector2:
            row.append(i*j)
        matrix.append(row)
    return matrix


if __name__ == "__main__":

    print(dotProduct([1, 1, 1], [0, 0, 1]))

    print(outerProduct([1,2,3], [1, 2, 1, 3]))
