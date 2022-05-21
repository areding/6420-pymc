#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# for colab
get_ipython().run_line_magic('pip', 'install pgmpy')


# In[1]:


import matplotlib.pyplot as plt
import networkx as nx
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import CausalInference
from pgmpy.models import BayesianNetwork


# # Alarm
# From [Codes for Unit 3](https://www2.isye.gatech.edu/isye6420/supporting.html).
# 
# Associated lecture videos: Unit 3 [Lesson 7](https://www.youtube.com/watch?v=IbHOo6ifJYE&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=16) and [Lesson 8](https://www.youtube.com/watch?v=iVFycPG26OQ&list=PLv0FeK5oXK4l-RdT6DWJj0_upJOG2WKNO&index=17).
# 
# *Your house has an alarm system against burglary. The house is located in the seismically active area and the alarm system can get occasionally set off by an earthquake. You have two neighbors, Mary and John, who do not know each other. If they hear the alarm they call you, but this is not guaranteed. They also call you from time to time just to chat. The BUGS code provides an approximate solution for conditional  distributions of nodes given the evidence.*
# 
# *1. Find the probability John calls given an earthquake.*
# 
# *2. Find the probability that there was an earthquake given John has called.*
# 
# *3. Find the probability of an earthquake given John has not called and Mary has called.*
# 
# *Practice: Find the probability that there was a burglary given an alarm has gone off and Mary has not called.*
# 
# Based on the example at https://pgmpy.org/examples/Earthquake.html, which is almost the exact same problem.

# In[2]:


# Defining network structure
alarm_model = BayesianNetwork(
    [
        ("Burglary", "Alarm"),
        ("Earthquake", "Alarm"),
        ("Alarm", "JohnCalls"),
        ("Alarm", "MaryCalls"),
    ]
)

# Defining the parameters
cpd_burglary = TabularCPD(
    variable="Burglary", variable_card=2, values=[[0.999], [0.001]]
)

cpd_earthquake = TabularCPD(
    variable="Earthquake", variable_card=2, values=[[0.998], [0.002]]
)

cpd_alarm = TabularCPD(
    variable="Alarm",
    variable_card=2,
    values=[[0.999, 0.71, 0.06, 0.05], [0.001, 0.29, 0.94, 0.95]],
    evidence=["Burglary", "Earthquake"],
    evidence_card=[2, 2],
)

cpd_marycalls = TabularCPD(
    variable="MaryCalls",
    variable_card=2,
    values=[[0.99, 0.30], [0.01, 0.70]],
    evidence=["Alarm"],
    evidence_card=[2],
)

cpd_johncalls = TabularCPD(
    variable="JohnCalls",
    variable_card=2,
    values=[[0.95, 0.1], [0.05, 0.9]],
    evidence=["Alarm"],
    evidence_card=[2],
)

# Associating the parameters with the model structure
alarm_model.add_cpds(
    cpd_burglary, cpd_earthquake, cpd_alarm, cpd_johncalls, cpd_marycalls
)

alarm_model.check_model()

print(f"Nodes: {alarm_model.nodes()}")
print(f"Edges: {alarm_model.edges()}")


# In[3]:


# plot the network

options = {
    "arrowsize": 40,
    "font_size": 8,
    "font_weight": "bold",
    "node_size": 4000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 2,
    "width": 5,
    "alpha": 0.9,
}

nx.draw(alarm_model, with_labels=True, **options)

# Set margins for the axes so that nodes aren't clipped
ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()


# In[4]:


alarm_infer = CausalInference(alarm_model)

# probability John calls given an earthquake.
q = alarm_infer.query(variables=["JohnCalls"], evidence={"Earthquake": True})
print("P(J|E):")
print(q)

# probability that there was an earthquake given John has called.
q = alarm_infer.query(variables=["Earthquake"], evidence={"JohnCalls": True})
print("P(E|J):")
print(q)

# probability of an earthquake given John has not called and Mary has called.
q = alarm_infer.query(
    variables=["Earthquake"], evidence={"JohnCalls": False, "MaryCalls": True}
)
print("P(E|J^c, M):")
print(q)

# probability of a burglary given an alarm and that Mary has not called.
q = alarm_infer.query(
    variables=["Burglary"], evidence={"Alarm": True, "MaryCalls": False}
)
print("P(B|A, M^c):")
print(q)


# ## Practice Midterm, Question 1
# 
# From [this practice midterm](https://www2.isye.gatech.edu/isye6420/Bank/MidtermFall2019.pdf).
# 
# **Emily, Car, Stock Market, Sweepstakes, Vacation and Bayes.** 
# 
# *Emily is taking Bayesian Analysis course. She believes she will get an A with probability 0.6, a B with probability 0.3, and a C or less with probability 0.1. At the end of semester she will get a car as a present form her (very) rich uncle depending on her class performance. For getting an A in the course Emily will get a car with probability 0.8, for B with probability 0.5, and for anything less than B, she will get a car with probability of 0.2. These are the probabilities if the market is bullish. If the market is bearish, the uncle is less likely to make expensive presents, and the above probabilities are 0.5, 0.3, and 0.1, respectively. The probabilities of bullish and bearish market are equal, 0.5 each. If Emily gets a car, she would travel to Redington Shores with probability 0.7, or stay on campus with probability 0.3. If she does not get a car, these two probabilities are 0.2 and 0.8, respectively. Independently, Emily may be a lucky winner of a sweepstake lottery for a free air ticket and vacation in hotel Sol at Redington Shores. The chance to win the sweepstake is 0.001, but if Emily wins, she will go to vacation with probability of 0.99, irrespective of what happened with the car.*
# 
# *After the semester was over you learned that Emily is at Redington Shores.*
# 
# *(a) What is the probability that she got a car?*
# 
# *(b) What is the probability that she won the sweepstakes?*
# 
# *(c) What is the probability that she got a B in the course?*
# 
# *(d) What is the probability that the market was bearish?*
# 
# *Hint: You can solve this problem by any of the 3 ways: (i) use of WinBUGS or OpenBUGS, (ii) direct simulation using Octave/MATLAB, R, or Python, and (iii) exact calculation. Use just one of the three ways to solve it. WinBUGS/OpenBUGS or direct simulation are recommended. The exact solution, although straightforward, may be quite messy.*
# 
# ----------------
# 
# This is a bit more complicated than the alarm example, but still pretty easy with pgmpy. The only tricky part is making sure you've entered everything in the correct order.
# 

