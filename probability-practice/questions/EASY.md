# Easy Conditional Probability and Bayes Theorem Questions

## Law of Total Probability - Verifying Marginals

Given the following contingency table for customer purchases at a retail store:

|            | Premium Member (B) | Regular Customer (¬B) | Total |
|------------|-------------------|-----------------------|-------|
| Made Purchase (A) | 70            | 30                    | 100   |
| No Purchase (¬A)  | 30            | 70                    | 100   |
| **Total**  | **100**           | **100**               | **200** |

Use the law of total probability to compute P(B) from P(B | A) and P(B | ¬A):

P(B) = P(B | A) × P(A) + P(B | ¬A) × P(¬A)

Verify your answer matches the marginal probability in the table.

### Solution

First, calculate the components:
- P(B | A) = 70/100 = 0.70
- P(A) = 100/200 = 0.50
- P(B | ¬A) = 30/100 = 0.30
- P(¬A) = 100/200 = 0.50

Using the law of total probability:

P(B) = P(B | A) × P(A) + P(B | ¬A) × P(¬A)

P(B) = (0.70)(0.50) + (0.30)(0.50)

P(B) = 0.35 + 0.15 = 0.50

**Verification:** From the table, P(B) = 100/200 = 0.50 ✓

**Answer: 0.50 or 50%**

### Notes

- Quality: GOOD
- Difficulty: EASY
- Notes: Clear demonstration of law of total probability with verification against marginals

## Testing for Independence with Calculations

Given the following contingency table for credit card usage and online shopping:

|                  | Online Shopper (B) | Not Online Shopper (¬B) | Total |
|------------------|-------------------|------------------------|-------|
| Credit Card (A)  | 48                | 32                     | 80    |
| Debit Only (¬A)  | 12                | 8                      | 20    |
| **Total**        | **60**            | **40**                 | **100** |

1. Calculate P(A | B) and compare it to P(A)
2. Are events A and B independent? Explain why or why not.

### Solution

**Part 1: Calculate P(A | B) and P(A)**

P(A | B) = 48/60 = 4/5 = 0.80

P(A) = 80/100 = 4/5 = 0.80

**Part 2: Independence check**

Since P(A | B) = P(A) = 0.80, the events appear to be independent. Knowing that someone is an online shopper doesn't change the probability they have a credit card.

**Explanation:**

Two events A and B are independent if P(A | B) = P(A).

We can verify this further:
- P(A | ¬B) = 32/40 = 4/5 = 0.80
- P(A ∩ B) = 48/100 = 0.48 = P(A) × P(B) = (0.80)(0.60) = 0.48 ✓

All checks confirm independence: having a credit card and being an online shopper are independent in this dataset.

### Notes

- Quality: GOOD
- Difficulty: EASY
- Notes: Demonstrates multiple ways to verify independence; shows that P(A|B) = P(A|¬B) = P(A) when events are independent

## Library Books

A library has three sections: Fiction (F), Non-Fiction (N), and Reference (R). 50% of the books are Fiction, 30% are Non-Fiction, and 20% are Reference.

The checkout rates for each section are:
- P(Checked Out | Fiction) = 0.6
- P(Checked Out | Non-Fiction) = 0.4
- P(Checked Out | Reference) = 0.1

**Questions:**
1. What is the overall probability that a randomly selected book is checked out?
2. Given that a book is checked out, what is the probability it's a Fiction book?

### Solution

**Part 1: Overall checkout probability**

Using the law of total probability:

P(Checked Out) = P(C|F)×P(F) + P(C|N)×P(N) + P(C|R)×P(R)

P(Checked Out) = (0.6)(0.5) + (0.4)(0.3) + (0.1)(0.2)

P(Checked Out) = 0.3 + 0.12 + 0.02 = 0.44

**Answer: 0.44 or 44%**

**Part 2: Probability it's Fiction given checked out**

Using Bayes' theorem:

P(Fiction | Checked Out) = P(Checked Out | Fiction) × P(Fiction) / P(Checked Out)

P(Fiction | Checked Out) = (0.6)(0.5) / 0.44

P(Fiction | Checked Out) = 0.3 / 0.44 = 15/22 ≈ 0.682

**Answer: 15/22 ≈ 0.682 or about 68.2%**

**Interpretation:** Among checked-out books, about 68% are fiction, which is higher than the overall 50% fiction rate. This makes sense because fiction has the highest checkout rate (60%).

### Notes

- Quality: GOOD
- Difficulty: EASY
- Notes: Practical application combining law of total probability with Bayes' theorem; library context is relatable

