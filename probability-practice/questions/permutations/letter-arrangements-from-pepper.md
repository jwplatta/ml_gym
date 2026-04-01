---
subject: permutations
difficulty: EASY
quality: GOOD
---
# Letter Arrangements from PEPPER
## Question
How many different letter arrangements can be formed from the letters PEPPER?
## Solution
This is a permutation with repetition problem.

The word PEPPER has:
- Total letters: 6
- P appears: 3 times
- E appears: 2 times
- R appears: 1 time

When we have repeated items, we use the formula:

Number of arrangements = n! / (n₁! × n₂! × ... × nₖ!)

where n is the total number of items, and n₁, n₂, ..., nₖ are the frequencies of each repeated item.

Number of arrangements = 6! / (3! × 2! × 1!)

Calculate:
- 6! = 720
- 3! = 6
- 2! = 2
- 1! = 1

Number of arrangements = 720 / (6 × 2 × 1) = 720 / 12 = 60

**Answer: 60 different letter arrangements**

**Examples of arrangements:** PEPPER, PERPEP, EPPREP, REPPER, EPRPEP, etc.

**Key Insight:** When items are identical, we divide by the factorial of each group's size to avoid counting identical arrangements multiple times.
