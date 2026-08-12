# Very Easy Conditional Probability and Bayes Theorem Questions

## Basic Conditional Probability Calculation

Given the following contingency table for a clinical drug trial:

|            | Side Effects (B) | No Side Effects (¬B) | Total |
|------------|------------------|----------------------|-------|
| Drug (A)   | 12               | 38                   | 50    |
| Placebo (¬A) | 8              | 42                   | 50    |
| **Total**  | **20**           | **80**               | **100** |

Compute P(A | B) - the probability that a patient received the drug given that they experienced side effects.

### Solution

P(A | B) = P(A ∩ B) / P(B) = (12/100) / (20/100) = 12/20 = 3/5 = 0.6

**Answer: 0.6 or 60%**

**Interpretation:** Among the 20 patients who experienced side effects, 12 received the drug. So there's a 60% probability that a patient who experienced side effects received the drug.

### Notes

- Quality: GOOD
- Difficulty: VERY EASY
- Notes: Clear introduction to conditional probability formula

## Comparing Conditional Probabilities

Given the following contingency table for student performance:

|            | Passed Exam (B) | Failed Exam (¬B) | Total |
|------------|-----------------|------------------|-------|
| Studied (A) | 45             | 5                | 50    |
| Didn't Study (¬A) | 15      | 35               | 50    |
| **Total**  | **60**          | **40**           | **100** |

Compute both P(A | B) and P(B | A). Are they equal?

### Solution

P(A | B) = 45/60 = 3/4 = 0.75

P(B | A) = 45/50 = 9/10 = 0.90

**Are they equal?** No, P(A | B) = 0.75 ≠ 0.90 = P(B | A)

**Interpretation:**
- P(A | B) = 0.75 means: Among students who passed, 75% had studied
- P(B | A) = 0.90 means: Among students who studied, 90% passed

These answer different questions, so they're generally not equal.

### Notes

- Quality: EXCELLENT
- Difficulty: VERY EASY
- Notes: Important lesson that P(A|B) ≠ P(B|A) in general; demonstrates asymmetry of conditional probability

## Medical Test - Bayes Theorem Application

Given the following contingency table representing a medical test for a disease:

|                | Test + (B) | Test - (¬B) | Total |
|----------------|------------|-------------|-------|
| Disease (A)    | 90         | 10          | 100   |
| No Disease (¬A) | 50        | 850         | 900   |
| **Total**      | **140**    | **860**     | **1000** |

If a patient tests positive (B), what is the probability they actually have the disease (A)? Use Bayes' theorem to find P(A | B).

### Solution

**Direct method:**
P(A | B) = 90/140 = 9/14 ≈ 0.643

**Using Bayes' theorem:**
P(A | B) = P(B | A) × P(A) / P(B)

Where:
- P(B | A) = 90/100 = 0.90 (sensitivity)
- P(A) = 100/1000 = 0.10 (prevalence)
- P(B) = 140/1000 = 0.14

Therefore:
P(A | B) = (0.90 × 0.10) / 0.14 = 0.09 / 0.14 = 9/14 ≈ 0.643

**Answer: 9/14 ≈ 0.643 or about 64.3%**

This is the positive predictive value (PPV) of the test.

### Notes

- Quality: EXCELLENT
- Difficulty: VERY EASY
- Notes: Classic medical test example showing both direct calculation and Bayes' theorem approach

## Conditional Probability with Multiple Categories

Given the following contingency table for investment performance by market sector:

|            | High Return (B) | Low Return (¬B) | Total |
|------------|-----------------|-----------------|-------|
| Tech (A)   | 30              | 20              | 50    |
| Finance    | 15              | 35              | 50    |
| **Total**  | **45**          | **55**          | **100** |

Given that an investment had a high return (B occurred), what is the probability it was in the Tech sector? Compute P(A | B).

### Solution

P(A | B) = P(A ∩ B) / P(B)

From the table:
- P(A ∩ B) = 30/100
- P(B) = 45/100

Therefore:
P(A | B) = (30/100) / (45/100) = 30/45 = 2/3 ≈ 0.667

**Answer: 2/3 ≈ 0.667 or about 66.7%**

**Interpretation:** Among all 45 investments with high returns, 30 were in the Tech sector, so P(Tech | High Return) = 2/3.

### Notes

- Quality: GOOD
- Difficulty: VERY EASY
- Notes: Demonstrates conditional probability in financial context with clear interpretation

