# Introduction

This repository contains Python translations of the examples from Georgia Tech's [ISYE 6420: Bayesian Statistics](https://www2.isye.gatech.edu/isye6420/), created by Professor Brani Vidakovic and currently taught by Professor Roshan Joseph and Head TA Greg Schreiter. It also has additional notes on each lecture.

## Why?

I created this site to address some of the most common student complaints and questions. At the time, the most frequent source of dissatisfaction was the course's use of outdated software, namely WinBUGS/OpenBUGS. So I redid the lecture examples in Python and PyMC.

A close second was the lecture quality—some students said they were too dense, some said they didn't delve deeply enough into the underlying theory, and others said they wanted to see more problems worked out step-by-step. 

I think the main problem with the lectures comes from the professor assuming a bit too much background knowledge for many of us in the program. The course is also a very broad overview, so it's tough to go too deep when covering any individual subject. These two combine to cause another problem, which is that it can be tough to judge the importance of any given bit of information in each lecture.

To help with this, I've added notes that provide context to the lectures and address the most common questions we get about each one. As someone who originally took the class a little light on the necessary math and statistics knowledge, I hope my perspective helps other people coming in with similar backgrounds.

## Site structure

This site was built with [Jupyter Book](https://jupyterbook.org/en/stable/intro.html) and is made up of a combination of Markdown files and Jupyter notebooks. You can download the source for any page in the upper right, or view the entire repository on [Github](https://github.com/areding/6420-pymc). 

All pages match a corresponding lecture on Canvas, except when there are more pages than lectures in a unit, in which case the additional pages will be at the end of the unit. For example, there are only eight lectures in Unit 3 on Canvas. The first eight pages here match the lecture numbers, while the ninth page has a supplementary problem and wasn't part of the original lectures.

Any necessary data will either have a download link or, if the data is compact enough, will be included in the code.

```{warning}
I'm working on converting the site structure to match the lecture numbering. That means right now lots of pages are blank, just placeholders for that lecture. All the pages with code are marked with a star for now so you can find them.
```

## Plans

As of February 2023, I've got most of the lecture examples translated to Python/[PyMC](https://www.pymc.io/welcome.html) and updated to v5. Now I'm working on adding notes and more explanation for each lecture and some of the [supplementary exercises](https://www2.isye.gatech.edu/isye6420/supporting.html).
