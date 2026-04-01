---
subject: permutations
difficulty: MEDIUM
quality: GOOD
---
# Bookshelf Arrangement by Subject
## Question
Ms. Jones has 10 books that she is going to put on her bookshelf. Of these, 4 are mathematics books, 3 are chemistry books, 2 are history books, and 1 is a language book. Ms. Jones wants to arrange her books so that all the books dealing with the same subject are together on the shelf. How many different arrangements are possible?
## Solution
Since books of the same subject must be together, we can think of this as a two-step process:

**Step 1: Arrange the 4 subject groups**

We have 4 subjects (Math, Chemistry, History, Language) that can be arranged in:
4! = 24 ways

**Step 2: Arrange books within each subject group**

- Math books can be arranged in: 4! = 24 ways
- Chemistry books can be arranged in: 3! = 6 ways
- History books can be arranged in: 2! = 2 ways
- Language book: 1! = 1 way (no variation)

**Apply multiplication principle:**

Total arrangements = (Ways to arrange groups) × (Ways within Math) × (Ways within Chem) × (Ways within History) × (Ways within Language)

Total = 4! × 4! × 3! × 2! × 1!

Total = 24 × 24 × 6 × 2 × 1 = 6,912

**Answer: 6,912 different arrangements**

**Key Insight:** This is a hierarchical permutation problem - first arrange groups, then arrange within each group, then multiply.
