---
course: JEB105
topic: "Generalized Likelihood Ratio Test"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_10_Testing_Statistical_Hypotheses-1.pdf"
tags: [JEB105, statistics, GLRT, generalized-likelihood-ratio, hypothesis-testing]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_10_Testing_Statistical_Hypotheses-1.pdf]]
Related: [[Neyman_Pearson_Lemma]], [[Maximum_Likelihood_Estimation]], [[Hypothesis_Testing_Framework]], [[Standard_Tests_Catalog]]

---

## Generalized Likelihood Ratio Test

### Motivation

The [[Neyman_Pearson_Lemma]] provides the optimal test for simple $H_0$ vs. simple $H_1$. When one or both hypotheses are composite (involving multiple parameter values), we generalise using the **generalised likelihood ratio (GLR)** statistic.

### The Generalised Likelihood Ratio

**Definition 53 (Lecture):** The **generalised likelihood ratio statistic** is:

$$\lambda(X) = \frac{\sup_{\theta \in \Theta_0} f(X, \theta)}{\sup_{\theta \in \Theta} f(X, \theta)}.$$

- The numerator is the maximum likelihood of the data under $H_0$.
- The denominator is the unrestricted maximum likelihood (the MLE over the full parameter space).
- Since $\Theta_0 \subseteq \Theta$: $\lambda(X) \leq 1$.

Note: Some texts define the generalised likelihood ratio as:
$$v(X) = \frac{\sup_{\theta \in \Theta_1} f(X, \theta)}{\sup_{\theta \in \Theta_0} f(X, \theta)},$$
rejecting $H_0$ when $v(X)$ is large. The relationship is $v(X)\lambda(X) \leq 1$, so large $v$ corresponds to small $\lambda$.

### Critical Region

Reject $H_0$ when $\lambda(X)$ is **small** (equivalently, $v(X)$ is large). The $\alpha$-level critical region is:

$$C = \{\lambda(X) \leq K_\alpha\}$$

where $K_\alpha$ is chosen so that $P(\lambda(X) \leq K_\alpha \mid H_0) = \alpha$.

When $\Theta_0$ is a closed set, $\sup_{\theta \in \Theta_0} f(X,\theta)$ is attained by the **constrained MLE** and $\sup_{\theta \in \Theta} f(X,\theta)$ by the unconstrained MLE.

### Wilks' Theorem (Asymptotic Distribution)

Under $H_0$ and regularity conditions, as $n \to \infty$:

$$-2\log\lambda(X) \xrightarrow{d} \chi^2_r,$$

where $r = \dim(\Theta) - \dim(\Theta_0)$ is the number of restrictions imposed by $H_0$.

This provides a simple asymptotic test: reject $H_0$ at level $\alpha$ if $-2\log\lambda(X) > \chi^2_{\alpha, r}$.

### Example 98: Normal Mean Test

$X_1, \ldots, X_n \overset{\text{i.i.d.}}{\sim} N(\mu, \sigma^2)$, both unknown.

$H_0: \mu = \mu_0$, $\sigma^2 > 0$ arbitrary; vs. $H_1: \mu \neq \mu_0$, $\sigma^2 > 0$ arbitrary.

- Constrained MLE (under $H_0$): $\hat{\mu}_0 = \mu_0$, $\hat{\sigma}_0^2 = \frac{1}{n}\sum(X_i - \mu_0)^2$.
- Unconstrained MLE: $\hat{\mu} = \bar{X}$, $\hat{\sigma}^2 = \frac{1}{n}\sum(X_i - \bar{X})^2$.

The GLR statistic simplifies to a function of the $t$-statistic, and the test based on $\lambda(X)$ is equivalent to the standard $t$-test for the mean (see [[Standard_Tests_Catalog]]).

### Connection to Standard Tests

The GLRT unifies many classical tests:
- **$z$-test for the mean** (known variance): GLRT reduces to the $z$-statistic.
- **$t$-test for the mean** (unknown variance): GLRT reduces to the $t$-statistic.
- **$\chi^2$-test for variance:** GLRT reduces to the chi-squared statistic.
- **$F$-test for equality of variances:** GLRT reduces to the $F$-statistic.

### Interpretation

The GLRT compares two models: $H_0$ (restricted) and the full model. If the data are much more likely under the full model than under $H_0$, we reject $H_0$. The GLR statistic $\lambda(X)$ measures this relative fit. Wilks' theorem provides a universal asymptotic distribution for the test statistic, making the GLRT widely applicable regardless of the specific model — it is the standard method for constructing tests when no UMP test exists.
