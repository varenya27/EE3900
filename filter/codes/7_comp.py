import numpy as np 
from scipy.fft import fft,ifft
from matplotlib import pyplot as plt 
import time

def fft_matrix(x):
    # x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
    w=np.exp(2*np.pi*1j/len(x))
    # print(w)
    n=len(x)
    F = np.array([0+1j]*n**2).reshape(n,n)
    for i in range(n):
        for j in range(n):
            F[i][j]=w**(i*j)
    # print(F)
    X=np.dot(F,x)
    return X
t_mat,t_fft=[],[]
x_=[]
for i in range(5,500):
    x=3*np.random.random(i)

    s=time.time()
    X=fft_matrix(x)
    t_mat.append(time.time()-s)
    s=time.time()
    X=fft(x)
    t_fft.append(time.time()-s)
    x_.append(i)
print(t_mat,t_fft)

plt.figure()
plt.plot(x_,t_mat)
plt.plot(x_,t_fft)
plt.legend(['DFT','FFT'])
plt.savefig('figures/complexity.png')