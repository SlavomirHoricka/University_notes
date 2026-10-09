---
title: "Utility Function"
course: JEB104
topic: Consumer Theory
tags: [utility, ordinal-utility, MRS, monotone-transformation, Cobb-Douglas, consumer-theory]
date_created: 2026-04-19
---

# Utility Function

## Definition

A **utility function** $u: X \to \mathbb{R}$ is a real-valued function on the consumption set $X = \mathbb{R}^n_+$ that represents a preference relation $\succsim$:

$$u(x) \geq u(y) \iff x \succsim y$$

By Debreu's theorem, such a representation exists whenever $\succsim$ satisfies completeness, transitivity, and continuity. Monotonicity and convexity impose additional structure on $u$.

## Ordinal Nature of Utility

Consumer theory relies on the **ordinal** properties of utility — only the ordering of utility values matters, not their cardinal magnitude. Consequently:

**Theorem (Ordinal invariance):** If $u$ represents $\succsim$ and $f: \mathbb{R} \to \mathbb{R}$ is strictly increasing, then $\tilde{u} = f \circ u$ also represents $\succsim$.

Such a transformation $f$ is called a **positive monotone transformation**. All monotone transforms of $u$ represent the same preferences and yield identical demand behaviour.

## Marginal Utility and MRS

For a differentiable utility function, **marginal utility** with respect to good $i$ is:

$$MU_i = \frac{\partial u}{\partial x_i}$$

Under monotonicity, $MU_i > 0$ for all $i$.

The MRS between goods 1 and 2 is derived from the total differential condition $du = 0$ along an indifference curve:

$$MU_1 \, dx_1 + MU_2 \, dx_2 = 0 \implies MRS_{12} = -\frac{dx_2}{dx_1}\bigg|_{u=c} = \frac{MU_1}{MU_2}$$

**Important:** While the MRS equals $MU_1/MU_2$, it is invariant to monotone transformations (since the ratio cancels the derivative of $f$). The individual marginal utilities are not ordinal; the ratio is.

### Proof of MRS Invariance

Let $\tilde{u} = f(u)$. Then $\widetilde{MU}_i = f'(u) \cdot MU_i$. The transformed MRS:

$$\widetilde{MRS}_{12} = \frac{\widetilde{MU}_1}{\widetilde{MU}_2} = \frac{f'(u) MU_1}{f'(u) MU_2} = \frac{MU_1}{MU_2} = MRS_{12}$$

## Standard Utility Functions

### Cobb-Douglas

$$u(x_1, x_2) = x_1^a x_2^b \quad (a, b > 0)$$

- Indifference curves: strictly convex, smooth, asymptotic to axes
- MRS: $MRS_{12} = \frac{a x_2}{b x_1}$
- Monotone equivalent: $\tilde{u} = a \ln x_1 + b \ln x_2$
- Normalised form: $\tilde{u} = x_1^\alpha x_2^{1-\alpha}$ where $\alpha = a/(a+b)$
- Marshallian demand: $x_1^* = \frac{\alpha m}{p_1}$, $x_2^* = \frac{(1-\alpha)m}{p_2}$ (constant expenditure shares)

### Perfect Substitutes

$$u(x_1, x_2) = ax_1 + bx_2 \quad (a, b > 0)$$

- Indifference curves: straight lines, slope $-a/b$
- MRS constant: $MRS_{12} = a/b$
- Demand: corner solution unless $p_1/p_2 = a/b$ (any bundle on budget line)

### Perfect Complements

$$u(x_1, x_2) = \min\{ax_1, bx_2\} \quad (a, b > 0)$$

- Indifference curves: L-shaped, kink at $ax_1 = bx_2$
- MRS: undefined at kink; 0 or $\infty$ elsewhere
- Demand: always at kink, $ax_1^* = bx_2^*$

### Quasilinear

$$u(x_1, x_2) = v(x_1) + x_2 \quad (v' > 0, v'' < 0)$$

- Good 2 ("money") enters linearly; good 1 enters concavely
- MRS: $MRS_{12} = v'(x_1)$, depends only on $x_1$
- Indifference curves are vertical translates of each other
- No income effect on $x_1$ (see [[Marshallian_Demand]])

### Stone-Geary (Linear Expenditure System)

$$u(x_1, x_2) = (x_1 - \gamma_1)^{\alpha}(x_2 - \gamma_2)^{1-\alpha}$$

where $\gamma_i \geq 0$ are subsistence quantities. Demand has a Cobb-Douglas structure applied to spending above subsistence.

### CES (Constant Elasticity of Substitution)

$$u(x_1, x_2) = \left(a x_1^\rho + b x_2^\rho\right)^{1/\rho} \quad (\rho \leq 1, \rho \neq 0)$$

- Elasticity of substitution: $\sigma = 1/(1-\rho)$
- Special cases: $\rho \to 1$ (perfect substitutes), $\rho \to -\infty$ (perfect complements), $\rho \to 0$ (Cobb-Douglas)

## Convexity and Quasiconcavity

Strict convexity of preferences implies $u$ is **strictly quasiconcave**:

$$u(\lambda x + (1-\lambda)y) > \min\{u(x), u(y)\} \quad \forall \lambda \in (0,1), x \neq y$$

This is weaker than concavity. Quasiconcavity guarantees that upper contour sets $\{x : u(x) \geq k\}$ are convex — i.e., indifference curves are bowed toward the origin.

For the SOC of utility maximisation, the relevant condition is that the bordered Hessian of $u$ is negative definite, which holds under strict quasiconcavity.

## Related Concepts

- [[Preferences_and_Indifference_Curves]] — utility functions represent preference relations
- [[Utility_Maximization_and_Optimal_Choice]] — utility functions are the objective in the consumer's problem
- [[Marshallian_Demand]] — derived by maximising $u$ subject to the budget constraint
- [[Expenditure_Minimization_and_Hicksian_Demand]] — dual problem uses $u$ as a constraint
- [[Indirect_Utility_Function_and_Roys_Identity]] — the value function of the utility maximisation problem
