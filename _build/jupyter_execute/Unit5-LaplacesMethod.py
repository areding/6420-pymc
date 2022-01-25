#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy.stats import norm, gamma
import matplotlib.pyplot as plt


# # Laplace's Method
# 
# From [Codes for Unit 5: laplace.m](https://www2.isye.gatech.edu/isye6420/supporting.html).
# 
# Associated lecture video: [Unit 5 Lesson 3: Laplace's Method](https://www.youtube.com/watch?v=0FKg4sOvVu0&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=39).
# 
# This is just a direct translation into Python for now. I might add more explanation in the future.

# In[2]:


xx = np.arange(0, 16, .01)
r = 20
alpha = 5
beta = 1
x = 2

num = r - 1 + alpha
denom = x + beta

# normal parameters
mu = num/denom
sigma = num**.5/denom
# gamma parameters
shape = r + alpha
scale = 1/(beta + x)

exact = gamma.pdf(xx, a=shape, scale=scale)
approx = norm.pdf(xx, mu, sigma)

# credible intervals
exact_ci = gamma.ppf(.025, a=shape, scale=scale), gamma.ppf(.975, a=shape, scale=scale)
approx_ci = norm.ppf(.025, mu, sigma), norm.ppf(.975, mu, sigma)

print(f"Exact 95% credible interval: {exact_ci}")
print(f"Laplace approximation 95% credible interval: {approx_ci}")

plt.plot(xx, exact, label="Exact")
plt.plot(xx, approx, label="Laplace approx.")
plt.legend()
plt.show()

