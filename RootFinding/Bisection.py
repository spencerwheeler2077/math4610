import PracticeFunction


def bisection(a, b, function, tolerance, maxI):

    for i in range(maxI):
        c = (a + b) / 2
        fc = function(c)

        if function(a) * function(b) < 0:
            b = c

        else:
            a = c

        if abs(function(c)) < tolerance:
            return c

    return c

print(bisection(.6, 1.95, PracticeFunction.practFunc, 0.1, 4))

