import numpy as np 
import matplotlib.pyplot as plt
def u(n):
    if n<0: return 0
    return 1
T=1e7
c=1e-6
def v(n,vi):
    a = (4*c*T-3)/(4*c*T+3)
    b=4/(4*c*T+3)
    if len(vi)==0: vi.append(0)
    else:
        vi.append(a*vi[-1]+b)
    
t,v_sim = np.loadtxt('ckt-sig/codes/out.txt', unpack=True)
n = np.arange(1,111)/1e7

vi=[]
for i in n:
    v(i,vi)

plt.figure()
# plt.plot(n,2/3*(1-(1-7.5e5**(n*1e7))/(1+7.5e5**(n*1e7))),'.', label='pls work')
# t = np.linspace(0, 1e-5, 111)

plt.plot(n,np.array(vi),'.', label='difference equation from for loop') #spice
plt.plot(n,2/3 * (1 - ((4*c*T - 3)/(4*c*T + 3))**(n*1e7)),'.', label='inv z transform') #spice

plt.plot(t,v_sim,'.', label='ngspice simulation') #spice
plt.plot(t,0.66*(1-np.exp(-1.5e6*t)), label='theory') #analytic

#minor
plt.grid()
plt.legend()
plt.savefig('ckt-sig/figs/vns.png')
plt.show()
