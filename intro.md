# Introduction

This repository contains Python translations of the examples from Georgia Tech's online version of [ISYE 6420: Bayesian Statistics](https://www2.isye.gatech.edu/isye6420/), created by Professor Brani Vidakovic and currently taught by Professor Roshan Joseph. Most of the BUGS examples have been ported to [PyMC](https://docs.pymc.io/), except for several Bayesian network problems, which use [pgmpy](https://pgmpy.org/). There are also some miscellaneous MATLAB scripts redone using NumPy.

PyMC often has more than one way to do the same thing. It's also under active development, so things break semi-regularly. I'm also learning as I go, so these solutions will not be perfect! Everyone is welcome to contribute if you have a better way to code something. You can file an issue on Github, make a post on the class forums, email me, or submit a pull request.

I'm also going through and adding links to other related resources that I've found helpful.

## Current progress

Just updated everything to PyMC 5. The remaining incomplete files are:

### Unit 5

- Many redundant MATLAB MCMC examples. Not sure if we need to finish them.

### Unit 9

- cumulative2 example incomplete - right now it's using different methods to look at outliers.

### Unit 10

- growth.odc is working but getting slighty different results
- lister.odc
- italywines123.odc is working but getting different coefficients than BUGS
- sunspots.odc AR model is working, but ARMA hasn't been added.