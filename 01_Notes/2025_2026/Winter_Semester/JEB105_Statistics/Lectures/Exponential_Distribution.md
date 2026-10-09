---
course: JEB105
topic: "Exponential Distribution"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_06_Selected_Families_of_Distributions.pdf"
tags: [JEB105, statistics, exponential-distribution, memoryless, waiting-time]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_06_Selected_Families_of_Distributions.pdf]]
Related: [[Probability_Density_Function]], [[Poisson_Distribution]], [[Gamma_Distribution]], [[Expected_Value]], [[Variance]]

---

## Exponential Distribution

### Definition

A [[Random_Variable]] $X$ follows the **exponential distribution** with rate parameter $\lambda > 0$, written $X \sim \text{Exp}(\lambda)$, if its PDF is:

$$f(x; \lambda) = \lambda e^{-\lambda x}, \quad x \geq 0$$

(and $f(x) = 0$ for $x < 0$).

The CDF is:

$$F(x) = 1 - e^{-\lambda x}, \quad x \geq 0.$$

Alternative parametrisation: $X \sim \text{Exp}(\beta)$ with $\beta = 1/\lambda$ (mean parametrisation), $f(x) = \frac{1}{\beta}e^{-x/\beta}$.

### Properties

**Mean and variance:**
$$E[X] = \frac{1}{\lambda}, \quad \text{Var}(X) = \frac{1}{\lambda^2}.$$

**MGF:** $M_X(t) = \frac{\lambda}{\lambda - t}$ for $t < \lambda$.

**Memoryless property:** For $s, t \geq 0$:
$$P(X > s + t \mid X > s) = P(X > t).$$

**Proof:** $P(X > s+t \mid X > s) = \frac{P(X > s+t)}{P(X > s)} = \frac{e^{-\lambda(s+t)}}{e^{-\lambda s}} = e^{-\lambda t} = P(X > t)$.

The exponential is the **only continuous distribution** with the memoryless property.

**Relationship to Poisson:** In a Poisson process with rate $\lambda$, interarrival times are i.i.d. $\text{Exp}(\lambda)$.

**Minimum of exponentials:** If $X_i \sim \text{Exp}(\lambda_i)$ independently, then $\min(X_1, \ldots, X_n) \sim \text{Exp}(\lambda_1 + \cdots + \lambda_n)$.

### Derivation: Memoryless Property and Uniqueness

The functional equation $P(X > s + t) = P(X > s) P(X > t)$ for the survival function $\bar{F}(t) = P(X > t)$ implies $\bar{F}(t) = e^{-\lambda t}$ for some $\lambda > 0$ (for continuous $\bar{F}$). This characterises the exponential uniquely.

### Gamma Connection

$X \sim \text{Gamma}(\alpha, \lambda)$ if $X = \sum_{i=1}^{\alpha} X_i$ where $X_i \sim \text{Exp}(\lambda)$ i.i.d. (for integer $\alpha$). The exponential is $\text{Gamma}(1, \lambda)$.

### Examples

**Example 1:** Light bulb lifetime $X \sim \text{Exp}(1/1000)$ hours (mean 1000 hours). $P(X > 1200) = e^{-1200/1000} = e^{-1.2} \approx 0.301$.

**Example 2 (Memoryless):** Given the bulb has already lasted 500 hours, the probability it lasts another 1200 hours equals $P(X > 1200) = e^{-1.2}$ — the past doesn't matter.

### Interpretation

The exponential distribution models **waiting times** until the first event in a Poisson process. The memoryless property makes it mathematically elegant: an exponential random variable "forgets" its history. This models scenarios where the failure rate is constant (e.g., electronic components in their useful life phase). The hazard rate (failure rate) is $h(x) = f(x)/\bar{F}(x) = \lambda$, constant.
