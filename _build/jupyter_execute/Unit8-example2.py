#!/usr/bin/env python
# coding: utf-8

# In[1]:


import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymc as pm
from pymc.math import exp


# In[ ]:





# In[19]:


censored = np.array([np.inf, np.inf, 1, np.inf, 3])
y = np.array([2, 3, 1, 2.5, 3])


# In[20]:


with pm.Model() as m:
    λ = pm.Gamma("λ", 2, 3)
    α = 1.5
    β = λ ** (-1 / α)
    obs_latent = pm.Weibull.dist(α, β)
    likelihood = pm.Censored(
        "likelihood", obs_latent, lower=None, upper=censored, observed=y
    )

    trace = pm.sample(1000)

az.summary(trace)


# In[ ]:




