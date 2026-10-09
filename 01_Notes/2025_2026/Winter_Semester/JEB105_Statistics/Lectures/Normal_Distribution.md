---
course: JEB105
topic: "Normal Distribution"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_06_Selected_Families_of_Distributions.pdf"
tags: [JEB105, statistics, normal-distribution, Gaussian, bell-curve]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_06_Selected_Families_of_Distributions.pdf]]
Related: [[Random_Variable]], [[Expected_Value]], [[Variance]], [[Central_Limit_Theorem]], [[Normal_Distribution#Definition|Standard Normal Distribution]], [[Chi_Squared_Distribution]], [[t_Distribution]]

---

## Normal Distribution

### Definition

A [[Random_Variable]] $X$ has the **normal distribution** (Gaussian distribution) with mean $\mu \in \mathbb{R}$ and variance $\sigma^2 > 0$, written $X \sim N(\mu, \sigma^2)$, if its PDF is:

$$f(x; \mu, \sigma^2) = \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right), \quad x \in \mathbb{R}.$$

The **standard normal** $Z \sim N(0, 1)$ has PDF $\varphi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}$ and CDF $\Phi(z) = \int_{-\infty}^z \varphi(t)\, dt$.

### Properties

**Mean and variance:**
$$E[X] = \mu, \quad \text{Var}(X) = \sigma^2.$$

**Standardisation:** If $X \sim N(\mu, \sigma^2)$, then $Z = \frac{X - \mu}{\sigma} \sim N(0,1)$.

**Symmetry:** $f$ is symmetric about $\mu$; $\Phi(-z) = 1 - \Phi(z)$.

**MGF:** $M_X(t) = e^{\mu t + \sigma^2 t^2/2}$ (see [[Moment_Generating_Function]]).

**Reproductive property:** If $X_i \sim N(\mu_i, \sigma_i^2)$ independently, then:

$$\sum_{i=1}^n a_i X_i \sim N\!\left(\sum_i a_i \mu_i,\; \sum_i a_i^2 \sigma_i^2\right).$$

**68-95-99.7 rule:**
- $P(\mu - \sigma \leq X \leq \mu + \sigma) \approx 0.6827$
- $P(\mu - 2\sigma \leq X \leq \mu + 2\sigma) \approx 0.9545$
- $P(\mu - 3\sigma \leq X \leq \mu + 3\sigma) \approx 0.9973$

### Quantiles and Critical Values

The $(1-\alpha)$-quantile of $N(0,1)$ is $z_\alpha$ satisfying $P(Z \leq z_\alpha) = 1 - \alpha$.

Notation (lecture): $z_\alpha$ denotes the $(1-\alpha)$-lower quantile, so $P(Z \leq z_\alpha) = 1-\alpha$ and $z_{1-\alpha} = -z_\alpha$. Thus $P(|Z| \leq z_{\alpha/2}) = 1-\alpha$.

Common values: $z_{0.025} = 1.96$, $z_{0.005} = 2.576$.

### Derivation: Normalisation Integral

$$\int_{-\infty}^{\infty} e^{-x^2/2}\, dx = \sqrt{2\pi}.$$

**Proof (Gaussian integral):** Let $I = \int_{-\infty}^{\infty} e^{-x^2/2}\, dx$. Then:

$$I^2 = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} e^{-(x^2+y^2)/2}\, dx\, dy.$$

Convert to polar coordinates $r^2 = x^2 + y^2$:

$$I^2 = \int_0^{2\pi}\int_0^{\infty} e^{-r^2/2} r\, dr\, d\theta = 2\pi \int_0^{\infty} r e^{-r^2/2}\, dr = 2\pi \cdot 1 = 2\pi.$$

Hence $I = \sqrt{2\pi}$.

### Bivariate Normal

$(X,Y)$ is **bivariate normal** with parameters $\mu_1, \mu_2, \sigma_1^2, \sigma_2^2, \rho$ if:

$$f(x,y) = \frac{1}{2\pi\sigma_1\sigma_2\sqrt{1-\rho^2}} \exp\!\left(-\frac{1}{2(1-\rho^2)}\left[\frac{(x-\mu_1)^2}{\sigma_1^2} - 2\rho\frac{(x-\mu_1)(y-\mu_2)}{\sigma_1\sigma_2} + \frac{(y-\mu_2)^2}{\sigma_2^2}\right]\right).$$

Key property: $X \perp Y \iff \rho = 0$ (unique to the bivariate normal).

Conditional distribution: $X \mid Y = y \sim N\!\left(\mu_1 + \rho\frac{\sigma_1}{\sigma_2}(y - \mu_2),\; \sigma_1^2(1-\rho^2)\right)$.

### Examples

**Example 1:** $X \sim N(2, 9)$. $P(X > 5) = P\!\left(Z > \frac{5-2}{3}\right) = P(Z > 1) = 1 - \Phi(1) \approx 0.1587$.

**Example 2 (Lecture, Part 7):** Sample mean $\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i$ where $X_i \sim N(\mu, \sigma^2)$ i.i.d. Then $\bar{X} \sim N(\mu, \sigma^2/n)$.

### Interpretation

The normal distribution is the most important distribution in statistics for two reasons:
1. **Central Limit Theorem:** Sums of i.i.d. random variables converge in distribution to $N(\mu, \sigma^2/n)$ regardless of the original distribution.
2. **Maximum entropy:** Among all distributions with given mean $\mu$ and variance $\sigma^2$, the normal maximises entropy — it is in this sense the "most random" distribution.

The normal distribution underpins classical hypothesis tests ($z$-test, $t$-test), confidence intervals, and regression models.
