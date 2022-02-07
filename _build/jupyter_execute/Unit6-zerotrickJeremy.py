#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # Zero-trick Jeremy
# 
# ?????

# In[ ]:


y = 98
mu = 110
sigma = 8.944272  
tau = 10.954451


# In[ ]:


with pm.Model() as zerotrickjeremy:
    # priors

    tau = pm.Gamma('tau', alpha=.001, beta=.001)
    sigma = 1/np.sqrt(tau)

    # likelihood
    mu = (beta0 + beta1 * data['Acetic'].values + beta2*data['H2S'].values
        + beta3*data['Lactic'].values)

    taste = pm.Normal('score', mu=mu, sd=sigma, observed=data['taste'].values)

    # start sampling
    trace = pm.sample(1000, # samples
                      chains=2,
                      tune=500,
                      init='jitter+adapt_diag',
                      random_seed=1,
                      return_inferencedata=True)

