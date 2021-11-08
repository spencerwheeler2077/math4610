import math


def fixedPointIter(x0, function, tolerance=.000001, maxI=1000):
    for i in range(maxI):
        x1 = x0 - function(x0)
        error = abs(x1-x0)
        x0 = x1

        if error <= tolerance:
            return x1
    print('Failure to find root with given parameters')
    return None

def testFunction(x):
    return .00000001*(x*(math.e**(x**2*3))-7*x)


#print(fixedPointIter(2.1, testFunction, 10000000, .00000001))
#Test line above