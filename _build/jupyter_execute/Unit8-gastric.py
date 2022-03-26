#!/usr/bin/env python
# coding: utf-8

# In[180]:


import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymc as pm
from pymc.math import exp


# # Gastric Cancer Data 
# 
# Adapted from [Codes for Unit 8: gastric.odc](https://www2.isye.gatech.edu/isye6420/supporting.html).
# 
# Associated lecture video: [Unit 8 Lesson 6](https://www.youtube.com/watch?v=t4pHpZxtC0U&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=87).
# 
# Data can be found [here](https://raw.githubusercontent.com/areding/6420-pymc/main/data/gastric.csv).
# 
# Stablein et al. (1981) provide data on 90 patients affected by locally advanced, nonresectable gastric carcinoma. The patients are randomized to two treatments:
# chemotherapy alone (coded as 0) and chemotherapy plus radiation (coded as 1).
# Survival time is reported in days, with censoring indicator (1 = censored, 0 = observed).
# 
# Stablein, D. M., Carter, W. H., Novak, J. W. (1981). Analysis of survival data with nonproportional hazard functions. Control. Clin. Trials,  2 , 2, 149--159. 

# In[14]:


data = pd.read_csv("./data/gastric.csv")


# In[15]:


data


# In[25]:


x = data["type"].to_numpy(copy=True)
censored = data["censor"].to_numpy(copy=True)
y = data["times"].to_numpy(copy=True)
y[np.isnan(y)] = censored[np.isnan(y)]


# In[248]:


x


# In[29]:


censored[censored == 0] = y[censored == 0] + 1


# In[30]:


censored


# In[281]:


y.astype(int)


# In[255]:


np.exp(1.5)**(-1/100)


# ```{warning}
# PyMC and BUGS do not specify the Weibull distribution in the same way!
# ```

# In[279]:


with pm.Model() as m:
    x_data = pm.Data("x_data", x, mutable=True)
    y_data = pm.Data("y_data", y, mutable=False)
    
    beta0 = pm.Normal("beta0", 0, sigma=10)
    beta1 = pm.Normal("beta1", 0, sigma=10)
    α = pm.Exponential("α", 0.01)

    λ = exp(beta0 + beta1 * x_data)
    β = λ ** (-1 / α)

    obs_latent = pm.Weibull("test", alpha=α, beta=β, observed=y_data)
    # likelihood = pm.Censored(
    #    "likelihood", obs_latent, lower=0, upper=censored, observed=y, shape=len(y)
    # )

    trace = pm.sample(1000, init="auto")

az.summary(trace, hdi_prob=0.9)


# In[ ]:





# In[245]:


from tqdm.auto import tqdm

values = []
for _ in tqdm(range(500)):
    beta0 = pm.draw(pm.Normal.dist(0, sigma=10))
    beta1 = pm.draw(pm.Normal.dist(0, sigma=10))
    v = pm.draw(pm.Exponential.dist(0.01))
    x0 = np.random.choice(x)
    λ = np.exp(beta0 + beta1 * x0)

    likelihood = pm.draw(pm.Weibull.dist(v, λ ** -(1 / v)))
    values.append(
        (
            round(float(beta0), 2),
            round(float(beta1), 2),
            round(float(v), 2),
            round(x0, 2),
            round(λ, 2),
            round(float(likelihood), 10),
        )
    )

vals = pd.DataFrame(values, columns=("beta0", "beta1", "v", "x0", "λ", "likelihood"))


# In[246]:


vals.describe()


# In[238]:


vals


# In[280]:


expo = pm.draw(pm.Exponential.dist(0.01), 10000)
plt.plot(expo)


# In[ ]:




