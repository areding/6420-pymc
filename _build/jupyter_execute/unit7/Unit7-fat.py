#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pymc as pm
import pandas as pd
import numpy as np
import arviz as az


# # Brozek index prediction
# ## Simple linear regression with Bayesian $R^2$
# 
# Adapted from [Codes for Unit 7: fat2d.odc, fatmulti.odc](https://www2.isye.gatech.edu/isye6420/supporting.html). The first lecture uses fat1.odc, but that file wasn't provided. You can see the code in the Lesson 11 video, though. It just uses the X8 predictor.
# 
# Associated lecture videos: [Unit 7 Lesson 11](https://www.youtube.com/watch?v=yAix2H4V0_c&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=73) and [Lesson 13](https://www.youtube.com/watch?v=3YhloEC_LTE&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=75).
# 
# Data can be found [here](https://raw.githubusercontent.com/areding/6420-pymc/main/data/fat.tsv).
# 
# Percentage of body fat, age, weight, height, and ten body circumference measurements (e.g., abdomen) were recorded for 252 men. Percentage of body fat is estimated through an underwater weighing technique.
# 
# The data set has 252 observations and 15 variables. Brozek index (Brozek et al., 1963) is obtained by the underwater weighing while other 14 anthropometric variables are obtained using scales and a measuring tape.
# 
# - y = Brozek index
# - X1 = 1 (intercept)
# - X2 = age
# - X3 = weight
# - X4 = height
# - X5 = adipose
# - X6 = neck  
# - X7 = chest
# - X8 = abdomen
# - X9 = hip
# - X10 = thigh
# - X11 = knee   
# - X12 = ankle
# - X13 = bicep
# - X14 = forearm
# - X15 = wrist
# 
# These anthropometric variables are less intrusive but also less reliable in assessing the body fat index.
# 
# Set a linear regression to predict the Brozek index from these body measurements.

# ```{note}
# What "Bayesian R2" is could really use some more explanation. There's no one agreed-upon definition that I can find
# 
# ```

# ## Single predictor (X8)
# 
# This is a recreation of fat1.odc.

# In[17]:


data = pd.read_csv("data/fat.tsv", sep="\t")

y = data["y"].to_numpy(copy=True)
X = data["X8"].to_numpy(copy=True)

# p will be the number of predictors + intercept (1 + 1 in this case)
n, p = X.shape[0], 2


# In[18]:


with pm.Model() as m:
    tau = pm.Gamma("tau", .001, .001)
    beta0 = pm.Normal("beta0_intercept", 0, tau=.001)
    beta1 = pm.Normal("beta1_abdomen", 0, tau=.001)
    variance = pm.Deterministic("variance", 1/tau)
    
    mu = beta0 + beta1 * X
    likelihood = pm.Normal("likelihood", mu=mu, tau=tau, observed=y)
    
    # Bayesian R2 from fat1.odc
    sse = (n - p) * variance
    cy = y - y.mean()
    sst = pm.math.dot(cy, cy)
    br2 = pm.Deterministic("br2", 1 - sse/sst)
    
    trace = pm.sample(2000)
    ppc = pm.sample_posterior_predictive(trace)


# In[22]:


az.summary(trace, hdi_prob=.95)


# This matches the results from the U7 L11 video.
# 
# Another way to calculate the $R^2$ using a posterior predictive check (keeping in mind that there is no standard "Bayesian $R^2$") and the results will be slightly different:

# In[44]:


# get the mean y_pred across all chains
y_pred = np.array(ppc.posterior_predictive.likelihood.mean(axis=(0, 1)))

az.r2_score(y, y_pred)


# In this case they agree, but that won't always be true.

# ## All predictors
# 
# Based on fat2d.odc. No time to finish this right now, sorry.

# In[ ]:


data = pd.read_csv("../data/fat.tsv", sep="\t")

y = data["y"].to_numpy(copy=True)
X = data.iloc[:, 1:].to_numpy(copy=True)
# add intercept
X_aug = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)

n, p = X_aug.shape
# Zellner's g (constant, p^2)
g = p**2

