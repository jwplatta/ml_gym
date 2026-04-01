---
subject: marginal-probability
difficulty: MEDIUM
quality: GOOD
---
# Marginals as Sums of Joints - Law of Total Probability
## Question
Given the following contingency table for device ownership:

|              | Tablet (B) | No Tablet (¬B) | Total |
|--------------|------------|----------------|-------|
| Laptop (A)   | 30         | 50             | 80    |
| No Laptop (¬A) | 10       | 10             | 20    |
| **Total**    | **40**     | **60**         | **100** |

Express each marginal probability P(A), P(¬A), P(B), P(¬B) as a sum of joint probabilities. Verify the law of total probability holds.
## Solution
**Marginals from summing joints:**

P(A) = P(A ∩ B) + P(A ∩ ¬B) = 30/100 + 50/100 = 80/100 = 0.80 ✓

P(¬A) = P(¬A ∩ B) + P(¬A ∩ ¬B) = 10/100 + 10/100 = 20/100 = 0.20 ✓

P(B) = P(A ∩ B) + P(¬A ∩ B) = 30/100 + 10/100 = 40/100 = 0.40 ✓

P(¬B) = P(A ∩ ¬B) + P(¬A ∩ ¬B) = 50/100 + 10/100 = 60/100 = 0.60 ✓

**Verification:**
- P(A) + P(¬A) = 0.80 + 0.20 = 1.00 ✓
- P(B) + P(¬B) = 0.40 + 0.60 = 1.00 ✓

**Key Insight:** Marginal probabilities are obtained by "marginalizing out" (summing over) the other variable. This is the basis of the law of total probability.
