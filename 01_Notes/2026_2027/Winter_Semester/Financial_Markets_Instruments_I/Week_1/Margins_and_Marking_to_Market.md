[[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Financial_Markets_Instruments_I_main.md#Week 1|Back to Financial Markets Instruments I — Week 1]]

# Margins and marking to market

How can a contract create large gains or losses even though the trader initially deposits only a small amount? Futures margin supports performance of the obligation, while daily settlement realizes price changes in the account. Understanding the difference between a deposit, a trading result and an account balance is necessary before solving margin-call exercises. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 5–6]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=11|02_seminar.pdf, PDF p. 11–13]]

## The three margin concepts

**Initial margin**, I, is the required deposit when opening a position. Both the long and short must post it. The lecture says it is the trader's money in the margin account, not the price paid for the underlying asset. Because it is only a fraction of the underlying contract value, it creates leverage: a given movement in the full contract's price can be large relative to this initial deposit. The seminar gives 5–15% as a usual illustrative range rather than a universal required rate. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 5]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 4]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=11|02_seminar.pdf, PDF p. 11]]

**Maintenance margin**, M, is the minimum allowed account balance. Daily losses may reduce the balance below M. A **margin call** is then a notice to restore the balance to the specified target. The lecture allows a target of maintenance or initial margin; the handout describes restoring maintenance; the seminar's formula uses initial margin. The target must therefore be stated when doing calculations. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 5]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 4]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=13|02_seminar.pdf, PDF p. 13]]

The lecture and handout call the extra deposited funds **variation margin**. The seminar also uses that phrase for the daily transfer of settlement gains/losses and writes “Variation Margin = Initial Margin − Margin balance.” That expression describes a top-up to initial margin when the balance is deficient; it is not a formula saying every daily settlement payment equals I minus the balance. These meanings share the aim of limiting unpaid losses, but use different cash-account conventions. Below, “daily gain/loss” means the price-based transfer and “top-up” means the additional deposit after a call. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 5–6]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 4]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=12|02_seminar.pdf, PDF p. 12–13]]

The seminar describes maintenance both as a minimum balance and as a payment made after adverse movement. The minimum is the threshold; the required payment is the amount needed to restore the chosen target. Keeping these quantities separate prevents confusing a $2,000 threshold with a $2,000 deposit in every case. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=13|02_seminar.pdf, PDF p. 13]]

## Daily profit and loss, with units

Let $F_0$ be the opening futures price, $F_t$ the settlement price at the end of day t, N the number of contracts and q the multiplier converting one quoted price unit into money per contract. With a constant position size and multiplier,

$$G_t^{\mathrm{long}}=Nq(F_t-F_{t-1}),\qquad
G_t^{\mathrm{short}}=Nq(F_{t-1}-F_t)=-G_t^{\mathrm{long}}.$$

A price rise credits the long and debits the short; a fall reverses these transfers. The lecture writes the price difference for a normalized unit; Nq restores the contract units used by the seminar's tick examples. For a commodity quoted in dollars per pound, q is pounds per contract. For a contract quoted directly in dollars per contract, q=1. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 6]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 4–5]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=5|02_seminar.pdf, PDF p. 5, 12]]

Adding the daily transfers cancels every intermediate price:

$$\sum_{t=1}^{k}G_t^{\mathrm{long}}
=Nq\big[(F_1-F_0)+(F_2-F_1)+\cdots +(F_k-F_{k-1})\big]
=Nq(F_k-F_0).$$

The short obtains the opposite amount. This **telescoping sum** explains why the total trading result equals the closing minus opening price, even though it is paid in installments. The account can require cash along the way even when the final cumulative result is favorable. The source's reasoning ignores interest earned or paid on the timing of settlement cash flows. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 6]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 7]]

## From daily result to an account balance

Let $A_{t-1}$ be the previous ending account balance. Before any top-up or withdrawal, the new balance is

$$A_t^- = A_{t-1}+G_t.$$

If a call restores a target R, the deposit is $C_t=R-A_t^-$ when $A_t^-<M$; otherwise there is no call. With a withdrawal $W_t$, the ending balance becomes

$$A_t=A_t^-+C_t-W_t.$$

These equations are an explicit accounting synthesis of the source descriptions. A deposit increases the balance but does not create trading profit; a withdrawal decreases the balance but does not create trading loss. If a trader fails to meet a call, the exchange/clearing house can close the position through a reverse trade at that trader's cost. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 5–6]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 4]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=12|02_seminar.pdf, PDF p. 12–13]]

### The handout's five-day example

![[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_FI01_Margin_Table.png]]

*The complete source table has an opening price of 1,000 and both initial and maintenance margin equal to 200. Closing prices are 1,100, 1,200, 1,050, 950 and 900. The source uses a one-unit price-to-money normalization.* [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 9]]

The long receives 100 on each of the first two days, then loses 150, 100 and 50. Its cumulative gain/loss is therefore 100, 200, 50, −50 and −100. On day 4 the balance falls from 250 to 150 and a deposit of 50 restores it to 200. On day 5 the balance again needs 50. The long ends with 200 in the account after depositing 100 beyond its initial 200, but its trading result is −100. The account balance is not its profit. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 9]]

The short loses 100 on each of the first two days and posts 100 each time to restore 200. It then gains 150, 100 and 50, ending with 500. Total deposits were 400, so the account's net surplus over deposits is 100, equal to its trading gain. This compares the two positions' opposite cash transfers and illustrates why small initial deposits can require substantial later funding. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 9]]

## Payoff and the size of possible losses

For a position held to maturity with $F_T=S_T$, cumulative trading results are

$$\Pi_T^{\mathrm{long}}=Nq(S_T-F_0),\qquad
\Pi_T^{\mathrm{short}}=Nq(F_0-S_T).$$

They have equal magnitude and opposite signs. A long benefits from a higher final underlying price; a short benefits from a lower one. The source diagram crosses zero at $S_T=F_0$ and shows linear results on either side. Margin does not truncate either line. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 7–8]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 11]]

![[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_FI01_Long_Short_Payoffs.png]]

*The horizontal axis is the maturity spot price $S_T$. The long line slopes upward and the short line downward; their common break-even point is the opening futures price $F_0$. The vertical direction represents gain/loss, not the margin account balance.* [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 8]]

A claimed maximum long loss needs a lower bound on the price. If the modeled final price cannot go below zero, the maximum loss is $NqF_0$ at zero. If the problem imposes no lower bound, that particular finite maximum does not follow from the payoff formula. With no upper price bound, a short's theoretical loss has no finite maximum. These are algebraic consequences of the source payoff, and the required assumptions are made explicit in [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/Introduction_to_Futures_Seminar_Exercises.md|the copper exercise]]. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 8]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=19|02_seminar.pdf, PDF p. 19]]

## What to carry forward

The same price movement determines a trading result and alters the account, but deposits and withdrawals make those quantities different. Compute the signed daily result first, apply it to the balance, compare with maintenance, and only then calculate a top-up to the specified target. [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/Introduction_to_Futures_Seminar_Exercises.md|The Week 1 seminar exercises]] apply this sequence with actual contract multipliers and multiple positions. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=17|02_seminar.pdf, PDF p. 17–22]]
