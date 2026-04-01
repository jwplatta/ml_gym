---
subject: bayes-theorem
difficulty: MEDIUM
quality: AVERAGE
---
# Venture Capital Investment with Multiple Questions
## Question
A venture capital firm evaluates startup investments. Historical data shows:
- 60% of startups are in the "Tech" sector
- 40% of startups are in the "Healthcare" sector

The success rates differ by sector:
- P(Success | Tech) = 0.3
- P(Success | Healthcare) = 0.5

1. What is the overall probability that a randomly selected startup succeeds?
2. If a startup succeeds, what is the probability it was a Healthcare startup?
3. If the firm invests in 10 startups with the same success probabilities as above, what is the expected number of successful investments?
## Solution
**Part 1: Overall success probability (Law of Total Probability)**

P(Success) = P(Success | Tech) × P(Tech) + P(Success | Healthcare) × P(Healthcare)

P(Success) = (0.3)(0.6) + (0.5)(0.4)

P(Success) = 0.18 + 0.20 = 0.38

**Answer: 0.38 or 38%**

**Part 2: Probability of Healthcare given success (Bayes' Theorem)**

P(Healthcare | Success) = P(Success | Healthcare) × P(Healthcare) / P(Success)

P(Healthcare | Success) = (0.5)(0.4) / 0.38

P(Healthcare | Success) = 0.20 / 0.38 = 10/19 ≈ 0.526

**Answer: 10/19 ≈ 0.526 or about 52.6%**

**Part 3: Expected number of successes (Linearity of Expectation)**

Let Xᵢ be an indicator variable for startup i succeeding.

Total successes Y = X₁ + X₂ + ... + X₁₀

Each startup has the same success probability from Part 1:
E[Xᵢ] = P(Success) = 0.38

By linearity of expectation:
E[Y] = E[X₁] + E[X₂] + ... + E[X₁₀]

E[Y] = 10 × 0.38 = 3.8

**Answer: 3.8 successful investments expected**

**Summary:**
- Overall success rate: 38%
- Successful startups are slightly more likely to be Healthcare (52.6%) than Tech (47.4%), even though Tech makes up 60% of all startups
- This happens because Healthcare startups have a higher success rate (50% vs 30%)
- Out of 10 investments, expect about 3.8 to succeed on average

**Difficulty:** EASY
**Quality:** GOOD
**Source:** probability_mixed_easy_20260212.ipynb
