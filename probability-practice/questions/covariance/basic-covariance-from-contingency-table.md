---
subject: covariance
difficulty: VERY EASY
quality: GOOD
---
# Basic Covariance from Contingency Table
## Question
Given the following contingency table for customer behavior:

|              | Purchased (B) | No Purchase (¬B) | Total |
|--------------|---------------|------------------|-------|
| Email Sent (A) | 40          | 10               | 50    |
| No Email (¬A) | 20           | 30               | 50    |
| **Total**    | **60**        | **40**           | **100** |

Let X and Y be indicator variables for events A and B respectively (X=1 if email sent, Y=1 if purchased). Compute Cov(X, Y) = E[XY] - E[X]E[Y].
## Solution
**Step 1: Calculate E[X]**

E[X] = P(A) = 50/100 = 0.50

**Step 2: Calculate E[Y]**

E[Y] = P(B) = 60/100 = 0.60

**Step 3: Calculate E[XY]**

E[XY] = P(X=1 and Y=1) = P(A ∩ B) = 40/100 = 0.40

**Step 4: Calculate Cov(X, Y)**

Cov(X, Y) = E[XY] - E[X]E[Y]
          = 0.40 - (0.50)(0.60)
          = 0.40 - 0.30
          = 0.10

**Answer: Cov(X, Y) = 0.10**

**Interpretation:** The positive covariance (0.10) indicates that sending an email and making a purchase are positively associated. If A and B were independent, Cov(X,Y) would equal 0.
