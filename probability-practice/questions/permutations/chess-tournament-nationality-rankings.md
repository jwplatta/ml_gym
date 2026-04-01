---
subject: permutations
difficulty: MEDIUM
quality: GOOD
---
# Chess Tournament Nationality Rankings
## Question
A chess tournament has 10 competitors, of which 4 are Russian, 3 are from the United States, 2 are from Great Britain, and 1 is from Brazil. If the tournament result lists just the nationalities of the players in the order in which they placed, how many outcomes are possible?
## Solution
Since we only care about the nationalities (not individual players), this is a permutation with repetition problem.

We have:
- Total positions: 10
- Russian (R): 4 players
- USA (U): 3 players
- Great Britain (G): 2 players
- Brazil (B): 1 player

Number of nationality orderings = 10! / (4! × 3! × 2! × 1!)

Calculate:
- 10! = 3,628,800
- 4! = 24
- 3! = 6
- 2! = 2
- 1! = 1

Number of orderings = 3,628,800 / (24 × 6 × 2 × 1)
Number of orderings = 3,628,800 / 288
Number of orderings = 12,600

**Answer: 12,600 different nationality orderings**

**Example orderings:** RRRRUUUGGB, BRRRRUUUGG, UUUGGBRRR, etc.

**Key Insight:** This is the multinomial coefficient, which counts the number of ways to arrange n items where items fall into k distinct groups with sizes n₁, n₂, ..., nₖ.
