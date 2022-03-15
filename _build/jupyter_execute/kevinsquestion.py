#!/usr/bin/env python
# coding: utf-8

# Kevin's question:
# 
# I was working through some practice applications at work, and I ran into this issue.
# 
# What if there's no overlap of the prior and likelihood? (I.e. likelihood is zero in the domain of the prior and vice versa)
# 
# Would you just observe the resulting zero posterior and try again with a wider prior? 
# 
# I came into this class thinking that the likelihood shifted the prior density, which is kinda true, but not if they don't overlap in theta space. Am I missing something?
# 
# 

# Want to try inventing weird situations where the likelihood, prior, and data don't overlap at all.
# 
# Todo:
# - Try sampling from improper posterior. 
# - Try creating a bimodal posterior. 
# - Try creating a flat posterior.
# - Can you actually create a posterior around zero?

# In[42]:


import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pymc3 as pm


# In[ ]:


# invent some data

with pm.Model() as model:
    # priors
    alpha = pm.Normal("alpha", sigma=1)
    beta = pm.Normal("beta", sigma=1)
    # using precision for direct comparison with BUGS output
    sigma = pm.Normal("sigma", mu=0, sigma=1)

    mu = alpha + beta * X
    likelihood = pm.Normal("likelihood", mu=mu, sd=sigma, observed=y)

    # start sampling
    trace = pm.sample(
        3000,  # samples
        chains=4,
        tune=500,
        init="jitter+adapt_diag",
        random_seed=1,
        cores=4,  # parallel processing of chains
        return_inferencedata=True,  # return arviz inferencedata object
    )


# In[27]:


alpha = .05

1 - (1- alpha/2)**(1/11)


# In[30]:


((alpha/2) - 1)**(1/11) + 1


# In[31]:


(-alpha/2)**(1/11) +1


# In[32]:


(-alpha)**(1/11) + 1


# In[36]:


.42/.58


# In[35]:


.99/.01


# In[37]:


1.36/26


# In[38]:


.58/.42


# In[39]:


(alpha/2)**(1/11)


# In[46]:


1 - np.exp(np.log(alpha)/11)


# In[53]:


((-1)**(10/11)*(alpha-2)**(1/11))/2**(1/11)


# In[58]:


(-1)**(3/11)


# In[52]:


1 - alpha**(1/11)/2**(1/11)


# In[59]:


float("inf")


# In[61]:


0.9998475842/1.524e-4


# In[ ]:




