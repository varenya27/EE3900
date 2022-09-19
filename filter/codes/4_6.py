import numpy as np
import matplotlib.pyplot as plt
#if using termux
import subprocess
import shlex
#end if


#DTFT
def H(z):
	num = np.polyval([1,0,1],z**(-1))
	den = np.polyval([0.5,1],z**(-1))
	H = num/den
	return H
		


#Input and Output
omega = np.linspace(-3*np.pi,3*np.pi,100)

#subplots
dx=0.2
plt.plot(omega, abs(H(np.exp(1j*omega))))
plt.plot(0,4/3,marker='o', color= 'black')
plt.plot(2*np.pi,4/3,marker='o',color='black')
plt.text(0+dx,4/3, "0,1.33")
plt.text(2*np.pi+dx,4/3, "2$\pi$,1.33")
plt.title('Filter Frequency Response')
plt.xlabel('$\omega$')
plt.ylabel('$|H(e^{\jmath\omega})| $')
plt.grid()# minor

#if using termux
# plt.savefig('../figs/dtft.pdf')
# plt.savefig('../figs/dtft.eps')
# subprocess.run(shlex.split("termux-open ../figs/dtft.pdf"))
#else
plt.show()