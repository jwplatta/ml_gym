# Very Easy Conditional Probability and Bayes Theorem Questions

### Question 1

**Prompt:**
Given the contingency table:

{{table}}

Compute P(A | B).

**Solution:**
P(A | B) = P(A ∩ B) / P(B) = ({{joint_AB}}/{{total}}) / ({{marginal_B}}/{{total}}) = {{joint_AB}}/{{marginal_B}} = {{simplified}}

### Question 2

**Prompt:**
Given the contingency table:

{{table}}

Compute both P(A | B) and P(B | A). Are they equal?

**Solution:**
P(A | B) = {{joint_AB}}/{{marginal_B}} = {{prob_A_given_B}}
P(B | A) = {{joint_AB}}/{{marginal_A}} = {{prob_B_given_A}}
{{comparison}}

### Question 3

**Prompt:**
Given the contingency table representing a medical test:

{{table}}

If a patient tests positive (B), what is the probability they actually have the disease (A)? Use Bayes' theorem to find P(A | B).

**Solution:**
**Direct method:**
P(A | B) = {{joint_AB}}/{{marginal_B}} = {{simplified}}

**Using Bayes' theorem:**
P(A | B) = P(B | A) × P(A) / P(B)

Where:
- P(B | A) = {{joint_AB}}/{{marginal_A}} = {{prob_B_given_A}} (sensitivity)
- P(A) = {{marginal_A}}/{{total}} = {{prob_A}} (prevalence)
- P(B) = {{marginal_B}}/{{total}} = {{prob_B}}

Therefore:
P(A | B) = ({{joint_AB}}/{{marginal_A}}) × ({{marginal_A}}/{{total}}) / ({{marginal_B}}/{{total}}) = {{joint_AB}}/{{marginal_B}} = {{simplified}}

This is the positive predictive value (PPV) of the test.

### Question 4

**Prompt:**
Given the contingency table with multiple categories:

{{table}}

Given that B occurred, what is the probability of A? Compute P(A | B) where A is one of several mutually exclusive categories.

**Solution:**
P(A | B) = P(A ∩ B) / P(B)

From the table:
- P(A ∩ B) = {{joint_AB}}/{{total}}
- P(B) = {{marginal_B}}/{{total}}

Therefore:
P(A | B) = ({{joint_AB}}/{{total}}) / ({{marginal_B}}/{{total}}) = {{joint_AB}}/{{marginal_B}} = {{simplified}}

**Interpretation:** Among all instances where B occurred ({{marginal_B}} total), {{joint_AB}} also had A, so P(A | B) = {{simplified}}.

### Question 5

**Prompt:**
Given the contingency table with multiple categories on both axes:

{{table}}

Compute both P(A | B) and P(B | A) where both A and B are categorical variables with multiple values. Are they equal? Why or why not?

**Solution:**
P(A | B) = {{joint_AB}}/{{marginal_B}} = {{prob_A_given_B}}
P(B | A) = {{joint_AB}}/{{marginal_A}} = {{prob_B_given_A}}

{{comparison}}

**Explanation:**
- P(A | B) = {{prob_A_given_B}} means {{interpretation_A_given_B}}
- P(B | A) = {{prob_B_given_A}} means {{interpretation_B_given_A}}

These have different denominators ({{marginal_B}} vs {{marginal_A}}), so they represent different questions and are generally not equal.

### Question 6

**Prompt:**
Given the contingency table with three mutually exclusive categories:

{{table}}

Use the law of total probability to compute P(B) from P(B | A₁), P(B | A₂), P(B | A₃) and their respective priors:
P(B) = P(B | A₁) × P(A₁) + P(B | A₂) × P(A₂) + P(B | A₃) × P(A₃)

Verify your answer matches the marginal probability in the table.

**Solution:**
First, calculate the components:
- P(B | A₁) = {{joint_A1_B}}/{{marginal_A1}}
- P(A₁) = {{marginal_A1}}/{{total}}
- P(B | A₂) = {{joint_A2_B}}/{{marginal_A2}}
- P(A₂) = {{marginal_A2}}/{{total}}
- P(B | A₃) = {{joint_A3_B}}/{{marginal_A3}}
- P(A₃) = {{marginal_A3}}/{{total}}

Using the law of total probability:
P(B) = P(B | A₁) × P(A₁) + P(B | A₂) × P(A₂) + P(B | A₃) × P(A₃)
P(B) = ({{joint_A1_B}}/{{marginal_A1}}) × ({{marginal_A1}}/{{total}}) + ({{joint_A2_B}}/{{marginal_A2}}) × ({{marginal_A2}}/{{total}}) + ({{joint_A3_B}}/{{marginal_A3}}) × ({{marginal_A3}}/{{total}})
P(B) = {{joint_A1_B}}/{{total}} + {{joint_A2_B}}/{{total}} + {{joint_A3_B}}/{{total}}
P(B) = {{marginal_B}}/{{total}} ✓

**Verification:** From the table, P(B) = {{marginal_B}}/{{total}} ✓

### Question 7

**Prompt:**
Given the contingency table with multiple categories:

{{table}}

1. Calculate P(A | B) and compare it to P(A)
2. Are events A and B independent? Explain why or why not.
3. Verify using the product rule: Does P(A ∩ B) = P(A) × P(B)?

**Solution:**
**Part 1: Calculate P(A | B) and P(A)**

P(A | B) = {{joint_AB}}/{{marginal_B}} = {{prob_A_given_B}}
P(A) = {{marginal_A}}/{{total}} = {{prob_A}}

**Part 2: Independence check**

{{independence_check}}

**Part 3: Verify with product rule**

P(A ∩ B) = {{joint_AB}}/{{total}} = {{prob_joint}}
P(A) × P(B) = ({{marginal_A}}/{{total}}) × ({{marginal_B}}/{{total}}) = {{prob_product}}

{{product_verification}}

**Explanation:**
Two events A and B are independent if P(A | B) = P(A).

{{independence_explanation}}

In this case: {{independence_conclusion}}
