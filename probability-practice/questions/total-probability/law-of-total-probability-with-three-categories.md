---
subject: total-probability
difficulty: VERY EASY
quality: GOOD
---
# Law of Total Probability with Three Categories
## Question
Given the following contingency table for customer satisfaction across three service tiers:

|              | Satisfied (B) | Not Satisfied (¬B) | Total |
|--------------|---------------|-------------------|-------|
| Premium (A₁) | 40            | 10                | 50    |
| Standard (A₂)| 24            | 16                | 40    |
| Basic (A₃)   | 6             | 4                 | 10    |
| **Total**    | **70**        | **30**            | **100** |

Use the law of total probability to compute P(B) from the conditional probabilities:

P(B) = P(B | A₁) × P(A₁) + P(B | A₂) × P(A₂) + P(B | A₃) × P(A₃)
## Solution
First, calculate the components:
- P(B | A₁) = 40/50 = 0.80
- P(A₁) = 50/100 = 0.50
- P(B | A₂) = 24/40 = 0.60
- P(A₂) = 40/100 = 0.40
- P(B | A₃) = 6/10 = 0.60
- P(A₃) = 10/100 = 0.10

Using the law of total probability:

P(B) = P(B | A₁) × P(A₁) + P(B | A₂) × P(A₂) + P(B | A₃) × P(A₃)

P(B) = (0.80)(0.50) + (0.60)(0.40) + (0.60)(0.10)

P(B) = 0.40 + 0.24 + 0.06 = 0.70

**Verification:** From the table, P(B) = 70/100 = 0.70 ✓

**Answer: 0.70 or 70%**
