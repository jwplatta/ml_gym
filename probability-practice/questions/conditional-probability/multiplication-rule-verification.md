---
subject: conditional-probability
difficulty: MEDIUM
quality: GOOD
---
# Multiplication Rule Verification
## Question
Given the following contingency table for project outcomes:

|              | Success (B) | Failure (¬B) | Total |
|--------------|-------------|--------------|-------|
| Experienced Team (A) | 56 | 14       | 70    |
| New Team (¬A) | 24        | 36           | 60    |
| **Total**    | **80**      | **50**       | **130** |

Show that P(A ∩ B) = P(A | B) × P(B) using the table data. Then verify the same using P(A ∩ B) = P(B | A) × P(A).
## Solution
**Method 1: P(A ∩ B) = P(A | B) × P(B)**

P(A | B) = 56/80 = 7/10 = 0.70

P(B) = 80/130 = 8/13 ≈ 0.615

P(A | B) × P(B) = (56/80) × (80/130) = 56/130

Direct from table: P(A ∩ B) = 56/130 ✓

**Method 2: P(A ∩ B) = P(B | A) × P(A)**

P(B | A) = 56/70 = 4/5 = 0.80

P(A) = 70/130 = 7/13 ≈ 0.538

P(B | A) × P(A) = (56/70) × (70/130) = 56/130

Direct from table: P(A ∩ B) = 56/130 ✓

**Conclusion:** Both formulations of the multiplication rule give the same result, confirming their equivalence.
