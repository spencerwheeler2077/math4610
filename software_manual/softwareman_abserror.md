
**Routine Name:** abserror

**Author:** Spencer Wheeler

**Language:** Python

**Description/Purpose:** This routine will calculate the absolute error of two numbers.

**Input:** Input two numbers, the first being you approximation and the second being you exact number. 

**Output:** A single floating point number will be returned after running the routine. 

**Usage/Example:**

The routine is just a single function that can be imported into other projects. This import is done with the following

    import */Absolute Error
replacing * with the file path to where the file is located. Next just call this function where needed in your code. 
Replacing x and y with your needed inputs. 

    abserror(x,y)

The code for this routine is found below. 

    

    def abserror(xAprox, xexact):
        return abs(xAprox-xexact)
   