## Asymmetry of Conditional Probabilities

Given the following contingency table for employee promotions:

|              | Promoted (B) | Not Promoted (¬B) | Total |
|--------------|--------------|-------------------|-------|
| MBA Degree (A) | 24        | 16                | 40    |
| No MBA (¬A)  | 6           | 54                | 60    |
| **Total**    | **30**      | **70**            | **100** |

Compute both P(A | B) and P(B | A). Are they equal? Why or why not?

### Solution

P(A | B) = 24/30 = 4/5 = 0.80

P(B | A) = 24/40 = 3/5 = 0.60

**Are they equal?** No, P(A | B) = 0.80 ≠ 0.60 = P(B | A)

**Explanation:**
- P(A | B) = 0.80 means: Among promoted employees, 80% had an MBA
- P(B | A) = 0.60 means: Among employees with an MBA, 60% were promoted

These have different denominators (30 vs 40), so they represent different questions and are generally not equal.

### Notes

- Quality: EXCELLENT
- Difficulty: VERY EASY
- Notes: Reinforces asymmetry concept with real-world employment example; helps students understand the importance of conditioning event

## Law of Total Probability with Three Categories

Given the following contingency table for customer satisfaction across three service tiers:

|              | Satisfied (B) | Not Satisfied (¬B) | Total |
|--------------|---------------|-------------------|-------|
| Premium (A₁) | 40            | 10                | 50    |
| Standard (A₂)| 24            | 16                | 40    |
| Basic (A₃)   | 6             | 4                 | 10    |
| **Total**    | **70**        | **30**            | **100** |

Use the law of total probability to compute P(B) from the conditional probabilities:

P(B) = P(B | A₁) × P(A₁) + P(B | A₂) × P(A₂) + P(B | A₃) × P(A₃)

### Solution

First, calculate the components:
- P(B | A₁) = 40/50 = 0.80
- P(A₁) = 50/100 = 0.50
- P(B | A₂) = 24/40 = 0.60
- P(A₂) = 40/100 = 0.40
- P(B | A₃) = 6/10 = 0.60
- P(A₃) = 10/100 = 0.10

Using the law of total probability:

P(B) = P(B | A₁) × P(A₁) + P(B | A₂) × P(A₂) + P(B | A₃) × P(A₃)

P(B) = (0.80)(0.50) + (0.60)(0.40) + (0.60)(0.10)

P(B) = 0.40 + 0.24 + 0.06 = 0.70

**Verification:** From the table, P(B) = 70/100 = 0.70 ✓

**Answer: 0.70 or 70%**

### Notes

- Quality: GOOD
- Difficulty: VERY EASY
- Notes: Clear demonstration of law of total probability with three mutually exclusive categories

## Testing for Independence

Given the following contingency table for coin flips and dice rolls:

|              | Even Die (B) | Odd Die (¬B) | Total |
|--------------|--------------|--------------|-------|
| Heads (A)    | 30           | 20           | 50    |
| Tails (¬A)   | 30           | 20           | 50    |
| **Total**    | **60**       | **40**       | **100** |

1. Calculate P(A | B) and compare it to P(A)
2. Are events A and B independent? Explain why or why not.
3. Verify using the product rule: Does P(A ∩ B) = P(A) × P(B)?

### Solution

**Part 1: Calculate P(A | B) and P(A)**

P(A | B) = 30/60 = 1/2 = 0.50

P(A) = 50/100 = 1/2 = 0.50

**Part 2: Independence check**

Since P(A | B) = P(A), the events appear to be independent. Knowing that the die showed an even number doesn't change the probability of getting heads.

**Part 3: Verify with product rule**

P(A ∩ B) = 30/100 = 0.30

P(A) × P(B) = (50/100) × (60/100) = 0.50 × 0.60 = 0.30

Since P(A ∩ B) = P(A) × P(B), this confirms independence! ✓

**Explanation:**

Two events A and B are independent if P(A | B) = P(A), which means learning that B occurred doesn't change the probability of A.

**In this case:** Events A (Heads) and B (Even Die) are independent. This makes sense because a coin flip and a die roll are physically independent processes - the outcome of one doesn't affect the other.

### Notes

- Quality: EXCELLENT
- Difficulty: VERY EASY
- Notes: Clear example of independence with verification using both conditional probability and product rule; uses physically independent events for intuition
