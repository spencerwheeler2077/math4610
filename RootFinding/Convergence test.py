from matplotlib import pyplot as plt
import PracticeFunction
import numpy


def test(list):
    k = list[0]
    kPlus1 = list[1]
    logk = []
    for i in k:
        logk.append(numpy.log(i))

    logKplus = []
    for i in kPlus1:
        logKplus.append(numpy.log(i+1))


    plt.plot(logk, logKplus)
    plt.show()


def NewtonsMethod(aproxX, function, derivative, tolerance, maxI):
    x0 = aproxX
    k = []
    kPlus1 = []

    for j in range(maxI):

        x1 = x0 - (function(x0)/derivative(aproxX))
        error = abs(x1 - x0)

        if j != 0:
            kPlus1.append(error)

        if j != (maxI - 1):
            k.append(error)

        if error < tolerance:
            return [k, kPlus1]
        else:
            x0 = x1
    return [k, kPlus1]


def secant(firstx, secondx, function, tolerance, maxI):
    x0 = firstx
    x1 = secondx
    f0 = function(x0)
    f1 = function(x1)
    k = []
    kPlus1 = []

    for i in range(maxI):
        x2 = x1 - (f1*((x1-x0)/(f1-f0)))
        error = abs(x2 - x1)
        if i != 0:
            kPlus1.append(error)

        if i != (maxI - 1):
            k.append(error)
        if error < tolerance:
            return [k, kPlus1]
        else:
            x0 = x1
            x1 = x2
            f0 = function(x0)
            f1 = function(x1)

    return [k, kPlus1]

#test(NewtonsMethod(1, PracticeFunction.practFunc, PracticeFunction.practDeriv, .001, 10))
test(secant(-2, 1.1, PracticeFunction.practFunc, .0000001, 7))

