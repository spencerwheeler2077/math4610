import PracticeFunction


def secant(x0, x1, function, tolerance, maxI):
    f0 = function(x0)
    f1 = function(x1)


    for i in range(maxI):
        x2 = x1-((x1-x0)/(f1-f0))
        error = abs(x2 - x1)
        if error < tolerance:
            return x2
        else:
            x0 = x1
            x1 = x2
            f0 = function(x0)
            f1 = function(x1)

    return None

print(secant(1, 0, PracticeFunction.practFunc, .000001, 10000))

