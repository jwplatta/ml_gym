---
subject: covariance
difficulty: EASY
quality: GOOD
---
# Independence and Covariance
## Question
Consider two random variables X and Y with the following joint distribution:

| X \ Y | Y=0 | Y=1 |
|-------|-----|-----|
| X=0   | 0.3 | 0.2 |
| X=1   | 0.3 | 0.2 |

**Questions:**
1. Check if X and Y are independent by testing if P(X=x, Y=y) = P(X=x) × P(Y=y) for all (x, y).
2. Calculate Cov(X, Y).
3. What relationship do you observe between independence and covariance?
## Solution
**Part 1: Test for independence**

Calculate marginal probabilities:
- P(X=0) = 0.3 + 0.2 = 0.5
- P(X=1) = 0.3 + 0.2 = 0.5
- P(Y=0) = 0.3 + 0.3 = 0.6
- P(Y=1) = 0.2 + 0.2 = 0.4

Test each cell:

**Cell (X=0, Y=0):**
- Joint: P(X=0, Y=0) = 0.3
- Product: P(X=0) × P(Y=0) = 0.5 × 0.6 = 0.3 ✓

**Cell (X=0, Y=1):**
- Joint: P(X=0, Y=1) = 0.2
- Product: P(X=0) × P(Y=1) = 0.5 × 0.4 = 0.2 ✓

**Cell (X=1, Y=0):**
- Joint: P(X=1, Y=0) = 0.3
- Product: P(X=1) × P(Y=0) = 0.5 × 0.6 = 0.3 ✓

**Cell (X=1, Y=1):**
- Joint: P(X=1, Y=1) = 0.2
- Product: P(X=1) × P(Y=1) = 0.5 × 0.4 = 0.2 ✓

**Conclusion: X and Y are independent!**

**Part 2: Calculate Cov(X, Y)**

E[X] = P(X=1) = 0.5 (from marginals)

E[Y] = P(Y=1) = 0.4 (from marginals)

E[XY] = (1×1) × P(X=1, Y=1) = 1 × 0.2 = 0.2

Cov(X, Y) = E[XY] - E[X]E[Y]

Cov(X, Y) = 0.2 - (0.5)(0.4)

Cov(X, Y) = 0.2 - 0.2 = 0

**Answer: Cov(X, Y) = 0**

**Part 3: Relationship between independence and covariance**

**Key Theorem:**
- If X and Y are independent, then Cov(X, Y) = 0
- However, the converse is not always true: Cov(X, Y) = 0 does not necessarily imply independence

In this problem, X and Y are independent, and as expected, Cov(X, Y) = 0.

**Why is covariance zero for independent variables?**

If X and Y are independent, then E[XY] = E[X]E[Y], which means:

Cov(X, Y) = E[XY] - E[X]E[Y] = E[X]E[Y] - E[X]E[Y] = 0
