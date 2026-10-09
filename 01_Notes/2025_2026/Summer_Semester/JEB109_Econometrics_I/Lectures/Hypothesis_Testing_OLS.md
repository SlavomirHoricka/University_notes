---
course: "JEB109"
topic: "Hypothesis Testing in OLS — t-test, Confidence Intervals, Linear Combinations"
source: "00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_05_JEB109_2026.pdf"
tags: [JEB109, econometrics, hypothesis-testing, t-test, confidence-interval, p-value, inference]
created: 2026-04-19
---

Parent: [[JEB109_Econometrics_I_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_05_JEB109_2026.pdf]]
Related: [[Gauss_Markov_Theorem]], [[Variance_of_OLS_Estimator]], [[F_Test_and_Multiple_Restrictions]], [[OLS_Consistency_and_Asymptotics]]

# Hypothesis Testing in OLS — t-test and Confidence Intervals

## Sampling Distribution of $\hat\beta_j$

Under the full CLM assumptions (MLR.1–MLR.6):

$$\frac{\hat\beta_j - \beta_j}{\text{se}(\hat\beta_j)} \sim t_{n-k-1},$$

where $n - k - 1$ are the degrees of freedom. This is the **exact** finite-sample distribution.

Under MLR.1–MLR.5 only (without normality of $u$):

$$\frac{\hat\beta_j - \beta_j}{\text{se}(\hat\beta_j)} \overset{a}{\sim} N(0,1) \approx t_{n-k-1} \quad \text{for large } n.$$

---

## The $t$ Ratio (Two-Sided Test for $\beta_j = 0$)

The most common test is $H_0{:}\ \beta_j = 0$ vs. $H_1{:}\ \beta_j \neq 0$. Define the **$t$ ratio**:

$$t_{\hat\beta_j} \equiv \frac{\hat\beta_j}{\text{se}(\hat\beta_j)}.$$

Under $H_0$: $t_{\hat\beta_j} \sim t_{n-k-1}$.

**Decision rule (two-sided):**
- Reject $H_0$ at significance level $\alpha$ if $|t_{\hat\beta_j}| > c_{\alpha/2}$, where $c_{\alpha/2}$ is the $(1 - \alpha/2)$ quantile of $t_{n-k-1}$.
- For $n - k - 1 > 120$: use $c_{0.025} \approx 1.96$ (the "2-sigma rule" for $\alpha = 5\%$).

**One-sided alternatives:**
- $H_1{:}\ \beta_j > 0$: reject if $t_{\hat\beta_j} > c_\alpha$.
- $H_1{:}\ \beta_j < 0$: reject if $t_{\hat\beta_j} < -c_\alpha$.

---

## Generalised $t$ Statistic

For a general null $H_0{:}\ \beta_j = a_j$:

$$t_{\hat\beta_j} \equiv \frac{\hat\beta_j - a_j}{\text{se}(\hat\beta_j)} \sim t_{n-k-1} \quad \text{under } H_0.$$

**Applications:**
- Testing a unit elasticity: $H_0{:}\ \beta_j = 1$ in a log-log model.
- Testing the efficient markets hypothesis: $H_0{:}\ \alpha_i = 0,\, \beta_i = 1$ in the CAPM regression $r_{i,t} - r_{f,t} = \alpha_i + \beta_i(r_{M,t} - r_{f,t}) + u_{i,t}$.

---

## The $p$-Value

The **$p$-value** is the probability of observing a test statistic at least as extreme as the computed value, under $H_0$:

$$p\text{-value} = P\!\left(|T| \geq |t_{\hat\beta_j}|\bigm| H_0\right) = 2\cdot P\!\left(T \geq |t_{\hat\beta_j}|\right)$$

for a two-sided test, where $T \sim t_{n-k-1}$.

**Interpretation:** A small $p$-value (e.g., $< 0.05$) means the observed data are unlikely under $H_0$. We reject $H_0$ when $p\text{-value} < \alpha$.

**Critical:** "not rejecting $H_0$" is **not** the same as "accepting $H_0$".

---

## Economic vs. Statistical Significance

A result can be **statistically significant** (small $p$-value) but **economically trivial** (tiny effect size), especially in large samples. Conversely, with small $n$, a practically important coefficient may be imprecisely estimated and thus statistically insignificant.

**Recommended practice:**
1. Check statistical significance first; if significant, assess economic/practical magnitude.
2. Even if not significant, examine the actual $p$-value and effect size — the evidence may be close to significant.
3. Always consider whether bias is a concern (see [[Omitted_Variable_Bias]]).

---

## Confidence Interval for $\beta_j$

Under MLR.1–MLR.6, a **$(1-\alpha)$ confidence interval** for $\beta_j$:

$$\hat\beta_j \pm t_{n-k-1,\, 1-\alpha/2}\cdot \text{se}(\hat\beta_j).$$

For $n - k - 1 > 120$ and $\alpha = 5\%$: $\hat\beta_j \pm 1.96\cdot\text{se}(\hat\beta_j)$.

**Interpretation:** If the sampling procedure were repeated many times, $(1-\alpha) \times 100\%$ of the constructed intervals would contain the true $\beta_j$. A single realized interval either does or does not contain $\beta_j$.

---

## Testing a Linear Combination of Parameters

Sometimes the hypothesis of interest involves *multiple* coefficients. Example:

$$H_0{:}\ \beta_1 = \beta_2 \iff H_0{:}\ \beta_1 - \beta_2 = 0.$$

Define $\theta \equiv \beta_1 - \beta_2$. We cannot directly compute $\text{se}(\hat\beta_1 - \hat\beta_2)$ from individual standard errors alone without the covariance term.

### Reparameterisation Trick

Substitute $\beta_1 = \theta + \beta_2$ into the model:

$$y = \beta_0 + (\theta + \beta_2)x_1 + \beta_2 x_2 + u = \beta_0 + \theta x_1 + \beta_2(x_1 + x_2) + u.$$

Estimate this reparameterised model by OLS and test $H_0{:}\ \theta = 0$ using a standard $t$ test. The standard error of $\hat\theta$ is directly reported by OLS software.

**Catch:** The reparameterisation must be algebraically correct, so $\hat\beta_2$ and $\hat\theta$ from the new model can be used to recover the original parameters exactly.

---

## Historical Note: William Sealy Gosset (1876–1937)

The $t$ distribution was derived by Gosset while working as a statistician at Guinness brewery in Dublin. Small sample sizes in beer quality experiments forced him beyond Gaussian large-sample methods. He published under the pseudonym "Student" (Guinness prohibited staff from publishing under their own names), giving rise to "Student's $t$ distribution." His 1908 paper established the framework for small-sample inference that is central to econometrics.
