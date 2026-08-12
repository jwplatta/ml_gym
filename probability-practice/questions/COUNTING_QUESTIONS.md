# Counting Questions

## Sample Space Size

Given the following contingency table for customer satisfaction:

|              | Satisfied (B) | Not Satisfied (¬B) | Total |
|--------------|---------------|-------------------|-------|
| Product A    | 45            | 15                | 60    |
| Product B (¬A) | 20          | 20                | 40    |
| **Total**    | **65**        | **35**            | **100** |

How many outcomes are in the sample space?

### Solution

The sample space contains all possible outcomes. From the table, the total count is 100.

Therefore, |S| = 100 outcomes.

**Answer: 100 outcomes**

**Key Concept:** The sample space size equals the total number of observations or trials in the contingency table.

### Notes

- Quality: AVERAGE
- Difficulty: VERY EASY
- Notes: Basic counting of sample space from contingency table

## Counting Intersection Events

Given the following contingency table for student status:

|              | Passed (B) | Failed (¬B) | Total |
|--------------|------------|-------------|-------|
| Studied (A)  | 72         | 8           | 80    |
| Didn't Study (¬A) | 12    | 8           | 20    |
| **Total**    | **84**     | **16**      | **100** |

How many outcomes satisfy the condition "A and B both occur" (student studied AND passed)?

### Solution

Outcomes where both A and B occur are in the cell (A ∩ B), which has 72 outcomes.

**Answer: 72 outcomes**

**Interpretation:** Out of 100 total students, 72 both studied and passed the exam.

### Notes

- Quality: GOOD
- Difficulty: VERY EASY
- Notes: Demonstrates counting joint events from contingency table

## Counting Union Events

Given the following contingency table for marketing responses:

|              | Clicked Ad (B) | No Click (¬B) | Total |
|--------------|----------------|---------------|-------|
| Opened Email (A) | 30         | 20            | 50    |
| No Open (¬A) | 15             | 35            | 50    |
| **Total**    | **45**         | **55**        | **100** |

How many outcomes satisfy "A or B (or both)" (opened email OR clicked ad OR both)?

### Solution

Outcomes with A or B are in cells (A∩B), (A∩¬B), and (¬A∩B):

Count = 30 + 20 + 15 = 65

**Answer: 65 outcomes**

**Verification using complement:**
Count(A ∪ B) = Total - Count(¬A ∩ ¬B) = 100 - 35 = 65 ✓

**Key Insight:** To count A ∪ B, sum all cells except (¬A ∩ ¬B).

### Notes

- Quality: GOOD
- Difficulty: EASY
- Notes: Demonstrates counting union events using inclusion principle; includes verification

## Selecting Without Replacement

Given the following contingency table for product defects:

|              | Defective (B) | Good (¬B) | Total |
|--------------|---------------|-----------|-------|
| Factory 1 (A) | 5            | 45        | 50    |
| Factory 2 (¬A) | 10          | 40        | 50    |
| **Total**    | **15**        | **85**    | **100** |

If you randomly select 2 outcomes from the sample space without replacement, how many ways can you do this?

### Solution

This is a combination problem: choosing 2 items from 100 without regard to order.

C(100, 2) = 100! / (2! × 98!)
          = (100 × 99) / 2
          = 9,900 / 2
          = 4,950

**Answer: 4,950 ways**

**Key Concept:** Combinations C(n,k) count the number of ways to choose k items from n items where order doesn't matter.

### Notes

- Quality: AVERAGE
- Difficulty: VERY EASY
- Notes: Basic combination calculation from contingency table context

## Permutations of All Outcomes

Given the following contingency table:

|              | Event B | Event ¬B | Total |
|--------------|---------|----------|-------|
| Event A      | 3       | 2        | 5     |
| Event ¬A     | 1       | 4        | 5     |
| **Total**    | **4**   | **6**    | **10** |

Suppose you arrange all 10 outcomes in a line. How many such arrangements are possible?

### Solution

The number of ways to arrange 10 distinct outcomes is 10! (factorial).

10! = 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 3,628,800

**Answer: 3,628,800 arrangements**

**Key Concept:** The number of permutations of n distinct objects is n!

### Notes

- Quality: AVERAGE
- Difficulty: EASY
- Notes: Demonstrates factorial counting for permutations of all elements

## Permutations - Stock Rankings

A fund manager needs to rank their top 3 performing stocks from a portfolio of 8 stocks. How many different rankings are possible?

### Solution

This is a permutation problem because the order of ranking matters.

P(8, 3) = 8! / (8-3)! = 8! / 5!

P(8, 3) = 8 × 7 × 6 = 336

**Answer: 336 different rankings**

**Explanation:**
- For 1st place: 8 choices
- For 2nd place: 7 remaining choices
- For 3rd place: 6 remaining choices
- Total: 8 × 7 × 6 = 336

### Notes

- Quality: AVERAGE
- Difficulty: VERY EASY
- Notes: Basic permutation problem demonstrating ordered selection
- Source: probability_mixed_easy_20260212.ipynb

## Combinations - Committee Formation

An investment committee has 12 members. They need to form a subcommittee of 4 members to review a merger proposal. How many different subcommittees can be formed?

### Solution

This is a combination problem because the order doesn't matter (just choosing a group).

C(12, 4) = 12! / (4! × 8!)

C(12, 4) = (12 × 11 × 10 × 9) / (4 × 3 × 2 × 1)

C(12, 4) = 11,880 / 24 = 495

**Answer: 495 different subcommittees**

**Key Distinction:**
- Permutations (order matters): P(n,k) = n!/(n-k)!
- Combinations (order doesn't matter): C(n,k) = n!/(k!(n-k)!)
- Relationship: C(n,k) = P(n,k) / k!

### Notes

- Quality: AVERAGE
- Difficulty: VERY EASY
- Notes: Basic combination problem demonstrating unordered selection
- Source: probability_mixed_easy_20260212.ipynb

## Portfolio Construction with Constraints

A portfolio manager must select 5 stocks from a universe of:
- 6 technology stocks
- 4 healthcare stocks
- 5 financial stocks

The portfolio must include **at least 2 technology stocks** and **at least 1 healthcare stock**.

**Question:** How many different portfolios satisfy these constraints?

### Solution

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

### Notes

- Quality: GOOD
- Difficulty: EASY
- Notes: Uses complementary counting approach; tests understanding of combinations with multiple constraints