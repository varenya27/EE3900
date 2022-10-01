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
for i in range(10,1000,10):
    x=3*np.random.random(i)

    s=time.time()
    X=fft_matrix(x)
    t_mat.append(time.time()-s)
    s=time.time()
    X=fft(x)
    t_fft.append(time.time()-s)
    x_.append(i)
t=75*10**(-8)
x_=np.array(x_)
plt.figure()
plt.grid()
plt.scatter(x_,t_mat,color='#253f85',s=1)
plt.scatter(x_,t_fft,color='orange',s=1)
plt.plot(x_,t*x_*x_,color='#253f85')
plt.plot(x_,t*x_*np.log(x_),color='orange')
plt.title('Time analysis of the two algorithms')
plt.xlabel('Number of iterations')
plt.ylabel('Time (ms)')
plt.legend(['DFT - matrix multiplication','FFT','$O(n^2)$','$O(nlogn)$'])
plt.savefig('filter/figures/complexity2.png')