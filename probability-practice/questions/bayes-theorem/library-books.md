---
subject: bayes-theorem
difficulty: EASY
quality: GOOD
---
# Library Books
## Question
A library has three sections: Fiction (F), Non-Fiction (N), and Reference (R). 50% of the books are Fiction, 30% are Non-Fiction, and 20% are Reference.

The checkout rates for each section are:
- P(Checked Out | Fiction) = 0.6
- P(Checked Out | Non-Fiction) = 0.4
- P(Checked Out | Reference) = 0.1

**Questions:**
1. What is the overall probability that a randomly selected book is checked out?
2. Given that a book is checked out, what is the probability it's a Fiction book?
## Solution
**Part 1: Overall checkout probability**

Using the law of total probability:

P(Checked Out) = P(C|F)×P(F) + P(C|N)×P(N) + P(C|R)×P(R)

P(Checked Out) = (0.6)(0.5) + (0.4)(0.3) + (0.1)(0.2)

P(Checked Out) = 0.3 + 0.12 + 0.02 = 0.44

**Answer: 0.44 or 44%**

**Part 2: Probability it's Fiction given checked out**

Using Bayes' theorem:

P(Fiction | Checked Out) = P(Checked Out | Fiction) × P(Fiction) / P(Checked Out)

P(Fiction | Checked Out) = (0.6)(0.5) / 0.44

P(Fiction | Checked Out) = 0.3 / 0.44 = 15/22 ≈ 0.682

**Answer: 15/22 ≈ 0.682 or about 68.2%**

**Interpretation:** Among checked-out books, about 68% are fiction, which is higher than the overall 50% fiction rate. This makes sense because fiction has the highest checkout rate (60%).
