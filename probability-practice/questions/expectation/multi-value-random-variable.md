---
subject: expectation
difficulty: EASY
quality: GOOD
---
# Multi-Value Random Variable
## Question
Given the following contingency table for project outcomes:

|              | Success (B) | Failure (¬B) | Total |
|--------------|-------------|--------------|-------|
| Experienced (A) | 48        | 12           | 60    |
| Novice (¬A) | 12           | 28           | 40    |
| **Total**    | **60**       | **40**       | **100** |

Define a random variable Z that takes value 100 if both A and B occur, 50 if exactly one occurs, and 0 if neither occurs. Compute E[Z].
## Solution
**Step 1: Find probabilities**

P(Z = 100) = P(A ∩ B) = 48/100 = 0.48

P(Z = 50) = P(A ∩ ¬B) + P(¬A ∩ B)
          = 12/100 + 12/100
          = 24/100
          = 0.24

P(Z = 0) = P(¬A ∩ ¬B) = 28/100 = 0.28

**Step 2: Calculate expectation**

E[Z] = 100 × (0.48) + 50 × (0.24) + 0 × (0.28)
     = 48 + 12 + 0
     = 60

**Answer: 60**

**Interpretation:** On average, the random variable Z takes value 60, even though it never actually equals 60 (it's always 0, 50, or 100).
