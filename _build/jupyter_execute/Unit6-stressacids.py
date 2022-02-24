#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # Stress, Diet and Plasma Acids
# 
# 
# 
# In the study [Interrelationships Between Stress, Dietary Intake, and Plasma Ascorbic Acid During Pregnancy](https://vtechworks.lib.vt.edu/handle/10919/74486) conducted at the Virginia Polytechnic Institute and State University, the plasma ascorbic acid levels of pregnant women were compared for smokers versus non-smokers. Thirty-two women in the last three months of pregnancy, free of major health disorders, and ranging in age from 15 to 32 years were selected for the study. Prior to the collection of 20 ml of blood, the participants were told to avoid breakfast, forego their vitamin supplements, and avoid foods high in ascorbic acid content. From the blood samples, the plasma ascorbic acid values of each subject were determined in milligrams per 100 milliliters.

# In[2]:


# fmt: off
plasma = [0.97, 0.72, 1.00, 0.81, 0.62, 1.32, 1.24, 0.99, 0.90, 0.74,
          0.88, 0.94, 1.06, 0.86, 0.85, 0.58, 0.57, 0.64, 0.98, 1.09,
          0.92, 0.78, 1.24, 1.18, 0.48, 0.71, 0.98, 0.68, 1.18, 1.36,
          0.78, 1.64]
smo = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
       1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]
# fmt: on

nonsmokers = [x for x, y in zip(plasma, smo) if y == 1]
smokers = [x for x, y in zip(plasma, smo) if y == 2]


# In[3]:


with pm.Model() as stressacids:
    # priors
    tau_nonsmokers = pm.Gamma("tau_nonsmokers", alpha=0.0001, beta=0.0001)
    sigma_nonsmokers = 1 / pm.math.sqrt(tau_nonsmokers)
    mu_nonsmokers = pm.Normal("mu_nonsmokers", mu=0, sigma=100)

    tau_smokers = pm.Gamma("tau_smokers", alpha=0.0001, beta=0.0001)
    sigma_smokers = 1 / pm.math.sqrt(tau_smokers)
    mu_smokers = pm.Normal("mu_smokers", mu=0, sigma=100)

    # likelihood
    plasma_aa_nonsmokers = pm.Normal(
        "nonsmokers_aa", mu=mu_nonsmokers, sd=sigma_nonsmokers, observed=nonsmokers
    )
    plasma_aa_smokers = pm.Normal(
        "smokers_aa", mu=mu_smokers, sd=sigma_smokers, observed=smokers
    )

    # start sampling
    trace = pm.sample(
        1000,  # samples
        chains=4,
        tune=500,
        init="jitter+adapt_diag",
        random_seed=1,
        return_inferencedata=True,
    )


# In[ ]:




