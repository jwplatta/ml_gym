---
subject: expectation
difficulty: VERY EASY
quality: AVERAGE
---
# Linearity of Expectation with Portfolio
## Question
A portfolio contains 3 stocks. Each stock has a probability of 0.6 of having a positive return tomorrow.

Let X₁, X₂, X₃ be indicator variables (= 1 if stock has positive return, 0 otherwise).

**Question:** What is the expected number of stocks with positive returns? Use linearity of expectation.
## Solution
Let Y = X₁ + X₂ + X₃ = total number of stocks with positive returns.

For each indicator variable:
- E[X₁] = P(Stock 1 positive) = 0.6
- E[X₂] = P(Stock 2 positive) = 0.6
- E[X₃] = P(Stock 3 positive) = 0.6

By linearity of expectation:

E[Y] = E[X₁ + X₂ + X₃] = E[X₁] + E[X₂] + E[X₃]

E[Y] = 0.6 + 0.6 + 0.6 = 1.8

**Answer: 1.8 stocks**

**Interpretation:**

On average, you expect 1.8 of your 3 stocks to have positive returns.

Of course, on any given day:
- You'll observe 0, 1, 2, or 3 stocks with positive returns (not 1.8)
- But over many days, the average will be 1.8

**Key Property of Linearity of Expectation:**

E[X + Y] = E[X] + E[Y] **always holds**, even if X and Y are dependent!

We didn't need to know whether the stock returns are correlated. This makes linearity of expectation extremely powerful for calculations.
