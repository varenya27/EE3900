import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0,10)

print(x)
plt.figure()
plt.plot(x,x**2)
plt.grid()
plt.savefig("phone_plit.png")

