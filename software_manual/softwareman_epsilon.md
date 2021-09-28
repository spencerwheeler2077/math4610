
**Routine Name:**           smaceps

**Author:** Joe Koebbe

**Language:** Python

**Description/Purpose:** This routine will compute the double precision value for the machine epsilon or the number of digits
in the representation of real numbers in double precision. This is a routine for analyzing the behavior of any computer. This
usually will need to be run one time for each computer.

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

The code for this routine is found below. 

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
   