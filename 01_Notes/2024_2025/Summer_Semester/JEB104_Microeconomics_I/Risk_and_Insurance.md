---
course: JEB104
topic: Risk, Insurance, and Asset Markets
source: 00_Materials/2024_2025/Summer_Semester/JEB104_Microeconomics_I/JEB104_17_Uncertainty_II_Students.pdf
tags: [JEB104, microeconomics, risk, insurance, portfolio, Arrow-Debreu, state-contingent, adverse-selection, moral-hazard]
created: 2026-04-19
---

Parent: [[JEB104_Microeconomics_I_main]]
Source: [[00_Materials/2024_2025/Summer_Semester/JEB104_Microeconomics_I/JEB104_17_Uncertainty_II_Students.pdf]]
Related: [[Uncertainty_and_Expected_Utility]], [[Endowment_Economy_and_Buying_Selling]], [[Utility_Function]], [[Duality]]

# Risk and Insurance

## State-Contingent Commodity Framework

Decision-making under uncertainty can be cast as ordinary consumer theory using **state-contingent commodities** (Arrow 1953; Debreu 1959):

- There are $S$ possible states of the world: $s = 1, 2, \ldots, S$.
- Each occurring with probability $\pi_s$ ($\sum_s \pi_s = 1$).
- A **state-contingent commodity** $x_s$ is a claim to consumption in state $s$.

The consumer chooses a state-contingent consumption bundle $(x_1, \ldots, x_S)$ to maximise expected utility:

$$\max_{(x_s)} \sum_{s=1}^S \pi_s u(x_s)$$

subject to a budget constraint on **Arrow-Debreu securities** (assets paying 1 unit in state $s$ and 0 elsewhere, priced at $q_s$):

$$\sum_{s=1}^S q_s x_s \leq W$$

This is **formally identical** to the consumer's standard problem, with states playing the role of goods.

## Insurance Markets

### Basic Setup

A risk-averse consumer faces:
- Wealth without loss: $W$ (probability $1 - \pi$).
- Wealth with loss: $W - L$ (probability $\pi$, where $L$ is the loss).

**Without insurance:** Expected utility = $(1-\pi) u(W) + \pi u(W-L)$.

**Full insurance at premium $\alpha$:** Pay premium $\alpha$ in both states; receive $L$ in the loss state. Consumption:
- No loss: $W - \alpha$
- Loss: $W - L + L - \alpha = W - \alpha$ (same in both states — full coverage eliminates risk).

**Actuarially fair insurance:** Premium equals expected loss: $\alpha = \pi L$. Full insurance at a fair premium is always optimal for a **risk-averse** consumer.

**Proof:** At the fair premium, consumption is $W - \pi L$ for certain. Compare to the lottery: by risk aversion, $u(W - \pi L) > (1-\pi)u(W) + \pi u(W-L)$. $\blacksquare$

### Optimal Insurance with Loading

If the insurance premium is **loaded** (actuarially unfair): $\alpha > \pi L$ (insurer earns profit). The consumer solves:

$$\max_\alpha (1-\pi) u(W - \alpha) + \pi u(W - L + (L-\alpha) \cdot 0 + L - \alpha)$$

Wait — with **coverage $K$** (partial insurance), premium $= \gamma K$ where $\gamma > \pi$ (unfair):

$$\max_K (1-\pi) u(W - \gamma K) + \pi u(W - L + K - \gamma K)$$

**FOC:** $(1-\pi)(-\gamma) u'(W - \gamma K) + \pi(1-\gamma) u'(W - L + K(1-\gamma)) = 0$

Rearranging:

$$\frac{u'(c_{\text{loss}})}{u'(c_{\text{no-loss}})} = \frac{(1-\pi)\gamma}{\pi(1-\gamma)}$$

Since $\gamma > \pi$ (loading), the ratio on the right exceeds 1, so $u'(c_{\text{loss}}) > u'(c_{\text{no-loss}})$, implying $c_{\text{loss}} < c_{\text{no-loss}}$ — the consumer **partially insures** (does not fully equalise consumption across states).

