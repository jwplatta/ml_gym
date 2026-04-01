---
subject: variance
difficulty: VERY EASY
quality: GOOD
---
# Variance of Indicator Variable
## Question
Given the following contingency table for student performance:

|              | Passed (B) | Failed (¬B) | Total |
|--------------|------------|-------------|-------|
| Studied (A)  | 70         | 10          | 80    |
| No Study (¬A) | 10        | 10          | 20    |
| **Total**    | **80**     | **20**      | **100** |

Let X be an indicator variable for event A (X=1 if student studied, X=0 otherwise). Compute Var(X) using the formula Var(X) = E[X²] - (E[X])².
## Solution
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
