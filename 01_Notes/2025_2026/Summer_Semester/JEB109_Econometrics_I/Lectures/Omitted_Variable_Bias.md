---
course: "JEB109"
topic: "Omitted Variable Bias"
source: "00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_03_JEB109_2026-1.pdf"
tags: [JEB109, econometrics, OVB, bias, misspecification, endogeneity]
created: 2026-04-19
---

Parent: [[JEB109_Econometrics_I_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_03_JEB109_2026-1.pdf]]
Related: [[MLR_Assumptions_and_OLS_Unbiasedness]], [[Variance_of_OLS_Estimator]], [[OLS_Consistency_and_Asymptotics]]

# Omitted Variable Bias (OVB)

## Set-Up

Suppose the **true population model** is:

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + u \quad (\text{MLR.1–MLR.4 hold}),$$

but the researcher **omits** $x_2$ and estimates the restricted (underspecified) model:

$$y = \tilde\beta_0 + \tilde\beta_1 x_1 + v.$$

---

## Derivation of the Bias

The OLS estimator of $\tilde\beta_1$ (based on the simple regression of $y$ on $x_1$):

$$\hat{\tilde\beta}_1 = \frac{\sum_{i=1}^n y_i(x_{i1} - \bar x_1)}{\sum_{i=1}^n (x_{i1} - \bar x_1)^2}.$$

Substituting the true DGP $y_i = \beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + u_i$:

$$\hat{\tilde\beta}_1 = \beta_1 + \beta_2 \cdot \underbrace{\frac{\sum_{i=1}^n x_{i2}(x_{i1} - \bar x_1)}{\sum_{i=1}^n (x_{i1} - \bar x_1)^2}}_{\equiv\, \hat\delta_1} + \frac{\sum_{i=1}^n u_i(x_{i1} - \bar x_1)}{\sum_{i=1}^n (x_{i1} - \bar x_1)^2}.$$

Taking conditional expectation (using MLR.4):

$$E(\hat{\tilde\beta}_1) = \beta_1 + \beta_2 \hat\delta_1,$$

where $\hat\delta_1$ is the OLS coefficient from the **auxiliary regression** of $x_2$ on $x_1$.

$$\text{Bias} = E(\hat{\tilde\beta}_1) - \beta_1 = \beta_2 \cdot \hat\delta_1 = \beta_2 \cdot \frac{\sum(x_{i2} - \bar x_2)(x_{i1} - \bar x_1)}{\sum(x_{i1} - \bar x_1)^2}.$$

Note that $\hat\delta_1 \approx \frac{\text{Cov}(x_1, x_2)}{\text{Var}(x_1)} = \beta_1^{\text{aux}}$, the regression coefficient of $x_2$ on $x_1$.

---

## Direction of the Bias: Summary Table

| | $\text{Corr}(x_2, x_1) > 0$ | $\text{Corr}(x_2, x_1) < 0$ |
|---|---|---|
| $\beta_2 > 0$ | **Positive bias** (upward) | **Negative bias** (downward) |
| $\beta_2 < 0$ | **Negative bias** (downward) | **Positive bias** (upward) |

**Rule of thumb:** Bias direction = sign($\beta_2$) × sign($\text{Corr}(x_1, x_2)$).

---

## Two Conditions for OVB

Omitting $x_2$ causes bias **if and only if both** conditions hold:
1. $\beta_2 \neq 0$: $x_2$ is actually relevant (has a true non-zero effect on $y$),
2. $\text{Cov}(x_1, x_2) \neq 0$: $x_2$ is correlated with the included regressor $x_1$.

If either condition fails — if $x_2$ is irrelevant OR if $x_2$ is orthogonal to $x_1$ — OLS remains unbiased.

---

## Examples

### 1. Wage Regression
True model: $\log(\text{wage}) = \beta_0 + \beta_1\,\text{educ} + \beta_2\,\text{ability} + u$.

If ability is unobserved and omitted:
- $\beta_2 > 0$ (higher ability → higher wage),
- $\text{Corr}(\text{educ}, \text{ability}) > 0$ (smarter people get more education),
- $\Rightarrow$ OVB is **positive**: $\hat\beta_1^{\text{OLS}}$ **overstates** the return to education.

### 2. Class Size and Test Scores
True model: $\text{score} = \beta_0 + \beta_1\,\text{classsize} + \beta_2\,\text{income} + u$.

If income is omitted:
- $\beta_2 > 0$ (richer areas score higher),
- $\text{Corr}(\text{classsize}, \text{income}) < 0$ (richer areas have smaller classes),
- $\Rightarrow$ OVB is **negative**: OLS overstates the harm of large classes.

---

## OVB in Population Terms (Inconsistency)

In large samples, the inconsistency of $\hat\beta_1$ when $x_2$ is omitted:

$$\text{plim}(\hat{\tilde\beta}_1) - \beta_1 = \frac{\text{Cov}(x_1, u)}{\text{Var}(x_1)} = \beta_2 \cdot \frac{\text{Cov}(x_1, x_2)}{\text{Var}(x_1)}.$$

This is the asymptotic version of the bias formula, expressed in population terms. See [[OLS_Consistency_and_Asymptotics]] for the formal consistency discussion.

---

## Remedies

| Problem | Solution |
|---------|---------|
| Unobserved confounder correlated with $x_1$ | Instrumental Variables (IV) |
| Observable confounder | Include it as control variable |
| Panel data with fixed unit effects | Fixed effects estimator |
| Randomized experiment | Randomization ensures $\text{Cov}(x_1, u) = 0$ by design |
