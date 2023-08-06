# Bayes Networks

Bayes networks or belief networks are a type of directed acyclic graph (DAG) model that represent the probabilistic relationships among a set of variables.

The nodes represent random variables and the edges represent causal relationships between the variables. "Directed" means that the relationships have a direction (from cause to effect), and the acyclic means that it's not possible to start at one node and follow a sequence of edges that leads back to the starting node.

When we get new evidence (when an unobserved node becomes observed), we update the probabilities throughout the network. This process is called inference. There are various algorithms to perform efficient inference, both exact and sampled. We won't go into them much in this course. The professor uses OpenBUGS in the next lecture, while I've chosen to use Pgmpy. I think with the new pm.Categorical class, it would be fairly easy to redo these in PyMC, but I haven't made it a priority yet.