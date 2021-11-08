import RootFinding.Bisection as Bisection
import RootFinding.NewtonsMethod as Newtons
import RootFinding.secantMethod as Secant
import RootFinding.fixedPointIter as Fixed

import math


def function(x):
    return math.e**(-(x**2))*math.sin(4*(x**2)-1) + 0.051


def fixedFunction(x):
    return .5*function(x)

def derivative(x):
    return 8*x*(math.e**(-(x**2)))*math.cos(4*(x**2)-1) - 2*x*(math.e**(-(x**2)))*math.sin(4*(x**2)-1)


def main():
    tolerance = .00001
    middle = Bisection.bisection(0, .9, function, tolerance, 10)
    print(middle, "after 15 steps of bisection")

    print(Newtons.NewtonsMethod(middle, function, derivative, tolerance, 50),
          "Result of Newton's method")

    #print(Secant.secant(middle - .01 , middle + 0.01, function, tolerance, 500),
    #      "Result of Secant method")

    print(Fixed.fixedPointIter(middle, fixedFunction, tolerance, 10000),
          "Result of fixed point iteration")

    '''
    This was my attempt to do task 5, if you run these lines they both produce errors. 
    print("Newton's method starting at -5", Newtons.NewtonsMethod(-5, function, derivative, tolerance, 50))
    print("Newton's method starting at 6", Newtons.NewtonsMethod(6, function, derivative, tolerance, 50))
    '''
    return



if __name__ == "__main__":
    main()
