---
subject: counting
difficulty: EASY
quality: GOOD
---
# Counting Union Events
## Question
Given the following contingency table for marketing responses:

|              | Clicked Ad (B) | No Click (¬B) | Total |
|--------------|----------------|---------------|-------|
| Opened Email (A) | 30         | 20            | 50    |
| No Open (¬A) | 15             | 35            | 50    |
| **Total**    | **45**         | **55**        | **100** |

How many outcomes satisfy "A or B (or both)" (opened email OR clicked ad OR both)?
## Solution
Outcomes with A or B are in cells (A∩B), (A∩¬B), and (¬A∩B):

Count = 30 + 20 + 15 = 65

**Answer: 65 outcomes**

**Verification using complement:**
Count(A ∪ B) = Total - Count(¬A ∩ ¬B) = 100 - 35 = 65 ✓

**Key Insight:** To count A ∪ B, sum all cells except (¬A ∩ ¬B).
