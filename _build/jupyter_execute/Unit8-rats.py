#!/usr/bin/env python
# coding: utf-8

# In[12]:


import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pymc as pm


# # Rats 
# 
# I'm just going to do ratsignorable2.odc for now since it is relevant for HW6. Eventually I'll add the other examples.
# 
# Adapted from [Codes for Unit 8: ratsignorable2.odc](https://www2.isye.gatech.edu/isye6420/supporting.html).
# 
# Associated lecture video: [Unit 8 Lesson 2](https://www.youtube.com/watch?v=T5vkLsIs3f8&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=83).
# 
# Data can be found [here](https://raw.githubusercontent.com/areding/6420-pymc/main/data/rats.txt).
# 
# 
# We had a previous example about [Dugongs](https://areding.github.io/6420-pymc/Unit6-dugongs.html) that dealt with missing data in the observed data (y values). This example shows how to deal with missing data in the input data (x).
# 
# For now I'm leaving the variable names the same as the BUGS example. Might go back and make them more descriptive later.

# In[16]:


T = 5
x = [8.0, 15.0, 22.0, np.nan, 36.0]
y = np.loadtxt("./data/rats.txt")
data.shape


# In[17]:


# create masked data
y = y.copy()
y = np.nan_to_num(y, nan=-1)
y = np.ma.masked_values(y, value=-1)

x = x.copy()
x = np.nan_to_num(x, nan=-1)
x = np.ma.masked_values(x, value=-1)


# In[14]:


with pm.Model() as m:
    x_data = pm.Data("x_data", x, mutable=True)
    y_data = pm.Data("y_data", y, mutable=False)
    
    tau_c = pm.Gamma("tau.c", 0.001, 0.001)
    alpha_c = pm.Normal("alpha.c", 0, tau=1e-6)
    alpha_tau = pm.Gamma("alpha.tau", 0.001, 0.001)
    beta_c = pm.Normal("beta.c", 0, tau=1e-6)
    beta_tau = pm.Gamma("beta.tau", .001, .001)
    
    alpha = pm.Normal("alpha", alpha_c, tau=alpha_tau, shape=?)
    beta = pm.Normal("beta", beta_c, tau=beta_tau, shape or size or whatever)
    
    mu = alpha + beta * x_data
    likelihood = pm.Normal("likelihood", mu, tau=tau_c, observed=y_data)
    
    trace = pm.sample(
        2000,
        chains=4,
        tune=500,
        cores=4,
        init="adapt_diag",
        random_seed=1,
        return_inferencedata=True,
        initvals=inits
    )

az.summary(trace, hdi_prob=.95)


# In[ ]:




