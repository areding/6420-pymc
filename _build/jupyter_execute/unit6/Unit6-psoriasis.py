#!/usr/bin/env python
# coding: utf-8

# In[1]:


import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pymc3 as pm
from pymc3.math import switch


# # Psoriasis: Two sample problem with paired data
# 
# Adapted from [Codes for Unit 6: psoriasis.odc](https://www2.isye.gatech.edu/isye6420/supporting.html).
# 
# Associated lecture video: [Unit 6 Lesson 7](https://www.youtube.com/watch?v=aF1whV0brtw&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=58).
# 
# Woo and McKenna (2003) investigated the effect of broadband ultraviolet B (UVB) therapy and topical calcipotriol cream used together on areas of psoriasis. One of the outcome variables is the Psoriasis Area and Severity Index (PASI), where a lower score is better.
# 
# The PASI scores for 20 subjects are measured at baseline and after 8 treatments.  Do these data provide sufficient evidence to indicate that the combination therapy reduces PASI scores?
# 
# Classical Analysis:
# ```
#    d = baseline - after;
#    n = length(d);
#    dbar = mean(d);  dbar = 6.3550
#    sdd = sqrt(var(d));  sdd = 4.9309
#    tstat = dbar/(sdd/sqrt(n));  tstat = 5.7637
# 
#    Reject H_0 at the level alpha=0.05 since the p_value = 0.00000744 < 0.05
# 
#    95% CI is [4.0472, 8.6628]
#    ```
# 

# ---
# See [Unit 6: Stress, Diet and Plasma Acids](https://areding.github.io/6420-pymc/Unit6-stressacids.html) to find out more about converting the BUGS step function.

# In[2]:


# fmt: off
baseline = np.array((5.9, 7.6, 12.8, 16.5, 6.1, 14.4, 6.6, 5.4, 9.6, 11.6, 
                     11.1, 15.6, 9.6, 15.2, 21.0, 5.9, 10.0, 12.2, 20.2, 
                     6.2))
after = np.array((5.2, 12.2, 4.6, 4.0, 0.4, 3.8, 1.2, 3.1, 3.5, 4.9, 11.1,
                  8.4, 5.8, 5, 6.4, 0.0, 2.7, 5.1, 4.8, 4.2))
# fmt: on


# In[3]:


with pm.Model() as m:
    # priors
    mu = pm.Normal("mu", mu=0, sigma=316)
    prec = pm.Gamma("prec", alpha=0.001, beta=0.001)
    sigma = pm.Deterministic("sigma", 1 / pm.math.sqrt(prec))

    ph1 = pm.Deterministic("ph1", switch(mu >= 0, 1, 0))

    diff = pm.Normal("diff", mu=mu, sigma=sigma, observed=baseline - after)

    # start sampling
    trace = pm.sample(
        10000,
        chains=4,
        tune=500,
        cores=4,
        init="jitter+adapt_diag",
        random_seed=1,
        return_inferencedata=True,
    )


# In[4]:


az.summary(trace, hdi_prob=0.95, var_names=["~prec"])


# Even though we're getting lots of warnings, our model agrees with the BUGS results:
# 
# |          | mean     | sd      | MC_error | val2.5pc | median | val97.5pc | start | sample |
# |----------|----------|---------|----------|----------|--------|-----------|-------|--------|
# | pH1      | 1        | 0       | 3.16E-13 | 1        | 1      | 1         | 1001  | 100000 |
# | mu       | 6.352    | 1.169   | 0.003657 | 4.043    | 6.351  | 8.666     | 1001  | 100000 |
# | sigma    | 5.142    | 0.8912  | 0.003126 | 3.74     | 5.026  | 7.203     | 1001  | 100000 |
# | pval     | 4.20E-04 | 0.02049 | 6.04E-05 | 0        | 0      | 0         | 1001  | 100000 |

# In[ ]:




