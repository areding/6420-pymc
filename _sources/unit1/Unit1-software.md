# Software

## Probabilistic programming languages

As the professor says, [BUGS](https://www.mrc-bsu.cam.ac.uk/software/bugs/) (Bayesian Inference using Gibbs Sampling) is actually a pretty good choice for learning the basics of Bayesian inference. There are things that BUGS can do that are still a pain to implement in PyMC. PyMC is also under active development; since Spring 2022 when this site went up, it's already gone through two major version changes. Every semester there are changes to be researched and worked around, whereas BUGS hasn't changed much for 15 years. So I understand why the professor stuck with it, even in 2018 when putting this course online.

But there's a tension there between students who are looking to practice career skills—they tend to want to use something Python or R-based. So I've redone most of the course examples in PyMC and provide Python solutions to any homework or exam problems we ask.

Students are welcome to use any PPL for our course. If you're only interested in the underlying theory and don't want to add learning new software to your workload, you might be happiest sticking with OpenBUGS since it has a GUI and you'll be able to pick it up easily.

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

If you want to learn a more stable tool with excellent documentation, try [Stan](https://mc-stan.org/). One of the other TAs is working on creating course examples in Stan now, and I'll link to his repository when they are ready.

If you're really adventurous and want to learn Julia, maybe try [Turing.jl](https://github.com/TuringLang/Turing.jl). If you love trying the absolute latest thing and you want to go into completely uncharted territory for this class, you could look at [AeMCMC](https://github.com/aesara-devs/aemcmc), [Blackjax](https://blackjax-devs.github.io/blackjax/examples/quickstart.html#), [NumPyro](https://github.com/pyro-ppl/numpyro), [Oryx](https://github.com/jax-ml/oryx), [Tensorflow Probability](https://www.tensorflow.org/probability), [Distrax](https://github.com/deepmind/distrax), or go find something I've never heard of (and tell me about it)!

If you redo any of the course examples in a new language I would love to hear about it. Even better, if you host your examples somewhere, let me know and I'll add a link here.

#### A note about BAMBI and other higher-level interfaces

Please be careful if you choose to use interfaces like [BAMBI](https://github.com/bambinos/bambi). These abstraction layers will add an interface on top of a lower-level PPL. BAMBI, for example, will look very familiar to people who've used R's ```glm()``` function for general linear models. It uses PyMC under the hood, but you can specify models like this:

```python
model = bmb.Model("y ~ x1 + x2", data)
fitted = model.fit()
```

These are really cool packages. But students often run into trouble when using them for the homeworks and exams because this simplicity means making a lot of decisions for you. I don't want to discourage anyone from using them, but sometimes it can be useful to explicitly write out each part of the model, especially when learning. There have been past exam questions that weren't possible in BAMBI but were doable in PyMC!

## General purpose programming languages

Most people use Python, but quite a few also use R. MATLAB or Octave work fine for the first half of the course. I've almost never seen them used for the second half. A few students have tried Julia. It's up to you. I'm most comfortable with Python so that's what I'm using for these examples.