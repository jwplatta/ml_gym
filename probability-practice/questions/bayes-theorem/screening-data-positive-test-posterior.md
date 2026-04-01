---
subject: bayes-theorem
difficulty: VERY EASY
quality: GOOD
---
# Screening Data Positive Test Posterior
## Question
A screening program tests for a condition in a population.

|                      | Positive Test (+) | Negative Test (-) | Total |
|----------------------|-------------------|-------------------|-------|
| Condition (C)        | 24                | 6                 | 30    |
| No Condition (¬C)    | 18                | 252               | 270   |
| **Total**            | **42**            | **258**           | **300** |

Use Bayes' theorem to find P(C | +), the probability a person has the condition given that the test was positive.
## Solution
First compute the pieces:

P(+ | C) = 24/30 = 0.80

P(C) = 30/300 = 0.10

P(+) = 42/300 = 0.14

Apply Bayes' theorem:

P(C | +) = (P(+ | C) × P(C)) / P(+)
         = (0.80 × 0.10) / 0.14
         = 0.08 / 0.14
         = 4/7 ≈ 0.571

**Answer:** P(C | +) = 4/7 ≈ 0.571

So a positive test result corresponds to about a 57.1% chance of actually having the condition.
