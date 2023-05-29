# Conditioning, Part 1

## The queen of spades

Professor Vidakovic uses this example to demonstrate the concept of independence. Remember, by definition, independence means $P(AB) = P(A)P(B)$. Here we have a standard deck of 52 cards. There are 13 of each suit and 4 queens. Define Event A as drawing a spade and Event B as drawing a queen. $P(AB)$ is then the probability of drawing the queen of spades. This card is unique, so it occurs $1/52$ times.

If we multiply it out:

$$P(A)P(B) = \frac{13}{52} \times \frac{4}{52} = \frac{1}{52}$$

So $P(AB) = P(A)P(B)$ and the two events are independent.

But are they still independent if we first remove the two of diamonds from the deck? Let's see:


$$P(AB) = \frac{1}{51}$$
$$P(AB) = P(A)P(B) = \frac{13}{51} \times \frac{4}{51} = \frac{52}{2601}$$
$$ \frac{1}{51} \neq \frac{52}{2601}$$

They are no longer independent! It's easy to follow the math, but the intuition can take time to click. Think about it in terms of the information you have. If there are an equal number of cards left in the deck from each suit, any given suit has the same probability of being a queen.

In the second case, if you draw a spade, heart, or club, the probability your card is a queen will be different than the probability of a queen given that you drew a diamond. You have slightly more information about diamonds since there are only 12 remaining in the deck.

So now depending on the suit, a queen might be more likely. In other words, the probability of a queen is no longer independent of the suit.


## Causal independence vs. logical independence

```{epigraph}
Quite generally, as the robot’s state of knowledge represented by H and X changes, probabilities conditional on them may change from independent to dependent or vice versa; yet the real properties of the events remain the same. Then one who attributed the property of dependence or independence to the events would be, in effect, claiming for the robot the power of psychokinesis. We must be vigilant against this confusion between reality and a state of knowledge about reality, which we have called the ‘mind projection fallacy’.

-- {cite:t}`jaynes2003` p. 92
```

Some students have gotten really hung up on this example in past semesters. I think it may be useful to distinguish between physical, causal independence and logical independence. The suit of a card does not physically affect or cause any change in the probability of a queen. Neither does removing the two of diamonds, except for the fact that there are fewer cards to draw from. What we're talking about here is logical independence, which is reflected in the state of our knowledge about the cards.