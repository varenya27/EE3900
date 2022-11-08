import numpy as np 
import matplotlib.pyplot as plt

inf = int(1e3)
t = np.linspace(0,0.025,inf)
def c(k):
    if (k%2): return 24/np.pi/(1-k**2)
    return 0
def c1(k):
    return 24/np.pi/(1-k**2)

k = np.arange(-inf/10,inf/10,2)
print(np.exp(100*np.pi*1j*t))
x_sum=np.zeros(len(t))*np.exp(2j*np.pi)
for i in (k):
    x_sum+=c1(i)*np.exp(100*np.pi*1j*t*i)
print(x_sum)
A,f = 12,50
print(np.sin(2*np.pi))
plt.figure() 
plt.plot(t,A*abs(np.sin( 2*(np.pi)*f*t) ), label = 'theory')
plt.scatter(t,x_sum, 5,color='orange', label = 'sim')
plt.grid()
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.savefig('charger/figures/xt-sim.png')