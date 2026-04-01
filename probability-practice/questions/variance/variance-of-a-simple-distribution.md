---
subject: variance
difficulty: EASY
quality: GOOD
---
# Variance of a Simple Distribution
## Question
Let X be a random variable with the following distribution:

| x | 0 | 2 | 4 |
|---|---|---|---|
| P(X = x) | 0.2 | 0.5 | 0.3 |

**Questions:**
1. Calculate E[X]
2. Calculate Var(X)
## Solution
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
