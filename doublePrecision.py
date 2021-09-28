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