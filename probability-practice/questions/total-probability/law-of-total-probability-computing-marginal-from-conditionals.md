---
subject: total-probability
difficulty: VERY EASY
quality: GOOD
---
# Law of Total Probability - Computing Marginal from Conditionals
## Question
Given the following contingency table for medical test results:

|         | Test + (B) | Test - (¬B) | Total |
|---------|------------|-------------|-------|
| Disease (A) | 30 | 20 | 50 |
| No Disease (¬A) | 15 | 35 | 50 |
| **Total** | **45** | **55** | **100** |

Use the law of total probability to compute P(B) from P(B | A) and P(B | ¬A):

P(B) = P(B | A) × P(A) + P(B | ¬A) × P(¬A)
## Solution
P(B | A) = 30/50 = 0.6
P(A) = 50/100 = 0.5
P(B | ¬A) = 15/50 = 0.3
P(¬A) = 50/100 = 0.5

P(B) = (30/50) × (50/100) + (15/50) × (50/100)
     = 30/100 + 15/100
     = 45/100 = 0.45

Verify: From the table, P(B) = 45/100 = 0.45 ✓

**Key Insight:** The law of total probability allows us to compute marginal probabilities by partitioning on any event and using conditional probabilities.
