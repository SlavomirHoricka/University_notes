---
course: "JEB109"
topic: "OLS Consistency and Asymptotic Properties"
source: "00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_06_JEB109_2026.pdf"
tags: [JEB109, econometrics, consistency, asymptotic-normality, asymptotics, large-sample]
created: 2026-04-19
---

Parent: [[JEB109_Econometrics_I_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_06_JEB109_2026.pdf]]
Related: [[Gauss_Markov_Theorem]], [[F_Test_and_Multiple_Restrictions]], [[MLR_Assumptions_and_OLS_Unbiasedness]], [[Probability_Theory_Review]]

# OLS Consistency and Asymptotic Properties

## Why Asymptotics?

**Unbiasedness** is a finite-sample property: $E(\hat\beta_j) = \beta_j$ for any $n$. However, unbiasedness cannot always be achieved (e.g., when MLR.4 is violated). **Consistency** is considered the *minimum requirement* for any serious estimator.

Moreover, normality of the error term (MLR.6) is a strong assumption. Asymptotics — behaviour as $n \to \infty$ — rescue inference without MLR.6, via the Central Limit Theorem ([[Probability_Theory_Review]]).

---

## OLS Consistency

### Weakened Assumption for Consistency

For consistency of OLS, we do not need the full MLR.4 zero conditional mean. It suffices with:

> **MLR.4′ Zero mean and zero correlation:** $E(u) = 0$ and $\text{Cov}(x_j, u) = 0$ for all $j = 1, \ldots, k$.

MLR.4 (zero conditional mean) implies MLR.4′ but not vice versa.

### Consistency Theorem

**Theorem:** Under MLR.1–MLR.3 and MLR.4′, the OLS estimator is **consistent**:

$$\text{plim}_{n \to \infty}\, \hat\beta_j = \beta_j, \quad j = 0, 1, \ldots, k.$$

This means: for all $\varepsilon > 0$, $P(|\hat\beta_j - \beta_j| > \varepsilon) \to 0$ as $n \to \infty$.

**MLR.5 and MLR.6 are not needed for consistency** — in the same way they are not needed for unbiasedness.

### Proof Idea (Simple Regression Case)

$$\hat\beta_1 = \beta_1 + \frac{\frac{1}{n}\sum(x_i - \bar x)u_i}{\frac{1}{n}\sum(x_i - \bar x)^2}.$$

By the Law of Large Numbers (LLN):
- Numerator: $\frac{1}{n}\sum(x_i - \bar x)u_i \xrightarrow{p} \text{Cov}(x, u) = 0$ (by MLR.4′).
- Denominator: $\frac{1}{n}\sum(x_i - \bar x)^2 \xrightarrow{p} \text{Var}(x) > 0$ (by MLR.3).

Therefore: $\text{plim}\,\hat\beta_1 = \beta_1 + 0/\text{Var}(x) = \beta_1$. $\blacksquare$

---

## Inconsistency (Omitted Variable)

When MLR.4′ is violated (e.g., an omitted variable correlated with $x_1$), the OLS estimator is **inconsistent**:

$$\text{plim}(\hat\beta_1) - \beta_1 = \frac{\text{Cov}(x_1, u)}{\text{Var}(x_1)}.$$

This is the asymptotic analogue of [[Omitted_Variable_Bias]] expressed in population moments.

---

## Asymptotic Normality of OLS

### Theorem

Under the Gauss-Markov assumptions MLR.1–MLR.5 (without MLR.6):

1. $\hat\beta_j$ is **asymptotically normally distributed** for each $j$:

$$\sqrt{n}(\hat\beta_j - \beta_j) \overset{a}{\sim} N(0,\; \text{asymptotic Var}_j).$$

2. $\hat\sigma^2$ is a **consistent estimator** of $\sigma^2 = \text{Var}(u)$.

3. Consequently:

$$\frac{\hat\beta_j - \beta_j}{\text{sd}(\hat\beta_j)} \overset{a}{\sim} N(0, 1) \quad \text{and} \quad \frac{\hat\beta_j - \beta_j}{\text{se}(\hat\beta_j)} \overset{a}{\sim} N(0, 1).$$

**Implication:** For large $n$, even without MLR.6, the $t$ ratios and $F$ statistics are approximately valid — these are called **asymptotic $t$ statistics** and **asymptotic $F$ statistics**.

**Critical caveat:** We **still need MLR.5 (homoskedasticity)** for the asymptotic $t$ and $F$ statistics to be valid. If heteroskedasticity is present, one must use **heteroskedasticity-robust standard errors**.

---

## Asymptotic Efficiency

Under MLR.1–MLR.5, OLS estimators are **asymptotically efficient** — among consistent asymptotically normal estimators, OLS has the smallest asymptotic variance. The variance shrinks to zero at rate $1/n$, so $\text{se}(\hat\beta_j)$ shrinks at rate $1/\sqrt{n}$.

---

## Consistency vs. Unbiasedness

| Property | Unbiasedness | Consistency |
|----------|-------------|------------|
| Definition | $E(\hat\theta) = \theta$ for all $n$ | $\text{plim}_{n\to\infty}\hat\theta = \theta$ |
| What it guarantees | Correct on average | Converges to truth as $n \to \infty$ |
| Relationship | Unbiased + bounded SE → consistent | Consistent does not imply unbiased |
| MLR required | 1–4 | 1–3 + MLR.4′ |

---

## How Large Must $n$ Be?

There is no general rule, but rough guidelines:
- $n > 30$ is often considered sufficient for CLT to provide a good approximation.
- With highly non-normal errors or many regressors, larger $n$ (e.g., $> 100$) may be needed.
- The asymptotic $t_{n-k-1} \approx N(0,1)$ approximation is typically used for $n - k - 1 > 120$.

---

## Historical Note: Andrey Markov (1856–1922)

Markov extended the LLN and CLT to dependent sequences, introducing what we now call Markov chains (each state depends on the current, not the full past). He also provided the modern proof of the Gauss-Markov theorem without normality. His analysis of Pushkin's *Eugene Onegin* — counting vowel-to-consonant transition frequencies — is an early empirical application of stochastic dependence modelling.
