---
subject: expectation
difficulty: EASY
quality: GOOD
---
# Linearity of Expectation
## Question
Given the following contingency table for employee benefits:

|              | Health Plan (B) | No Health Plan (¬B) | Total |
|--------------|-----------------|---------------------|-------|
| Full-time (A) | 70             | 10                  | 80    |
| Part-time (¬A) | 10            | 10                  | 20    |
| **Total**    | **80**          | **20**              | **100** |

Let X and Y be indicator variables for events A and B respectively. Compute E[X + Y] using linearity of expectation.
## Solution
E[X] = P(A) = 80/100 = 0.80

E[Y] = P(B) = 80/100 = 0.80

By linearity of expectation:

E[X + Y] = E[X] + E[Y]
         = 0.80 + 0.80
         = 1.60

**Answer: 1.60**

**Key Property:** Linearity of expectation holds for **any** random variables, even if they're dependent! We didn't need to check whether A and B are independent.
