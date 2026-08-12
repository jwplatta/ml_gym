## Basic Bayes' Rule Application

Given the following contingency table for disease screening:

|              | Positive Test (B) | Negative Test (¬B) | Total |
|--------------|------------------|-------------------|-------|
| Disease (A)  | 90               | 10                | 100   |
| No Disease (¬A) | 50            | 850               | 900   |
| **Total**    | **140**          | **860**           | **1000** |

You know B occurred (test is positive). Use Bayes' rule to find P(A | B) from P(B | A), P(A), and P(B).

### Solution

**Step 1: Calculate components**

P(B | A) = 90/100 = 0.90 (sensitivity)

P(A) = 100/1000 = 0.10 (prevalence)

P(B) = 140/1000 = 0.14

**Step 2: Apply Bayes' rule**

P(A | B) = P(B | A) × P(A) / P(B)
         = (0.90) × (0.10) / (0.14)
         = 0.09 / 0.14
         = 9/14
         ≈ 0.643

**Answer: 9/14 ≈ 0.643 or about 64.3%**

**Interpretation:** If the test is positive, there's a 64% chance of actually having the disease.

### Notes

- Quality: GOOD
- Difficulty: VERY EASY
- Notes: Basic introduction to Bayes' rule; demonstrates calculation from contingency table

## Verifying Bayes' Rule

Given the following contingency table for customer behavior:

|              | Purchased (B) | No Purchase (¬B) | Total |
|--------------|---------------|------------------|-------|
| Ad Click (A) | 45            | 15               | 60    |
| No Click (¬A) | 15           | 25               | 40    |
| **Total**    | **60**        | **40**           | **100** |

Compute P(B | A) directly. Then verify using Bayes' rule: P(B | A) = P(A | B) × P(B) / P(A).

### Solution

**Direct calculation:**

P(B | A) = 45/60 = 3/4 = 0.75

**Verification using Bayes' rule:**

P(A | B) = 45/60 = 3/4 = 0.75

P(B) = 60/100 = 3/5 = 0.60

P(A) = 60/100 = 3/5 = 0.60

P(B | A) = P(A | B) × P(B) / P(A)
         = (3/4) × (3/5) / (3/5)
         = 3/4
         = 0.75 ✓

**Both methods give P(B | A) = 0.75**

### Notes

- Quality: EXCELLENT
- Difficulty: EASY
- Notes: Demonstrates equivalence of direct calculation and Bayes' rule; reinforces understanding

## Bayesian Updating Framework

Given the following contingency table for email classification:

|              | Spam (B) | Not Spam (¬B) | Total |
|--------------|----------|---------------|-------|
| Contains "Free" (A) | 80 | 40         | 120   |
| No "Free" (¬A) | 20    | 60            | 80    |
| **Total**    | **100**  | **100**       | **200** |

Suppose you observe event B (email is spam). Use Bayes' theorem to update your belief about A:
- Prior: P(A) = ?
- Likelihood: P(B | A) = ?
- Evidence: P(B) = ?
- Posterior: P(A | B) = ?

### Solution

**Prior: P(A)**

P(A) = 120/200 = 3/5 = 0.60

**Likelihood: P(B | A)**

P(B | A) = 80/120 = 2/3 ≈ 0.667

**Evidence: P(B)**

P(B) = 100/200 = 1/2 = 0.50

**Posterior: P(A | B)**

P(A | B) = P(B | A) × P(A) / P(B)
         = (2/3) × (3/5) / (1/2)
         = (2/5) / (1/2)
         = 4/5
         = 0.80

**Answer: P(A | B) = 4/5 = 0.80 or 80%**

**Interpretation:** If we know an email is spam, there's an 80% probability it contains the word "Free". This is higher than the prior 60%, showing that spam emails are more likely to contain "Free".

### Notes

- Quality: EXCELLENT
- Difficulty: EASY
- Notes: Demonstrates Bayesian updating framework with prior, likelihood, evidence, and posterior; clear interpretation

## Odds Ratio Calculation

Given the following contingency table for treatment effectiveness:

|              | Improved (B) | No Improvement (¬B) | Total |
|--------------|--------------|---------------------|-------|
| Treatment (A) | 60          | 20                  | 80    |
| Control (¬A) | 30           | 90                  | 120   |
| **Total**    | **90**       | **110**             | **200** |

Compute the odds ratio: [P(A|B) / P(¬A|B)] / [P(A|¬B) / P(¬A|¬B)]. This measures how much B affects the odds of A.

### Solution

**Odds of A given B:**

P(A | B) = 60/90 = 2/3

P(¬A | B) = 30/90 = 1/3

Odds(A | B) = (2/3) / (1/3) = 2

**Odds of A given ¬B:**

P(A | ¬B) = 20/110 = 2/11

P(¬A | ¬B) = 90/110 = 9/11

Odds(A | ¬B) = (2/11) / (9/11) = 2/9

**Odds Ratio:**

