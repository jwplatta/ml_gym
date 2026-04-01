---
subject: total-probability
difficulty: EASY
quality: GOOD
---
# Law of Total Probability - Verifying Marginals
## Question
Given the following contingency table for customer purchases at a retail store:

|            | Premium Member (B) | Regular Customer (¬B) | Total |
|------------|-------------------|-----------------------|-------|
| Made Purchase (A) | 70            | 30                    | 100   |
| No Purchase (¬A)  | 30            | 70                    | 100   |
| **Total**  | **100**           | **100**               | **200** |

Use the law of total probability to compute P(B) from P(B | A) and P(B | ¬A):

P(B) = P(B | A) × P(A) + P(B | ¬A) × P(¬A)

Verify your answer matches the marginal probability in the table.
## Solution
First, calculate the components:
- P(B | A) = 70/100 = 0.70
- P(A) = 100/200 = 0.50
- P(B | ¬A) = 30/100 = 0.30
- P(¬A) = 100/200 = 0.50

Using the law of total probability:

P(B) = P(B | A) × P(A) + P(B | ¬A) × P(¬A)

P(B) = (0.70)(0.50) + (0.30)(0.50)

P(B) = 0.35 + 0.15 = 0.50

**Verification:** From the table, P(B) = 100/200 = 0.50 ✓

**Answer: 0.50 or 50%**
