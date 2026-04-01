---
subject: conditional-probability
difficulty: EASY
quality: GOOD
---
# Complement Rule for Conditional Probabilities
## Question
Given the following contingency table for loan applications:

|              | Approved (B) | Denied (¬B) | Total |
|--------------|--------------|-------------|-------|
| High Score (A) | 70         | 10          | 80    |
| Low Score (¬A) | 20          | 50          | 70    |
| **Total**    | **90**       | **60**      | **150** |

Verify that P(A | B) + P(¬A | B) = 1.
## Solution
P(A | B) = 70/90 = 7/9 ≈ 0.778

P(¬A | B) = 20/90 = 2/9 ≈ 0.222

Sum = 7/9 + 2/9 = 9/9 = 1 ✓

**Verification:** The conditional probabilities of complementary events given the same condition must sum to 1.

**Key Property:** For any events A and B, P(A | B) + P(¬A | B) = 1, just as P(A) + P(¬A) = 1 for unconditional probabilities.
