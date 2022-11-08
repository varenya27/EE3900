import numpy as np 
import matplotlib.pyplot as plt

inf = int(1e3)
t = np.linspace(0,0.025,inf)

def a(k):
    if k==0: return 24/np.pi
    if ~(k%2): return 48/np.pi/(1-k**2)
    return 0
k = np.arange(0,inf,2)
x_sum=np.zeros(len(t))
for i in (k):
    x_sum+=a(i)*np.cos(100*np.pi*t*i)
A,f = 12,50
plt.figure() 
plt.plot(t,A*abs(np.sin( 2*(np.pi)*f*t) ), label = 'theory')
plt.scatter(t,x_sum, 5,color='pink', label = 'sim, $a_k,b_k$')
plt.grid()
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.savefig('charger/figures/xt-sim-ab.png')