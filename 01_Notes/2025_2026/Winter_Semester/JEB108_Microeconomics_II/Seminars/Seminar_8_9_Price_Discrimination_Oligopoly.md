---
course: "JEB108"
topic: "Seminar Applications — Price Discrimination & Oligopoly"
source: "00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Seminars/Seminar_8_9_Solutions-1.pdf"
tags: [JEB108, microeconomics, seminars, price-discrimination, oligopoly, cournot, bertrand, stackelberg]
created: 2026-04-19
---
Parent: [[JEB108_Microeconomics_II_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Seminars/Seminar_8_9_Solutions-1.pdf]]
Related: [[Price_Discrimination]], [[Oligopoly_Models]], [[Monopoly]], [[Industry_Equilibrium]]

# Seminar Applications — Price Discrimination & Oligopoly (Seminars 8–9)

Worked exercises consolidating price discrimination theory and all three canonical oligopoly models (Stackelberg, Cournot, Bertrand).

---

## Price Discrimination Applications

### Third-Degree Price Discrimination — Market Segmentation

**Setup:** Monopolist serves two markets:
- Market 1: $D_1(p_1) = 100 - p_1$ → $MR_1 = 100 - 2y_1$
- Market 2: $D_2(p_2) = 60 - p_2$ → $MR_2 = 60 - 2y_2$
- $MC = 20$ (constant)

**Optimal quantities** ($MR_i = MC$):

$$100 - 2y_1 = 20 \Rightarrow y_1 = 40, \quad p_1 = 60$$

$$60 - 2y_2 = 20 \Rightarrow y_2 = 20, \quad p_2 = 40$$

**Check:** Market 1 (less elastic at $p_1 = 60$): $|\varepsilon_1| = 100/60 \cdot 1 = 60/60 = 1.5$. Market 2 (more elastic at $p_2 = 40$): $|\varepsilon_2| = 60/40 = 1.5$. In this symmetric case, prices still differ because demand intercepts differ — higher willingness to pay in market 1 → higher price.

**No-discrimination uniform price** ($MR_{total} = MC$): Total demand $D = 160 - 2p$ → $MR = 80 - y$ → $y^* = 60$, $p = 50$. Welfare comparison: discrimination increases total output and reduces DWL.

### Two-Part Tariff Design

**Setup:** Single market, $D(p) = 100 - p$, $MC = 20$. Firm can charge fixed fee $A$ + per-unit price $p_u$.

**Optimal design (homogeneous consumers):**
1. Set $p_u = MC = 20$ → eliminates all DWL.
2. At $p_u = 20$: $y = 80$, $CS = \frac{1}{2}(100-20)(80) = 3{,}200$.
3. Set $A = CS = 3{,}200$ → extracts all surplus.

Total profit: $\pi = A + (p_u - MC) \cdot y = 3{,}200 + 0 = 3{,}200$.

Versus uniform monopoly profit: $(p^M - MC) \cdot y^M = (60-20)(40) = 1{,}600$.

**→ Two-part tariff doubles profit while achieving efficiency.**

---

## Oligopoly: Worked Exercises

### Stackelberg Exercise

**Setup:** $D(p) = 12 - p$ → inverse demand $p = 12 - y_1 - y_2$.

Costs: Leader $c_1(y_1) = 2y_1 + 12$, Follower $c_2(y_2) = 4y_2 + 1$.

**Step 1 — Follower's reaction function:**

$$\pi_2 = (12 - y_1 - y_2)y_2 - 4y_2 - 1$$

$$\frac{\partial \pi_2}{\partial y_2} = 12 - y_1 - 2y_2 - 4 = 0 \Rightarrow y_2^*(y_1) = \frac{8 - y_1}{2} = 4 - \frac{y_1}{2}$$

**Step 2 — Leader's optimum:** Substitute $y_2^*(y_1)$ into leader's profit:

$$\pi_1 = \left(12 - y_1 - \left(4 - \frac{y_1}{2}\right)\right)y_1 - 2y_1 - 12 = \left(8 - \frac{y_1}{2}\right)y_1 - 2y_1 - 12$$

$$\frac{\partial \pi_1}{\partial y_1} = 8 - y_1 - 2 = 0 \Rightarrow y_1^* = 6$$

**Step 3 — Outcomes:**

$$y_2^* = 4 - 3 = 1, \quad Y^* = 7, \quad p^* = 12 - 7 = 5$$

$$\pi_1^* = (5)(6) - 2(6) - 12 = 30 - 12 - 12 = 6, \quad \pi_2^* = (5)(1) - 4(1) - 1 = 0$$

### Cournot Exercise (same setup)

**Both firms maximize simultaneously:**

$$\frac{\partial \pi_1}{\partial y_1} = 12 - 2y_1 - y_2 - 2 = 0 \Rightarrow y_1 = \frac{10 - y_2}{2}$$

$$\frac{\partial \pi_2}{\partial y_2} = 12 - y_1 - 2y_2 - 4 = 0 \Rightarrow y_2 = \frac{8 - y_1}{2}$$

**Solving simultaneously:**

$$y_1 = \frac{10 - \frac{8-y_1}{2}}{2} = \frac{10 - 4 + y_1/2}{2} = 3 + y_1/4 \Rightarrow \frac{3y_1}{4} = 3 \Rightarrow y_1^C = 4$$

$$y_2^C = \frac{8-4}{2} = 2, \quad Y^C = 6, \quad p^C = 6$$

$$\pi_1^C = 6(4) - 2(4) - 12 = 24 - 8 - 12 = 4, \quad \pi_2^C = 6(2) - 4(2) - 1 = 3$$

**Comparison (same market, heterogeneous costs):**

| Model | $y_1$ | $y_2$ | $Y$ | $p$ | $\pi_1$ | $\pi_2$ |
|---|---|---|---|---|---|---|
| Stackelberg | 6 | 1 | 7 | 5 | 6 | 0 |
| Cournot | 4 | 2 | 6 | 6 | 4 | 3 |

**Observation:** Stackelberg gives higher total output and lower price than Cournot. The leader gains by committing first; the follower is worse off (squeezed out with efficiency advantage of leader's commitment).

---

## Bertrand Paradox — Discussion

With **homogeneous goods** and **constant MC**: even two firms competing in prices drives $p = MC$ and $\Pi = 0$ — identical to perfect competition.

**Resolutions of the Bertrand Paradox:**

| Extension | Outcome |
|---|---|
| Capacity constraints | Cournot-like outcome |
| Differentiated products | Prices above MC in equilibrium |
| Repeated interaction | Collusion may be sustained |
| Asymmetric costs | Lower-cost firm wins all at $p = MC_{high}$ |
| Increasing MC | Cournot-like (multiple firms share market) |

**Practical relevance:** Bertrand competition is most realistic in **commodity markets** (standardized products, no switching costs, price publicly observable). Quantity-setting (Cournot) is more realistic when firms commit to capacity in advance.
