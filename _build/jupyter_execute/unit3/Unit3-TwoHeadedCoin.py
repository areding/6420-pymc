#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# # Two-headed Coin
# From [Codes for Unit 3](https://www2.isye.gatech.edu/isye6420/supporting.html).
# 
# Associated lecture videos: Unit 3 [Lesson 4](https://www.youtube.com/watch?v=FYjmNM1iMkA&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=14) and [Lesson 6](https://www.youtube.com/watch?v=M4kbEw7xFy4&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=15).
# 
# 
# This is a pretty simple one. I'm sure no one needed help redoing this in Python, I'm just including it for the sake of completeness!
# 
# Out of N coins only one has two heads. A coin is selected at random from the pile and flipped k times. Heads appears k times in a row. What is the probability that the coin with two heads was selected?

# In[2]:


N = 1000000
flips = 40


def prob(k, N):
    """
    Calculate probability that we've selected a two-headed coin.

    k int: number of flips that come up as heads (consecutively)
    N int: number of coins we selected from.

    returns: probability at k flips in a row
    """
    return 2 ** k / (2 ** k + N - 1)


# create a list of probabilities for different values of k
probabilities = [prob(k, N) for k in range(flips)]

# plot using matplotlib
plt.plot(probabilities)
plt.xlabel("Flips")
plt.ylabel("Probability")
plt.suptitle("Probability that selected coin is two-headed")
plt.title("(given k flips in a row landing on heads)")
plt.show()

