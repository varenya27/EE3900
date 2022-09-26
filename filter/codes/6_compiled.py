import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.fft import fft, ifft

#y(n) from the difference equation
y = np.zeros(20)
x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
k = 20
y[0] = x[0]
y[1] = -0.5*y[0]+x[1]

for n in range(2,k-1):
	if n < 6:
		y[n] = -0.5*y[n-1]+x[n]+x[n-2]
	elif n > 5 and n < 8:
		y[n] = -0.5*y[n-1]+x[n-2]
	else:
		y[n] = -0.5*y[n-1]
print(y)

#y(n) from dft
N = 14
n = np.arange(N)
fn=(-1/2)**n
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))
h = hn1+hn2

xtemp=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
x=np.pad(xtemp, (0,8), 'constant', constant_values=(0))

X = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
	for n in range(0,N):
		X[k]+=x[n]*np.exp(-1j*2*np.pi*n*k/N)
H = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
	for n in range(0,N):
		H[k]+=h[n]*np.exp(-1j*2*np.pi*n*k/N)

Y = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
	Y[k] = X[k]*H[k]
	
yd = np.zeros(N) + 1j*np.zeros(N)
ydft = np.zeros(N) + 1j*np.zeros(N)
for k in range(0,N):
	for n in range(0,N):
		yd[k]+=Y[n]*np.exp(1j*2*np.pi*n*k/N)

#print(X)
ydft = np.real(yd)/N
print(ydft)
#y(n) from fft
Xfft= fft(x)
Hfft = fft(h)
Yfft=X*H
yfft=ifft(Y).real
print(yfft)
#plots
# plt.figure()
# plt.stem(range(0,N),y,linefmt='turquoise')
# plt.stem(range(0,N),ydft[0:14],linefmt='orange')
# plt.stem(range(0,N),yfft[0:14],linefmt='green')

markerline1, stemlines, _ = plt.stem(range(0,N), y[0:14])
plt.setp(markerline1, 'markerfacecolor', 'b')
markerline2, stemlines, _ = plt.stem(range(0,N), ydft)
plt.setp(markerline2, 'markerfacecolor', 'r')
markerline3, stemlines, _ = plt.stem(range(0,N), yfft)
plt.setp(markerline3, 'markerfacecolor', 'g')
plt.title('y(n) from three different methods')
plt.legend(["From Difference Equation","From DFT","From FFT"])
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor
# plt.show()
plt.savefig('filter/figures/Figure_all.png')