---
course: "JEB109"
topic: "Variance of the OLS Estimator"
source: "00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_03_JEB109_2026-1.pdf"
tags: [JEB109, econometrics, OLS, variance, homoskedasticity, multicollinearity, VIF]
created: 2026-04-19
---

Parent: [[JEB109_Econometrics_I_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_03_JEB109_2026-1.pdf]]
Related: [[MLR_Assumptions_and_OLS_Unbiasedness]], [[Gauss_Markov_Theorem]], [[Omitted_Variable_Bias]], [[Hypothesis_Testing_OLS]]

# Variance of the OLS Estimator

## The Fifth MLR Assumption — Homoskedasticity

To derive the sampling variance of $\hat{\boldsymbol\beta}^{\text{OLS}}$, we need a fifth assumption:

> **MLR.5 Homoskedasticity:** The error $u$ has the same variance given any values of the independent variables:
> $$\text{Var}(u \mid x_1, \ldots, x_k) = \sigma^2.$$

In matrix form: $\text{Var}(\mathbf{u} \mid \mathbf{X}) = \sigma^2 \mathbf{I}_n$.

If MLR.5 is violated — i.e., $\text{Var}(u \mid \mathbf{x})$ depends on $\mathbf{x}$ — we have **heteroskedasticity**. OLS is still unbiased but is no longer BLUE; inference based on standard errors is invalid. Heteroskedasticity is treated in Lectures 10–11.

---

## Variance Formula (Scalar Form)

### Assumptions

Under **MLR.1 through MLR.5**, conditional on the sample values of the independent variables:

$$\text{Var}(\hat\beta_j) = \frac{\sigma^2}{\text{SST}_j(1 - R_j^2)}, \quad j = 1, 2, \ldots, k,$$

where:
- $\text{SST}_j = \sum_{i=1}^n (x_{ij} - \bar x_j)^2$ — total sample variation in $x_j$,
- $R_j^2$ — the $R^2$ from regressing $x_j$ on all other independent variables (and the intercept).

**Interpretation of terms:**
| Term | Effect on $\text{Var}(\hat\beta_j)$ |
|------|-------------------------------------|
| Larger $\sigma^2$ | Increases variance (noisier errors → less precision) |
| Larger $\text{SST}_j$ | Decreases variance (more variation in $x_j$ → more information) |
| Larger $R_j^2$ | Increases variance (high collinearity → imprecision) |

---

## Variance Formula (Matrix Form)

$$\text{Var}(\hat{\boldsymbol\beta} \mid \mathbf{X}) = \sigma^2\,(\mathbf{X}^T\mathbf{X})^{-1}.$$

### Derivation

Starting from $\hat{\boldsymbol\beta} = \boldsymbol\beta + (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{u}$ (established in [[MLR_Assumptions_and_OLS_Unbiasedness]]):

$$\text{Var}(\hat{\boldsymbol\beta} \mid \mathbf{X}) = \text{Var}\!\left[(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{u} \mid \mathbf{X}\right]$$

Using $\text{Var}(\mathbf{A}\mathbf{u}) = \mathbf{A}\,\text{Var}(\mathbf{u})\,\mathbf{A}^T$ and MLR.5 ($\text{Var}(\mathbf{u}) = \sigma^2\mathbf{I}_n$):

$$= (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\cdot\sigma^2\mathbf{I}_n\cdot\mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1} = \sigma^2(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{X}(\mathbf{X}^T\mathbf{X})^{-1} = \sigma^2(\mathbf{X}^T\mathbf{X})^{-1}. \quad\blacksquare$$

---

## Estimating $\sigma^2$

The true error variance $\sigma^2$ is unobserved. Under MLR.1–MLR.5, the unbiased estimator is:

$$\hat\sigma^2 = \frac{\text{SSR}}{n - k - 1} = \frac{\sum_{i=1}^n \hat u_i^2}{n - k - 1}.$$

The denominator $n - k - 1$ accounts for the **degrees of freedom** lost: estimation of $k + 1$ parameters imposes $k + 1$ linear restrictions on the residuals:

$$\sum_{i=1}^n \hat u_i = 0, \quad \sum_{i=1}^n x_{ij}\hat u_i = 0, \quad j = 1, \ldots, k.$$

- **Standard error of the regression (SER):** $\hat\sigma = \sqrt{\hat\sigma^2}$.
- **Standard error of $\hat\beta_j$:**
  $$\text{se}(\hat\beta_j) = \frac{\hat\sigma}{\sqrt{\text{SST}_j(1 - R_j^2)}}.$$
  In matrix form: $\text{se}(\hat\beta_j) = \hat\sigma\,\sqrt{[(\mathbf{X}^T\mathbf{X})^{-1}]_{j+1,\, j+1}}$.

---

## Variance Inflation Factor (VIF)

To isolate the role of multicollinearity, define the **Variance Inflation Factor**:

$$\text{VIF}_j = \frac{1}{1 - R_j^2}, \quad \text{so that} \quad \text{Var}(\hat\beta_j) = \frac{\sigma^2}{\text{SST}_j} \cdot \text{VIF}_j.$$

- $R_j^2 = 0$ (no collinearity): $\text{VIF}_j = 1$ — baseline, lowest possible variance.
- $R_j^2 \to 1$ (near-perfect collinearity): $\text{VIF}_j \to \infty$ — variance explodes.
- Common rule of thumb: $\text{VIF}_j > 10$ signals severe multicollinearity.

**Note:** Multicollinearity does not cause bias — it only degrades precision. This is the **bias–variance trade-off** in model specification: overspecified models (too many variables) are unbiased but imprecise; underspecified models are precise but biased (see [[Omitted_Variable_Bias]]).

---

## Variance in Misspecified Models

### Overspecified Model (Irrelevant Variable Included)

Including an irrelevant variable $x_{k+1}$ (with true $\beta_{k+1} = 0$):
- OLS remains **unbiased** for all $\beta_j$ (MLR.4 still holds).
- $R_j^2$ typically increases (or stays) → **variance increases**.

### Underspecified Model (Relevant Variable Omitted)

Omitting a relevant $x_2$ that is correlated with $x_1$:
- $R_j^2$ for $x_1$ decreases → **variance of $\hat\beta_1$ decreases**.
- But: OLS becomes **biased** (see [[Omitted_Variable_Bias]]).
- The reduced variance comes at the cost of introducing a bias — a canonical bias-variance trade-off.

---

## Practical Guidance

The optimal model specification minimizes **Mean Squared Error (MSE)**:

$$\text{MSE}(\hat\beta_j) = \text{Var}(\hat\beta_j) + \left[\text{Bias}(\hat\beta_j)\right]^2.$$

In general, a correctly specified model (neither over- nor under-specified) achieves the BLUE property — see [[Gauss_Markov_Theorem]].
