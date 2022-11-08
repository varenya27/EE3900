from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
import numpy as np

f0 = 50
A = 12

N,tp = int(1e4),int(1e4)
t = np.linspace(-tp, tp, N)
x = 5*np.pi*f0/12*np.sinc(2*f0*t)
h = A*np.abs(np.sin(2*np.pi*f0*t))
y = np.convolve(h, x, mode='same')
plt.plot(t, y*(2*tp/N))
plt.grid()
plt.xlabel('t')
plt.ylabel('y(t)',)
plt.savefig('charger/figures/conv-hx.png')