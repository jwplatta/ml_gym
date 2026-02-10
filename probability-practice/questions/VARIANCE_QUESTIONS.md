### Question 1

**Prompt:**
Given the contingency table:

{{table}}

Let X be an indicator variable for event A. Compute Var(X) using the formula Var(X) = E[X²] - (E[X])².

**Solution:**
For an indicator variable X:
E[X] = P(A) = {{marginal_A}}/{{total}}
E[X²] = 1² × P(A) + 0² × P(¬A) = P(A) = {{marginal_A}}/{{total}}

Var(X) = E[X²] - (E[X])² = {{marginal_A}}/{{total}} - ({{marginal_A}}/{{total}})² = {{variance_result}}

For Bernoulli(p): Var(X) = p(1-p) = ({{marginal_A}}/{{total}}) × ({{marginal_notA}}/{{total}}) = {{variance_result}}

## Variance of a Simple Distribution - Easy

**Prompt:**
Let X be a random variable with the following distribution:

| x | 0 | 2 | 4 |
|---|---|---|---|
| P(X = x) | 0.2 | 0.5 | 0.3 |

**Questions:**
1. Calculate E[X]
2. Calculate Var(X)

**Solution:**

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

## medium

### Question 1

**Prompt:**
Given the contingency table:

{{table}}

Define X as an indicator for A and Y as an indicator for B. If X and Y were independent, what would Var(X + Y) equal?

**Solution:**
Var(X) = P(A) × P(¬A) = ({{marginal_A}}/{{total}}) × ({{marginal_notA}}/{{total}}) = {{var_x}}
Var(Y) = P(B) × P(¬B) = ({{marginal_B}}/{{total}}) × ({{marginal_notB}}/{{total}}) = {{var_y}}

If X and Y are independent:
Var(X + Y) = Var(X) + Var(Y) = {{var_x}} + {{var_y}} = {{var_sum}}