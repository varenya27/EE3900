import numpy as np

x=np.array([1.0,2.0,3.0,4.0,2.0,1.0])
w=np.exp(2*np.pi*1j/len(x))
# print(w)

F = np.array([0+1j]*36).reshape(6,6)
for i in range(6):
    for j in range(6):
        F[i][j]=w**(i*j)
# print(F)
X=np.dot(F,x)
print(X)