# Expectation

## Expectation of Indicator Variable

Given the following contingency table for customer churn:

|              | Churned (B) | Retained (¬B) | Total |
|--------------|-------------|---------------|-------|
| Unhappy (A)  | 40          | 10            | 50    |
| Happy (¬A)   | 10          | 90            | 100   |
| **Total**    | **50**      | **100**       | **150** |

Let X be an indicator variable for event A (X=1 if customer is unhappy, X=0 otherwise). Compute E[X].

### Solution

X = 1 with probability P(A) = 50/150 = 1/3

X = 0 with probability P(¬A) = 100/150 = 2/3

E[X] = 1 × P(A) + 0 × P(¬A)
     = 1 × (1/3) + 0 × (2/3)
     = 1/3
     ≈ 0.333

**Answer: 1/3 ≈ 0.333**

**Key insight:** The expected value of an indicator variable equals the probability of the event. E[indicator of A] = P(A).

### Notes

- Quality: GOOD
- Difficulty: VERY EASY
- Notes: Fundamental property connecting expectation and probability for indicator variables

## Expectation of Scaled Indicator

Given the following contingency table for product sales:

|              | Premium (B) | Standard (¬B) | Total |
|--------------|-------------|---------------|-------|
| Corporate (A) | 60         | 40            | 100   |
| Individual (¬A) | 20        | 80            | 100   |
| **Total**    | **80**      | **120**       | **200** |

Let Y be a random variable that equals 10 if B occurs (premium sale) and 0 otherwise. Compute E[Y].

### Solution

Y = 10 with probability P(B) = 80/200 = 2/5 = 0.40

Y = 0 with probability P(¬B) = 120/200 = 3/5 = 0.60

E[Y] = 10 × (0.40) + 0 × (0.60)
     = 4 + 0
     = 4

**Answer: 4**

**Interpretation:** On average, each sale generates an expected value of 4 from the premium indicator (10 points if premium, 0 otherwise).

### Notes

- Quality: GOOD
- Difficulty: VERY EASY
- Notes: Demonstrates scaling of indicator variables; E[cX] = cE[X]

## Linearity of Expectation

Given the following contingency table for employee benefits:

|              | Health Plan (B) | No Health Plan (¬B) | Total |
|--------------|-----------------|---------------------|-------|
| Full-time (A) | 70             | 10                  | 80    |
| Part-time (¬A) | 10            | 10                  | 20    |
| **Total**    | **80**          | **20**              | **100** |

Let X and Y be indicator variables for events A and B respectively. Compute E[X + Y] using linearity of expectation.

### Solution

E[X] = P(A) = 80/100 = 0.80

E[Y] = P(B) = 80/100 = 0.80

By linearity of expectation:

E[X + Y] = E[X] + E[Y]
         = 0.80 + 0.80
         = 1.60

**Answer: 1.60**

**Key Property:** Linearity of expectation holds for **any** random variables, even if they're dependent! We didn't need to check whether A and B are independent.

### Notes

- Quality: EXCELLENT
- Difficulty: EASY
- Notes: Demonstrates linearity of expectation; works regardless of dependence

## Multi-Value Random Variable

Given the following contingency table for project outcomes:

|              | Success (B) | Failure (¬B) | Total |
|--------------|-------------|--------------|-------|
| Experienced (A) | 48        | 12           | 60    |
| Novice (¬A) | 12           | 28           | 40    |
| **Total**    | **60**       | **40**       | **100** |

Define a random variable Z that takes value 100 if both A and B occur, 50 if exactly one occurs, and 0 if neither occurs. Compute E[Z].

### Solution

**Step 1: Find probabilities**

P(Z = 100) = P(A ∩ B) = 48/100 = 0.48

P(Z = 50) = P(A ∩ ¬B) + P(¬A ∩ B)
          = 12/100 + 12/100
          = 24/100
          = 0.24

P(Z = 0) = P(¬A ∩ ¬B) = 28/100 = 0.28

**Step 2: Calculate expectation**

E[Z] = 100 × (0.48) + 50 × (0.24) + 0 × (0.28)
     = 48 + 12 + 0
     = 60

**Answer: 60**

