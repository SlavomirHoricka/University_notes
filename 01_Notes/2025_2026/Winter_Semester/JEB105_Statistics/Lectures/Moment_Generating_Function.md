---
course: JEB105
topic: "Moment Generating Function"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_04_Expectations-1.pdf"
tags: [JEB105, statistics, MGF, moments, characteristic-function]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_04_Expectations-1.pdf]]
Related: [[Expected_Value]], [[Variance]], [[Random_Variable]], [[Normal_Distribution]], [[Central_Limit_Theorem]]

---

## Moment Generating Function

### Definition

The **moment generating function** (MGF) of a [[Random_Variable]] $X$ is:

$$M_X(t) = E\!\left[e^{tX}\right], \quad t \in \mathbb{R},$$

defined for all $t$ in an open interval $(-h, h)$ with $h > 0$ where the expectation is finite.

**Discrete case:** $M_X(t) = \sum_i e^{t x_i} p(x_i)$.

**Continuous case:** $M_X(t) = \int_{-\infty}^{\infty} e^{tx} f(x)\, dx$.

### Properties

**Moment generation:** If $M_X(t)$ exists in a neighbourhood of 0:

$$E[X^k] = M_X^{(k)}(0) = \left.\frac{d^k}{dt^k} M_X(t)\right|_{t=0}.$$

**Proof:** $\frac{d^k}{dt^k} e^{tX} = X^k e^{tX}$, so $M_X^{(k)}(t) = E[X^k e^{tX}]$ and at $t=0$: $M_X^{(k)}(0) = E[X^k]$.

**Uniqueness Theorem:** If $M_X(t) = M_Y(t)$ for all $t$ in a neighbourhood of 0, then $X$ and $Y$ have the same distribution.

**Independence:** If $X \perp Y$:

$$M_{X+Y}(t) = E[e^{t(X+Y)}] = E[e^{tX}] E[e^{tY}] = M_X(t) M_Y(t).$$

**Linear transformation:** $M_{aX+b}(t) = e^{bt} M_X(at)$.

### MGFs of Common Distributions

**Bernoulli $\text{Ber}(p)$:** $M(t) = 1 - p + pe^t$.

**Binomial $\text{Bin}(n,p)$:** $M(t) = (1-p+pe^t)^n$.

**Poisson $\text{Poi}(\lambda)$:** $M(t) = e^{\lambda(e^t - 1)}$.

**Normal $N(\mu, \sigma^2)$:** $M(t) = \exp\!\left(\mu t + \frac{\sigma^2 t^2}{2}\right)$.

**Exponential $\text{Exp}(\lambda)$:** $M(t) = \frac{\lambda}{\lambda - t}$ for $t < \lambda$.

**Gamma $\Gamma(\alpha, \beta)$:** $M(t) = \left(\frac{\beta}{\beta - t}\right)^\alpha$ for $t < \beta$.

### Derivation: Normal MGF

For $X \sim N(\mu, \sigma^2)$:

$$M_X(t) = \int_{-\infty}^{\infty} e^{tx} \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} dx.$$

Complete the square in the exponent:

$$tx - \frac{(x-\mu)^2}{2\sigma^2} = -\frac{1}{2\sigma^2}\left[x^2 - 2(\mu + \sigma^2 t)x + \mu^2\right] = -\frac{(x - (\mu+\sigma^2 t))^2}{2\sigma^2} + \mu t + \frac{\sigma^2 t^2}{2}.$$

Hence: $M_X(t) = e^{\mu t + \frac{\sigma^2 t^2}{2}} \cdot \underbrace{\int_{-\infty}^{\infty} \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-(\mu+\sigma^2 t))^2}{2\sigma^2}} dx}_{=1} = e^{\mu t + \sigma^2 t^2 / 2}.$

**Moments from MGF:**
$$M'_X(0) = (\mu + \sigma^2 t) e^{\mu t + \sigma^2 t^2/2}\big|_{t=0} = \mu = E[X]. \checkmark$$

### Application: Reproductive Property of Normal

If $X_i \sim N(\mu_i, \sigma_i^2)$ independently, then $\sum_i X_i \sim N\!\left(\sum_i \mu_i, \sum_i \sigma_i^2\right)$.

**Proof via MGFs:** $M_{\sum X_i}(t) = \prod_i M_{X_i}(t) = \prod_i e^{\mu_i t + \sigma_i^2 t^2/2} = e^{(\sum \mu_i)t + (\sum \sigma_i^2) t^2/2}$, which is the MGF of $N(\sum \mu_i, \sum \sigma_i^2)$.

### Interpretation

The MGF encodes all moments of a distribution in a single function. Its uniqueness property makes it a powerful tool for identifying distributions and proving convergence results. The MGF of the normal distribution's quadratic exponent structure explains why sums of normal variables remain normal — a key fact underlying classical statistical tests.
