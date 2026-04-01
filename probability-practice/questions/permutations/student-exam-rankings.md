---
subject: permutations
difficulty: EASY
quality: GOOD
---
# Student Exam Rankings
## Question
A class in probability theory consists of 6 sophomores and 4 juniors. An examination is given, and the students are ranked according to their performance. Assume that no two students obtain the same score.

**(a)** How many different rankings are possible?

**(b)** If the sophomores are ranked just among themselves and the juniors just among themselves, how many different rankings are possible?
## Solution
**Part (a): Total rankings of all 10 students**

We have 10 students total that need to be ranked.

Number of rankings = 10! = 3,628,800

**Answer: 3,628,800 different rankings**

**Part (b): Separate rankings within each class**

If sophomores are ranked among themselves and juniors among themselves, we have:
- Rankings of 6 sophomores: 6!
- Rankings of 4 juniors: 4!

By the multiplication principle:

Total different ranking combinations = 6! × 4!

6! = 720
4! = 24

Total = 720 × 24 = 17,280

**Answer: 17,280 different ranking combinations**

**Key Insight:** Part (b) uses the multiplication principle: when we have independent choices (sophomore rankings and junior rankings), we multiply the number of ways for each choice.
