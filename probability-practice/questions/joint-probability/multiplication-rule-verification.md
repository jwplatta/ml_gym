---
subject: joint-probability
difficulty: EASY
quality: GOOD
---
# Multiplication Rule Verification
## Question
Given the following contingency table for subscription tier and feature usage:

|              | Used Feature (B) | Didn't Use (¬B) | Total |
|--------------|------------------|-----------------|-------|
| Premium (A)  | 45               | 15              | 60    |
| Basic (¬A)   | 15               | 25              | 40    |
| **Total**    | **60**           | **40**          | **100** |

Verify that P(A ∩ B) = P(A) × P(B | A) using the table data.
## Solution
Calculate components:

P(A) = 60/100 = 0.60

P(B | A) = 45/60 = 3/4 = 0.75

**Using multiplication rule:**

P(A) × P(B | A) = (60/100) × (45/60) = 45/100 = 0.45

**Direct from table:**

P(A ∩ B) = 45/100 = 0.45

Both equal 0.45, verifying the multiplication rule! ✓

**Key Insight:** The multiplication rule P(A ∩ B) = P(A) × P(B | A) provides an alternative way to compute joint probabilities using marginal and conditional probabilities.
