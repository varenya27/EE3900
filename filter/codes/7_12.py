import numpy as np
from scipy.fft import fft, ifft

x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
x=np.pad(x, (0,2), 'constant', constant_values=(0))
# print(x)
X=fft(x)
print(X)