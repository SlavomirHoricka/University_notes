---
course: JEB105
topic: "Binomial Distribution"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_06_Selected_Families_of_Distributions.pdf"
tags: [JEB105, statistics, binomial, discrete-distribution, Bernoulli]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_06_Selected_Families_of_Distributions.pdf]]
Related: [[Probability_Mass_Function]], [[Expected_Value]], [[Variance]], [[Poisson_Distribution]], [[Normal_Distribution]], [[Bernoulli_Distribution]], [[Binomial_Coefficient]]

---

## Binomial Distribution

### Definition

The **binomial distribution** $\text{Bin}(n, p)$ models the number of successes in $n$ independent Bernoulli trials, each with success probability $p \in (0,1)$.

**PMF:**

$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, \ldots, n.$$

**Parameters:** $n \in \mathbb{N}$ (number of trials), $p \in (0,1)$ (success probability).

### Properties

**Mean and variance:**
$$E[X] = np, \quad \text{Var}(X) = np(1-p).$$

**Derivation of mean:** $X = \sum_{i=1}^n X_i$ where $X_i \sim \text{Ber}(p)$ i.i.d. By linearity: $E[X] = nE[X_1] = np$. By independence: $\text{Var}(X) = n\text{Var}(X_1) = np(1-p)$.

**MGF:** $M_X(t) = (1 - p + pe^t)^n$.

**Reproductive property:** If $X \sim \text{Bin}(m, p)$ and $Y \sim \text{Bin}(n, p)$ independently, then $X + Y \sim \text{Bin}(m+n, p)$.

**Normalisation identity:** $\sum_{k=0}^n \binom{n}{k} p^k (1-p)^{n-k} = 1$ (binomial theorem).

### Approximations

**Normal approximation (CLT):** For large $n$, $X \approx N(np, np(1-p))$, i.e.,

$$\frac{X - np}{\sqrt{np(1-p)}} \xrightarrow{d} N(0,1).$$

Rule of thumb: approximation adequate when $np \geq 5$ and $n(1-p) \geq 5$.

**Poisson approximation (rare events):** If $n$ large, $p$ small, $np = \lambda$ fixed, then $\text{Bin}(n,p) \approx \text{Poi}(\lambda)$.

**Proof sketch:** $\binom{n}{k} p^k (1-p)^{n-k} \to \frac{\lambda^k e^{-\lambda}}{k!}$ as $n \to \infty$, $p = \lambda/n$.

### Derivation: Mean and Variance via PGF

The **probability generating function** is $G_X(s) = E[s^X] = (1-p+ps)^n$.

$G'_X(1) = E[X] = np$. $G''_X(1) = E[X(X-1)] = n(n-1)p^2$.

$\text{Var}(X) = G''_X(1) + G'_X(1) - [G'_X(1)]^2 = n(n-1)p^2 + np - n^2p^2 = np(1-p)$.

### Examples

**Example 1:** $X \sim \text{Bin}(10, 0.3)$. $P(X = 3) = \binom{10}{3}(0.3)^3(0.7)^7 \approx 0.267$.

**Example 2 (Lecture, Part 7):** $X \sim \text{Bin}(n,p)$. The MLE of $p$ is $\hat{p} = X/n = \bar{X}$.

**Example 3 (Lecture, Ex. 96 — orange shipment):** Oranges with defect rate $p$, sample $n = 30$, critical region: reject if more than 1 defective. The critical region $C = \{X \geq 2\}$ where $X \sim \text{Bin}(30, p)$.

### Interpretation

The binomial distribution is the natural model for count data arising from a fixed number of independent, identical binary trials. It appears in quality control (number of defects), clinical trials (number of responders), and polling (number of supporters). Its connection to the Bernoulli, Poisson, and normal distributions makes it a bridge between discrete and continuous statistical theory.
