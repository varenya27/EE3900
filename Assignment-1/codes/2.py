import numpy as np
import matplotlib.pyplot as plt

#making data in python
if(0):
	x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
	k = 20
	y = np.zeros(20)


	y[0] = x[0]
	y[1] = -0.5*y[0]+x[1]

	for n in range(2,k-1):
		if n < 6:
			y[n] = -0.5*y[n-1]+x[n]+x[n-2]
		elif n > 5 and n < 8:
			y[n] = -0.5*y[n-1]+x[n-2]
		else:
			y[n] = -0.5*y[n-1]
	print(y)
#accessing data from txt file
if(1):
	k=20
	x=np.loadtxt('codes/2_x.txt')
	y=np.loadtxt('codes/2_y.txt')
	print(x,y)
#subplots
plt.subplot(2, 1, 1)
plt.stem(range(0,6),x)
plt.title('Digital Filter Input-Output')
plt.ylabel('$x(n)$')
plt.grid()# minor


plt.subplot(2, 1, 2)
plt.stem(range(0,k),y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()# minor

#If using termux
# plt.savefig('EE3900\Assignment-1\figures/xnyn.pdf')
# plt.savefig('EE3900\Assignment-1\figures/xnyn.eps')
# subprocess.run(shlex.split("termux-open EE3900\Assignment-1\figures/xnyn.pdf"))
# else
# plt.show()
plt.savefig('figures/Figure_1_C.png')
