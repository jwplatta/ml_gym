---
subject: counting
difficulty: VERY EASY
quality: AVERAGE
---
# Selecting Without Replacement
## Question
Given the following contingency table for product defects:

|              | Defective (B) | Good (¬B) | Total |
|--------------|---------------|-----------|-------|
| Factory 1 (A) | 5            | 45        | 50    |
| Factory 2 (¬A) | 10          | 40        | 50    |
| **Total**    | **15**        | **85**    | **100** |

If you randomly select 2 outcomes from the sample space without replacement, how many ways can you do this?
## Solution
This is a combination problem: choosing 2 items from 100 without regard to order.

C(100, 2) = 100! / (2! × 98!)
          = (100 × 99) / 2
          = 9,900 / 2
          = 4,950

**Answer: 4,950 ways**

**Key Concept:** Combinations C(n,k) count the number of ways to choose k items from n items where order doesn't matter.
