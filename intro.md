# Introduction

This repository contains Python translations of the examples from Georgia Tech's [ISYE 6420: Bayesian Statistics](https://www2.isye.gatech.edu/isye6420/), created by Professor Brani Vidakovic and currently taught by Professor Roshan Joseph and Head TA Greg Schreiter. I'm also going to slowly add my notes for each lecture.

## Why?

During my second semester as a TA, I created this site to address the most common student complaints and questions. At the time, the most frequent grievance centered on the course's use of outdated software, namely WinBUGS/OpenBUGS. A close second was the lectures—some students said they were too dense, some said they didn't delve deeply enough into the underlying theory, and still others said they wanted to see more step-by-step examples of problems like the homework worked out.

As someone who originally took the class a little light on the necessary math and statistics knowledge, I hope my perspective helps other people coming in with similar backgrounds.

## Site structure

This site was built with [Jupyter Book](https://jupyterbook.org/en/stable/intro.html) and is made up of a combination of Markdown files and Jupyter notebooks. You can download the source for any page in the upper right, or view the entire repository on [Github](https://github.com/areding/6420-pymc). It mostly follows the [original course outline](https://www2.isye.gatech.edu/isye6420/plan.html). Each example lists the corresponding lecture video and contains a download link to the original code file(s). Any necessary data will either have a download link or, if the data is compact enough, will be included in the code.

I plan on adding notes for each lecture that will expand over time. This will include correcting any mistakes made in the lecture slides. These notes are not necessarily complete learning resources—for the most part, they're meant to supplement the lectures, not replace them.

```{warning}
I'm working on converting the site structure to match the lecture numbering. That means right now lots of pages are blank, just placeholders for that lecture. All the pages with code are marked with a star for now so you can find them.
```

## Plans

As of February 2023, I've got most of the lecture examples translated to Python/[PyMC](https://www.pymc.io/welcome.html) and updated to v5. Now I'm working on adding notes and more explanation for each lecture and the [supplementary exercises](https://www2.isye.gatech.edu/isye6420/supporting.html).