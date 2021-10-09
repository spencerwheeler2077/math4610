def bisection(a, b, function, tolerance):
    fa = function(a)
    fb = function(b)
    maxI = 100

    for i in range(maxI):
        c = (a + b) * 0.5
        fc = function(c)

        if fa * fb < 0:
            b = c
            fb = fc

        else:
            a = c
            fa = fc
        error = abs(b-a)
        if error <= tolerance:
            return c
    print("Failure to find root with given parameters")
    return

