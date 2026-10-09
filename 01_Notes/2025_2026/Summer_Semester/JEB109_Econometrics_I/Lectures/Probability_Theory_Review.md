---
course: "JEB109"
topic: "Probability Theory Review"
source: "00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_01_JEB109_2026-1.pdf"
tags: [JEB109, econometrics, statistics, probability, distributions, LLN, CLT]
created: 2026-04-19
---

Parent: [[JEB109_Econometrics_I_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_01_JEB109_2026-1.pdf]]
Related: [[Introduction_to_Econometrics]], [[OLS_Estimator_Simple_Regression]], [[Gauss_Markov_Theorem]]

# Probability Theory Review for Econometrics

This note consolidates the prerequisite statistical knowledge required for JEB109. For fuller treatment see [[Central_Limit_Theorem]] (JEB105).

---

## 1. Random Variables and Distribution Functions

A **random variable** $X$ maps outcomes from a sample space to the real line. For any random variable $X$, the **cumulative distribution function (CDF)** is:

$$F_X(x) = P(X \leq x), \quad x \in \mathbb{R}.$$

Properties of $F_X$:
- Non-decreasing,
- $\lim_{x \to -\infty} F_X(x) = 0$,
- $\lim_{x \to +\infty} F_X(x) = 1$.

For a **continuous** random variable, the **probability density function (PDF)** $f_X(x)$ satisfies:

$$F_X(x) = \int_{-\infty}^{x} f_X(t)\, dt.$$

---

## 2. Moments of a Distribution

### Expected Value (Mean)

$$E(X) = \int_{-\infty}^{+\infty} x\, f_X(x)\, dx.$$

Key properties:
- $E(X + c) = E(X) + c$,
- $E(cX) = cE(X)$,
- $E(X + Y) = E(X) + E(Y)$,
- **Law of Iterated Expectations (LIE):** $E(Y) = E\bigl(E(Y \mid X)\bigr)$.

The LIE is foundational in econometrics: it allows the decomposition of conditional and unconditional expectations.

### Variance

$$\text{Var}(X) = E\bigl(X - E(X)\bigr)^2 = E(X^2) - \bigl(E(X)\bigr)^2.$$

Properties:
- $\text{Var}(X) \geq 0$,
- $\text{Var}(b) = 0$ for constant $b$,
- $\text{Var}(aX + b) = a^2 \text{Var}(X)$.

The **standard deviation** $\sigma = \sqrt{\text{Var}(X)}$ is in the same units as $X$.

### Covariance

$$\text{Cov}(X, Y) = E(XY) - E(X)E(Y).$$

Variance of a linear combination:

$$\text{Var}\!\left(\sum_{i=1}^n a_i X_i + b\right) = \sum_{i=1}^n a_i^2\, \text{Var}(X_i) + 2\sum_{i<j} a_i a_j\, \text{Cov}(X_i, X_j).$$

For pairwise uncorrelated variables: $\text{Var}\!\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{Var}(X_i)$ and $\text{Var}(\bar{X}_n) = \sigma^2/n$.

### Correlation Coefficient

$$\text{Corr}(X, Y) = \rho_{X,Y} = \frac{\text{Cov}(X, Y)}{\sqrt{\text{Var}(X)\,\text{Var}(Y)}}, \quad -1 \leq \rho_{X,Y} \leq 1.$$

---

## 3. Key Distributions in Econometrics

### Normal (Gaussian) Distribution

$X \sim N(\mu, \sigma^2)$ with PDF:

$$f_X(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(x - \mu)^2}{2\sigma^2}\right), \quad x \in \mathbb{R}.$$

$E(X) = \mu$, $\text{Var}(X) = \sigma^2$. The standard normal $N(0,1)$ has important quantiles:

| $\alpha$ | $z_{1-\alpha}$ |
|----------|----------------|
| 10% | 1.282 |
| 5% | 1.645 |
| 2.5% | 1.960 |
| 1% | 2.326 |
| 0.5% | 2.576 |

The "two-sigma rule": $\Phi(1.96) \approx 0.975$, so $\pm 1.96$ covers 95% of the standard normal distribution.

### Chi-Squared Distribution

If $Z_1, \ldots, Z_m \overset{\text{i.i.d.}}{\sim} N(0, 1)$, then:

$$X = Z_1^2 + \cdots + Z_m^2 \sim \chi^2_m.$$

$E(X) = m$, $\text{Var}(X) = 2m$. Chi-squared distributions are additive: if $X_i \sim \chi^2_{m_i}$ independently, then $\sum_i X_i \sim \chi^2_{\sum_i m_i}$.

### Student's $t$ Distribution

If $Z \sim N(0,1)$ and $X \sim \chi^2_m$ independently:

$$T = \frac{Z}{\sqrt{X/m}} \sim t_m.$$

For large $m$: $t_m \xrightarrow{d} N(0,1)$. Critical: for $m > 120$, $t_m \approx N(0,1)$ in practice. The $t$ distribution arises naturally in OLS inference when $\sigma^2$ is estimated.

### $F$ Distribution (Fisher-Snedecor)

If $X_1 \sim \chi^2_{m_1}$ and $X_2 \sim \chi^2_{m_2}$ independently:

$$F = \frac{X_1/m_1}{X_2/m_2} \sim F_{m_1, m_2}.$$

The $F$ distribution is used for joint hypothesis tests (F tests) and is related to the $t$ distribution: $t_m^2 \sim F_{1,m}$.

---

## 4. Law of Large Numbers (LLN)

**Weak LLN:** Let $X_1, X_2, \ldots$ be i.i.d. with mean $\mu$ and finite variance. Then:

$$\text{plim}_{n \to \infty}\, \bar{X}_n = \mu,$$

i.e., for all $\varepsilon > 0$:

$$\lim_{n \to \infty} P\!\left(|\bar{X}_n - \mu| > \varepsilon\right) = 0.$$

**Intuition:** With enough data, the sample mean converges in probability to the population mean. This justifies using sample moments to estimate population moments (method of moments).

---

## 5. Central Limit Theorem (CLT)

Let $X_1, X_2, \ldots$ be i.i.d. with mean $\mu$ and finite variance $\sigma^2 > 0$. Then:

$$\frac{\sqrt{n}(\bar{X}_n - \mu)}{\sigma} \xrightarrow{d} N(0, 1) \quad \text{as } n \to \infty.$$

**Econometric importance:** The CLT underpins asymptotic inference. Even if the error term $u$ is not normally distributed, the OLS estimator $\hat\beta_j$ is asymptotically normal under the Gauss-Markov assumptions (MLR.1–MLR.5), enabling valid inference in large samples without MLR.6 normality.

---

## 6. Hypothesis Testing Framework

The classical framework:

1. State $H_0$ (null hypothesis) and $H_1$ (alternative hypothesis).
2. Choose a significance level $\alpha$ (Type I error probability): typically 1%, 5%, or 10%.
3. Compute a **test statistic** whose sampling distribution under $H_0$ is known.
4. **Reject** $H_0$ if the test statistic falls in the critical region (or equivalently if p-value $< \alpha$).

**Type I error:** Reject $H_0$ when it is true. Probability = $\alpha$.  
**Type II error:** Fail to reject $H_0$ when it is false. Probability = $\beta$.  
**Power** = $1 - \beta = P(\text{reject } H_0 \mid H_1 \text{ true})$.

Key distinction: "not rejecting" $H_0$ is **not** the same as "accepting" $H_0$.
