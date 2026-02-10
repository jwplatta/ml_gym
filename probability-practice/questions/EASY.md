# Easy Conditional Probability and Bayes Theorem Questions

### Question 1

**Prompt:**
Given the contingency table:

{{table}}

Use the law of total probability to compute P(B) from P(B | A) and P(B | ¬A):
P(B) = P(B | A) × P(A) + P(B | ¬A) × P(¬A)

Verify your answer matches the marginal probability in the table.

**Solution:**
First, calculate the components:
- P(B | A) = {{joint_AB}}/{{marginal_A}}
- P(A) = {{marginal_A}}/{{total}}
- P(B | ¬A) = {{joint_notA_B}}/{{marginal_notA}}
- P(¬A) = {{marginal_notA}}/{{total}}

Using the law of total probability:
P(B) = P(B | A) × P(A) + P(B | ¬A) × P(¬A)
P(B) = ({{joint_AB}}/{{marginal_A}}) × ({{marginal_A}}/{{total}}) + ({{joint_notA_B}}/{{marginal_notA}}) × ({{marginal_notA}}/{{total}})
P(B) = {{joint_AB}}/{{total}} + {{joint_notA_B}}/{{total}}
P(B) = {{marginal_B}}/{{total}}

**Verification:** From the table, P(B) = {{marginal_B}}/{{total}}

### Question 2

**Prompt:**
Given the contingency table:

{{table}}

1. Calculate P(A | B) and compare it to P(A)
2. Are events A and B independent? Explain why or why not.

**Solution:**
**Part 1: Calculate P(A | B) and P(A)**

P(A | B) = {{joint_AB}}/{{marginal_B}} = {{prob_A_given_B}}
P(A) = {{marginal_A}}/{{total}} = {{prob_A}}

**Part 2: Independence check**

{{independence_check}}

**Explanation:**
Two events A and B are independent if P(A | B) = P(A).

{{independence_explanation}}

We can verify this further:
- P(A | ¬B) = {{joint_A_notB}}/{{marginal_notB}} = {{prob_A_given_notB}}
- P(A ∩ B) = {{joint_AB}}/{{total}} {{product_check}} P(A) × P(B) = {{prob_A}} × {{prob_B}}

---

## Word Problems (No Contingency Tables)

### Question 3: Library Books

**Prompt:**
A library has three sections: Fiction (F), Non-Fiction (N), and Reference (R). 50% of the books are Fiction, 30% are Non-Fiction, and 20% are Reference.

The checkout rates for each section are:
- P(Checked Out | Fiction) = 0.6
- P(Checked Out | Non-Fiction) = 0.4
- P(Checked Out | Reference) = 0.1

Questions:
1. What is the overall probability that a randomly selected book is checked out?
2. Given that a book is checked out, what is the probability it's a Fiction book?

**Solution:**

**Part 1: Overall checkout probability**

Using the law of total probability:
P(Checked Out) = P(C|F)×P(F) + P(C|N)×P(N) + P(C|R)×P(R)
P(Checked Out) = (0.6)(0.5) + (0.4)(0.3) + (0.1)(0.2)
P(Checked Out) = 0.3 + 0.12 + 0.02 = 0.44

**Part 2: Probability it's Fiction given checked out**

Using Bayes' theorem:
P(Fiction | Checked Out) = P(Checked Out | Fiction) × P(Fiction) / P(Checked Out)
P(Fiction | Checked Out) = (0.6)(0.5) / 0.44
P(Fiction | Checked Out) = 0.3 / 0.44 = 15/22 ≈ 0.682

### Question 4: Email Spam Filter

**Prompt:**
An email filter analyzes incoming messages. Based on historical data:
- 30% of all emails are spam
- 70% of all emails are legitimate

The filter flags emails as "Suspicious" based on certain keywords:
- P(Flagged | Spam) = 0.85 (true positive rate)
- P(Flagged | Legitimate) = 0.15 (false positive rate)

Question: If an email is flagged as suspicious, what is the probability it's actually spam?

**Solution:**

**Step 1: Calculate P(Flagged) using law of total probability**

P(Flagged) = P(Flagged | Spam) × P(Spam) + P(Flagged | Legitimate) × P(Legitimate)
P(Flagged) = (0.85)(0.3) + (0.15)(0.7)
P(Flagged) = 0.255 + 0.105 = 0.36

**Step 2: Apply Bayes' theorem**

P(Spam | Flagged) = P(Flagged | Spam) × P(Spam) / P(Flagged)
P(Spam | Flagged) = (0.85)(0.3) / 0.36
P(Spam | Flagged) = 0.255 / 0.36 = 17/24 ≈ 0.708

### Question 5: Manufacturing Quality Control