OR = Odds(A | B) / Odds(A | ¬B) = 2 / (2/9) = 2 × (9/2) = 9

**Answer: Odds Ratio = 9**

**Interpretation:** The odds of having received treatment are 9 times higher among those who improved compared to those who didn't improve.

### Notes

- Quality: GOOD
- Difficulty: MEDIUM
- Notes: Demonstrates odds ratio calculation; important measure of association

## Symmetry in Bayes' Theorem

Given the following contingency table for customer segments:

|              | High Value (B) | Low Value (¬B) | Total |
|--------------|----------------|----------------|-------|
| Loyalty Member (A) | 70 | 30          | 100   |
| Non-Member (¬A) | 20   | 80            | 100   |
| **Total**    | **90**         | **110**        | **200** |

Show that P(A | B) > P(A) if and only if P(B | A) > P(B). Verify using the table.

### Solution

**Test P(A | B) vs P(A):**

P(A) = 100/200 = 0.50

P(A | B) = 70/90 = 7/9 ≈ 0.778

Comparison: P(A | B) = 0.778 > 0.50 = P(A) ✓

**Test P(B | A) vs P(B):**

P(B) = 90/200 = 0.45

P(B | A) = 70/100 = 0.70

Comparison: P(B | A) = 0.70 > 0.45 = P(B) ✓

**Verified:** Both inequalities go in the same direction (both ">")

**Key Insight:** This symmetry property shows that if knowing B makes A more likely, then knowing A makes B more likely. They increase each other's probabilities.

### Notes

- Quality: EXCELLENT
- Difficulty: MEDIUM
- Notes: Demonstrates important symmetry property in Bayes' theorem; conceptually important

## Law of Total Probability with Bayes' Rule

Given the following contingency table for product quality:

|              | Defective (B) | Good (¬B) | Total |
|--------------|---------------|-----------|-------|
| Factory 1 (A) | 12           | 88        | 100   |
| Factory 2 (¬A) | 18          | 132       | 150   |
| **Total**    | **30**        | **220**   | **250** |

Use the law of total probability to compute P(B) from P(B | A) and P(B | ¬A):
P(B) = P(B | A) × P(A) + P(B | ¬A) × P(¬A)

Then use this with Bayes' rule to find P(A | B).

### Solution

**Step 1: Calculate conditional probabilities**

P(B | A) = 12/100 = 0.12

P(A) = 100/250 = 2/5 = 0.40

P(B | ¬A) = 18/150 = 3/25 = 0.12

P(¬A) = 150/250 = 3/5 = 0.60

**Step 2: Apply law of total probability**

P(B) = P(B | A) × P(A) + P(B | ¬A) × P(¬A)
     = (0.12)(0.40) + (0.12)(0.60)
     = 0.048 + 0.072
     = 0.12

**Verification:** From table, P(B) = 30/250 = 0.12 ✓

**Step 3: Apply Bayes' rule**

P(A | B) = P(B | A) × P(A) / P(B)
         = (0.12)(0.40) / (0.12)
         = 0.048 / 0.12
         = 0.40

**Answer: P(A | B) = 0.40 or 40%**

**Interpretation:** Even knowing a product is defective doesn't change the probability it came from Factory 1 (still 40%), because both factories have the same defect rate (12%).

### Notes

- Quality: GOOD
- Difficulty: MEDIUM
- Notes: Combines law of total probability with Bayes' rule; shows case where posterior equals prior when likelihoods are equal

## Credit Card Fraud Detection

A credit card company's fraud detection system analyzes transactions:
- 0.1% of all transactions are fraudulent (P(Fraud) = 0.001)
- 99.9% of transactions are legitimate (P(Legitimate) = 0.999)

The system flags suspicious transactions:
- P(Flagged | Fraud) = 0.99 (catches 99% of fraud)
- P(Flagged | Legitimate) = 0.02 (2% false positive rate)

If a transaction is flagged, what is the probability it's actually fraudulent?

### Solution

**Step 1: Calculate P(Flagged) using law of total probability**

P(Flagged) = P(Flagged | Fraud) × P(Fraud) + P(Flagged | Legitimate) × P(Legitimate)

P(Flagged) = (0.99)(0.001) + (0.02)(0.999)

P(Flagged) = 0.00099 + 0.01998 = 0.02097

**Step 2: Apply Bayes' theorem**

P(Fraud | Flagged) = P(Flagged | Fraud) × P(Fraud) / P(Flagged)

P(Fraud | Flagged) = (0.99)(0.001) / 0.02097

P(Fraud | Flagged) = 0.00099 / 0.02097 ≈ 0.0472

**Answer: ≈ 0.047 or about 4.7%**

**Interpretation:**

Even with a highly accurate fraud detector (99% detection rate), only about 4.7% of flagged transactions are actually fraudulent!

This happens because:
- Fraud is very rare (0.1% base rate)
- There are many legitimate transactions (99.9%)
- Even a small 2% false positive rate on legitimate transactions generates many false alarms