## Email Spam Filter

An email filter analyzes incoming messages. Based on historical data:
- 30% of all emails are spam
- 70% of all emails are legitimate

The filter flags emails as "Suspicious" based on certain keywords:
- P(Flagged | Spam) = 0.85 (true positive rate)
- P(Flagged | Legitimate) = 0.15 (false positive rate)

**Question:** If an email is flagged as suspicious, what is the probability it's actually spam?

### Solution

**Step 1: Calculate P(Flagged) using law of total probability**

P(Flagged) = P(Flagged | Spam) × P(Spam) + P(Flagged | Legitimate) × P(Legitimate)

P(Flagged) = (0.85)(0.3) + (0.15)(0.7)

P(Flagged) = 0.255 + 0.105 = 0.36

**Step 2: Apply Bayes' theorem**

P(Spam | Flagged) = P(Flagged | Spam) × P(Spam) / P(Flagged)

P(Spam | Flagged) = (0.85)(0.3) / 0.36

P(Spam | Flagged) = 0.255 / 0.36 = 17/24 ≈ 0.708

**Answer: 17/24 ≈ 0.708 or about 70.8%**

**Interpretation:** About 71% of flagged emails are actually spam, while 29% are false positives (legitimate emails incorrectly flagged).

### Notes

- Quality: GOOD
- Difficulty: EASY
- Notes: Relevant modern application; demonstrates importance of false positive rates in classification systems

## Manufacturing Quality Control

A factory has three machines (A, B, C) that produce widgets. Machine A produces 50% of the widgets, Machine B produces 30%, and Machine C produces 20%.

The defect rates are:
- P(Defective | Machine A) = 0.02
- P(Defective | Machine B) = 0.03
- P(Defective | Machine C) = 0.05

**Questions:**
1. If you randomly select a widget from the factory output, what is the probability it's defective?
2. If a widget is found to be defective, what is the probability it came from Machine A?
3. If a widget is found to be defective, which machine is most likely to have produced it?

### Solution

**Part 1: Overall defect rate**

Using the law of total probability:

P(Defective) = P(D|A)×P(A) + P(D|B)×P(B) + P(D|C)×P(C)

P(Defective) = (0.02)(0.5) + (0.03)(0.3) + (0.05)(0.2)

P(Defective) = 0.01 + 0.009 + 0.01 = 0.029

**Answer: 0.029 or 2.9%**

**Part 2: Probability from Machine A given defective**

Using Bayes' theorem:

P(Machine A | Defective) = P(D|A) × P(A) / P(D)

P(Machine A | Defective) = (0.02)(0.5) / 0.029

P(Machine A | Defective) = 0.01 / 0.029 = 10/29 ≈ 0.345

**Answer: 10/29 ≈ 0.345 or about 34.5%**

**Part 3: Compare all machines**

Calculate for each machine:

P(Machine B | Defective) = (0.03)(0.3) / 0.029 = 0.009 / 0.029 = 9/29 ≈ 0.310

P(Machine C | Defective) = (0.05)(0.2) / 0.029 = 0.01 / 0.029 = 10/29 ≈ 0.345

**Answer: Machines A and C are equally likely (both 34.5%)**

**Interpretation:** Even though Machine C has the highest defect rate (5%), it produces the fewest widgets (20%). Machine A has the lowest defect rate (2%) but produces the most widgets (50%). These factors balance out, making them equally likely sources of defects.

### Notes

- Quality: EXCELLENT
- Difficulty: EASY
- Notes: Great example showing how prior probabilities (production volume) interact with likelihoods (defect rates); three-way comparison reinforces Bayes' theorem

## Weather and Commute Time

Your commute time depends on the weather. Historical data shows:
- P(Rain) = 0.3
- P(No Rain) = 0.7

Your commute is "Long" (over 45 minutes) with probabilities:
- P(Long Commute | Rain) = 0.6
- P(Long Commute | No Rain) = 0.2

**Questions:**
1. What is the probability that you have a long commute on any given day?
2. If you had a long commute today, what is the probability that it rained?
3. If you had a short commute today, what is the probability that it didn't rain?

### Solution

**Part 1: Probability of long commute**

Using the law of total probability:

P(Long) = P(Long | Rain) × P(Rain) + P(Long | No Rain) × P(No Rain)

P(Long) = (0.6)(0.3) + (0.2)(0.7)

P(Long) = 0.18 + 0.14 = 0.32

**Answer: 0.32 or 32%**

