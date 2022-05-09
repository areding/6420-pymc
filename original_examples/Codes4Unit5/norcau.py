g# -*- coding: utf-8 -*-
"""
Bayes estimator delta(x) for x=2,
for Normal-Cauchy Model
Created on Thu Dec 28 11:56:56 2017
@author: bv20
"""

from scipy import integrate, inf, exp
x = 2
num = lambda th: th * exp(-0.5*(x-th)**2)/(1+th**2)
denom = lambda th: exp(-0.5*(x-th)**2)/(1+th**2) 
delta2 = integrate.quad(num,-inf,inf)[0]/integrate.quad(denom,-inf,inf)[0]
#delta(2)
print(delta2) #1.2821951026935339

# Errors

numerator =integrate.quad(num,-inf,inf)[0]    #0.9159546679977636
denominator=integrate.quad(denom,-inf,inf)[0] #0.714364503556127
errnum=integrate.quad(num,-inf,inf)[1]        #1.0415234856193602e-09
errdenom=integrate.quad(denom,-inf,inf)[1]    #1.2022419107752649e-08

err = delta2 * (errnum/numerator + errdenom/denominator)
print(err)   #2.3036713479165735e-08