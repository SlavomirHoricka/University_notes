---
course: "JEB109"
topic: "F-Test and Multiple Restrictions"
source: "00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_06_JEB109_2026.pdf"
tags: [JEB109, econometrics, F-test, multiple-restrictions, LM-test, exclusion-restrictions]
created: 2026-04-19
---

Parent: [[JEB109_Econometrics_I_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_06_JEB109_2026.pdf]]
Related: [[Hypothesis_Testing_OLS]], [[Gauss_Markov_Theorem]], [[OLS_Consistency_and_Asymptotics]], [[Variance_of_OLS_Estimator]]

# F-Test and Testing Multiple Linear Restrictions

## Motivation: Testing Multiple Restrictions Simultaneously

A $t$ test evaluates a **single** linear restriction. When we want to test the joint significance of several coefficients, we need the **$F$ test**.

**Example:** In the model $y = \beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k + u$, test whether $q$ of the $k$ regressors together have any effect:

$$H_0{:}\ \beta_{k-q+1} = 0,\; \beta_{k-q+2} = 0,\; \ldots,\; \beta_k = 0.$$

These are called **exclusion restrictions** — $q$ regressors are jointly excluded under $H_0$.

---

## The F Statistic

Run two regressions:
- **Unrestricted model (UR):** includes all $k$ regressors — compute $\text{SSR}_{\text{UR}}$, degrees of freedom $df_{\text{UR}} = n - k - 1$.
- **Restricted model (R):** imposes $H_0$ (drops $q$ regressors) — compute $\text{SSR}_{\text{R}}$, $df_{\text{R}} = n - k - 1 + q$.

The **F statistic**:

$$F = \frac{(\text{SSR}_{\text{R}} - \text{SSR}_{\text{UR}})/q}{\text{SSR}_{\text{UR}}/(n - k - 1)}.$$

Under $H_0$ and the CLM assumptions: $F \sim F_{q,\, n-k-1}$.

**Equivalent $R^2$ form** (when the same dependent variable is used in both models):

$$F = \frac{(R_{\text{UR}}^2 - R_{\text{R}}^2)/q}{(1 - R_{\text{UR}}^2)/(n - k - 1)}.$$

Note: The $R^2$ form cannot be used when $H_0$ involves **non-zero restrictions** (e.g., $\beta_1 = 1$), because the restricted model may differ in its dependent variable — only the SSR form is universally valid.

---

## Interpreting the F Statistic

- A large $F$ means the restricted model fits the data **significantly worse** than the unrestricted model, suggesting the restrictions are false.
- Reject $H_0$ at significance level $\alpha$ if $F > c_\alpha$, where $c_\alpha$ is the $\alpha$-upper critical value of $F_{q,\, n-k-1}$.
- Equivalently, reject if $p\text{-value} < \alpha$.

---

## Overall Significance of the Regression

A special and important F test is the **overall F test**:

$$H_0{:}\ \beta_1 = \beta_2 = \cdots = \beta_k = 0$$

(all slope coefficients are zero; only the intercept survives). This tests whether the model has any explanatory power.

$$F = \frac{R^2/k}{(1 - R^2)/(n - k - 1)} \sim F_{k,\, n-k-1} \quad \text{under } H_0.$$

Every standard OLS output table reports this statistic.

---

## General Linear Restrictions

The F test framework extends to any set of $q$ **linear restrictions** on $\boldsymbol\beta$, expressible as $\mathbf{R}\boldsymbol\beta = \mathbf{r}$ for a $q \times (k+1)$ matrix $\mathbf{R}$ and vector $\mathbf{r}$.

**Example:** $H_0{:}\ \beta_1 = 1,\; \beta_2 = 0,\; \beta_3 = 0$ in a model with 4 regressors.  
The restricted model becomes $y = \beta_0 + x_1 + u$, i.e., $y - x_1 = \beta_0 + u$.

**CAPM example:**  
In the CAPM regression $r_{i,t} - r_{f,t} = \alpha_i + \beta_i(r_{M,t} - r_{f,t}) + u_{i,t}$, test the efficient market null $H_0{:}\ \alpha_i = 0,\, \beta_i = 1$.  
The restricted residuals: $\text{SSR}_{\text{R}} = \sum_t (r_{i,t} - r_{M,t})^2$ (nothing to estimate).

---

## Connection to the t Test

For $q = 1$ exclusion restriction, the F test and t test are equivalent:

$$F_{1,\, n-k-1} = t_{n-k-1}^2.$$

The $F$ test is always two-sided for $q = 1$; for one-sided alternatives one must use the $t$ test.

---

## Lagrange Multiplier (LM) Test

An asymptotically equivalent approach for testing $q$ exclusion restrictions **without assuming MLR.6**:

### Procedure

1. State $H_0{:}\ \beta_{k-q+1} = \cdots = \beta_k = 0$.
2. Estimate the **restricted model** (without the $q$ variables) → save residuals $\tilde u_i$.
3. Run an **auxiliary regression**: regress $\tilde u_i$ on **all** independent variables (including the $q$ restricted ones) → obtain $R^2_{\tilde u}$.
4. Compute $\text{LM} = n\cdot R^2_{\tilde u}$.
5. Under $H_0$: $\text{LM} \overset{a}{\sim} \chi^2_q$.
6. Reject $H_0$ if $\text{LM} > c_\alpha$ (the $\alpha$-upper critical value of $\chi^2_q$).

**Intuition:** If the excluded variables are truly irrelevant ($H_0$ true), they should be nearly uncorrelated with the restricted model residuals — $R^2_{\tilde u}$ should be close to zero and hence LM small.

**Advantage over F test:** LM does not require normality (MLR.6). It is a large-sample test based on the CLT.

---

## Historical Note: Ronald Fisher (1890–1962)

Ronald A. Fisher formalised the $F$ test as part of ANOVA (Analysis of Variance). His approach: compare between-group variation relative to within-group variation. If the between-group ratio is large, the groups differ significantly. The "F" in $F$ statistic honours Fisher. Fisher's demonstration using the "lady tasting tea" experiment illustrated the principle of randomized testing and clear decision rules that carry over directly to econometric model testing.
