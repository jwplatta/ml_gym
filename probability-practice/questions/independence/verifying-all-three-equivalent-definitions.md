---
subject: independence
difficulty: MEDIUM
quality: GOOD
---
# Verifying All Three Equivalent Definitions
## Question
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
## Solution
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
