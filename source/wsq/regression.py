"""
Linear Regression for Beta and Alpha Estimation

This script demonstrates how to use regression analysis to decompose stock returns into:
1. Beta (systematic risk/market exposure)
2. Alpha (excess return/manager skill)

Key Financial Model: CAPM (Capital Asset Pricing Model)
    R_stock = α + β × R_market + ε

Where:
    - R_stock: Return of the stock (dependent variable)
    - R_market: Return of market benchmark (independent variable)
    - β (beta): Sensitivity to market movements (slope)
    - α (alpha): Excess return beyond what beta explains (intercept)
    - ε (epsilon): Residual/idiosyncratic risk (unexplained variation)

This is the same concept as Homework 4, but implemented with sklearn instead of manual formulas.
"""

import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.linear_model import LinearRegression


def compute_ols_tvalues(X: np.ndarray, y: np.ndarray, beta: np.ndarray) -> np.ndarray:
    """
    Compute OLS t-values for regression coefficients to test statistical significance.

    Args:
        X: Design matrix (n_obs × n_params) - MUST include intercept column
        y: Dependent variable vector (n_obs,)
        beta: Coefficient estimates (n_params,) - [intercept, slope, ...]

    Returns:
        np.ndarray: T-values for each coefficient (t = coefficient / std_error)

    Statistical Context:
        T-values test the null hypothesis that a coefficient is zero:
        - |t| > 2: Roughly significant at 5% level (rule of thumb)
        - |t| > 3: Highly significant
        - |t| < 2: Not significantly different from zero

        In finance:
        - T-value of alpha: Is excess return statistically significant (skill vs luck)?
        - T-value of beta: Is market exposure significant (almost always is)?

    Mathematical Steps:
        1. Compute predictions: ŷ = X @ β
        2. Calculate residuals: ε = y - ŷ
        3. Residual sum of squares: RSS = εᵀε
        4. Estimate variance: σ² = RSS / (n - k)  [degrees of freedom adjustment]
        5. Coefficient variance matrix: Var(β) = σ² × (XᵀX)⁻¹
        6. Standard errors: SE(β) = sqrt(diag(Var(β)))
        7. T-values: t = β / SE(β)
    """
    n_obs, n_params = X.shape

    # Predicted values from the model
    y_hat = X @ beta

    # Residuals (unexplained returns)
    resid = y - y_hat

    # Residual sum of squares (total unexplained variance)
    rss = float(resid.T @ resid)

    # Degrees of freedom = observations - parameters estimated
    dof = n_obs - n_params

    # Estimate residual variance (σ²)
    # This is an unbiased estimator of the error variance
    sigma2 = rss / dof

    # Inverse of X'X matrix (needed for coefficient variance)
    # (X'X)⁻¹ captures how the design matrix affects coefficient uncertainty
    xtx_inv = np.linalg.inv(X.T @ X)

    # Variance-covariance matrix of coefficient estimates
    var_beta = sigma2 * xtx_inv

    # Standard errors: square root of diagonal elements (variance of each coefficient)
    se_beta = np.sqrt(np.diag(var_beta))

    # T-statistic: coefficient divided by its standard error
    return beta / se_beta


