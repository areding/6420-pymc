#!/usr/bin/env python
# coding: utf-8

# In[1]:


import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymc3 as pm


# # Taste of Cheese
# 
# Adapted from [Codes for Unit 6: cheese.odc](https://www2.isye.gatech.edu/isye6420/supporting.html).
# 
# Associated lecture videos: [Unit 6 Lesson 4](https://www.youtube.com/watch?v=xomK4tcePmc&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=56) and [Lesson 7](https://www.youtube.com/watch?v=OThLwqQtXE4&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=59).
# 
# 
# The link in the original .odc file is dead. I downloaded the data from [here](https://www3.nd.edu/~busiforc/handouts/Data%20and%20Stories/multicollinearity/Cheese%20Taste/Cheddar%20Cheese%20Data.html) and have a copy [here](https://raw.githubusercontent.com/areding/6420-pymc/main/data/cheese.csv).
# 
# As cheddar cheese matures, a variety of chemical processes take place. The taste of matured cheese is related to the concentration of several chemicals in the final product. In a study of cheddar cheese from the LaTrobe Valley of Victoria, Australia, samples of cheese were analyzed for their chemical composition and were subjected to taste tests. Overall taste scores were obtained by combining the scores from several tasters.
# 
# Can the score be predicted well by the predictors: Acetic, H2S, and Lactic?

# In[2]:


data = pd.read_csv("./data/cheese.csv", index_col=0)
X = data[["Acetic", "H2S", "Lactic"]].values
# add intercept column to X
X_aug = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)
y = data["taste"].values


# In[3]:


with pm.Model() as cheese:
    # associate data with model (this makes prediction easier)
    X_data = pm.Data("X", X_aug)
    y_data = pm.Data("y", y)

    # priors
    beta = pm.Normal("beta", mu=0, sigma=1000, shape=X.shape[1] + 1)
    tau = pm.Gamma("tau", alpha=0.001, beta=0.001)
    sigma = 1 / pm.math.sqrt(tau)

    mu = pm.math.dot(X_data, beta)

    # likelihood
    taste_score = pm.Normal("taste_score", mu=mu, sd=sigma, observed=y_data)

    # start sampling
    trace = pm.sample(
        10000,  # samples
        chains=4,
        tune=1000,
        init="jitter+adapt_diag",
        random_seed=1,
        cores=4,
        return_inferencedata=True,
        target_accept=0.95,
    )


# In[4]:


az.summary(trace, hdi_prob=0.95)


# Results are pretty close to OpenBUGS:
# 
# |         mean |     sd   |        MC_error |   val2.5pc | median  |   val97.5pc | start   | sample |        |
# |--------------|----------|-----------------|------------|---------|-------------|---------|--------|--------|
# | beta0        | -29.75   | 20.24           | 0.7889     | -70.06  | -29.75      | 11.11   | 1000   | 100001 |
# | beta1        | 0.4576   | 4.6             | 0.189      | -8.716  | 0.4388      | 9.786   | 1000   | 100001 |
# | beta2        | 3.906    | 1.291           | 0.02725    | 1.345   | 3.912       | 6.47    | 1000   | 100001 |
# | beta3        | 19.79    | 8.893           | 0.2379     | 2.053   | 19.88       | 37.2    | 1000   | 100001 |
# | tau          | 0.009777 | 0.002706        | 2.29E-05   | 0.00522 | 0.009528    | 0.01575 | 1000   | 100001 |

# But PyMC3 gives some warnings about the model unless we increase the ```target_accept``` parameter of ```pm.sample```. PyMC3 uses more diagnostics than BUGS to check if there are any problems with its exploration of the parameter space. Divergences indicate bias in the results. BUGS will happily run this model without reporting any problems, but it doesn't mean that there aren't any.
# 
# For further reading, check out [Diagnosing Biased Inference with Divergences](https://docs.pymc.io/en/v3/pymc-examples/examples/diagnostics_and_criticism/Diagnosing_biased_Inference_with_Divergences.html).

# It looks like there are multiple ways to get predictions on out-of-sample data in PyMC. The easiest way is to set up a shared variable using pm.Data in the original model, then using pm.set_data to change to the new observations before calling pm.sample_posterior_predictive. This section still needs some experimentation.

# In[5]:


# prediction
new_obs = np.array([[1.0, 5.0, 7.1, 1.5]])
pm.set_data({"X": new_obs}, model=cheese)
ppc = pm.sample_posterior_predictive(trace, model=cheese, samples=30)


# In[6]:


az.summary(ppc, hdi_prob=0.95)

