
def fixedPointIter(x0, function, maxI=1000,  tolerance=.000001):
    for i in range(maxI):
        x1 = x0 - function(x0)
        error = abs(x1-x0)
        x0 = x1

        if error <= tolerance:
            return x1, i

