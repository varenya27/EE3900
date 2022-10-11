import numpy as np 
from matplotlib import pyplot as plt 

def x(n):
    if(n==1 or n==0): return 1
    return x(n-1)+x(n-2)

n=10
x_=[]
for i in range(n+1): x_.append(x(i))
plt.figure()
plt.stem(np.arange(11),x_)
plt.grid()
plt.ylabel('$x(n)$')
plt.xlabel('$n$')
plt.title('Pingala Series stem plot')
# plt.show()
plt.savefig('pingala/figures/2_2.png')
