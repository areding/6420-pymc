#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymc3 as pm
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gamma as gamma_func
from scipy.optimize import fsolve
from scipy.stats import gamma


# # Gamma Gamma
# 
# 
# From [Codes for Unit 4: gammagamma.m](https://www2.isye.gatech.edu/isye6420/supporting.html).
# 
# Associated lecture videos: [Unit 4 Lesson 10: Credible Sets](https://www.youtube.com/watch?v=AV7PtxWQYVw&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=27) and [Unit 4 Lesson 11](https://www.youtube.com/watch?v=kXRS22YMrSk&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=28).
# 
# Professor Vidakovic usually calls them credible sets. If you search for more information online, you'll see a lot of terms thrown around: Bayesian credible intervals or just credible intervals, highest density regions, highest posterior density intervals (HDPI) or just highest density intervals (HDI), percentile intervals, and compatibility intervals. Not to be confused with confidence intervals!
# 
# These terms don't all mean exactly the same thing. For our class, the main distinction the professor draws is between HPD-credible sets and equitailed credible sets. Sometimes the homework will ask for one or the other, or both, so make sure you understand the difference. If the homework doesn't specify, you can use either, but the equitailed credible set is easier to calculate.
# 
# First, here's a direct translation from the MATLAB code.

# In[2]:


def gamma_pdf(x, a, b):
    """
    Gamma pdf
    
    x: numpy array or float
    a: int or float. shape (α)
    b: int or float. rate (β)
    
    returns a numpy array or float
    """
    return 1/gamma_func(a) * x**(a - 1) * b**a * np.exp(-b*x)


# In[3]:


# figure 1

# unlike MATLAB i:j:k syntax, arange is not inclusive at the high end
xx = np.arange(.01, .601, .001)
a = 4
b = 29

# curve
plt.plot(xx, gamma_pdf(xx, a, b))

# additional markings
plt.plot(xx, np.full_like(xx, .857), 'r-')
plt.plot(.0246, gamma_pdf(.0246, a, b), 'o')
plt.plot(.0246, 0, 'ro')
plt.plot(.2741, gamma_pdf(.2741, a, b), 'o')
plt.plot(.2741, 0, 'ro')
plt.plot([0.0246, 0.2741], [0, 0], 'r-', linewidth=4)
plt.show()


# In[4]:


# hpd credible set

k = .857368863848

lower_hpd = fsolve(lambda x: gamma_pdf(x, a, b) - k, 0.05)[0]
upper_hpd = fsolve(lambda x: gamma_pdf(x, a, b) - k, 0.4)[0]
print(f'Equitailed credible set: [{lower_hpd} {upper_hpd}]')

prob_hpd = gamma.cdf(upper_hpd, a, scale=1/b) - gamma.cdf(lower_hpd, a, scale=1/b)
print(f'Probability within hpd bounds: {prob_hpd}')
print(f'length of hpd cs: {upper_hpd - lower_hpd}')


# In[5]:


# equi-tailed credible set

# percent point function aka quantile aka inverse cdf
lower_eqt = gamma.ppf(.025, a, scale=1/b)
upper_eqt = gamma.ppf(.975, a, scale=1/b)
print(f'Equitailed credible set: [{lower_eqt} {upper_eqt}]')

prob_eqt = gamma.cdf(upper_eqt, a, scale=1/b) - gamma.cdf(lower_eqt, a, scale=1/b)
print(f'Probability within eqt bounds: {prob_eqt}')
print(f'length of eqt cs: {upper_eqt - lower_eqt}')


# In[6]:


# figure 2

# curve
plt.plot(xx, gamma_pdf(xx, a, b), 'k-', linewidth=2)

plt.plot(lower_eqt, gamma_pdf(lower_eqt, a, b), 'o')
plt.plot(lower_eqt, 0, 'ro')
plt.plot(upper_eqt, gamma_pdf(upper_eqt, a, b), 'o')
plt.plot(upper_eqt, 0, 'ro')
plt.plot([lower_eqt, upper_eqt], [0, 0], 'r-', linewidth=4)
plt.plot([lower_eqt, upper_eqt],
         [gamma_pdf(lower_eqt, a, b), gamma_pdf(upper_eqt, a, b)],
         'k-',
         linewidth=1)
plt.show()


# Right now I want to get through these examples so Spring 2022 students can get some use out of them. Later on, I think this example could use a lot more explanation and expansion.

# In[ ]:




