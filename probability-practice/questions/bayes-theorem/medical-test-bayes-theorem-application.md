---
subject: bayes-theorem
difficulty: VERY EASY
quality: GOOD
---
# Medical Test - Bayes Theorem Application
## Question
Given the following contingency table representing a medical test for a disease:

|                | Test + (B) | Test - (¬B) | Total |
|----------------|------------|-------------|-------|
| Disease (A)    | 90         | 10          | 100   |
| No Disease (¬A) | 50        | 850         | 900   |
| **Total**      | **140**    | **860**     | **1000** |

If a patient tests positive (B), what is the probability they actually have the disease (A)? Use Bayes' theorem to find P(A | B).
## Solution
**Direct method:**
P(A | B) = 90/140 = 9/14 ≈ 0.643

**Using Bayes' theorem:**
P(A | B) = P(B | A) × P(A) / P(B)

Where:
- P(B | A) = 90/100 = 0.90 (sensitivity)
- P(A) = 100/1000 = 0.10 (prevalence)
- P(B) = 140/1000 = 0.14

Therefore:
P(A | B) = (0.90 × 0.10) / 0.14 = 0.09 / 0.14 = 9/14 ≈ 0.643

**Answer: 9/14 ≈ 0.643 or about 64.3%**

This is the positive predictive value (PPV) of the test.
