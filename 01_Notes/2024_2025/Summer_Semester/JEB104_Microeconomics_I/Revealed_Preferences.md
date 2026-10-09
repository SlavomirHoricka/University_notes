---
course: JEB104
topic: Revealed Preference Theory
source: 00_Materials/2024_2025/Summer_Semester/JEB104_Microeconomics_I/JEB104_10_Revealed_preferences_Students.pdf
tags: [JEB104, microeconomics, revealed-preference, WARP, SARP, demand]
created: 2026-04-19
---

Parent: [[JEB104_Microeconomics_I_main]]
Source: [[00_Materials/2024_2025/Summer_Semester/JEB104_Microeconomics_I/JEB104_10_Revealed_preferences_Students.pdf]]
Related: [[Marshallian_Demand]], [[Slutsky_Equation]], [[Preferences_and_Indifference_Curves]], [[Utility_Function]]

# Revealed Preference Theory

## Motivation

Classical preference theory starts from **unobservable** preferences and derives observable demand behaviour. Revealed preference inverts this: starting from **observed demand choices**, it recovers and tests preference properties without assuming a utility function.

**Core idea:** If a consumer chooses bundle $x$ when $y$ is also affordable, then $x$ is *revealed preferred* to $y$.

## Direct Revealed Preference

**Definition:** Bundle $x$ is **directly revealed preferred** to bundle $y$, written $x \succ^R y$ (or $x R y$), if:

$$p \cdot x \leq m \quad \text{and} \quad x \neq y$$

i.e., $y$ was affordable when $x$ was chosen.

## Weak Axiom of Revealed Preference (WARP)

**Statement:** If $x$ is directly revealed preferred to $y$, then $y$ cannot be directly revealed preferred to $x$:

$$x R y \implies \neg(y R x)$$

**Formally:** If $(p, m)$ yields choice $x$ and $(p', m')$ yields choice $y$, and

$$p \cdot y \leq m$$

then it must **not** be the case that $p' \cdot x \leq m'$.

### Implications of WARP

WARP is the observable counterpart of preference consistency (transitivity + completeness). It implies:

1. **Slutsky matrix is NSD:** The matrix $S$ with entries $S_{ij} = \partial h_i/\partial p_j$ is negative semi-definite.
2. **Own-price Slutsky terms are non-positive:** $S_{ii} \leq 0$, consistent with compensated demand being downward sloping.
3. **WARP does not fully characterise rationality** in multi-good settings — stronger conditions are needed.

### WARP and the Law of Demand

Under WARP, for any two price-income pairs:

$$(\mathbf{p}' - \mathbf{p}) \cdot (\mathbf{x}' - \mathbf{x}) \leq 0$$

when the income change is the **Slutsky compensation**: $m' = p' \cdot x$. This states that compensated demand moves opposite to price changes.

**Proof sketch:**
- $m' = p' \cdot x$ means $x$ is affordable at $(p', m')$, so $y = x$ is an alternative; by WARP, $p' \cdot x' \leq m' = p' \cdot x$.
- At $(p, m)$, $x$ was chosen and $x'$ was affordable: $p \cdot x' \leq m = p \cdot x$.
- Adding: $(p' - p) \cdot x \geq (p' - p) \cdot x'$, i.e., $\Delta p \cdot \Delta x \leq 0$. $\blacksquare$

## Strong Axiom of Revealed Preference (SARP)

WARP only covers **direct** revealed preferences. **SARP** extends this to the transitive closure:

**Definition:** $x$ is **indirectly revealed preferred** to $z$ if there exists a chain $x R y_1 R y_2 R \ldots R z$.

**SARP:** No bundle can be indirectly revealed preferred to itself. The revealed preference relation $R^*$ must be **acyclic**.

### WARP vs SARP

| Property | WARP | SARP |
|----------|------|------|
| Covers | Direct comparisons | Transitive closure |
| Equivalent to | NSD Slutsky matrix | Full rationalisability by preferences |
| Requires | Consistency of pairwise choices | Global consistency |

With **two goods**, WARP implies SARP. With **three or more goods**, they diverge.

## Rationalisation

**Theorem (Afriat, 1967):** A finite data set $\{(p^t, x^t)\}_{t=1}^T$ is rationalised by a locally non-satiated utility function if and only if it satisfies **SARP** (equivalently, the **General Axiom of Revealed Preference, GARP**).

**GARP:** If $x^s$ is revealed preferred (weakly) to $x^t$, then $x^t$ cannot be strictly directly revealed preferred to $x^s$.

Afriat's theorem is constructive: given GARP, one can explicitly build a concave, continuous utility function that rationalises the data.

## Testability of Demand

Revealed preference allows **non-parametric testing** of utility maximisation:

1. Collect price-quantity observations $(p^t, x^t)$.
2. Check GARP.
3. If GARP holds: data is consistent with rational behaviour.
4. If GARP is violated: at least one choice is irrational.

**Afriat efficiency index:** Measures how close a data set is to satisfying GARP, allowing for small optimisation errors.

## Demand Restrictions from WARP

From WARP, for **compensated** price changes, the **substitution matrix** $S$ satisfies:
- **Symmetry:** $S_{ij} = S_{ji}$ (requires SARP / full rationalisability; WARP alone implies NSD but not symmetry in general).
- **NSD:** $v^T S v \leq 0 \ \forall v$.
- **$S p = 0$:** Euler's theorem / homogeneity.

## Related Concepts

- [[Preferences_and_Indifference_Curves]] — the preference relation that revealed preference seeks to recover
- [[Marshallian_Demand]] — the observed demand function that revealed preference tests
- [[Slutsky_Equation]] — the Slutsky matrix inherits properties from WARP / SARP
- [[Duality]] — duality theory provides the bridge from observed demand to expenditure / utility functions
- [[Utility_Function]] — Afriat's theorem guarantees a rationalising utility function under SARP / GARP
