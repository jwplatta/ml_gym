# Conditional Probability Questions

## Basic Conditional Probability P(A|B)

Given the following contingency table for product purchases:

|              | Premium (B) | Standard (¬B) | Total |
|--------------|-------------|---------------|-------|
| Existing Customer (A) | 60    | 40            | 100   |
| New Customer (¬A)     | 20    | 30            | 50    |
| **Total**    | **80**      | **70**        | **150** |

Compute P(A | B) - the probability a customer is existing given they purchased premium.

### Solution

P(A | B) = P(A ∩ B) / P(B)
         = (60/150) / (80/150)
         = 60/80
         = 3/4
         = 0.75

**Answer: 3/4 = 0.75 or 75%**

**Interpretation:** Among premium customers, 75% are existing customers.

### Notes

- Quality: GOOD
- Difficulty: VERY EASY
- Notes: Basic introduction to conditional probability formula

## Basic Conditional Probability P(B|A)

Given the following contingency table for employee performance:

|              | High Performer (B) | Low Performer (¬B) | Total |
|--------------|-------------------|-------------------|-------|
| Manager (A)  | 35                | 15                | 50    |
| Individual (¬A) | 45             | 30                | 75    |
| **Total**    | **80**            | **45**            | **125** |

Compute P(B | A) - the probability an employee is a high performer given they are a manager.

### Solution

P(B | A) = P(A ∩ B) / P(A)
         = (35/125) / (50/125)
         = 35/50
         = 7/10
         = 0.70

**Answer: 7/10 = 0.70 or 70%**

**Interpretation:** Among managers, 70% are high performers.

### Notes

- Quality: GOOD
- Difficulty: VERY EASY
- Notes: Demonstrates the distinction between P(A|B) and P(B|A)

## Alternative Phrasing

Given the following contingency table for medical screening:

|              | Positive Test (B) | Negative Test (¬B) | Total |
|--------------|------------------|-------------------|-------|
| Disease (A)  | 45               | 5                 | 50    |
| No Disease (¬A) | 10            | 140               | 150   |
| **Total**    | **55**           | **145**           | **200** |

What is the probability of having the disease given a positive test result?

### Solution

P(A | B) = 45/55 = 9/11 ≈ 0.818

**Answer: 9/11 ≈ 0.818 or about 81.8%**

**Interpretation:** Among those who tested positive, about 82% actually have the disease.

### Notes

- Quality: GOOD
- Difficulty: VERY EASY
- Notes: Medical context for conditional probability; demonstrates positive predictive value

## Conditional Probability of Complement

Given the following contingency table for marketing campaigns:

|              | Converted (B) | No Conversion (¬B) | Total |
|--------------|---------------|-------------------|-------|
| Email Sent (A) | 25          | 75                | 100   |
| No Email (¬A) | 10           | 90                | 100   |
| **Total**    | **35**        | **165**           | **200** |

Find P(¬A | B) - the probability no email was sent given a conversion occurred.

### Solution

P(¬A | B) = P(¬A ∩ B) / P(B)
          = (10/200) / (35/200)
          = 10/35
          = 2/7
          ≈ 0.286

**Answer: 2/7 ≈ 0.286 or about 28.6%**

**Interpretation:** Among conversions, about 29% occurred without sending an email.

### Notes

- Quality: GOOD
- Difficulty: VERY EASY
- Notes: Introduces conditional probability with complement events

## Company Size and Growth

Using the following contingency table:

|           | High Growth | Low Growth | **Total** |
|-----------|-------------|------------|----------|
| **Large** | 30          | 20         | 50       |
| **Small** | 15          | 35         | 50       |
| **Total** | 45          | 55         | 100      |

**Questions:**
1. Given that a company is Large, what is the probability it has High Growth?
2. Given that a company has High Growth, what is the probability it's Small?

### Solution

**Part 1: P(High Growth | Large)**

Method 1 (Direct counting): Given Large, restrict to the Large row:
- Total Large companies: 50
- Large companies with High Growth: 30
- P(High Growth | Large) = 30 / 50 = 3/5 = 0.6

Method 2 (Using formula):
P(High Growth | Large) = P(Large and High Growth) / P(Large)
                        = (30/100) / (50/100)
                        = 30/50 = 0.6

**Answer: 0.6 or 60%**

**Part 2: P(Small | High Growth)**

Method 1 (Direct counting): Given High Growth, restrict to the High Growth column:
- Total High Growth companies: 45
- Small companies with High Growth: 15
- P(Small | High Growth) = 15 / 45 = 1/3 ≈ 0.333

Method 2 (Using formula):
P(Small | High Growth) = P(Small and High Growth) / P(High Growth)
                        = (15/100) / (45/100)
                        = 15/45 = 1/3

