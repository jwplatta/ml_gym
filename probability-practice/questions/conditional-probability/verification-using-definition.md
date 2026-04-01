---
subject: conditional-probability
difficulty: EASY
quality: GOOD
---
# Verification Using Definition
## Question
Given the following contingency table for website traffic:

|              | Converted (B) | No Conversion (¬B) | Total |
|--------------|---------------|-------------------|-------|
| Ad Click (A) | 40            | 60                | 100   |
| Organic (¬A) | 20            | 80                | 100   |
| **Total**    | **60**        | **140**           | **200** |

Use the definition P(A | B) = P(A ∩ B) / P(B) to find P(A | B), then verify by directly counting in the table.
## Solution
**Formula method:**

P(A | B) = P(A ∩ B) / P(B)
         = (40/200) / (60/200)
         = 40/60
         = 2/3
         ≈ 0.667

**Direct count method:**

In column B (60 conversions total), 40 came from ad clicks.

So P(A | B) = 40/60 = 2/3 ≈ 0.667 ✓

**Both methods agree!**
