#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # Gibbs Sampler Example 2: Pumps
# 
# Adapted from [Codes for Unit 5: pumpsmc.m](https://www2.isye.gatech.edu/isye6420/supporting.html).
# 
# Associated lecture video: [Unit 5 Lesson 13](https://www.youtube.com/watch?v=DKlP93sD0O0&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=49).

# In[ ]:


rng = np.random.default_rng(1)

obs = 100000
burn = 1000

# data from Gaver and O'Muircheartaigh, 1987
X = np.array([5, 1, 5, 14, 3, 19, 1, 1, 4, 22])
t = [94.32, 15.52, 62.88, 125.76, 5.24, 31.44, 1.048, 1.048, 2.096, 10.48]
n = len(X)

# params
c = .1
d = 1

# inits
theta = np.ones(n)
beta = 1

thetas = np.zeros(obs)
lambdas = np.zeros(obs)

# pre-generate randoms where possible
randn = rng.standard_normal(obs)

for i in tqdm(range(obs)):
    d = tau2 + lam*sigma2
    theta = (tau2/d * x + lam*sigma2/d * mu) + np.sqrt(tau2*sigma2/d) * randn[i]
    lam = rng.exponential(1/((tau2 + (theta - mu)**2)/(2*tau2)))
    
    thetas[i] = theta
    lambdas[i] = lam

thetas = thetas[burn:]
lambdas = lambdas[burn:]

print(f'{np.mean(thetas)=}')
print(f'{np.var(thetas)=}')
print(f'{np.mean(lambdas)=}')
print(f'{np.var(lambdas)=}')

plt.hist(thetas, 40)
plt.xlabel('theta')
plt.show()

plt.hist(lambdas, 40)
plt.xlabel('lambda')
plt.show()

