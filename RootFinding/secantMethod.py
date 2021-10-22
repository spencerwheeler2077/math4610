import PracticeFunction


def secant(firstx, secondx, function, tolerance, maxI):
    x0 = firstx
    x1 = secondx
    f0 = function(x0)
    f1 = function(x1)

    for i in range(maxI):
        x2 = x1 - (f0*((x1-x0)/(f1-f0)))
        error = abs(x2 - x1)
        if error < tolerance:
            return x2
        else:
            x0 = x1
            x1 = x2
            f0 = function(x0)
            f1 = function(x1)

    return None


#print(secant(-.5, -1, PracticeFunction.practFunc, .000000001, 10000000))