**Answer: 1/3 ≈ 0.333 or about 33.3%**

**Key Insight:** When computing P(A | B), you "restrict" your attention to only the outcomes where B occurred.

### Notes

- Quality: AVERAGE
- Difficulty: VERY EASY
- Notes: Multi-part question demonstrating two calculation methods
- Source: probability_mixed_easy_20260212.ipynb

## Card Drawing Without Replacement

You draw 2 cards from a standard deck of 52 cards without replacement.

**Questions:**
1. What is the probability that both cards are aces?
2. What is the probability that the second card is an ace, given that the first card was an ace?
3. What is the probability that at least one card is an ace?

### Solution

**Part 1: P(both cards are aces)**

P(both aces) = P(1st ace) × P(2nd ace | 1st ace)

P(1st ace) = 4/52 = 1/13

P(2nd ace | 1st ace) = 3/51 = 1/17

P(both aces) = (4/52) × (3/51) = 12/2,652 = 1/221

**Answer: 1/221 ≈ 0.00452 or about 0.45%**

**Part 2: P(2nd ace | 1st ace)**

Given the first card was an ace, there are now:
- 51 cards remaining
- 3 aces remaining

P(2nd ace | 1st ace) = 3/51 = 1/17 ≈ 0.0588

**Answer: 1/17 ≈ 0.0588 or about 5.88%**

**Part 3: P(at least one ace)**

Method 1 (Complement):

P(at least one ace) = 1 - P(no aces)

P(no aces) = P(1st not ace) × P(2nd not ace | 1st not ace)

P(no aces) = (48/52) × (47/51) = 2,256/2,652 = 188/221

P(at least one ace) = 1 - 188/221 = 33/221

**Answer: 33/221 ≈ 0.1493 or about 14.93%**

Method 2 (Direct):

P(at least one) = P(ace, not ace) + P(not ace, ace) + P(ace, ace)

= (4/52)(48/51) + (48/52)(4/51) + (4/52)(3/51)

= 192/2,652 + 192/2,652 + 12/2,652

= 396/2,652 = 33/221 ✓

**Key Insight:** When sampling without replacement, probabilities change after each draw. The complement approach is often simpler for "at least one" questions.

### Notes

- Quality: GOOD
- Difficulty: EASY
- Notes: Tests understanding of conditional probability with changing sample space; demonstrates complement method

## Comparing P(A|B) and P(B|A)

Given the following contingency table for insurance claims:

|              | Filed Claim (B) | No Claim (¬B) | Total |
|--------------|-----------------|---------------|-------|
| Young Driver (A) | 20          | 30            | 50    |
| Older Driver (¬A) | 10         | 90            | 100   |
| **Total**    | **30**          | **120**       | **150** |

Compute both P(A | B) and P(B | A). Are they equal?

### Solution

P(A | B) = 20/30 = 2/3 ≈ 0.667

P(B | A) = 20/50 = 2/5 = 0.40

**Are they equal?** No, P(A | B) = 0.667 ≠ 0.40 = P(B | A)

**Interpretation:**
- P(A | B) = 0.667 means: Among those who filed claims, 66.7% are young drivers
- P(B | A) = 0.40 means: Among young drivers, 40% filed claims

These answer different questions, so they're generally not equal.

### Notes

- Quality: EXCELLENT
- Difficulty: EASY
- Notes: Demonstrates the asymmetry of conditional probability; important conceptual lesson

## Complement Rule for Conditional Probabilities

Given the following contingency table for loan applications:

|              | Approved (B) | Denied (¬B) | Total |
|--------------|--------------|-------------|-------|
| High Score (A) | 70         | 10          | 80    |
| Low Score (¬A) | 20          | 50          | 70    |
| **Total**    | **90**       | **60**      | **150** |

Verify that P(A | B) + P(¬A | B) = 1.

### Solution

P(A | B) = 70/90 = 7/9 ≈ 0.778

P(¬A | B) = 20/90 = 2/9 ≈ 0.222

Sum = 7/9 + 2/9 = 9/9 = 1 ✓

**Verification:** The conditional probabilities of complementary events given the same condition must sum to 1.

**Key Property:** For any events A and B, P(A | B) + P(¬A | B) = 1, just as P(A) + P(¬A) = 1 for unconditional probabilities.

### Notes

- Quality: GOOD
- Difficulty: EASY
- Notes: Demonstrates complement rule for conditional probabilities; fundamental property

## Comparing Conditional Probabilities

Given the following contingency table for customer retention:

