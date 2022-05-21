#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pymc as pm

get_ipython().run_line_magic('load_ext', 'watermark')


# In[ ]:


get_ipython().run_line_magic('watermark', '--iversions')


# # Bartholomew (1957) for Type I censoring
# 
# Adapted from [Codes for Unit 6: exponential1.odc](https://www2.isye.gatech.edu/isye6420/supporting.html).
# 
# Associated lecture videos: [Unit 6 Lesson 9](https://www.youtube.com/watch?v=6gKnM6vL8Po&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=60).
# 
# Dataset and table from: [A Problem in Life Testing (Bartholemew 1957)](https://www.jstor.org/stable/2280905?seq=1#metadata_info_tab_contents).
# 
# ## Results of a life test on ten pieces of equipment
# |Item No.|1|2|3|4|5|6|7|8|9|10|
# |-|-|-|-|-|-|-|-|-|-|-|
# |Date of installation|11 June|21 June|22 June|2 July|21 July|31 July|31 July|1 Aug.|2 Aug.|10 Aug.|
# |Date of Failure|13 June| - | 12 Aug.| - |23 Aug.|27 Aug.|14 Aug.|25 Aug.|6 Aug.| - |
# |Life in Days|2|(119)|51|(77)|33|27|14|24|4|(37)|
# |No. Days to End of Period|81|72|70|60|41|31|31|30|29|21|
# 
# The observations above are the result of a test on the lifespan of some piece of equipment. The test had to end on August 31, but items 2, 4, and 10 did not fail by that date (the values in parentheses are the eventual lifespans of those pieces of equipment, but they were not known on August 31). So all we know for the purposes of the experiment is that they worked for 72, 60, and 21 days, respectively, and that they will continue working for some unknown additional time period.
# 
# The goal of the experiment is to provide a lifespan estimate. We could:
# 
# 1. Take the censored data as observed:
#     - Divide the total observed working time (308 days) and divide by the equipment count (10) to get an average lifetime of 308 for an estimate of 30.8 days.
#     - Problem: underestimates actual average lifespan.
# 
# 2. Ignore the equipment that didn't fail:
#     - Take mean lifetime of the pieces of equipment that broke within the experiment period for an estimate of 22.1 days.
#     - Problems: selection bias, underestimates even more.
# 
# 3. Use the classical method:
#     - Maximum Likelihood Estimation (MLE) under an exponential model. Total observed lifetime divided by 7 (number of observed failures) for an estimate of 44.0 days.
#     - Problem: small sample size.
# 
# The actual mean lifespan of all pieces of equipment was 38.8 days.
# 
# ## Bayesian approach
# What we need to do is called Type-1 censoring. We will right-censor the three machines that still hadn't failed by August 31, following [this example](https://docs.pymc.io/projects/examples/en/latest/generalized_linear_models/GLM-truncated-censored-regression.html#censored-regression-model).
# 
# ```{note}
# This is using PyMC 4.0 beta 3!
# ```

# In[6]:


# gamma dist parameters
α = 0.01
β = 0.1

# max possible observed life for each piece of equipment (before end of experiment)
censored = (81, 72, 70, 60, 41, 31, 31, 30, 29, 21)

# observed life within experiment dates
y = (2, 72, 51, 60, 33, 27, 14, 24, 4, 21)


with pm.Model() as m:
    λ = pm.Gamma("λ", α, β)
    μ = pm.Deterministic("μ", 1 / λ)
    obs_latent = pm.Exponential.dist(λ)

    observed = pm.Censored(
        "observed", obs_latent, lower=None, upper=censored, observed=y, shape=len(y)
    )

    trace = pm.sample(
        100000,
        chains=4,
        tune=10000,
        cores=4,
        init="jitter+adapt_diag",
        random_seed=1,
        return_inferencedata=True,
    )


# In[7]:


az.summary(trace, hdi_prob=0.95)


# BUGS results:
# 
# |               |            mean | sd     | MC_error | val2.5pc | median  | val97.5pc | start | sample |
# |---------------|-----------------|--------|----------|----------|---------|-----------|-------|--------|
# | lambda        | 0.02281         | 0.0086 | 3.66E-05 | 0.009229 | 0.02169 | 0.04248   | 1001  | 100000 |
# | mu            | 51.07           | 22.61  | 0.1018   | 23.54    | 46.09   | 108.4     | 1001  | 100000 |
# | observed[2]   | 122.8           | 60.45  | 0.2442   | 73.12    | 103.5   | 284.5     | 1001  | 100000 |
# | observed[4]   | 110.8           | 59.93  | 0.2145   | 61.09    | 91.81   | 269.8     | 1001  | 100000 |
# | observed[10]  | 72.01           | 60.28  | 0.2155   | 22.13    | 52.89   | 232.6     | 1001  | 100000 |
# 
# Okay, these results are pretty close. We end up with $1/.023=43.5$ days, compared to $43.8$ days for BUGS. But we're missing the imputed values for each censored observation. I don't see an easy way to do that in PyMC right now, but I will circle back to this eventually.

# In[ ]:




