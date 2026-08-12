# Joint Probability Questions

## Basic Joint Probability

Given the following contingency table for weather and traffic conditions:

|          | Heavy Traffic (B) | Light Traffic (¬B) | Total |
|----------|-------------------|--------------------|-------|
| Rain (A) | 35                | 15                 | 50    |
| Clear (¬A) | 20              | 30                 | 50    |
| **Total** | **55**           | **45**             | **100** |

Compute P(A ∩ B) - the probability that it rains AND there is heavy traffic.

### Solution

P(A ∩ B) = 35/100 = 7/20 = 0.35

**Answer: 7/20 = 0.35 or 35%**

**Interpretation:** There's a 35% probability that on any given day, it will both rain and have heavy traffic.

### Notes

- Quality: AVERAGE
- Difficulty: VERY EASY
- Notes: Basic joint probability calculation; straightforward reading from contingency table

## Joint Probability with Complement

Given the following contingency table for student attendance and exam performance:

|               | Passed Exam (B) | Failed Exam (¬B) | Total |
|---------------|-----------------|------------------|-------|
| Attended (A)  | 72              | 8                | 80    |
| Absent (¬A)   | 12              | 8                | 20    |
| **Total**     | **84**          | **16**           | **100** |

What is P(A ∩ ¬B) - the probability a student attended class but failed the exam?

### Solution

P(A ∩ ¬B) = 8/100 = 2/25 = 0.08

**Answer: 2/25 = 0.08 or 8%**

**Interpretation:** Only 8% of students attended class but still failed the exam. This is relatively low, suggesting attendance is strongly associated with passing.

### Notes

- Quality: GOOD
- Difficulty: VERY EASY
- Notes: Introduces joint probability with complement events; shows how to read different cells from table

## Multiplication Rule Verification

Given the following contingency table for subscription tier and feature usage:

|              | Used Feature (B) | Didn't Use (¬B) | Total |
|--------------|------------------|-----------------|-------|
| Premium (A)  | 45               | 15              | 60    |
| Basic (¬A)   | 15               | 25              | 40    |
| **Total**    | **60**           | **40**          | **100** |

Verify that P(A ∩ B) = P(A) × P(B | A) using the table data.

### Solution

Calculate components:

P(A) = 60/100 = 0.60

P(B | A) = 45/60 = 3/4 = 0.75

**Using multiplication rule:**

P(A) × P(B | A) = (60/100) × (45/60) = 45/100 = 0.45

**Direct from table:**

P(A ∩ B) = 45/100 = 0.45

Both equal 0.45, verifying the multiplication rule! ✓

**Key Insight:** The multiplication rule P(A ∩ B) = P(A) × P(B | A) provides an alternative way to compute joint probabilities using marginal and conditional probabilities.

### Notes

- Quality: EXCELLENT
- Difficulty: EASY
- Notes: Demonstrates multiplication rule; shows equivalence between direct calculation and using conditionals; important foundational concept

## Both Events Not Occurring

Given the following contingency table for marketing campaign response:

|                | Opened Email (B) | Didn't Open (¬B) | Total |
|----------------|------------------|------------------|-------|
| Clicked Ad (A) | 18               | 2                | 20    |
| No Click (¬A)  | 30               | 50               | 80    |
| **Total**      | **48**           | **52**           | **100** |

Compute P(¬A ∩ ¬B) - the probability that a user neither opened the email nor clicked the ad.

### Solution

P(¬A ∩ ¬B) = 50/100 = 1/2 = 0.50

**Answer: 1/2 = 0.50 or 50%**

**Interpretation:** Half of all users had no engagement at all - they neither opened the email nor clicked the ad. This represents the completely unengaged segment.

**Additional Insight:** We can verify using complements:

P(¬A ∩ ¬B) = 1 - P(A ∪ B) = 1 - [P(A) + P(B) - P(A ∩ B)]
           = 1 - [20/100 + 48/100 - 18/100]
           = 1 - 50/100 = 50/100 = 0.50 ✓

### Notes

- Quality: GOOD
- Difficulty: EASY
- Notes: Shows joint probability of both complements; includes verification using union/complement relationship; practical marketing context
