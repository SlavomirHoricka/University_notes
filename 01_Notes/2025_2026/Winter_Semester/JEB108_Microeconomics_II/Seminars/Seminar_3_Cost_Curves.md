---
course: "JEB108"
topic: "Seminar Applications — Cost Curves"
source: "00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Seminars/Seminar_3_Solutions.pdf"
tags: [JEB108, microeconomics, seminars, cost-curves, short-run, long-run]
created: 2026-04-19
---
Parent: [[JEB108_Microeconomics_II_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Seminars/Seminar_3_Solutions.pdf]]
Related: [[Cost_Curves]], [[Cost_Minimization]], [[Firm_Supply_Curve]]

# Seminar Applications — Cost Curves (Seminar 3)

These exercises apply the theoretical cost curve framework from [[Cost_Curves]] to concrete functional forms.

---

## Core Identities

For any cost function $TC(y)$:

$$MC(y) = \frac{dTC}{dy}, \quad AC(y) = \frac{TC(y)}{y}, \quad AVC(y) = \frac{VC(y)}{y}, \quad AFC(y) = \frac{FC}{y}$$

**Key geometric result:** $MC = AC$ at the **minimum of $AC$**, because:

$$\frac{d(AC)}{dy} = \frac{MC \cdot y - TC}{y^2} = \frac{MC - AC}{y} = 0 \iff MC = AC$$

---

## Worked Problems

### Problem 1 — $TC(y) = (y-2)^2 + 1$

$$MC = 2(y-2) = 2y - 4$$

$$AC = \frac{(y-2)^2 + 1}{y} = y - 4 + \frac{5}{y}$$

**Intersection $MC = AC$:**

$$2y - 4 = y - 4 + \frac{5}{y} \Rightarrow y = \frac{5}{y} \Rightarrow y^2 = 5 \Rightarrow y = \sqrt{5}$$

**Intersection $TC = MC \cdot y$** (where $TC = VC$ since $AC(y) = AVC(y)$ if no separate FC):

$(y-2)^2 + 1 = y(2y-4) \Rightarrow y^2 - 4y + 5 = 2y^2 - 4y \Rightarrow y^2 = 5 \Rightarrow y = \sqrt{5}$

**Profit at $y = 5$ given market price = ?** (needs $p$; at $y^* = \sqrt{5}$, $AC = 2\sqrt{5} - 4$)

### Problem 2 — $LTC = 3y^3 - 8y^2 - 11y$

$$LMC = 9y^2 - 16y - 11$$

$$LAC = 3y^2 - 8y - 11$$

**Supply curve** (long-run, no fixed costs → shut-down at $\min LAC$):

$$S^{-1}(y^*) = LMC = 9y^2 - 16y - 11 \quad \text{for } y \geq \frac{4}{3}$$

**Minimum price $p_0$:** Set $LMC = LAC$:

$$9y^2 - 16y - 11 = 3y^2 - 8y - 11 \Rightarrow 6y^2 - 8y = 0 \Rightarrow y = 4/3$$

At $y = 4/3$: $LAC = 3(16/9) - 8(4/3) - 11 = 16/3 - 32/3 - 33/3 = -49/3 < 0$

Since $p_0 = \min(LAC) < 0$: effectively $p_0 = 0$ (firm always produces if $p \geq 0$).

**Long-run supply function:**

$$9y^2 - 16y - (11+p) = 0 \Rightarrow y = \frac{16 + \sqrt{256 + 36(11+p)}}{18} = \frac{8 + \sqrt{163 + 9p}}{9}$$

### Problem 3 — $STC = y^3 - 80y^2 + 2{,}500y + 40{,}000$

$$SRMC = 3y^2 - 160y + 2{,}500$$

$$SRAVC = y^2 - 80y + 2{,}500$$

**Minimum AVC:** $d(AVC)/dy = 2y - 80 = 0 \Rightarrow y_0 = 40$

$$\min(AVC) = 1{,}600 - 3{,}200 + 2{,}500 = 900$$

So $p_0 = 900$ — firm shuts down for $p < 900$.

**At $p = 500 < 900$:** $y = 0$ (firm shuts down).

**Supply function** (for $p \geq 900$):

$$3y^2 - 160y + (2{,}500 - p) = 0 \Rightarrow S(p) = \frac{80 + \sqrt{6{,}400 - 3(2{,}500 - p)}}{6} = \frac{80 + \sqrt{3p - 1{,}100}}{3}$$

---

## Short-Run vs. Long-Run: Conceptual Review

| Concept | Short Run | Long Run |
|---|---|---|
| Fixed inputs | Yes ($\bar{x}_2$) | No (all inputs variable) |
| Fixed costs | Present | Absent (or only quasi-fixed) |
| Shut-down condition | $p < \min(AVC)$ | $p < \min(ATC)$ |
| Supply elasticity | Lower | Higher |

**Key theorem (Envelope):** $LTC(y) \leq STC(y, \bar{x}_2)$ for all $y$; equality at the output level where $\bar{x}_2 = x_2^{LR*}(y)$. See [[Cost_Curves]] for derivation.
