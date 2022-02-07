#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pymc3 as pm
import arviz as az
import matplotlib.pyplot as plt


# # Dugongs: Dealing with Missing Data
# 
# Adapted from [Codes for Unit 6: dugongsmissing.odc](https://www2.isye.gatech.edu/isye6420/supporting.html).
# 
# Associated lecture video: [Unit 6 Lesson 6](https://www.youtube.com/watch?v=dZly6DDPViE&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=57).
# 
# Carlin and Gelfand (1991) investigated the age (x) and length (y) of 27 captured dugongs (sea cows). Estimate parameters in a nonlinear growth model.
# 
# Data provided by Ratkowsky (1983).
# 
# Carlin, B. and Gelfand, B. (1991). An Iterative Monte Carlo Method for 
# Nonconjugate Bayesian Analysis, Statistics and Computing, 1, (2), 119†128.
# 
# Ratkowsky, D. (1983). Nonlinear regression modeling: A unified practical approach. M. Dekker, NY, viii, 276 p.
# 
# 

# In[2]:


X = [1.0, 1.5, 1.5, 1.5, 2.5, 4.0, 5.0, 5.0, 7.0, 8.0, 8.5, 9.0, 9.5, 
     9.5, 10.0, 12.0, 12.0, 13.0, 13.0, 14.5, 15.5, 15.5, 16.5, 17.0,
     22.5, 29.0, 31.5]
y = [1.80, 1.85, 1.87, -1, 2.02, 2.27, 2.15, 2.26, 2.47, 2.19, 2.26,
     2.40, 2.39, 2.41, 2.50, 2.32, 2.32, 2.43, 2.47, 2.56, 2.65, 2.47,
     2.64, 2.56, 2.70, 2.72, -1]


# PyMC3 imputes missing data automatically, similar to BUGS, but it requires the missing data be input as a NumPy masked array. See the NumPy docs for [np.ma.masked_values()](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_values.html). For ```y```, above, you can enter whatever number at the missing data positions, then plug it into the ```value``` parameter below. Just make sure the number you're using isn't actually in the data!
# 
# Using np.nan for the missing values doesn't seem to work at the moment (NumPy handles it fine, but PyMC3 throws an error).
# 
# Note that this method only works for missing *observed* data. We'll learn about missing data in X later.

# In[3]:


y = np.ma.masked_values(y, value=-1)


# Check it out! The array now has a mask attribute.

# In[4]:


y


# In[5]:


with pm.Model() as dugongs:
    # priors
    alpha = pm.Uniform('alpha', 0, 100)
    beta = pm.Uniform('beta', 0, 100)
    gamma = pm.Uniform('gamma', 0, 1)
    sigma = pm.math.exp(pm.Uniform('sigma', -10, 10))

    mu = alpha - beta * gamma**X

    likelihood = pm.Normal('likelihood', mu=mu, sd=sigma, observed=y)

    # start sampling
    trace = pm.sample(10000, # samples
                      chains=4,
                      tune=500,
                      cores=4,
                      init='jitter+adapt_diag',
                      random_seed=1,
                      return_inferencedata=True)


# In[7]:


az.summary(trace, hdi_prob=.95)


# This output is very close to the BUGS results if you use the inits labeled Alternative (full) inits (initializing the missing values at 1):
# 
# |           | mean    | sd      | MC_error | val2.5pc | median  | val97.5pc | start | sample |
# |-----------|---------|---------|----------|----------|---------|-----------|-------|--------|
# | alpha     | 2.731   | 0.1206  | 0.003167 | 2.551    | 2.711   | 3.025     | 1001  | 100000 |
# | beta      | 0.9846  | 0.1021  | 0.002008 | 0.8053   | 0.9773  | 1.212     | 1001  | 100000 |
# | gamma     | 0.8874  | 0.03381 | 7.64E-04 | 0.8124   | 0.8908  | 0.9427    | 1001  | 100000 |
# | log.sigma | -2.342  | 0.1543  | 7.83E-04 | -2.622   | -2.349  | -2.018    | 1001  | 100000 |
# | sigma     | 0.09733 | 0.0155  | 7.96E-05 | 0.07267  | 0.09547 | 0.1329    | 1001  | 100000 |
# | y[4]      | 1.906   | 0.1098  | 6.23E-04 | 1.689    | 1.906   | 2.123     | 1001  | 100000 |
# | y[27]     | 2.69    | 0.1255  | 0.001916 | 2.446    | 2.689   | 2.941     | 1001  | 100000 |
# 
# 
# If you use the first set of inits, as Professor Vidakovic did in the video, BUGS gives the y[4] mean as 2.047 and y[27] as 3.04. All the other variables are very different here, too. This is quite a mystery - as far as I can tell, the only difference is that the missing values use BUGS-generated inits for the following results. If someone figures out what's going on here, let me know!
# 
# |       | mean   | sd       | MC_error | val2.5pc | median | val97.5pc | start | sample |
# |-------|--------|----------|----------|----------|--------|-----------|-------|--------|
# | alpha | 32.54  | 3.698    | 0.2076   | 23.51    | 32.69  | 40.31     | 1001  | 100000 |
# | beta  | 30.55  | 3.697    | 0.2076   | 21.52    | 30.69  | 38.31     | 1001  | 100000 |
# | gamma | 0.9989 | 2.08E-04 | 8.70E-06 | 0.9984   | 0.9989 | 0.9992    | 1001  | 100000 |
# | sigma | 0.1328 | 0.02071  | 8.17E-05 | 0.09964  | 0.1303 | 0.1805    | 1001  | 100000 |
# | y[4]  | 2.047  | 0.1424   | 5.18E-04 | 1.766    | 2.046  | 2.329     | 1001  | 100000 |
# | y[27] | 3.04   | 0.1606   | 7.42E-04 | 2.722    | 3.04   | 3.358     | 1001  | 100000 |

# In[ ]:




