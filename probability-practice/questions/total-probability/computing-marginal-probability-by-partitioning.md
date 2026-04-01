---
subject: total-probability
difficulty: VERY EASY
quality: GOOD
---
# Computing Marginal Probability by Partitioning
## Question
Given the following contingency table for stock performance and economic conditions:

|                 | High Growth (B) | Low Growth (¬B) | Total |
|-----------------|-----------------|-----------------|-------|
| Good Economy (A) | 40 | 10 | 50 |
| Bad Economy (¬A) | 10 | 40 | 50 |
| **Total** | **50** | **50** | **100** |

Express P(A) using the law of total probability by partitioning on B:

P(A) = P(A | B) × P(B) + P(A | ¬B) × P(¬B)
## Solution
P(A | B) = 40/50 = 0.8
P(B) = 50/100 = 0.5
P(A | ¬B) = 10/50 = 0.2
P(¬B) = 50/100 = 0.5

P(A) = (40/50) × (50/100) + (10/50) × (50/100)
     = 40/100 + 10/100
     = 50/100 = 0.5

Verify: From the table, P(A) = 50/100 = 0.5 ✓

**Key Insight:** We can partition on any event to compute marginals. Here we partition on growth to compute the probability of good economy.
