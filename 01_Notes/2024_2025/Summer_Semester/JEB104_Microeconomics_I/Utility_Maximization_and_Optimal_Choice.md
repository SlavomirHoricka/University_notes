---
title: "Utility Maximization and Optimal Choice"
course: JEB104
topic: Consumer Theory
tags: [utility-maximization, Lagrangian, FOC, KKT, corner-solution, consumer-theory]
date_created: 2026-04-19
---

# Utility Maximization and Optimal Choice

## The Consumer's Problem

The consumer chooses a consumption bundle $(x_1, x_2)$ to solve:

$$\max_{x_1, x_2} \; u(x_1, x_2) \quad \text{subject to} \quad p_1 x_1 + p_2 x_2 = m, \quad x_1, x_2 \geq 0$$

**Existence:** By Weierstrass's theorem, a maximum exists if $u$ is continuous and the budget set is compact (closed and bounded). The budget set $\{x \in \mathbb{R}^2_+ : p_1 x_1 + p_2 x_2 \leq m\}$ is compact when $p \gg 0$, $m \geq 0$.

**Uniqueness:** Strict quasiconcavity of $u$ guarantees a unique interior solution (when it exists).

## Interior Solution: Lagrangian Method

For an interior optimum $(x_1^*, x_2^*) \gg 0$, form the Lagrangian:

$$\mathcal{L}(x_1, x_2, \lambda) = u(x_1, x_2) - \lambda (p_1 x_1 + p_2 x_2 - m)$$

**First-Order Conditions (FOCs):**

$$\frac{\partial \mathcal{L}}{\partial x_1} = \frac{\partial u}{\partial x_1} - \lambda p_1 = 0 \implies MU_1 = \lambda p_1$$

$$\frac{\partial \mathcal{L}}{\partial x_2} = \frac{\partial u}{\partial x_2} - \lambda p_2 = 0 \implies MU_2 = \lambda p_2$$

$$\frac{\partial \mathcal{L}}{\partial \lambda} = p_1 x_1 + p_2 x_2 - m = 0$$

### Optimality Condition

Dividing the first two FOCs:

$$\frac{MU_1}{MU_2} = \frac{p_1}{p_2} \implies MRS_{12} = \frac{p_1}{p_2}$$

**Interpretation:** At the optimum, the rate at which the consumer is willing to trade good 2 for good 1 (the MRS) equals the rate at which the market allows such a trade (the price ratio). Equivalently:

$$\frac{MU_1}{p_1} = \frac{MU_2}{p_2} = \lambda$$

The Lagrange multiplier $\lambda$ is the **marginal utility of income** — the increase in maximal utility per unit increase in $m$.

### Geometric Interpretation

The optimum occurs where the highest attainable indifference curve is tangent to the budget line. At a tangency, the slope of the indifference curve ($-MRS$) equals the slope of the budget line ($-p_1/p_2$).

## Corner Solutions

When the tangency condition cannot be satisfied in the interior, the optimum occurs at a corner $(x_1^* = 0$ or $x_2^* = 0)$.

### Kuhn-Tucker Conditions

The general necessary conditions (assuming $u$ is differentiable, $x_i \geq 0$):

$$MU_1 - \lambda p_1 \leq 0, \quad x_1 (MU_1 - \lambda p_1) = 0$$
$$MU_2 - \lambda p_2 \leq 0, \quad x_2 (MU_2 - \lambda p_2) = 0$$
$$p_1 x_1 + p_2 x_2 = m, \quad \lambda \geq 0$$

**Complementary slackness:** $x_i > 0 \implies MU_i = \lambda p_i$ (FOC holds with equality); $MU_i < \lambda p_i \implies x_i = 0$ (corner solution for good $i$).

### Perfect Substitutes Example

For $u = ax_1 + bx_2$: $MU_1/p_1 = a/p_1$ and $MU_2/p_2 = b/p_2$.

- If $a/p_1 > b/p_2$: spend all income on good 1 ($x_1^* = m/p_1$, $x_2^* = 0$)
- If $a/p_1 < b/p_2$: spend all income on good 2 ($x_1^* = 0$, $x_2^* = m/p_2$)
- If $a/p_1 = b/p_2$: any bundle on the budget line is optimal

### Perfect Complements Example

For $u = \min\{x_1, x_2\}$ with $p_1, p_2 > 0$: optimum at $x_1^* = x_2^*$. Substituting into the budget constraint: $x_1^* = x_2^* = m/(p_1 + p_2)$.

## Kinked Budget Constraints

When the budget constraint has a kink (e.g., quantity discounts, rationing, in-kind transfers), the optimum may occur at the kink. At a kink, the MRS condition becomes an inequality:

$$MRS_{\text{right}} \leq \frac{p_1}{p_2} \leq MRS_{\text{left}}$$

where $MRS_{\text{left}}$ and $MRS_{\text{right}}$ are the limits of the MRS from each side.

## Second-Order Conditions

For a true maximum (not a minimum or saddle point), the bordered Hessian of the Lagrangian must be negative definite. For the two-good case, this requires:

$$\begin{vmatrix} 0 & p_1 & p_2 \\ p_1 & u_{11} & u_{12} \\ p_2 & u_{21} & u_{22} \end{vmatrix} > 0$$

Under strict quasiconcavity, this condition is satisfied.

## Demand Functions

Solving the FOCs simultaneously yields the **Marshallian (Walrasian) demand functions**:

$$x_i^*(p_1, p_2, m) = \underset{x}{\arg\max} \; u(x) \quad \text{s.t.} \quad p \cdot x = m$$

See [[Marshallian_Demand]] for full treatment of these functions and their properties.

## Related Concepts

- [[Budget_Constraint]] — defines the feasible set
- [[Preferences_and_Indifference_Curves]] — the indifference curves whose tangency determines the optimum
- [[Utility_Function]] — the objective function
- [[Marshallian_Demand]] — the demand functions derived from this problem
- [[Indirect_Utility_Function_and_Roys_Identity]] — the value function $v(p,m) = u(x^*(p,m))$
- [[Expenditure_Minimization_and_Hicksian_Demand]] — the dual problem
