# 4. Bayes' Theorem

Say we have hypothesis $H_i$ and some data $D$.

$$P(H_i \mid D) = \frac{P(D \mid H_i)}{P(D)} \times P(H_i)$$

We'll update the notation in Unit 4 when we start dealing with continuous distributions, but the structure won't change. $P(H_i)$ represents the prior probability of $H_i$. $P(H_i \mid D)$ the posterior probability, which is the prior  updated by $\frac{P(D \mid H_i)}{P(D)}$. 

For now, we can call $P(D \mid H_i)$ the sampling probability. It contains the observed data, which for the moment can be just a number (later it will be the assumed distribution of that data and we'll call it a likelihood).

Finally we have $P(D)$, which is the marginal probability or normalization factor. This is necessary to normalize the updated sampling probability; otherwise, the posterior will not be limited to between 0 and 1.

In {cite:t}`jaynes2003`, Bayes' theorem is represented a bit differently:

$$P(H_i \mid DX) = \frac{P(D \mid H_i X)}{P(D \mid X)} \times P(H_i \mid X)$$

This is the same thing! The reason he adds the additional $X$ is to represent the prior information more clearly. Sometimes just representing it as $P(H_i)$ confuses students because it incorrectly gives the impression that it's something completely different than the posterior.

```{epigraph}
The left-hand side . . . is generally called a ‘*posterior probability*’, with the same *caveat* that this means only ‘logically later in the particular chain of inference being made’, and not necessarily ‘later in time’. And again the distinction is conventional, not fundamental; one man’s prior probability is another man’s posterior probability. There is really only one kind of probability; our different names for them refer only to a particular way of organizing a calculation. 

-- {cite:t}`jaynes2003` p. 89
```