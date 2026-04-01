---
subject: bayes-theorem
difficulty: EASY
quality: GOOD
---
# Manufacturing Quality Control
## Question
A factory has three machines (A, B, C) that produce widgets. Machine A produces 50% of the widgets, Machine B produces 30%, and Machine C produces 20%.

The defect rates are:
- P(Defective | Machine A) = 0.02
- P(Defective | Machine B) = 0.03
- P(Defective | Machine C) = 0.05

**Questions:**
1. If you randomly select a widget from the factory output, what is the probability it's defective?
2. If a widget is found to be defective, what is the probability it came from Machine A?
3. If a widget is found to be defective, which machine is most likely to have produced it?
## Solution
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
