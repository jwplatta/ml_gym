---
subject: conditional-probability
difficulty: VERY EASY
quality: GOOD
---
# Student Status and Missed Payments
## Question
A bank records whether a customer is a student and whether they missed a credit card payment.

|                         | Missed Payment (M) | No Missed Payment (¬M) | Total |
|-------------------------|--------------------|-------------------------|-------|
| Student (S)             | 18                 | 42                      | 60    |
| Non-Student (¬S)        | 12                 | 78                      | 90    |
| **Total**               | **30**             | **120**                 | **150** |

Compute both:
1. P(S | M)
2. P(M | S)

Are they equal?
## Solution
P(S | M) = 18/30 = 0.60

P(M | S) = 18/60 = 0.30

They are **not** equal.

**Why not?**
Because conditioning changes the sample space. In the first case we restrict to customers who missed a payment. In the second case we restrict to students.

**Answers:**
- P(S | M) = 0.60
- P(M | S) = 0.30
