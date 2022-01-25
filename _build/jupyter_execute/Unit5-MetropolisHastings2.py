#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from tqdm.auto import tqdm


# # Metropolis-Hastings Example 2
# 
# Adapted from [Codes for Unit 5: metro2.m](https://www2.isye.gatech.edu/isye6420/supporting.html).
# 
# Associated lecture video: [Unit 5 Lesson 9](https://www.youtube.com/watch?v=Zs3y-Hs76sM&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=45).

# In[ ]:


rng = np.random.default_rng(1)

burn = 500
theta = 1 # init
thetas = np.zeros(n)

# inits
alpha = 2
eta = 2
data = [.2, .1, .25] # observed
n = len(data) # observations

# generate proposals all at once for speed
theta_prop = rng.standard_normal(n) + x

for i in tqdm(range(n)):
    r = (1 + theta**2)/(1 + theta_prop[i]**2)
    rho = min(r, 1)
    if rng.uniform() < rho:
        theta = theta_prop[i]
    
    thetas[i] = theta

thetas = thetas[burn:]

print(f'{np.mean(thetas)=}')
print(f'{np.var(thetas)=}')

plt.hist(thetas, 50)
plt.show()

