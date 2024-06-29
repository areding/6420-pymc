# 1. Introduction to Hierarchical Models

Contributed by [Amanuel Anteneh](https://github.com/amanuelanteneh).

In his introductory textbook *A Student’s Guide to Bayesian Statistics* {cite:t}`lambert2018student` Ben Lambert provides a great introduction to the concept of hierarchial models with an example. We will go over a modified version of this example here.
Hierarchical models can be seen as a compromise between two other types of models. The first is what Lambert calls 'fully pooled' models and the second are called 'heterogenous' models. Let's look to a specific example to compare and contrast the two models. 

## Fully pooled versus heterogenous models

Imagine that we are in the state of Georgia and are analyzing math SAT test scores from 100 schools in the state. For each school we have the scores for $N$ randomly selected senior students. Suppose we want to estimate the average SAT score of a randomly chosen senior student from Georgia. 

### Fully pooled model
For this model we simply ignore what school each score came from and aggregate or 'pool' all the data together.
After looking at a plot of the pooled data we decide to model the scores as being normally distributed 

$$
S_{ij} \sim \mathcal{N}(\mu, \sigma^2)
$$

with average $\mu$ and variance $\sigma^2$ 
where $S_{ij}$ denotes the test score of student $i$ who attends school $j$. While this method does yield the quantity we are after (the average score of a randomly chosen senior from the state of Georgia) it arrives at this answer without adequately accounting for the variation of scores *between schools*. Therefore it's likely that our posterior distribution is far too narrow. In the example Lambert gives he shows this to be the case using a posterior predictive check.

### Heterogenous model
After recognizing the disadvantages of simply pooling the data we decide to try to take the inter-school variation into account in our model. To do this we decide to use a model that estimates a separate average and variance for each school

$$
S_{ij} \sim \mathcal{N}(\mu_j, \sigma^2_j)
$$ 

where $\mu_j$ and $ \sigma^2_j$ are the estimated average and variance for school $j$. While this model will certainly take the inter-school variation into account the disadvantage is that it's not clear how we can get an estimate for the average SAT score at the state level which is what we were after in the first place.

## Hierarchical model
Hierarchical models can be seen as a middle ground between these two models. The pooled model does not fully take the inter-school variation into account and this is not realistic since there are certainly differences between schools that can effect student test scores such as the amount of funding the school receives. The heterogenous model does capture the variation of scores for each school but it treats each school as independent from all the others. This is not realistic either since there should be some relation between the schools given that they are all in the state of Georgia which has it's own Department of Education which determines certain state-wide public school polices. Hierarchical models allow us to build in this relation between schools while also accounting for inter-school score variation. 

For the case of the Georgia schools we can decide that the average score $\mu_j$ for school $j$ is drawn from a state level distribution of averages 

$$
\mu_j \sim \mathcal{N}(\bar{\mu}, \bar{\sigma^2})
$$

and put a non-informative prior on the variance of scores for school $j$

$$
\sigma_j^2 \sim \text{InverseGa}(0.001, 0.001).
$$

Here $\bar{\mu}$ is the average of the average test scores across all of the schools in Georgia and $\bar{\sigma}^2$ is the variance of the school averages around $\bar{\mu}$ and we can place non-informative priors on them

$$ 
\bar{\mu} \sim \mathcal{N}(1000, 10), \quad \bar{\sigma}^2 \sim \text{InverseGa}(0.001, 0.001). 
$$

This model allows us to capture the fact that the average test scores for schools are related to each other in some way while also taking into account that there will be variations in the average test scores between schools. Note that we set the mean of the normal distribution for $\bar{\mu}$ to be 1000 since the range of SAT test scores is $[400,1600]$.  

## Non-spatially separated groups
In the above example our data come in groups (the schools from Georgia) that are separated spatially however the groups that our data come in need not only be separated spatially. These groups can also be separated temporally such as the case from Gelfand et al (1990) we will cover later in this section or spatio-temporally in the case of a meta-analysis of different studies.