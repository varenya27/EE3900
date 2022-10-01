import numpy as np 
from matplotlib import pyplot as plt 

def x(n):
    if(n==1 or n==0): return 1
    return x(n-1)+x(n-2)

def y(n):
    return x(n-1)+x(n+1)
n=10
x_=[]
y_=[]
for i in range(1,n+1): 
    x_.append(x(i))
    y_.append(y(i))
plt.figure()
plt.stem(np.arange(n),y_)
plt.grid()
plt.ylabel('$y(n)$')
plt.xlabel('$n$')
plt.title('Pingala Series stem plot')
# plt.show()
# plt.legend(['y(n)','x(n)'])
plt.savefig('pingala/figures/2_5.png')