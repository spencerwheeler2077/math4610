import math


def fixedPointIter(x0, function, maxI=1000,  tolerance=.000001):
    for i in range(maxI):
        x1 = x0 - function(x0)
        error = abs(x1-x0)
        x0 = x1


        if error <= tolerance:
            return x1
    print('Failure to find root with given parameters')
    return None

def testFunction(x):
    return .01*(x*(math.e**(x**2*3))-7*x)


#print(fixedPointIter(1, testFunction, 100000, .0000000001))
#Test line above