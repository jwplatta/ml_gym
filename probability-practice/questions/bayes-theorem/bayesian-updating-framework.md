---
subject: bayes-theorem
difficulty: EASY
quality: GOOD
---
# Bayesian Updating Framework
## Question
Given the following contingency table for email classification:

|              | Spam (B) | Not Spam (¬B) | Total |
|--------------|----------|---------------|-------|
| Contains "Free" (A) | 80 | 40         | 120   |
| No "Free" (¬A) | 20    | 60            | 80    |
| **Total**    | **100**  | **100**       | **200** |

Suppose you observe event B (email is spam). Use Bayes' theorem to update your belief about A:
- Prior: P(A) = ?
- Likelihood: P(B | A) = ?
- Evidence: P(B) = ?
- Posterior: P(A | B) = ?
## Solution
**Prior: P(A)**

P(A) = 120/200 = 3/5 = 0.60

**Likelihood: P(B | A)**

P(B | A) = 80/120 = 2/3 ≈ 0.667

**Evidence: P(B)**

P(B) = 100/200 = 1/2 = 0.50

**Posterior: P(A | B)**

P(A | B) = P(B | A) × P(A) / P(B)
         = (2/3) × (3/5) / (1/2)
         = (2/5) / (1/2)
         = 4/5
         = 0.80

**Answer: P(A | B) = 4/5 = 0.80 or 80%**

**Interpretation:** If we know an email is spam, there's an 80% probability it contains the word "Free". This is higher than the prior 60%, showing that spam emails are more likely to contain "Free".
