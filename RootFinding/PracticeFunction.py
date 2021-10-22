import math


def practFunc(x):
    return x*(math.e**(3*(x**2)))-7*x


def practDeriv(x):
    return math.e**(3*(x**2)) + 18*(x**3)*math.e**(3*(x**2)) - 7

