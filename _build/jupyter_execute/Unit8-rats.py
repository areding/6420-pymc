#!/usr/bin/env python
# coding: utf-8

# In[1]:


import arviz as az
import numpy as np
import pymc as pm
from pymc.math import dot

get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '--iversions')


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
# We had a previous example about [Dugongs](https://areding.github.io/6420-pymc/Unit6-dugongs.html) that dealt with missing data in the observed data (y values). This example shows how to deal with missing data in the input data (x). It's still pretty easy. You could look at it like creating another likelihood in the model, a very simple one where the observed data is x, and you use a single distribution to fill in the missing values (see ```x_imputed``` in the model below).
# 
# For now I'm leaving the variable names the same as the BUGS example. Might go back and make them more descriptive later.
# 
# There are some differences with my version:
# 
# 1. My gamma priors on tau are more informative. This is because PyMC was having some computational issues with the Gamma(.001, .001) priors the professor used. I don't know if it's because of the sampling algorithm or if it's a problem with the new computational backend. I will look into it more later, for now I just want to get these examples up.
# 
# 2. I imputed the x values with a more informative prior for similar reasons. That Uniform(0, 500) prior seems kind of crazy to me, and I wanted to rule out more computational issues.
# 
# 3. I got rid of the separate definition of the intercept as alpha, it is now beta[0].
# 
# I have not checked this model for any kind of correctness or compared the answers to the BUGS version. It may make no sense at all! But I

# In[2]:


# note that I added a 1 to the first value for x, this is for the intercept beta[0]
x = [1.0, 8.0, 15.0, 22.0, np.nan, 36.0]
y = np.loadtxt("./data/rats.txt")
y.shape


# In[3]:


# create masked data
y = y.copy()
y = np.nan_to_num(y, nan=-1)
y = np.ma.masked_values(y, value=-1)

x = x.copy()
x = np.nan_to_num(x, nan=-1)
x = np.ma.masked_values(x, value=-1)


# In[ ]:


with pm.Model() as m:
    x_data = pm.Data("x_data", x, mutable=True)
    y_data = pm.Data("y_data", y, mutable=False)

    tau_c = pm.Gamma("tau.c", 1, 1)
    beta_c = pm.Normal("beta.c", 0, tau=1e-6)
    beta_tau = pm.Gamma("beta.tau", 1, 1)

    beta = pm.Normal("beta", beta_c, tau=beta_tau, shape=6)

    x_imputed = pm.Normal("x_imputed", mu=20, sigma=10, observed=x_data)

    mu = dot(beta, x_imputed)
    likelihood = pm.Normal("likelihood", mu, tau=tau_c, observed=y_data, shape=5)

    trace = pm.sample(
        10000,
        tune=2000,
        cores=4,
        init="jitter+adapt_diag",
    )


# In[ ]:


az.summary(trace, hdi_prob=0.95)


# In[ ]:




