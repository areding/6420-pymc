#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from tqdm.auto import tqdm


# # Metropolis-Hastings Example 1
# 
# Adapted from [Codes for Unit 5: norcaumet.m](https://www2.isye.gatech.edu/isye6420/supporting.html).
# 
# Associated lecture video: [Unit 5 Lesson 7](https://www.youtube.com/watch?v=hH2VCAgrQEQ&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=43).
# 
# 
# Let $f(x)$ be proportional to the target pdf. $x_j$ is the current value and $q(x|x_j)$ is a proposal distribution.
# 1. Sample $x_* ∼ q(x|x_j)$.
# 2. Calculate the acceptance probability: 
# $ρ(x_j, x_*) = min\left\{1, \frac{f(x_*)}{f(x_j)}\frac{q(x_j|x_*)}{q(x_*|x_j)}\right\}$
# 3. Update $x_{j+1} = x_*$ with probability $ρ(x_j, x_*)$, otherwise $x_{j+1}$ remains equal to $x_j$.
# 
# There are different variations on the algorithm. They differ when calculating $ρ$.
# - Random-walk Metropolis:
#   - If $q$ is symmetric, then you can simplify the acceptance probability to $ρ(x_j, x_*) = min\left\{1, \frac{f(x_*)}{f(x_j)}\right\}$
# - Independent Metropolis-Hastings:
#   - If $q$ is independent, then the acceptance probability is $ρ(x_j, x_*) = min\left\{1, \frac{f(x_*)}{f(x_j)}\frac{q(x_j)}{q(x_*)}\right\}$

# For this example:
# 
# $X|\theta~\sim{N}(\theta, 1)$ and $\theta~\sim {\rm Cauchy}(0, 1)$

# In[2]:


rng = np.random.default_rng(1)

n = 1000000 # observations
burn = 500
theta = 1 # init
thetas = np.zeros(n)
x = 2 # observed

# generating necessary randoms as arrays is faster
theta_prop = rng.standard_normal(n) + x
unif = rng.uniform(size=n)

for i in tqdm(range(n)):
    r = (1 + theta**2)/(1 + theta_prop[i]**2)
    rho = min(r, 1)
    if unif[i] < rho:
        theta = theta_prop[i]
    
    thetas[i] = theta

thetas = thetas[burn:]

print(f'{np.mean(thetas)=}')
print(f'{np.var(thetas)=}')

plt.hist(thetas, 50)
plt.show()


# In[ ]:




