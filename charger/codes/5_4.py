import numpy as np
from matplotlib import pyplot as plt
from scipy import signal

A = np.loadtxt('cheb.txt')
n = 4
fc = 60
delta = 0.5
b, a = signal.cheby1(n, delta, fc, analog=True)
f, h = signal.freqs(b, a)
plt.plot(A[:,0], A[:,1], '.',label='sim')
plt.semilogx(f, 20*np.log10(np.abs(h)),label='analysis')
plt.grid()
plt.legend()
plt.savefig('../figs/cheb.png')