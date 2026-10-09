---
course: "JEB109"
topic: "Dummy Variable Interactions and Chow Test"
source: "00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_09_JEB109_2026.pdf"
tags: [JEB109, econometrics, dummy-variables, interactions, chow-test, structural-break]
created: 2026-04-28
---

Parent: [[JEB109_Econometrics_I_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_09_JEB109_2026.pdf]]
Related: [[Dummy_Variables]], [[F_Test_and_Multiple_Restrictions]], [[MLR_Assumptions_and_OLS_Unbiasedness]], [[Linear_Probability_Model]]

---

# Dummy Variable Interactions and the Chow Test

## Interactions Among Dummy Variables

When a model contains two or more binary explanatory variables, their **interaction term** (the product $D_1 \cdot D_2$) allows the effect of one dummy to differ depending on the value of the other.

### Multi-criterial dummies vs. interacting dummies

Both approaches span the same four group cells but serve different analytical purposes:

| Approach | Typical use |
|---|---|
| **Multi-criterial dummies** (one per group): $y = \gamma_0 + \gamma_1 D_{UC} + \gamma_2 D_{EF} + \gamma_3 D_{UF} + v$ | Testing *differences between specific groups* directly |
| **Interacting dummies**: $y = \beta_0 + \beta_1 E + \beta_2 C + \beta_3 (E \cdot C) + v$ | Testing *whether an interaction itself is significant* (e.g., does the employment income differential depend on citizenship?) |

### Identifying the base group

With interacting dummies the base group is the cell where **all** constituent dummies and their products equal zero. In the employment–citizenship example:

$$\text{income} = \beta_0 + \beta_1 E + \beta_2 C + \beta_3 E \cdot C + v$$

- $E = 0, C = 0$ (unemployed foreigners) → **base group**
- $E = 0, C = 1$ (unemployed citizens) → test $\beta_2 = 0$
- $E = 1, C = 0$ (employed foreigners) → test $\beta_1 = 0$
- $E = 1, C = 1$ (employed citizens) → test $\theta \equiv \beta_1 + \beta_2 + \beta_3 = 0$ (requires reparameterisation)

When interaction terms are included, the constituent main-effect dummies should also be present in the model.

---

## Slope Dummy Variables

An **intercept dummy** $D$ shifts the regression function vertically (see [[Dummy_Variables]]). An interaction between $D$ and a continuous regressor $x$ creates a **slope dummy**, allowing the slope of $x$ to differ across groups.

### Model specification

$$y = \beta_0 + \beta_1 x + \beta_2 D + \beta_3 Dx + u$$

This is equivalent to two separate sub-population regressions:

$$D_i = 0 : \quad y_i = \beta_0 + \beta_1 x_i + u_i$$

$$D_i = 1 : \quad y_i = (\beta_0 + \beta_2) + (\beta_1 + \beta_3) x_i + u_i$$

The dummy variable trap is **not** triggered here: $D$ is not perfectly collinear with $Dx$ because $x$ is continuous and varies.

### Interpretation

- $\beta_2$: difference in intercepts between the two groups (intercept shift).
- $\beta_3$: difference in slopes between the two groups (slope shift).
- A wage-education example (Wooldridge):

$$\text{wage} = \beta_0 + \delta_0 \, \text{female} + \beta_1 \, \text{educ} + \delta_1 (\text{female} \cdot \text{educ}) + u$$

If $\delta_0 < 0$ and $\delta_1 < 0$, women have both a lower starting wage and a lower return to education. If $\delta_0 < 0$ and $\delta_1 > 0$, women start lower but catch up faster with education.

### Joint significance

Both the individual coefficients ($\beta_2$, $\beta_3$) and their joint significance ($H_0: \beta_2 = 0$ and $\beta_3 = 0$) can be tested using the standard $t$ and $F$ tests. High sample correlation between $D$ and $Dx$ may inflate standard errors (a form of multicollinearity).

---

## Chow Test for Differences Between Groups

### Motivation

The **Chow test** (Gregory Chow, 1960) is an $F$-based test of whether the underlying population regression model is **identical** across two subpopulations. It formalises the question: "Are all regression coefficients — intercept and slopes — the same in both groups?"

### Setup

Consider a population model with $k$ regressors ($k = 1$ for exposition):

$$y = \beta_0 + \beta_1 x + u$$

Define a binary indicator $D_i$ (0 for group 1, 1 for group 2). Extend to the **unrestricted model**:

$$y_i = \beta_0 + \delta_0 D_i + \beta_1 x_i + \delta_1 D_i x_i + u_i \tag{1}$$

The null hypothesis of **parameter stability** across groups:

$$H_0: \delta_0 = 0 \text{ and } \delta_1 = 0 \qquad \text{vs.} \qquad H_1: \delta_0 \neq 0 \text{ or } \delta_1 \neq 0$$

### Chow statistic

Let:
- $\text{SSR}_1$, $\text{SSR}_2$: residual sums of squares from separate OLS regressions on each sub-sample.
- $\text{SSR}_U = \text{SSR}_1 + \text{SSR}_2$: unrestricted residual sum of squares (algebraic identity).
- $\text{SSR}_P$: residual sum of squares from OLS on the **pooled** sample (restricted model, imposing $H_0$).

The Chow statistic:

$$\boxed{F = \frac{\text{SSR}_P - (\text{SSR}_1 + \text{SSR}_2)}{\text{SSR}_1 + \text{SSR}_2} \cdot \frac{n - 2(k+1)}{k+1}}$$

Under $H_0$ and homoskedasticity (MLR.5), $F \sim F_{k+1,\; n-2(k+1)}$.

### Alternative (less strict) Chow test

The classical Chow test restricts **all** parameters. A softer version allows the intercept to differ (keeps $\delta_0$ free) and tests only slope equality:

$$F^* = \frac{\text{SSR}^*_P - (\text{SSR}_1 + \text{SSR}_2)}{\text{SSR}_1 + \text{SSR}_2} \cdot \frac{n - 2(k+1)}{k}$$

where $\text{SSR}^*_P$ comes from the restricted model that already includes an intercept dummy. Under $H_0$, $F^* \sim F_{k,\; n-2(k+1)}$.

### Assumptions and caveats

- Both the standard $F$ distribution and asymptotics require **MLR.1–MLR.4**. Normality (MLR.6) gives an exact $F$ distribution; without it the test is asymptotically valid.
- The Chow test assumes **homoskedasticity** across both groups. If variances differ, robust or group-specific standard errors are preferable.
- The test does not identify *which* parameter differs — only whether any does.

### Relationship to the slope-dummy specification

Estimating the interacted model (1) by OLS is equivalent to running separate regressions on each sub-sample. The Chow $F$ statistic therefore corresponds to the joint $F$ test of $H_0: \delta_0 = 0, \delta_1 = 0$ in model (1).

---

## Summary

| Tool | What it tests | Output |
|---|---|---|
| Interaction term $D \cdot x$ | Whether slope differs across groups | $t$-stat on $\beta_3$ |
| Joint $F$-test (intercept + slope dummy) | Whether *any* parameter differs | $F \sim F_{2, n-k-1}$ |
| Chow test | Full parameter equality across sub-samples | $F \sim F_{k+1, n-2(k+1)}$ |
