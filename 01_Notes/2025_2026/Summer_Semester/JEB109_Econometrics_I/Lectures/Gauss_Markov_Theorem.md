---
course: "JEB109"
topic: "Gauss-Markov Theorem"
source: "00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_04_JEB109_2026.pdf"
tags: [JEB109, econometrics, Gauss-Markov, BLUE, efficiency, CLM-assumptions]
created: 2026-04-19
---

Parent: [[JEB109_Econometrics_I_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_04_JEB109_2026.pdf]]
Related: [[MLR_Assumptions_and_OLS_Unbiasedness]], [[Variance_of_OLS_Estimator]], [[Hypothesis_Testing_OLS]], [[OLS_Consistency_and_Asymptotics]]

# Gauss-Markov Theorem

## The Complete MLR Assumption Set

For inference we collect all six assumptions:

| # | Assumption | Description |
|---|-----------|-------------|
| MLR.1 | Linear in parameters | $y = \beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k + u$ |
| MLR.2 | Random sampling | i.i.d. sample from the population |
| MLR.3 | No perfect collinearity | $\mathbf{X}$ has full column rank |
| MLR.4 | Zero conditional mean | $E(u \mid x_1, \ldots, x_k) = 0$ |
| MLR.5 | Homoskedasticity | $\text{Var}(u \mid x_1, \ldots, x_k) = \sigma^2$ |
| MLR.6 | Normality | $u \mid x_1, \ldots, x_k \sim N(0, \sigma^2)$ |

MLR.1–MLR.5 are the **Gauss-Markov assumptions**. MLR.1–MLR.6 together constitute the **Classical Linear Model (CLM) assumptions**.

---

## Statement of the Gauss-Markov Theorem

> **Theorem (Gauss-Markov):** Under assumptions MLR.1 through MLR.5, the OLS estimator $\hat{\boldsymbol\beta}^{\text{OLS}}$ is the **Best Linear Unbiased Estimator (BLUE)** of $\boldsymbol\beta$.

That is, among all linear unbiased estimators of $\boldsymbol\beta$, OLS has the **smallest variance** (is most efficient).

---

## What "BLUE" Means

**B — Best:** Smallest variance (most precise) in the class.

**L — Linear:** The estimator is a linear function of the outcome $\mathbf{Y}$:
$$\tilde{\boldsymbol\beta} = \mathbf{C}\mathbf{Y},$$
for some matrix $\mathbf{C}$ that may depend on $\mathbf{X}$ but not on $\boldsymbol\beta$ or $\sigma^2$.

**U — Unbiased:** $E(\tilde{\boldsymbol\beta}) = \boldsymbol\beta$ for all $\boldsymbol\beta$.

**E — Estimator.**

OLS is BLUE: for any other linear unbiased estimator $\tilde\beta_j$,

$$\text{Var}(\tilde\beta_j) \geq \text{Var}(\hat\beta_j^{\text{OLS}}).$$

---

## Proof Sketch

Let $\tilde{\boldsymbol\beta} = \mathbf{C}\mathbf{Y}$ be any linear unbiased estimator. Write $\mathbf{C} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T + \mathbf{D}$ for some matrix $\mathbf{D}$.

Unbiasedness requires $\mathbf{D}\mathbf{X} = \mathbf{0}$. Then:

$$\text{Var}(\tilde{\boldsymbol\beta} \mid \mathbf{X}) = \sigma^2\mathbf{C}\mathbf{C}^T = \sigma^2(\mathbf{X}^T\mathbf{X})^{-1} + \sigma^2\mathbf{D}\mathbf{D}^T.$$

Since $\mathbf{D}\mathbf{D}^T$ is positive semi-definite:

$$\text{Var}(\tilde{\boldsymbol\beta}) - \text{Var}(\hat{\boldsymbol\beta}^{\text{OLS}}) = \sigma^2\mathbf{D}\mathbf{D}^T \succeq 0. \quad\blacksquare$$

---

## Implication: Normality of OLS Estimators (CLM)

Under the **full CLM assumptions** MLR.1–MLR.6, the OLS estimator is **normally distributed** in finite samples:

$$\hat{\boldsymbol\beta}^{\text{OLS}} \mid \mathbf{X} \sim N\!\left(\boldsymbol\beta,\; \sigma^2(\mathbf{X}^T\mathbf{X})^{-1}\right).$$

This follows because $\hat{\boldsymbol\beta} = \boldsymbol\beta + (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{u}$ is a linear transformation of $\mathbf{u}$, and a linear transformation of a normal random vector is normal.

Standardising the $j$-th component:

$$\frac{\hat\beta_j - \beta_j}{\text{sd}(\hat\beta_j)} \sim N(0, 1),$$

and replacing $\sigma$ with $\hat\sigma$:

$$\frac{\hat\beta_j - \beta_j}{\text{se}(\hat\beta_j)} \sim t_{n-k-1}.$$

This $t$ distribution is exact under MLR.6, and asymptotically valid even without MLR.6 (by CLT) — see [[OLS_Consistency_and_Asymptotics]].

---

## Historical Note: The Name

**Carl Friedrich Gauss** (1777–1855) first derived the least-squares principle in 1795 and showed its optimality properties. **Andrey Markov** (1856–1922) provided a rigorous modern proof in 1900 that does not require normality of errors — he showed BLUE under the weaker Gauss-Markov assumptions only. The theorem thus combines contributions from both. The name "OLS" itself reflects the least-squares minimization; it is distinctly a Bayesian-free, frequentist approach to estimation.

---

## Scope and Limitations

- The Gauss-Markov theorem applies **only within the class of linear estimators**. Nonlinear unbiased estimators may have smaller variance when MLR.6 fails (e.g., maximum likelihood under non-normal errors).
- Under **heteroskedasticity** (MLR.5 violated), OLS is no longer BLUE; Weighted Least Squares (WLS) is the BLUE linear estimator instead — covered in the heteroskedasticity lecture.
- As sample size grows, asymptotic properties (consistency, asymptotic efficiency) take over; see [[OLS_Consistency_and_Asymptotics]].
