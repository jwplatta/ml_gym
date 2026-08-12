# Marginal Probability Questions

## Computing Marginal Probability P(A)

Given the following contingency table for product quality ratings:

|              | Satisfied (B) | Unsatisfied (¬B) | Total |
|--------------|---------------|------------------|-------|
| Premium (A)  | 42            | 18               | 60    |
| Standard (¬A) | 28           | 12               | 40    |
| **Total**    | **70**        | **30**           | **100** |

Compute P(A) - the probability a customer purchased a Premium product.

### Solution

P(A) = 60/100 = 3/5 = 0.60

**Answer: 3/5 = 0.60 or 60%**

**Interpretation:** 60% of customers purchased Premium products. This is the row marginal for Premium.

### Notes

- Quality: AVERAGE
- Difficulty: VERY EASY
- Notes: Basic marginal probability calculation from row total

## Computing Marginal Probability P(B)

Given the following contingency table for employee performance:

|                | High Performer (B) | Low Performer (¬B) | Total |
|----------------|-------------------|-------------------|-------|
| Manager (A)    | 24                | 16                | 40    |
| Individual (¬A) | 36               | 24                | 60    |
| **Total**      | **60**            | **40**            | **100** |

Compute P(B) - the probability an employee is a high performer.

### Solution

P(B) = 60/100 = 3/5 = 0.60

**Answer: 3/5 = 0.60 or 60%**

**Interpretation:** 60% of all employees are high performers. This is the column marginal for High Performer.

### Notes

- Quality: AVERAGE
- Difficulty: VERY EASY
- Notes: Basic marginal probability calculation from column total

## Alternative Phrasing for Marginal Probability

Given the following contingency table for age and smartphone ownership:

|              | Smartphone (B) | No Smartphone (¬B) | Total |
|--------------|----------------|-------------------|-------|
| Young (A)    | 75             | 25                | 100   |
| Older (¬A)   | 30             | 70                | 100   |
| **Total**    | **105**        | **95**            | **200** |

What is the probability of event A (being young)?

### Solution

P(A) = 100/200 = 1/2 = 0.50

**Answer: 1/2 = 0.50 or 50%**

**Interpretation:** Half of the population is young. This demonstrates that marginal probabilities represent overall proportions regardless of the other variable.

### Notes

- Quality: AVERAGE
- Difficulty: VERY EASY
- Notes: Reinforces marginal probability concept with different phrasing

## Complement Marginal Probability

Given the following contingency table for vaccination status and illness:

|              | Got Sick (B) | Stayed Healthy (¬B) | Total |
|--------------|--------------|---------------------|-------|
| Vaccinated (A) | 8          | 72                  | 80    |
| Not Vaccinated (¬A) | 32   | 48                  | 80    |
| **Total**    | **40**       | **120**             | **160** |

Find P(¬A) - the probability someone is not vaccinated.

### Solution

P(¬A) = 80/160 = 1/2 = 0.50

**Answer: 1/2 = 0.50 or 50%**

**Interpretation:** Half of the population is not vaccinated. We can verify: P(A) + P(¬A) = 80/160 + 80/160 = 160/160 = 1 ✓

### Notes

- Quality: GOOD
- Difficulty: VERY EASY
- Notes: Introduces complement marginal probability; demonstrates that P(A) + P(¬A) = 1

## Company Size and Growth Classification

A financial analyst categorizes companies by **Size** (Large, Small) and **Growth** (High, Low). Here's the distribution:

|           | High Growth | Low Growth | **Total** |
|-----------|-------------|------------|----------|
| **Large** | 30          | 20         | 50       |
| **Small** | 15          | 35         | 50       |
| **Total** | 45          | 55         | 100      |

**Questions:**
1. What is P(Large)?
2. What is P(High Growth)?
3. What is P(Small and Low Growth)?

### Solution

**Part 1: P(Large)**

P(Large) = 50 / 100 = 1/2 = 0.5

**Answer: 0.5 or 50%**

**Part 2: P(High Growth)**

P(High Growth) = 45 / 100 = 9/20 = 0.45

**Answer: 0.45 or 45%**

**Part 3: P(Small and Low Growth)**

This is a joint probability from the cell (Small, Low Growth):

P(Small and Low Growth) = 35 / 100 = 7/20 = 0.35

**Answer: 0.35 or 35%**

**Key Concepts:**
- **Marginal probabilities** (P(A) or P(B)): sum of row or column
- **Joint probabilities** (P(A and B)): individual cell values
- All probabilities in the table sum to 1

### Notes

- Quality: AVERAGE
- Difficulty: VERY EASY
- Notes: Multi-part question distinguishing marginals from joints; good reinforcement
- Source: probability_mixed_easy_20260212.ipynb

## Comparing Two Marginal Probabilities

Given the following contingency table for gender and color preference:

|            | Prefers Blue (B) | Prefers Red (¬B) | Total |
|------------|------------------|------------------|-------|
| Male (A)   | 30               | 20               | 50    |
| Female (¬A) | 30              | 20               | 50    |
| **Total**  | **60**           | **40**           | **100** |

Compute both P(A) and P(B). Are they equal?

### Solution

P(A) = 50/100 = 1/2 = 0.50

P(B) = 60/100 = 3/5 = 0.60

**Are they equal?** No, P(A) = 0.50 ≠ 0.60 = P(B)

**Interpretation:** Marginal probabilities for different events need not be equal. Here, 50% are male but 60% prefer blue, so these probabilities differ.

### Notes

- Quality: GOOD
- Difficulty: VERY EASY
- Notes: Helps students understand that marginals for different events are independent quantities

## Verifying Complement Property

Given the following contingency table for loan approval:

|              | Approved (B) | Denied (¬B) | Total |
|--------------|--------------|-------------|-------|
| High Score (A) | 70         | 10          | 80    |
| Low Score (¬A) | 15         | 5           | 20    |
| **Total**    | **85**       | **15**      | **100** |

Verify that P(A) + P(¬A) = 1.

### Solution

P(A) = 80/100 = 0.80

P(¬A) = 20/100 = 0.20

Sum = 0.80 + 0.20 = 1.00 ✓

**Verification:** The probabilities of complementary events must sum to 1. This is a fundamental property of probability.

### Notes

- Quality: GOOD
- Difficulty: VERY EASY
- Notes: Verifies complement rule; fundamental probability axiom

## Union Probability Using Inclusion-Exclusion

Given the following contingency table for event attendance:

|               | Weekend Event (B) | Weekday Event (¬B) | Total |
|---------------|-------------------|--------------------|-------|
| Registered (A) | 40               | 30                 | 70    |
| Walk-in (¬A)  | 10               | 20                 | 30    |
| **Total**     | **50**            | **50**             | **100** |

Compute P(A ∪ B) using the formula P(A ∪ B) = P(A) + P(B) - P(A ∩ B).

### Solution

P(A) = 70/100 = 0.70
P(B) = 50/100 = 0.50
P(A ∩ B) = 40/100 = 0.40

P(A ∪ B) = 0.70 + 0.50 - 0.40 = 0.80

**Answer: 0.80 or 80%**

**Verification by counting:**
Outcomes with A or B or both = 40 (A∩B) + 30 (A∩¬B) + 10 (¬A∩B) = 80
So P(A ∪ B) = 80/100 = 0.80 ✓

**Key Insight:** The inclusion-exclusion principle prevents double-counting the intersection.

### Notes

- Quality: EXCELLENT
- Difficulty: EASY
- Notes: Demonstrates inclusion-exclusion principle; includes verification by direct counting

## Joint Probability as Fraction

Given the following contingency table for insurance claims:

|              | Filed Claim (B) | No Claim (¬B) | Total |
|--------------|-----------------|---------------|-------|
| Young (A)    | 18              | 42            | 60    |
| Older (¬A)   | 12              | 28            | 40    |
| **Total**    | **30**          | **70**        | **100** |

What fraction of all outcomes are in the cell (A ∩ B)?

### Solution

P(A ∩ B) = 18/100 = 9/50 = 0.18

**Answer: 9/50 = 0.18 or 18%**