**Prompt:**
A factory has three machines (A, B, C) that produce widgets. Machine A produces 50% of the widgets, Machine B produces 30%, and Machine C produces 20%.

The defect rates are:
- P(Defective | Machine A) = 0.02
- P(Defective | Machine B) = 0.03
- P(Defective | Machine C) = 0.05

Questions:
1. If you randomly select a widget from the factory output, what is the probability it's defective?
2. If a widget is found to be defective, what is the probability it came from Machine A?
3. If a widget is found to be defective, which machine is most likely to have produced it?

**Solution:**

**Part 1: Overall defect rate**

P(Defective) = P(D|A)×P(A) + P(D|B)×P(B) + P(D|C)×P(C)
P(Defective) = (0.02)(0.5) + (0.03)(0.3) + (0.05)(0.2)
P(Defective) = 0.01 + 0.009 + 0.01 = 0.029

**Part 2: Probability from Machine A given defective**

P(Machine A | Defective) = P(D|A) × P(A) / P(D)
P(Machine A | Defective) = (0.02)(0.5) / 0.029
P(Machine A | Defective) = 0.01 / 0.029 = 10/29 ≈ 0.345

**Part 3: Compare all machines**

P(Machine B | Defective) = (0.03)(0.3) / 0.029 = 0.009 / 0.029 = 9/29 ≈ 0.310
P(Machine C | Defective) = (0.05)(0.2) / 0.029 = 0.01 / 0.029 = 10/29 ≈ 0.345

Machines A and C are equally likely (both 34.5%)

### Question 6: Weather and Commute Time

**Prompt:**
Your commute time depends on the weather. Historical data shows:
- P(Rain) = 0.3
- P(No Rain) = 0.7

Your commute is "Long" (over 45 minutes) with probabilities:
- P(Long Commute | Rain) = 0.6
- P(Long Commute | No Rain) = 0.2

Questions:
1. What is the probability that you have a long commute on any given day?
2. If you had a long commute today, what is the probability that it rained?
3. If you had a short commute today, what is the probability that it didn't rain?

**Solution:**

**Part 1: Probability of long commute**

P(Long) = P(Long | Rain) × P(Rain) + P(Long | No Rain) × P(No Rain)
P(Long) = (0.6)(0.3) + (0.2)(0.7)
P(Long) = 0.18 + 0.14 = 0.32

**Part 2: Probability it rained given long commute**

P(Rain | Long) = P(Long | Rain) × P(Rain) / P(Long)
P(Rain | Long) = (0.6)(0.3) / 0.32
P(Rain | Long) = 0.18 / 0.32 = 9/16 = 0.5625

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

### Question 7: Medical Diagnosis

**Prompt:**
A rare disease affects 1% of the population. A diagnostic test has been developed:
- P(Disease) = 0.01
- P(No Disease) = 0.99

The test has the following characteristics:
- Sensitivity: P(Positive Test | Disease) = 0.95
- Specificity: P(Negative Test | No Disease) = 0.90

Questions:
1. What is the probability of testing positive?
2. If someone tests positive, what is the probability they actually have the disease?
3. If someone tests negative, what is the probability they don't have the disease?

**Solution:**

First, identify all conditional probabilities:
- P(Positive | Disease) = 0.95 (sensitivity)
- P(Negative | No Disease) = 0.90 (specificity)
- P(Positive | No Disease) = 1 - 0.90 = 0.10 (false positive rate)
- P(Negative | Disease) = 1 - 0.95 = 0.05 (false negative rate)

**Part 1: Probability of testing positive**

P(Positive) = P(Positive | Disease) × P(Disease) + P(Positive | No Disease) × P(No Disease)
P(Positive) = (0.95)(0.01) + (0.10)(0.99)
P(Positive) = 0.0095 + 0.099 = 0.1085

**Part 2: Probability of disease given positive test (Positive Predictive Value)**

P(Disease | Positive) = P(Positive | Disease) × P(Disease) / P(Positive)
P(Disease | Positive) = (0.95)(0.01) / 0.1085
P(Disease | Positive) = 0.0095 / 0.1085 = 19/217 ≈ 0.0876

**Part 3: Probability of no disease given negative test (Negative Predictive Value)**

First, find P(Negative):
P(Negative) = P(Negative | Disease) × P(Disease) + P(Negative | No Disease) × P(No Disease)
P(Negative) = (0.05)(0.01) + (0.90)(0.99) = 0.0005 + 0.891 = 0.8915

Then apply Bayes' theorem:
P(No Disease | Negative) = P(Negative | No Disease) × P(No Disease) / P(Negative)
P(No Disease | Negative) = (0.90)(0.99) / 0.8915
P(No Disease | Negative) = 0.891 / 0.8915 ≈ 0.9994
