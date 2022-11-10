import matplotlib.pyplot as plt
import numpy as np

v= np.loadtxt('butt_final.txt',unpack=True)
plt.figure()
t=np.linspace(0,10,len(v))
plt.plot(t,v)
plt.savefig('tmp.png')
