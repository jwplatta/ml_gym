---
subject: probability-axioms
difficulty: EASY
quality: AVERAGE
---
# Probability Axioms Question 1
## Question
Two gamblers are playing a coin toss game. Gambler A has n+{{random_int(min_val=1, max_val=100)}} fair coins. Gambler B has n fair coins. Both gamblers flip all of their coins. What is the probability that A will have more heads than B?
## Solution
We proceed using symmetry and basic reasoning. The extra coin gives A an advantage. To analyze this, remove one coin from A so that both gamblers now flip exactly n coins. This makes the situation symmetric between A and B. Let us compare the number of heads obtained from these n coins. There are three possible events:

E_1: A's n coins have more heads than B's n coins,
E_2: A's n coins have the same number of heads as B's n coins,
E_3: A's n coins have fewer heads than B's n coins.

By symmetry, the probability that A has more heads than B is the same as the probability that B has more heads than A, so P(E_1) = P(E_3). Let P(E_1) = P(E_3) = x, and P(E_2) = y. Since these events exhaust all possibilities, we have 2x + y = 1.

Now consider A's additional (n+1)-st coin. In event E_1, A already has more heads than B, regardless of how the extra coin lands. In event E_3, A cannot have more heads than B, regardless of the extra coin. In event E_2, the extra coin does matter: if it lands heads (with probability 0.5), A will have more heads than B; if it lands tails, the totals remain tied.

Therefore, the extra coin increases the probability that A has more heads by 0.5y. The total probability that A has more heads than B is x + 0.5y. Using y = 1 - 2x, we obtain x + 0.5(1 - 2x) = 0.5.

So, when A has n+1 fair coins and B has n fair coins, the probability that A ends up with more heads than B is exactly one half.
