---
subject: covariance
difficulty: EASY
quality: GOOD
---
# Simple Covariance Calculation
## Question
Consider two random variables X and Y with the following joint distribution:

| X \ Y | Y=0 | Y=1 |
|-------|-----|-----|
| X=0   | 0.2 | 0.3 |
| X=1   | 0.4 | 0.1 |

Calculate Cov(X, Y) using the formula: Cov(X, Y) = E[XY] - E[X]E[Y]
## Solution
**Step 1: Calculate E[X]**

E[X] = 0 × P(X=0, Y=0) + 0 × P(X=0, Y=1) + 1 × P(X=1, Y=0) + 1 × P(X=1, Y=1)

E[X] = 0 × (0.2) + 0 × (0.3) + 1 × (0.4) + 1 × (0.1)

E[X] = 0 + 0 + 0.4 + 0.1 = 0.5

**Alternative:** E[X] = P(X=1) = 0.4 + 0.1 = 0.5

**Step 2: Calculate E[Y]**

E[Y] = 0 × P(X=0, Y=0) + 1 × P(X=0, Y=1) + 0 × P(X=1, Y=0) + 1 × P(X=1, Y=1)

E[Y] = 0 × (0.2) + 1 × (0.3) + 0 × (0.4) + 1 × (0.1)

E[Y] = 0 + 0.3 + 0 + 0.1 = 0.4

**Alternative:** E[Y] = P(Y=1) = 0.3 + 0.1 = 0.4

**Step 3: Calculate E[XY]**

E[XY] = (0×0) × (0.2) + (0×1) × (0.3) + (1×0) × (0.4) + (1×1) × (0.1)

E[XY] = 0 + 0 + 0 + 0.1 = 0.1

**Note:** XY = 1 only when both X=1 and Y=1, which happens with probability 0.1

**Step 4: Calculate Cov(X, Y)**

Cov(X, Y) = E[XY] - E[X]E[Y]

Cov(X, Y) = 0.1 - (0.5)(0.4)

Cov(X, Y) = 0.1 - 0.2 = -0.1

**Answer: Cov(X, Y) = -0.1**

**Interpretation:** The negative covariance indicates that X and Y are negatively associated. When X is large, Y tends to be small, and vice versa. Looking at the table, we can verify this: P(X=1, Y=1) = 0.1 is less than P(X=1)×P(Y=1) = 0.5×0.4 = 0.2, confirming negative association.
