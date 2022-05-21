#!/usr/bin/env python
# coding: utf-8

# In[9]:


import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pymc3 as pm
from pymc3.math import log, sqr


# # Jeremy with Zero Tricks
# 
# Adapted from [Codes for Unit 6: zerotrickjeremy.odc](https://www2.isye.gatech.edu/isye6420/supporting.html).
# 
# Associated lecture video: [Unit 6 Lesson 10](https://www.youtube.com/watch?v=wilCD0fSv20&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=61).
# 
# There's a running example in the lectures about Jeremy testing his IQ. At some point I will track all those down and add links here, but for now I'm just going to port the code.
# 
# I'm not sure what's going on when the professor sets ```z1``` as both a deterministic and random variable. I'll need to test some things out in BUGS once the Citrix virtual machines are back online. For now, here's a first pass at recreating the model, where I interpret the ```z <- 0``` as feeding an observation of zero to the variable.
# 
# That said, I don't think we will ever need to use the zeros or ones tricks in the homeworks. If we do I will definitely expand this page.
# 
# I played around with using Greek letters as variable names for this example. Not sure if I'll continue doing so, but it's really easy in Jupyter Lab. Just type \theta and hit TAB in a code cell.

# In[46]:


y = 98
μ = 110
σ = 8.944272
τ = 10.954451
constant = 1000 # can't let lambda be lower than zero

inits = {"θ": 100}


# In[53]:


with pm.Model() as m:
    θ = pm.Flat("θ")

    λ1 = pm.Deterministic("λ1", log(σ) + 0.5 * sqr(((y - θ) / σ)) + constant)
    λ2 = pm.Deterministic("λ2", log(τ) + 0.5 * sqr(((θ - μ) / τ)) + constant)

    z1 = pm.Poisson("z1", λ1, observed=0)
    z2 = pm.Poisson("z2", λ2, observed=0)

    trace = pm.sample(
        10000,
        chains=4,
        cores=4,
        tune=1000,
        init="jitter+adapt_diag",
        random_seed=1,
        return_inferencedata=True,
        start=inits,
    )


# In[54]:


az.summary(trace, hdi_prob=0.95)


# Again, it's not clear to me what BUGS is doing, but these PyMC results are almost exactly the same as the professor's results so this must be close. I have also tried passing vectors of zeros to each ```z```, putting more weight on the zero "observations." This ended up reducing the credible interval and standard deviation of theta. 
# 
# I found [this page](http://www.medicine.mcgill.ca/epidemiology/Joseph/courses/common/Tricks.html) that briefly mentions the same trick. They note that "... this method can be very inefficient and give a very high MC error."
# 
# 

# In[ ]:




