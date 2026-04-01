---
subject: conditional-probability
difficulty: VERY EASY
quality: AVERAGE
---
# Company Size and Growth
## Question
Using the following contingency table:

|           | High Growth | Low Growth | **Total** |
|-----------|-------------|------------|----------|
| **Large** | 30          | 20         | 50       |
| **Small** | 15          | 35         | 50       |
| **Total** | 45          | 55         | 100      |

**Questions:**
1. Given that a company is Large, what is the probability it has High Growth?
2. Given that a company has High Growth, what is the probability it's Small?
## Solution
**Part 1: P(High Growth | Large)**

Method 1 (Direct counting): Given Large, restrict to the Large row:
- Total Large companies: 50
- Large companies with High Growth: 30
- P(High Growth | Large) = 30 / 50 = 3/5 = 0.6

Method 2 (Using formula):
P(High Growth | Large) = P(Large and High Growth) / P(Large)
                        = (30/100) / (50/100)
                        = 30/50 = 0.6

**Answer: 0.6 or 60%**

**Part 2: P(Small | High Growth)**

Method 1 (Direct counting): Given High Growth, restrict to the High Growth column:
- Total High Growth companies: 45
- Small companies with High Growth: 15
- P(Small | High Growth) = 15 / 45 = 1/3 ≈ 0.333

Method 2 (Using formula):
P(Small | High Growth) = P(Small and High Growth) / P(High Growth)
                        = (15/100) / (45/100)
                        = 15/45 = 1/3

**Answer: 1/3 ≈ 0.333 or about 33.3%**

**Key Insight:** When computing P(A | B), you "restrict" your attention to only the outcomes where B occurred.
