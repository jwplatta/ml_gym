---
subject: independence
difficulty: MEDIUM
quality: GOOD
---
# Expected vs Actual Counts Under Independence

## Question
Given the following contingency table for product returns by purchase channel:

|              | Returned (B) | Kept (¬B) | Total |
|--------------|--------------|-----------|-------|
| Online (A)   | 24           | 96        | 120   |
| In-Store (¬A) | 6           | 54        | 60    |
| **Total**    | **30**      | **150**   | **180** |

Assume A and B were independent. Compute what the cell counts would be. Compare to actual counts to measure departure from independence.

## Solution
**Under independence, expected counts:**

E(A ∩ B) = 120 × 30 / 180 = 20
E(A ∩ ¬B) = 120 × 150 / 180 = 100
E(¬A ∩ B) = 60 × 30 / 180 = 10
E(¬A ∩ ¬B) = 60 × 150 / 180 = 50

**Actual counts:**
- A ∩ B: 24
- A ∩ ¬B: 96
- ¬A ∩ B: 6
- ¬A ∩ ¬B: 54

**Differences (Actual - Expected):**
- Δ(A ∩ B) = 24 - 20 = +4
- Δ(A ∩ ¬B) = 96 - 100 = -4
- Δ(¬A ∩ B) = 6 - 10 = -4
- Δ(¬A ∩ ¬B) = 54 - 50 = +4

**Interpretation:** The actual counts differ from expected counts under independence. There are MORE online returns than expected (+4) and FEWER in-store returns than expected (-4). This suggests online purchases have a slightly higher return rate than in-store purchases, indicating **dependence** between purchase channel and returns.

**Pattern:** Notice the differences follow a pattern: (+4, -4, -4, +4). This is characteristic of dependence in 2×2 tables - the deviations must sum to zero in each row and column.
