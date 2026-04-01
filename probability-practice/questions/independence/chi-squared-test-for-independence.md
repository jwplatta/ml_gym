---
subject: independence
difficulty: MEDIUM
quality: GOOD
---
# Chi-Squared Test for Independence

## Question
Given the following contingency table for voting patterns by age group:

|           | Voted Yes (B) | Voted No (¬B) | Total |
|-----------|---------------|---------------|-------|
| Young (A) | 40            | 60            | 100   |
| Old (¬A)  | 60            | 40            | 100   |
| **Total** | **100**       | **100**       | **200** |

Compute the chi-squared statistic: χ² = Σ (observed - expected)² / expected for all four cells, where expected = (row total × column total) / grand total.

## Solution
**Expected counts under independence:**

E(A ∩ B) = 100 × 100 / 200 = 50
E(A ∩ ¬B) = 100 × 100 / 200 = 50
E(¬A ∩ B) = 100 × 100 / 200 = 50
E(¬A ∩ ¬B) = 100 × 100 / 200 = 50

**Chi-squared calculation:**

χ² = (40 - 50)² / 50 + (60 - 50)² / 50 + (60 - 50)² / 50 + (40 - 50)² / 50

χ² = 100/50 + 100/50 + 100/50 + 100/50

χ² = 2 + 2 + 2 + 2 = 8

**Interpretation:** χ² = 8 is relatively large, suggesting the events are NOT independent. Young voters and old voters have different voting patterns (young tend to vote No, old tend to vote Yes).

For a 2×2 table with 1 degree of freedom, χ² > 3.841 indicates significant dependence at the 0.05 level. Since 8 > 3.841, we reject independence.
