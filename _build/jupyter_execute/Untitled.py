#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import arviz as az
import pymc3 as pm
import numpy as np
from sklearn.linear_model import LinearRegression
from warnings import filterwarnings

get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


filterwarnings('ignore')


# # A Simple Regression
# 
# From [Codes for Unit 1](https://www2.isye.gatech.edu/isye6420/supporting.html).
# 
# Associated lecture video: [Unit 1 Lesson 4](https://www.youtube.com/watch?v=c9VXDzJGmNw&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=4)
# 
# You don't necessarily need to set inits in PyMC. The default method of generating inits is 'jitter+adapt_diag', which chooses them based on the model and input data while adding some randomness.
# 
# If you do want to set an initial value, pass a dictionary to the start parameter of pm.sample.
# 
# ```python
# inits = {"alpha": np.array(0.),
#          "beta": np.array(0.)}
# 
# trace = pm.sample(2000, start=inits)
# ```
# 

# In[3]:


X = np.array([1, 2, 3, 4, 5])
y = np.array([1, 3, 3, 3, 5])
x_bar = np.mean(X)

with pm.Model() as asr:
  # priors
    alpha = pm.Normal('alpha', sigma=100)
    beta = pm.Normal('beta', sigma=100)

    tau = pm.Gamma('tau', alpha=.001, beta=.001) 
    sigma = 1/pm.math.sqrt(tau) 

    mu = alpha + beta * (X - x_bar)
    likelihood = pm.Normal('likelihood', mu=mu, sd=sigma, observed=y)

    # start sampling
    trace = pm.sample(3000, # samples
                      chains=4,
                      tune=500,
                      init='jitter+adapt_diag',
                      random_seed=1,
                      cores=4, # parallel processing
                     )


# In[6]:


# this will remove the first 500 samples
burned = trace.sel(draw=slice(500, None))


# In[7]:


# this course (arbitrarily) asks for the 95% credible interval or set
# so specify hdi_prob = .95
az.summary(burned, hdi_prob=.95)


# In[8]:


# intercept
# alpha - beta * x.bar
burned.posterior.alpha.mean() - burned.posterior.beta.mean() * x_bar


# In[10]:


get_ipython().run_cell_magic('html', '', '<style>\n  table {margin-left: 0 !important;}\n</style>')


# 
# OpenBugs results are nearly identical:
# 
# |       | mean   | sd     | MC_error | val2.5pc | median | val97.5pc | start | sample |
# |-------|--------|--------|----------|----------|--------|-----------|-------|--------|
# | alpha | 2.995  | 0.5388 | 0.005863 | 1.947    | 3.008  | 4.015     | 1000  | 9001   |
# | beta  | 0.7963 | 0.3669 | 0.003795 | 0.08055  | 0.7936 | 1.526     | 1000  | 9001   |
# | tau   | 1.88   | 1.524  | 0.02414  | 0.1416   | 1.484  | 5.79      | 1000  | 9001   |

# In[11]:


# double-check with sklearn standard linear regression
reg = LinearRegression().fit(X.reshape(-1, 1), y)
reg.intercept_, reg.coef_


# In[ ]:




