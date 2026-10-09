---
course: "JEB109"
topic: "Multiple Linear Regression — Assumptions and OLS Unbiasedness"
source: "00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_03_JEB109_2026-1.pdf"
tags: [JEB109, econometrics, MLR, OLS, unbiasedness, matrix-algebra, omitted-variable-bias]
created: 2026-04-19
---

Parent: [[JEB109_Econometrics_I_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_03_JEB109_2026-1.pdf]]
Related: [[Simple_Linear_Regression]], [[OLS_Estimator_Simple_Regression]], [[Variance_of_OLS_Estimator]], [[Omitted_Variable_Bias]], [[Gauss_Markov_Theorem]]

# Multiple Linear Regression (MLR) — Assumptions and OLS Unbiasedness

## The General MLR Model

The **multiple linear regression (MLR)** model with $k$ regressors:

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_k x_k + u,$$

where $\beta_0$ is the intercept and $\beta_1, \ldots, \beta_k$ are the slope coefficients. The inclusion of $\beta_0$ implies $E(u) = 0$.

### Matrix Notation

Stacking $n$ observations:

$$\mathbf{Y} = \mathbf{X}\boldsymbol\beta + \mathbf{u},$$

where:

$$\mathbf{Y} = \begin{pmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{pmatrix}, \quad \mathbf{X} = \begin{pmatrix} 1 & x_{11} & \cdots & x_{1k} \\ 1 & x_{21} & \cdots & x_{2k} \\ \vdots & \vdots & \ddots & \vdots \\ 1 & x_{n1} & \cdots & x_{nk} \end{pmatrix}, \quad \boldsymbol\beta = \begin{pmatrix} \beta_0 \\ \beta_1 \\ \vdots \\ \beta_k \end{pmatrix}, \quad \mathbf{u} = \begin{pmatrix} u_1 \\ u_2 \\ \vdots \\ u_n \end{pmatrix}.$$

Dimensions: $\mathbf{Y}_{n\times 1}$, $\mathbf{X}_{n\times(k+1)}$, $\boldsymbol\beta_{(k+1)\times 1}$, $\mathbf{u}_{n\times 1}$.

---

## MLR Assumptions (MLR.1 – MLR.4 for Unbiasedness)

| Assumption | Statement |
|-----------|-----------|
| **MLR.1** Linear in parameters | Population model $y = \beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k + u$ |
| **MLR.2** Random sampling | i.i.d. random sample $\{(y_i, \mathbf{x}_i)\}_{i=1}^n$ from the population |
| **MLR.3** No perfect collinearity | $\mathbf{X}$ has full column rank ($k+1$); none of the $x_j$'s is constant or an exact linear function of others |
| **MLR.4** Zero conditional mean | $E(u \mid x_1, \ldots, x_k) = 0$, implying $\text{Cov}(x_j, u) = 0$ for all $j$ |

MLR.3 is essential: if $\mathbf{X}$ is rank-deficient, $(\mathbf{X}^T\mathbf{X})^{-1}$ does not exist and OLS cannot be computed uniquely. This arises with **perfect multicollinearity** (e.g., dummy variable trap).

---

## OLS Estimator in Matrix Form

### Minimizing SSR

Define the residual vector $\hat{\mathbf{u}} = \mathbf{Y} - \mathbf{X}\hat{\boldsymbol\beta}$. The SSR in matrix form:

$$\text{SSR} = \hat{\mathbf{u}}^T \hat{\mathbf{u}} = (\mathbf{Y} - \mathbf{X}\hat{\boldsymbol\beta})^T(\mathbf{Y} - \mathbf{X}\hat{\boldsymbol\beta}).$$

Expanding and applying matrix differentiation rules:

$$\frac{\partial\,\hat{\mathbf{u}}^T\hat{\mathbf{u}}}{\partial\,\hat{\boldsymbol\beta}} = 0 \implies -2\mathbf{X}^T\mathbf{Y} + 2\mathbf{X}^T\mathbf{X}\hat{\boldsymbol\beta} = 0.$$

Solving (using MLR.3 to ensure $\mathbf{X}^T\mathbf{X}$ is invertible):

$$\boxed{\hat{\boldsymbol\beta}^{\text{OLS}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}.}$$

This is the **matrix OLS formula**. In the SLR case ($k=1$) it reduces to the slope formula derived in [[OLS_Estimator_Simple_Regression]].

---

## Interpretation of OLS Estimates

- $\hat\beta_0$: predicted value of $y$ when $x_1 = \cdots = x_k = 0$.
- $\hat\beta_j$ ($j \geq 1$): **partial effect** — expected change in $y$ per unit increase in $x_j$, *holding all other regressors fixed*.

From the SRF: $\Delta\hat y = \hat\beta_1\Delta x_1 + \cdots + \hat\beta_k\Delta x_k$, so

$$\hat\beta_j = \frac{\Delta\hat y}{\Delta x_j}\Bigg|_{x_{\ell\neq j}\ \text{fixed}}.$$

The ceteris paribus interpretation holds even for **observational/non-experimental** data — this is the power of multiple regression.

---

## Unbiasedness of OLS

**Theorem** (Unbiasedness under MLR.1–MLR.4): $E(\hat{\boldsymbol\beta}^{\text{OLS}}) = \boldsymbol\beta$.

**Proof:**

Substitute $\mathbf{Y} = \mathbf{X}\boldsymbol\beta + \mathbf{u}$ into the OLS formula:

$$\hat{\boldsymbol\beta} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T(\mathbf{X}\boldsymbol\beta + \mathbf{u}) = \boldsymbol\beta + (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{u}.$$

Taking expectations (conditioning on $\mathbf{X}$ and using MLR.4 $E(\mathbf{u} \mid \mathbf{X}) = \mathbf{0}$):

$$E(\hat{\boldsymbol\beta} \mid \mathbf{X}) = \boldsymbol\beta + (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\underbrace{E(\mathbf{u} \mid \mathbf{X})}_{= \mathbf{0}} = \boldsymbol\beta. \quad \blacksquare$$

By the Law of Iterated Expectations: $E(\hat{\boldsymbol\beta}) = E_{\mathbf{X}}[E(\hat{\boldsymbol\beta} \mid \mathbf{X})] = \boldsymbol\beta$.

---

## Model Misspecification

### Overspecification (Including Irrelevant Variables)

If a variable $x_j$ with true coefficient $\beta_j = 0$ is included, OLS remains **unbiased** — the irrelevant variable simply has expected coefficient zero. The cost is **increased variance** (see [[Variance_of_OLS_Estimator]]).

### Underspecification (Omitting Relevant Variables)

This is the major threat. See [[Omitted_Variable_Bias]] for the formal analysis. The intuition: an omitted variable $x_2$ (with true $\beta_2 \neq 0$) that is correlated with the included $x_1$ contaminates $\hat\beta_1$:

$$E(\hat\beta_1) = \beta_1 + \beta_2 \cdot \frac{\sum(x_{i2} - \bar x_2)(x_{i1} - \bar x_1)}{\sum(x_{i1} - \bar x_1)^2} \neq \beta_1.$$

The direction of the bias depends on the sign of $\beta_2$ and the sign of $\text{Corr}(x_1, x_2)$.
