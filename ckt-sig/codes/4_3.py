import numpy as np
from matplotlib import pyplot as plt 

s = np.linspace(0,10e6)
H = 0.5e6/(s+1.5e6)
plt.figure()
plt.plot(s,H)
plt.grid()
plt.xlabel('$s$')
plt.ylabel('$H(s)$')
plt.title('Transfer function')
# plt.show()
plt.savefig('../figs/transfer.png')
