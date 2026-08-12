## Law of Total Probability - Computing Marginal from Conditionals

Given the following contingency table for medical test results:

|         | Test + (B) | Test - (¬B) | Total |
|---------|------------|-------------|-------|
| Disease (A) | 30 | 20 | 50 |
| No Disease (¬A) | 15 | 35 | 50 |
| **Total** | **45** | **55** | **100** |

Use the law of total probability to compute P(B) from P(B | A) and P(B | ¬A):

P(B) = P(B | A) × P(A) + P(B | ¬A) × P(¬A)

### Solution

P(B | A) = 30/50 = 0.6
P(A) = 50/100 = 0.5
P(B | ¬A) = 15/50 = 0.3
P(¬A) = 50/100 = 0.5

P(B) = (30/50) × (50/100) + (15/50) × (50/100)
     = 30/100 + 15/100
     = 45/100 = 0.45

Verify: From the table, P(B) = 45/100 = 0.45 ✓

**Key Insight:** The law of total probability allows us to compute marginal probabilities by partitioning on any event and using conditional probabilities.

### Notes

- Quality: GOOD
- Difficulty: VERY EASY
- Notes: Clear demonstration of law of total probability with medical test context

## Computing Marginal Probability by Partitioning

Given the following contingency table for stock performance and economic conditions:

|                 | High Growth (B) | Low Growth (¬B) | Total |
|-----------------|-----------------|-----------------|-------|
| Good Economy (A) | 40 | 10 | 50 |
| Bad Economy (¬A) | 10 | 40 | 50 |
| **Total** | **50** | **50** | **100** |

Express P(A) using the law of total probability by partitioning on B:

P(A) = P(A | B) × P(B) + P(A | ¬B) × P(¬B)

### Solution

P(A | B) = 40/50 = 0.8
P(B) = 50/100 = 0.5
P(A | ¬B) = 10/50 = 0.2
P(¬B) = 50/100 = 0.5

P(A) = (40/50) × (50/100) + (10/50) × (50/100)
     = 40/100 + 10/100
     = 50/100 = 0.5

Verify: From the table, P(A) = 50/100 = 0.5 ✓

**Key Insight:** We can partition on any event to compute marginals. Here we partition on growth to compute the probability of good economy.

### Notes

- Quality: GOOD
- Difficulty: VERY EASY
- Notes: Demonstrates symmetry and flexibility of law of total probability

## Easy - Portfolio Returns Based on Market State

A portfolio's return depends on the market state. There are three possible states:
- Bull market: P(Bull) = 0.4
- Neutral market: P(Neutral) = 0.4
- Bear market: P(Bear) = 0.2

The probability of a positive return in each state:
- P(Positive Return | Bull) = 0.8
- P(Positive Return | Neutral) = 0.5
- P(Positive Return | Bear) = 0.2

What is the overall probability of a positive return?

### Solution

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

### Notes

- Quality: AVERAGE
- Difficulty: VERY EASY
- Notes: Good financial application topic
- Source: probability_mixed_easy_20260212.ipynb

## Law of Total Probability with Condiational Probabilities

A factory produces light bulbs. 10% are defective (D), 90% are not defective (¬D). Each bulb is inspected twice.
- If a bulb is defective, each inspection independently flags it as “bad” with probability 0.9.
- If a bulb is not defective, each inspection independently flags it as “bad” with probability 0.05.

Suppose the first inspection flagged the bulb as bad. What is the probability that the second inspection also flags it as bad?

### Solution

P(Bad₂ | Bad₁)

Using the law of total probability inside the conditional world where Bad₁ has already happened:

P(Bad₂ | Bad₁) = P(Bad₂ | D, Bad₁) P(D | Bad₁) + P(Bad₂ | ¬D, Bad₁) P(¬D | Bad₁)

This step is always valid — we’re partitioning on D vs ¬D while conditioning on Bad₁. Then, using conditional independence of inspections given defect status:

P(Bad₂ | D, Bad₁) = P(Bad₂ | D) = 0.9
P(Bad₂ | ¬D, Bad₁) = P(Bad₂ | ¬D) = 0.05

So: P(Bad₂ | Bad₁) = 0.9 · P(D | Bad₁) + 0.05 · P(¬D | Bad₁)

That is exactly the law of total probability operating "inside" a conditional world.

The structure is always:

P(A | B) = P(A | C, B) P(C | B) + P(A | ¬C, B) P(¬C | B)

You're just slicing uncertainty about C after already assuming B happened.

### Notes

- Quality: EXCELLENT
- Difficulty: EASY
- Notes: Advanced application showing law of total probability operating inside a conditional world

## Law of Total Probability Inside a Conditional World

A factory produces electronic chips. Let D denote the event that a chip is defective.

Suppose: P(D) = 0.1, P(not D) = 0.9

Each chip is tested once. Let T1 be the event that the first test flags the chip as defective.

P(T1 | D) = 0.9, P(T1 | not D) = 0.05

Assume tests are conditionally independent given defect status.

Suppose the first test flagged the chip as defective.

Compute: P(T2 | T1)

### Solution

Apply the law of total probability inside the conditional world where T1 has occurred:

P(T2 | T1) = P(T2 | D, T1) P(D | T1) + P(T2 | not D, T1) P(not D | T1)

By conditional independence:

P(T2 | D, T1) = P(T2 | D) = 0.9

P(T2 | not D, T1) = P(T2 | not D) = 0.05

So:

P(T2 | T1) = 0.9 P(D | T1) + 0.05 P(not D | T1)

Now compute P(D | T1) using Bayes:

P(D | T1) = (0.9 * 0.1) / (0.9 * 0.1 + 0.05 * 0.9) = 0.09 / 0.135 = 2/3

Thus:

P(T2 | T1) = 0.9 * (2/3) + 0.05 * (1/3) = 0.6 + 0.0167 = 0.6167

### Notes

- Quality: EXCELLENT
- Difficulty: EASY
- Notes: Excellent example combining Bayes theorem with law of total probability in conditional settings