# Introduction

This repository contains Python translations of the examples from Georgia Tech's online version of [ISYE 6420: Bayesian Statistics](https://www2.isye.gatech.edu/isye6420/), created by Professor Brani Vidakovic and currently taught by Professor Roshan Joseph. Most of the BUGS examples have been ported to [PyMC](https://docs.pymc.io/), except for several Bayesian network problems, which use [pgmpy](https://pgmpy.org/). There are also some miscellaneous MATLAB scripts redone using NumPy.

PyMC often has more than one way to do the same thing. I'm also learning as I go, so these solutions will not be perfect! Everyone is welcome to contribute if you have a better way to code something. You can file an issue on Github, make a post on the class forums, email me, or submit a pull request.

I'm also going through and adding links to other related resources that I've found helpful.

## Current progress

Right now I'm working on redoing the "Codes for Unit X" files from the [supporting material page](https://www2.isye.gatech.edu/isye6420/supporting.html). For this first pass, I'm mostly just recreating the models as closely as possible to the professor's original examples, vectorizing them where possible. Eventually, I'd like to go through and update them with current best practices, because PyMC complains about a lot of these models and some reparameterization could help. Prior and posterior predictive checks, which were barely talked about in the original course, could help guide the reparameterizations.

The remaining incomplete files are:

### Unit 5

- Many redundant MATLAB MCMC examples. Not sure if we need to finish them.

### Unit 8

- ratsinformative.odc model needs to be added to the rats notebook.

### Unit 10

- growth.odc
- lister.odc
- italywines123.odc is working but getting different coefficients than BUGS
- sunspots.odc AR model is working, but ARMA hasn't been added. PyMC team is working on adding ARMA this summer, so will revisit that later rather than manually coding it.

## Future plans

- Update model parameterizations, add posterior/prior predictive checks, more plotting.
- Fix markdown table sizes.
- Add FAQs.
- Add solutions to the optional exercises.
- Add more explanation/content related to MCMC algorithms
- add Unit 11, with next steps and links to further reading
