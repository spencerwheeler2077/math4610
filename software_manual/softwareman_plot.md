
**Routine Name:** plot

**Author:** Spencer Wheeler

**Language:** Python

**Description/Purpose:** This routine will create a graph of given expressions.

**Input:** Input at least one algebraic expression using x, as your variable. Multiple arguments can be given as
arguments, just seperate them with columns as such,

    plot("x", "2*x")

most math operations will work just as python normally handles them. So make sure if you want to do multiplication use 
"*" the routine will not automatically evaluate something like "2x". The python library math is imported into this 
routine so if you would like to use an operation that is not normally supported by python(, use the operation that is 
in this library, input it as something like the following,

    plot("math.*(x)")

replace ing "*" with operation that you would like to use. 


**Output:** Will create a graph, that will appear on your screen. 

**Usage/Example:**

The routine is just a single function that can be imported into other projects. This import is done with the following

    import */plot


The code for this routine is found below. 

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
    
    
    plot("2*x+4", "3*x**2-x+math.sin(2*x)")

   