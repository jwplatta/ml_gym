# Expectation

## Question 1

**Prompt:**
Given the contingency table:

{{table}}

Let X be an indicator variable for event A (X=1 if A occurs, X=0 otherwise). Compute E[X].

**Solution:**
X = 1 with probability P(A) = {{marginal_A}}/{{total}}
X = 0 with probability P(¬A) = {{marginal_notA}}/{{total}}

E[X] = 1 × P(A) + 0 × P(¬A) = P(A) = {{marginal_A}}/{{total}} = {{simplified}}

Key insight: The expected value of an indicator variable equals the probability of the event.

## Question 2

**Prompt:**
Given the contingency table:

{{table}}

Let Y be a random variable that equals 10 if B occurs and 0 otherwise. Compute E[Y].

**Solution:**
Y = 10 with probability P(B) = {{marginal_B}}/{{total}}
Y = 0 with probability P(¬B) = {{marginal_notB}}/{{total}}

E[Y] = 10 × ({{marginal_B}}/{{total}}) + 0 × ({{marginal_notB}}/{{total}}) = 10 × {{marginal_B}}/{{total}} = {{expectation_result}}

## Question 3

**Prompt:**
Given the contingency table:

{{table}}

Let X and Y be indicator variables for events A and B respectively. Compute E[X + Y] using linearity of expectation.

**Solution:**
E[X] = P(A) = {{marginal_A}}/{{total}}
E[Y] = P(B) = {{marginal_B}}/{{total}}

By linearity of expectation:
E[X + Y] = E[X] + E[Y] = {{marginal_A}}/{{total}} + {{marginal_B}}/{{total}} = {{expectation_sum}}/{{total}}

## Question 4

**Prompt:**
Given the contingency table:

{{table}}

Define a random variable Z that takes value 100 if both A and B occur, 50 if exactly one occurs, and 0 if neither occurs. Compute E[Z].

**Solution:**
P(Z = 100) = P(A ∩ B) = {{joint_AB}}/{{total}}
P(Z = 50) = P(A ∩ ¬B) + P(¬A ∩ B) = {{joint_A_notB}}/{{total}} + {{joint_notA_B}}/{{total}} = {{exactly_one}}/{{total}}
P(Z = 0) = P(¬A ∩ ¬B) = {{joint_notA_notB}}/{{total}}

E[Z] = 100 × ({{joint_AB}}/{{total}}) + 50 × ({{exactly_one}}/{{total}}) + 0 × ({{joint_notA_notB}}/{{total}})
     = {{ez_term1}}/{{total}} + {{ez_term2}}/{{total}}
     = {{expectation_z}}/{{total}}

## Indicator Variable Property - Very Easy

**Prompt:**
Consider flipping a fair coin. Let X be an indicator variable:
- X = 1 if the coin lands heads
- X = 0 if the coin lands tails

Calculate E[X].

**Solution:**

E[X] = 1 × P(X = 1) + 0 × P(X = 0)

E[X] = 1 × P(Heads) + 0 × P(Tails)

E[X] = 1 × (1/2) + 0 × (1/2)

E[X] = 1/2 = 0.5

**Answer: 0.5**

**Key Insight:** For any indicator variable, E[indicator of A] = P(A). This is an extremely useful property that simplifies many calculations!

In this case: E[X] = P(Heads) = 0.5

**Note:** This is a fundamental concept in probability. The expected value of an indicator random variable equals the probability of the event it indicates. This property is used extensively in more complex probability calculations.

## Lottery Ticket - Easy

**Prompt:**
You buy a lottery ticket for $5. The ticket has the following payouts:
- Win $100 with probability 0.01
- Win $20 with probability 0.05
- Win $0 with probability 0.94

**Questions:**
1. What is the expected value of your winnings (before subtracting the ticket cost)?
2. What is your expected net gain (after subtracting the $5 ticket cost)?

**Solution:**

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