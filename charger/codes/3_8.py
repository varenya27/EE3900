import numpy as np
from scipy.fft import fft,fftfreq
from scipy.signal import unit_impulse
from matplotlib import pyplot as plt

inf=1e2

A,f0 = 12,50
def delta(x):
    if x==0: return 800
    return 0
def x(t):
    return A*abs(np.sin(2*np.pi*f0*t))

def X(f):
    k_=np.arange(-inf,inf)
    ft=0
    for k in k_:
        ft+=(2*A/(np.pi*(1-4*k**2))*delta(2*k*f0+f))
    return ft
plt.figure()
f=np.arange(-5*f0,5*f0,10)
t = np.arange(-1/300,1/300,10/300)
x_ft,x_t=[],[]

for i in f:
    x_ft.append(np.abs(X(i)))

# print(x_ft)
# plt.stem(f,x_ft)
ts = 1e-4
t_fft = np.arange(-2/f0, 2/f0, ts)
sig = A*np.abs(np.sin(2*np.pi*f0*t_fft))
sig_fft = fft(sig)
sampl_freq = fftfreq(sig.size, d=ts)
markers,stems,base =plt.stem(sampl_freq, np.abs(sig_fft),label='sim',)
stems.set_linewidth(1)    
markers.set_markersize(5)
base.set_color('black')
# plt.plot(sampl_freq, np.abs(sig_fft),'C1',5,label='sim',)
plt.scatter(f,x_ft,20,color='orange',label='analysis')

plt.legend()
plt.xlim(-5*f0, 5*f0)
plt.grid()
# plt.show()
plt.savefig('charger/figures/xt-ft.png')