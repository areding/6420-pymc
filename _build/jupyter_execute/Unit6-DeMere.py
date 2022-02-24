#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# # Demere
# 
# Not sure what this is from! The professor doesn't mention it in lectures, but it was in the Codes4Unit6 archive so here you go!
# 
# - What is more likely in rolling 3 fair dice: sum 11 or sum 12?
# - What is more likely in rolling 300 fair dice: sum 1111 or sum 1112?

# In[3]:


rng = np.random.default_rng(1)
sims = 1000000


def prob_sum(arr, s):
    """
    return probability of sum s in (sims, dice)-shaped np array arr
    """
    sims = arr.shape[0]
    return (arr.sum(axis=1) == s).sum() / sims


# simulate 3 dice rolls
rolls_3 = rng.integers(1, 6, (sims, 3), endpoint=True)
print("Results with 3 dice")
print("Simulated probability of rolling 11:", prob_sum(rolls_3, 11))
print("Simulated probability of rolling 12:", prob_sum(rolls_3, 12))

# simulate 300 dice rolls
rolls_300 = rng.integers(1, 6, (sims, 300), endpoint=True)
print("\nResults with 300 dice")
print("Simulated probability of rolls summing to 1111:", prob_sum(rolls_300, 1111))
print("Simulated probability of rolls summing to 1112:", prob_sum(rolls_300, 1112))


# In[ ]:




