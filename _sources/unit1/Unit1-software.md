# 1.3: Software

## Probabilistic Programming Languages (PPLs)

As the professor says, [BUGS](https://www.mrc-bsu.cam.ac.uk/software/bugs/) (Bayesian Inference using Gibbs Sampling) is actually a pretty good choice for learning the basics of Bayesian inference. There are things that BUGS can do that are still a pain to implement in PyMC. PyMC is also under active development - since Spring 2022 when this site went up, it's already gone through two major version changes (3 to 5). Features I was using for this class are being deprecated! Every semester there's some breaking change to be researched and worked around. Whereas BUGS probably hasn't changed for 15 years. So I understand why the professor stuck with it, even in 2018 when putting this course online.

But there's a tension there between students who are looking to practice career skills - they tend to want to use something Python or R-based. So I've redone most of the course examples in PyMC and provide Python solutions to any homework or exam problems we ask.

Students are welcome to use any PPL for our course. If you're only interested in the underlying theory and don't want to add learning new software to your workload, you might be happiest sticking with OpenBUGS since it has a GUI and you'll be able to pick it up easily. If you want something a little more challenging and are comfortable with or interested in learning Python, try [PyMC](https://www.pymc.io/welcome.html). If you want to learn a more stable tool with excellent documentation, try [Stan](https://mc-stan.org/). We have a TA working on creating course examples in Stan now.

If you're really adventurous, maybe try [Turing.jl](https://github.com/TuringLang/Turing.jl). If you're one of those people who needs to try the absolute latest thing and you want to go into completely uncharted territory for this class, try [AeMCMC](https://github.com/aesara-devs/aemcmc), [NumPyro](https://github.com/pyro-ppl/numpyro), [Oryx](https://github.com/jax-ml/oryx), [Tensorflow Probability](https://www.tensorflow.org/probability), or go find something I've never heard of!

## General Purpose Programming Languages

MATLAB or Octave work fine for the first half of the course. I've never seen them used for the second half. Most people use Python, but quite a few also use R. I've seen a few students try Julia. It's up to you. I'm most comfortable with Python so that's what I'm using for these examples.