# Introduction

This repository contains Python translations of the examples from Georgia Tech's online version of [ISYE 6420: Bayesian Statistics](https://www2.isye.gatech.edu/isye6420/), created by Professor Brani Vidakovic and currently taught by Professor Roshan Joseph. Most of the BUGS examples have been ported to [PyMC](https://docs.pymc.io/), except for several Bayesian network problems, which use [pgmpy](https://pgmpy.org/). There are also some miscellaneous MATLAB scripts redone using NumPy.

PyMC often has more than one way to do the same thing. I'm also learning as I go, so these solutions will not be perfect! Everyone is welcome to contribute if you have a better way to code something. You can file an issue on Github, make a post on the class forums, email me, or submit a pull request.

## Future plans

Right now I'm working on redoing the "Codes for Unit X" files from the [Supporting material page](https://www2.isye.gatech.edu/isye6420/supporting.html). The remaining incomplete files are:

### Unit 5

- [ ] Many redundant MATLAB MCMC examples. Not sure if we need to finish them.

### Unit 8

- [ ] ratsinformative.odc model needs to be added to the rats notebook.

### Unit 9

- [ ] haldsvss.odc needs to be added to the Hald notebook.
- [ ] gesell.odc is still incomplete.

### Unit 10

- [ ] growth.odc
- [ ] lister.odc
- [ ] italywines123.odc is working but getting different coefficients than BUGS
- [ ] sunspots.odc AR model is working, but ARMA hasn't been added. PyMC team is working on adding ARMA this summer, so will revisit that later rather than manually coding it.

### Other things to do:

- [ ] Fix markdown table sizes.

- [ ] Add FAQs based on student questions.

- [ ] Add solutions to the optional exercises.

- [ ] Add more explanation/content related to MCMC algorithms
