---
course: "JEB109"
topic: "Linear Probability Model (LPM)"
source: "00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_09_JEB109_2026.pdf"
tags: [JEB109, econometrics, LPM, binary-dependent-variable, probability-model, heteroskedasticity]
created: 2026-04-28
---

Parent: [[JEB109_Econometrics_I_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_09_JEB109_2026.pdf]]
Related: [[Dummy_Variables]], [[Dummy_Variable_Interactions_and_Chow_Test]], [[MLR_Assumptions_and_OLS_Unbiasedness]], [[Gauss_Markov_Theorem]], [[Heteroskedasticity]]

---

# Linear Probability Model (LPM)

## Binary Dependent Variables

Until Lecture 8, qualitative (dummy) variables appeared only as **regressors**. Many economically interesting outcomes are themselves binary: loan approval, labour-force participation, home ownership, programme take-up. The binary dependent variable $y \in \{0, 1\}$ requires a reinterpretation of the standard regression framework.

The population model has the same algebraic form as a standard MLR:

$$y = \beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k + u$$

but now $y$ is a **Bernoulli** random variable:

$$y = \begin{cases} 1 & \text{with probability } P \\ 0 & \text{with probability } 1 - P \end{cases}$$

---

## Assumptions

### Expected value

Under **MLR.1–MLR.4**, OLS remains unbiased and consistent. The conditional expectation is:

$$\mathbb{E}(y \mid \mathbf{X}) = \beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k$$

Because $\mathbb{E}(y \mid \mathbf{X}) = 1 \cdot P(y=1 \mid \mathbf{X}) + 0 \cdot (1 - P(y=1 \mid \mathbf{X}))$, we obtain the key identity:

$$\boxed{\mathbb{E}(y \mid \mathbf{X}) = P(y = 1 \mid \mathbf{X})}$$

The conditional mean of $y$ equals the **probability of success** (the event $y = 1$) given the regressors.

---

## The Linear Probability Model

Exploiting the identity above, the probability of success is modelled as a linear function of the regressors:

$$p(\mathbf{X}) \equiv P(y = 1 \mid \mathbf{X}) = \mathbb{E}(y \mid \mathbf{X}) = \beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k$$

This is the **Linear Probability Model (LPM)**. Because both $P(y=1 \mid \mathbf{X})$ and $P(y=0 \mid \mathbf{X}) = 1 - p(\mathbf{X})$ are linear in the $\beta_j$, the model receives its name from this linearity.

### Interpretation of coefficients

$$\Delta p(\mathbf{X}) = \Delta P(y = 1 \mid \mathbf{X}) = \beta_j \cdot \Delta x_j$$

Each $\beta_j$ is the **change in the probability of success** when $x_j$ increases by one unit, holding all other regressors constant. The fitted value $\hat{y}_i$ is interpreted as the **predicted probability of success** for observation $i$.

Dummy variables can be included among the regressors in the usual way; their $\beta_j$ measures the probability differential between the group indicated by $D = 1$ and the base group.

---

## Shortcomings of the LPM

### 1. Unbounded predicted probabilities

The linear specification does not constrain $\hat{y}$ to $[0,1]$. For extreme values of $x_j$, the LPM can predict probabilities below 0 or above 1 — a logical impossibility.

**Partial remedies:**
- **Censoring**: replace predicted values outside $[0,1]$ by $0$ or $1$. Risk: too many exact predictions of 0% and 100%.
- **Thresholding**: classify $\hat{y} > c$ as $y = 1$. Risk: the threshold $c$ is arbitrary and data-dependent.

Both remedies are ad hoc; the structural fix is to use a logit or probit model (beyond the scope of JEB109).

### 2. Constant marginal effect

The LPM imposes a **constant** partial effect $\partial p / \partial x_j = \beta_j$ everywhere in the covariate space. In reality, the probability response is typically S-shaped — large in the middle of the distribution and small near the boundaries — so a constant slope is often unrealistic.

### 3. Inherent heteroskedasticity

Because $y$ is Bernoulli, the error variance is:

$$\text{Var}(u \mid \mathbf{X}) = \text{Var}(y \mid \mathbf{X}) = \mathbb{E}(y^2 \mid \mathbf{X}) - \left[\mathbb{E}(y \mid \mathbf{X})\right]^2$$

$$= 1^2 \cdot p(\mathbf{X}) + 0^2 \cdot (1 - p(\mathbf{X})) - [p(\mathbf{X})]^2 = \boxed{p(\mathbf{X})\bigl(1 - p(\mathbf{X})\bigr)}$$

The variance depends on the regressors, so **MLR.5 (homoskedasticity) is always violated** in a correctly specified LPM. Consequences:

- OLS remains **unbiased and consistent** (MLR.1–4 still hold).
- OLS is **no longer BLUE** (efficiency is lost; [[Gauss_Markov_Theorem]] fails).
- The standard $t$ and $F$ statistics are **invalid even asymptotically** without a heteroskedasticity correction (see [[Heteroskedasticity]]).

The known variance form $\hat{h}_i = \hat{y}_i (1 - \hat{y}_i)$ can be used as weights in a WLS (feasible GLS) correction — see [[Heteroskedasticity]].

### 4. Non-normal error term

Since $y \in \{0,1\}$, for given $\mathbf{X}$ the error $u$ takes only two values:

$$u = \begin{cases} 1 - p(\mathbf{X}) & \text{if } y = 1 \\ -p(\mathbf{X}) & \text{if } y = 0 \end{cases}$$

MLR.6 (normality) is violated by construction. This invalidates exact finite-sample $t$ and $F$ distributions; asymptotic approximations must be used.

---

## Advantages and Practical Use

Despite its shortcomings, the LPM is widely used in applied economics:

1. **Simple estimation**: OLS is unbiased and consistent; standard software applies directly.
2. **Straightforward interpretation**: $\beta_j$ is a probability change — directly interpretable without marginal-effects calculations.
3. **Fixable inference**: heteroskedasticity and non-normality can be corrected via heteroskedasticity-robust standard errors (see [[Heteroskedasticity]]).
4. **Reasonable fit near the mean**: for $x_j$ values close to the sample averages, the LPM approximates non-linear models well.

**Caution on $R^2$ and $\bar{R}^2$**: these are no longer meaningful goodness-of-fit measures for the LPM because $y$ is binary; a correct-prediction rate or pseudo-$R^2$ should be used instead.

---

## WLS Correction for the LPM

Because the heteroskedasticity form is **known** — $\text{Var}(u \mid \mathbf{X}) = p(\mathbf{X})(1-p(\mathbf{X}))$ — it can be estimated observation-by-observation once the OLS fitted values $\hat{y}_i$ are available:

$$\hat{h}_i = \hat{y}_i (1 - \hat{y}_i)$$

WLS then weights each observation by $1/\sqrt{\hat{h}_i}$. Two practical difficulties:

- Predicted probabilities outside $(0,1)$ produce negative or undefined weights; censoring to a small interval (e.g., $[0.01, 0.99]$) is the usual fix.
- Even after WLS, **robust standard errors are recommended** because the weights are estimated (not known) and other forms of misspecification may remain.

---

## Summary Table

| Issue | Consequence | Remedy |
|---|---|---|
| Predicted $\hat{y} \notin [0,1]$ | Logical impossibility | Logit/probit; censoring |
| Constant marginal effect | Unrealistic for extremes | Logit/probit |
| Inherent heteroskedasticity | Invalid $t$/$F$ statistics | Robust SEs; WLS |
| Non-normal errors | No exact small-sample distributions | Asymptotic justification |
