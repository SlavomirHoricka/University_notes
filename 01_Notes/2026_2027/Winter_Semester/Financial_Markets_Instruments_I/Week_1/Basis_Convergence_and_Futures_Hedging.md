[[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Financial_Markets_Instruments_I_main.md#Week 1|Back to Financial Markets Instruments I — Week 1]]

# Basis, convergence and futures hedging

Why can a futures position fix the price of a later purchase or sale, and why does closing it early leave uncertainty? The answer joins two prices observed at the same time: the spot price and the futures price. Their difference is the basis. Daily settlement offsets the changing spot price completely only when the remaining basis is zero. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 8–10]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 6–7]]

## Basis and calendar spread are different comparisons

For a delivery month X, let $S_t$ be the spot price at time t and $F_t^X$ the futures price at that time for delivery in X. This course uses

$$B_t^X=S_t-F_t^X.$$

The basis compares spot with one futures maturity. **Contango** means $F_t^X>S_t$, so the basis is negative; **backwardation** means $F_t^X<S_t$, so it is positive. Some markets use the opposite definition, $F-S$; always state the convention before assigning signs. The seminar sometimes spells this quantity “Base,” but the lecture and handout use “basis.” [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 8]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 6]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=10|02_seminar.pdf, PDF p. 10]]

A **calendar spread** compares two futures prices. If X is the earlier delivery month and Y the later one, the lecture defines

$$D_t^{X,Y}=F_t^X-F_t^Y.$$

It also notes the opposite sign convention. The lecture's **normal contango** ordering is $F_t^Y>F_t^X>S_t$, while its **normal backwardation** ordering is $F_t^Y<F_t^X<S_t$. These are the meanings of those labels in the supplied lecture; do not substitute a different definition of “normal” without stating it. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 8]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 7]]

The seminar lists market expectations, cost of carrying a position (including opportunity cost), and payments expected before delivery as reasons spot and futures prices can differ. Week 1 introduces these factors; the cost-of-carry pricing model in the later handout chapter is outside this ingestion scope. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=10|02_seminar.pdf, PDF p. 10]]

## Why the prices converge at delivery

The source's no-arbitrage argument compares executable spot purchase/sale with delivery under the matching futures contract. If $F>S$ at delivery, buy the asset spot for S and deliver it through a short futures position for F. If $S>F$, buy through a long futures position for F and sell the asset spot for S. Either case produces a positive difference before trading, delivery or borrowing costs. The handout's examples use F=100, S=80 or F=80, S=100, producing a difference of 20 per unit. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 9]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 6]]

The theoretical conclusion is $F_T=S_T$, hence $B_T=0$. It presumes the compared asset is eligible for the contract and the required purchases, sales and deliveries can occur on the relevant terms; otherwise the cash-flow comparison is not established. In the second case, the handout also describes selling a borrowed security spot, taking futures delivery and returning it. **Short selling of the asset** involves borrowing and later returning that asset; it differs operationally from merely opening a short futures position. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 6–7]]

The **Exchange Delivery Settlement Price**, or EDSP, is the price used in final settlement. The handout calls it the closing price on the last trading day, determined by the clearing house through an exact procedure. The lecture gives an average of selected spot quotations as its introductory description and says its determination implements zero basis. These descriptions establish that final settlement follows a defined reference procedure; they do not supply a universal formula covering every contract type. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 6]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 7, 9]]

![[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_L10_Convergence_Patterns.png]]

*The green line is spot and the red lines are futures for the earlier month X and later month Y. Each futures line meets spot at its own delivery date $D^X$ or $D^Y$. The curves need not be straight or monotonic: convergence concerns the endpoint, not a prediction that either price moves smoothly toward it.* [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 9]]

## A purchase hedge, derived step by step

Suppose a buyer needs Nq units of the same underlying asset at maturity T and opens N matching long futures contracts at $F_0$. Ignore transaction costs and interest on interim margin flows, as in the source's cash-flow arithmetic. By maturity the cumulative futures gain is $Nq(F_T-F_0)$. Buying the asset spot costs $NqS_T$. Net positive expenditure is therefore

