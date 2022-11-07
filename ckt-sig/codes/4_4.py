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
#for i in t:
 #   print(v(i))
 #   vi.append(v(i))
plt.figure()
plt.plot(t,v_sim,'.', label='ngspice simulation')
#plt.plot(t,vi,'ro', label='difference equation')
plt.plot(t,0.66*(1-np.exp(-1.5e6*t)), label='theory')
#plt.label(['ngspice simulations','theory'])

T = 1e-7
tau = 2e-6/3
p = (2*tau-T)/(2*tau+T)
t = np.linspace(0, 1e-5, 111)
n = np.arange(0, 111, 1)
vn = 1 - p**n
print(vn)
print(np.pad(vn, (0,1), constant_values=(0,0)))
print(np.pad(4, (1,0), constant_values=(0,0)))
vn = np.pad(vn, (0,1), constant_values=(0,0)) + np.pad(vn, (1,0), constant_values=(0,0))
vn =0.5* 0.666*vn
plt.plot(t,vn[0:111],'.', label='difference equation')
plt.legend()
plt.savefig('tmp.png')
