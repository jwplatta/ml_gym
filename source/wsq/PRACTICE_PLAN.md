# WSQ Practice Examples

## Example Index

### Core Workflow Examples (Ordered by Workflow Stage)

**Stage 1-2: Signal Ideas & Unconstrained Backtests**
- `momentum_returns.py` - Time-series momentum using rolling Sharpe ratios
- `unconstrained_backtest_SP500.py` - Mean-reversion on S&P 500 (rank-based & decile)
- `turnover.py` - Mean-reversion with transaction cost analysis (crypto)

**Stage 3: Breadth (Multi-Asset)**
- `beta_alpha_factor_models.py` - Beta/alpha decomposition across FAANG stocks
- `unconstrained_backtest_SP500.py` - 500-stock universe strategies

**Stage 4: Weighting & Portfolio Construction**
- `portfolio_weighting.py` - Comparing optimal, equal-vol, and Sharpe-weighted portfolios
- `price_of_hedging.py` - Optimal weights with hedging cost sensitivity analysis

**Stage 5-6: Performance & Risk Analysis**
- `prof_perf_sign.py` - P&L calculation, hit rates, signal quality metrics
- `regression.py` - Beta/alpha estimation, Information Ratio vs Sharpe Ratio
- `fama_french_3_factor.py` - Multi-factor risk attribution, alpha purification
- `beta_alpha_factor_models.py` - Factor decomposition, correlation analysis

**Stage 7: Optimization**
- `price_of_hedging.py` - Optimal portfolio construction with constraints

### Supporting Scripts
- `fundamental_stock_data.py` - Loading fundamental data (SimFin, Yahoo Finance)

### Notebooks
- `notebooks/wallstreet_quants/Homework3 Solutions.ipynb` - Momentum strategy implementation
- `notebooks/wallstreet_quants/Homework4 Solutions.ipynb` - Beta/alpha factor models
- `notebooks/wallstreet_quants/PythonRisk.ipynb` - Fama-French 3-factor risk analysis

### Key Concepts by File

| File | Primary Concepts | Tools/Libraries |
|------|-----------------|-----------------|
| `prof_perf_sign.py` | P&L, hit rate, signal analysis | NumPy, basic loops |
| `regression.py` | CAPM, beta, alpha, t-stats | sklearn, statsmodels |
| `momentum_returns.py` | Momentum, Sharpe signals, portfolio construction | pandas, yfinance |
| `beta_alpha_factor_models.py` | Factor decomposition, correlations, IR vs SR | pandas rolling, correlations |
| `portfolio_weighting.py` | Mean-variance optimization, risk parity, position sizing | NumPy linear algebra |
| `price_of_hedging.py` | Optimal weights, hedging costs, sensitivity analysis | NumPy optimization |
| `turnover.py` | Transaction costs, turnover, gross vs net returns | Binance API, pandas |
| `fama_french_3_factor.py` | Multi-factor models, risk attribution, neutralization | statsmodels OLS |
| `unconstrained_backtest_SP500.py` | Cross-sectional strategies, rank-based portfolios | pandas rank, Wikipedia scraping |

---

## Goal

Build fluency with the quant workflow and the tools required to execute it. The goal is not to build successful trading strategies. It is to internalize a way of thinking: **story → pipeline → SR gate → out-of-sample check → purification → t-stat gate**. By the end of two weeks, this sequence should feel like a reflex, not a checklist.

Constraints:
- Follow deliberate practice: repetition, task variety, immediate feedback, progressive difficulty
- Focus on load-bearing concepts first
- 2 weeks, 2 hours/day
- Stages 1-7 of the workflow (paper/live trading excluded)

## Quant Workflow

1. Start with a Signal Idea
2. Unconstrained Backtest
3. Extend Across Securities (Breadth)
4. Weighting and Portfolio Construction
5. Performance Evaluation Beyond Sharpe
6. Risk Factor Analysis and Alpha Purification
7. Optimized Backtest
8. Paper Trading
9. Live Trading and Scaling

---

## Standing Rules (Apply Every Day)

These rules are non-negotiable throughout the plan. Internalize them as habits:

1. **Story first**: Before writing any code, write one sentence — what you believe is true about markets and why it should predict returns. No hypothesis, no signal.

2. **Name the strategy type**: Before coding, state whether the strategy is **cross-sectional** (ranks assets relative to each other, always long/short, market-neutral) or **time-series** (trades each asset based on its own past, may be net long or short). These are fundamentally different structures.

3. **Train/validate split**: From Day 2 onward, always split data before doing any parameter work. Convention used in this plan: **2016–2021 = training, 2022–2024 = validation**. Iterate only on training data. Check validation once, at the end — not during iteration.

4. **The canonical pipeline**: Every unconstrained backtest follows this exact sequence. Memorize it:
   ```
   signal → rank (cross-sectional) or threshold (time-series) → demean → normalize → shift → returns → evaluate
   ```

5. **Sharpe gate**: A gross Sharpe below 1.0 on training data means the signal isn't there. Stop, change the signal. Do not tune parameters to push a weak signal over the gate — that is overfitting.

6. **Always compute drawdown**: Every perf eval includes max drawdown and recovery time, not just Sharpe. A strategy with SR=1.5 and 60% max drawdown is not the same as one with SR=1.5 and 12% drawdown.

   ```python
   cumulative = strat_ret.cumsum()
   drawdown = cumulative - cumulative.cummax()
   max_dd = drawdown.min()
   ```

---

## Key Concepts Reference

These are the concepts the plan builds toward. Return to this list to test yourself.

**Fundamental Law of Active Management**
```
SR_portfolio = SR_per_bet × √N
```
N = number of independent bets. Extending a strategy to more uncorrelated assets is almost always worth it. Check that the improvement in SR approximates √N as you add assets.

**Correlation thresholds for breadth**
- 0.0–0.25 between strategies: acceptable, genuine breadth
- > 0.25: diminishing returns, bets are not independent
- Negative: best case, diversification multiplier

