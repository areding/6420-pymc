#!/usr/bin/env python
# coding: utf-8

# In[1]:


import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pymc3 as pm
from pymc3.math import switch


# # Equivalence of Generic and Brand-Name Drugs 
# 
# 
# Adapted from [Codes for Unit 6: equivalence.odc](https://www2.isye.gatech.edu/isye6420/supporting.html).
# 
# Associated lecture video: [Unit 6 Lesson 7](https://www.youtube.com/watch?v=aF1whV0brtw&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=58).
# 
# The manufacturer wishes to demonstrate that their generic drug for a particular metabolic disorder is equivalent to a brand name drug. One of indication of the disorder is an abnormally low concentration of levocarnitine, an amino acid derivative, in the plasma. The treatment with the brand name drug substantially increases this concentration.
# 
# A small clinical trial is conducted with 43 patients, 18 in the Brand Name Drug arm and 25 in the Generic Drug arm. The increases in the log-concentration of levocarnitine are in the data below.
# 
# The FDA declares that bioequivalence among the two drugs can be established if the difference in response to the two drugs is within 2 units of log-concentration. Assuming that the log-concentration measurements follow normal distributions with equal population variance, can these two drugs be declared bioequivalent within a tolerance +/-2  units?
# 

# ---
# The way the data is set up in the .odc file is strange. It seems simpler to just have a separate list for each increase type.

# In[2]:


# fmt: off
increase_type1 = [7, 8, 4, 6, 10, 10, 5, 7, 9, 8, 6, 7, 8, 4, 6, 10, 8, 9]
increase_type2 = [6, 7, 5, 9, 5, 5, 3, 7, 5, 10, 8, 5, 8, 4, 4, 8, 6, 11, 
                  7, 5, 5, 5, 7, 4, 6]
# fmt: on


# We're using ```pm.math.switch``` to recreate the BUGS ```step()``` function for the ```probint``` variable.

# In[3]:


with pm.Model() as equivalence:
    # priors
    mu1 = pm.Normal("mu1", mu=10, sigma=316)
    mu2 = pm.Normal("mu2", mu=10, sigma=316)
    mudiff = pm.Deterministic("mudiff", mu1 - mu2)
    prec = pm.Gamma("prec", alpha=0.001, beta=0.001)
    sigma = 1 / pm.math.sqrt(prec)

    probint = pm.Deterministic(
        "probint",
        switch(mudiff + 2 >= 0, 1, 0) * switch(2 - mudiff >= 0, 1, 0),
    )

    y_type1 = pm.Normal("y_type1", mu=mu1, sd=sigma, observed=increase_type1)
    y_type2 = pm.Normal("y_type2", mu=mu2, sd=sigma, observed=increase_type2)

    # start sampling
    trace = pm.sample(
        10000,
        chains=4,
        tune=500,
        init="jitter+adapt_diag",
        random_seed=1,
        return_inferencedata=True,
    )


# In[4]:


az.summary(trace, hdi_prob=0.95)


# BUGS results:
# 
# |          | mean   | sd      | MC_error | val2.5pc | median | val97.5pc | start | sample |
# |----------|--------|---------|----------|----------|--------|-----------|-------|--------|
# | mu[1]    | 7.332  | 0.473   | 0.001469 | 6.399    | 7.332  | 8.264     | 1001  | 100000 |
# | mu[2]    | 6.198  | 0.4006  | 0.001213 | 5.406    | 6.199  | 6.985     | 1001  | 100000 |
# | mudiff   | 1.133  | 0.618   | 0.00196  | -0.07884 | 1.134  | 2.354     | 1001  | 100000 |
# | prec     | 0.2626 | 0.05792 | 1.90E-04 | 0.1617   | 0.2584 | 0.3877    | 1001  | 100000 |
# | probint  | 0.9209 | 0.2699  | 9.07E-04 | 0        | 1      | 1         | 1001  | 100000 |
