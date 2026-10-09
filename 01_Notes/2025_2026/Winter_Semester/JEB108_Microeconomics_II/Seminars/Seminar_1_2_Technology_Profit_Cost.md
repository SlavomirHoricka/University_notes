---
course: "JEB108"
topic: "Seminar Applications — Technology, Profit & Cost"
source: "00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Seminars/Seminar_1-2_Solutions.pdf"
tags: [JEB108, microeconomics, seminars, technology, profit, cost, exercises]
created: 2026-04-19
---
Parent: [[JEB108_Microeconomics_II_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Seminars/Seminar_1-2_Solutions.pdf]]
Related: [[Production_Technology]], [[Returns_to_Scale]], [[Profit_Maximization_Firm]], [[Cost_Minimization]]

# Seminar Applications — Technology, Profit & Cost (Seminars 1–2)

These exercises consolidate the theoretical foundations from Lectures 1–3 through worked problems on production functions, returns to scale, profit maximization, and cost minimization.

---

## Technology: Production Functions

### Worked Problems

**1. Cobb-Douglas — TRS and Returns to Scale**

Given $f(x_1, x_2) = x_1^{1/2} x_2^{1/2}$:

- $TRS = -\dfrac{MP_1}{MP_2} = -\dfrac{x_2}{x_1}$
- Returns to scale: $a + b = 1/2 + 1/2 = 1$ → **CRS**

**2. Linear Technology — Cost and TRS**

Given $f(x_1, x_2) = 2x_1 + 3x_2$:

- $TRS = -2/3$ (constant — inputs are perfect substitutes)
- If $w_1/w_2 < 2/3$: use only $x_1$; if $w_1/w_2 > 2/3$: use only $x_2$ (corner solution)

**3. Leontief Technology — Conditional Demands**

Given $f(x_1, x_2) = \min\{x_1, 2x_2\}$:

- Optimal ratio: $x_1 = 2x_2$ (kink point)
- Conditional demands: $x_1^* = y$, $x_2^* = y/2$
- Cost function: $c(w_1, w_2, y) = (w_1 + w_2/2)y$

---

## Profit Maximization: Key Questions

**Q:** Can a profit-maximizing firm facing perfect competition ever produce under IRS?

**A:** No — under IRS, if profits are positive at any scale, scaling all inputs by $t > 1$ raises profit by factor $t > 1$, so no finite optimum exists. The competitive IRS firm either shuts down or is not a well-defined optimizer.

**Q:** What does the Weak Axiom of Profit Maximization (WAPM) imply?

**A:** $\Delta p \cdot \Delta y - \Delta w_1 \cdot \Delta x_1 - \Delta w_2 \cdot \Delta x_2 \geq 0$. This is a revealed-preference inequality that:
- Implies supply is upward-sloping ($\Delta p \cdot \Delta y \geq 0$ when only $p$ changes)
- Implies factor demand is downward-sloping in own price ($-\Delta w_i \cdot \Delta x_i \geq 0$)

---

## Cost Minimization: Exercises

**1. Cobb-Douglas — $f(x_1, x_2) = x_1^{1/3} x_2^{2/3}$**

At $y = 48$, $w_1 = 4$, $w_2 = 64$:

TRS condition: $\displaystyle\frac{w_1}{w_2} = \frac{MP_1}{MP_2} = \frac{(1/3)x_2}{(2/3)x_1} = \frac{x_2}{2x_1}$

$$\frac{4}{64} = \frac{x_2}{2x_1} \Rightarrow x_2 = \frac{x_1}{8}$$

Substituting into constraint: $x_1^{1/3}(x_1/8)^{2/3} = 48 \Rightarrow x_1 \cdot (1/8)^{2/3} = 48$

$(1/8)^{2/3} = 1/4 \Rightarrow x_1 = 48 \times 4 = 192$, $x_2 = 192/8 = 24$

Minimized cost: $c = 4(192) + 64(24) = 768 + 1536 = \mathbf{2304}$

**2. Corner Solution — $f(x_1, x_2) = \sqrt{x_1 + 5} + 2\sqrt{x_2}$**

At $y_0 = 50$, $w_1 = 12$, $w_2 = 2$:

Check interior: $TRS = -\dfrac{1/(2\sqrt{x_1+5})}{1/\sqrt{x_2}} = -\dfrac{\sqrt{x_2}}{2\sqrt{x_1+5}}$

Interior condition: $\dfrac{w_1}{w_2} = 6 = \dfrac{\sqrt{x_2}}{2\sqrt{x_1+5}}$

This implies $12\sqrt{x_1+5} = \sqrt{x_2}$, i.e., $x_2 = 144(x_1+5)$ — a very large quantity of $x_2$ needed. Check corner $x_1 = 0$: $\sqrt{5} + 2\sqrt{x_2} = 50 \Rightarrow x_2 = [(50 - \sqrt{5})/2]^2 \approx 551$. Check interior: $\sqrt{x_2} = 12\sqrt{x_1+5}$ gives even higher cost. → **Corner solution at $x_1 = 0$**.

---

## Opportunity Cost

**Opportunity cost** is the value of the next-best foregone alternative — the correct concept for all economic cost calculations.

**Exercise (Eric Clapton concert):**
- You have a free Clapton ticket (non-resalable).
- Alternative: Bob Dylan concert at \$40, for which you'd pay up to \$50.
- Net value of Dylan: $50 - 40 = \$10$ (consumer surplus foregone).
- **Opportunity cost of attending Clapton = \$10** (the surplus you give up, not the ticket price).

This illustrates that opportunity cost is not the ticket price but the *net* value of the best alternative.