# When defining variables in pgmpy, the columns are evidence, the rows are the states of the variable. The order you enter evidence matters. See the comments above the ```cpd_car``` and ```cpd_vacation``` variables. I'm going to use the ```state_names``` parameter of ```TabularCPD()``` to help keep track of what's going on here. 

# In[5]:


# Defining network structure
emily_model = BayesianNetwork(
    [
        ("Grade", "Car"),
        ("Car", "Vacation"),
        ("Sweepstakes", "Vacation"),
        ("Market", "Car"),
    ]
)

# Defining the variables
cpd_market = TabularCPD(
    variable="Market",
    variable_card=2,
    values=[[0.5], [0.5]],
    state_names={"Market": ["Bull", "Bear"]},
)

cpd_grade = TabularCPD(
    variable="Grade",
    variable_card=3,
    values=[[0.6], [0.3], [0.1]],
    state_names={"Grade": ["A", "B", "C"]},
)

#    Car variable
#    +---------+---------+---------+---------+---------+---------+---------+
#    | Market  | Bull    | Bull    | Bull    | Bear    | Bear    | Bear    |
#    +---------+---------+---------+---------+---------+---------+---------+
#    | Grade   | A       | B       | C       | A       | B       | C       |
#    +---------+---------+---------+---------+---------+---------+---------+
#    | Car     | 0.8     | 0.5     | 0.2     | 0.5     | 0.3     | 0.1     |
#    +---------+---------+---------+---------+---------+---------+---------+
#    | No car  | 0.2     | 0.5     | 0.8     | 0.5     | 0.7     | 0.9     |
#    +---------+---------+---------+---------+---------+---------+---------+

cpd_car = TabularCPD(
    variable="Car",
    variable_card=2,  # there are two possible outcomes, car or no car
    values=[
        [0.8, 0.5, 0.2, 0.5, 0.3, 0.1],  # car
        [0.2, 0.5, 0.8, 0.5, 0.7, 0.9],  # no car
    ],
    evidence=["Market", "Grade"],
    evidence_card=[2, 3],  # 2 possible states for the market, 3 for grade
    state_names={
        "Market": ["Bull", "Bear"],
        "Grade": ["A", "B", "C"],
        "Car": ["Yes", "No"],
    },
)

cpd_sweepstakes = TabularCPD(
    variable="Sweepstakes",
    variable_card=2,
    values=[[0.001], [0.999]],
    state_names={"Sweepstakes": ["Win", "Lose"]},
)

#    +----------------+---------+---------+---------+---------+
#    | Sweepstakes    | Win     | Win     | Lose    | Lose    |
#    +----------------+---------+---------+---------+---------+
#    | Car            | Yes     | No      | Yes     | No      |
#    +----------------+---------+---------+---------+---------+
#    | Vacation (yes) | 0.99    | 0.99    | 0.7     | 0.2     |
#    +----------------+---------+---------+---------+---------+
#    | Vacation (no)  | 0.01    | 0.01    | 0.3     | 0.8     |
#    +----------------+---------+---------+---------+---------+

cpd_vacation = TabularCPD(
    variable="Vacation",
    variable_card=2,
    values=[
        [0.99, 0.99, 0.7, 0.2],  # vacation
        [0.01, 0.01, 0.3, 0.8],  # no vacation
    ],
    evidence=["Sweepstakes", "Car"],
    evidence_card=[2, 2],
    state_names={
        "Sweepstakes": ["Win", "Lose"],
        "Car": ["Yes", "No"],
        "Vacation": ["Yes", "No"],
    },
)

# Associating the parameters with the model structure
emily_model.add_cpds(cpd_market, cpd_grade, cpd_car, cpd_sweepstakes, cpd_vacation)

emily_model.check_model()

print(f"Nodes: {emily_model.nodes()}")
print(f"Edges: {emily_model.edges()}")


# In[6]:


# plot the network

options = {
    "arrowsize": 40,
    "font_size": 8,
    "font_weight": "bold",
    "node_size": 4000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 2,
    "width": 5,
    "alpha": 0.9,
}

nx.draw(emily_model, with_labels=True, **options)

# Set margins for the axes so that nodes aren't clipped
ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()


# If the above network makes sense, we're good to go! Remember, we know Emily did go to Redington Shores for her vacation, so everything is conditional on that.

# In[7]:


emily_infer = CausalInference(emily_model)

evidence = {"Vacation": "Yes"}

# a: probability Emily got a car.
q = emily_infer.query(variables=["Car"], evidence=evidence)
print("P(C|V):")
print(q)

# b: probability she won the sweepstakes.
q = emily_infer.query(variables=["Sweepstakes"], evidence=evidence)
print("P(SS|V):")
print(q)

# c: probability she got a B.
q = emily_infer.query(variables=["Grade"], evidence=evidence)
print("P(G|V):")
print(q)

# d: probability the stock market was bearish
q = emily_infer.query(variables=["Market"], evidence=evidence)
print("P(SM|V):")
print(q)

