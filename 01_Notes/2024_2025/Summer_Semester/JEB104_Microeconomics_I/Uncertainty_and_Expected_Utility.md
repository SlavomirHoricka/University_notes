---
course: JEB104
topic: Uncertainty and Expected Utility
source: 00_Materials/2024_2025/Summer_Semester/JEB104_Microeconomics_I/JEB104_16_Uncertainty_Students.pdf
tags: [JEB104, microeconomics, uncertainty, expected-utility, von-Neumann-Morgenstern, risk-aversion, lottery]
created: 2026-04-19
---

Parent: [[JEB104_Microeconomics_I_main]]
Source: [[00_Materials/2024_2025/Summer_Semester/JEB104_Microeconomics_I/JEB104_16_Uncertainty_Students.pdf]]
Related: [[Utility_Function]], [[Preferences_and_Indifference_Curves]], [[Risk_and_Insurance]], [[Intertemporal_Choice]]

# Uncertainty and Expected Utility Theory

## Setup: Lotteries

A **lottery** (or prospect) is a probability distribution over outcomes. With $n$ possible monetary outcomes $x_1 < x_2 < \ldots < x_n$ and probabilities $(p_1, p_2, \ldots, p_n)$ (with $\sum_i p_i = 1$, $p_i \geq 0$):

$$L = (x_1, p_1; x_2, p_2; \ldots; x_n, p_n)$$

**Expected value of the lottery:**

$$\mathbb{E}[x] = \sum_{i=1}^n p_i x_i$$

## Von Neumann–Morgenstern Expected Utility Theory

**Axioms (von Neumann & Morgenstern, 1944):**

1. **Completeness:** For any two lotteries $L$ and $L'$, either $L \succeq L'$ or $L' \succeq L$.
2. **Transitivity:** If $L \succeq L'$ and $L' \succeq L''$, then $L \succeq L''$.
3. **Continuity (Archimedean):** If $L \succ L' \succ L''$, there exists $\alpha \in (0,1)$ such that $\alpha L + (1-\alpha) L'' \sim L'$.
4. **Independence:** If $L \succ L'$, then for any $L''$ and $\alpha \in (0,1)$: $\alpha L + (1-\alpha) L'' \succ \alpha L' + (1-\alpha) L''$.

**VNM Representation Theorem:** The above axioms hold if and only if preferences can be represented by an **expected utility function**:

$$U(L) = \sum_{i=1}^n p_i u(x_i) = \mathbb{E}[u(x)]$$

where $u: \mathbb{R} \to \mathbb{R}$ is the **Bernoulli utility function** (utility of certain wealth). The function $U$ is unique up to positive affine transformation.

## Risk Attitudes

### Risk Aversion

A consumer is **risk averse** if they prefer the expected value of a lottery to the lottery itself:

$$u(\mathbb{E}[x]) > \mathbb{E}[u(x)]$$

Equivalently, $u$ is **strictly concave** ($u'' < 0$).

By **Jensen's inequality**: $u(\mathbb{E}[x]) \geq \mathbb{E}[u(x)]$ when $u$ is concave, with equality iff the lottery is degenerate (certain).

### Risk Neutrality

$$u(\mathbb{E}[x]) = \mathbb{E}[u(x)]$$

$u$ is **linear** ($u'' = 0$). The consumer cares only about the expected value and is indifferent to risk.

### Risk Loving

$$u(\mathbb{E}[x]) < \mathbb{E}[u(x)]$$

$u$ is **strictly convex** ($u'' > 0$). The consumer prefers lotteries to their expected value.

## Certainty Equivalent and Risk Premium

**Certainty equivalent (CE):** The amount of certain wealth that yields the same utility as the lottery:

$$u(CE) = \mathbb{E}[u(x)] \implies CE = u^{-1}(\mathbb{E}[u(x)])$$

**Risk premium:** The amount the consumer is willing to pay to avoid the lottery:

$$RP = \mathbb{E}[x] - CE$$

- Risk averse: $RP > 0$ (would pay to avoid risk).
- Risk neutral: $RP = 0$.
- Risk loving: $RP < 0$ (would pay to accept risk).

## Measures of Risk Aversion

### Arrow-Pratt Absolute Risk Aversion (ARA)

$$A(x) = -\frac{u''(x)}{u'(x)}$$

Measures risk aversion at wealth level $x$. **Decreasing ARA (DARA):** wealthier individuals are less risk averse (empirically plausible).

### Relative Risk Aversion (RRA)

$$R(x) = -\frac{x \cdot u''(x)}{u'(x)} = x \cdot A(x)$$

Measures the elasticity of marginal utility. Relevant for proportional risks (e.g., portfolio allocation).

### Common Utility Functions

| $u(x)$ | ARA $A(x)$ | RRA $R(x)$ | Property |
|---------|------------|------------|----------|
| $\ln x$ | $1/x$ | $1$ | DARA, constant RRA |
| $x^\alpha$, $0 < \alpha < 1$ | $(1-\alpha)/x$ | $1-\alpha$ | DARA, constant RRA (CRRA) |
| $-e^{-ax}$, $a > 0$ | $a$ | $ax$ | Constant ARA (CARA) |
| $-1/x$ | $2/x$ | $2$ | DARA, constant RRA = 2 |

## Mean-Variance Approach

For **small risks** (or CARA-Normal framework), expected utility can be approximated by:

$$U \approx \mathbb{E}[x] - \frac{1}{2} A(\bar{x}) \cdot \text{Var}(x)$$

**Derivation (Taylor expansion around $\mu = \mathbb{E}[x]$):**

$$\mathbb{E}[u(x)] \approx u(\mu) + u'(\mu) \cdot 0 + \frac{1}{2} u''(\mu) \sigma^2$$

$$= u(\mu) + \frac{1}{2} u''(\mu) \sigma^2$$

The risk premium is approximately $RP \approx \frac{1}{2} A(\mu) \sigma^2$ — half the product of ARA and variance.

## Stochastic Dominance

**First-Order Stochastic Dominance (FSD):** Lottery $F$ dominates lottery $G$ in the FSD sense if for every non-decreasing $u$:

$$\int u\, dF \geq \int u\, dG$$

Equivalently: $F(x) \leq G(x)$ for all $x$ — the CDF of $F$ lies nowhere above the CDF of $G$.

**Second-Order Stochastic Dominance (SSD):** $F$ dominates $G$ for all non-decreasing **concave** $u$:

$$\int_a^x F(t)\, dt \leq \int_a^x G(t)\, dt \quad \forall x$$

SSD formalises "less risky" — if $F$ and $G$ have the same mean and $F$ SSD-dominates $G$, then $F$ has less spread.

## Related Concepts

- [[Utility_Function]] — the Bernoulli utility function $u(x)$ is the primitive of expected utility theory
- [[Preferences_and_Indifference_Curves]] — VNM axioms are preference axioms extended to lotteries
- [[Risk_and_Insurance]] — risk aversion creates demand for insurance; the CE and RP determine willingness to pay for coverage
- [[Intertemporal_Choice]] — intertemporal utility under uncertainty leads to the stochastic Euler equation
