---
subject: joint-probability
difficulty: EASY
quality: GOOD
---
# Both Events Not Occurring
## Question
Given the following contingency table for marketing campaign response:

|                | Opened Email (B) | Didn't Open (¬B) | Total |
|----------------|------------------|------------------|-------|
| Clicked Ad (A) | 18               | 2                | 20    |
| No Click (¬A)  | 30               | 50               | 80    |
| **Total**      | **48**           | **52**           | **100** |

Compute P(¬A ∩ ¬B) - the probability that a user neither opened the email nor clicked the ad.
## Solution
P(¬A ∩ ¬B) = 50/100 = 1/2 = 0.50

**Answer: 1/2 = 0.50 or 50%**

**Interpretation:** Half of all users had no engagement at all - they neither opened the email nor clicked the ad. This represents the completely unengaged segment.

**Additional Insight:** We can verify using complements:

P(¬A ∩ ¬B) = 1 - P(A ∪ B) = 1 - [P(A) + P(B) - P(A ∩ B)]
           = 1 - [20/100 + 48/100 - 18/100]
           = 1 - 50/100 = 50/100 = 0.50 ✓
