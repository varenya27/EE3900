import numpy as np
from matplotlib import pyplot as plt

s = np.linspace(0,1e7)
plt.figure()
plt.plot(s,1e6/(2*(s+1.5e6)))
plt.grid()
plt.xlabel('s')
plt.ylabel('H(s)')
plt.savefig('../figs/4_3.png')
