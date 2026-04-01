---
subject: independence
difficulty: VERY EASY
quality: GOOD
---
# Testing for Independence
## Question
Given the following contingency table for coin flips and dice rolls:

|              | Even Die (B) | Odd Die (¬B) | Total |
|--------------|--------------|--------------|-------|
| Heads (A)    | 30           | 20           | 50    |
| Tails (¬A)   | 30           | 20           | 50    |
| **Total**    | **60**       | **40**       | **100** |

1. Calculate P(A | B) and compare it to P(A)
2. Are events A and B independent? Explain why or why not.
3. Verify using the product rule: Does P(A ∩ B) = P(A) × P(B)?
## Solution
**Part 1: Calculate P(A | B) and P(A)**

P(A | B) = 30/60 = 1/2 = 0.50

P(A) = 50/100 = 1/2 = 0.50

**Part 2: Independence check**

Since P(A | B) = P(A), the events appear to be independent. Knowing that the die showed an even number doesn't change the probability of getting heads.

**Part 3: Verify with product rule**

P(A ∩ B) = 30/100 = 0.30

P(A) × P(B) = (50/100) × (60/100) = 0.50 × 0.60 = 0.30

Since P(A ∩ B) = P(A) × P(B), this confirms independence! ✓

**Explanation:**

Two events A and B are independent if P(A | B) = P(A), which means learning that B occurred doesn't change the probability of A.

**In this case:** Events A (Heads) and B (Even Die) are independent. This makes sense because a coin flip and a die roll are physically independent processes - the outcome of one doesn't affect the other.