|              | Renewed (B) | Churned (¬B) | Total |
|--------------|-------------|--------------|-------|
| Contacted (A) | 80         | 20           | 100   |
| Not Contacted (¬A) | 30    | 70           | 100   |
| **Total**    | **110**     | **90**       | **200** |

Compute P(A | B) and P(A | ¬B). Which conditioning event makes A more likely?

### Solution

P(A | B) = 80/110 = 8/11 ≈ 0.727

P(A | ¬B) = 20/90 = 2/9 ≈ 0.222

**Comparison:** P(A | B) = 0.727 > 0.222 = P(A | ¬B)

**Conclusion:** Conditioning on B (renewal) makes A (being contacted) much more likely. This suggests that contacting customers is associated with higher renewal rates.

### Notes

- Quality: EXCELLENT
- Difficulty: EASY
- Notes: Demonstrates how different conditioning events affect probabilities; good for understanding association

## Verification Using Definition

Given the following contingency table for website traffic:

|              | Converted (B) | No Conversion (¬B) | Total |
|--------------|---------------|-------------------|-------|
| Ad Click (A) | 40            | 60                | 100   |
| Organic (¬A) | 20            | 80                | 100   |
| **Total**    | **60**        | **140**           | **200** |

Use the definition P(A | B) = P(A ∩ B) / P(B) to find P(A | B), then verify by directly counting in the table.

### Solution

**Formula method:**

P(A | B) = P(A ∩ B) / P(B)
         = (40/200) / (60/200)
         = 40/60
         = 2/3
         ≈ 0.667

**Direct count method:**

In column B (60 conversions total), 40 came from ad clicks.

So P(A | B) = 40/60 = 2/3 ≈ 0.667 ✓

**Both methods agree!**

### Notes

- Quality: GOOD
- Difficulty: EASY
- Notes: Demonstrates equivalence of formula and direct counting methods

## All Four Conditional Probabilities

Given the following contingency table for product returns:

|              | Returned (B) | Kept (¬B) | Total |
|--------------|--------------|-----------|-------|
| Online (A)   | 30           | 70        | 100   |
| In-Store (¬A) | 10          | 90        | 100   |
| **Total**    | **40**       | **160**   | **200** |

Compute all four conditional probabilities: P(A|B), P(¬A|B), P(A|¬B), P(¬A|¬B). Verify that P(A|B) + P(¬A|B) = 1 and P(A|¬B) + P(¬A|¬B) = 1.

### Solution

**Conditional on B (Returned):**

P(A | B) = 30/40 = 3/4 = 0.75

P(¬A | B) = 10/40 = 1/4 = 0.25

**Conditional on ¬B (Kept):**

P(A | ¬B) = 70/160 = 7/16 ≈ 0.438

P(¬A | ¬B) = 90/160 = 9/16 ≈ 0.562

**Verify complement rules:**

P(A|B) + P(¬A|B) = 3/4 + 1/4 = 1 ✓

P(A|¬B) + P(¬A|¬B) = 7/16 + 9/16 = 16/16 = 1 ✓

**Interpretation:** Online purchases have a higher return rate (30%) compared to in-store purchases (10%), which is reflected in the conditional probabilities.

### Notes

- Quality: EXCELLENT
- Difficulty: MEDIUM
- Notes: Comprehensive problem covering all conditional probabilities in a 2×2 table

## Multiplication Rule Verification

Given the following contingency table for project outcomes:

|              | Success (B) | Failure (¬B) | Total |
|--------------|-------------|--------------|-------|
| Experienced Team (A) | 56 | 14       | 70    |
| New Team (¬A) | 24        | 36           | 60    |
| **Total**    | **80**      | **50**       | **130** |

Show that P(A ∩ B) = P(A | B) × P(B) using the table data. Then verify the same using P(A ∩ B) = P(B | A) × P(A).

### Solution

**Method 1: P(A ∩ B) = P(A | B) × P(B)**

P(A | B) = 56/80 = 7/10 = 0.70

P(B) = 80/130 = 8/13 ≈ 0.615

P(A | B) × P(B) = (56/80) × (80/130) = 56/130

Direct from table: P(A ∩ B) = 56/130 ✓

**Method 2: P(A ∩ B) = P(B | A) × P(A)**

P(B | A) = 56/70 = 4/5 = 0.80

P(A) = 70/130 = 7/13 ≈ 0.538

P(B | A) × P(A) = (56/70) × (70/130) = 56/130

Direct from table: P(A ∩ B) = 56/130 ✓

**Conclusion:** Both formulations of the multiplication rule give the same result, confirming their equivalence.

### Notes

- Quality: EXCELLENT
- Difficulty: MEDIUM
- Notes: Demonstrates multiplication rule from two perspectives; fundamental relationship between joint and conditional probabilities
