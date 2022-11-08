from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
import numpy as np
from scipy import fft
def rect(x):
    y=[]
    for i in x:
        if abs(i)<=1: y.append(1)
        else: y.append(0)
    return np.array(y)

f0= 50
f=np.arange(-f0,f0,0.5)
x=np.linspace(0,1)
t=np.arange(-10,10,.1)
plt.figure()
# plt.plot(f,rect(f))

y = np.fft.fft(rect(t))
freq=np.fft.fftfreq(t.shape[-1])
print(t.shape[-1])

# plt.scatter(freq,y.real/10,color='orange',label='sim')

ts = 1e-2
sig = np.zeros(200)
sig[:100] = 1
print(sig)
ft = fft.fftshift(fft.fft(sig))
ft = np.abs(ft)/max(np.abs(ft))
freq = fft.fftshift(fft.fftfreq(sig.size, d=ts))
plt.plot(freq, ft, '.',label='sim')
plt.plot(freq,np.sinc(f),label='analysis')

plt.grid()
plt.xlabel('f')
plt.ylabel('sinc(f)')
plt.legend()
plt.savefig('charger/figures/rect-ft.png')