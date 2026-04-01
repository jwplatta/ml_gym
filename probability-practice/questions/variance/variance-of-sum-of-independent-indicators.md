---
subject: variance
difficulty: MEDIUM
quality: GOOD
---
# Variance of Sum of Independent Indicators

## Question
Given the following contingency table for product features:

|              | Feature B | No Feature B (¬B) | Total |
|--------------|-----------|-------------------|-------|
| Feature A    | 30        | 30                | 60    |
| No Feature A (¬A) | 20   | 20                | 40    |
| **Total**    | **50**    | **50**            | **100** |

Define X as an indicator for A and Y as an indicator for B (X=1 if product has Feature A, Y=1 if product has Feature B). If X and Y were independent, what would Var(X + Y) equal?

## Solution
**Step 1: Calculate Var(X)**

Var(X) = P(A) × P(¬A)
       = (60/100) × (40/100)
       = 0.60 × 0.40
       = 0.24

**Step 2: Calculate Var(Y)**

Var(Y) = P(B) × P(¬B)
       = (50/100) × (50/100)
       = 0.50 × 0.50
       = 0.25

**Step 3: If X and Y are independent, calculate Var(X + Y)**

For independent random variables, the variance of the sum equals the sum of the variances:

Var(X + Y) = Var(X) + Var(Y)
           = 0.24 + 0.25
           = 0.49

**Answer: Var(X + Y) = 0.49**

**Key Property:** When X and Y are independent, Var(X + Y) = Var(X) + Var(Y). This property does NOT hold if X and Y are dependent - in that case, we need to account for covariance: Var(X + Y) = Var(X) + Var(Y) + 2Cov(X, Y).
