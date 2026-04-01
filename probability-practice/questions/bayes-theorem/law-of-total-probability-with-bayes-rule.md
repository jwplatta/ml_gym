---
subject: bayes-theorem
difficulty: MEDIUM
quality: GOOD
---
# Law of Total Probability with Bayes' Rule
## Question
Given the following contingency table for product quality:

|              | Defective (B) | Good (¬B) | Total |
|--------------|---------------|-----------|-------|
| Factory 1 (A) | 12           | 88        | 100   |
| Factory 2 (¬A) | 18          | 132       | 150   |
| **Total**    | **30**        | **220**   | **250** |

Use the law of total probability to compute P(B) from P(B | A) and P(B | ¬A):
P(B) = P(B | A) × P(A) + P(B | ¬A) × P(¬A)

Then use this with Bayes' rule to find P(A | B).
## Solution
**Step 1: Calculate conditional probabilities**

P(B | A) = 12/100 = 0.12

P(A) = 100/250 = 2/5 = 0.40

P(B | ¬A) = 18/150 = 3/25 = 0.12

P(¬A) = 150/250 = 3/5 = 0.60

**Step 2: Apply law of total probability**

P(B) = P(B | A) × P(A) + P(B | ¬A) × P(¬A)
     = (0.12)(0.40) + (0.12)(0.60)
     = 0.048 + 0.072
     = 0.12

**Verification:** From table, P(B) = 30/250 = 0.12 ✓

**Step 3: Apply Bayes' rule**

P(A | B) = P(B | A) × P(A) / P(B)
         = (0.12)(0.40) / (0.12)
         = 0.048 / 0.12
         = 0.40

**Answer: P(A | B) = 0.40 or 40%**

**Interpretation:** Even knowing a product is defective doesn't change the probability it came from Factory 1 (still 40%), because both factories have the same defect rate (12%).
