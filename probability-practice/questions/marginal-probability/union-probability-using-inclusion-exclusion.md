---
subject: marginal-probability
difficulty: EASY
quality: GOOD
---
# Union Probability Using Inclusion-Exclusion
## Question
Given the following contingency table for event attendance:

|               | Weekend Event (B) | Weekday Event (¬B) | Total |
|---------------|-------------------|--------------------|-------|
| Registered (A) | 40               | 30                 | 70    |
| Walk-in (¬A)  | 10               | 20                 | 30    |
| **Total**     | **50**            | **50**             | **100** |

Compute P(A ∪ B) using the formula P(A ∪ B) = P(A) + P(B) - P(A ∩ B).
## Solution
P(A) = 70/100 = 0.70
P(B) = 50/100 = 0.50
P(A ∩ B) = 40/100 = 0.40

P(A ∪ B) = 0.70 + 0.50 - 0.40 = 0.80

**Answer: 0.80 or 80%**

**Verification by counting:**
Outcomes with A or B or both = 40 (A∩B) + 30 (A∩¬B) + 10 (¬A∩B) = 80
So P(A ∪ B) = 80/100 = 0.80 ✓

**Key Insight:** The inclusion-exclusion principle prevents double-counting the intersection.
