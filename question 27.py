## exercice 0
for x in 'bnj':
    print(x+'o')

##exercice 1
x=0
for i in range(34):
    x=x+i**2
print(x)

## exercice 2
n=10
a=1
for i in range(1,n+1):
    a=a*i
    print(a,i)

## exercice 3
def triplet(x,a,b):
    s=0
    p=1
    for k in range (1,a):
        p=p*x
    for k in range(a,b+1):
        p=p*x
        s=s+p
        print(s,p,k)
    return s

#### PARTIE 2

## question 2.1

K=[]
for i in range(1,16):
    K.append(i**2)
print(K)

## question 2.2

K.extend(K)
print(K)

## question 2.3

print(K[17])
K.pop(17)
print(K)

## question 2.4
Kinv=[]
for i in range (len(K)):
    Kinv.append(K[len(K)-1-i])
print (Kinv)

## question 2.5
l=[a,'b','c',[1.5,4],'salut']
print(l[3][0])

### CHAPITRES PLOT ET COURBE

from math import*
import math as m
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt

## exercice 1


X=np.linspace(0,5,11)

def f(x):
    return m.sqrt(abs(x**2-3*x+2))

Y=[0]*len(X)
for k in range (len(X)):
    Y[k]=f(X[k])

X1=np.linspace(0,5,51)

Y1=[0]*len(X1)
for k in range (len(X1)):
    Y1[k]=f(X1[k])

plt.plot(X,Y)
plt.plot(X1,Y1)
plt.show()


