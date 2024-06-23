# About This Course

The course was originally developed at Georgia Tech in 2004 by Professor Brani Vidakovic, who is now the head of the [Texas A&M Department of Statistics](https://science.tamu.edu/news/2020/07/branislav-vidakovic-named-head-of-texas-am-statistics/). Prof. Vidakovic also wrote the textbook [*Engineering Biostatistics*](https://statbook.gatech.edu/index.html)). That's why many of the examples in the course reference medical and biological research. Don't worry—the methods are broadly applicable. We'll reference this book often in the course, often as "The Statbook."

:::{seealso}
Professor Vidakovic's [publication history](https://scholar.google.com/citations?user=mjLdzMAAAAAJ).

[Professor Joseph's.](https://scholar.google.com/citations?hl=en&user=-XDlRfAAAAAJ)
:::

This site mostly follows the original [course outline](https://www2.isye.gatech.edu/isye6420/plan.html). Each example lists the corresponding lecture video and contains a download link to the original code file(s). Any necessary data will either have a download link or, if the data is compact enough, will be included in the code.

(content:other_resources)=
## Other recommended resources

These are not required for the class, but they might be helpful. Prof. Vidakovic's lectures often assume that the student has a certain amount of background knowledge, so if you feel lost, or just want to dive deeper into the subject, check them out.

### Textbooks and courses

- [*Statistical Rethinking*](https://xcelab.net/rm/statistical-rethinking/) by Richard McElreath is a great book for gaining intuition about Bayesian inference and modeling in general. It's aimed at non-statisticians, so I find it more accessible.

- [*Bayesian Modeling and Computation in Python*](https://bayesiancomputationbook.com/welcome.html) by Osvaldo Martin, Ravin Kumar, and Junpeng Lao, as you might guess from the title, has a more computational perspective. All three co-authors are contributors to PyMC. This book is freely available online. If you've taken [ISYE 8803: HDDA](https://omscs.gatech.edu/isye-8803-topics-high-dimensional-data-analytics), you might enjoy Chapter 5: Splines. Chapter 7: Bayesian Additive Regression Trees are another cool model type that we don't cover in this class, but might make for a fun project topic. Chapter 10 is an overview of creating a probabilistic programming language. Not that you need to create one for this class—it, along with Unit 5 of our class, just might help you understand more about what's going on under the hood in these languages.

- [*Bayesian Data Analysis*](http://www.stat.columbia.edu/~gelman/book/) by Gelman, Carlin, Stern, Dunson, Vehtari, and Rubin goes into more mathematical theory than *Statistical Rethinking*. I mostly use it as a reference. It's freely available on the linked site.

- *The Bayesian Choice* by Christian P. Robert is referenced several times in the course materials, so if you're looking for more info on some weird derivation that the professor didn't explain, check it out. Available as a PDF to GT students through [Springer](https://link.springer.com/book/10.1007/0-387-71599-1).

- *Probability Theory: The Logic of Science* by E.T. Jaynes is a classic that builds up to Bayesian inference from logical first principles. I usually dip into it when students ask more philosophical questions.

- [*Probabilistic Machine Learning: An Introduction*](https://probml.github.io/pml-book/) by Kevin P. Murphy is one I haven't looked at too much yet. It seems incredibly broad, containing just about everything we've got in this class along with half the OMSA program, all viewed through a probabilistic and decision theoretical lense.

### Blogs

- Andrew Gelman, author of *Bayesian Data Analysis* (above), has a blog: [Statistical Modeling, Causal Inference, and Social Science](https://statmodeling.stat.columbia.edu/).
- [Dan Simpson](https://dpsimpson.github.io/), one of the maintainers of the [Stan PPL](https://mc-stan.org/), has a blog called [Un garçon pas comme les autres (Bayes)](https://dansblog.netlify.app/) with opinionated and funny deep dives into various Bayesian topics. Warning: NSFW language.
- [Count Bayesie: Probably a probability blog](https://www.countbayesie.com/) by Will Kurt.
- Michael Betancourt, another Stan developer, has a [series of incredibly in-depth](https://betanalpha.github.io/writing/) posts and notebooks on Bayesian modeling.
- PyMC developer [Austin Rochford's blog](https://austinrochford.com/posts.html) has a lot of good posts.
- Another PyMC developer, [Oriol Abril](https://oriolabrilpla.cat/blog/), posts some really helpful PyMC examples.
- If you're interested in how ideas from the course might be used in a business context, you might enjoy the posts on the [PyMC Labs blog](https://www.pymc-labs.io/blog-posts/).


### Videos and podcasts

- [Learn Bayes Stats](https://learnbayesstats.com/) by Alex Andorra, one of the PyMC developers.
- [Bayesian Statistics](https://www.youtube.com/watch?v=-1dYY43DRMA&list=PLvcbYUQ5t0UEkf2NUEo7XSsyVTyeEk3Gq) by ritvikmath. Very accessible playlist of videos on a variety of Bayesian topics.
- [3blue1brown](https://www.youtube.com/playlist?list=PLnDGnVHTlzsNJc6WHxYnF-vpSxrEehhTA) has a few videos on probability and Bayes' Rule. His video on Bayes factors is really helpful for this class.

### Other

- I don't use Stan at all, but I still reference the [Stan User's Guide](https://mc-stan.org/docs/2_29/stan-users-guide/index.html) often.