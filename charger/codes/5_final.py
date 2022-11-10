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
t_fft = np.arange(0, 50/f0, ts)
x = A*np.abs(np.sin(2*np.pi*f0*t_fft))
X = fft(x)
f = fftfreq(x.size, d=ts)

H= 1/np.sqrt(1+(f/fc)**(2*n))
print(H)
Y=np.abs(H*X)
x1 = ifft(X)
h1 = ifft(H)
y1 = np.convolve(x1,h1)
plt.plot(f,np.abs(X),label='X(f)',)
plt.plot(f,(Y),label='Y(f)',)
plt.plot(f,np.abs(H),label='H(f)',)
y=(ifft(Y))
# t = fftfreq(y.size, d=1/ts)
t=1/f


# plt.plot(abs(t)[0:100], abs((y1)[len(t)-1:][0:100]-2.5), label='analysis')
# t_spice,v_spice= np.loadtxt('butt_final.txt',unpack=True)
# plt.scatter(t_spice,0.48*v_spice,5,color='orange',label='sim')


plt.grid()
plt.legend()
# plt.xlabel('t')
# plt.ylabel('y(t)',)

plt.xlabel('f')
# plt.ylabel('y(t)',)

# plt.savefig('../figures/butt_filt_phone.png')
plt.savefig('../figures/butt_filt_phone_transfer.png')
plt.title('The input, output and transfer functions in the freq domain')
plt.show()
