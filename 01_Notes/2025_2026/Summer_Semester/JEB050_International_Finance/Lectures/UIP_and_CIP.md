---
course: JEB050
topic: Uncovered and Covered Interest Parity
source: 00_Materials/2025_2026/Summer_Semester/JEB050_International_Finance/Week_4/week4_Slides.pdf
tags: [JEB050, UIP, CIP, interest-parity, forward-premium-puzzle, exchange-rate-determination]
created: 2026-04-24
---

Parent: [[JEB050_International_Finance_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB050_International_Finance/Week_4/week4_Slides.pdf]]
Related: [[Exchange_Rate_Types_and_Triangular_Arbitrage]], [[DD_AA_Model]], [[International_Fisher_Effect_and_REER]]

# Uncovered and Covered Interest Parity

## Uncovered Interest Parity (UIP)

**UIP** is the equilibrium condition in the foreign exchange market when investors are risk-neutral and capital is freely mobile. It states that the expected return on domestic-currency deposits must equal the expected return on foreign-currency deposits (expressed in domestic currency).

### Derivation

Consider an investor choosing between:
- **Domestic deposit:** Invest 1 CZK at rate $R_{CZK}$; receive $1 + R_{CZK}$ after one period.
- **Foreign deposit (EUR):** Convert 1 CZK to EUR at spot rate $E_{CZK/\euro}$; deposit at $R_\euro$; convert back at expected future rate $E^e_{CZK/\euro}$.

Return from EUR deposit (in CZK):

$$\frac{1}{E_{CZK/\euro}} \cdot (1 + R_\euro) \cdot E^e_{CZK/\euro} = (1 + R_\euro) \cdot \frac{E^e_{CZK/\euro}}{E_{CZK/\euro}}$$

**Indifference condition (exact form):**

$$(1 + R_{CZK}) = (1 + R_\euro) \cdot \frac{E^e_{CZK/\euro}}{E_{CZK/\euro}}$$

**Approximation** (for small rates):

$$\boxed{R_{CZK} \approx R_\euro + \frac{E^e_{CZK/\euro} - E_{CZK/\euro}}{E_{CZK/\euro}}}$$

The second term, $\frac{E^e - E}{E}$, is the **expected rate of depreciation** of CZK.

### Interpretation

| Condition | Implication |
|---|---|
| $R_{CZK} > R_\euro + \frac{E^e - E}{E}$ | Domestic deposits more attractive → capital inflow → CZK appreciates (E falls) until UIP holds |
| $R_{CZK} < R_\euro + \frac{E^e - E}{E}$ | Foreign deposits more attractive → capital outflow → CZK depreciates (E rises) until UIP holds |

In equilibrium, the interest rate differential equals the expected depreciation. A country with higher interest rates has a currency expected to **depreciate**.

### UIP Equilibrium Diagram

In the standard diagram (return on y-axis, exchange rate E on x-axis):
- Domestic return: horizontal line at $R_{domestic}$
- Foreign return in domestic currency: downward-sloping curve (higher E today → cheaper to buy foreign currency → expected return lower if $E^e$ is fixed)
- Equilibrium: intersection of the two

## Covered Interest Parity (CIP)

**CIP** is an **arbitrage** condition (not merely an equilibrium condition). It eliminates exchange rate risk by using a **forward contract** to lock in the conversion rate.

### Derivation

Covered return on EUR deposit (lock forward rate $F$):

$$\frac{1}{E_{CZK/\euro}} \cdot (1 + R_\euro) \cdot F_{CZK/\euro}$$

No-arbitrage requires this to equal $(1 + R_{CZK})$:

$$(1 + R_{CZK}) = (1 + R_\euro) \cdot \frac{F_{CZK/\euro}}{E_{CZK/\euro}}$$

**Exact CIP:**

$$\boxed{F_{CZK/\euro} = E_{CZK/\euro} \cdot \frac{1 + R_{CZK}}{1 + R_\euro}}$$

**Approximation:**

$$\frac{F - E}{E} \approx R_{CZK} - R_\euro$$

The forward premium $(F - E)/E$ equals the interest rate differential.

### CIP vs. UIP Comparison

| | UIP | CIP |
|---|---|---|
| **Condition type** | Equilibrium (no arbitrage given risk tolerance) | Pure arbitrage (mechanically enforced) |
| **Exchange rate used** | **Expected future spot** $E^e$ | **Forward rate** $F$ (contractually fixed today) |
| **Risk** | Exposed to exchange rate risk | Risk-free (hedged) |
| **Empirical status** | Frequently violated (forward premium puzzle) | Held tightly pre-2008; small deviations post-GFC |

## The Forward Premium Puzzle

If CIP holds (linking $F$ to interest differentials), then UIP implies:

$$E[S_{t+1}] = F_t$$

i.e., the forward rate should be an unbiased predictor of the future spot rate.

**Fama (1984)** regression test:

$$S_{t+1} - S_t = \alpha + \beta \cdot (F_t - S_t) + \varepsilon_{t+1}$$

UIP + CIP → $\beta = 1$. Empirically, $\beta$ is typically **negative** across major currency pairs — the forward rate systematically predicts the **wrong direction**. Currencies with high interest rates (high forward premium) tend to **appreciate**, not depreciate.

**Zigraiova, Havranek & Novak (2020)** — meta-analysis correcting for publication bias:
- Corrected $\hat{\beta} \approx 0.31$ for **developed** countries (partial departure from UIP)
- Corrected $\hat{\beta} \approx 0.98$ for **emerging market** currencies (close to UIP)

**Explanations for the puzzle:**
1. **Risk premium:** Investors require compensation for holding high-yield currencies — the peso problem.
2. **Irrational expectations:** Investors systematically misforecast exchange rates.
3. **Learning/peso problem:** Occasional large realignments distort small-sample regressions.
4. **Transaction costs and limits to arbitrage** in the CIP context (post-2008 deviation).
