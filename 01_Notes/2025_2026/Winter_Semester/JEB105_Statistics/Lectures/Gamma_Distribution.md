---
course: JEB105
topic: "Gamma Distribution"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_06_Selected_Families_of_Distributions.pdf"
tags: [JEB105, statistics, gamma-distribution, continuous-distribution]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_06_Selected_Families_of_Distributions.pdf]]
Related: [[Exponential_Distribution]], [[Chi_Squared_Distribution]], [[Expected_Value]], [[Variance]], [[Probability_Density_Function]]

---

## Gamma Distribution

### Definition

The **gamma function** is defined for $\alpha > 0$:

$$\Gamma(\alpha) = \int_0^{\infty} t^{\alpha-1} e^{-t}\, dt.$$

Key properties: $\Gamma(\alpha + 1) = \alpha \Gamma(\alpha)$, $\Gamma(1) = 1$, $\Gamma(n) = (n-1)!$ for $n \in \mathbb{N}$, $\Gamma(1/2) = \sqrt{\pi}$.

A [[Random_Variable]] $X$ has the **Gamma distribution** $\text{Gamma}(\alpha, \beta)$ if:

$$f(x; \alpha, \beta) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x}, \quad x > 0,$$

where $\alpha > 0$ is the **shape** parameter and $\beta > 0$ is the **rate** parameter (or $\theta = 1/\beta$ is the **scale**).

### Properties

**Mean and variance:**
$$E[X] = \frac{\alpha}{\beta}, \quad \text{Var}(X) = \frac{\alpha}{\beta^2}.$$

**MGF:** $M_X(t) = \left(\frac{\beta}{\beta - t}\right)^\alpha$ for $t < \beta$.

**Reproductive property:** If $X_i \sim \text{Gamma}(\alpha_i, \beta)$ independently with the same rate $\beta$:

$$\sum_i X_i \sim \text{Gamma}\!\left(\sum_i \alpha_i, \beta\right).$$

**Special cases:**
- $\text{Gamma}(1, \beta) = \text{Exp}(\beta)$
- $\text{Gamma}(n/2, 1/2) = \chi^2_n$ ([[Chi_Squared_Distribution]])

### Derivation: Mean

$$E[X] = \int_0^{\infty} x \cdot \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x}\, dx = \frac{\beta^\alpha}{\Gamma(\alpha)} \cdot \frac{\Gamma(\alpha+1)}{\beta^{\alpha+1}} = \frac{\alpha\Gamma(\alpha)}{\Gamma(\alpha)\beta} = \frac{\alpha}{\beta}.$$

### Chi-Squared as Special Case

If $Z \sim N(0,1)$, then $Z^2 \sim \chi^2_1 = \text{Gamma}(1/2, 1/2)$.

If $Z_1, \ldots, Z_n \sim N(0,1)$ i.i.d., then $\sum_i Z_i^2 \sim \chi^2_n = \text{Gamma}(n/2, 1/2)$.

This gives the $\chi^2_n$ distribution directly. See [[Chi_Squared_Distribution]].

### Examples

**Example 1:** $X \sim \text{Gamma}(3, 2)$. $E[X] = 3/2 = 1.5$, $\text{Var}(X) = 3/4 = 0.75$.

**Example 2 (Sum of exponentials):** Waiting time for the 5th Poisson event with rate $\lambda$: $T_5 \sim \text{Gamma}(5, \lambda)$, $E[T_5] = 5/\lambda$.

### Interpretation

The gamma distribution generalises the exponential to model waiting times for the $\alpha$-th event in a Poisson process. It is the conjugate prior for the Poisson rate $\lambda$ in Bayesian analysis. Its flexibility (controlled by $\alpha$) makes it widely used for modelling positive, skewed data such as insurance claim amounts, rainfall, and failure times.
