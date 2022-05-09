# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 22:18:07 2017
@author: bv20
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate
#COIN

plt.figure()
p = np.arange(0,1,0.001)
p10t = lambda p: 11 * (1-p)**10
plt.plot(p, p10t(p),label='density')
 
area = scipy.integrate.quad(p10t, 0, 1)
print(area)
#
#for the mean
pp10t = lambda p: 11 * p * (1-p)**10 
mean=scipy.integrate.quad(pp10t, 0, 1)
print(mean)
# for the median
is05 = scipy.integrate.quad(p10t, 0, 0.0610690893384)
print(is05)
#
plt.scatter((0,0), (0,11), color = 'r', alpha=0.5, s=100, label='mode')
plt.scatter((1/12,1/12), (0,p10t(1/12)), color = 'g', alpha=0.5, s=100, label='mean')
x=(0.06107, 0.06107); y=(0,  p10t(0.06107))
plt.scatter(x, y, color = 'k', alpha=0.5, s=100, label='median')
plt.legend(loc='upper right')
plt.show()
