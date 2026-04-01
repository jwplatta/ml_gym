---
subject: marginal-probability
difficulty: EASY
quality: GOOD
---
# Verifying All Four Joint Probabilities Sum to One
## Question
Given the following contingency table for project success:

|               | Successful (B) | Failed (¬B) | Total |
|---------------|----------------|-------------|-------|
| Experienced (A) | 48           | 12          | 60    |
| Novice (¬A)   | 24             | 16          | 40    |
| **Total**     | **72**         | **28**      | **100** |

Compute all four joint probabilities: P(A ∩ B), P(A ∩ ¬B), P(¬A ∩ B), P(¬A ∩ ¬B). Verify they sum to 1.
## Solution
P(A ∩ B) = 48/100 = 0.48
P(A ∩ ¬B) = 12/100 = 0.12
P(¬A ∩ B) = 24/100 = 0.24
P(¬A ∩ ¬B) = 16/100 = 0.16

Sum = 0.48 + 0.12 + 0.24 + 0.16 = 1.00 ✓

**Verification:** All four cells partition the sample space, so their probabilities must sum to 1.

**Key Insight:** The four joint probabilities in a 2×2 table form a complete partition of the sample space.
