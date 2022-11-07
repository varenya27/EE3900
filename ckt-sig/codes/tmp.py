import numpy as np
from matplotlib import pyplot as plt
import os
#from scipy import signal


os.system('cat 4_7.cir | ngspice')
k = 1.5e6
T = 1e-7
tau = 2e-6/3
p = (2*tau-T)/(2*tau+T)
R1 = 1
R2 = 2
V2 = 2
C0 = 1e-6
t = np.linspace(0, 1e-5, 101)
n = np.arange(0, 101, 1)
vn = 1 - p**n
print(vn)
print(np.pad(vn, (0,1), constant_values=(0,0)))
print(np.pad(4, (1,0), constant_values=(0,0)))
vn = np.pad(vn, (0,1), constant_values=(0,0)) + np.pad(vn, (1,0), constant_values=(0,0))
vn = 0.666*vn
vn[0] = 0
plt.plot(t, 2*(1 - np.exp(-k*t))/3)
plt.plot(t, (V2*tau/(2*C0*R2))*vn[:len(t)], '.')
plt.legend(['Theory (continuous)', 'Theory (discrete)', 'Simulation (ngspice)'])
# plt.show()
