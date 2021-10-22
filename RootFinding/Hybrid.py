import PracticeFunction
from NewtonsMethod import NewtonsMethod


def hybrid(a, b, function, derivative, x0, tolerance, MaxI):
    f0 = function(x0)
    d0 = derivative(x0)

    x1 = x0 - (f0/d0)
    e0 = abs(b-a)
    e1 = abs(x1-x0)
    while e1 > e0:
        x0, a, b = bisection(a, b, function, 4)
        f0 = function(x0)
        d0 = derivative(x0)
        x1 = x0 - f0 / d0
        e0 = abs(b - a)
        e1 = abs(x1 - x0)
    NewtonsMethod(x0, function, derivative, tolerance, MaxI)


def bisection(a, b, function, maxI):

    for i in range(maxI):
        c = (a + b) / 2
        fc = function(c)

        if function(a) * function(b) < 0:
            b = c

        else:
            a = c

    return c, a, b

print(hybrid(.5, 1, PracticeFunction.practFunc, PracticeFunction.practDeriv, .1, .0001, 100000))
