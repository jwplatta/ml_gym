---
subject: bayes-theorem
difficulty: EASY
quality: GOOD
---
# Weather and Commute Time
## Question
Your commute time depends on the weather. Historical data shows:
- P(Rain) = 0.3
- P(No Rain) = 0.7

Your commute is "Long" (over 45 minutes) with probabilities:
- P(Long Commute | Rain) = 0.6
- P(Long Commute | No Rain) = 0.2

**Questions:**
1. What is the probability that you have a long commute on any given day?
2. If you had a long commute today, what is the probability that it rained?
3. If you had a short commute today, what is the probability that it didn't rain?
## Solution
**Part 1: Probability of long commute**

Using the law of total probability:

P(Long) = P(Long | Rain) × P(Rain) + P(Long | No Rain) × P(No Rain)

P(Long) = (0.6)(0.3) + (0.2)(0.7)

P(Long) = 0.18 + 0.14 = 0.32

**Answer: 0.32 or 32%**

**Part 2: Probability it rained given long commute**

Using Bayes' theorem:

P(Rain | Long) = P(Long | Rain) × P(Rain) / P(Long)

P(Rain | Long) = (0.6)(0.3) / 0.32

P(Rain | Long) = 0.18 / 0.32 = 9/16 = 0.5625

**Answer: 9/16 = 0.5625 or 56.25%**

**Part 3: Probability it didn't rain given short commute**

First, find the conditional probabilities for short commute:
- P(Short | Rain) = 1 - P(Long | Rain) = 1 - 0.6 = 0.4
- P(Short | No Rain) = 1 - P(Long | No Rain) = 1 - 0.2 = 0.8

Then, find P(Short):

P(Short) = P(Short | Rain) × P(Rain) + P(Short | No Rain) × P(No Rain)

P(Short) = (0.4)(0.3) + (0.8)(0.7) = 0.12 + 0.56 = 0.68

Finally, apply Bayes' theorem:

P(No Rain | Short) = P(Short | No Rain) × P(No Rain) / P(Short)

P(No Rain | Short) = (0.8)(0.7) / 0.68 = 0.56 / 0.68 = 14/17 ≈ 0.824

**Answer: 14/17 ≈ 0.824 or about 82.4%**

**Interpretation:** A short commute is good evidence it didn't rain (82% probability), while a long commute is moderate evidence it rained (56% probability). This asymmetry occurs because rain strongly increases commute time, but other factors can also cause long commutes.
