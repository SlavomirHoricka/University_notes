---
course: JEB105
topic: "Poisson Distribution"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_06_Selected_Families_of_Distributions.pdf"
tags: [JEB105, statistics, Poisson, discrete-distribution, counting-process]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_06_Selected_Families_of_Distributions.pdf]]
Related: [[Probability_Mass_Function]], [[Expected_Value]], [[Variance]], [[Binomial_Distribution]], [[Exponential_Distribution]], [[Conditional_Distribution]]

---

## Poisson Distribution

### Definition

A [[Random_Variable]] $X$ follows the **Poisson distribution** with parameter $\lambda > 0$, written $X \sim \text{Poi}(\lambda)$, if:

$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k = 0, 1, 2, \ldots$$

**Normalisation:** $\sum_{k=0}^{\infty} \frac{\lambda^k e^{-\lambda}}{k!} = e^{-\lambda} e^{\lambda} = 1$.

### Properties

**Mean and variance:**
$$E[X] = \lambda, \quad \text{Var}(X) = \lambda.$$

The Poisson is the unique distribution for which **mean equals variance**.

**MGF:** $M_X(t) = e^{\lambda(e^t - 1)}$.

**Reproductive property:** If $X_i \sim \text{Poi}(\lambda_i)$ independently, then $\sum_i X_i \sim \text{Poi}(\sum_i \lambda_i)$.

**Poisson process connection:** In a Poisson process with rate $\lambda$, the number of events in time interval $[0, t]$ follows $\text{Poi}(\lambda t)$; interarrival times are i.i.d. $\text{Exp}(\lambda)$.

### Derivation: Mean and Variance

**Mean:**
$$E[X] = \sum_{k=0}^{\infty} k \frac{\lambda^k e^{-\lambda}}{k!} = \lambda e^{-\lambda} \sum_{k=1}^{\infty} \frac{\lambda^{k-1}}{(k-1)!} = \lambda e^{-\lambda} e^{\lambda} = \lambda.$$

**Variance via $E[X(X-1)]$:**
$$E[X(X-1)] = \lambda^2 e^{-\lambda} \sum_{k=2}^{\infty} \frac{\lambda^{k-2}}{(k-2)!} = \lambda^2.$$

$$\text{Var}(X) = E[X^2] - (E[X])^2 = E[X(X-1)] + E[X] - (E[X])^2 = \lambda^2 + \lambda - \lambda^2 = \lambda.$$

### Derivation: Poisson as Limit of Binomial

Let $X_n \sim \text{Bin}(n, \lambda/n)$. As $n \to \infty$:

$$P(X_n = k) = \binom{n}{k}\left(\frac{\lambda}{n}\right)^k\left(1-\frac{\lambda}{n}\right)^{n-k}.$$

$$= \frac{n(n-1)\cdots(n-k+1)}{k!} \cdot \frac{\lambda^k}{n^k} \cdot \left(1-\frac{\lambda}{n}\right)^n \cdot \left(1-\frac{\lambda}{n}\right)^{-k}.$$

As $n \to \infty$: $\frac{n(n-1)\cdots(n-k+1)}{n^k} \to 1$, $\left(1-\frac{\lambda}{n}\right)^n \to e^{-\lambda}$, $\left(1-\frac{\lambda}{n}\right)^{-k} \to 1$.

Hence $P(X_n = k) \to \frac{\lambda^k e^{-\lambda}}{k!}$.

### Binomial Thinning (Lecture Example 59)

If $Y \sim \text{Poi}(\lambda)$ and $X \mid Y = n \sim \text{Bin}(n, p)$ (each of $Y$ events independently observed with probability $p$), then $X \sim \text{Poi}(\lambda p)$.

**Proof via MGF:** $M_X(t) = E[M_{X|Y}(t)] = E[(1-p+pe^t)^Y] = M_Y(\log(1-p+pe^t)) = e^{\lambda(1-p+pe^t - 1)} = e^{\lambda p(e^t - 1)}$, which is the MGF of $\text{Poi}(\lambda p)$.

### Examples

**Example 1:** Cars arrive at a toll booth at rate $\lambda = 3$ per minute. $P(\text{exactly 5 arrive in 1 min}) = e^{-3} \cdot 3^5 / 5! \approx 0.1008$.

**Example 2 (Lecture, Ex. 59):** $Y \sim \text{Poi}(5)$ eggs; each hatches with probability $p = 0.6$. Then $X \sim \text{Poi}(3)$; $E[X] = 3$, $\text{Var}(X) = 3$.

### Interpretation

The Poisson distribution models rare events in a large number of opportunities, or counts of events in a fixed time or space interval under stationarity and independence assumptions. It is the natural model for counts: accidents, defects, emails per hour, customer arrivals. Its equidispersion property ($\mu = \sigma^2$) can be tested; overdispersion ($\sigma^2 > \mu$) suggests a negative binomial model.
