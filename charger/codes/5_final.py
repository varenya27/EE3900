from scipy.fft import fft, fftfreq, ifft
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import math
plt.figure()

inf=1e2

A,f0 = 12,50
def delta(x):
    if math.isclose(x,0): return 80000
    return 0
def x_(t):
    return A*abs(np.sin(2*np.pi*f0*t))
def X(f):
    k_=np.arange(-inf,inf)
    ft=0
    for k in k_:
        ft+=(2*A/(np.pi*(1-4*k**2))*delta(2*k*f0+f))
    return ft

x_ft=[]

n = 5
fc = 50
b, a = signal.butter(n, fc, analog=True)
f, H = signal.freqs(b, a)
t=1/f


ts = 1e-4
t_fft = np.arange(-2/f0, 2/f0, ts)
x = A*np.abs(np.sin(2*np.pi*f0*t_fft))
X = fft(x)
f = fftfreq(x.size, d=ts)

H= 1/np.sqrt(1+(f/fc)**(2*n))
print(H)
Y=np.abs(H*X)
# plt.plot(sampl_freq,np.abs(sig_fft),label='X(f)',color='blue')
# plt.plot(f,(Y),label='Y(f)',color='orange')
# plt.plot(f,np.abs(H),label='H(f)',color='red')
y=(ifft(Y))
t = fftfreq(y.size, d=1/ts)
t=1/f
print('t=',t)
# t=np.linspace(-1,1,len(y))
# y=(fft(Y))
# plt.plot(f, Y)
# plt.plot(sampl_freq_y,5*(y),label='y(t)')
# plt.plot(t,ifft(x_ft))
plt.plot(np.abs(t), (y), label='y(t)')
plt.grid()
plt.legend()
plt.xlabel('t')
plt.ylabel('y(t)',)
plt.show()