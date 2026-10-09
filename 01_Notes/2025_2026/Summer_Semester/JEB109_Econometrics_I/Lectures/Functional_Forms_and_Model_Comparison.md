---
course: "JEB109"
topic: "Functional Forms and Model Comparison"
source: "00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_07_JEB109_2026.pdf"
tags: [JEB109, econometrics, functional-form, logarithms, quadratic, interaction, adjusted-R2]
created: 2026-04-19
---

Parent: [[JEB109_Econometrics_I_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_07_JEB109_2026.pdf]]
Related: [[OLS_Estimator_Simple_Regression]], [[MLR_Assumptions_and_OLS_Unbiasedness]], [[Dummy_Variables]], [[F_Test_and_Multiple_Restrictions]]

# Functional Forms and Model Comparison

## 1. Effects of Scaling on OLS Statistics

### Rescaling an Independent Variable

Suppose we replace $x_1$ with $x_1^* = x_1/c$ ($c > 0$). The reparameterised model:

$$y = \beta_0 + \gamma_1 x_1^* + \cdots + u, \quad \gamma_1 = c\beta_1.$$

Effects on OLS output:
- $\hat\gamma_1 = c\hat\beta_1$ (estimate scales by $c$),
- $\text{se}(\hat\gamma_1) = c\cdot\text{se}(\hat\beta_1)$ (SE scales by $c$, since $\text{SST}_{x^*} = \text{SST}_x / c^2$),
- $t_{\hat\gamma_1} = t_{\hat\beta_1}$ (t-statistic **invariant** to scaling),
- $p$-value unchanged.

### Rescaling the Dependent Variable

Replace $y$ with $y^* = cy$:
- All slope estimates scale: $\hat\gamma_j = c\hat\beta_j$,
- SEs scale: $\text{se}(\hat\gamma_j) = |c|\cdot\text{se}(\hat\beta_j)$,
- $t$ statistics and $p$-values unchanged.

### Logarithmic Variables

Rescaling a log-transformed variable changes **only the intercept**:

$$\log(cy) = \log(c) + \log(y) \implies \hat\gamma_0 = \hat\beta_0 + \log(c),$$

leaving all slope estimates unchanged. Similarly for $\log(cx_j)$.

---

## 2. Logarithmic Forms

### Summary of Log Specifications

| Model | Equation | Slope interpretation of $\beta_1$ |
|-------|----------|----------------------------------|
| Level-level | $y = \beta_0 + \beta_1 x + u$ | $\Delta y = \beta_1 \Delta x$ |
| Log-level | $\log(y) = \beta_0 + \beta_1 x + u$ | $\%\Delta y \approx 100\beta_1\,\Delta x$ (semi-elasticity) |
| Level-log | $y = \beta_0 + \beta_1\log(x) + u$ | $\Delta y \approx (\beta_1/100)\,\%\Delta x$ |
| Log-log | $\log(y) = \beta_0 + \beta_1\log(x) + u$ | $\%\Delta y \approx \beta_1\,\%\Delta x$ (**constant elasticity**) |

**Exact percentage change for log-level model:**

$$\%\Delta\hat y = 100\bigl(\exp(\hat\beta_1\,\Delta x) - 1\bigr),$$

which differs from the approximation $100\hat\beta_1\,\Delta x$ when $|\hat\beta_1\,\Delta x|$ is large.

**Why use logarithms?**
- Compresses large positive values and reduces heteroskedasticity.
- Gives a direct elasticity interpretation (log-log).
- Models where $y$ has a right-skewed distribution (wages, prices, market values) often more closely satisfy CLM assumptions after log transformation (linearity, homoskedasticity, normality).

---

## 3. Quadratic and Polynomial Forms

### Quadratic Model

$$y = \beta_0 + \beta_1 x + \beta_2 x^2 + u.$$

The marginal effect of $x$ on $y$ is **not constant** but depends on the level of $x$:

$$\frac{\partial\hat y}{\partial x} = \hat\beta_1 + 2\hat\beta_2 x.$$

Common use case: diminishing marginal returns ($\hat\beta_1 > 0$, $\hat\beta_2 < 0$, $|\hat\beta_1| \gg |\hat\beta_2|$).

**Turning point (TP):** Set the marginal effect to zero:

$$x^* = -\frac{\hat\beta_1}{2\hat\beta_2}.$$

$x^* > 0$ is only economically meaningful if the data have support in that region.

### Log-Quadratic Model

$$\log(y) = \beta_0 + \beta_1\log(x) + \beta_2\bigl(\log(x)\bigr)^2 + u.$$

Note: it is the **square of $\log(x)$** (not the log of $x^2$). The elasticity:

$$\%\Delta\hat y \approx \bigl(\hat\beta_1 + 2\hat\beta_2\log(x)\bigr)\,\%\Delta x.$$

---

## 4. Interaction Terms

When the effect of $x_1$ on $y$ depends on the level of $x_2$:

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_1 x_2 + u.$$

Partial effect of $x_1$:

$$\frac{\partial\hat y}{\partial x_1} = \hat\beta_1 + \hat\beta_3 x_2.$$

This is an **interaction effect**: the marginal effect of $x_1$ varies linearly with $x_2$.

**Testing for interaction:** Standard $t$ test on $\hat\beta_3$ or $F$ test for $H_0{:}\ \beta_3 = 0$.

**Reporting practice:** Since $\hat\beta_1$ alone no longer gives the full partial effect, report the effect for economically meaningful values of $x_2$ (mean, median, selected quantiles).

---

## 5. Goodness of Fit: Adjusted $\bar R^2$

### Problem with $R^2$

$R^2$ **never decreases** when a new variable is added to the model (even a completely irrelevant one), because SSR cannot increase. Therefore $R^2$ is useless for comparing models with different numbers of regressors.

### Adjusted $R^2$

Define the **adjusted coefficient of determination** $\bar R^2$ that penalises for adding regressors:

$$R^2 = 1 - \frac{\text{SSR}/n}{\text{SST}/n}, \qquad \bar R^2 = 1 - \frac{\text{SSR}/(n-k-1)}{\text{SST}/(n-1)}.$$

Equivalently:

$$\bar R^2 = 1 - (1 - R^2)\,\frac{n-1}{n-k-1}.$$

Properties:
- $\bar R^2 \leq R^2$ always (penalty for $k > 0$).
- $\bar R^2 \to R^2$ as $n \to \infty$ (penalty vanishes asymptotically).
- $\bar R^2$ **can be negative** (model worse than predicting $\bar y$ for all observations).

**Key result:** Adding a variable increases $\bar R^2$ if and only if its $|t|$ statistic exceeds 1. Similarly, adding a group of variables increases $\bar R^2$ if and only if their $F$ statistic exceeds 1.

---

## 6. Comparing Non-Nested Models

**Non-nested models** are models where neither is a special case of the other. Example:

$$\text{Model A:}\quad y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + u,$$
$$\text{Model B:}\quad y = \gamma_0 + \gamma_1 x_1 + \gamma_2 x_3 + v.$$

Here $x_2 \neq x_3$. We **cannot** use the standard F test (neither model is restricted by the other). Options:

- Compare $\bar R^2$ (only valid when dependent variable is the same in both models).
- Use information criteria: AIC, BIC (penalise $k$ differently).
- **Davidson-MacKinnon J test**: a model selection test for non-nested models (beyond this course).

**Caution:** Comparing $R^2$ across models with **different dependent variables** (e.g., $y$ vs. $\log(y)$) is **invalid** — SST differs.
