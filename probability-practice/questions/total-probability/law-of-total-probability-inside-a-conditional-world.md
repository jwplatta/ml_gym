---
subject: total-probability
difficulty: EASY
quality: GOOD
---
# Law of Total Probability Inside a Conditional World
## Question
A factory produces electronic chips. Let D denote the event that a chip is defective.

Suppose: P(D) = 0.1, P(not D) = 0.9

Each chip is tested once. Let T1 be the event that the first test flags the chip as defective.

P(T1 | D) = 0.9, P(T1 | not D) = 0.05

Assume tests are conditionally independent given defect status.

Suppose the first test flagged the chip as defective.

Compute: P(T2 | T1)
## Solution
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
