---
course: "JEB109"
topic: "OLS Estimator — Simple Regression"
source: "00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_02_JEB109_2026.pdf"
tags: [JEB109, econometrics, OLS, estimation, method-of-moments, least-squares]
created: 2026-04-19
---

Parent: [[JEB109_Econometrics_I_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_02_JEB109_2026.pdf]]
Related: [[Simple_Linear_Regression]], [[MLR_Assumptions_and_OLS_Unbiasedness]], [[Variance_of_OLS_Estimator]], [[Gauss_Markov_Theorem]]

# OLS Estimator — Simple Linear Regression

## Deriving OLS via Method of Moments

The **method of moments (MM)** replaces population moment conditions with their sample analogues. From SLR.4:

$$E(u) = E(y - \beta_0 - \beta_1 x) = 0$$
$$\text{Cov}(x, u) = E\bigl[x(y - \beta_0 - \beta_1 x)\bigr] = 0.$$

Substituting sample moments (with $\frac{1}{n}\sum_{i=1}^n \equiv \overline{\phantom{X}}$):

$$\frac{1}{n}\sum_{i=1}^n (y_i - \hat\beta_0 - \hat\beta_1 x_i) = 0,$$
$$\frac{1}{n}\sum_{i=1}^n x_i(y_i - \hat\beta_0 - \hat\beta_1 x_i) = 0.$$

### Solving the MM System

From the first equation:

$$\hat\beta_0 = \bar y - \hat\beta_1 \bar x.$$

Substituting into the second equation and solving:

$$\hat\beta_1^{\text{OLS}} = \frac{\sum_{i=1}^n x_i(y_i - \bar y)}{\sum_{i=1}^n x_i(x_i - \bar x)} = \frac{\sum_{i=1}^n (x_i - \bar x)(y_i - \bar y)}{\sum_{i=1}^n (x_i - \bar x)^2}.$$

The denominator $\text{SST}_x = \sum_{i=1}^n (x_i - \bar x)^2 > 0$ is guaranteed by SLR.3.

**Alternative forms of $\hat\beta_1$** (all equivalent):

$$\hat\beta_1^{\text{OLS}} = \frac{\sum x_i(y_i - \bar y)}{\sum x_i(x_i - \bar x)} = \frac{\sum y_i(x_i - \bar x)}{\sum (x_i - \bar x)^2} = \frac{\sum (x_i - \bar x)(y_i - \bar y)}{\sum (x_i - \bar x)^2}.$$

---

## Deriving OLS via Least Squares Minimization

Define the **residual** $\hat u_i = y_i - \hat y_i = y_i - \hat\beta_0 - \hat\beta_1 x_i$.

The **sum of squared residuals (SSR)** is the objective function:

$$\text{SSR} \equiv \sum_{i=1}^n \hat u_i^2 = \sum_{i=1}^n (y_i - \hat\beta_0 - \hat\beta_1 x_i)^2.$$

**First-Order Conditions (FOCs):**

$$\frac{\partial \text{SSR}}{\partial \hat\beta_0} = 0 \implies -2\sum_{i=1}^n (y_i - \hat\beta_0 - \hat\beta_1 x_i) = 0,$$
$$\frac{\partial \text{SSR}}{\partial \hat\beta_1} = 0 \implies -2\sum_{i=1}^n x_i(y_i - \hat\beta_0 - \hat\beta_1 x_i) = 0.$$

These **normal equations** are identical to the MM system, so OLS and MM yield the same estimator. Hence the name **Ordinary Least Squares (OLS)**.

---

## Sample Regression Function (SRF)

The estimated (sample) regression line is:

$$\hat y = \hat\beta_0 + \hat\beta_1 x.$$

This is the **SRF** or **OLS regression line**. It is an *estimate* of the PRF $E(y \mid x) = \beta_0 + \beta_1 x$ and differs across samples.

---

## Algebraic Properties of OLS

The OLS estimator satisfies by construction:

1. $\sum_{i=1}^n \hat u_i = 0$ — residuals sum to zero,
2. $\sum_{i=1}^n x_i \hat u_i = 0$ — residuals are orthogonal to $x$,
3. The point $(\bar x, \bar y)$ always lies on the SRF: $\bar y = \hat\beta_0 + \hat\beta_1 \bar x$,
4. $\sum_{i=1}^n \hat y_i = \sum_{i=1}^n y_i$ — fitted values sum to observed values.

---

## Goodness of Fit: $R^2$

Decompose total variation:

$$\underbrace{\sum_{i=1}^n (y_i - \bar y)^2}_{\text{SST}} = \underbrace{\sum_{i=1}^n (\hat y_i - \bar y)^2}_{\text{SSE}} + \underbrace{\sum_{i=1}^n \hat u_i^2}_{\text{SSR}}.$$

The **coefficient of determination** (fraction of variance explained):

$$R^2 = \frac{\text{SSE}}{\text{SST}} = 1 - \frac{\text{SSR}}{\text{SST}} \in [0, 1].$$

In the SLR model, $R^2 = \hat\rho_{x,y}^2$ (squared sample correlation between $x$ and $y$).

**Caution:** $R^2$ cannot decrease when adding regressors, so it is not suitable for model selection in MLR. Use adjusted $\bar R^2$ instead — see [[Functional_Forms_and_Model_Comparison]].

---

## Standard Error of the Regression

An unbiased estimator of $\sigma^2 = \text{Var}(u)$ is:

$$\hat\sigma^2 = \frac{\text{SSR}}{n - 2} = \frac{\sum_{i=1}^n \hat u_i^2}{n - 2},$$

where $n - 2$ are the degrees of freedom (we lose 2 for estimating $\beta_0$ and $\beta_1$).

The **standard error of the regression (SER)** is $\hat\sigma = \sqrt{\hat\sigma^2}$.

Standard errors of the estimates:

$$\text{se}(\hat\beta_1) = \frac{\hat\sigma}{\sqrt{\text{SST}_x}}, \qquad \text{se}(\hat\beta_0) = \hat\sigma\sqrt{\frac{\sum x_i^2}{n\,\text{SST}_x}}.$$

---

## Distinction: Estimator vs. Estimate

| Concept | Definition |
|---------|-----------|
| **Estimator** $\hat\beta_1$ | A random variable (function of the sample) |
| **Estimate** $\hat\beta_1 = 0.45$ | A specific real number from a given dataset |

The OLS estimator has a sampling distribution; its properties (unbiasedness, efficiency) are statements about this distribution across all possible samples.
