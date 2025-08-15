# 2. Reasons to Use Hierarchical Models

## Why the heirarchy?

1. Modeling requirement. For example, a [meta-analysis](https://areding.github.io/6420-pymc/unit7/Unit7-metaanalysis.html)
2. Prior information can be separated into structural and subjective/noninformative part ([like this example](https://areding.github.io/6420-pymc/unit7/Unit7-priors.html))
3. Robustness + objectivity, let the data "talk" about the hyperparameters
4. Computing issues (MCMC efficiency, perhaps to a lesser extent now than in the past)

## Example

Posterior with single parameter $\theta$:  

$$\prod_{i=1}^n f(y_i | \theta) \pi(\theta)$$

Posterior with an independent $\theta_i$ for each $y_i$:  

$$\prod_{i=1}^n f(y_i | \theta_i) \pi(\theta_i)$$

Now let's create a heirarchical posterior with a $\theta_i$ for each $y_i$, and shared prior $\phi$ on the $\theta_i$'s. The $\theta_i$'s are no longer independent, but *exchangeable*, meaning the order of the $y_i$'s does not impact the posterior distribution.

$$\pi(\phi)\prod_{i=1}^n f(y_i | \theta_i) \pi(\theta_i | \phi)$$

If $y_i$'s are independent, then they are automatically exchangeable, because of the communative property when they are multiplied together in the joint distribution.

However, exchangeable variables may be dependent. For example, the 2-dimensional multivariate Normal,

$$(X,Y) \sim \text{MVN}_2(0,\left( \begin{matrix}
    1 & \rho \\
    \rho & 1 \end{matrix}\right)), \space \rho \in (-1,1) $$

the 2 variable $X$ and $Y$ are not independent, they are correlated, and yet the are exchangeable because the distribution of $(Y,X)$ is the same as the distribution of $(X,Y)$.
