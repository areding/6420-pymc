#!/usr/bin/env python
# coding: utf-8

# In[1]:


import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pymc as pm
from pymc.math import switch, ge


# ```{note}
# This is using PyMC 4.0 beta 4! Syntax should be backwards-compatible except for the imports.
# ```

# # Stress, Diet and Plasma Acids
# 
# Adapted from [Codes for Unit 6: stressacids.odc](https://www2.isye.gatech.edu/isye6420/supporting.html).
# 
# Associated lecture video: [Unit 6 Lesson 5](https://www.youtube.com/watch?v=xomK4tcePmc&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=56).
# 
# In the study [Interrelationships Between Stress, Dietary Intake, and Plasma Ascorbic Acid During Pregnancy](https://vtechworks.lib.vt.edu/handle/10919/74486) conducted at the Virginia Polytechnic Institute and State University, the plasma ascorbic acid levels of pregnant women were compared for smokers versus non-smokers. Thirty-two women in the last three months of pregnancy, free of major health disorders, and ranging in age from 15 to 32 years were selected for the study. Prior to the collection of 20 ml of blood, the participants were told to avoid breakfast, forego their vitamin supplements, and avoid foods high in ascorbic acid content. From the blood samples, the plasma ascorbic acid values of each subject were determined in milligrams per 100 milliliters.
# 
# ---

# The purpose of this example in lectures was mostly just to show different ways to load data in BUGS. I'm not going to go into that too much, just want to get this example up just in case it's useful. In the next cell, I start with the data formatted the same way as in ```stressacids.odc```, and use list comprehensions to create two lists, one of smokers and one of non-smokers.

# In[2]:


# fmt: off
plasma = [0.97, 0.72, 1.00, 0.81, 0.62, 1.32, 1.24, 0.99, 0.90, 0.74,
          0.88, 0.94, 1.06, 0.86, 0.85, 0.58, 0.57, 0.64, 0.98, 1.09,
          0.92, 0.78, 1.24, 1.18, 0.48, 0.71, 0.98, 0.68, 1.18, 1.36,
          0.78, 1.64]
smo = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
       1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]
# fmt: on

nonsmokers = [x for x, y in zip(plasma, smo) if y == 1]
smokers = [x for x, y in zip(plasma, smo) if y == 2]


# ## BUGS step function
# 
# I think this is the first time we've seen the BUGS step function.
# 
# BUGS defines the step function like this:
# 
# ```step(e)``` is 1 if e >= 0; 0 otherwise.
# 
# Keep in mind that in PyMC, step functions are how they refer to the algorithms used for sampling, as in NUTS or Metropolis. Just different terminology.
# 
# We can recreate the BUGS step function with ```pm.math.switch()```:
# 
# ```
# pm.math.switch(e >= 0, 1, 0)
# 
# ```
# 
# We should also probably use pm.math.ge for greater than or equal, as well, so:
# 
# ```
# pm.math.switch(ge(e,0), 1, 0)
# 
# ```

# ## How do I track non-random variables in PyMC?
# 
# One nice thing about BUGS is you can easily track both deterministic and non-deterministic variables while sampling. For PyMC, you can wrap these in [```pm.Deterministic()```](https://docs.pymc.io/en/v3/api/model.html). Just make sure to use [```pm.math```](https://docs.pymc.io/en/v3/api/math.html) functions where possible.

# In[3]:


with pm.Model() as m:
    # priors
    tau_nonsmokers = pm.Gamma("tau_nonsmokers", alpha=0.0001, beta=0.0001)
    sigma_nonsmokers = 1 / pm.math.sqrt(tau_nonsmokers)
    mu_nonsmokers = pm.Normal("mu_nonsmokers", mu=0, sigma=100)

    tau_smokers = pm.Gamma("tau_smokers", alpha=0.0001, beta=0.0001)
    sigma_smokers = 1 / pm.math.sqrt(tau_smokers)
    mu_smokers = pm.Normal("mu_smokers", mu=0, sigma=100)

    # likelihood
    plasma_aa_ns = pm.Normal(
        "nonsmokers_aa", mu=mu_nonsmokers, sd=sigma_nonsmokers, observed=nonsmokers
    )
    plasma_aa_s = pm.Normal(
        "smokers_aa", mu=mu_smokers, sd=sigma_smokers, observed=smokers
    )
    
    testmu = pm.Deterministic("test_mu", switch(ge(mu_smokers, mu_nonsmokers), 1, 0))
    r = pm.Deterministic("prec_ratio", tau_nonsmokers/tau_smokers)
    
    # start sampling
    trace = pm.sample(
        5000,
        chains=4,
        tune=1000,
        cores=4,
        init="jitter+adapt_diag",
        random_seed=1,
        return_inferencedata=True,
    )


# In[4]:


az.summary(trace, hdi_prob=0.95)


# In[ ]:




