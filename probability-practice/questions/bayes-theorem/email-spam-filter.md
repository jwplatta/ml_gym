---
subject: bayes-theorem
difficulty: EASY
quality: GOOD
---
# Email Spam Filter
## Question
An email filter analyzes incoming messages. Based on historical data:
- 30% of all emails are spam
- 70% of all emails are legitimate

The filter flags emails as "Suspicious" based on certain keywords:
- P(Flagged | Spam) = 0.85 (true positive rate)
- P(Flagged | Legitimate) = 0.15 (false positive rate)

**Question:** If an email is flagged as suspicious, what is the probability it's actually spam?
## Solution
**Step 1: Calculate P(Flagged) using law of total probability**

P(Flagged) = P(Flagged | Spam) × P(Spam) + P(Flagged | Legitimate) × P(Legitimate)

P(Flagged) = (0.85)(0.3) + (0.15)(0.7)

P(Flagged) = 0.255 + 0.105 = 0.36

**Step 2: Apply Bayes' theorem**

P(Spam | Flagged) = P(Flagged | Spam) × P(Spam) / P(Flagged)

P(Spam | Flagged) = (0.85)(0.3) / 0.36

P(Spam | Flagged) = 0.255 / 0.36 = 17/24 ≈ 0.708

**Answer: 17/24 ≈ 0.708 or about 70.8%**

**Interpretation:** About 71% of flagged emails are actually spam, while 29% are false positives (legitimate emails incorrectly flagged).
