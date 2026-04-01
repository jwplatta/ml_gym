---
subject: expectation
difficulty: VERY EASY
quality: GOOD
---
# Expectation of Indicator Variable
## Question
Given the following contingency table for customer churn:

|              | Churned (B) | Retained (¬B) | Total |
|--------------|-------------|---------------|-------|
| Unhappy (A)  | 40          | 10            | 50    |
| Happy (¬A)   | 10          | 90            | 100   |
| **Total**    | **50**      | **100**       | **150** |

Let X be an indicator variable for event A (X=1 if customer is unhappy, X=0 otherwise). Compute E[X].
## Solution
X = 1 with probability P(A) = 50/150 = 1/3

X = 0 with probability P(¬A) = 100/150 = 2/3

E[X] = 1 × P(A) + 0 × P(¬A)
     = 1 × (1/3) + 0 × (2/3)
     = 1/3
     ≈ 0.333

**Answer: 1/3 ≈ 0.333**

**Key insight:** The expected value of an indicator variable equals the probability of the event. E[indicator of A] = P(A).
