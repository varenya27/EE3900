import numpy as np
from matplotlib import pyplot as plt
from scipy import signal

A = np.loadtxt('butt.txt')
n = 5
fc = 60
b, a = signal.butter(n, fc, analog=True)
f, h = signal.freqs(b, a)
plt.plot(A[:,0], A[:,1], '.',label='sim')
plt.semilogx(f, 20*np.log10(np.abs(h)),label='analysis')
plt.grid()
plt.legend()
plt.show()
# plt.savefig('../figures/butt.png')