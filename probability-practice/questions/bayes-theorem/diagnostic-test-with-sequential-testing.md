---
subject: bayes-theorem
difficulty: MEDIUM
quality: GOOD
---
# Diagnostic Test with Sequential Testing
## Question
A disease affects 2% of the population. A new test has:
- Sensitivity: 95% (P(Positive | Disease) = 0.95)
- Specificity: 90% (P(Negative | No Disease) = 0.90)

**Questions:**
1. If a person tests positive, what is the probability they have the disease?
2. If a person tests positive on the first test and takes a second independent test that also comes back positive, what is the probability they have the disease?

*Assume the second test has the same accuracy and is independent given disease status.*
## Solution
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
