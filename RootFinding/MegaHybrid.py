from RootFinding import Hybrid
import numpy


def megaHybrid(minX, maxX, function, derivative, tolerance, maxI):
    interval = 0.01
    yList = []
    xList = []
    index = 0
    for i in numpy.arange(int(minX), maxX, interval):
        yList.append(function(i))
        if len(yList) > 1:
            if yList[index] * yList[index - 1] < 0:
                xList.append([(i-interval), i])
        index = index + 1

    roots = []
    for rootInterval in xList:
        a = rootInterval[0]
        b = rootInterval[1]
        roots.append(Hybrid.hybrid(a, b, function, derivative, tolerance, maxI))
    return roots

