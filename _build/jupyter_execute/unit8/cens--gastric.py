#!/usr/bin/env python
# coding: utf-8

# In[1]:


import arviz as az
import numpy as np
import pymc as pm
from pymc.math import exp

np.set_printoptions(suppress=True)


# # Gastric cancer example
# 
# Adapted from code for [unit 8: gastric.odc](https://raw.githubusercontent.com/areding/6420-pymc/main/original_examples/Codes4Unit8/gastric.odc).
# 
# Data can be found [here](https://raw.githubusercontent.com/areding/6420-pymc/main/data/gastric.txt).
# 
# ## Associated lecture video: Unit 8, Lesson 6

# In[2]:


get_ipython().run_cell_magic('html', '', '<iframe width="560" height="315" src="https://www.youtube.com/embed?v=t4pHpZxtC0U&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=87" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>')


# ## Problem statement
# Stablein et al. (1981) provide data on 90 patients affected by locally advanced, nonresectable gastric carcinoma. The patients are randomized to two treatments: chemotherapy alone (coded as 0) and chemotherapy plus radiation (coded as 1). Survival time is reported in days. Recorded times are censored if the patient stopped participating in the study before it finished.
# 
# Stablein, D. M., Carter, W. H., Novak, J. W. (1981). Analysis of survival data with nonproportional hazard functions. Control. Clin. Trials,  2 , 2, 149--159.
# 
# ### Data
# Columns are, from left to right:
# - type: Treatment type, chemotherapy (0) or chemotherapy + radiation (1)
# - censored: If censored, meaning the patient survived the observation period, the time in days appears here rather than in the times column. 0 if not censored.
# - times: Recorded days without cancer recurrence. NaN if censored.
# 
# ### Model changes
# I didn't implement S, f, or h from the original model. They should be simple enough, but I really just wanted to get another example of censoring up before HW6. I will add those later.
# 
# PyMC really did not like the noninformative exponential prior on v (α in this model). To avoid the divide by zero errors, I just kept increasing lambda until the model ran all the way through. This is not ideal, but I haven't had time to look into it further. The results actually came out fairly close to the BUGS results.
# 

# ## Method 1: ```pm.Censored```
# 
# The way PyMC censoring works is described in some detail in [this notebook](https://docs.pymc.io/projects/examples/en/latest/generalized_linear_models/GLM-truncated-censored-regression.html#censored-regression-model) by [Dr. Benjamin T. Vincent](https://github.com/drbenvincent). This is accomplished in the source code [here](https://github.com/aesara-devs/aeppl/blob/751979802f1aef5478fdbf7cc1839df07df60825/aeppl/truncation.py#L79) if you want to take a look. For right-censoring, try this: ```pm.Censored("name", dist, lower=None, upper=censored, observed=y)```. The censored values can be an array of the same shape as the y values. 
# 
# If the y value equals the right-censored value, [```pm.Censored```](https://docs.pymc.io/en/latest/api/distributions/generated/pymc.Censored.html#pymc.Censored) returns the complement to the CDF evaluated at the censored value. If the y value is greater than the censored value, it returns ```-np.inf```. Otherwise, the distribution you passed to the ```dist``` parameter works as normal. What I've been doing is setting the values in the censored array to ```np.inf``` if the corresponding y value is not censored, and equal to the y value if it should be censored.
# 
# ```{note}
# I've noticed that this method is unstable with some distributions. Try using the imputed censoring model (below) if this one isn't working.
# ```

# In[2]:


data = np.loadtxt("./data/gastric.txt")
data.shape


# In[3]:


x = data[:, 0].copy()
censored = data[:, 1].copy()
y = data[:, 2].copy()
# for pymc, right-censored values must be greater than or equal to than the "upper" value
y[np.isnan(y)] = censored[np.isnan(y)]
censored[censored == 0] = np.inf


# In[4]:


y


# In[5]:


censored


# ```{warning}
# PyMC and BUGS do not specify the Weibull distribution in the same way!
# 
# α = v
# 
# β = λ ** (-1 / α)
# 
# ```

# In[6]:


log2 = np.log(2)

with pm.Model() as m:
    beta0 = pm.Normal("beta0", 0, tau=0.0001)
    beta1 = pm.Normal("beta1", 0, tau=0.0001)
    α = pm.Exponential("α", 3)

    λ = exp(beta0 + beta1 * x)
    β = λ ** (-1 / α)

    obs_latent = pm.Weibull.dist(alpha=α, beta=β)
    likelihood = pm.Censored(
        "likelihood",
        obs_latent,
        lower=None,
        upper=censored,
        observed=y,
    )

    median0 = pm.Deterministic("median0", (log2 * exp(-beta0)) ** (1 / α))
    median1 = pm.Deterministic("median1", (log2 * exp(-beta0 - beta1)) ** (1 / α))

    trace = pm.sample(
        10000, tune=2000, cores=4, init="auto", step=[pm.NUTS(target_accept=0.9)]
    )


# In[7]:


az.summary(trace, hdi_prob=0.9)


# ## Method 2: Imputed Censoring
# 
# This method is from [this notebook](https://docs.pymc.io/projects/examples/en/latest/survival_analysis/censored_data.html#censored-data-model1) by [Luis Mario Domenzain](https://github.com/domenzain), [George Ho](https://github.com/eigenfoo), and [Dr. Ben Vincent](https://github.com/drbenvincent). This method imputes the values using what is almost another likelihood (not sure if it actually meets the definition of one, so I'm calling the variable ```impute_censored```) in the model, with the right-censored values as lower bounds. Since the two likelihoods share the same priors, this ends up working nearly as well as the previous method. Better, in the case of homework 6 question 2, since the previous method doesn't seem to work for the required model at all. This method will work for the homework, albeit more slowly and with some extra warnings.

# In[8]:


data = np.loadtxt("./data/gastric.txt")
x = data[:, 0].copy()
censored_vals = data[:, 1].copy()
y = data[:, 2].copy()

# we need to separate the observed values and the censored values
observed_mask = censored_vals == 0

censored = censored_vals[~observed_mask]
y_uncensored = y[observed_mask]
x_censored = x[~observed_mask]
x_uncensored = x[observed_mask]


# In[9]:


log2 = np.log(2)

with pm.Model() as m:
    beta0 = pm.Normal("beta0", 0, tau=0.0001)
    beta1 = pm.Normal("beta1", 0, tau=0.0001)
    α = pm.Exponential("α", 3)

    λ_censored = exp(beta0 + beta1 * x_censored)
    β_censored = λ_censored ** (-1 / α)

    λ_uncensored = exp(beta0 + beta1 * x_uncensored)
    β_uncensored = λ_uncensored ** (-1 / α)

    impute_censored = pm.Bound(
        "impute_censored",
        pm.Weibull.dist(alpha=α, beta=β_censored),
        lower=censored,
        shape=censored.shape[0],
    )

    likelihood = pm.Weibull(
        "likelihood",
        alpha=α,
        beta=β_uncensored,
        observed=y_uncensored,
        shape=y_uncensored.shape[0],
    )

    median0 = pm.Deterministic("median0", (log2 * exp(-beta0)) ** (1 / α))
    median1 = pm.Deterministic("median1", (log2 * exp(-beta0 - beta1)) ** (1 / α))

    trace = pm.sample(
        10000, tune=2000, cores=4, init="auto", step=[pm.NUTS(target_accept=0.95)]
    )


# In[10]:


az.summary(trace, hdi_prob=0.9)


# In[ ]:




