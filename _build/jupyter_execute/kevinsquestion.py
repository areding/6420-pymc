#!/usr/bin/env python
# coding: utf-8

# Kevin's question:
# 
# I was working through some practice applications at work, and I ran into this issue.
# 
# What if there's no overlap of the prior and likelihood? (I.e. likelihood is zero in the domain of the prior and vice versa)
# 
# Would you just observe the resulting zero posterior and try again with a wider prior? 
# 
# I came into this class thinking that the likelihood shifted the prior density, which is kinda true, but not if they don't overlap in theta space. Am I missing something?
# 
# 

# Want to try inventing weird situations where the likelihood, prior, and data don't overlap at all.
# 
# Todo:
# - Try sampling from improper posterior. 
# - Try creating a bimodal posterior. 
# - Try creating a flat posterior.
# - Can you actually create a posterior around zero?

# In[1]:


import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pymc3 as pm


# In[ ]:


# invent some data

with pm.Model() as model:
    # priors
    alpha = pm.Normal("alpha", sigma=1)
    beta = pm.Normal("beta", sigma=1)
    # using precision for direct comparison with BUGS output
    sigma = pm.Normal("sigma", mu=0, sigma=1)

    mu = alpha + beta * X
    likelihood = pm.Normal("likelihood", mu=mu, sd=sigma, observed=y)

    # start sampling
    trace = pm.sample(
        3000,  # samples
        chains=4,
        tune=500,
        init="jitter+adapt_diag",
        random_seed=1,
        cores=4,  # parallel processing of chains
        return_inferencedata=True,  # return arviz inferencedata object
    )

