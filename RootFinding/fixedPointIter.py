import math


def fixedPointIter(x0, function, tolerance, maxI):
    g = function
    for i in range(maxI):
        x1 = x0 + eval(function.replace("x", f"({x0})"))
        error = abs(x1-x0)
        x0 = x1
        print(i)

        if error <= tolerance:
            return x1, i

print(fixedPointIter(1.9, "(x-2)**2", .00001, 10000))
# the line above was for testing the function.
