---
course: "JEB108"
topic: "Seminar Applications — Industry Supply & Equilibrium"
source: "00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Seminars/Seminar_5-6_Solutions-1.pdf"
tags: [JEB108, microeconomics, seminars, industry-supply, equilibrium, tax-incidence]
created: 2026-04-19
---
Parent: [[JEB108_Microeconomics_II_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB108_Microeconomics_II/Seminars/Seminar_5-6_Solutions-1.pdf]]
Related: [[Industry_Equilibrium]], [[Firm_Supply_Curve]], [[Consumer_Surplus_and_Welfare_Measures]]

# Seminar Applications — Industry Supply & Equilibrium (Seminars 5–6)

Applied exercises on aggregating firm supply into market supply, computing equilibria, and analyzing the incidence and deadweight loss of taxation.

---

## Market Supply Aggregation

**Kink in aggregate supply curve:** If $S_1(p) = p - 10$ and $S_2(p) = p - 5$:

- Firm 1 enters at $p = 10$; Firm 2 enters at $p = 5$.
- For $p < 5$: neither firm supplies; $Q^S = 0$.
- For $5 \leq p < 10$: only Firm 2 supplies; $Q^S = p - 5$.
- For $p \geq 10$: both supply; $Q^S = (p-10) + (p-5) = 2p - 15$.

**→ Kink at $p = 10$.**

---

## Long-Run Equilibrium: Conditions and Computation

**Q: True or False — In long-run industry equilibrium no firm loses money.**

**A: True.** With free entry/exit and no fixed costs in the long run: any firm with $\pi < 0$ exits, reducing supply until $p$ rises to $\min(ATC)$. Long-run equilibrium requires $\pi^* = 0$.

**Exception:** NYC cab operators may show accounting profits even in the "long run" because cab licences are a **fixed factor in inelastic supply** — the apparent profit is an **economic rent** on the scarce licence, not true economic profit. This does not violate the competitive model. See [[Industry_Equilibrium]].

---

## Worked Problem — Full Industry Equilibrium

**Setup:** All firms identical with $LTC(y) = y^3 - 3y^2 + 5y$.

$$LAC(y) = y^2 - 3y + 5, \quad LMC(y) = 3y^2 - 6y + 5$$

**Minimum LAC:** $dLAC/dy = 2y - 3 = 0 \Rightarrow y^* = 3/2$

$$\min LAC = (3/2)^2 - 3(3/2) + 5 = 9/4 - 9/2 + 5 = 11/4$$

→ **Long-run equilibrium price:** $p^* = 11/4$, each firm produces $y^* = 3/2$, with $\pi^* = 0$.

**Industry output with $D(p) = 101 - 4p$:**

$$Q^* = 101 - 4(11/4) = 101 - 11 = 90$$

$$n^* = Q^*/y^* = 90/(3/2) = \mathbf{60 \text{ firms}}$$

**Demand shift + input price doubles** ($D^1(p) = 152 - 4p$):

Doubling input prices doubles all costs: $LAC^1(y) = 2y^2 - 6y + 10$ → $\min LAC^1 = 11/2$ at $y_1^* = 3/2$.

$p_1^* = 11/2$, $Q_1^* = 152 - 4(11/2) = 152 - 22 = 130$, $n_1^* = 130/(3/2) = \mathbf{86\tfrac{2}{3} \approx 87}$ firms.

---

## Tax Incidence and Deadweight Loss

**Setup:** $Q^D = 300 - 2p^2$, $Q^S = 20 + 4p^2$.

**Equilibrium without tax:**

$$300 - 2p^2 = 20 + 4p^2 \Rightarrow 6p^2 = 280 \Rightarrow p^* = \sqrt{280/6} \approx 6.83, \quad Q^* \approx 206.7$$

**Per-unit tax $t = 5$ on producers:** Producers receive $p_S = p - 5$; equilibrium shifts.

$$Q^D = Q^S: \quad 300 - 2p^2 = 20 + 4(p-5)^2$$

Expanding: $300 - 2p^2 = 20 + 4p^2 - 40p + 100$

$\Rightarrow 6p^2 - 40p - 180 = 0 \Rightarrow p_{SR}^* = \frac{40 + \sqrt{1600 + 4320}}{12} \approx 9.75$

**Consumer price rises from 6.83 to 9.75** (consumers bear most of the burden — demand relatively inelastic compared to supply). **Long-run price:** $p_{LR}^* \approx 11.83$ (as firms exit, supply contracts further).

**Tax revenue (short run):** Government collects $t \cdot Q^* = 5 \times Q_{SR}^*$. Consumers pay $(p_{SR} - p_0) \times Q_{SR}^* \approx (9.75 - 6.83) \times Q_{SR}$ to the government indirectly; producers remit the full $t$ per unit. Result: firms pay \$550 total tax but collect only \$320 extra from consumers → producers absorb \$230.

**Deadweight loss:**

$$DWL = \frac{1}{2} \cdot t \cdot \Delta Q = \frac{1}{2} \cdot 5 \cdot (Q^* - Q_{SR}^*)$$

(area of the welfare triangle lost to the tax wedge).

---

## Key Insight: Tax Statutory vs. Economic Incidence

The identity of the party legally obligated to pay a tax (statutory incidence) is irrelevant to economic incidence. The market equilibrium is identical whether the tax is collected from buyers or sellers — only the **elasticities** of supply and demand determine the burden split:

$$\text{Consumer burden} = \frac{\varepsilon_S}{\varepsilon_S + |\varepsilon_D|}, \quad \text{Producer burden} = \frac{|\varepsilon_D|}{\varepsilon_S + |\varepsilon_D|}$$

**Policy application (cigarette tax):**
- Short run: demand is perfectly inelastic → consumers bear 100% of the tax (price rises by full amount of $t$).
- Long run: demand becomes elastic → burden shifts to producers as consumers substitute away (price to consumers rises less; producer price falls).
