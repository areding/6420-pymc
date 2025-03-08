# BUGS Examples, Volume 1

This appendix will port the original WinBUGS examples  volumes [1 (mirror)](https://www2.isye.gatech.edu/isyebayes/bank/eg05vol1.pdf) {cite:t}`spiegelhalter1996vol1` and [2 (mirror)](https://www2.isye.gatech.edu/isyebayes/bank/eg05vol2.pdf){cite:t}`spiegelhalter1996vol2` to PyMC. These were included with WinBUGS. To start with, I'm working off the linked versions (0.5) but may update over time if I find a different source.

These models are not tested to the level of a published work. They came with the following disclaimer:

```{warning}
These worked examples illustrate the use of the BUGS language and sampler in a wide range of problems. They contain a number of useful “tricks”, but are certainly not exhaustive of the models that may be analysed.

We emphasise that all the results for these examples have been derived in the most naive way: in general a burn-in of 500 iterations and a single long run of 1000 iterations. This is not recommended as a general technique: no tests of convergence have been carried out, and traces of the estimates have not even been plotted. However, comparisons with published results have been made where possible. Times have been measured on a 60 MHz superSPARC: a 60 MHz Pentium PC appears to be about 4 times slower, and a 30 MHz superSPARC about 2 times slower.

Users are warned to be extremely careful about assuming convergence, especially when using complex models including errors in variables, crossed random effects and intrinsic priors in undirected models.
```

It will be interesting to see what PyMC's convergence diagnostics make of the models.

```{tableofcontents}
```