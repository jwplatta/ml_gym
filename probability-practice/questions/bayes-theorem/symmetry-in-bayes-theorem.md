---
subject: bayes-theorem
difficulty: MEDIUM
quality: GOOD
---
# Symmetry in Bayes' Theorem
## Question
Given the following contingency table for customer segments:

|              | High Value (B) | Low Value (¬B) | Total |
|--------------|----------------|----------------|-------|
| Loyalty Member (A) | 70 | 30          | 100   |
| Non-Member (¬A) | 20   | 80            | 100   |
| **Total**    | **90**         | **110**        | **200** |

Show that P(A | B) > P(A) if and only if P(B | A) > P(B). Verify using the table.
## Solution
**Test P(A | B) vs P(A):**

P(A) = 100/200 = 0.50

P(A | B) = 70/90 = 7/9 ≈ 0.778

Comparison: P(A | B) = 0.778 > 0.50 = P(A) ✓

**Test P(B | A) vs P(B):**

P(B) = 90/200 = 0.45

P(B | A) = 70/100 = 0.70

Comparison: P(B | A) = 0.70 > 0.45 = P(B) ✓

**Verified:** Both inequalities go in the same direction (both ">")

**Key Insight:** This symmetry property shows that if knowing B makes A more likely, then knowing A makes B more likely. They increase each other's probabilities.
