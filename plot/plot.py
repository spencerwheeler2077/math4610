from matplotlib import pyplot as plt

import math


def plot(*args):
    for arg in args:
        xLimit = 20
        xValues = []
        yValues = []

        i = -20  # changing this number will change the lower bound

        while i < xLimit:
            argument = arg.replace("x", f"({i})")
            yValues.append(eval(argument))
            xValues.append(i)
            i = i + 0.1

        plt.plot(xValues, yValues)

    plt.show()



plot("x", "2*x")