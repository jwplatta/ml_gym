---
subject: counting
difficulty: VERY EASY
quality: AVERAGE
---
# Combinations - Committee Formation
## Question
An investment committee has 12 members. They need to form a subcommittee of 4 members to review a merger proposal. How many different subcommittees can be formed?
## Solution
This is a combination problem because the order doesn't matter (just choosing a group).

C(12, 4) = 12! / (4! × 8!)

C(12, 4) = (12 × 11 × 10 × 9) / (4 × 3 × 2 × 1)

C(12, 4) = 11,880 / 24 = 495

**Answer: 495 different subcommittees**

**Key Distinction:**
- Permutations (order matters): P(n,k) = n!/(n-k)!
- Combinations (order doesn't matter): C(n,k) = n!/(k!(n-k)!)
- Relationship: C(n,k) = P(n,k) / k!
