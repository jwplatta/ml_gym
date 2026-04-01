---
subject: conditional-probability
difficulty: MEDIUM
quality: GOOD
---
# All Four Conditional Probabilities
## Question
Given the following contingency table for product returns:

|              | Returned (B) | Kept (¬B) | Total |
|--------------|--------------|-----------|-------|
| Online (A)   | 30           | 70        | 100   |
| In-Store (¬A) | 10          | 90        | 100   |
| **Total**    | **40**       | **160**   | **200** |

Compute all four conditional probabilities: P(A|B), P(¬A|B), P(A|¬B), P(¬A|¬B). Verify that P(A|B) + P(¬A|B) = 1 and P(A|¬B) + P(¬A|¬B) = 1.
## Solution
**Conditional on B (Returned):**

P(A | B) = 30/40 = 3/4 = 0.75

P(¬A | B) = 10/40 = 1/4 = 0.25

**Conditional on ¬B (Kept):**

P(A | ¬B) = 70/160 = 7/16 ≈ 0.438

P(¬A | ¬B) = 90/160 = 9/16 ≈ 0.562

**Verify complement rules:**

P(A|B) + P(¬A|B) = 3/4 + 1/4 = 1 ✓

P(A|¬B) + P(¬A|¬B) = 7/16 + 9/16 = 16/16 = 1 ✓

**Interpretation:** Online purchases have a higher return rate (30%) compared to in-store purchases (10%), which is reflected in the conditional probabilities.
