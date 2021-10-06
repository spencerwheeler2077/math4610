
**Routine Name:** doublePrecision, and singlePrecision

**Author:** Spencer Wheeler

**Language:** Python

**Description/Purpose:** These routine will compute the precision value for the machine epsilon or the number of digits
in the representation of real numbers in double and single precision. This is a routine for analyzing the behavior of 
any computer. The two routines are the exact same, only doublePrecision calculates the precision of double precision
values, and singlePrecision calculates the precision of single double precision values. 

For the rest of this page I will only talk about the doublePrecision routine, but everything should be the same for 
singlePrecision only the outputs will differ from each other, due to what each routine is calculating. 

**Input:** There are no inputs needed in this case. Even though there are arguments supplied, the real purpose is to
return values in those variables.

**Output:** This routine returns a single precision value for the number of decimal digits that can be represented on the
computer being queried.

**Usage/Example:**

The routine simple needs to be ran in a terminal, using this line,

    python *.doublePrecision.py
replacing * with the file path to where the file is located. The machine epsilon value should be printed to the screen as well as how many iterations it took to find the number, similar as seen here,

    -53 Iterations
    -2.220446049250313e-16

The code for doublePrecision is found below. 

    def doublePrecision():
    x = 1
    epsilon = .5
    for i in range(1, 100):
        xAprox = x+(epsilon)
        error = abs(x-xAprox)

        if error == 0:
            print(i, "Iterations")
            print(epsilon*2) #I multipied my final epsilon by two because I used numpy to find the actual epsilon
                             # and it seems my program would always do one more iteration after it found the epsilon
            break
        else:
            epsilon = epsilon / 2

    doublePrecision()

The code for singlePrecision is shown below

    from numpy import float32

    def singlePrecision():
        x = float32(1)
        epsilon = float32(.5)
        for i in range(1, 100):
            xAprox = x+(epsilon)
            error = abs(x-xAprox)
    
            if error == 0:
                print(i, "Iterations")
                print(epsilon*2) #I multipied my final epsilon by two because I used numpy to find the actual epsilon
                                 # and it seems my program would always do one more iteration after it found the epsilon
                break
            else:
                epsilon = epsilon / 2

   