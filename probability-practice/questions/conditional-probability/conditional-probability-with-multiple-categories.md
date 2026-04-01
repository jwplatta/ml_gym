---
subject: conditional-probability
difficulty: VERY EASY
quality: GOOD
---
# Conditional Probability with Multiple Categories
## Question
Given the following contingency table for investment performance by market sector:

|            | High Return (B) | Low Return (¬B) | Total |
|------------|-----------------|-----------------|-------|
| Tech (A)   | 30              | 20              | 50    |
| Finance    | 15              | 35              | 50    |
| **Total**  | **45**          | **55**          | **100** |

Given that an investment had a high return (B occurred), what is the probability it was in the Tech sector? Compute P(A | B).
## Solution
P(A | B) = P(A ∩ B) / P(B)

From the table:
- P(A ∩ B) = 30/100
- P(B) = 45/100

Therefore:
P(A | B) = (30/100) / (45/100) = 30/45 = 2/3 ≈ 0.667

**Answer: 2/3 ≈ 0.667 or about 66.7%**

**Interpretation:** Among all 45 investments with high returns, 30 were in the Tech sector, so P(Tech | High Return) = 2/3.
