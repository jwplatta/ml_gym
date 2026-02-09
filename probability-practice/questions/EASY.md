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
