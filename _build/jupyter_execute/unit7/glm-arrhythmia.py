#!/usr/bin/env python
# coding: utf-8

# In[85]:


import arviz as az
import numpy as np
import pymc as pm
from pymc.math import log, dot
import pandas as pd
get_ipython().run_line_magic('load_ext', 'watermark')


# # Arrhythmia
# 
# Adapted from [Codes for Unit 7: arrhythmia.odc](https://www2.isye.gatech.edu/isye6420/supporting.html).
# 
# Associated lecture video: [Unit 7 Lesson 15](https://www.youtube.com/watch?v=999v5stS8jw&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=77).
# 
# Data can be found [here](https://raw.githubusercontent.com/areding/6420-pymc/main/data/arrhythmia.csv).
# 
# Patients who undergo Coronary Artery Bypass Graft Surgery (CABG) have an approximate 19-40% chance of developing atrial fibrillation (AF). AF can lead to blood clots forming causing greater in-hospital mortality, strokes, and longer hospital stays. While this can be prevented with drugs, it is very expensive and sometimes dangerous if not warranted. Ideally, several risk factors which would indicate an increased risk of developing AF in this population could save lives and money by indicating which patients need pharmacological intervention. Researchers began collecting data from CABG patients during their hospital stay such as demographics like age and sex, as well as heart rate, cholesterol, operation time, etc.. Then, the researchers recorded which patients developed AF during their hospital stay. Researchers now want to find those pieces of data which indicate high risk of AF. In the past, indicators like age, hypertension, and body surface area (BSA) have been good indicators, though these alone have not produced a satisfactory solution.
# 
# Fibrillation occurs when the heart muscle begins a quivering motion instead of a normal, healthy pumping rhythm. Fibrillation can affect the atrium (atrial fibrillation) or the ventricle (ventricular  fibrillation); ventricular fibrillation is imminently life threatening.
# 
# Atrial fibrillation is the quivering, chaotic motion in the upper chambers of the heart, known as the atria. Atrial fibrillation is often due to serious underlying medical conditions, and should be evaluated by a physician. It is not typically a medical emergency.
# 
# Ventricular fibrillation occurs in the ventricles (lower chambers) of the heart; it is always a medical emergency. If left untreated, ventricular fibrillation (VF, or V-fib) can lead to death within minutes. When a heart goes into V-fib, effective pumping of the blood stops. V-fib is considered a form of cardiac arrest, and an individual suffering from it will not survive unless cardiopulmonary resuscitation (CPR) and defibrillation are provided immediately.
# 
# DATA Arrhythmia
# - Y = Fibrillation
# - X1 = Age
# - X2 = Aortic Cross Clamp Time
# - X3 = Cardiopulmonary Bypass Time:
#     - Bypass of the heart and lungs as, for example, in open heart surgery. Blood returning to the heart is diverted through a heart-lung machine (a pump-oxygenator) before returning it to the arterial circulation. The machine does the work both of the heart (pump blood) and the lungs (supply oxygen to red blood cells).
# - X4 = ICU Time	(Intensive Care Unit)
# - X5 = Avg Heart Rate	
# - X6 = Left Ventricle Ejection Fraction
# - X7 = Hypertension
# - X8 = Gender [1 -Female; 0-Male]
# - X9 = Diabetis
# - X10 = Previous MI
# 
# 
# ----------------------------
# 
# Just throwing this up real quick because it might be useful for homework 5. Note this is using PyMC 4.0 beta 3. I didn't add the residual calculation yet because I don't think it's required for this homework.

# In[24]:


get_ipython().run_line_magic('watermark', '--iversions')


# In[79]:


data_df = pd.read_csv("./data/arrhythmia.csv")
data_df.info()
X = data_df.iloc[:, 1:].values
# add intercept column to X
X_aug = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)
y = data_df["Fibrillation"].values


# In[88]:


with pm.Model() as m:
    X_data = pm.Data("X_data", X_aug)
    y_data = pm.Data("y_data", y)

    betas = pm.Normal("beta", mu=0, tau=0.001, shape=X.shape[1] + 1)

    p = dot(X_data, betas)

    lik = pm.Bernoulli("y", logit_p=p, observed=y_data)

    trace = pm.sample(
        10000,
        chains=4,
        tune=500,
        cores=4,
        random_seed=1,
    )


# In[90]:


az.summary(trace, hdi_prob=.95)

