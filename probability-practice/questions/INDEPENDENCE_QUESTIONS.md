# Independence Questions

## Product Rule Test for Independence

Given the following contingency table for smartphone ownership and social media usage:

|              | Social Media (B) | No Social Media (¬B) | Total |
|--------------|------------------|----------------------|-------|
| Smartphone (A) | 72              | 18                   | 90    |
| No Phone (¬A) | 8               | 2                    | 10    |
| **Total**    | **80**          | **20**               | **100** |

Check if A and B are independent by testing if P(A ∩ B) = P(A) × P(B).

### Solution

P(A) = 90/100 = 0.90
P(B) = 80/100 = 0.80
P(A) × P(B) = (90/100) × (80/100) = 7200/10000 = 0.72

P(A ∩ B) = 72/100 = 0.72

Since P(A ∩ B) = 0.72 = 0.72 = P(A) × P(B), events A and B are **independent**.

**Interpretation:** Having a smartphone and using social media are independent in this dataset. The product of marginal probabilities equals the joint probability.

### Notes

- Quality: GOOD
- Difficulty: VERY EASY
- Notes: Clear introduction to independence using product rule; demonstrates calculation and verification

## Conditional Probability Test for Independence

Given the following contingency table for coffee preference and morning person status:

|                | Coffee Drinker (B) | Non-Drinker (¬B) | Total |
|----------------|-------------------|------------------|-------|
| Morning Person (A) | 30             | 20               | 50    |
| Not Morning (¬A) | 30              | 20               | 50    |
| **Total**      | **60**            | **40**           | **100** |

Check if A and B are independent by testing if P(A | B) = P(A).

### Solution

P(A) = 50/100 = 0.50

P(A | B) = 30/60 = 0.50

Since P(A | B) = 0.50 = 0.50 = P(A), events A and B are **independent**.

**Interpretation:** Knowing someone drinks coffee doesn't change the probability they're a morning person. The conditional probability equals the marginal probability, confirming independence.

### Notes

- Quality: GOOD
- Difficulty: VERY EASY
- Notes: Demonstrates conditional probability test for independence; shows that conditioning doesn't change probabilities when independent

## Chi-Squared Test for Independence

Given the following contingency table for voting patterns by age group:

|           | Voted Yes (B) | Voted No (¬B) | Total |
|-----------|---------------|---------------|-------|
| Young (A) | 40            | 60            | 100   |
| Old (¬A)  | 60            | 40            | 100   |
| **Total** | **100**       | **100**       | **200** |

Compute the chi-squared statistic: χ² = Σ (observed - expected)² / expected for all four cells, where expected = (row total × column total) / grand total.

### Solution

**Expected counts under independence:**

E(A ∩ B) = 100 × 100 / 200 = 50
E(A ∩ ¬B) = 100 × 100 / 200 = 50
E(¬A ∩ B) = 100 × 100 / 200 = 50
E(¬A ∩ ¬B) = 100 × 100 / 200 = 50

**Chi-squared calculation:**

χ² = (40 - 50)² / 50 + (60 - 50)² / 50 + (60 - 50)² / 50 + (40 - 50)² / 50

χ² = 100/50 + 100/50 + 100/50 + 100/50

χ² = 2 + 2 + 2 + 2 = 8

**Interpretation:** χ² = 8 is relatively large, suggesting the events are NOT independent. Young voters and old voters have different voting patterns (young tend to vote No, old tend to vote Yes).

For a 2×2 table with 1 degree of freedom, χ² > 3.841 indicates significant dependence at the 0.05 level. Since 8 > 3.841, we reject independence.

### Notes

- Quality: GOOD
- Difficulty: MEDIUM
- Notes: Introduces chi-squared test as statistical measure of independence; requires understanding of expected values

## Verifying All Three Equivalent Definitions

Given the following contingency table for exercise habits and diet quality:

|              | Healthy Diet (B) | Unhealthy Diet (¬B) | Total |
|--------------|------------------|---------------------|-------|
| Exercises (A) | 45              | 15                  | 60    |
| No Exercise (¬A) | 30           | 10                  | 40    |
| **Total**    | **75**          | **25**              | **100** |

Verify all three equivalent definitions of independence:
1. P(A ∩ B) = P(A) × P(B)
2. P(A | B) = P(A)
3. P(B | A) = P(B)

If any one fails, all three should fail.

### Solution

**Test 1: P(A ∩ B) ?= P(A) × P(B)**

P(A ∩ B) = 45/100 = 0.45

P(A) × P(B) = (60/100) × (75/100) = 4500/10000 = 0.45

Test 1: 0.45 = 0.45 ✓ **PASS**

**Test 2: P(A | B) ?= P(A)**

P(A | B) = 45/75 = 3/5 = 0.60

P(A) = 60/100 = 3/5 = 0.60

Test 2: 0.60 = 0.60 ✓ **PASS**

**Test 3: P(B | A) ?= P(B)**

P(B | A) = 45/60 = 3/4 = 0.75

P(B) = 75/100 = 3/4 = 0.75

Test 3: 0.75 = 0.75 ✓ **PASS**

**Conclusion:** All three tests pass, confirming that events A (Exercises) and B (Healthy Diet) are **independent** in this dataset.

**Key Insight:** The three definitions are mathematically equivalent. If any one holds, all must hold. This provides multiple ways to verify independence.

### Notes

- Quality: EXCELLENT
- Difficulty: MEDIUM
- Notes: Comprehensive demonstration showing equivalence of three independence definitions; reinforces conceptual understanding

## Expected vs Actual Counts Under Independence

Given the following contingency table for product returns by purchase channel:

|              | Returned (B) | Kept (¬B) | Total |
|--------------|--------------|-----------|-------|
| Online (A)   | 24           | 96        | 120   |
| In-Store (¬A) | 6           | 54        | 60    |
| **Total**    | **30**      | **150**   | **180** |

Assume A and B were independent. Compute what the cell counts would be. Compare to actual counts to measure departure from independence.

### Solution

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

### Notes

- Quality: EXCELLENT
- Difficulty: MEDIUM
- Notes: Shows how to calculate expected counts under independence assumption; comparing actual vs expected reveals dependence patterns; demonstrates chi-squared components