**Prior vs Posterior:**
- Prior: P(Fraud) = 0.1%
- Posterior: P(Fraud | Flagged) = 4.7%
- The flagged indicator increases our belief in fraud by ~47x, but it's still unlikely!

**Difficulty:** EASY
**Quality:** GOOD
**Source:** probability_mixed_easy_20260212.ipynb

## Venture Capital Investment with Multiple Questions

A venture capital firm evaluates startup investments. Historical data shows:
- 60% of startups are in the "Tech" sector
- 40% of startups are in the "Healthcare" sector

The success rates differ by sector:
- P(Success | Tech) = 0.3
- P(Success | Healthcare) = 0.5

1. What is the overall probability that a randomly selected startup succeeds?
2. If a startup succeeds, what is the probability it was a Healthcare startup?
3. If the firm invests in 10 startups with the same success probabilities as above, what is the expected number of successful investments?

### Solution

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

## Sequential Bayes Update with Two Positive Tests

Let D denote the event that a patient has a disease.

Suppose: P(D) = 0.02, P(not D) = 0.98

A medical test satisfies: P(Pos | D) = 0.95, P(Pos | not D) = 0.10

Assume two independent tests are administered.

Compute: P(D | Pos1, Pos2)

### Solution

First update after the first positive:

P(D | Pos1) = P(Pos1 | D) P(D) / P(Pos1)

where

P(Pos1) = 0.95 * 0.02 + 0.10 * 0.98 = 0.019 + 0.098 = 0.117

So:

P(D | Pos1) = 0.019 / 0.117 ≈ 0.1624

Now apply Bayes again using Pos2:

P(D | Pos1, Pos2) = P(Pos2 | D) P(D | Pos1) / P(Pos2 | Pos1)

Compute the denominator using the law of total probability:

P(Pos2 | Pos1) = 0.95 * 0.1624 + 0.10 * (1 − 0.1624) = 0.1543 + 0.0838 = 0.2381

Thus:

P(D | Pos1, Pos2) = (0.95 * 0.1624) / 0.2381 = 0.1543 / 0.2381 ≈ 0.648

So after two independent positive tests, the posterior probability is approximately 0.648, or 64.8%.

## Diagnostic Test with Sequential Testing

A disease affects 2% of the population. A new test has:
- Sensitivity: 95% (P(Positive | Disease) = 0.95)
- Specificity: 90% (P(Negative | No Disease) = 0.90)

**Questions:**
1. If a person tests positive, what is the probability they have the disease?
2. If a person tests positive on the first test and takes a second independent test that also comes back positive, what is the probability they have the disease?

*Assume the second test has the same accuracy and is independent given disease status.*

### Solution

**Part 1: P(Disease | Positive)**

First, find P(Positive) using law of total probability:

P(Positive) = P(Pos | Disease) × P(Disease) + P(Pos | No Disease) × P(No Disease)

P(Pos | No Disease) = 1 - Specificity = 1 - 0.90 = 0.10

P(Positive) = (0.95)(0.02) + (0.10)(0.98)

P(Positive) = 0.019 + 0.098 = 0.117

Now apply Bayes' theorem:

P(Disease | Positive) = P(Pos | Disease) × P(Disease) / P(Positive)

P(Disease | Positive) = (0.95)(0.02) / 0.117

P(Disease | Positive) = 0.019 / 0.117 ≈ 0.1624

**Answer: ≈ 0.162 or about 16.2%**

**Part 2: P(Disease | Two Positive Tests)**

After the first positive test, our updated probability is 0.1624.

Now use this as the prior for the second test:

P(Disease after 1st test) = 0.1624
P(No Disease after 1st test) = 1 - 0.1624 = 0.8376

Find P(2nd Pos | 1st Pos) using law of total probability:

P(2nd Pos | 1st Pos) = P(2nd Pos | Disease) × P(Disease | 1st Pos) + P(2nd Pos | No Disease) × P(No Disease | 1st Pos)

P(2nd Pos | 1st Pos) = (0.95)(0.1624) + (0.10)(0.8376)

P(2nd Pos | 1st Pos) = 0.1543 + 0.0838 = 0.2381

Apply Bayes' theorem:

P(Disease | Both Positive) = P(2nd Pos | Disease) × P(Disease | 1st Pos) / P(2nd Pos | 1st Pos)

P(Disease | Both Positive) = (0.95)(0.1624) / 0.2381

P(Disease | Both Positive) = 0.1543 / 0.2381 ≈ 0.648

**Answer: ≈ 0.648 or about 64.8%**

**Interpretation:**
- One positive test: 16.2% chance of disease
- Two positive tests: 64.8% chance of disease
- Sequential testing significantly increases diagnostic confidence
- This is Bayesian updating in action - each test updates our belief

**Key Insight:** Sequential Bayes - the posterior from one test becomes the prior for the next test.

### Notes

- Quality: GOOD
- Difficulty: MEDIUM
- Notes: Good question that tests Bayes theorem and conditional independence of events; demonstrates sequential Bayesian updating