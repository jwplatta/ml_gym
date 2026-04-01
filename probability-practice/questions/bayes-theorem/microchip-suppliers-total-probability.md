---
subject: bayes-theorem
difficulty: VERY EASY
quality: GOOD
---
# Microchip Suppliers and Total Probability
## Question
A company buys microchips from two suppliers.

- 40% of chips come from Supplier A
- 60% of chips come from Supplier B
- 3% of Supplier A chips are defective
- 8% of Supplier B chips are defective

Find:
1. The overall probability that a chip is defective
2. Given that a chip is defective, the probability it came from Supplier B
## Solution
Let D be the event that a chip is defective.

First compute the overall defect probability using the law of total probability:

P(D) = P(D | A)P(A) + P(D | B)P(B)
     = (0.03)(0.40) + (0.08)(0.60)
     = 0.012 + 0.048
     = 0.060

So the overall defect probability is 0.06.

Now apply Bayes' theorem:

P(B | D) = (P(D | B)P(B)) / P(D)
         = (0.08 × 0.60) / 0.06
         = 0.048 / 0.06
         = 0.80

**Answers:**
- Overall defective probability: 0.06
- P(B | D) = 0.80

Interpretation: Supplier B provides 60% of chips but accounts for 80% of defective chips because its defect rate is higher.
