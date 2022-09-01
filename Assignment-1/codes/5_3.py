import numpy as np
import matplotlib.pyplot as plt

#checking for stability:
n = np.arange(1000)
fn=(-1/2)**n
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))
sum=np.sum(hn1)+np.sum(hn2)
if sum<np.inf:
    print(sum,'Stable')
else: 
    print('Unstable')

#plotting

n=np.arange(10)
fn=(-1/2)**n
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))
print(hn1+hn2)
plt.stem(np.arange(12), hn1+hn2)
plt.title('Filter Impulse Response')
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()
plt.show()
