---
title: "Indirect Utility Function and Roy's Identity"
course: JEB104
topic: Consumer Theory
tags: [indirect-utility, Roy-identity, value-function, consumer-theory, duality]
date_created: 2026-04-19
---

# Indirect Utility Function and Roy's Identity

## Definition

The **indirect utility function** $v(p, m)$ is the value function of the Utility Maximization Problem (UMP):

$$v(p, m) = \max_{x \geq 0} \; u(x) \quad \text{s.t.} \quad p \cdot x \leq m$$

It gives the maximum utility attainable at prices $\mathbf{p}$ and income $m$:

$$v(p, m) = u(x^*(p, m))$$

## Properties of $v(p, m)$

**P1 — Homogeneous of degree zero in $(p, m)$:**
$$v(\lambda p, \lambda m) = v(p, m) \quad \forall \lambda > 0$$
Multiplying all prices and income by $\lambda$ leaves the budget set unchanged.

**P2 — Non-increasing in $p_i$:**
$$\frac{\partial v}{\partial p_i} \leq 0$$
Higher prices can only reduce attainable utility (the feasible set shrinks).

**P3 — Non-decreasing in $m$:**
$$\frac{\partial v}{\partial m} \geq 0$$
Higher income allows at least the same choices as before.

**P4 — Quasi-convex in $p$ (for fixed $m$):**

The set $\{(p, m) : v(p, m) \leq k\}$ is convex for all $k$. Intuitively, if the consumer can achieve utility $k$ at prices $p$ and $p'$, they can also do so at any convex combination of prices.

**P5 — Continuous in $(p, m)$** when $u$ is continuous and $p \gg 0$.

## Roy's Identity

**Roy's Identity** recovers the Marshallian demand function from the indirect utility function:

$$x_i^*(p, m) = -\frac{\partial v / \partial p_i}{\partial v / \partial m}$$

### Derivation via Envelope Theorem

Differentiating $v(p, m) = u(x^*(p, m))$ with respect to $p_i$:

$$\frac{\partial v}{\partial p_i} = \nabla_x u(x^*) \cdot \frac{\partial x^*}{\partial p_i} = \lambda^* \mathbf{p} \cdot \frac{\partial x^*}{\partial p_i}$$

where the last step uses the FOC $\nabla_x u = \lambda^* \mathbf{p}$.

Differentiating the budget constraint $\mathbf{p} \cdot x^* = m$ with respect to $p_i$:

$$x_i^* + \mathbf{p} \cdot \frac{\partial x^*}{\partial p_i} = 0 \implies \mathbf{p} \cdot \frac{\partial x^*}{\partial p_i} = -x_i^*$$

Therefore:

$$\frac{\partial v}{\partial p_i} = -\lambda^* x_i^*$$

Similarly, differentiating with respect to $m$: $\frac{\partial v}{\partial m} = \lambda^*$.

Combining:

$$x_i^* = -\frac{\partial v / \partial p_i}{\partial v / \partial m} = -\frac{\partial v / \partial p_i}{\lambda^*}$$

**Interpretation:** The Lagrange multiplier $\lambda^* = \partial v / \partial m$ is the **marginal utility of income**. Roy's identity states that the demand for good $i$ equals minus the price-shadow of $v$ divided by the income-shadow.

## Cobb-Douglas Example

For $u = x_1^\alpha x_2^{1-\alpha}$, the Marshallian demands are $x_1^* = \alpha m / p_1$ and $x_2^* = (1-\alpha)m/p_2$, so:

$$v(p, m) = \left(\frac{\alpha m}{p_1}\right)^\alpha \left(\frac{(1-\alpha)m}{p_2}\right)^{1-\alpha} = m \cdot \frac{\alpha^\alpha (1-\alpha)^{1-\alpha}}{p_1^\alpha p_2^{1-\alpha}}$$

**Verification of Roy's Identity:**

$$\frac{\partial v}{\partial p_1} = -\frac{\alpha}{p_1} v(p,m)$$

$$\frac{\partial v}{\partial m} = \frac{v(p,m)}{m}$$

$$-\frac{\partial v/\partial p_1}{\partial v/\partial m} = \frac{(\alpha/p_1) v}{v/m} = \frac{\alpha m}{p_1} = x_1^* \checkmark$$

## Duality Relations

The indirect utility function and expenditure function are related by:

$$v(p, e(p, \bar{u})) = \bar{u}$$
$$e(p, v(p, m)) = m$$

These are the fundamental duality identities (see [[Duality]]). They allow recovery of one function from the other.

## Related Concepts

- [[Utility_Maximization_and_Optimal_Choice]] — $v$ is the value function of the UMP
- [[Expenditure_Minimization_and_Hicksian_Demand]] — $e$ is the dual value function of the EMP
- [[Marshallian_Demand]] — Roy's identity recovers $x_i^*$ from $v$
- [[Duality]] — the relationship $v(p,e(p,u))=u$ and $e(p,v(p,m))=m$
- [[Slutsky_Equation]] — derivable from differentiating the duality identity
