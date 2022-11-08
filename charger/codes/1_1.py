import numpy as np 
from matplotlib import pyplot as plt 
import math
A,f = 12,50
t = np.arange(-0.025,0.025,0.0001)
print(np.sin(2*np.pi))
plt.figure() 
plt.plot(t,A*abs(np.sin( 2*(np.pi)*f*t) ))
plt.grid()
plt.xlabel('t')
plt.ylabel('x(t)')
plt.savefig('charger/figures/1_1.png')