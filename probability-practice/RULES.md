# Rules

## Notebooks

- Write all notebooks to the `/notebooks/practice` folder.
- Notebooks should not include summaries.

## Bayes Theorem Problems

- Do not provide the full contingency table for Bayes theorem problems. This makes them too easy because students can directly read P(A | B) from the table without actually using Bayes' theorem.
- Instead, provide only:
  - Prior probabilities: P(A), P(¬A)
  - Likelihoods: P(B | A), P(B | ¬A)
- Students should be forced to calculate P(B) by marginalizing: P(B) = P(B | A) × P(A) + P(B | ¬A) × P(¬A)
- This is what makes Bayes theorem problems challenging and ensures students practice the full calculation.
