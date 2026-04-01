---
subject: independence
difficulty: EASY
quality: GOOD
---
# Testing for Independence with Calculations
## Question
Given the following contingency table for credit card usage and online shopping:

|                  | Online Shopper (B) | Not Online Shopper (¬B) | Total |
|------------------|-------------------|------------------------|-------|
| Credit Card (A)  | 48                | 32                     | 80    |
| Debit Only (¬A)  | 12                | 8                      | 20    |
| **Total**        | **60**            | **40**                 | **100** |

1. Calculate P(A | B) and compare it to P(A)
2. Are events A and B independent? Explain why or why not.
## Solution
**Part 1: Calculate P(A | B) and P(A)**

P(A | B) = 48/60 = 4/5 = 0.80

P(A) = 80/100 = 4/5 = 0.80

**Part 2: Independence check**

Since P(A | B) = P(A) = 0.80, the events appear to be independent. Knowing that someone is an online shopper doesn't change the probability they have a credit card.

**Explanation:**

Two events A and B are independent if P(A | B) = P(A).

We can verify this further:
- P(A | ¬B) = 32/40 = 4/5 = 0.80
- P(A ∩ B) = 48/100 = 0.48 = P(A) × P(B) = (0.80)(0.60) = 0.48 ✓

All checks confirm independence: having a credit card and being an online shopper are independent in this dataset.
