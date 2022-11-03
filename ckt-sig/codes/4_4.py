import numpy as np 
import matplotlib.pyplot as plt
def u(n):
    if n<0: return 0
    return 1

def v(n):
    C=1e-6
    a= (C-0.75e-7)/(C+0.75e-7)
    b= 1/(C+0.75)

    return -(1-a**(n-1))/(1-a)


vi=[]


t,v_sim = np.loadtxt('out.txt', unpack=True)
for i in t:
    print(v(i))
    vi.append(v(i))
plt.figure()
plt.plot(t,v_sim,'bo', label='ngspice simulation')
plt.plot(t,vi,'ro', label='difference equation')
plt.plot(t,0.66*(1-np.exp(-1.5e6*t)), label='theory')
#plt.label(['ngspice simulations','theory'])
plt.legend()
plt.savefig('tmp.png')
