---
subject: expectation
difficulty: EASY
quality: GOOD
---
# Lottery Ticket
## Question
You buy a lottery ticket for $5. The ticket has the following payouts:
- Win $100 with probability 0.01
- Win $20 with probability 0.05
- Win $0 with probability 0.94

**Questions:**
1. What is the expected value of your winnings (before subtracting the ticket cost)?
2. What is your expected net gain (after subtracting the $5 ticket cost)?
## Solution
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
