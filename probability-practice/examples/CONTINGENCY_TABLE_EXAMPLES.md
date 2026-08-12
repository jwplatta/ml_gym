# Contingency Table Examples

This file contains distinct examples of contingency tables organized by size. Each table is properly dimensioned (e.g., 3x3 means 3 features on both row and column axes).

## 2x2 Tables

### Example 1: Coffee and Tea Preferences
Context: Survey of 100 people about their coffee and tea drinking habits

|       | Tea (T) | No Tea (¬T) | Total |
|-------|---------|-------------|-------|
| Coffee (C) | 30 | 25 | 55 |
| No Coffee (¬C) | 20 | 25 | 45 |
| Total | 50 | 50 | 100 |

**Uses:** Basic conditional probability, comparing P(A|B) vs P(B|A)

---

### Example 2: Medical Test
Context: Diagnostic test for disease with 100 patients

|       | Test Positive (T+) | Test Negative (T-) | Total |
|-------|-------------------|-------------------|-------|
| Disease (D) | 18 | 2 | 20 |
| No Disease (¬D) | 8 | 72 | 80 |
| Total | 26 | 74 | 100 |

**Uses:** Bayes' theorem, sensitivity, specificity, positive predictive value

---

### Example 3: Study Habits and Exam Performance
Context: 100 university students

|       | Pass (P) | Fail (¬P) | Total |
|-------|----------|-----------|-------|
| Study (S) | 56 | 14 | 70 |
| Don't Study (¬S) | 12 | 18 | 30 |
| Total | 68 | 32 | 100 |

**Uses:** Law of total probability

---

### Example 4: Remote Work and Pet Ownership
Context: Company survey of 100 employees

|       | Pet (P) | No Pet (¬P) | Total |
|-------|---------|-------------|-------|
| Remote (R) | 24 | 16 | 40 |
| Not Remote (¬R) | 36 | 24 | 60 |
| Total | 60 | 40 | 100 |

**Uses:** Independence testing, this table exhibits perfect independence

---

### Example 5: Medical Screening (Larger Sample)
Context: Disease screening with 500 patients

|                  | Test + | Test - | Total |
|------------------|--------|--------|-------|
| Disease          | 85     | 15     | 100   |
| No Disease       | 40     | 360    | 400   |
| Total            | 125    | 375    | 500   |

**Uses:** Bayes' theorem with larger numbers, sensitivity = 85%, specificity = 90%

---

## 3x2 Tables (3 rows × 2 columns)

### Example 1: Transportation and Commuting
Context: Survey of 200 people about transportation preferences

|       | Commute (C) | No Commute (¬C) | Total |
|-------|-------------|-----------------|-------|
| Car   | 60          | 20              | 80    |
| Bus   | 45          | 15              | 60    |
| Bike  | 25          | 35              | 60    |
| Total | 130         | 70              | 200   |

**Uses:** Conditional probability with multiple categories on one axis

---

## 2x3 Tables (2 rows × 3 columns)

### Example 1: Course Difficulty and Pass Rates
Context: University students across 300 course enrollments

|        | Pass | Fail | Total |
|--------|------|------|-------|
| Easy   | 76   | 4    | 80    |
| Medium | 84   | 36   | 120   |
| Hard   | 40   | 60   | 100   |
| Total  | 200  | 100  | 300   |

**Uses:** Law of total probability with three conditioning events

---

## 3x3 Tables (3 rows × 3 columns)

### Example 1: Employee Satisfaction by Department
Context: Company with 240 employees across 3 departments

|             | Sales | Engineering | Marketing | Total |
|-------------|-------|-------------|-----------|-------|
| High        | 24    | 36          | 20        | 80    |
| Medium      | 30    | 40          | 30        | 100   |
| Low         | 16    | 24          | 20        | 60    |
| Total       | 70    | 100         | 70        | 240   |

**Uses:** Multiple conditional probabilities, comparing P(A|B) vs P(B|A) with more categories

---

### Example 2: Content Preferences by Subscription Tier
Context: Streaming service with 300 users

|               | Basic | Premium | Total |
|---------------|-------|---------|-------|
| Movies        | 48    | 72      | 120   |
| TV Shows      | 40    | 60      | 100   |
| Documentaries | 32    | 48      | 80    |
| Total         | 120   | 180     | 300   |

**Uses:** Independence testing with multiple categories, exhibits perfect independence (40% Basic across all content types)

---

## Notes on Table Dimensions

- **2x2 tables**: The fundamental case with binary variables (A vs ¬A, B vs ¬B)
- **3x2 or 2x3 tables**: One variable has 3+ categories, the other is binary
- **3x3 tables**: Both variables have 3 categories (no negation column/row)
- **nxm tables**: General case with n categories on one axis, m on the other

## Common Uses by Size

### 2x2 Tables
- Simplest case for learning conditional probability
- Easy to verify calculations manually
- Good for Bayes' theorem with binary outcomes
- Independence testing is straightforward

### 3x2 or 2x3 Tables
- Law of total probability with multiple partitions
- One variable is categorical, other is binary outcome
- Common in practical scenarios (multiple treatments, binary success/failure)

### 3x3 Tables
- Both variables are categorical
- More complex conditional probability calculations
- Better for practicing with realistic data
- Can still check independence, but requires checking multiple cells

## Pattern Recognition

### Independence Pattern
A table exhibits independence when:
- P(A|B) = P(A) for all categories
- Each row has the same proportions as the total
- Example: The streaming service table (40% Basic, 60% Premium in every row)

### Dependence Pattern
A table shows dependence when:
- P(A|B) ≠ P(A)
- Row proportions differ from overall proportions
- Example: The transportation table (Car users: 60/80 = 75% commute, but overall only 130/200 = 65% commute)
