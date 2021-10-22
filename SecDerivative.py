import numpy
from matplotlib import pyplot as plt


h = [1, .5]
for j in range(1, 17):
    h.append(h[-1]/10)

x = 2
exact = -numpy.cos(x)
error = []
derivList = []

for i in h:

    approxDer = (numpy.cos(x+i)-2*numpy.cos(x)+numpy.cos(x-i))/(i**2)
    derivList.append(approxDer)
    error.append(abs(exact-approxDer))

logerror = []
for i in error:
    logerror.append(numpy.log(i))

logH = []
for i in h:
    logH.append(numpy.log(i))


plt.xlabel('log(h-value)')
plt.ylabel('logerror')
plt.plot(logH, logerror)
plt.show()



print("h-value   error")
for i in range(len(h)):
    if i < 10:
        print(f"1e-{i}      {error[i]}")
    else:
        print(f"1e-{i}     {error[i]}")
