---
subject: expectation
difficulty: MEDIUM
quality: AVERAGE
---
# Investment Fund Performance
## Question
An investment fund can be in one of three states each quarter:
- **Outperform** (beats benchmark): probability 0.4
- **Match** (equals benchmark): probability 0.3
- **Underperform** (below benchmark): probability 0.3

The quarterly returns depend on performance:
- If Outperform: return is Uniform[8%, 15%]
- If Match: return is exactly 6%
- If Underperform: return is Uniform[0%, 5%]

**Questions:**
1. What is the expected quarterly return?
2. If the fund returned 10% this quarter, what is the probability it outperformed?
3. If the fund returned 4% this quarter, what is the probability it underperformed?
## Solution
**Part 1: Expected quarterly return**

For Uniform[a, b], the expected value is (a + b) / 2:

E[Return | Outperform] = (8% + 15%) / 2 = 11.5%

E[Return | Match] = 6%

E[Return | Underperform] = (0% + 5%) / 2 = 2.5%

Using law of total expectation:

E[Return] = E[R | O] × P(O) + E[R | M] × P(M) + E[R | U] × P(U)

E[Return] = (11.5%)(0.4) + (6%)(0.3) + (2.5%)(0.3)

E[Return] = 4.6% + 1.8% + 0.75% = 7.15%

**Answer: 7.15%**

**Part 2: P(Outperform | Return = 10%)**

A 10% return can only occur in the Outperform state (since 10% ∈ [8%, 15%]).

The Match state gives exactly 6%, and Underperform gives [0%, 5%], so neither can produce 10%.

Therefore: P(Outperform | Return = 10%) = 1

**Answer: 1 or 100%**

**Part 3: P(Underperform | Return = 4%)**

A 4% return could come from:
- Outperform: No (4% ∉ [8%, 15%])
- Match: No (Match = 6% exactly)
- Underperform: Yes (4% ∈ [0%, 5%])

Since 4% can only occur in the Underperform state:

P(Underperform | Return = 4%) = 1

**Answer: 1 or 100%**

**Alternative rigorous approach for Part 3 (using densities):**

For continuous distributions, we use:

P(State | Return = r) = f(r | State) × P(State) / f(r)

For Uniform[a, b], the pdf is 1/(b-a) for x ∈ [a, b], and 0 otherwise.

f(4% | Underperform) = 1/(5% - 0%) = 1/0.05 = 20 (density, not probability)

f(4% | Outperform) = 0 (since 4% ∉ [8%, 15%])

f(4% | Match) = 0 (since Match is exactly 6%)

f(4%) = f(4% | O) × P(O) + f(4% | M) × P(M) + f(4% | U) × P(U)

f(4%) = 0 × 0.4 + 0 × 0.3 + 20 × 0.3 = 6

P(Underperform | 4%) = (20)(0.3) / 6 = 6 / 6 = 1 ✓

**Key Insight:** When using Bayes with continuous distributions, non-overlapping ranges can make certain states impossible, giving probability 1 to the only possible state.
