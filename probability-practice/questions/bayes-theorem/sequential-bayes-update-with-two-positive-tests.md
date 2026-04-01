---
subject: bayes-theorem
difficulty: MEDIUM
quality: AVERAGE
---
# Sequential Bayes Update with Two Positive Tests
## Question
Let D denote the event that a patient has a disease.

Suppose: P(D) = 0.02, P(not D) = 0.98

A medical test satisfies: P(Pos | D) = 0.95, P(Pos | not D) = 0.10

Assume two independent tests are administered.

Compute: P(D | Pos1, Pos2)
## Solution
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
