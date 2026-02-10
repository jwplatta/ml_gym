# Quant Practice Rules

1. Prefer explicit core formulas over convenience shortcuts when teaching important concepts.
2. For returns, prefer `ret = px / px.shift() - 1` over `px.pct_change()` so students see and internalize the underlying calculation.
3. Apply the same principle to other foundational metrics (e.g., Sharpe, beta, residual returns): show the full expression when feasible.
