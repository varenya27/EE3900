import numpy as np 
import matplotlib.pyplot as plt
def u(n):
    if n<0: return 0
    return 1

def v(n,v_list):
    C=1e-6
    if n==0: return 0
    if len(v_list)!=0:
        return (1+v_list[-1]*(1.5-C))/(1.5+C) 
    return v(n)*((C-0.75)/(C+0.75))+(u(n+1)+u(n))/(2*C+1.5)

n=np.linspace(0,1e-5)
vi=[]

for i in n:
    vi.append(v(i,vi))
plt.figure()
plt.plot(n,vi)
print(vi)
plt.show()