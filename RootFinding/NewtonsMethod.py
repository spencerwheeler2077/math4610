import PracticeFunction


def NewtonsMethod(aproxX, function, derivative, tolerance, maxI):
    x0 = aproxX
    fx = function(x0)
    fprimex = derivative(aproxX)

    for i in range(maxI):
        x1 = x0 - (fx/fprimex)
        error = abs(x1 - x0)
        if error <= tolerance:
            return x1
        else:
            x0 = x1
            fx = function(x0)
            fprimex = derivative(x0)
    return x1


#print(NewtonsMethod(.3, PracticeFunction.practFunc, PracticeFunction.practDeriv, .0001, 10000000))