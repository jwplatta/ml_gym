---
subject: conditional-probability
difficulty: EASY
quality: GOOD
---
# Comparing Conditional Probabilities
## Question
Given the following contingency table for customer retention:

|              | Renewed (B) | Churned (¬B) | Total |
|--------------|-------------|--------------|-------|
| Contacted (A) | 80         | 20           | 100   |
| Not Contacted (¬A) | 30    | 70           | 100   |
| **Total**    | **110**     | **90**       | **200** |

Compute P(A | B) and P(A | ¬B). Which conditioning event makes A more likely?
## Solution
P(A | B) = 80/110 = 8/11 ≈ 0.727

P(A | ¬B) = 20/90 = 2/9 ≈ 0.222

**Comparison:** P(A | B) = 0.727 > 0.222 = P(A | ¬B)

**Conclusion:** Conditioning on B (renewal) makes A (being contacted) much more likely. This suggests that contacting customers is associated with higher renewal rates.
