from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
import numpy as np
from scipy import fft
def rect(x):
    y=[]
    for i in x:
        if abs(i)<=0.5: y.append(1)
        else: y.append(0)
    return np.array(y)

f0= 4
t0=1e4
f=np.arange(-f0,f0,0.01)
t=np.arange(-t0,t0,0.1)

plt.figure()

ts = 2e-4
N = 100
mid = int(N/ts)
sig = np.sinc(np.arange(-N, N, ts))
sig_fft = fft.fftshift(fft.fft(sig))
sig_fft = np.abs(sig_fft)/np.abs(sig_fft[mid])
sf = fft.fftshift(fft.fftfreq(sig.size, d=ts))
plt.plot(sf, sig_fft, '.')

plt.plot(f,rect(f),label='analysis')
plt.grid()
plt.xlabel('f')
plt.ylabel('rect(f)')
plt.xlim(-5,5)
plt.legend()
plt.savefig('charger/figures/sinc-ft.png')