---
subject: bayes-theorem
difficulty: EASY
quality: GOOD
---
# Verifying Bayes' Rule
## Question
Given the following contingency table for customer behavior:

|              | Purchased (B) | No Purchase (¬B) | Total |
|--------------|---------------|------------------|-------|
| Ad Click (A) | 45            | 15               | 60    |
| No Click (¬A) | 15           | 25               | 40    |
| **Total**    | **60**        | **40**           | **100** |

Compute P(B | A) directly. Then verify using Bayes' rule: P(B | A) = P(A | B) × P(B) / P(A).
## Solution
**Direct calculation:**

P(B | A) = 45/60 = 3/4 = 0.75

**Verification using Bayes' rule:**

P(A | B) = 45/60 = 3/4 = 0.75

P(B) = 60/100 = 3/5 = 0.60

P(A) = 60/100 = 3/5 = 0.60

P(B | A) = P(A | B) × P(B) / P(A)
         = (3/4) × (3/5) / (3/5)
         = 3/4
         = 0.75 ✓

**Both methods give P(B | A) = 0.75**
