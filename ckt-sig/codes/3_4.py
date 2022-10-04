import numpy as np
from matplotlib import pyplot as plt 

x = np.linspace(0,1e-5)

plt.figure()
plt.plot(x,(2/3)*(1+np.exp(-1.5 * x * (10**6) )))
plt.grid()
plt.xlabel('t')
plt.ylabel('$v_{C_0}(t)$')
plt.title('Voltage across the capacitor')
#plt.show()
plt.savefig('../figs/vct2.png')
