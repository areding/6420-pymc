#!/usr/bin/env python
# coding: utf-8

# In[1]:


import arviz as az
import numpy as np
import pandas as pd
import pymc as pm

get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '--iversions')


# # ANOVA Coagulation
# 
# Adapted from [Codes for Unit 7: anovacoagulation.odc](https://www2.isye.gatech.edu/isye6420/supporting.html).
# 
# Associated lecture video: [Unit 7 Lesson 7](https://www.youtube.com/watch?v=C1PGMZ147wA&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=69).
# 
# Here 24 animals (Box, Hunter, Hunter; Statistics for Experimenters, p. 166) are randomly allocated to 4 different diets,  but the numbers allocated to different diets  are not the same. The coagulation time for blood\ is measured for each animal. Are the diet-based differences significant?
# 

# In[9]:


# fmt: off
times = (62, 60, 63, 59, 63, 67, 71, 64, 65, 66, 68, 66, 71, 67, 68, 68, 56, 62, 60, 61, 63, 64, 63, 59)
diets = (1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4)
# fmt: on

times_by_diet = {}
for diet_code in set(diets):
    time_sep = [time for time, diet in zip(times, diets) if diet == diet_code]
    times_by_diet[diet_code] = time_sep

times_by_diet


# In[ ]:


model{
for (i in 1:ntotal){
times[i] ~ dnorm( mu[i], tau )
mu[i] <-  mu0 + alpha[diets[i]] 
}
#alpha[1] <- 0.0;     #CR constraints 
alpha[1] <- -sum( alpha[2:a] ); #STZ Constraint

mu0 ~ dnorm(0, 0.0001)
alpha[2] ~ dnorm(0, 0.0001)
alpha[3] ~ dnorm(0, 0.0001)
alpha[4] ~ dnorm(0, 0.0001)
tau ~ dgamma(0.001, 0.001)
sigma <- sqrt(1/tau)
#pairwise
  for(i in 1:3){
    for(j in i+1:4){
    adiff[i,j] <- alpha[i]-alpha[j]
    }
  }
}


# In[15]:


with pm.Model() as m:
    μ0 = pm.Normal("μ0", 0, tau=.0001)
    τ = pm.Gamma("τ", .001, .001)
    
    alphas = pm.Normal("alphas", 0, tau=.0001, shape=3)
    stz = -pm.math.sum(alphas, axis=1)
    
    α = pm.math.concatenate([stz, alphas])
    
    μ = μ0 + α
    
    likelihood = pm.Normal("likelihood", μ, tau=τ, observed=times)
    
    pairwise_diff = pm.Deterministic("pairwise_diff", α.flatten().reshape((-1, 1)) - α.flatten())
    
    trace = pm.sample(
        5000,
        chains=4,
        tune=2000,
        cores=4,
        init="jitter+adapt_diag",
        random_seed=1,
        return_inferencedata=True,
    )


# In[ ]:




