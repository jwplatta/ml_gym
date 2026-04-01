---
subject: bayes-theorem
difficulty: VERY EASY
quality: GOOD
---
# Basic Bayes' Rule Application
## Question
Given the following contingency table for disease screening:

|              | Positive Test (B) | Negative Test (¬B) | Total |
|--------------|------------------|-------------------|-------|
| Disease (A)  | 90               | 10                | 100   |
| No Disease (¬A) | 50            | 850               | 900   |
| **Total**    | **140**          | **860**           | **1000** |

You know B occurred (test is positive). Use Bayes' rule to find P(A | B) from P(B | A), P(A), and P(B).
## Solution
**Step 1: Calculate components**

P(B | A) = 90/100 = 0.90 (sensitivity)

P(A) = 100/1000 = 0.10 (prevalence)

P(B) = 140/1000 = 0.14

**Step 2: Apply Bayes' rule**

P(A | B) = P(B | A) × P(A) / P(B)
         = (0.90) × (0.10) / (0.14)
         = 0.09 / 0.14
         = 9/14
         ≈ 0.643

**Answer: 9/14 ≈ 0.643 or about 64.3%**

**Interpretation:** If the test is positive, there's a 64% chance of actually having the disease.
