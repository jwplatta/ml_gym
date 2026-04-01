---
subject: bayes-theorem
difficulty: EASY
quality: GOOD
---
# Medical Diagnosis - Rare Disease
## Question
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
## Solution
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
