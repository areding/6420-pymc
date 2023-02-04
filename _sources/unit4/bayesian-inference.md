# Bayesian inference

For now, this is just a list of what I consider the most important parts of the unit. This is a lot of stuff, so don't worry if you don't understand it all right away. It will sink in as we go through the course.

I hope to expand these notes over time.

## Distributions

Understand what a random variable is.

The most commonly used distributions in this class:

### Continuous

- Normal
- Uniform
- Exponential
- Gamma
- Beta
- Multivariate normal
- Weibull
- Student's *t*-distribution

### Discrete

- Bernoulli
- Binomial
- Poisson
- Multinomial

Understand that there are different ways to parameterize distributions and what those parameters mean for different distributions (keywords: shape, rate, scale, location). Probably the most-common mistake in this course is mistaking precision for variance in the normal distribution! Use the parameterizations in [*Engineering Biostatistics*](statbook.gatech.edu) unless otherwise specified.

Joint distributions and conditional distributions will be important for Units 4 and 5.

## Bayes' theorem and the likelihood principle

Understand the likelihood principle and how Bayes' theorem is applied to distributions (before we were practicing with probabilities).

Be aware that conjugate distributions exist and check out the table in the statbook.

## Point estimates

Mean, median, MAP.

## Credible intervals (aka credible sets)

See the [Gamma Gamma](https://areding.github.io/6420-pymc/unit4/Unit4-GammaGamma.html) example.


## Non-informative priors

The professor uses tons of non-informative priors throughout the course. My impression is that  use of these priors has fallen out of favor. There's no such thing as a completely non-informative prior!

That said, the priors in this lecture (Unit 4 lession 15) come up often later on. No need to memorize anything, but it's worth making a note for later reference.
