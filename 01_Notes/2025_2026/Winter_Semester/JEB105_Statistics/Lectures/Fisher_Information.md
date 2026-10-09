---
course: JEB105
topic: "Fisher Information"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_08_Point_Estimation.pdf"
tags: [JEB105, statistics, Fisher-information, score-function, Rao-Cramer, efficiency]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_08_Point_Estimation.pdf]]
Related: [[Point_Estimation]], [[Bias_and_MSE]], [[Rao_Cramer_Lower_Bound]], [[Maximum_Likelihood_Estimation]], [[Confidence_Intervals]]

---

## Fisher Information

### Regularity Assumption

Assume the distribution $f(x,\theta)$ satisfies the **regularity assumption**: the set $\{x : f(x,\theta) > 0\}$ does not depend on $\theta$. This excludes cases like $U[0,\theta]$ where the support changes with $\theta$. Under this condition, no single observation can completely rule out any value of $\theta$.

### Score Function

**Definition 43 (Lecture):** The **score function** is the partial derivative of the log-likelihood with respect to $\theta$:

$$J(X, \theta) = \frac{\partial}{\partial \theta} \log f(X, \theta).$$

The score measures how sensitive the log-density is to the parameter $\theta$ at the observed value $X$.

### Fisher Information

**Definition 43 (Lecture, continued):** The **Fisher information** about $\theta$ contained in a single observation $X$ is:

$$I(\theta) = E_\theta\!\left[(J(X,\theta))^2\right] = E_\theta\!\left[\left(\frac{\partial}{\partial\theta}\log f(X,\theta)\right)^2\right],$$

provided the expectation exists.

### Properties of Fisher Information (Theorem 58)

Under regularity assumptions:

**a)** $E_\theta[J(X,\theta)] = 0$.

*Proof:* $E_\theta[J] = \int \frac{f'(x,\theta)}{f(x,\theta)} f(x,\theta)\,dx = \frac{d}{d\theta}\int f(x,\theta)\,dx = \frac{d}{d\theta} 1 = 0$.

**b)** $\text{Var}_\theta[J(X,\theta)] = I(\theta)$.

This follows from $E[J] = 0$: $\text{Var}(J) = E[J^2] - (E[J])^2 = I(\theta)$.

**c)** Alternative formula (second-derivative form):

$$I(\theta) = -E_\theta\!\left[\frac{\partial^2}{\partial\theta^2} \log f(X,\theta)\right].$$

**d)** Fisher information in a sample of $n$ observations:

$$I_n(\theta) = n \cdot I(\theta).$$

This additivity reflects the independence of the observations.

### Examples

**Example 84:** $X \sim N(\theta, \sigma^2)$ (estimating the mean, $\sigma^2$ known).

$$J(X,\theta) = \frac{\partial}{\partial\theta}\!\left(-\log\sigma\sqrt{2\pi} - \frac{(X-\theta)^2}{2\sigma^2}\right) = \frac{X-\theta}{\sigma^2}.$$

$$I(\theta) = E\!\left[\left(\frac{X-\theta}{\sigma^2}\right)^2\right] = \frac{1}{\sigma^4}E[(X-\theta)^2] = \frac{\sigma^2}{\sigma^4} = \frac{1}{\sigma^2}.$$

**Example 85:** Bernoulli trial with $P(X=1|\theta) = \theta$.

$$J(X,\theta) = \begin{cases} -\frac{1}{1-\theta} & X=0 \\ \frac{1}{\theta} & X=1 \end{cases}, \qquad I(\theta) = \frac{1}{\theta(1-\theta)}.$$

$I(\theta)$ is minimised at $\theta = 1/2$ (most ambiguous case) and diverges as $\theta \to 0$ or $1$ (the experiment becomes highly informative about extreme parameters).

### Interpretation

Fisher information quantifies how much information a single observation $X$ carries about the parameter $\theta$:
- **Large $I(\theta)$:** The likelihood function is sharply peaked around $\theta$ — data are highly informative and estimation is precise.
- **Small $I(\theta)$:** The likelihood is flat — data are relatively uninformative.

Fisher information is the foundational quantity connecting the statistical model to the precision limits of estimation (via the [[Rao_Cramer_Lower_Bound]]) and to the asymptotic variance of the MLE (via [[Maximum_Likelihood_Estimation]]).
