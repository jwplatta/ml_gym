---
subject: marginal-probability
difficulty: MEDIUM
quality: GOOD
---
# Union via Counting vs Formula
## Question
Given the following contingency table for streaming service usage:

|               | Netflix (B) | No Netflix (¬B) | Total |
|---------------|-------------|-----------------|-------|
| Amazon (A)    | 35          | 25              | 60    |
| No Amazon (¬A) | 30         | 10              | 40    |
| **Total**     | **65**      | **35**          | **100** |

Show that P(A ∪ B) = (number of outcomes with A or B or both) / total. Then verify using the inclusion-exclusion formula.
## Solution
**Count method:**
Outcomes with A or B = 35 (A∩B) + 25 (A∩¬B) + 30 (¬A∩B) = 90
So P(A ∪ B) = 90/100 = 0.90

**Formula method:**
P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
         = 60/100 + 65/100 - 35/100
         = 90/100 = 0.90 ✓

**Interpretation:** 90% of people use at least one streaming service (Amazon, Netflix, or both).