$$E_T=NqS_T-Nq(F_T-F_0)
=Nq\big[F_0+(S_T-F_T)\big]
=Nq(F_0+B_T).$$

If convergence gives $B_T=0$, net expenditure equals $NqF_0$. A rise in the spot purchase price is offset by a futures gain; a fall reduces the spot cost but creates a futures loss. The hedge fixes the effective opening price under these matching assumptions. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 10]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 7]]

The lecture instead writes signed cash flow with outflows negative:

$$(F_T-F_0)-S_T=-F_0-B_T=-F_0.$$

This is the same accounting with the opposite sign for expenditure. Defining the sign first avoids interpreting the negative amount as a negative purchase price. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 10]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 7]]

The handout's five-day example ends at a spot and futures price of 900, after opening at 1,000. The long has lost 100 on futures, so buying spot for 900 costs 1,000 after that loss. This illustrates the hedge even though the futures leg itself is unprofitable. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 9]]

## A sale hedge and early termination

A seller expecting to have the matching asset opens a short. Its futures gain is $Nq(F_0-F_t)$, while its spot sale produces $NqS_t$. The net receipt at time t is

$$R_t=NqS_t+Nq(F_0-F_t)=Nq(F_0+B_t).$$

The long buyer's positive expenditure at the same time is also $Nq(F_0+B_t)$, while its signed cash flow is $-Nq(F_0+B_t)$. At maturity the source's zero-basis condition fixes both purchase expenditure and sale revenue at the opening futures price. Before maturity, $B_t$ is unknown when the hedge is opened. This is **basis risk**: the uncertainty about the future spot–futures difference remains after the broad price movement has been hedged. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 10]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 7]]

The handout says hedging is “possible only” on delivery dates, but its following formula explicitly describes an early hedge with remaining basis. Its operational distinction is between the exact opening-price lock at zero basis and the imperfect early hedge exposed to basis risk. The early net-cost formula exists; it does not guarantee a predetermined cost. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 7]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 10]]

The handout's final early-hedge line writes $-F_0+(F_t-S_t)$ but labels it “futures price − basis”. With its own definition $B_t=S_t-F_t$, the displayed expression is $-F_0-B_t$: the long buyer's signed cash flow. Its positive expenditure is $F_0+B_t$. The verbal label therefore has an apparent sign inconsistency; the distinction between signed cash flow and positive expenditure above preserves the algebra. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 6–7, final early-hedge line on p. 7]]

## The lecture's value convention

The lecture labels $S_T-F_0$ for a normalized long and $F_0-S_T$ for a short as value at expiration. Those expressions equal the cumulative payoff described in the handout. Before expiration it presents a deferred-payment illustration:

$$V_t^{\mathrm{long}}=\frac{F_t-F_0}{1+r(T-t)},\qquad
V_t^{\mathrm{short}}=\frac{F_0-F_t}{1+r(T-t)}.$$

Here r is the simple interest rate and $T-t$ the remaining time in matching units. The denominator discounts a cash difference **assumed paid at T** back to t. At inception $F_t=F_0$, so the source's value is zero. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 11]]

Keep this illustration distinct from the lecture's actual daily marking-to-market mechanism. Slide 6 realizes changes day by day; slide 11 describes a price difference as income at maturity. The selected sources do not reconcile the timing conventions or provide a valuation of interest on all daily settlement flows. The discounted expression should therefore be learned as slide 11's stated deferred-payment representation, without treating it as the margin-account balance or as a proved universal value of a daily-settled contract. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 6, 11]]

## What to carry forward

A futures trading gain is only one leg of a hedge. Combining it with the matching spot transaction gives the opening price plus the remaining basis. At zero basis the hedge fixes the price; at an earlier date it leaves basis risk. The result depends on matching quantity, asset and maturity and on the source's cash-flow assumptions. [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/Margins_and_Marking_to_Market.md|Margins and marking to market]] explains why funding obligations may still arise before the hedge reaches its final result. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 5–6, 10]]
