---
title: "Preferences and Indifference Curves"
course: JEB104
topic: Consumer Theory
tags: [preferences, indifference-curves, MRS, axioms, consumer-theory]
date_created: 2026-04-19
---

# Preferences and Indifference Curves

## Binary Preference Relation

A consumer's preferences are represented by a binary relation $\succsim$ on the consumption set $X = \mathbb{R}^n_+$:

- $x \succsim y$: "$x$ is at least as good as $y$" (weak preference)
- $x \succ y$: "$x$ is strictly preferred to $y$" ($x \succsim y$ but not $y \succsim x$)
- $x \sim y$: "$x$ is indifferent to $y$" ($x \succsim y$ and $y \succsim x$)

## Preference Axioms

### A1 — Completeness
For all $x, y \in X$: $x \succsim y$ or $y \succsim x$ (or both).

Every pair of bundles is comparable. The consumer is never "indecisive."

### A2 — Reflexivity
For all $x \in X$: $x \succsim x$.

Any bundle is at least as good as itself.

### A3 — Transitivity
For all $x, y, z \in X$: if $x \succsim y$ and $y \succsim z$, then $x \succsim z$.

Preferences are consistent — no intransitive cycles.

### A4 — Continuity
For all $y \in X$, the sets $\{x : x \succsim y\}$ (upper contour set) and $\{x : y \succsim x\}$ (lower contour set) are both closed.

Continuity rules out "jumps" in preferences and guarantees existence of a continuous utility representation.

### A5 — Monotonicity (Non-satiation)
For all $x, y \in X$: if $x_i \geq y_i$ for all $i$ and $x_j > y_j$ for at least one $j$, then $x \succ y$.

More of every good is strictly preferred. **Weak monotonicity** requires only $x \succsim y$.

### A6 — Convexity
For all $x, y \in X$ with $x \sim y$ and $\lambda \in [0,1]$: $\lambda x + (1-\lambda)y \succsim y$.

**Strict convexity:** $\lambda x + (1-\lambda)y \succ y$ for $\lambda \in (0,1)$ and $x \neq y$.

Convexity captures the notion of a "preference for variety" — mixtures are weakly preferred to extremes. Geometrically, upper contour sets are convex.

## Indifference Curves

The **indifference curve** through bundle $y$ is:

$$IC(y) = \{x \in X : x \sim y\}$$

### Properties Under A1–A6

1. **Completeness and transitivity** imply indifference curves partition $X$ — every bundle lies on exactly one indifference curve.
2. **Monotonicity** implies indifference curves are downward-sloping: to maintain indifference, increasing $x_1$ requires decreasing $x_2$.
3. **Monotonicity** further implies indifference curves cannot be thick bands.
4. **Transitivity** implies indifference curves never cross. (Proof: Suppose $x \sim y$ and $x \sim z$ at a crossing point $x$, but $y \succ z$ elsewhere. Then transitivity requires $y \sim z$, contradicting $y \succ z$.)
5. **Convexity** implies indifference curves are bowed toward the origin — upper contour sets are convex.

## Marginal Rate of Substitution

The **Marginal Rate of Substitution (MRS)** at bundle $(x_1, x_2)$ is the rate at which the consumer is willing to trade good 2 for good 1 while remaining on the same indifference curve:

$$MRS_{12} = -\frac{dx_2}{dx_1}\bigg|_{u = \text{const}}$$

The MRS is the absolute value of the slope of the indifference curve.

### Diminishing MRS

Under strict convexity, the MRS is **diminishing** along an indifference curve: as $x_1$ increases (and $x_2$ decreases), the consumer values additional units of $x_1$ less relative to $x_2$. This is equivalent to the indifference curve being strictly convex (bowed inward).

## Special Preference Types

### Perfect Substitutes
$$u(x_1, x_2) = ax_1 + bx_2$$

Indifference curves are straight lines with constant slope $-a/b$. Optimal choice is typically a corner solution.

### Perfect Complements
$$u(x_1, x_2) = \min\{ax_1, bx_2\}$$

Indifference curves are L-shaped with kink at $ax_1 = bx_2$. Optimal choice always at the kink.

### Cobb-Douglas
$$u(x_1, x_2) = x_1^a x_2^b$$

Smooth, strictly convex indifference curves. Interior solutions at $MRS = p_1/p_2$.

### Quasilinear
$$u(x_1, x_2) = v(x_1) + x_2$$

Indifference curves are vertical translates of each other. No income effect on $x_1$.

### Satiation
Preferences exhibit satiation (bliss point) — more is not always better. Indifference curves may be closed curves around the bliss point.

## Relationship to Utility Representation

By a theorem of Debreu (1954), if $\succsim$ satisfies completeness, transitivity, and continuity, there exists a continuous utility function $u: X \to \mathbb{R}$ such that:

$$x \succsim y \iff u(x) \geq u(y)$$

See [[Utility_Function]] for details on the utility representation and its properties.

## Related Concepts

- [[Budget_Constraint]] — the budget set determines which bundles are affordable; preferences determine which is best
- [[Utility_Function]] — a numerical representation of preferences
- [[Utility_Maximization_and_Optimal_Choice]] — optimal choice requires tangency of indifference curve and budget line
- [[Marshallian_Demand]] — derived from utility maximisation over the budget set
- [[Income_and_Substitution_Effects]] — decomposition uses the indifference curve structure
