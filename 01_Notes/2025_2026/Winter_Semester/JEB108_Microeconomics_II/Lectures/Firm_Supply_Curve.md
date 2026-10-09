---
course: "JEB108"
topic: "Firm Supply Curve"
source: "00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Lectures/5_firm_supply-4.pdf"
tags: [JEB108, microeconomics, supply, firm-behaviour, competitive-firm]
created: 2026-04-19
---
Parent: [[JEB108_Microeconomics_II_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Lectures/5_firm_supply-4.pdf]]
Related: [[Profit_Maximization_Firm]], [[Cost_Curves]], [[Cost_Minimization]], [[Industry_Equilibrium]], [[Marshallian_Demand]]

# Firm Supply Curve

## Definition

The **firm supply curve** $S(p)$ assigns to every output price $p$ the output level $y^*$ that maximises the firm's profit:

$$S(p) = \arg\max_y \{py - TC(y)\}$$

For a competitive firm (price-taker), this is derived directly from the profit maximization conditions.

---

## Derivation: Interior Supply

When the firm produces a **strictly positive** output:

**FOC:** $p = MC(y^*)$
**SOC:** $dMC/dy > 0$ (upward-sloping portion of MC)

Inverting $MC$: the firm's **inverse supply function** is $p = MC(y)$.
The **supply function** $y = S(p)$ is the inverse of $MC$ restricted to the upward-sloping section.

---

## Shut-Down Condition

### Short Run

In the short run, fixed costs $FC$ are unavoidable. The firm:
- **Produces** if revenue ≥ variable costs: $py \geq VC(y) \Rightarrow p \geq AVC$
- **Shuts down** if $p < \min(AVC)$

**Short-run firm supply:**
$$S^{SR}(p) = \begin{cases} MC^{-1}(p) & \text{if } p \geq \min(AVC) \\ 0 & \text{if } p < \min(AVC) \end{cases}$$

### Long Run

In the long run, all costs are variable. The firm:
- **Produces** if revenue ≥ total costs: $py \geq TC(y) \Rightarrow p \geq ATC$
- **Exits** if $p < \min(ATC)$

**Long-run firm supply:**
$$S^{LR}(p) = \begin{cases} MC^{-1}(p) & \text{if } p \geq \min(ATC) \\ 0 & \text{if } p < \min(ATC) \end{cases}$$

**Key threshold:** $\min(ATC)$ is the **break-even price** — the minimum price at which the firm is willing to operate in the long run.

---

## Graphical Representation

The firm supply curve under perfect competition is the **upward-sloping portion of the MC curve** that lies **at or above** $\min(AVC)$ (short run) or $\min(ATC)$ (long run).

---

## Special Case: Constant Returns to Scale

Under CRS, $MC = ATC$ at all output levels (both constant). The firm's supply curve is:
- **Horizontal** at $p = AC = MC$
- Any quantity is produced at this price; the firm is indifferent about scale.

---

## Comparative Statics

### Effect of Output Price on Supply

From FOC $p = MC(y^*)$, differentiating implicitly:

$$\frac{dy^*}{dp} = \frac{1}{MC'(y^*)} > 0$$

since $MC' > 0$ by SOC. **Supply is increasing in price.**

### Effect of Input Price

An increase in $w_i$ shifts the MC curve upward → supply curve shifts **inward** (less output at every price).

---

## Short-Run vs. Long-Run Supply Elasticity

The long-run supply curve is more **elastic** (flatter) than the short-run supply curve because:
- In the short run, output can only expand by increasing variable inputs.
- In the long run, the firm can also expand fixed capital.

$$\varepsilon_{S}^{LR} > \varepsilon_{S}^{SR}$$

---

## Exercise

**Setup:** $TC(y) = 2y^3 - 30y^2 + 150y$

**Q1:** $S(p) = ?$ at $p = 6$:
- $MC = 6y^2 - 60y + 150$
- $AVC = 2y^2 - 30y + 150$ (no fixed costs, so $AVC = ATC$)
- $\min(AVC)$: $dAVC/dy = 4y - 30 = 0 \Rightarrow y = 7.5$, $\min(AVC) = 2(56.25) - 30(7.5) + 150 = 112.5 - 225 + 150 = 37.5$
- Since $p = 6 < 37.5 = \min(ATC)$, **firm shuts down**: $S(6) = 0$.

**Q2: Inverse supply function** (for $p \geq 37.5$):
$$p = MC = 6y^2 - 60y + 150$$

**Q3: Supply function:** Solving $6y^2 - 60y + (150-p) = 0$:
$$y = \frac{60 + \sqrt{3600 - 24(150-p)}}{12} = 5 + \frac{\sqrt{600 + 24p - 3600}}{12} = 5 + \frac{\sqrt{24p - 3000}}{12}$$

(taking the root that corresponds to the upward-sloping portion of MC, i.e., SOC satisfied).
