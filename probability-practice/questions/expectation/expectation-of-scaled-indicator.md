---
subject: expectation
difficulty: VERY EASY
quality: GOOD
---
# Expectation of Scaled Indicator
## Question
Given the following contingency table for product sales:

|              | Premium (B) | Standard (¬B) | Total |
|--------------|-------------|---------------|-------|
| Corporate (A) | 60         | 40            | 100   |
| Individual (¬A) | 20        | 80            | 100   |
| **Total**    | **80**      | **120**       | **200** |

Let Y be a random variable that equals 10 if B occurs (premium sale) and 0 otherwise. Compute E[Y].
## Solution
Y = 10 with probability P(B) = 80/200 = 2/5 = 0.40

Y = 0 with probability P(¬B) = 120/200 = 3/5 = 0.60

E[Y] = 10 × (0.40) + 0 × (0.60)
     = 4 + 0
     = 4

**Answer: 4**

**Interpretation:** On average, each sale generates an expected value of 4 from the premium indicator (10 points if premium, 0 otherwise).