**Look-ahead bias**: Using information at time *t* that wasn't available until *t+1*. The canonical fix is `.shift()` on portfolio weights before multiplying by returns. If you forget it, your backtest will be unrealistically good. Always verify with a deliberate test: run without `.shift()`, confirm Sharpe inflates, put `.shift()` back.

**Research pitfalls**:
- *Overfitting*: tuning parameters until the backtest looks good. Fix: out-of-sample split + smooth parameter surface (Sharpe shouldn't spike at one specific parameter value).
- *Over-modeling*: adding complexity when the signal isn't there. The noise-to-signal ratio in financial data is very high. Simple signals that work are more trustworthy than complex models that barely work.

**Alpha t-stat gate**: An alpha t-stat below 2.0 means the excess return is statistically indistinguishable from noise. This is the Week 2 equivalent of the SR gate.

---

## Study Plan

### Overview

**Total Time**: 2 weeks × 7 days × 2 hours = 28 hours
**Focus**: Workflow stages 1-7 (paper/live trading excluded)
**Approach**: Deliberate practice with increasing complexity

---

### Week 1: Foundations (Workflow Stages 1-4)

**Theme**: Build muscle memory for the workflow. By the end of this week you should be able to go from signal idea → unconstrained backtest → weighted portfolio → net-of-cost Sharpe without looking anything up.

---

#### Day 1: P&L, Hit Rate, and Signal Quality (2 hrs)

**Concept focus**: What a signal is. What makes a signal have value. The spread between positive and negative signal regimes is the first test of whether a signal predicts returns.

**Study** (40 min): Read and run `prof_perf_sign.py` completely.
- Trace the logic of `analyze_signal`: what does the spread mean? When is it zero? When is it meaningful?
- Note: this script uses random data. The spread will be near zero. That is the point — a random signal has no predictive value.

**Practice** (80 min):

- **Exercise 1 — Look-ahead bias demonstration**: Replace the random `signal` with `rets` itself — use the same period's return as the signal. Run `analyze_signal(rets, rets)`. The spread will be very large and positive. This simulates the most common form of look-ahead bias: your signal accidentally incorporates the return you're trying to predict (e.g., computing a signal from end-of-day prices and using it to trade at that same end-of-day price). Now restore the independent random signal — spread collapses back to near zero. The gap between the two spreads is how much a biased backtest inflates results. In the DataFrame-based exercises that follow, `.shift()` on portfolio weights is what enforces this boundary — signals formed at time *t* can only be applied to returns at time *t+1*.

- **Exercise 2 — Real signal**: Replace the random signal with `ret[idx-1]` (yesterday's return as the signal). State your hypothesis first: *"I believe yesterday's return predicts today's return because..."*. Is this a momentum or reversal hypothesis? Compute the spread. Does the signal have value?

- **Exercise 3 — Drawdown**: Simulate a P&L series by summing returns when `signal[idx] > 1`. Add `compute_stats` to also return `max_drawdown` and the longest run of negative returns (drawdown duration). Compare two signal variants: which has a higher hit rate but worse drawdown?

**Deliverable**: Working script with a clear answer to: *does yesterday's return predict today's return?* Include the spread, hit rate, and max drawdown for each signal variant.

---

#### Day 2: Time-Series Momentum (2 hrs)

**Concept focus**: Time-series strategy structure. The canonical pipeline for the first time. Training/validation discipline.

**Before coding**: Write your hypothesis for rolling Sharpe momentum. Why should an asset that has had a high risk-adjusted return over the past year continue to perform well?

**Study** (40 min): Read and run `momentum_returns.py`.
- Identify where the canonical pipeline steps appear: signal (`compute_momentum`) → threshold (Sharpe > 1) → normalize (`div`) → shift → returns.
- Confirm this is a **time-series** strategy: each asset is traded based on its own past, not relative to other assets.

**Practice** (80 min):

- **Exercise 1 — Pipeline from memory**: Close the script. On a new file, implement the same strategy on `['SPY', 'TLT', 'GLD', 'BTC-USD']` without looking at `momentum_returns.py`. Write each step explicitly: signal → threshold → normalize → shift → returns. Check your output against the script.

- **Exercise 2 — Training/validation split**: Apply the split (train: 2016–2021, validate: 2022–2024). Run all parameter iteration on training only. Record training Sharpe and drawdown. At the very end, run on validation. Does it hold up?

- **Exercise 3 — Fundamental Law preview**: Your universe has 4 assets. Using the Fundamental Law formula (`SR_portfolio = SR_per_bet × √N`), estimate what Sharpe you'd expect if each asset individually had the same SR. Compare to the actual portfolio SR. Does diversification across 4 assets deliver the expected lift?

- **Exercise 4 — Parameter range**: On training data only, vary the Sharpe threshold from 0.25 to 2.0 in steps of 0.25. Plot SR vs threshold. Look for a smooth surface — if SR spikes only at one value, be skeptical. Pick a threshold that sits in a flat region.

**Deliverable**: Momentum strategy with train/validate split. Report training SR, training max drawdown, and validation SR. Note whether the SR held up out of sample. Include a plot of the **drawdown time series** (not just the minimum — the full curve of `cumulative - cumulative.cummax()` over time). This plot shows you *when* and *how long* the strategy was underwater, not just how bad the worst moment was. Also report the longest drawdown duration: the maximum number of consecutive days spent below the prior peak.

---

#### Day 3: Cross-Sectional Mean Reversion (2 hrs)

**Concept focus**: Cross-sectional strategy structure. Contrasting it with time-series. The rank-demean-normalize pipeline. Look-ahead bias via `.shift()`.

**Before coding**: Write your hypothesis for 1-day mean reversion. Why would a stock that falls sharply today bounce back tomorrow? What market mechanism causes this? This is a **cross-sectional** strategy — classify it before you start.

**Study** (30 min): Read `unconstrained_backtest_SP500.py`.
- Identify the pipeline: negate → rank → demean → normalize → shift → returns. This is the cross-sectional version of the canonical pipeline.
- Why does it demean? Because after demeaning, the sum of weights is zero — the portfolio is market-neutral by construction. That is the structural difference from a time-series strategy.

**Practice** (90 min):

- **Exercise 1 — Pipeline from memory, small universe**: On a new file, implement the rank-demean-normalize pipeline on `['SPY', 'QQQ', 'IWM', 'EEM', 'TLT', 'GLD']`. Do not look at the script. Write each step explicitly. Verify market neutrality: `port.sum(1)` should be near zero at every date.

- **Exercise 2 — Look-ahead bias test**: Run the strategy *without* `.shift()` (use current weights against current returns). Record the SR. Then add `.shift()` back. Record the SR. Compare. The gap is how much your backtest was cheating. This is the canonical demonstration of look-ahead bias.

- **Exercise 3 — Cross-sectional vs. time-series**:  Take the same 6-asset universe. Build both a cross-sectional mean-reversion strategy (rank-based, today's losers → long) and a time-series momentum strategy (rolling Sharpe threshold). Calculate the correlation between the two strategy return series. Are they independent bets? What does this suggest about combining them?

- **Exercise 4 — Fundamental Law**: Implement the mean-reversion strategy on 2, 4, and 6 assets. Record the SR for each. Does it scale approximately with √N? Plot SR vs. N to visualize the relationship.

**Deliverable**: Cross-sectional mean-reversion on 6 assets. Report SR and max drawdown. Include the look-ahead bias comparison table and the correlation between the cross-sectional and time-series strategies.

---

#### Day 4: Portfolio Weighting Schemes (2 hrs)

**Concept focus**: Why weighting matters. The hierarchy: equal weight → equal vol → Sharpe optimal (Σ⁻¹μ). Correlation thresholds. The Fundamental Law in the context of weighting.

**Study** (50 min): Read and run `portfolio_weighting.py`.
- This script works in **strategy space** (3 pre-built strategies A, B, C), not stock space. Note why: in strategy space, historical returns are a reasonable estimate of μ and historical covariance is a reasonable estimate of Σ. In stock space, historical returns tell you almost nothing about future stock returns.
- Trace why optimal beats equal-vol: it accounts for correlations between strategies. Equal-vol ignores them.
- Note that optimal weights allow negative values (short positions). Normalization is by `np.abs(wgt).sum()`, not `wgt.sum()`.

**Practice** (70 min):

- **Exercise 1 — Apply all 3 schemes to real data**: Take your Day 2 momentum strategy returns and Day 3 mean-reversion returns as two strategies in strategy space. Compute optimal, equal-vol, and Sharpe-ratio weights between them. Which scheme gives the highest combined SR?

- **Exercise 2 — Correlation check**: Before weighting, compute the correlation between your two strategy return series. Is it below 0.25? If it's above 0.25, the two strategies are not genuinely independent bets and the Fundamental Law's gains will be smaller than predicted. Report the correlation alongside the combined SR.

- **Exercise 3 — Fundamental Law verification**: Using the combined portfolio SR from Exercise 1, compare to what the Fundamental Law predicts given the per-strategy SR and correlation. Use the Law of Diversification formula: `SR_portfolio = SR_per_bet / √((1 + corr) / 2)`. How close is the actual to the predicted?

- **Exercise 4 — Leverage invariance**: Multiply the optimal weights by 3 (3x leverage). Confirm that SR doesn't change. Confirm that returns and volatility both scale by 3. Now confirm that max drawdown *also* scales by 3 — a 3x levered strategy suffers 3x larger drawdowns in return space. Compute the **Calmar ratio** (annualized return / |max drawdown|) before and after leverage. It should be invariant to leverage, just like SR. This is why both SR and Calmar are the right metrics for comparing strategies across leverage levels.

**Deliverable**: Comparison table of weighting schemes on your 2-strategy combination. Report SR, vol, max drawdown, and Calmar ratio for each weighting scheme, plus the inter-strategy correlation.

---

#### Day 5: Transaction Costs Reality Check (2 hrs)

**Concept focus**: Gross vs. net Sharpe. Turnover as a cost multiplier. The breakeven analysis. Signal smoothing as a lever.

**Study** (40 min): Read and run `turnover.py`.
- Understand the two-step cost formula: `net_ret = gross_ret - turnover × cost_bps × 1e-4`.
- Note that turnover is a function of how much the *weights* change day to day, not how much prices move.

**Practice** (80 min):

- **Exercise 1 — Turnover on your Day 3 strategy**: Calculate turnover for your cross-sectional mean-reversion strategy. This is a high-turnover strategy by nature (rebalances daily). Calculate net SR at 10bps, 20bps, and 50bps.

- **Exercise 2 — Breakeven analysis**: For your mean-reversion strategy, plot net SR vs. cost assumption from 1bps to 100bps. Find the breakeven cost (where net SR hits zero). Is the strategy viable at realistic equity trading costs (~5-10bps)?

- **Exercise 3 — Signal smoothing**: High turnover comes from a signal that changes rapidly day to day. Smooth the signal with a 3-day rolling average before ranking. Recalculate turnover and net SR. What is the tradeoff: you lose some signal sharpness (gross SR may drop slightly) but gain in cost reduction (net SR may improve). Report the tradeoff explicitly.

- **Exercise 4 — SR gate check**: Using your net SR (after costs), does the strategy still pass the SR > 1.0 gate? If not, what would the signal need to look like to survive real-world costs?

**Deliverable**: Turnover analysis with breakeven cost chart. Gross vs. net SR comparison before and after signal smoothing.

---

#### Day 6: Integration — Build a Complete Strategy (2 hrs)

**No new material.** This is a workflow integration day. The goal is to execute stages 1-4 in sequence, making the SR gate and out-of-sample check explicit decision points.

**Starter universe**: `['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'META', 'NVDA', 'JPM', 'GS', 'SPY', 'TLT']`

**Practice** (120 min):

1. **Write your hypothesis** (1 sentence). Decide: cross-sectional or time-series?
2. **Implement the pipeline from memory**. Do not look at scripts. Write signal → rank/threshold → demean → normalize → shift → returns.
3. **Check look-ahead bias**: verify `.shift()` is in place. Do the deliberate test.
4. **SR gate**: Check gross SR on training data (2016–2021). If SR < 1.0, iterate on the signal. Do not move forward.
5. **Add a second strategy** (if your first is cross-sectional, add a time-series, or vice versa). Check the correlation between them. If corr > 0.25, they are not independent bets.
6. **Weight them** using equal-vol. Calculate combined SR and max drawdown.
7. **Apply costs**: Calculate net SR at 20bps.
8. **Out-of-sample check**: Run on validation data (2022–2024). Report validation SR vs. training SR.

**SR gate rule**: If gross SR < 1.0 at step 4, stop and iterate. If net SR < 0.5, the strategy is unlikely to be viable — identify whether the problem is weak signal or high turnover. Also flag max drawdown > 40%: even a strategy that passes the SR gate is operationally difficult to hold through if it periodically loses 40%+ — especially under leverage.

**Deliverable**: End-to-end documented strategy. Report training SR, training max drawdown, net SR, validation SR. Compare cross-sectional and time-series components and their correlation.

---

#### Day 7: Research Pitfalls and Week 1 Review (2 hrs)

**Concept focus**: Overfitting. Smooth parameter surfaces. Consolidation.

**Review** (30 min): Revisit your Day 2-6 exercises. For each, verify: did you write a hypothesis? Did you enforce the train/validate split? What is the gap between training and validation SR?

**Overfitting demonstration** (60 min):

This is the most important exercise of Week 1.

Using your Day 3 or Day 5 strategy:

1. Grid-search the lookback window across 20 values (e.g., 5, 10, 15, ..., 100 days) on **training data only**.
2. Record the SR for each value. Plot SR vs. lookback. Find the best-performing lookback.
3. Deliberately pick that best value. Lock it in.
4. Now run on **validation data** with that best value.
5. Compare: did validation SR hold up, or did it collapse?

**This is overfitting in your hands.** The best parameter value in the training window is unlikely to be the best going forward. Look at the shape of the SR vs. lookback curve: a smooth, flat region is a trustworthy parameter range. A sharp spike at one value is a fitting artifact.

**Week 1 Challenge** (30 min): Revisit your Day 6 integration strategy. Now that you've seen the overfitting demonstration, do you still trust the parameter choices you made? Check whether your lookback window sat in a smooth region of the SR surface.

**Deliverable**: Grid-search plot (SR vs. lookback, train and validate). A written answer: what is the difference between a trustworthy signal and an overfit signal?

---

### Week 2: Advanced Topics (Workflow Stages 5-7)

**Theme**: Performance evaluation beyond Sharpe. Risk decomposition. Alpha purification. By the end of this week you should be able to look at any strategy's returns and know whether the performance is genuine alpha or just factor exposure you could have gotten cheaper.

---

#### Day 8: Beta and Alpha Decomposition (2 hrs)

**Concept focus**: CAPM regression. Beta contribution vs. alpha contribution. The alpha t-stat gate.

**Study** (50 min): Read and run `regression.py`.
- Trace the decomposition: total return = beta × market return + alpha + residual.
- The Information Ratio is the Sharpe ratio of the *alpha component only*. A high SR but low IR means the returns are coming from market exposure, not skill.
- **The alpha t-stat gate**: an alpha t-stat below 2.0 means you cannot statistically distinguish your alpha from zero. This is the Week 2 SR gate equivalent.

**Practice** (70 min):

- **Exercise 1 — Decompose your Week 1 strategy**: Run the CAPM regression of your Day 6 integration strategy returns against SPY. Report beta, alpha, alpha t-stat, IR. Does the alpha t-stat pass 2.0?

- **Exercise 2 — SR vs. IR vs. Calmar**: If SR > IR, your strategy's performance is partly beta-driven. Calculate what fraction of total return came from beta exposure (`beta × SPY_return`) vs. alpha. Also compute the **Calmar ratio** of both the total strategy and the alpha component separately. It's possible to have a strategy with a good SR but a bad Calmar (deep drawdowns), meaning it looks good risk-adjusted but is hard to hold in practice. Qualitatively: if you could just buy SPY with leverage to match the beta, would you?

- **Exercise 3 — Rolling beta**: Calculate 252-day rolling beta. Does beta change over time? A stable beta means predictable market exposure; an unstable beta means your factor exposure is drifting, which complicates portfolio management.

- **Exercise 4 — Alpha t-stat gate**: Apply the gate: does your strategy pass alpha t-stat ≥ 2.0? If not, the alpha is not statistically real. This doesn't mean the strategy is useless — it may still have valid gross Sharpe — but it cannot be claimed as skill-based alpha.

**Deliverable**: CAPM decomposition table with SR, IR, beta, alpha, alpha t-stat. Written verdict: is the alpha statistically significant?

---

#### Day 9: Multi-Stock Factor Models (2 hrs)

**Concept focus**: Beta as a common factor. How removing beta changes the correlation structure across stocks. Why diversification within a sector doesn't work as expected.

**Study** (40 min): Read `beta_alpha_factor_models.py`.
- The key result is the correlation tables: before and after removing beta, correlations drop dramatically. Most stock-to-stock correlation is driven by shared market exposure, not anything stock-specific.
- IR vs. SR comparison: if IR << SR, the stock's performance is almost entirely from riding the market.

**Practice** (80 min):

- **Exercise 1 — FAANG factor decomposition**: Run the script on `['AAPL', 'MSFT', 'NVDA', 'GOOGL']` vs. `QQQ`. Report original correlations and residual correlations. By how much do correlations drop after removing the QQQ factor?

- **Exercise 2 — Breadth illusion**: Calculate the SR of an equal-weight portfolio of the 4 stocks before removing beta. Then calculate the SR of an equal-weight portfolio of the *residuals* (alpha components). Compare. What does this tell you about whether holding more tech stocks gives you genuine breadth?

- **Exercise 3 — Correlation threshold check**: After removing beta, do the residual correlations fall below 0.25? If so, the stocks have genuine independent alpha. If not, there is some other shared factor driving them (e.g., sector momentum) that isn't captured by QQQ alone.

- **Exercise 4 — Which stock has the highest IR?** This is the stock with the most genuine alpha per unit of idiosyncratic risk. Would you weight it more heavily in an alpha portfolio? How does this connect to the Sharpe-optimal weighting formula?

**Deliverable**: Correlation matrix before and after beta removal. IR vs SR table for each stock. Written answer: do these stocks represent genuine independent bets after accounting for market exposure?

---

#### Day 10: Fama-French 3-Factor Analysis (2 hrs)

**Concept focus**: Multi-factor risk attribution. R-squared and risk contribution. Factor neutralization — extracting pure alpha.

**Study** (50 min): Read and run `fama_french_3_factor.py`.
- Three factors: market (Mkt-RF), size (SMB), value/growth (HML). Each captures a different systematic risk premium.
- R-squared tells you what fraction of returns come from known factors. High R-squared = mostly factor exposure, not stock picking.
- Risk contribution: which factor drives the most portfolio volatility?
- Factor neutralization: subtract factor exposures to isolate pure alpha. If the neutralized SR is much lower than the original SR, the returns were factor-driven.

**Practice** (70 min):

- **Exercise 1 — Predict before running**: Before running the FF3 regression on QQQ and TLT, write your predictions. For QQQ: what sign do you expect for Mkt-RF? SMB (large or small cap tilt)? HML (growth or value tilt)? For TLT: will it even load on equity factors? Run the regressions and check your predictions.

- **Exercise 2 — R-squared decomposition**: What percentage of QQQ's variance is explained by the three factors? What percentage is idiosyncratic? Does QQQ's manager (if you can call index management that) add any alpha beyond factor exposure?

- **Exercise 3 — Factor neutralization on your Day 6 strategy**: Run FF3 regression on your integration strategy returns. Report factor loadings. Calculate the neutralized returns. Compare original SR to neutralized SR. What fraction of your strategy's performance survives factor purification?

- **Exercise 4 — Alpha t-stat gate on neutralized returns**: Does the alpha t-stat on the FF3 residual pass 2.0? If it passed the CAPM gate (Day 8) but fails the FF3 gate, what does that mean? (It means the excess return was factor exposure — size or value tilt — not genuine alpha.)

**Deliverable**: FF3 factor loading table for QQQ and TLT with your pre-run predictions vs. actuals. FF3 analysis of your Week 1 strategy with SR before and after neutralization.

---

#### Day 11: Constrained Optimization (2 hrs)

**Concept focus**: The analytic Σ⁻¹μ formula is the solution to an unconstrained problem. Real trading requires constraints — no short-selling, position limits, turnover limits. `cvxpy` lets you add these without abandoning the optimization framework. The Primer's Stage 7 framing: the optimizer's job is to *minimize tracking error to ideal signal weights subject to real-world constraints*, not to maximize raw returns.

**Study** (30 min): Read `price_of_hedging.py`.
- This is the unconstrained baseline. Σ⁻¹μ finds the exact maximum-Sharpe weights when there are no constraints.
- Note the sensitivity analysis: as hedge returns vary, the optimal weights shift continuously. This is what optimization gives you — a principled way to handle tradeoffs.
- The limitation: Σ⁻¹μ allows unlimited short positions and ignores turnover costs. In practice neither is acceptable.

**Optimization concept** (20 min reading before exercises):

The unconstrained problem:
```
maximize  w'μ / sqrt(w'Σw)
→ equivalent to: minimize w'Σw  subject to  w'μ = 1
→ closed-form solution: w = Σ⁻¹μ
```

The constrained problem (what you actually solve in production):
```python
import cvxpy as cp

w = cp.Variable(n)
objective = cp.Minimize(cp.quad_form(w, sigma))   # minimize portfolio variance
constraints = [
    cp.sum(w) == 1,       # fully invested
    w >= 0,               # long-only
    w <= 0.30,            # no more than 30% in any asset
]
prob = cp.Problem(objective, constraints)
prob.solve()
```

**Practice** (70 min):

- **Exercise 1 — Verify cvxpy matches Σ⁻¹μ (unconstrained)**: Use your Day 6 strategy returns. Solve the unconstrained minimum-variance problem with cvxpy (no constraints except `sum(w) = 1`, allow negatives). Confirm the weights match `np.linalg.inv(sigma) @ mu` (normalized). This is the sanity check that the optimizer is working correctly before you add constraints.

- **Exercise 2 — Add long-only constraint**: Add `w >= 0` to the problem. How do the weights change? Which strategies get zeroed out? Does SR drop? The gap between constrained SR and unconstrained SR is the cost of the long-only constraint — what you pay for not being allowed to short.

- **Exercise 3 — Add position limits**: Add `w <= 0.30` (max 30% per asset). How does this affect the most concentrated positions from Exercise 2? Report SR and max drawdown with and without the constraint. Position limits typically cost less than the long-only constraint but improve drawdown behavior.

- **Exercise 4 — Tracking error formulation**: This is the Stage 7 framing. Given your ideal signal weights `w_ideal` (from the unconstrained backtest), find the closest feasible portfolio subject to constraints:
  ```python
  w = cp.Variable(n)
  objective = cp.Minimize(cp.sum_squares(w - w_ideal))  # minimize distance to ideal
  constraints = [cp.sum(w) == 1, w >= 0, w <= 0.30]
  ```
  Compare this portfolio to the raw signal weights. How much does enforcing constraints force you to deviate from your ideal? Report the net SR — this is closer to what you'd actually achieve in live trading.

**Deliverable**: Table comparing unconstrained vs. long-only vs. position-limited portfolios on SR, max drawdown, and Calmar ratio. Written answer: what is the cost (in SR terms) of each constraint you added, and is it worth paying?

---

#### Day 12: Risk Attribution Deep Dive (2 hrs)

**Concept focus**: Complete risk decomposition. Stress testing. Connecting factor exposure to portfolio risk.

**Study** (20 min): Review risk contribution and stress testing sections of `fama_french_3_factor.py`.

**Practice** (100 min):

Apply to your Day 6 integration strategy (the most complete strategy you've built):

- **Exercise 1 — Factor risk attribution**: What percentage of total portfolio volatility comes from the market factor? Size factor? Value factor? Idiosyncratic risk? Use `risk_contr = X.multiply(res.params).std() / ret.std()` from the FF3 script.

- **Exercise 2 — 5-sigma stress test**: For each factor, calculate the impact of an extreme (5 standard deviation) move. If the market dropped 7% in a day (which has happened), what would your portfolio's single-day loss be? Does this stress loss feel acceptable given your position size?

- **Exercise 3 — Factor-neutral SR and Calmar**: Calculate your strategy's SR after full FF3 neutralization. Compare: original SR → CAPM-purified SR → FF3-purified SR. Do the same for Calmar ratio at each step. A strategy can lose SR after purification but improve its Calmar (the factor exposure was causing large correlated drawdowns). If FF3-purified SR is still high, you have genuine multi-factor-adjusted alpha.

- **Exercise 4 — The full verdict**: Apply both gates. Does the strategy pass SR > 1.0 (gross, in-sample)? Does it pass alpha t-stat ≥ 2.0 after FF3 purification? Does it survive out-of-sample? Is the stress loss acceptable? Write up the verdict as if presenting to a portfolio manager.

**Deliverable**: Complete risk attribution table. Stress test results. Written verdict with gate results.

---

#### Day 13: Integration — Optimized Strategy Build (2 hrs)

**No new material.** Execute the full workflow — stages 1 through 7 — in sequence. Every gate must be checked explicitly before moving to the next stage.

**Practice** (120 min):

1. **Hypothesis** (written): What is the story? Cross-sectional or time-series?
2. **Stage 2 — Unconstrained backtest**: Pipeline from memory. SR gate on training data (SR < 1.0 = stop).
3. **Stage 3 — Breadth**: Add assets. Check correlation between components (corr > 0.25 = flag as redundant). Verify SR improvement approximates √N.
4. **Stage 4 — Weighting**: Apply equal-vol weighting. If two components have corr < 0.25, the combination genuinely improves SR. If not, one is redundant.
5. **Stage 5 — Performance beyond Sharpe**: Report max drawdown, IR, alpha t-stat (CAPM). t-stat < 2.0 = alpha is not statistically real.
6. **Stage 6 — Factor purification**: Run FF3. Report factor loadings and neutralized SR. Alpha t-stat < 2.0 on FF3 residual = factor exposure, not alpha.
7. **Stage 7 — Costs**: Apply 20bps. Report net SR. Signal smooth if needed.
8. **Out-of-sample check**: Run on validation data (2022–2024). If validation SR < 50% of training SR, the strategy may be overfit — inspect the parameter surface.

**Deliverable**: Strategy with documented gate results at each stage. Where did the strategy fail a gate, and what did you do about it?

---

#### Day 14: Final Project and Review (2 hrs)

Build a complete, documented strategy. The structure of the deliverable mirrors the full workflow — each section is a stage, and each stage reports whether the gate was passed.

**Final Project** (120 min):

```
1. Hypothesis and strategy type
   - Story (1-2 sentences)
   - Cross-sectional or time-series? Why?

2. Unconstrained backtest
   - Pipeline steps (written out explicitly)
   - Training SR and drawdown
   - SR gate: pass or fail?

3. Breadth
   - How many assets? What is the correlation between components?
   - Actual SR improvement vs. Fundamental Law prediction

4. Weighting
   - Scheme chosen and why
   - Combined SR and drawdown

5. Performance beyond Sharpe
   - SR, max drawdown, IR, hit rate
   - CAPM alpha t-stat (gate: ≥ 2.0?)

6. Risk factor analysis
   - FF3 factor loadings
   - Neutralized SR
   - FF3 alpha t-stat (gate: ≥ 2.0?)

7. Costs
   - Turnover, gross SR, net SR at 20bps

8. Out-of-sample
   - Validation SR vs. training SR
   - Parameter surface: smooth or spiky?

9. Verdict
   - Overall: does this strategy pass all gates?
   - What would you need to improve to take it further?
```

---

### Deliberate Practice Principles Applied

**Repetition**: The canonical pipeline is re-implemented from memory on each new dataset starting Day 2. By Day 14 it should be automatic.

**Task Variety**: Different signal types (momentum, mean-reversion), universes (ETFs, stocks, crypto), and structures (time-series vs. cross-sectional). The evaluation framework stays constant — what changes is what you're evaluating.

**Immediate Feedback**: Every exercise produces a number. SR, drawdown, t-stat, correlation. These are not subjective — a strategy either passes the gate or it doesn't.

**Progressive Difficulty**:
- Week 1: Basic workflow with one signal at a time
- Days 8-10: Add factor decomposition on top of Week 1 strategies
- Days 11-12: Optimization and full risk attribution
- Day 13-14: Full workflow executed end-to-end from memory

---

### Success Metrics

After 2 weeks, you should be able to:

**Workflow**:
- [ ] Given a market observation, articulate a testable hypothesis (story first)
- [ ] Identify whether a strategy is cross-sectional or time-series and explain the structural difference
- [ ] Implement the full unconstrained backtest pipeline from memory, without looking at scripts
- [ ] Apply a train/validate split without being reminded
- [ ] Know when to stop iterating on a signal (SR gate)

**Concepts**:
- [ ] Demonstrate look-ahead bias and fix it with `.shift()`
- [ ] Calculate drawdown and interpret it alongside Sharpe
- [ ] Compute the Fundamental Law prediction and compare to actual SR improvement
- [ ] Check inter-strategy correlation and know whether breadth is genuine
- [ ] Decompose returns into beta and alpha components
- [ ] Run a Fama-French regression and interpret factor loadings
- [ ] Calculate the neutralized SR and compare to total SR
- [ ] Apply both gates: SR ≥ 1.0 (gross) and alpha t-stat ≥ 2.0

**Research discipline**:
- [ ] Perform a grid search, plot the parameter surface, and identify overfitting
- [ ] Know the difference between a trustworthy parameter choice and one that was tuned to the data
- [ ] Report validation SR alongside training SR in every final evaluation

---

### Tools Mastery Checklist

**Pandas**:
- [ ] Rolling calculations (`.rolling()`)
- [ ] Rank operations (`.rank()`)
- [ ] Cross-sectional operations (`.subtract()`, `.divide()` with axis)
- [ ] Correlation matrices (`.corr()`, `.corrwith()`)
- [ ] Date indexing and resampling
- [ ] `.shift()` and when it is mandatory

**Stats/Regression**:
- [ ] OLS regression (statsmodels)
- [ ] Beta and alpha calculation
- [ ] T-statistic interpretation and the 2.0 threshold
- [ ] R-squared and risk contribution

**Portfolio math**:
- [ ] Mean-variance optimal weights (`np.linalg.inv(sigma) @ mu`)
- [ ] Equal-vol weights
- [ ] Turnover calculation
- [ ] Drawdown time series (`cumulative - cumulative.cummax()`)
- [ ] Max drawdown and longest drawdown duration
- [ ] Calmar ratio (`annualized return / |max drawdown|`)

**Data Sources**:
- [ ] yfinance for stocks/ETFs
- [ ] Binance API for crypto
- [ ] Fama-French data library

---

### After 2 Weeks

**Next Steps**:
- Build 10 more strategies using the full workflow, applying every gate
- Read academic papers and implement their strategies — use the hypothesis-first discipline to predict what the paper will find before reading the results
- Begin using an optimizer (e.g., `cvxpy`) to implement the Stage 7 optimized backtest with real constraints

---

## Quick Reference: Key Formulas

**Portfolio Return** (core mechanic of every backtest):
```python
strat_ret = (weights.shift() * returns).sum(axis=1)
# shift() uses yesterday's weights — mandatory to avoid look-ahead bias
```

**Canonical Pipeline** (cross-sectional):
```python
signal = -1 * ret.rolling(hor).mean()       # e.g. negate for mean-reversion
ranked = signal.rank(axis=1)                 # rank cross-sectionally each day
demeaned = ranked.subtract(ranked.mean(1), axis=0)   # market-neutral: weights sum to 0
port = demeaned.divide(demeaned.abs().sum(1), axis=0) # normalize: |weights| sum to 1
strat_ret = (port.shift() * ret).sum(1)      # shift then apply
```

**Annualized Return and Volatility**:
```python
ann_return = returns.mean() * 252
ann_vol    = returns.std() * np.sqrt(252)
```

**Sharpe Ratio (Annualized)**:
```python
sharpe = returns.mean() / returns.std() * np.sqrt(252)
```

**Beta (CAPM)**:
```python
beta = returns.cov(market_returns) / market_returns.var()
# rolling version:
beta = returns.rolling(252).corr(market) * returns.rolling(252).std() / market.rolling(252).std()
```

**Alpha Extraction**:
```python
alpha = returns - beta * market_returns   # residual after removing market exposure
# constant alpha (from regression intercept) + time-varying residual
```

**Information Ratio**:
```python
IR = alpha.mean() / alpha.std() * np.sqrt(252)
```

**R-Squared** (fraction of variance explained by factors):
```python
r_sq = model.predict(X).var() / returns.var()
# or from statsmodels: res.rsquared
```

**Risk Contribution** (fraction of total vol from each factor):
```python
risk_contr = X.multiply(res.params).std()[factors] / returns.std()
# sum of risk contributions ≈ R-squared
```

**Equal-Vol Weights**:
```python
vols = returns.std()
weights = 1 / vols
weights = weights / weights.abs().sum()   # normalize
```

**Sharpe-Optimal Weights (Mean-Variance)**:
```python
weights = np.linalg.inv(cov_matrix) @ mean_returns
weights = weights / np.abs(weights).sum()  # normalize — allows short positions
```

**Turnover**:
```python
turnover = (weights - weights.shift()).abs().sum(axis=1)
```

**Transaction Cost Drag**:
```python
cost_drag = turnover * cost_bps * 1e-4
net_returns = gross_returns - cost_drag
```

**Max Drawdown**:
```python
cumulative = returns.cumsum()
drawdown = cumulative - cumulative.cummax()
max_drawdown = drawdown.min()
```

**Drawdown Duration** (longest consecutive days below prior peak):
```python
in_drawdown = (drawdown < 0).astype(int)
# count consecutive 1s — longest run is the max drawdown duration
duration = in_drawdown.groupby((in_drawdown != in_drawdown.shift()).cumsum()).cumsum()
max_duration = duration.max()
```

**Calmar Ratio**:
```python
calmar = (returns.mean() * 252) / abs(drawdown.min())
```

**Fundamental Law of Active Management**:
```python
SR_portfolio = SR_per_bet * np.sqrt(N)  # N = number of independent bets
```

**Law of Diversification** (two assets with equal SR and vol):
```python
SR_portfolio = SR_per_bet / np.sqrt((1 + corr) / 2)
```

---

## Strategies to Implement After 2 Weeks

These are drawn from the papers and examples in the lecture notes. Each one is a full workflow exercise: hypothesis → pipeline → backtest → breadth → weighting → costs → factor purification. Work through each using the same gates and discipline built in the 2-week plan.

### Momentum

- **UMD (Up Minus Down)** — Jegadeesh & Titman (1993). Buy stocks with the highest returns over the past 12 months, short those with the lowest, but skip the most recent month's return to avoid short-term reversal contamination. The canonical academic momentum strategy. *Paper: "Returns to Buying Winners and Selling Losers"*

- **Time Series Momentum** — Moskowitz, Ooi & Pedersen. For each asset, go long if its own past 12-month return is positive, short if negative. Unlike UMD this is a time-series strategy, not cross-sectional. *Paper: "Time Series Momentum"*

- **Industry Momentum** — Moskowitz & Grinblatt. Rank industries (not individual stocks) by past returns and go long/short at the industry level. Individual stock momentum largely disappears once industry momentum is controlled for. *Paper: "Do Industries Explain Momentum?"*

- **Style Momentum** — Chen & de Bondt. Buy stocks whose characteristics (market cap, B/M, dividend yield) are currently in favor (i.e., those characteristics have done well recently). *Paper: "Style momentum within the S&P 500"*

- **Tactical Asset Allocation** — Faber. Time-series momentum applied to asset class ETFs (equities, bonds, commodities, real estate). Go long an asset class only when it is above its 10-month moving average. *Paper: "A Quantitative Approach to Tactical Asset Allocation"*

### Short-Term Momentum (Activity-Based)

- **Post-Earnings Announcement Drift (PEAD)** — trade in the direction of the earnings surprise (actual minus consensus estimate) for days or weeks after the announcement. *Paper: "Earnings Announcements are Full of Surprises" — Brandt, Kishore, Santa-Clara, Venkatachalam*

- **Post Forecast-Revision Drift (PFRD)** — prices continue to drift in the direction of analyst forecast revisions for about six months. Go long stocks with upward revisions, short those with downward revisions. *Paper: "Common Stock Returns Surrounding Earnings Forecast Revisions" — Stickel*

- **Short-Term Momentum on High Volume** — stocks with high recent volume exhibit short-term momentum. Volume is a proxy for high-activity stocks. *Paper: "Short-term Momentum" — Medhat & Schmeling*

### Seasonality

- **Time of Day Effect** — high returns in a given 30-minute interval today predict outperformance in the same 30-minute interval on subsequent days. Autocorrelated institutional flows drive this. *Paper: "Are you trading predictably?" — Heston, Korajczyk, Sadka, Thorson*

- **Time of Year Effect** — high returns in a given calendar month predict outperformance in the same month in future years. *Paper: "Return Seasonalities" — Keloharju, Linnainmaa, Nyberg*

- **Friday Earnings** — next-day stock reaction to Friday earnings surprises is ~60% lower than for non-Friday announcements. Trade the underreaction. *Paper: "Strategic Release of Information on Friday" — DellaVigna & Pollet*

- **Option Expiration Clustering** — stock prices cluster around levels that maximize pain to option buyers before expiration. *Paper: "Stock Price Clustering on Option Expiration Dates" — Ni et al.*

### Event-Driven

- **Index Rebalance / S&P 500 Additions** — buy stocks announced for S&P 500 addition before the effective date; short those announced for removal. The intraday breakdown has a specific pattern worth studying. *Paper: "The S&P 500 Index Effect in Continuous Time" — Kappou et al.*

- **Merger Arbitrage** — after a merger is announced, buy the target and short the acquirer. Hold until deal closes, earning the spread. Risk: deal breaks and the spread reverses.

- **Intraday Market Momentum** — the return in the last 30 minutes before market close is predicted by the return during the rest of the day. Driven by gamma hedging from market makers and leveraged ETF rebalancing. *Paper: "Market Intraday Momentum" — Gao, Han, Li, Zhou*

### Reversal

- **Short-Term Reversal (equity)** — the cross-sectional version from `unconstrained_backtest_SP500.py` extended to the full S&P 500 over multiple years and time periods. Test robustness across market regimes (2008, 2020 Covid, 2022 rate shock).

- **Reversal vs. Momentum Horizon (crypto)** — implement `crypto_reversal_momentum.py` logic on equities. At what lookback horizon does reversal flip to momentum? Does the horizon differ by asset class?

- **Pairs Trading** — find two historically correlated stocks (e.g., Coke vs Pepsi, Goldman vs Morgan Stanley). When the spread between them diverges beyond a threshold, short the outperformer and long the underperformer. This is a time-series cross-sectional combination strategy.

### Value

- **Book-to-Price (B/P)** — rank S&P 500 stocks by book value of common equity divided by market cap. Go long high B/P (cheap), short low B/P (expensive). The classic Fama-French value factor.

- **Earnings Yield (E/P)** — rank by trailing 12-month earnings divided by market cap. Less susceptible to manipulation than book value.

- **EBITDA/EV** — rank by EBITDA divided by enterprise value (market cap + debt - cash). EV accounts for leverage, making it a fairer comparison across companies with different capital structures.

- **Gross Profit/EV** — Novy-Marx value metric. Less susceptible to manipulation than EBIT-based metrics.

### Crypto-Specific

- **Channel Breakout (CBR)** — go long when current high exceeds the past Y-day highest high; exit when low drops below the past X-day lowest low (X < Y). Short the mirror image. Grid-search Y and X; look for flat SR surfaces, not spikes.

- **Moving Average Crossover** — short-horizon EMA crosses above long-horizon EMA → long signal. Normalize by rolling volatility. *Paper: "Momentum and Trend Following Trading Strategies for Currencies Revisited" — Rohrbach*

- **Crypto Carry** — in futures markets, the basis (futures price minus spot price) is a carry signal. Coins with positive basis (futures trade at a premium) are in contango — short carry. Coins with negative basis are in backwardation — long carry.

- **Weekend Retail Effect** — crypto trades 24/7, but institutions mostly trade during business hours. Retail-dominated weekend flow may have different momentum/reversal characteristics than weekday institutional flow. Test whether weekend returns predict weekday returns or vice versa.
