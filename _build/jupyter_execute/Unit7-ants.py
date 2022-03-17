#!/usr/bin/env python
# coding: utf-8

# In[15]:


import arviz as az
import numpy as np
import pymc as pm
from pymc.math import exp
import pandas as pd
get_ipython().run_line_magic('load_ext', 'watermark')


# # Ants
# 
# Adapted from [Codes for Unit 7: ants.odc](https://www2.isye.gatech.edu/isye6420/supporting.html).
# 
# Associated lecture video: [Unit 7 Lesson 15](https://www.youtube.com/watch?v=999v5stS8jw&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=77).
# 
# Data can be found [here](https://raw.githubusercontent.com/areding/6420-pymc/main/data/ants.csv).
# 
# 
# The data discussed in Gotelli and Ellison (2002) provide the ant species richness (number of ant species) found in 64-square-meter sampling grids in 22 forests (coded as 1) and 22 bogs (coded as 2) surrounding the forests in  Connecticut, Massachusetts, and Vermont. The sites span 3Ê• of latitude in New England. There are 44 observations on four variables (columns in data set): 
# 
# - Ants: number of species, 
# - Habitat: forests (1) and bogs (2), 
# - Latitude
# - Elevation: in meters above sea level.
# 
# (a) Using Poisson regression, model the number of ant species (Ants) with covariates Habitat and Elevation.  
# (b) For a sampling grid unit located in a forest at the elevation of 100 m how many species the model from (a) predicts? For the model coefficients and the prediction report 95% credible  sets.
# 
# -----------------------
# 
# Just going to throw this up real quick because it's relevant to homework 5! Will add more in the future. Note that I've switched to PyMC 4 beta 3 here.

# In[16]:


get_ipython().run_line_magic('watermark', '--iversions')


# In[2]:


data = pd.read_csv("./data/ants.csv")
data.info()


# In[12]:


with pm.Model() as m:
    ant_species = pm.Data("ant_species", data["ants"].to_numpy(), mutable=False)
    habitat = pm.Data("habitat", data["habitat"].to_numpy(), mutable=True)
    elevation = pm.Data("elevation", data["elevation"].to_numpy(), mutable=True)
    
    beta0 = pm.Normal("beta0_intercept", mu=0, tau=.0001)
    beta1 = pm.Normal("beta1_habitat", mu=0, tau=.0001)
    beta2 = pm.Normal("beta2_elevation", mu=0, tau=.0001)

    μ = exp(beta0 + beta1 * habitat + beta2 * elevation)
            
    y = pm.Poisson("y", mu=μ, observed=ant_species)
    
    trace = pm.sample(
        5000,
        chains=4,
        tune=2000,
        cores=4,
        init="jitter+adapt_diag",
        random_seed=1,
        return_inferencedata=True,
    )


# In[13]:


az.summary(trace)


# In[14]:


with m:
    pm.set_data({"habitat": [1], "elevation": [100]})
    ppc = pm.sample_posterior_predictive(trace)

az.summary(ppc)


# In[ ]:




