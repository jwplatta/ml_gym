---
subject: permutations
difficulty: EASY
quality: GOOD
---
# Flag Signal Arrangements
## Question
How many different signals, each consisting of 9 flags hung in a line, can be made from a set of 4 white flags, 3 red flags, and 2 blue flags if all flags of the same color are identical?
## Solution
This is another permutation with repetition problem.

We have:
- Total flags: 9
- White flags: 4 (identical)
- Red flags: 3 (identical)
- Blue flags: 2 (identical)

Number of different signals = 9! / (4! × 3! × 2!)

Calculate:
- 9! = 362,880
- 4! = 24
- 3! = 6
- 2! = 2

Number of signals = 362,880 / (24 × 6 × 2)
Number of signals = 362,880 / 288
Number of signals = 1,260

**Answer: 1,260 different signals**

**Example signals:** WWWWRRRBBB, BWRWRWRWWB, RRRWWWWBB, etc.

**Key Insight:** This is the multinomial coefficient formula: n! / (n₁! × n₂! × ... × nₖ!), which gives the number of ways to arrange n objects when there are k types of identical objects with frequencies n₁, n₂, ..., nₖ.
