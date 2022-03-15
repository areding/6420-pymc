#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
from tqdm.auto import tqdm


# # Gibbs Sampler Example 2: Pumps
# 
# Adapted from [Codes for Unit 5: pumpsmc.m and pumpsbugs.odc](https://www2.isye.gatech.edu/isye6420/supporting.html).
# 
# Associated lecture video: [Unit 5 Lesson 13](https://www.youtube.com/watch?v=DKlP93sD0O0&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=49).
# 
# Based on [Conjugate Likelihood Distributions, George, Makov, and Smith, 1993](https://www.jstor.org/stable/4616270) and [Robust Empirical Bayes Analyses of Event Rates, Gaver and O'Muircheartaigh, 1987](https://www.jstor.org/stable/1269878).

# In[2]:


rng = np.random.default_rng(1)

obs = 100000
burn = 1000

# data from Gaver and O'Muircheartaigh, 1987
X = np.array([5, 1, 5, 14, 3, 19, 1, 1, 4, 22])
t = np.array([94.32, 15.52, 62.88, 125.76, 5.24, 31.44, 1.048, 1.048, 2.096, 10.48])
n = len(X)

# params
c = 0.1
d = 1

# inits
theta = np.ones(n)
beta = 1

thetas = np.zeros((obs, 10))
betas = np.zeros(obs)

for i in tqdm(range(obs)):
    theta = rng.gamma(shape=X + 1, scale=1 / (beta + t), size=n)
    sum_theta = np.sum(theta)

    beta = rng.gamma(shape=n + c, scale=1 / (sum_theta + d))

    thetas[i] = theta
    betas[i] = beta

thetas = thetas[burn:]
betas = betas[burn:]

print(f"{np.mean(thetas, axis=0)=}")
print(f"{np.std(thetas)=}")
print(f"{np.mean(betas)=}")
print(f"{np.std(betas)=}")


# In[3]:


np.mean(thetas, axis=0)


# Now for the PyMC model:

# In[4]:


with pm.Model() as m:
    times = pm.Data("times", t)
    data = pm.Data("data", X)

    beta = pm.Gamma("beta", alpha=c, beta=d)
    theta = pm.Gamma("theta", alpha=d, beta=beta, shape=n)
    rate = pm.Deterministic("rate", theta * times)

    likelihood = pm.Poisson("likelihood", mu=rate, observed=data)

    # start sampling
    trace = pm.sample(
        5000,
        chains=4,
        tune=500,
        init="jitter+adapt_diag",
        random_seed=1,
        cores=4,
        return_inferencedata=True,
    )


# In[5]:


az.summary(trace, var_names=["~rate"])


# Compare to BUGS results:
# 
# |           | mean    | sd      | MC_error | val2.5pc | median  | val97.5pc | start | sample |
# |-----------|---------|---------|----------|----------|---------|-----------|-------|--------|
# | beta      | 1.34    | 0.486   | 0.002973 | 0.5896   | 1.271   | 2.466     | 1001  | 50000  |
# | theta[1]  | 0.06261 | 0.02552 | 1.11E-04 | 0.02334  | 0.05914 | 0.1217    | 1001  | 50000  |
# | theta[2]  | 0.118   | 0.08349 | 3.69E-04 | 0.01431  | 0.09888 | 0.3296    | 1001  | 50000  |
# | theta[3]  | 0.09366 | 0.03829 | 1.71E-04 | 0.03439  | 0.08842 | 0.1828    | 1001  | 50000  |
# | theta[4]  | 0.1178  | 0.03048 | 1.47E-04 | 0.06595  | 0.115   | 0.1848    | 1001  | 50000  |
# | theta[5]  | 0.6116  | 0.3097  | 0.001409 | 0.1632   | 0.5589  | 1.361     | 1001  | 50000  |
# | theta[6]  | 0.6104  | 0.1366  | 6.45E-04 | 0.3705   | 0.6001  | 0.9058    | 1001  | 50000  |
# | theta[7]  | 0.8686  | 0.6494  | 0.003059 | 0.101    | 0.7124  | 2.537     | 1001  | 50000  |
# | theta[8]  | 0.8692  | 0.6481  | 0.003354 | 0.09784  | 0.7117  | 2.513     | 1001  | 50000  |
# | theta[9]  | 1.478   | 0.6897  | 0.00351  | 0.4705   | 1.367   | 3.128     | 1001  | 50000  |
# | theta[10] | 1.944   | 0.4133  | 0.002022 | 1.223    | 1.916   | 2.83      | 1001  | 50000  |
