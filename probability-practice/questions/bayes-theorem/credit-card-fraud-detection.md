---
subject: bayes-theorem
difficulty: MEDIUM
quality: AVERAGE
---
# Credit Card Fraud Detection
## Question
A credit card company's fraud detection system analyzes transactions:
- 0.1% of all transactions are fraudulent (P(Fraud) = 0.001)
- 99.9% of transactions are legitimate (P(Legitimate) = 0.999)

The system flags suspicious transactions:
- P(Flagged | Fraud) = 0.99 (catches 99% of fraud)
- P(Flagged | Legitimate) = 0.02 (2% false positive rate)

If a transaction is flagged, what is the probability it's actually fraudulent?
## Solution
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
