import numpy as np

x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
k = 20
y = np.zeros(20)


y[0] = x[0]

y[1] = -0.5*y[0]+x[1]

for n in range(2,k-1):
    if n < 6:
        y[n] = -0.5*y[n-1]+x[n]+x[n-2]
    elif n > 5 and n < 8:
        y[n] = -0.5*y[n-1]+x[n-2]
    else:
        y[n] = -0.5*y[n-1]