**Interpretation:** 18% of all people are both young AND filed a claim. This is the joint probability, which is different from the marginals P(A) = 60% and P(B) = 30%.

### Notes

- Quality: GOOD
- Difficulty: VERY EASY
- Notes: Reinforces difference between joint and marginal probabilities

## Verifying All Four Joint Probabilities Sum to One

Given the following contingency table for project success:

|               | Successful (B) | Failed (¬B) | Total |
|---------------|----------------|-------------|-------|
| Experienced (A) | 48           | 12          | 60    |
| Novice (¬A)   | 24             | 16          | 40    |
| **Total**     | **72**         | **28**      | **100** |

Compute all four joint probabilities: P(A ∩ B), P(A ∩ ¬B), P(¬A ∩ B), P(¬A ∩ ¬B). Verify they sum to 1.

### Solution

P(A ∩ B) = 48/100 = 0.48
P(A ∩ ¬B) = 12/100 = 0.12
P(¬A ∩ B) = 24/100 = 0.24
P(¬A ∩ ¬B) = 16/100 = 0.16

Sum = 0.48 + 0.12 + 0.24 + 0.16 = 1.00 ✓

**Verification:** All four cells partition the sample space, so their probabilities must sum to 1.

**Key Insight:** The four joint probabilities in a 2×2 table form a complete partition of the sample space.

### Notes

- Quality: EXCELLENT
- Difficulty: EASY
- Notes: Demonstrates partition property; all joint probabilities cover the entire sample space

## Union via Counting vs Formula

Given the following contingency table for streaming service usage:

|               | Netflix (B) | No Netflix (¬B) | Total |
|---------------|-------------|-----------------|-------|
| Amazon (A)    | 35          | 25              | 60    |
| No Amazon (¬A) | 30         | 10              | 40    |
| **Total**     | **65**      | **35**          | **100** |

Show that P(A ∪ B) = (number of outcomes with A or B or both) / total. Then verify using the inclusion-exclusion formula.

### Solution

**Count method:**
Outcomes with A or B = 35 (A∩B) + 25 (A∩¬B) + 30 (¬A∩B) = 90
So P(A ∪ B) = 90/100 = 0.90

**Formula method:**
P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
         = 60/100 + 65/100 - 35/100
         = 90/100 = 0.90 ✓

**Interpretation:** 90% of people use at least one streaming service (Amazon, Netflix, or both).

### Notes

- Quality: EXCELLENT
- Difficulty: MEDIUM
- Notes: Shows two equivalent methods for computing unions; reinforces inclusion-exclusion principle

## Marginals as Sums of Joints - Law of Total Probability

Given the following contingency table for device ownership:

|              | Tablet (B) | No Tablet (¬B) | Total |
|--------------|------------|----------------|-------|
| Laptop (A)   | 30         | 50             | 80    |
| No Laptop (¬A) | 10       | 10             | 20    |
| **Total**    | **40**     | **60**         | **100** |

Express each marginal probability P(A), P(¬A), P(B), P(¬B) as a sum of joint probabilities. Verify the law of total probability holds.

### Solution

**Marginals from summing joints:**

P(A) = P(A ∩ B) + P(A ∩ ¬B) = 30/100 + 50/100 = 80/100 = 0.80 ✓

P(¬A) = P(¬A ∩ B) + P(¬A ∩ ¬B) = 10/100 + 10/100 = 20/100 = 0.20 ✓

P(B) = P(A ∩ B) + P(¬A ∩ B) = 30/100 + 10/100 = 40/100 = 0.40 ✓

P(¬B) = P(A ∩ ¬B) + P(¬A ∩ ¬B) = 50/100 + 10/100 = 60/100 = 0.60 ✓

**Verification:**
- P(A) + P(¬A) = 0.80 + 0.20 = 1.00 ✓
- P(B) + P(¬B) = 0.40 + 0.60 = 1.00 ✓

**Key Insight:** Marginal probabilities are obtained by "marginalizing out" (summing over) the other variable. This is the basis of the law of total probability.

### Notes

- Quality: EXCELLENT
- Difficulty: MEDIUM
- Notes: Fundamental concept showing relationship between marginals and joints; demonstrates law of total probability
