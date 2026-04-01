---
subject: probability-axioms
difficulty: EASY
quality: AVERAGE
---
# Probability Axioms Question 2
## Question
A casino offers a simple card game. There are {{random_int(min_val=36, max_val=52)}} cards in a deck with {{random_int(min_val=2, max_val=4)}} cards for each value. Each time the cards are thoroughly shuffled (so each card has equal probability of being selected). You pick up a card from the deck and the dealer picks another one without replacement. If you have a larger number, you win; if the numbers are equal or yours is smaller, the house wins—as in all other casinos, the house always has better odds of winning. What is your probability of winning?
Hint: What are the possible results (events) if we compare the number of heads in A's first n coins with B's in coins? By making the number of coins equal, we can take advantage of symmetry. For each event, what will happen if A's last coin is a head? Or a tail?
## Solution
One answer to this problem is to consider all 13 different outcomes of your card. The card can have a value 2, 3, ..., A and each has 1/13 of probability. With a value of 2, the probability of winning is 0/51; with a value of 3, the probability of winning is 4/51 (when the dealer picks a 2); ...; with a value of A, the probability of winning is 48/51 (when the dealer picks a 2, 3, ..., or K). So your probability of winning is

(1/13) x (0/51 + 4/51 + ··· + 48/51)
= (4 / (13 x 51)) x (0 + 1 + ··· + 12)
= (4 / (13 x 51)) x (12 x 13 / 2)
= 8/17.

Although, this is a straightforward solution and it elegantly uses the sum of an integer sequence, it is not the most efficient way to solve the problem. If you have got the core spirits of the coin tossing problem, you may approach the problem by considering three different outcomes:

E₁: Your card has a number larger than the dealer's;
E₂: Your card has a number equal to the dealer's;
E₃: Your card has a number lower than the dealer's.

Again by symmetry, P(E₁) = P(E₃). So we only need to figure out P(E₂), the probability that two cards have equal value. Let's say you have randomly selected a card. Among the remaining 51 cards, only 3 cards will have the same value as your card. So the probability that the two cards have equal value is 3/51. As a result, the probability that you win is

P(E₁) = (1 - P(E₂)) / 2 = (1 - 3/51) / 2 = 8/17.
