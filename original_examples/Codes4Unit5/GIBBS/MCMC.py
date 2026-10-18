# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:42:53 2019

@author: bv20
"""

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(100)
n=100
y = np.random.normal(1,2,n) #construct the sample of size 100
#------------------------------------------
NN = 10000;
mus = np.array([])
taus = np.array([])
sumdata = np.sum(y) 
#hyperparameters
mu0=0.5
tau0 = 1/100
a= 1/2
b= 2
# start, initial values
mu =  0.5    
tau = 0.5   
for i in range(NN):
  newmu  = np.random.normal((tau * sumdata+tau0*mu0)/(tau0+n*tau), 
                            np.sqrt(1/(tau0+n*tau)))
  #par   = b+1/2 * np.sum ( (y - mu)**2) 
  par   = b+1/2 * np.sum ( (y -  mu)**2) 
  newtau = np.random.gamma(a + n/2, 1/par); #par is rate
  mus = np.append(mus, newmu)
  taus = np.append(taus, newtau)
  mu = newmu 
  tau = newtau 
 
 
burn =200 
mus  = mus[burn:NN] 
taus = taus[burn:NN] 

print(np.mean(mus))
print(np.mean(taus))

fig, ax = plt.subplots()
plt.subplot(2,1,1) 
plt.hist(mus, 40)
plt.subplot(2,1,2) 
plt.hist(taus, 40)
plt.show()
fig.savefig('gbs.eps',format='eps')


#fig, ax = plt.subplots()
# Do the plot code
#fig.savefig('myimage.svg', format='svg', dpi=1200)
