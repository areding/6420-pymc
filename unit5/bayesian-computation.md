# Bayesian computation

Once we move past conjugate cases, while we may have the posterior in analytical form as a result of Bayes' theorem, it won't be any recognizable distribution no matter how much we manipulate it. Many of the normalizing constants have no closed-form solution. As the professor shows in lessons 2 and 4 of this unit, we can try to approximate them numerically, but this may be imprecise or computationally intractable (with time complexity increasing exponentially with the number of parameters, as in the example from section 2.1 [of this paper](https://arxiv.org/pdf/1601.00670.pdf).

https://betanalpha.github.io/assets/case_studies/probabilistic_computation.html 

The second half of this course focuses more on modeling than on the specific method used to get at the posterior, but in order to do that, we need to choose a method for sampling from or approximating the posterior. There are a lot of ways out there (see [other methods](https://areding.github.io/6420-pymc/unit5/other-methods.html)), but we're going to focus on Markov Chain Monte Carlo (MCMC) methods. They have a lot of advantages, including a relatively easy algorithm to implement and understand.