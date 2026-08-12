# Covariance

## Basic Covariance from Contingency Table

Given the following contingency table for customer behavior:

|              | Purchased (B) | No Purchase (¬B) | Total |
|--------------|---------------|------------------|-------|
| Email Sent (A) | 40          | 10               | 50    |
| No Email (¬A) | 20           | 30               | 50    |
| **Total**    | **60**        | **40**           | **100** |

Let X and Y be indicator variables for events A and B respectively (X=1 if email sent, Y=1 if purchased). Compute Cov(X, Y) = E[XY] - E[X]E[Y].

### Solution

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

### Notes

- Quality: GOOD
- Difficulty: VERY EASY
- Notes: Clear introduction to covariance calculation using indicator variables from a contingency table

## Independence Implies Zero Covariance

Given the following contingency table for smartphone ownership and tablet ownership:

|              | Tablet (B) | No Tablet (¬B) | Total |
|--------------|------------|----------------|-------|
| Smartphone (A) | 36       | 24             | 60    |
| No Phone (¬A) | 24        | 16             | 40    |
| **Total**    | **60**     | **40**         | **100** |

Let X and Y be indicators for A and B (X=1 if smartphone, Y=1 if tablet). Show that if A and B are independent, then Cov(X, Y) = 0. Verify using the table data.

### Solution

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

### Notes

- Quality: EXCELLENT
- Difficulty: EASY
- Notes: Important theoretical result connecting independence and covariance; demonstrates that independent events have zero covariance

## Simple Covariance Calculation

Consider two random variables X and Y with the following joint distribution:

| X \ Y | Y=0 | Y=1 |
|-------|-----|-----|
| X=0   | 0.2 | 0.3 |
| X=1   | 0.4 | 0.1 |

Calculate Cov(X, Y) using the formula: Cov(X, Y) = E[XY] - E[X]E[Y]

### Solution

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

### Notes

- Quality: EXCELLENT
- Difficulty: EASY
- Notes: Clear step-by-step calculation of covariance; demonstrates negative association; includes interpretation

## Independence and Covariance

Consider two random variables X and Y with the following joint distribution:

| X \ Y | Y=0 | Y=1 |
|-------|-----|-----|
| X=0   | 0.3 | 0.2 |
| X=1   | 0.3 | 0.2 |

**Questions:**
1. Check if X and Y are independent by testing if P(X=x, Y=y) = P(X=x) × P(Y=y) for all (x, y).
2. Calculate Cov(X, Y).
3. What relationship do you observe between independence and covariance?

### Solution

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

### Notes

- Quality: EXCELLENT
- Difficulty: EASY
- Notes: Multi-part question combining independence testing and covariance calculation; demonstrates the theorem that independence implies zero covariance
