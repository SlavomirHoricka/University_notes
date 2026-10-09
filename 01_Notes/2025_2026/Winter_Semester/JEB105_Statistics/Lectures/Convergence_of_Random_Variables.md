---
course: JEB105
topic: "Convergence of Random Variables"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_07_Random_Samples.pdf"
tags: [JEB105, statistics, convergence, probability, almost-sure, distribution, LLN, CLT]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_07_Random_Samples.pdf]]
Related: [[Law_of_Large_Numbers]], [[Central_Limit_Theorem]], [[Random_Sample_and_Statistics]], [[Bias_and_MSE]]

---

## Convergence of Random Variables

### Motivation

In statistics, we want to know what happens to estimators like $\bar{X}_n$ as the sample size $n \to \infty$. Different notions of convergence formalise different senses in which a sequence of random variables $T_n$ "approaches" a limit $T$.

### Modes of Convergence

#### Convergence Almost Surely (a.s.)

$T_n \xrightarrow{a.s.} T$ if

$$P\!\left(\lim_{n\to\infty} T_n = T\right) = 1.$$

The sequence converges to $T$ on a set of probability 1. This is the strongest mode and implies convergence in probability.

#### Convergence in Probability

$T_n \xrightarrow{P} T$ if for every $\varepsilon > 0$:

$$\lim_{n\to\infty} P(|T_n - T| > \varepsilon) = 0.$$

This is the formal statement of **consistency** for an estimator: $T_n$ is (weakly) consistent for $\theta$ if $T_n \xrightarrow{P} \theta$.

#### Convergence in Distribution (in Law)

$T_n \xrightarrow{d} T$ if

$$\lim_{n\to\infty} F_{T_n}(x) = F_T(x)$$

at every continuity point $x$ of $F_T$. This is the weakest mode. The [[Central_Limit_Theorem]] is the canonical example: $\sqrt{n}(\bar{X}_n - \mu)/\sigma \xrightarrow{d} N(0,1)$.

### Implication Chain

$$\text{a.s.} \implies \text{in probability} \implies \text{in distribution.}$$

None of the reverse implications hold in general.

**Example of a.s. but not in probability failing the converse:** Convergence in probability does not imply a.s. convergence — the "typewriter sequence" is a standard counterexample.

### Useful Results

**Continuous mapping theorem:** If $T_n \xrightarrow{P} T$ (or $\xrightarrow{d}$) and $g$ is continuous, then $g(T_n) \xrightarrow{P} g(T)$ (or $\xrightarrow{d}$).

**Slutsky's theorem:** If $T_n \xrightarrow{d} T$ and $U_n \xrightarrow{P} c$ (a constant), then:
- $T_n + U_n \xrightarrow{d} T + c$
- $T_n \cdot U_n \xrightarrow{d} c \cdot T$
- $T_n / U_n \xrightarrow{d} T/c$ (if $c \neq 0$)

Slutsky's theorem is used heavily in asymptotic inference — e.g., replacing $\sigma$ by a consistent estimator $\hat{\sigma}$ in the CLT standardisation does not change the limiting distribution.

### Test of Consistency via Chebyshev's Inequality

For an estimator $T_n$ of $\theta$:
1. Compute $\text{Var}(T_n)$ and bias $B(T_n) = E[T_n] - \theta$.
2. $T_n$ is consistent if:
   - $T_n$ is unbiased and $\text{Var}(T_n) \to 0$, or
   - $T_n$ is biased but both $\text{Var}(T_n) \to 0$ and $B(T_n) \to 0$.

This follows from Chebyshev's inequality applied to $|T_n - \theta|$.

### Interpretation

- **Almost sure convergence** says the random path of $T_n$ eventually stays arbitrarily close to $T$ — the strongest guarantee.
- **Convergence in probability** says that the probability of being far from $T$ vanishes — this is the consistency property used in statistical inference.
- **Convergence in distribution** says the shape of the distribution of $T_n$ approaches that of $T$ — the basis for asymptotic approximations (e.g., using $N(0,1)$ critical values for large-$n$ tests).
