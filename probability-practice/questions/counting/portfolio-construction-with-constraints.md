---
subject: counting
difficulty: EASY
quality: GOOD
---
# Portfolio Construction with Constraints
## Question
A portfolio manager must select 5 stocks from a universe of:
- 6 technology stocks
- 4 healthcare stocks
- 5 financial stocks

The portfolio must include **at least 2 technology stocks** and **at least 1 healthcare stock**.

**Question:** How many different portfolios satisfy these constraints?
## Solution
**Solution using case-by-case counting:**

We need to select 5 stocks total with:
- At least 2 tech (T)
- At least 1 healthcare (H)
- Remaining from financials (F)

Let's enumerate valid compositions (T, H, F):

**Case 1: (2, 1, 2)** - 2 tech, 1 healthcare, 2 financial
- C(6,2) × C(4,1) × C(5,2) = 15 × 4 × 10 = 600

**Case 2: (2, 2, 1)** - 2 tech, 2 healthcare, 1 financial
- C(6,2) × C(4,2) × C(5,1) = 15 × 6 × 5 = 450

**Case 3: (2, 3, 0)** - 2 tech, 3 healthcare, 0 financial
- C(6,2) × C(4,3) × C(5,0) = 15 × 4 × 1 = 60

**Case 4: (3, 1, 1)** - 3 tech, 1 healthcare, 1 financial
- C(6,3) × C(4,1) × C(5,1) = 20 × 4 × 5 = 400

**Case 5: (3, 2, 0)** - 3 tech, 2 healthcare, 0 financial
- C(6,3) × C(4,2) × C(5,0) = 20 × 6 × 1 = 120

**Case 6: (4, 1, 0)** - 4 tech, 1 healthcare, 0 financial
- C(6,4) × C(4,1) × C(5,0) = 15 × 4 × 1 = 60

Total = 600 + 450 + 60 + 400 + 120 + 60 = **1,690 portfolios**

**Answer: 1,690 different portfolios**

**Key Insight:** When dealing with constraints, break the problem into mutually exclusive cases that satisfy all constraints, count each case separately, then sum.