**Interpretation:** On average, the random variable Z takes value 60, even though it never actually equals 60 (it's always 0, 50, or 100).

### Notes

- Quality: GOOD
- Difficulty: EASY
- Notes: Demonstrates expectation of multi-valued random variable from contingency table

## Indicator Variable Property
Consider flipping a fair coin. Let X be an indicator variable:
- X = 1 if the coin lands heads
- X = 0 if the coin lands tails

Calculate E[X].

### Solution

E[X] = 1 × P(X = 1) + 0 × P(X = 0)

E[X] = 1 × P(Heads) + 0 × P(Tails)

E[X] = 1 × (1/2) + 0 × (1/2)

E[X] = 1/2 = 0.5

**Answer: 0.5**

**Key Insight:** For any indicator variable, E[indicator of A] = P(A). This is an extremely useful property that simplifies many calculations!

In this case: E[X] = P(Heads) = 0.5

### Notes

- Quality: EXCELLENT
- Difficulty: VERY EASY
- Notes: Fundamental concept in probability; the expected value of an indicator random variable equals the probability of the event it indicates

## Lottery Ticket
You buy a lottery ticket for $5. The ticket has the following payouts:
- Win $100 with probability 0.01
- Win $20 with probability 0.05
- Win $0 with probability 0.94

**Questions:**
1. What is the expected value of your winnings (before subtracting the ticket cost)?
2. What is your expected net gain (after subtracting the $5 ticket cost)?

### Solution

**Part 1: Expected winnings**

E[Winnings] = 100 × (0.01) + 20 × (0.05) + 0 × (0.94)

E[Winnings] = 1 + 1 + 0 = 2

**Answer: $2**

**Part 2: Expected net gain**

Net Gain = Winnings - 5

E[Net Gain] = E[Winnings - 5] = E[Winnings] - 5 = 2 - 5 = -3

**Answer: -$3**

**Interpretation:** On average, you expect to win $2, but since you paid $5 for the ticket, your expected net loss is $3. This is an unfavorable game for the player (as most lotteries are!).

**Key Insight:** This demonstrates the linearity of expectation property: E[aX + b] = aE[X] + b. The expected value of your net gain is simply the expected winnings minus the constant ticket cost.

### Notes

- Quality: GOOD
- Difficulty: EASY
- Notes: Practical application demonstrating linearity of expectation with constants

## Binary Outcome Bet
A trader makes a bet on a coin flip:
- If heads (probability 0.5): win $20
- If tails (probability 0.5): lose $10

**Questions:**
1. What is the expected value of this bet?
2. Is this a favorable bet?

### Solution

**Part 1: Expected value**

Let X = the outcome of the bet.

E[X] = 20 × P(Heads) + (-10) × P(Tails)

E[X] = 20 × (0.5) + (-10) × (0.5)

E[X] = 10 - 5 = 5

**Answer: $5**

**Part 2: Is this favorable?**

Yes! Since E[X] = $5 > 0, this is a favorable bet.

On average, you expect to gain $5 per bet. Over many repetitions, you would make money.

**Interpretation:**
- You won't always win $5 (you'll either win $20 or lose $10 on each individual bet)
- But over many bets, your average gain will converge to $5 per bet
- The asymmetric payoffs ($20 vs -$10) make this favorable despite 50/50 odds

### Notes

- Quality: AVERAGE
- Difficulty: VERY EASY
- Notes: Demonstrates expected value with asymmetric payoffs
- Source: probability_mixed_easy_20260212.ipynb

## Indicator Variable for Dividend
Consider a stock that pays a dividend. Let D be an indicator variable:
- D = 1 if the stock pays a dividend (probability 0.7)
- D = 0 if no dividend (probability 0.3)

**Question:** What is E[D]?

### Solution

E[D] = 1 × P(D=1) + 0 × P(D=0)

E[D] = 1 × (0.7) + 0 × (0.3)

E[D] = 0.7

**Answer: 0.7**

**Key Insight:**

For any indicator variable (Bernoulli random variable):
```
E[indicator of event A] = P(A)
```

This is an extremely useful property! It means:
- Expected value of indicator = probability of the event
- You can think of probability as "expected proportion of times the event occurs"

**Example applications:**
- E[indicator of heads] = P(Heads) = 0.5
- E[indicator of dividend] = P(Dividend) = 0.7
- E[indicator of default] = P(Default)

### Notes

- Quality: AVERAGE
- Difficulty: VERY EASY
- Notes: Reinforces fundamental property of indicator variables
- Source: probability_mixed_easy_20260212.ipynb

## Linearity of Expectation with Portfolio
A portfolio contains 3 stocks. Each stock has a probability of 0.6 of having a positive return tomorrow.

Let X₁, X₂, X₃ be indicator variables (= 1 if stock has positive return, 0 otherwise).

**Question:** What is the expected number of stocks with positive returns? Use linearity of expectation.

### Solution

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

### Notes

- Quality: AVERAGE
- Difficulty: VERY EASY
- Notes: Demonstrates linearity of expectation with multiple indicator variables
- Source: probability_mixed_easy_20260212.ipynb

## Investment Fund Performance

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

### Solution

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

### Notes

- Quality: LOW
- Difficulty: MEDIUM
- Notes: Good idea but parts 2 and 3 are confusing and ultimately too easy since the return ranges don't overlap