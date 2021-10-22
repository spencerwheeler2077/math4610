import PracticeFunction
import NewtonsMethod


def bisection(a, b, function, maxI):
    """This is just like the normal bisection method but it returns c, and the new end points as well"""

    for i in range(maxI):
        c = (a + b) / 2
        fc = function(c)

        if function(a) * function(b) < 0:
            b = c

        else:
            a = c

    return c, a, b


def newtonsMethod(aproxX, function, derivative, tolerance, maxI):
    """This function is just like the newtonsMethod routine, but it returns the error not the x values."""

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


def checkConvergence(x0, function, derivative, tolerance):
    """
    This function runs two newtons methods, and see if the given values will begin to converge.
    """
    e0 = newtonsMethod(x0, function, derivative, tolerance, 1)
    e1 = newtonsMethod(x0, function, derivative, tolerance, 2)
    return e1 > e0


def hybrid(a, b, function, derivative, x0, tolerance, MaxI):
    condition = checkConvergence(x0, function, derivative, tolerance)

    while condition:  # this loop keeps doing bisection until newton's method begins to converge.
        x0, a, b = bisection(a, b, function, 4)
        condition = checkConvergence(x0, function, derivative, tolerance)

    return NewtonsMethod.NewtonsMethod(x0, function, derivative, tolerance, MaxI)
    # use Newtons method until root is found.

# print(hybrid(-3, 0, PracticeFunction.practFunc, PracticeFunction.practDeriv, 2, .0001, 100000))
