---
course: "JEB109"
topic: "Simple Linear Regression Model"
source: "00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_02_JEB109_2026.pdf"
tags: [JEB109, econometrics, OLS, simple-regression, SLR]
created: 2026-04-19
---

Parent: [[JEB109_Econometrics_I_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_02_JEB109_2026.pdf]]
Related: [[Introduction_to_Econometrics]], [[OLS_Estimator_Simple_Regression]], [[MLR_Assumptions_and_OLS_Unbiasedness]]

# Simple Linear Regression (SLR) Model

## Model Definition

The **simple linear regression model** (SLR) describes the relationship between a dependent variable $y$ and a single independent (explanatory) variable $x$ via a **population model**:

$$y = \beta_0 + \beta_1 x + u,$$

where:
- $y$ — dependent variable (regressand, outcome, response),
- $x$ — independent variable (regressor, predictor, explanatory variable),
- $\beta_0$ — **intercept**: the expected value of $y$ when $x = 0$,
- $\beta_1$ — **slope**: the change in the expected value of $y$ per unit increase in $x$, *ceteris paribus*,
- $u$ — **error term** (disturbance): captures all factors other than $x$ that affect $y$.

The model is **linear in parameters** $\beta_0$ and $\beta_1$, not necessarily linear in $x$ and $y$ (one can substitute $\log y$ or $x^2$).

---

## Population Regression Function (PRF)

The **PRF** is the conditional expectation of $y$ given $x$:

$$E(y \mid x) = \beta_0 + \beta_1 x.$$

This requires **SLR.4 Zero Conditional Mean**:

$$E(u \mid x) = 0.$$

The zero conditional mean assumption implies:
- $E(u) = 0$ (by the law of iterated expectations),
- $\text{Cov}(x, u) = 0$ (exogeneity of $x$).

---

## SLR Assumptions

| Assumption | Statement |
|-----------|-----------|
| **SLR.1** Linear in parameters | $y = \beta_0 + \beta_1 x + u$ |
| **SLR.2** Random sampling | $(y_i, x_i)$, $i = 1, \ldots, n$, is a random sample from the population |
| **SLR.3** Sample variation in $x$ | $\text{Var}(x) \neq 0$, i.e., $\sum_{i=1}^n (x_i - \bar{x})^2 > 0$ |
| **SLR.4** Zero conditional mean | $E(u \mid x) = 0$ |

SLR.1–SLR.4 suffice for **unbiasedness** of OLS. An additional assumption:

| **SLR.5** Homoskedasticity | $\text{Var}(u \mid x) = \sigma^2$ (constant) |

is needed for the standard variance formulas. Adding:

| **SLR.6** Normality | $u \mid x \sim N(0, \sigma^2)$ |

establishes the exact finite-sample $t$ and $F$ distributions.

---

## Interpretation of Coefficients

**Slope $\beta_1$:**

$$\beta_1 = \frac{\Delta E(y \mid x)}{\Delta x} = \frac{\partial E(y \mid x)}{\partial x}.$$

It measures the *ceteris paribus* change in $y$ for a one-unit increase in $x$. **Crucially**, this is a ceteris paribus statement: all other determinants of $y$ (captured by $u$) are held fixed.

**Intercept $\beta_0$:**
The predicted value of $y$ when $x = 0$. Often lacks economic meaning if $x = 0$ is outside the data range.

### Functional Form Variants

| Model | Equation | Slope interpretation |
|-------|----------|---------------------|
| Level-level | $y = \beta_0 + \beta_1 x + u$ | $\Delta y = \beta_1 \Delta x$ |
| Log-level | $\log(y) = \beta_0 + \beta_1 x + u$ | $\%\Delta y \approx 100\beta_1 \Delta x$ |
| Level-log | $y = \beta_0 + \beta_1 \log(x) + u$ | $\Delta y \approx (\beta_1/100)\%\Delta x$ |
| Log-log | $\log(y) = \beta_0 + \beta_1 \log(x) + u$ | $\%\Delta y \approx \beta_1\%\Delta x$ (elasticity) |

---

## Historical Note: Galton's Regression

Francis Galton (1822–1911) coined the term "regression" from studying *regression toward mediocrity* in hereditary stature: tall parents have tall children on average, but children's heights are closer to the population mean than parents'. This is a consequence of random measurement error and the statistical regression-to-the-mean phenomenon. His 1886 paper established the scatter plot and the regression line; his 1888 paper introduced correlation. See also [[OLS_Estimator_Simple_Regression]].
