---
subject: conditional-probability
difficulty: EASY
quality: GOOD
---
# Comparing P(A|B) and P(B|A)
## Question
Given the following contingency table for insurance claims:

|              | Filed Claim (B) | No Claim (¬B) | Total |
|--------------|-----------------|---------------|-------|
| Young Driver (A) | 20          | 30            | 50    |
| Older Driver (¬A) | 10         | 90            | 100   |
| **Total**    | **30**          | **120**       | **150** |

Compute both P(A | B) and P(B | A). Are they equal?
## Solution
P(A | B) = 20/30 = 2/3 ≈ 0.667

P(B | A) = 20/50 = 2/5 = 0.40

**Are they equal?** No, P(A | B) = 0.667 ≠ 0.40 = P(B | A)

**Interpretation:**
- P(A | B) = 0.667 means: Among those who filed claims, 66.7% are young drivers
- P(B | A) = 0.40 means: Among young drivers, 40% filed claims

These answer different questions, so they're generally not equal.
