---
subject: expectation
difficulty: VERY EASY
quality: AVERAGE
---
# Indicator Variable for Dividend
## Question
Consider a stock that pays a dividend. Let D be an indicator variable:
- D = 1 if the stock pays a dividend (probability 0.7)
- D = 0 if no dividend (probability 0.3)

**Question:** What is E[D]?
## Solution
E[D] = 1 × P(D=1) + 0 × P(D=0)

E[D] = 1 × (0.7) + 0 × (0.3)

E[D] = 0.7

**Answer: 0.7**

**Key Insight:**

For any indicator variable (Bernoulli random variable):
```
E[indicator of event A] = P(A)
```

This is an extremely useful property! It means:
- Expected value of indicator = probability of the event
- You can think of probability as "expected proportion of times the event occurs"

**Example applications:**
- E[indicator of heads] = P(Heads) = 0.5
- E[indicator of dividend] = P(Dividend) = 0.7
- E[indicator of default] = P(Default)