def main() -> None:
    """
    Perform regression analysis to decompose META returns into alpha and beta components.

    Analysis Steps:
        1. Download price data for META (stock) and SPY (market benchmark)
        2. Calculate daily returns
        3. Run regression: META_return = α + β × SPY_return + ε
        4. Compute statistical significance (t-values)
        5. Decompose returns into beta component and alpha component
        6. Analyze alpha quality (mean, IR, correlation with market)
    """
    # ==============================================================================
    # PART 1: Data Download and Preparation
    # ==============================================================================

    # Download price data
    # SPY: S&P 500 ETF (market benchmark)
    # META: Meta/Facebook stock (what we're analyzing)
    univ = ["SPY", "META"]
    px = yf.download(univ, start="2016-01-01")["Close"]

    # Calculate daily returns
    # ret[t] = price[t] / price[t-1] - 1
    ret = px / px.shift() - 1

    # Prepare regression data
    # X = independent variable (SPY returns)
    # Y = dependent variable (META returns)
    # dropna() removes the first row which has NaN due to shift()
    data = ret[["SPY", "META"]].dropna()
    X = data[["SPY"]]
    Y = data["META"]

    # ==============================================================================
    # PART 2: Fit Regression Model
    # ==============================================================================

    # Fit linear regression using sklearn
    # fit_intercept=True means we estimate both α (intercept) and β (slope)
    # Model: META = α + β × SPY + ε
    model = LinearRegression(fit_intercept=True)
    model.fit(X, Y)

    # Extract regression coefficients
    const = float(model.intercept_)  # α (alpha): excess return
    beta = float(model.coef_[0])     # β (beta): market sensitivity

    # Financial Interpretation of coefficients:
    # - beta = 1.2: META moves 20% more than SPY (high-beta stock)
    # - beta = 0.8: META moves 20% less than SPY (defensive stock)
    # - const = 0.0002 (daily): META earns ~5% annual excess return (0.0002 × 252)

    # ==============================================================================
    # PART 3: Statistical Significance Testing
    # ==============================================================================

    # Create design matrix with intercept column
    # sklearn separates intercept, but for t-values we need full design matrix
    X_design = np.column_stack([np.ones(len(X)), X.to_numpy()])
    y_vec = Y.to_numpy()
    beta_vec = np.array([const, beta])

    # Compute t-values to test if coefficients are statistically significant
    tvalues = compute_ols_tvalues(X_design, y_vec, beta_vec)

    # ==============================================================================
    # PART 4: Decompose Returns into Alpha and Beta Components
    # ==============================================================================

    # Generate predictions from the model
    # prediction[t] = α + β × SPY[t]
    prediction = pd.Series(model.predict(X), index=X.index)

    # Calculate residuals (unexplained returns)
    # resid[t] = actual_return[t] - predicted_return[t]
    resid = Y - prediction

    # Decompose total META return into two components:
    # META_return = beta_contribution + alpha_contribution

    # Beta contribution: return explained by market exposure
    # This is what you'd earn just from having beta exposure to SPY
    beta_contr = beta * X["SPY"]

    # Alpha contribution: excess return beyond beta
    # This includes both:
    #   1. Constant alpha (const): average daily excess return
    #   2. Residuals (resid): daily deviations from expected return
    alpha_contr = const + resid

    # Verification (should equal Y):
    # Y = beta_contr + alpha_contr
    # Y = (β × SPY) + (α + ε)

    # ==============================================================================
    # PART 5: Alpha Quality Analysis
    # ==============================================================================

    # Report results
    print("Params:")
    print({"const": const, "SPY": beta})

    print("T-values:")
    print({"const": float(tvalues[0]), "SPY": float(tvalues[1])})

    # Alpha statistics to evaluate if excess return is meaningful:

    # 1. Alpha mean: Average daily excess return
    # Positive = META outperformed what beta alone would predict
    print("Alpha mean:", float(alpha_contr.mean()))

    # 2. Information Ratio (IR): Risk-adjusted alpha quality
    # IR = alpha_mean / alpha_volatility (annualized)
    # Higher IR = more consistent alpha generation
    # IR > 0.5: Good, IR > 1.0: Excellent
    print("Alpha IR:", float(alpha_contr.mean() / alpha_contr.std() * np.sqrt(252)))

    # 3. Alpha correlation with SPY: Should be near zero
    # High correlation = alpha is not truly independent of market
    # We want alpha uncorrelated with market for diversification
    print("Alpha corr vs SPY:", float(alpha_contr.corr(X["SPY"])))

    # INTERPRETATION GUIDE:
    # - High |t-value| for const → alpha is statistically significant (skill, not luck)
    # - Beta close to 1.0 → stock moves with market
    # - Positive alpha IR → consistent outperformance
    # - Alpha corr near 0 → alpha is truly independent of market exposure


if __name__ == "__main__":
    main()