**Part 2: Probability it rained given long commute**

Using Bayes' theorem:

P(Rain | Long) = P(Long | Rain) × P(Rain) / P(Long)

P(Rain | Long) = (0.6)(0.3) / 0.32

P(Rain | Long) = 0.18 / 0.32 = 9/16 = 0.5625

**Answer: 9/16 = 0.5625 or 56.25%**

**Part 3: Probability it didn't rain given short commute**

First, find the conditional probabilities for short commute:
- P(Short | Rain) = 1 - P(Long | Rain) = 1 - 0.6 = 0.4
- P(Short | No Rain) = 1 - P(Long | No Rain) = 1 - 0.2 = 0.8

Then, find P(Short):

P(Short) = P(Short | Rain) × P(Rain) + P(Short | No Rain) × P(No Rain)

P(Short) = (0.4)(0.3) + (0.8)(0.7) = 0.12 + 0.56 = 0.68

Finally, apply Bayes' theorem:

P(No Rain | Short) = P(Short | No Rain) × P(No Rain) / P(Short)

P(No Rain | Short) = (0.8)(0.7) / 0.68 = 0.56 / 0.68 = 14/17 ≈ 0.824

**Answer: 14/17 ≈ 0.824 or about 82.4%**

**Interpretation:** A short commute is good evidence it didn't rain (82% probability), while a long commute is moderate evidence it rained (56% probability). This asymmetry occurs because rain strongly increases commute time, but other factors can also cause long commutes.

### Notes

- Quality: EXCELLENT
- Difficulty: EASY
- Notes: Excellent multi-part problem requiring complements, law of total probability, and Bayes' theorem; demonstrates asymmetry in inference

## Medical Diagnosis - Rare Disease

A rare disease affects 1% of the population. A diagnostic test has been developed:
- P(Disease) = 0.01
- P(No Disease) = 0.99

The test has the following characteristics:
- Sensitivity: P(Positive Test | Disease) = 0.95
- Specificity: P(Negative Test | No Disease) = 0.90

**Questions:**
1. What is the probability of testing positive?
2. If someone tests positive, what is the probability they actually have the disease?
3. If someone tests negative, what is the probability they don't have the disease?

### Solution

First, identify all conditional probabilities:
- P(Positive | Disease) = 0.95 (sensitivity)
- P(Negative | No Disease) = 0.90 (specificity)
- P(Positive | No Disease) = 1 - 0.90 = 0.10 (false positive rate)
- P(Negative | Disease) = 1 - 0.95 = 0.05 (false negative rate)

**Part 1: Probability of testing positive**

Using the law of total probability:

P(Positive) = P(Positive | Disease) × P(Disease) + P(Positive | No Disease) × P(No Disease)

P(Positive) = (0.95)(0.01) + (0.10)(0.99)

P(Positive) = 0.0095 + 0.099 = 0.1085

**Answer: 0.1085 or 10.85%**

**Part 2: Probability of disease given positive test (Positive Predictive Value)**

Using Bayes' theorem:

P(Disease | Positive) = P(Positive | Disease) × P(Disease) / P(Positive)

P(Disease | Positive) = (0.95)(0.01) / 0.1085

P(Disease | Positive) = 0.0095 / 0.1085 = 19/217 ≈ 0.0876

**Answer: 19/217 ≈ 0.0876 or about 8.76%**

**Part 3: Probability of no disease given negative test (Negative Predictive Value)**

First, find P(Negative):

P(Negative) = P(Negative | Disease) × P(Disease) + P(Negative | No Disease) × P(No Disease)

P(Negative) = (0.05)(0.01) + (0.90)(0.99) = 0.0005 + 0.891 = 0.8915

Then apply Bayes' theorem:

P(No Disease | Negative) = P(Negative | No Disease) × P(No Disease) / P(Negative)

P(No Disease | Negative) = (0.90)(0.99) / 0.8915

P(No Disease | Negative) = 0.891 / 0.8915 ≈ 0.9994

**Answer: ≈ 0.9994 or about 99.94%**

**Key Insight:** Even with a highly accurate test (95% sensitivity, 90% specificity), a positive result only means 8.76% chance of having the disease! This is the "base rate fallacy" - the disease is so rare (1%) that most positive tests are false positives. However, a negative test is very reliable (99.94% chance of being disease-free).

### Notes

- Quality: EXCELLENT
- Difficulty: EASY
- Notes: Classic example of base rate fallacy; demonstrates why positive predictive value is low for rare diseases despite high test accuracy; crucial for medical decision-making
