---
subject: total-probability
difficulty: VERY EASY
quality: AVERAGE
---
# Easy - Portfolio Returns Based on Market State
## Question
A portfolio's return depends on the market state. There are three possible states:
- Bull market: P(Bull) = 0.4
- Neutral market: P(Neutral) = 0.4
- Bear market: P(Bear) = 0.2

The probability of a positive return in each state:
- P(Positive Return | Bull) = 0.8
- P(Positive Return | Neutral) = 0.5
- P(Positive Return | Bear) = 0.2

What is the overall probability of a positive return?
## Solution
Using the law of total probability:

P(Positive Return) = P(PR | Bull) × P(Bull) + P(PR | Neutral) × P(Neutral) + P(PR | Bear) × P(Bear)

P(Positive Return) = (0.8)(0.4) + (0.5)(0.4) + (0.2)(0.2)

P(Positive Return) = 0.32 + 0.20 + 0.04

P(Positive Return) = 0.56

**Answer: 0.56 or 56%**

**Interpretation:**

The overall probability of a positive return is 56%, which is a weighted average of the three market states:
- Bull market contributes: 0.32 (32 percentage points)
- Neutral market contributes: 0.20 (20 percentage points)
- Bear market contributes: 0.04 (4 percentage points)

**Key Insight:** The law of total probability allows us to compute the probability of an event by partitioning the sample space into mutually exclusive scenarios and summing their contributions.
