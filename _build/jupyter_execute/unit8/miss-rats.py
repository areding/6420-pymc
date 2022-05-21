#!/usr/bin/env python
# coding: utf-8

# In[20]:


import arviz as az
import numpy as np
import pymc as pm
from pymc.math import dot, stack, concatenate

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
# ```{warning}
# This version of the model is not running!
# 
# I'm having trouble figuring out how to translate the professor's model into PyMC. If anyone gets it working, let me know. That said, the imputation parts are correct, the important thing is creating the masked data arrays and then choosing a good prior for x_imputed.
# ```
# 
# I hope it gives you an idea for how to handle the missing data question on HW6, which I have confirmed works well in PyMC.
# 
# Original paper [here.](https://www.jstor.org/stable/pdf/2289594.pdf)

# In[101]:


# trying to figure out how to get the shapes to work recreating ratsignoreable1.odc
# it looks like there are 30 alphas and taus in his model! 
x = np.array([1.0, 8.0, 15.0, 22.0, np.nan, 36.0]).reshape(-1, 1)
y = np.loadtxt("./data/rats.txt")


# In[102]:


# create masked data
y = y.copy()
y = np.nan_to_num(y, nan=-1)
y = np.ma.masked_values(y, value=-1)

x = x.copy()
x = np.nan_to_num(x, nan=-1)
x = np.ma.masked_values(x, value=-1)

y.shape, x.shape


# In[100]:


with pm.Model() as m:
    alpha_c = pm.Normal("alpha_c", 0, tau=1e-6)
    alpha_tau = pm.Gamma("alpha_tau", .001, .001)
    beta_c = pm.Normal("beta.c", 0, tau=1e-6)
    beta_tau = pm.Gamma("beta_tau", .001, .001)

    alpha = pm.Normal("alpha", alpha_c, tau=alpha_tau, shape=(30,1))
    beta = pm.Normal("beta", beta_c, tau=beta_tau, shape=(30,1))
    likelihood_tau = pm.Gamma("likelihood_tau", .001, .001)

    # This line is important for the homework!
    x_imputed = pm.TruncatedNormal("x_imputed", mu=20, sigma=10, lower=0, observed=x)

    #coef = concatenate([alpha, beta], axis=0)

    #mu = dot(coef, x_imputed)

    likelihood = pm.Normal("likelihood", mu, tau=likelihood_tau, observed=y, shape=y.shape)

    trace = pm.sample(
        5000,
        tune=1000,
        cores=4,
    )

    ppc = pm.sample_posterior_predictive(trace)


# In[ ]:


az.summary(trace, hdi_prob=0.95)


# Notes:
# 
# - Pretty sure it's mostly a shape problem. Need to take some time and do this by hand to confirm.
# 
# - can't impute data with pm.Data(mutable=True)? 
# 
#     - reading: https://github.com/pymc-devs/pymc/issues/4441 https://github.com/pymc-devs/pymc/pull/5295
# 

# In[ ]:




