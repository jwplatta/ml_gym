## Baseball Team Batting Order

How many different batting orders are possible for a baseball team consisting of 9 players?

### Solution

This is a permutation problem where we need to arrange 9 distinct players in a specific order.

The number of ways to arrange n distinct objects is n! (n factorial).

Number of batting orders = 9!

9! = 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 362,880

**Answer: 362,880 different batting orders**

**Explanation:**
- For the 1st position: 9 choices
- For the 2nd position: 8 remaining choices
- For the 3rd position: 7 remaining choices
- ... and so on
- Total: 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 9!

### Notes

- Quality: AVERAGE
- Difficulty: VERY EASY
- Notes: Basic factorial problem, good introduction to permutations

## Student Exam Rankings

A class in probability theory consists of 6 sophomores and 4 juniors. An examination is given, and the students are ranked according to their performance. Assume that no two students obtain the same score.

**(a)** How many different rankings are possible?

**(b)** If the sophomores are ranked just among themselves and the juniors just among themselves, how many different rankings are possible?

### Solution

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

### Notes

- Quality: GOOD
- Difficulty: EASY
- Notes: Tests understanding of factorial and multiplication principle with two-part question

## Bookshelf Arrangement by Subject

Ms. Jones has 10 books that she is going to put on her bookshelf. Of these, 4 are mathematics books, 3 are chemistry books, 2 are history books, and 1 is a language book. Ms. Jones wants to arrange her books so that all the books dealing with the same subject are together on the shelf. How many different arrangements are possible?

### Solution

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

### Notes

- Quality: GOOD
- Difficulty: MEDIUM
- Notes: Good example of hierarchical permutations and multiplication principle

## Letter Arrangements from PEPPER

How many different letter arrangements can be formed from the letters PEPPER?

### Solution

This is a permutation with repetition problem.

The word PEPPER has:
- Total letters: 6
- P appears: 3 times
- E appears: 2 times
- R appears: 1 time

When we have repeated items, we use the formula:

Number of arrangements = n! / (n₁! × n₂! × ... × nₖ!)

where n is the total number of items, and n₁, n₂, ..., nₖ are the frequencies of each repeated item.

Number of arrangements = 6! / (3! × 2! × 1!)

Calculate:
- 6! = 720
- 3! = 6
- 2! = 2
- 1! = 1

Number of arrangements = 720 / (6 × 2 × 1) = 720 / 12 = 60

**Answer: 60 different letter arrangements**

**Examples of arrangements:** PEPPER, PERPEP, EPPREP, REPPER, EPRPEP, etc.

**Key Insight:** When items are identical, we divide by the factorial of each group's size to avoid counting identical arrangements multiple times.

### Notes

- Quality: EXCELLENT
- Difficulty: EASY
- Notes: Classic permutations with repetition problem; teaches important concept of dividing by factorials of repeated items

## Chess Tournament Nationality Rankings

A chess tournament has 10 competitors, of which 4 are Russian, 3 are from the United States, 2 are from Great Britain, and 1 is from Brazil. If the tournament result lists just the nationalities of the players in the order in which they placed, how many outcomes are possible?

### Solution

Since we only care about the nationalities (not individual players), this is a permutation with repetition problem.

We have:
- Total positions: 10
- Russian (R): 4 players
- USA (U): 3 players
- Great Britain (G): 2 players
- Brazil (B): 1 player

Number of nationality orderings = 10! / (4! × 3! × 2! × 1!)

Calculate:
- 10! = 3,628,800
- 4! = 24
- 3! = 6
- 2! = 2
- 1! = 1

Number of orderings = 3,628,800 / (24 × 6 × 2 × 1)
Number of orderings = 3,628,800 / 288
Number of orderings = 12,600

**Answer: 12,600 different nationality orderings**

**Example orderings:** RRRRUUUGGB, BRRRRUUUGG, UUUGGBRRR, etc.

**Key Insight:** This is the multinomial coefficient, which counts the number of ways to arrange n items where items fall into k distinct groups with sizes n₁, n₂, ..., nₖ.

### Notes

- Quality: GOOD
- Difficulty: MEDIUM
- Notes: Good application of permutations with repetition; real-world tournament context

## Flag Signal Arrangements

How many different signals, each consisting of 9 flags hung in a line, can be made from a set of 4 white flags, 3 red flags, and 2 blue flags if all flags of the same color are identical?

### Solution

This is another permutation with repetition problem.

We have:
- Total flags: 9
- White flags: 4 (identical)
- Red flags: 3 (identical)
- Blue flags: 2 (identical)

Number of different signals = 9! / (4! × 3! × 2!)

Calculate:
- 9! = 362,880
- 4! = 24
- 3! = 6
- 2! = 2

Number of signals = 362,880 / (24 × 6 × 2)
Number of signals = 362,880 / 288
Number of signals = 1,260

**Answer: 1,260 different signals**

**Example signals:** WWWWRRRBBB, BWRWRWRWWB, RRRWWWWBB, etc.

**Key Insight:** This is the multinomial coefficient formula: n! / (n₁! × n₂! × ... × nₖ!), which gives the number of ways to arrange n objects when there are k types of identical objects with frequencies n₁, n₂, ..., nₖ.

### Notes

- Quality: GOOD
- Difficulty: EASY
- Notes: Practical application of permutations with repetition; flag signaling provides good visual context
