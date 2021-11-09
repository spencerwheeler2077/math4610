import RootFinding.Bisection as Bisection
import RootFinding.NewtonsMethod as Newtons
import RootFinding.secantMethod as Secant
import RootFinding.fixedPointIter as Fixed
import RootFinding.MegaHybrid as Mega

import math


def function(x):
    return math.e**(-(x**2))*math.sin(4*(x**2)-1) + 0.051


def fixedFunction(x):
    return .5*function(x)

def derivative(x):
    return 8*x*(math.e**(-(x**2)))*math.cos(4*(x**2)-1) - 2*x*(math.e**(-(x**2)))*math.sin(4*(x**2)-1)


def main():
    tolerance = .00001
    steps = 10
    middle = Bisection.bisection(0, .7, function, tolerance, steps)
    print(middle, f"after {steps} steps of bisection")

    print(Newtons.NewtonsMethod(middle, function, derivative, tolerance, 50),
          "Result of Newton's method")

    print(Secant.secant(middle, middle+.01, function, 0.01, 500),
          "Result of Secant method")

    print(Fixed.fixedPointIter(middle, fixedFunction, tolerance, 10000),
          "Result of fixed point iteration")

    '''
    This was my attempt to do task 5, if you run these lines they both produce errors.
    '''
    #print("Newton's method starting at -5", Newtons.NewtonsMethod(-5, function, derivative, tolerance, 50))
    #print("Newton's method starting at 6", Newtons.NewtonsMethod(6, function, derivative, tolerance, 50))

    return

def main2():

    minX = -5
    maxX = 6
    interval = .1
    # check around f(0)

    xList = []
    for i in range(0, int(maxX/interval) + 1):
        xList.append(function(interval*i))
        if len(xList) > 1:
            if xList[i]*xList[i-1] < 0:
                break

    print('Results for task 3,', Newtons.NewtonsMethod(i*interval, function, derivative, .001, 50))
    print('Results for task 4,', Secant.secant((i-1)*interval, i*interval, function, .001, 50))


def main3():

    print('All roots for task 5', Mega.megaHybrid(-5, 6, function, derivative, 0.001, 50))

if __name__ == "__main__":
    main()
    main2()
    main3()
