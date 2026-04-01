---
subject: conditional-probability
difficulty: EASY
quality: GOOD
---
# Card Drawing Without Replacement
## Question
You draw 2 cards from a standard deck of 52 cards without replacement.

**Questions:**
1. What is the probability that both cards are aces?
2. What is the probability that the second card is an ace, given that the first card was an ace?
3. What is the probability that at least one card is an ace?
## Solution
**Part 1: P(both cards are aces)**

P(both aces) = P(1st ace) × P(2nd ace | 1st ace)

P(1st ace) = 4/52 = 1/13

P(2nd ace | 1st ace) = 3/51 = 1/17

P(both aces) = (4/52) × (3/51) = 12/2,652 = 1/221

**Answer: 1/221 ≈ 0.00452 or about 0.45%**

**Part 2: P(2nd ace | 1st ace)**

Given the first card was an ace, there are now:
- 51 cards remaining
- 3 aces remaining

P(2nd ace | 1st ace) = 3/51 = 1/17 ≈ 0.0588

**Answer: 1/17 ≈ 0.0588 or about 5.88%**

**Part 3: P(at least one ace)**

Method 1 (Complement):

P(at least one ace) = 1 - P(no aces)

P(no aces) = P(1st not ace) × P(2nd not ace | 1st not ace)

P(no aces) = (48/52) × (47/51) = 2,256/2,652 = 188/221

P(at least one ace) = 1 - 188/221 = 33/221

**Answer: 33/221 ≈ 0.1493 or about 14.93%**

Method 2 (Direct):

P(at least one) = P(ace, not ace) + P(not ace, ace) + P(ace, ace)

= (4/52)(48/51) + (48/52)(4/51) + (4/52)(3/51)

= 192/2,652 + 192/2,652 + 12/2,652

= 396/2,652 = 33/221 ✓

**Key Insight:** When sampling without replacement, probabilities change after each draw. The complement approach is often simpler for "at least one" questions.
