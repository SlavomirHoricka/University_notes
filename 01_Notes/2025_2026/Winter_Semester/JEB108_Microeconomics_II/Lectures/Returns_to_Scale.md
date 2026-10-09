---
course: "JEB108"
topic: "Returns to Scale"
source: "00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Lectures/1_technology-1.pdf"
tags: [JEB108, microeconomics, production, returns-to-scale]
created: 2026-04-19
---
Parent: [[JEB108_Microeconomics_II_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Lectures/1_technology-1.pdf]]
Related: [[Production_Technology]], [[Cost_Minimization]], [[Profit_Maximization_Firm]], [[Firm_Supply_Curve]]

# Returns to Scale

## Definition

**Returns to scale** describe how output responds when **all** inputs are scaled by a common factor $t > 1$:

$$f(tx_1, tx_2, \ldots, tx_n) \text{ vs. } t \cdot f(x_1, x_2, \ldots, x_n)$$

This is a global (or local) property of the production function characterising the scale behaviour of technology.

---

## Types of Returns to Scale

### Constant Returns to Scale (CRS)

$$f(tx_1, \ldots, tx_n) = t \cdot f(x_1, \ldots, x_n) \quad \forall t > 0$$

Doubling all inputs exactly doubles output. The production function is **homogeneous of degree 1**.

**Example:** Cobb-Douglas $f = x_1^a x_2^b$ exhibits CRS when $a + b = 1$:
$$f(tx_1, tx_2) = (tx_1)^a(tx_2)^b = t^{a+b} x_1^a x_2^b = t \cdot f(x_1, x_2)$$

**Implication for long-run supply:** Under CRS, the firm's supply curve is **horizontal** at $p = AC = MC$ (see [[Firm_Supply_Curve]]).

### Increasing Returns to Scale (IRS)

$$f(tx_1, \ldots, tx_n) > t \cdot f(x_1, \ldots, x_n) \quad \text{for } t > 1$$

Scaling inputs by $t$ more than scales output by $t$. Arises from specialisation, indivisibilities, geometric relationships.

**Example:** Cobb-Douglas with $a + b > 1$.

**Implication:** Average cost is **decreasing** in output; natural monopoly tendencies (see [[Monopoly]]).

### Decreasing Returns to Scale (DRS)

$$f(tx_1, \ldots, tx_n) < t \cdot f(x_1, \ldots, x_n) \quad \text{for } t > 1$$

Scaling all inputs by $t$ less than scales output — typically arising from management/coordination inefficiencies or hidden fixed factors.

**Example:** Cobb-Douglas with $a + b < 1$.

---

## Relationship to Profit Maximization

Returns to scale have critical implications for the existence of a profit maximum (see [[Profit_Maximization_Firm]]):

| Returns to Scale | Profit under Perfect Competition |
|---|---|
| CRS | $\pi = 0$ at optimum or $\pi \to \infty$ (no finite max) |
| IRS | No finite profit maximum (produce without bound) |
| DRS | Unique, finite profit maximum exists |

**Proof sketch (CRS):** If $\pi(y^*) > 0$ at scale $\lambda = 1$, then at scale $\lambda > 1$: $p \cdot \lambda f(x) - \lambda w \cdot x = \lambda \pi(y^*) > \pi(y^*)$, so no finite maximum exists. Hence under CRS, the only equilibrium is $\pi = 0$.

---

## Local vs. Global Returns to Scale

Returns to scale may vary at different output levels. The **local returns to scale** at $y_0$ can be measured by the **output elasticity**:

$$\varepsilon(y) = \frac{d \ln f}{d \ln t}\bigg|_{x = x^*} = \sum_{i=1}^n \frac{\partial f}{\partial x_i} \cdot \frac{x_i}{f(x)}$$

where $\varepsilon > 1$ indicates local IRS, $\varepsilon = 1$ local CRS, $\varepsilon < 1$ local DRS. This quantity equals the sum of output elasticities: for Cobb-Douglas $f = x_1^a x_2^b$, $\varepsilon = a + b$.

---

## Short-Run vs. Long-Run Perspective

In the **short run**, some inputs are fixed, so returns to scale are not directly applicable — only variable inputs are scaled. In the **long run**, all inputs can be adjusted, and returns to scale fully characterise cost behaviour.

Link: [[Cost_Minimization]] — cost function concavity/convexity is directly determined by returns to scale.
