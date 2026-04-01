---
subject: bayes-theorem
difficulty: MEDIUM
quality: GOOD
---
# Odds Ratio Calculation
## Question
Given the following contingency table for treatment effectiveness:

|              | Improved (B) | No Improvement (¬B) | Total |
|--------------|--------------|---------------------|-------|
| Treatment (A) | 60          | 20                  | 80    |
| Control (¬A) | 30           | 90                  | 120   |
| **Total**    | **90**       | **110**             | **200** |

Compute the odds ratio: [P(A|B) / P(¬A|B)] / [P(A|¬B) / P(¬A|¬B)]. This measures how much B affects the odds of A.
## Solution
**Odds of A given B:**

P(A | B) = 60/90 = 2/3

P(¬A | B) = 30/90 = 1/3

Odds(A | B) = (2/3) / (1/3) = 2

**Odds of A given ¬B:**

P(A | ¬B) = 20/110 = 2/11

P(¬A | ¬B) = 90/110 = 9/11

Odds(A | ¬B) = (2/11) / (9/11) = 2/9

**Odds Ratio:**

OR = Odds(A | B) / Odds(A | ¬B) = 2 / (2/9) = 2 × (9/2) = 9

**Answer: Odds Ratio = 9**

**Interpretation:** The odds of having received treatment are 9 times higher among those who improved compared to those who didn't improve.
