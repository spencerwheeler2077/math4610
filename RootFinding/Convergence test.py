from matplotlib import pyplot as plt
import PracticeFunction
import numpy


def test(fList):
    iList = []
    for i in range(1, len(fList) + 1):
        iList.append(numpy.log(i))

    logErrorList = []
    for i in fList:
        logErrorList.append(numpy.log(i))

    plt.plot(iList, logErrorList)
    plt.show()

def NewtonsMethod(aproxX, function, derivative, tolerance, maxI):
    x0 = aproxX
    fx = function(x0)
    fprimex = derivative(aproxX)

    for i in range(maxI):
        x1 = x0 - (fx/fprimex)
        error = abs(x1 - x0)
        if error <= tolerance:
            return error
        else:
            x0 = x1
            fx = function(x0)
            fprimex = derivative(x0)
    return error

def secant(firstx, secondx, function, tolerance, maxI):
    x0 = firstx
    x1 = secondx
    f0 = function(x0)
    f1 = function(x1)

    for i in range(maxI):
        x2 = x1 - (f0*((x1-x0)/(f1-f0)))
        error = abs(x2 - x1)
        if error < tolerance:
            return error
        else:
            x0 = x1
            x1 = x2
            f0 = function(x0)
            f1 = function(x1)

    return error


newtonList = []
for i in range(1, 100):
    newtonList.append(NewtonsMethod(1, PracticeFunction.practFunc,PracticeFunction.practDeriv, 0.000001, i))

secantList = []
for i in range(1, 100):
    secantList.append(secant(.5, 1, PracticeFunction.practFunc, 0.000001, i))


test(newtonList)
test(secantList)
