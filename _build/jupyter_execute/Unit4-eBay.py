#!/usr/bin/env python
# coding: utf-8

# In[1]:


import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pymc3 as pm
from pymc3.math import invlogit

az.style.use("arviz-darkgrid")


# # eBay Purchase Example
# 
# From [Codes for Unit 4: ebay.odc](https://www2.isye.gatech.edu/isye6420/supporting.html).
# 
# Associated lecture video: [Unit 4 Lesson 17: eBay Purchase Example](https://www.youtube.com/watch?v=j-qvssN6llk&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=34).
# 
# You've decided to purchase a new Orbital Shaking Incubator for your research lab on eBay.
# 
# Two sellers are offering this item for the same price, both with free shipping. Seller A has 95% positive feedback from 100 responders, while seller B has 100% positive feedback from 3 responders. We assume that all 103 responders are different, unrelated customers, to avoid dependent responses.
# 
# From which seller should you order?
# 
# That depends on your priors!

# *Note: I changed labels 1 and 2 in the model to A and B to align with the problem definition.*

# In[2]:


# data
pos_A = 95
tot_A = 100

tot_B = 3
pos_B = 3


# In[3]:


with pm.Model() as ebay:
    # priors
    priors_A = (
        pm.Beta("uniform_A", alpha=1, beta=1),
        pm.Beta("jeffrey_A", alpha=0.5, beta=0.5),
        pm.Beta("informative_A", alpha=30, beta=2),
        pm.Deterministic(
            "zellner_A", invlogit(pm.Uniform("ignore_A", lower=-10000, upper=10000))
        ),
        pm.LogitNormal("norm_A", mu=3, sigma=1),
    )

    priors_B = (
        pm.Beta("uniform_B", alpha=1, beta=1),
        pm.Beta("jeffrey_B", alpha=0.5, beta=0.5),
        pm.Beta("informative_B", alpha=2.9, beta=0.1),
        pm.Deterministic(
            "zellner_B", invlogit(pm.Uniform("ignore_B", lower=-10000, upper=10000))
        ),
        pm.LogitNormal("norm_B", mu=3, sigma=1),
    )

    # likelihoods
    for A, B in zip(priors_A, priors_B):
        prior_type = A.name.strip("_A")

        y_A = pm.Binomial("y_" + A.name, n=tot_A, p=A, observed=pos_A)
        y_B = pm.Binomial("y_" + B.name, n=tot_B, p=B, observed=pos_B)

        diff = pm.Deterministic("diff_" + prior_type, A - B)

    # start sampling
    trace = pm.sample(
        4000, tune=1000, chains=4, cores=4, random_seed=1, return_inferencedata=True
    )


# In[4]:


az.summary(trace, var_names=["~ignore_A", "~ignore_B"], hdi_prob=0.95)


# The results are pretty close to the professor's BUGS results:
# 
# |           | mean     | sd       | MC_error | val2.5pc | median    | val97.5pc |
# |-----------|----------|----------|----------|----------|-----------|-----------|
# | diffps[1] | 0.1417   | 0.1649   | 4.93E-04 | -0.06535 | 0.1018    | 0.5448    |
# | diffps[2] | 0.06921  | 0.1485   | 4.63E-04 | -0.08247 | 0.01423   | 0.4774    |
# | diffps[3] | -0.03623 | 0.05252  | 1.70E-04 | -0.09355 | -0.04494  | 0.1144    |
# | diffps[4] | -0.05004 | 0.02177  | 7.02E-05 | -0.1003  | -0.04712  | -0.0164   |
# | diffps[5] | 0.00658  | 0.05593  | 1.73E-04 | -0.06808 | -0.005543 | 0.1526    |
# | p1[1]     | 0.9412   | 0.02319  | 7.40E-05 | 0.8882   | 0.9442    | 0.9778    |
# | p1[2]     | 0.9456   | 0.02235  | 7.13E-05 | 0.8944   | 0.9485    | 0.9808    |
# | p1[3]     | 0.9471   | 0.01937  | 6.09E-05 | 0.9031   | 0.9493    | 0.9782    |
# | p1[4]     | 0.9499   | 0.02169  | 7.04E-05 | 0.8997   | 0.9529    | 0.9836    |
# | p1[5]     | 0.9498   | 0.01973  | 5.96E-05 | 0.9043   | 0.9525    | 0.9804    |
# | p2[1]     | 0.7995   | 0.1632   | 4.89E-04 | 0.3982   | 0.8402    | 0.9938    |
# | p2[2]     | 0.8764   | 0.1468   | 4.56E-04 | 0.4694   | 0.9336    | 0.9999    |
# | p2[3]     | 0.9833   | 0.04892  | 1.58E-04 | 0.8344   | 0.9999    | 1         |
# | p2[4]     | 1        | 0.001891 | 5.84E-06 | 1        | 1         | 1         |
# |  p2[5]    | 0.9432   | 0.05234  | 1.66E-04 | 0.7986   | 0.9592    | 0.9935    |

# In[5]:


az.plot_trace(trace, var_names=["~ignore_A", "~ignore_B"])
plt.show()


# I'd like to expand on this answer in the future, leaving it for now!
