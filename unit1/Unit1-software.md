# Software

::::{important}
Starting in Fall 2025, we will be switching to PyMC and Python only for all course coding.
::::

## Probabilistic programming languages

As the professor says, [BUGS](https://www.mrc-bsu.cam.ac.uk/software/bugs/) (Bayesian Inference using Gibbs Sampling) is actually a pretty good choice for learning the basics of Bayesian inference. There are things that BUGS can do that are still a pain to implement in PyMC. PyMC is also under active development; since Spring 2022 when this site went up, it's already gone through two major version changes. Every semester there are changes to be researched and worked around, whereas BUGS hasn't changed much for 15 years. So I understand why the professor stuck with it, even in 2018 when putting this course online.

But there's a tension there between students who are looking to practice career skills—they tend to want to use something Python or R-based. So we've redone most of the course examples in PyMC and provide Python solutions to any homework or exam problems we ask.

Students are now required to use PyMC for our course. We are leaving this list of other PPLs below if you are interested and are no longer updating it.

### BUGS and family

#### WinBUGS and OpenBUGS

The professor sometimes references WinBUGS, but all the original course examples are actually written for [OpenBUGS](https://www.mrc-bsu.cam.ac.uk/software/bugs/openbugs/).

You can also try [R2OpenBUGS](https://cran.r-project.org/web/packages/R2OpenBUGS/index.html), which allows you to call BUGS to evaluate your models from the R language.

#### MultiBUGS, JAGS, and NIMBLE

Development of BUGS, or at least PPLs that use BUGS scripts, has continued!

[MultiBUGS](https://www.multibugs.org/) adds parallelization to BUGS. The last release was in 2020.

[JAGS](https://mcmc-jags.sourceforge.io/) is also based on the BUGS scripting language. The latest release was April 2022. Greg has many of the lecture examples in JAGS available for download [here](https://www2.isye.gatech.edu/isye6420/Bank/rjags_final.zip).

[NIMBLE](https://r-nimble.org/) seems really nice. If, like me, you're using a ARM-based Mac, this is the easiest way I've found to get going with BUGS models since it's just an R package with no need to download anything separately. This is still actively developed as of summer 2023.

### The wider PPL ecosystem

If you want something a little more challenging and are comfortable with, or interested in, learning Python, try [PyMC](https://www.pymc.io/welcome.html) along with the examples on this site.

If you want to learn a more stable tool with excellent documentation, try [Stan](https://mc-stan.org/).

If you're really adventurous and want to learn Julia, maybe try [Turing.jl](https://github.com/TuringLang/Turing.jl). If you love trying the absolute latest thing and you want to go into completely uncharted territory for this class, you could look at [AeMCMC](https://github.com/aesara-devs/aemcmc), [Blackjax](https://blackjax-devs.github.io/blackjax/examples/quickstart.html#), [NumPyro](https://github.com/pyro-ppl/numpyro), [Oryx](https://github.com/jax-ml/oryx), [Tensorflow Probability](https://www.tensorflow.org/probability), [Distrax](https://github.com/deepmind/distrax), or go find something I've never heard of (and tell me about it)!

## General purpose programming languages

Python is now required for our course.