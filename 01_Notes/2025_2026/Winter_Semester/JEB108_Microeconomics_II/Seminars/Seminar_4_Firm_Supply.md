---
course: "JEB108"
topic: "Seminar Applications — Firm Supply"
source: "00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Seminars/Seminar_4_Solutions.pdf"
tags: [JEB108, microeconomics, seminars, firm-supply, competitive-firm]
created: 2026-04-19
---
Parent: [[JEB108_Microeconomics_II_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Seminars/Seminar_4_Solutions.pdf]]
Related: [[Firm_Supply_Curve]], [[Cost_Curves]], [[Profit_Maximization_Firm]]

# Seminar Applications — Firm Supply (Seminar 4)

Applied derivation of supply curves from cost functions, with emphasis on shut-down conditions, inverse supply, and Leontief-based cost structures.

---

## Conceptual Review Questions

**Q: Is the short-run supply curve more or less elastic than the long-run supply curve?**

**A:** The **long-run supply curve is more elastic**. In the short run, some inputs are fixed, constraining the firm's ability to expand output. In the long run, all inputs are adjustable and the firm can also enter or exit, making it more responsive to price changes. The two curves intersect at the output level where the fixed short-run capital stock equals the optimal long-run choice.

**Q: In the MR = MC identity for a perfectly competitive firm, what is MR?**

**A:** Since the firm is a price-taker, $MR = p$ — it receives a constant price for each additional unit sold. Thus the FOC $p = MC$ holds directly.

**Q: Can a perfectly competitive firm produce with negative profit in the short run?**

**A:** Yes — but only down to $\pi = -FC$. If $p \geq \min(AVC)$, the firm covers variable costs and reduces its losses relative to shutting down (at which profit $= -FC$). Staying open is rational as long as $TR \geq VC$.

---

## Worked Problems

### Problem 1 — $TC(y) = (y-2)^2 + 1$

**AC, MC, intersection:**

$$AC = y - 4 + \frac{5}{y}, \quad MC = 2y - 4$$

$MC = AC$ at $y = \sqrt{5}$, $p_{\min AC} = 2\sqrt{5} - 4 \approx 0.47$.

**Profit at $y = 5$:** $\pi = py - TC = 5p - [(5-2)^2 + 1] = 5p - 10$.

### Problem 2 — $LTC(y) = 3y^3 - 8y^2 - 11y$ (long-run, no FC)

**Inverse supply:** $S^{-1}(y^*) = LMC = 9y^2 - 16y - 11$ for $y \geq 4/3$

**Minimum price:** $p_0 = \min(LAC) \approx -49/3$ → effectively $p_0 = 0$

**Supply function:** $S(p) = \dfrac{8 + \sqrt{163 + 9p}}{9}$

### Problem 3 — $STC = y^3 - 80y^2 + 2{,}500y + 40{,}000$

$p_0 = \min(AVC) = 900$ → firm shuts down for $p < 900$.

$S(p) = \dfrac{80 + \sqrt{3p - 1{,}100}}{3}$ for $p \geq 900$.

### Problem 4 — Leontief Technology: $f(x_1, x_2) = (\min\{3x_1, 2x_2\})^2$

**Conditional demands:** At the optimum, $3x_1 = 2x_2 = \sqrt{y}$, so:

$$x_1^* = \frac{\sqrt{y}}{3}, \quad x_2^* = \frac{\sqrt{y}}{2}$$

**Cost function:**

$$c(w_1, w_2, y) = w_1 \frac{\sqrt{y}}{3} + w_2 \frac{\sqrt{y}}{2} = \left(\frac{w_1}{3} + \frac{w_2}{2}\right)\sqrt{y}$$

**At $w_1 = 2$, $w_2 = 3$:**

$$c = \left(\frac{2}{3} + \frac{3}{2}\right)\sqrt{y} = \frac{13}{6}\sqrt{y}$$

$$MC = \frac{13}{12\sqrt{y}}, \quad AC = \frac{13}{6\sqrt{y}}$$

Note $MC = AC/2$ — since the technology gives DRS in $y$ (cost scales as $\sqrt{y}$, so output elasticity < 1), $MC < AC$ everywhere. **No shut-down threshold:** $\min(AC) \to \infty$ as $y \to 0$, but since there are **no fixed costs**, the firm never produces with negative profit.

**Supply:** $p = MC = 13/(12\sqrt{y}) \Rightarrow S(p) = y = \dfrac{169}{144 p^2}$

**Profit at $p = 1$:** $\pi = 1 \cdot \frac{169}{144} - \frac{13}{6}\sqrt{\frac{169}{144}} = \frac{169}{144} - \frac{13}{6} \cdot \frac{13}{12} = \frac{169}{144} - \frac{169}{72} = -\frac{169}{144} < 0$

Since no fixed costs and $\pi < 0$: **firm shuts down** ($p < \min AC$); $S(1) = 0$.

**Effect of $w_1$ increase on supply:**

$$\frac{\partial S(p,w)}{\partial w_1} = \frac{\partial}{\partial w_1}\left[\frac{144 p^2}{\left(\frac{w_1}{3}+\frac{w_2}{2}\right)^2 \cdot 4}\right]$$

As $w_1$ rises, the cost function shifts up → $MC$ curve shifts up → **supply decreases** (less produced at each price). Opposite to intuition at first glance, but correct: higher input price raises marginal cost, shifting supply curve inward.
