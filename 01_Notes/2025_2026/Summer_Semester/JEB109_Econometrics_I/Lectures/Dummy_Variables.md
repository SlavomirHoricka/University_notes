---
course: "JEB109"
topic: "Dummy Variables and Qualitative Information"
source: "00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_08_JEB109_2026.pdf"
tags: [JEB109, econometrics, dummy-variables, intercept-dummy, slope-dummy, qualitative, LPM]
created: 2026-04-19
---

Parent: [[JEB109_Econometrics_I_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_08_JEB109_2026.pdf]]
Related: [[Functional_Forms_and_Model_Comparison]], [[MLR_Assumptions_and_OLS_Unbiasedness]], [[F_Test_and_Multiple_Restrictions]]

# Dummy Variables and Qualitative Information

## Representing Qualitative Information

Many economically important variables are **binary** (yes/no, employed/unemployed, male/female) or **categorical** (education level, region, industry). These cannot be entered directly as continuous regressors; instead, we construct **dummy (binary / zero-one) variables**.

A dummy variable $D$ takes values:
- $D_i = 1$ if the unit belongs to a particular group,
- $D_i = 0$ otherwise.

---

## Single Intercept Dummy

Include a single dummy $D$ alongside continuous regressors:

$$y = \beta_0 + \beta_1 x_1 + \cdots + \beta_{k-1}x_{k-1} + \beta_k D + u.$$

This yields **two parallel regression functions** with different intercepts:

$$D_i = 0:\quad E(y \mid \mathbf{x}, D=0) = \beta_0 + \beta_1 x_1 + \cdots + \beta_{k-1}x_{k-1},$$
$$D_i = 1:\quad E(y \mid \mathbf{x}, D=1) = (\beta_0 + \beta_k) + \beta_1 x_1 + \cdots + \beta_{k-1}x_{k-1}.$$

The slopes $\beta_1, \ldots, \beta_{k-1}$ are **assumed identical** across groups (only the intercept shifts). This type is called an **intercept dummy**.

**Interpretation of $\beta_k$:** The ceteris paribus difference in $y$ between the group $D=1$ and the base group $D=0$, after controlling for all other regressors.

---

## Dummy Variables with Logarithms (Semi-Elasticity)

$$\log(y) = \beta_0 + \beta_1 x_1 + \cdots + \beta_k D + u.$$

Interpretation: holding other factors fixed, $y$ is approximately $100\beta_k\%$ higher for group $D=1$ compared to $D=0$. This is a **semi-elasticity** interpretation.

**Exact percentage difference:**

$$\%\Delta y \approx 100\bigl(\exp(\hat\beta_k) - 1\bigr),$$

which corrects for the approximation error when $|\hat\beta_k|$ is not small.

---

## The Dummy Variable Trap

When representing a categorical variable with $m$ mutually exclusive groups, create **$m-1$ dummy variables** (one for each group except the **base / benchmark group**).

**Why?** Including all $m$ dummies alongside the intercept violates **MLR.3 (no perfect collinearity)**, since the sum of all group dummies equals the intercept column of $\mathbf{X}$:

$$D_1 + D_2 + \cdots + D_m \equiv \mathbf{1}_n \quad \text{(the intercept column)}.$$

This makes $\mathbf{X}^T\mathbf{X}$ singular — the **dummy variable trap**.

**Solution:** Drop one group (the base group). Its effect is captured by $\beta_0$. The coefficients on the included dummies measure the difference relative to the base group.

---

## Multiple Categories

For two characteristics (e.g., employment $E$ and citizenship $C$), two approaches:

### Approach 1: Separate Dummies
$$\text{income} = \beta_0 + \beta_1 E + \beta_2 C + u.$$
Implies: employed citizens $= \beta_0 + \beta_1 + \beta_2$; unemployed foreigners $= \beta_0$.

**Restriction:** the employment premium $\beta_1$ is the same for citizens and foreigners. This may or may not be justified.

### Approach 2: Interaction-Based Group Dummies
Construct a dummy for each cell of the two-way table:

| Group | Employed Citizen (EC) | Unemployed Citizen (UC) | Employed Foreigner (EF) | Unemployed Foreigner (UF) |
|-------|-----------------------|-------------------------|-------------------------|---------------------------|
| Model | base group | separate dummy | separate dummy | separate dummy |

$$\text{income} = \gamma_0 + \gamma_1\,\text{UC} + \gamma_2\,\text{EF} + \gamma_3\,\text{UF} + v.$$

This imposes no restrictions on the group differences and allows easy testing of any pairwise comparison via $t$ tests.

---

## Ordinal Information

For an ordinal variable $Q \in \{0, 1, 2, 3\}$, two models:

**Model I (Cardinal treatment):**
$$y = \beta_0 + \beta_1 x + \beta_k Q + u.$$
Assumes equal-interval increments: going from $Q=0$ to $Q=1$ has the same effect as from $Q=2$ to $Q=3$.

**Model II (Full dummy decomposition):**
$$y = \beta_0 + \beta_1 x + \beta_{k-2} D_1 + \beta_{k-1} D_2 + \beta_k D_3 + u,$$
where $D_j = \mathbf{1}(Q = j)$ and $D_0$ is the base (omitted). This is more flexible but uses more degrees of freedom.

**Which to choose?** Defaults to Model I when the ordinal scale is plausibly cardinal; use Model II when the increments are heterogeneous or one wants to test for patterning.

---

## Variable Selection and Prediction

### Selection of Independent Variables

The choice of regressors should be guided by:
1. **Economic theory** — which variables have a causal argument?
2. **Avoiding OVB** — do not omit variables correlated with included regressors and $y$ (see [[Omitted_Variable_Bias]]).
3. **Parsimony** — avoid overspecification that costs precision (see [[Variance_of_OLS_Estimator]]).
4. **$\bar R^2$** — for comparing nested models with the same $y$ (see [[Functional_Forms_and_Model_Comparison]]).

### Predicting $E(y \mid \mathbf{x}^0)$ vs. Predicting $y^0$

**Conditional mean prediction** at $\mathbf{x}^0$:

$$\hat\theta = \hat\beta_0 + \hat\beta_1 x_1^0 + \cdots + \hat\beta_k x_k^0.$$

The $\text{se}(\hat\theta)$ comes entirely from the uncertainty in $\hat{\boldsymbol\beta}$ and gives the CI for $E(y \mid \mathbf{x}^0)$.

**Individual prediction** of $y^0 = \mathbf{x}^{0T}\boldsymbol\beta + u^0$:

The **prediction error** $\hat e^0 = y^0 - \hat y^0$ has variance:

$$\text{Var}(\hat e^0) = \sigma^2 + \text{Var}(\hat y^0),$$

giving:

$$\text{se}(\hat e^0) = \sqrt{\hat\sigma^2 + \text{Var}(\hat y^0)}.$$

A **prediction interval** for $y^0$ is wider than the CI for $E(y \mid \mathbf{x}^0)$ because it also accounts for the irreducible variance $\sigma^2$ of the individual error $u^0$.

---

## Uses of Residuals

OLS residuals $\hat u_i$ are not merely estimates of the error. Applications:
- **Investment:** over/under-valued stocks — positive $\hat u_i$ for a stock means its price exceeds the model's prediction (conditional on fundamentals).
- **Discrimination cases:** residuals from a wage regression reveal unexplained pay gaps after controlling for productivity-related characteristics.
- **Specification testing:** non-random patterns in residuals signal model misspecification.