## Portfolio Choice

A consumer with wealth $W$ allocates $\alpha$ to a risky asset (return $\tilde{r}$) and $W - \alpha$ to a safe asset (return $r_f$):

**Final wealth:** $\widetilde{W} = W(1+r_f) + \alpha(\tilde{r} - r_f)$

**Maximise:** $\mathbb{E}[u(\widetilde{W})]$

**FOC:**

$$\mathbb{E}[(\tilde{r} - r_f) u'(\widetilde{W})] = 0$$

**Result:** A risk-averse investor holds a positive risky asset position ($\alpha > 0$) iff $\mathbb{E}[\tilde{r}] > r_f$ — positive equity premium required.

**Comparative statics:** Under DARA, wealthier individuals invest a larger **absolute** amount in risky assets. Under constant RRA, the **share** of wealth in risky assets is constant (CRRA portfolios).

## Asymmetric Information and Market Failure

### Adverse Selection (Hidden Information)

When insurance buyers have **private information** about their risk type:

- **High-risk types** find insurance more valuable → self-select into insurance market.
- Insurer cannot distinguish types → must price at average risk.
- At the average price, low-risk types find insurance too expensive → exit the market (**adverse selection**).
- Remaining pool is higher-risk → price rises → more low-risk types exit (**unravelling**).

**Akerlof (1970) "market for lemons":** Adverse selection can cause market collapse. Equilibrium may involve **separating contracts** (high-coverage/high-premium for high-risk; low-coverage/low-premium for low-risk) or **pooling contracts** (single price, quantity constrained so high-risk don't over-consume).

### Moral Hazard (Hidden Action)

Once insured, the consumer may reduce **precautionary effort** (hidden effort $e$ lowers loss probability $\pi(e)$ with $\pi'(e) < 0$, $\pi''(e) > 0$):

**First-best (observable effort):** Insurer sets $e^*$ that maximises joint surplus.

**Second-best (hidden effort):** Full insurance eliminates incentives to exert effort ($e = 0$ is optimal for insured consumer since marginal cost of effort is borne by consumer but benefit accrues to insurer). Optimal **second-best contract** provides **partial coverage** — retains consumer "skin in the game":

$$\frac{d}{de}\left[(1-\pi(e))u(W - \alpha) + \pi(e)u(W - L + K)\right] = 0$$

$$-\pi'(e)\left[u(W - \alpha) - u(W - L + K)\right] = c'(e)$$

Partial coverage ($K < L$) ensures $u(W-\alpha) > u(W - L + K)$, giving positive effort incentives.

## State-Prices and Risk-Neutral Pricing

In a complete financial market, **Arrow-Debreu prices** $q_s$ can be decomposed:

$$q_s = \frac{\pi_s \cdot m_s}{\mathbb{E}[m]}$$

where $m_s = u'(c_s)/u'(c_0)$ is the **stochastic discount factor (pricing kernel)**. In equilibrium, the price of any asset with payoff $d_s$ is:

$$P = \mathbb{E}[m \cdot d] = \sum_s \pi_s m_s d_s$$

**Risk-neutral probability:** $\tilde\pi_s = q_s / \sum_s q_s = \pi_s m_s / \mathbb{E}[m]$ — state prices renormalised to sum to 1. Under risk-neutral probabilities, all assets earn the risk-free rate:

$$P = \frac{\mathbb{E}^Q[d]}{1+r_f}$$

## Related Concepts

- [[Uncertainty_and_Expected_Utility]] — the VNM framework and risk aversion measures are prerequisites for insurance analysis
- [[Endowment_Economy_and_Buying_Selling]] — state-contingent goods are an endowment economy across states of nature
- [[Utility_Function]] — the curvature of $u$ determines risk aversion and optimal insurance/portfolio
- [[Duality]] — the primal/dual structure of state-contingent markets mirrors the UMP/EMP duality
