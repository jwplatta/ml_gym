---
subject: covariance
difficulty: EASY
quality: GOOD
---
# Independence Implies Zero Covariance
## Question
Given the following contingency table for smartphone ownership and tablet ownership:

|              | Tablet (B) | No Tablet (¬B) | Total |
|--------------|------------|----------------|-------|
| Smartphone (A) | 36       | 24             | 60    |
| No Phone (¬A) | 24        | 16             | 40    |
| **Total**    | **60**     | **40**         | **100** |

Let X and Y be indicators for A and B (X=1 if smartphone, Y=1 if tablet). Show that if A and B are independent, then Cov(X, Y) = 0. Verify using the table data.
## Solution
**Step 1: Test if A and B are independent**

Calculate joint and product of marginals:

P(A ∩ B) = 36/100 = 0.36

P(A) × P(B) = (60/100) × (60/100) = 0.60 × 0.60 = 0.36

Since P(A ∩ B) = P(A) × P(B), events A and B are **independent**.

**Step 2: Compute Cov(X, Y)**

E[X] = P(A) = 60/100 = 0.60

E[Y] = P(B) = 60/100 = 0.60

E[XY] = P(A ∩ B) = 36/100 = 0.36

Cov(X, Y) = E[XY] - E[X]E[Y]
          = 0.36 - (0.60)(0.60)
          = 0.36 - 0.36
          = 0

**Answer: Cov(X, Y) = 0**

**Conclusion:** As expected, when A and B are independent, the covariance between their indicator variables is zero. This demonstrates the fundamental property that independence implies zero covariance.
