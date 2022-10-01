import numpy as np 
from math import isclose

alpha = (1+np.sqrt(5))/2
beta = (1-np.sqrt(5))/2

def a(n):
    return (alpha**n-beta**n)/(alpha-beta)
def b(n):
    return a(n-1)+a(n+1)

#1.1
n=np.random.randint(1,100)
sum_=0
for i in range(n+1): sum_+=a(i)
print('1.1:')
print('n=',n,'LHS =',round(sum_,3),'RHS =',round(a(n+2)-1,3))
print(isclose(sum_, a(n+2)-1))
#1.2
sum_=0
inf=100
for i in range(1,inf): sum_+=a(i)/(10**i)
print('1.2:')
print('Sum =', sum_,'10/89 =',10/89)
print(isclose(sum_,10/89))

#1.3
n=np.random.randint(1,100)
print('1.3: n =',n)
print('b(n) = ',round(b(n),3),'RHS = ',round(alpha**n+beta**n,3))
print(isclose(b(n), alpha**n+beta**n))

#1.4
print('1.4:')
sum_=0
inf=100
for i in range(1,inf): sum_+=b(i)/(10**i)
print('Sum =', sum_,'8/89 =',8/89)
print(isclose(sum_, 10/89))