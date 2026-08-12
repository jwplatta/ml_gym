## Variance of Indicator Variable

Given the following contingency table for student performance:

|              | Passed (B) | Failed (¬B) | Total |
|--------------|------------|-------------|-------|
| Studied (A)  | 70         | 10          | 80    |
| No Study (¬A) | 10        | 10          | 20    |
| **Total**    | **80**     | **20**      | **100** |

Let X be an indicator variable for event A (X=1 if student studied, X=0 otherwise). Compute Var(X) using the formula Var(X) = E[X²] - (E[X])².

### Solution

**Step 1: Calculate E[X]**

For an indicator variable X:

E[X] = P(A) = 80/100 = 0.80

**Step 2: Calculate E[X²]**

E[X²] = 1² × P(A) + 0² × P(¬A) = P(A) = 80/100 = 0.80

**Step 3: Calculate Var(X)**

Var(X) = E[X²] - (E[X])²
       = 0.80 - (0.80)²
       = 0.80 - 0.64
       = 0.16

**Answer: Var(X) = 0.16**

**Alternative using Bernoulli formula:**

For a Bernoulli random variable with parameter p, Var(X) = p(1-p):

Var(X) = P(A) × P(¬A) = (80/100) × (20/100) = 0.80 × 0.20 = 0.16 ✓

**Key Insight:** For indicator variables, the variance equals p(1-p), which is maximized when p = 0.5.

### Notes

- Quality: GOOD
- Difficulty: VERY EASY
- Notes: Clear introduction to variance of indicator variables; demonstrates two equivalent calculation methods

## Variance of a Simple Distribution

Let X be a random variable with the following distribution:

| x | 0 | 2 | 4 |
|---|---|---|---|
| P(X = x) | 0.2 | 0.5 | 0.3 |

**Questions:**
1. Calculate E[X]
2. Calculate Var(X)

### Solution

**Part 1: Calculate E[X]**

E[X] = 0 × (0.2) + 2 × (0.5) + 4 × (0.3)

E[X] = 0 + 1 + 1.2 = 2.2

**Answer: E[X] = 2.2**

**Part 2: Calculate Var(X)**

First, calculate E[X²]:

E[X²] = 0² × (0.2) + 2² × (0.5) + 4² × (0.3)

E[X²] = 0 × (0.2) + 4 × (0.5) + 16 × (0.3)

E[X²] = 0 + 2 + 4.8 = 6.8

Now calculate variance:

Var(X) = E[X²] - (E[X])²

Var(X) = 6.8 - (2.2)²

Var(X) = 6.8 - 4.84 = 1.96

**Answer: Var(X) = 1.96**

**Standard deviation:** σ = √Var(X) = √1.96 = 1.4

**Key Insight:** This demonstrates the computational formula for variance: Var(X) = E[X²] - (E[X])². This is often easier to compute than the alternative formula Var(X) = E[(X - μ)²], which requires calculating deviations from the mean first.

### Notes

- Quality: GOOD
- Difficulty: EASY
- Notes: Multi-part question demonstrating expectation and variance calculations; includes standard deviation calculation

## Variance of Sum of Independent Indicators

Given the following contingency table for product features:

|              | Feature B | No Feature B (¬B) | Total |
|--------------|-----------|-------------------|-------|
| Feature A    | 30        | 30                | 60    |
| No Feature A (¬A) | 20   | 20                | 40    |
| **Total**    | **50**    | **50**            | **100** |

Define X as an indicator for A and Y as an indicator for B (X=1 if product has Feature A, Y=1 if product has Feature B). If X and Y were independent, what would Var(X + Y) equal?

### Solution

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

### Notes

- Quality: EXCELLENT
- Difficulty: MEDIUM
- Notes: Demonstrates variance of sum property for independent variables; important theoretical result connecting independence and variance