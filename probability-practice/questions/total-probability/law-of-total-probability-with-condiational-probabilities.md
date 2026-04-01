---
subject: total-probability
difficulty: EASY
quality: GOOD
---
# Law of Total Probability with Condiational Probabilities
## Question
A factory produces light bulbs. 10% are defective (D), 90% are not defective (¬D). Each bulb is inspected twice.
- If a bulb is defective, each inspection independently flags it as “bad” with probability 0.9.
- If a bulb is not defective, each inspection independently flags it as “bad” with probability 0.05.

Suppose the first inspection flagged the bulb as bad. What is the probability that the second inspection also flags it as bad?
## Solution
P(Bad₂ | Bad₁)

Using the law of total probability inside the conditional world where Bad₁ has already happened:

P(Bad₂ | Bad₁) = P(Bad₂ | D, Bad₁) P(D | Bad₁) + P(Bad₂ | ¬D, Bad₁) P(¬D | Bad₁)

This step is always valid — we’re partitioning on D vs ¬D while conditioning on Bad₁. Then, using conditional independence of inspections given defect status:

P(Bad₂ | D, Bad₁) = P(Bad₂ | D) = 0.9
P(Bad₂ | ¬D, Bad₁) = P(Bad₂ | ¬D) = 0.05

So: P(Bad₂ | Bad₁) = 0.9 · P(D | Bad₁) + 0.05 · P(¬D | Bad₁)

That is exactly the law of total probability operating "inside" a conditional world.

The structure is always:

P(A | B) = P(A | C, B) P(C | B) + P(A | ¬C, B) P(¬C | B)

You're just slicing uncertainty about C after already assuming B happened.
