#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pymc3 as pm
import arviz as az
import matplotlib.pyplot as plt


# # Bartholomew (1957) for Type I censoring
# 
# 
# Adapted from [Codes for Unit 6: exponential1.odc](https://www2.isye.gatech.edu/isye6420/supporting.html).
# 
# Associated lecture videos: [Unit 6 Lesson 9](https://www.youtube.com/watch?v=6gKnM6vL8Po&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=60).
# 
# 
# These are the notes from the odc file (I'll clean these up another time):
# 
# ```
# all=[2  72*  51  60*  33  27  14  24  4  21*];
# sum(all) = 308
# observed=[2   51   33 27 14 24 4  ];
# sum(observed) =155
# n=10, r=7
# ```
# TAKE CENSORED AS OBSERVED  308/10=30.8
# 
# IGNORE CENSORED 155/7 = 22.1429
# 
# MLE UNDER EXPONENTIAL MODEL 308/7 = 44

# In[ ]:


alpha = .01
beta = .1

observed= (2, NA, 51, NA, 33, 27, 14, 24, 4, NA)
censored = (0, 72, 0, 60, 0, 0, 0, 0, 0, 21)


# In[ ]:


with pm.Model() as bartholomew:
    


# BUGS results:
# 
# |               |            mean | sd     | MC_error | val2.5pc | median  | val97.5pc | start | sample |
# |---------------|-----------------|--------|----------|----------|---------|-----------|-------|--------|
# | lambda        | 0.02281         | 0.0086 | 3.66E-05 | 0.009229 | 0.02169 | 0.04248   | 1001  | 100000 |
# | mu            | 51.07           | 22.61  | 0.1018   | 23.54    | 46.09   | 108.4     | 1001  | 100000 |
# | observed[2]   | 122.8           | 60.45  | 0.2442   | 73.12    | 103.5   | 284.5     | 1001  | 100000 |
# | observed[4]   | 110.8           | 59.93  | 0.2145   | 61.09    | 91.81   | 269.8     | 1001  | 100000 |
# | observed[10]  | 72.01           | 60.28  | 0.2155   | 22.13    | 52.89   | 232.6     | 1001  | 100000 |

# In[ ]:




