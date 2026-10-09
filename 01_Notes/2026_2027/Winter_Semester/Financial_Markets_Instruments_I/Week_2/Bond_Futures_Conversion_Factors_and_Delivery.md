[[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Financial_Markets_Instruments_I_main.md#Week 2|Back to Financial Markets Instruments I — Week 2]]

# Bond futures, conversion factors and delivery

How can one futures contract allow delivery of several real bonds when its underlying asset is a notional bond? Long-term bond futures specify a standardized reference instrument, then use a **conversion factor** to adjust the invoice for an eligible deliverable bond. The short chooses the bond and, in this tutorial, its delivery date within the month. Those options connect bond pricing to financing and coupon income. The lecture's hypothetical terms are recorded as supplied examples. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 2]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 9]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 11]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 13]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 14]]

## The notional contract and its monetary scale

The **Long-term Treasury Bond Futures Tutorial** refers to a notional 20-year Treasury bond with USD 100,000 face value and 7% yield to maturity. Its quotation $QP$ is a clean price per USD 100 nominal value, excluding accrued coupon. Since $100000/100=1000$,

$$CV=1000\,QP,$$

where $CV$ is contract value in dollars. A tick is USD 0.01 in the quoted price, so it changes contract value by $1000(0.01)=\text{USD }10$. Initial margin is USD 2,000, 2% of nominal contract value. Delivery months are March, June, September and December. The last trading day is two business days before the last business day of the delivery month. The short can deliver on any business day of the month. The source defines EDSP as the contract's futures price at 11:00 a.m. on the second business day before that last trading date. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 9]]

![[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Bond_Specification.png]]

*The full hypothetical specification distinguishes the quotation per USD 100 from the USD 100,000 contract. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 9]]*

The source says the zero-basis-at-maturity rule is theoretically applicable to the CTD bond because the underlying reference bond is notional. This qualification links convergence to the eligible delivery choice rather than asserting that every bond's raw clean spot quotation equals the unadjusted futures quotation. The lecture does not derive a precise conversion-adjusted basis formula here. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 9]]

### A short closing trade

The short sells ten contracts at $F_0=91.38$ and buys them back 45 days later at $F_{45}=91.23$. The quotation fell by 15 ticks. A short benefits from that fall:

$$\Pi=10(15)(10)=\text{USD }1{,}500.$$

The initial-margin return is $1500/(10\times2000)=7.5\%$. The source's simple annual scaling is $0.075\times365/45=60.83\%$. This closes the obligation before the separate delivery illustration. [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/Stock_Index_and_Currency_Futures.md#Read the contract before calculating|Read the contract before calculating]] explains the common sign and margin-denominator rules. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 10]]

## Clean price, full price and coupon dates

A clean price excludes accrued coupon. A **full price** includes the compensation owed to the seller for coupon accrued since the previous coupon payment:

$$P_{\mathrm{full}}=P_{\mathrm{clean}}+AC.$$

All quantities must use the same face-value basis. A purchase of the source's eligible bond costs a full spot price, while the contract quotes clean. This distinction is necessary when comparing the initial cash outflow with the eventual delivery invoice. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 9]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 10]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 14]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 15]]

The eligible-bond example has USD 100 face value, an annual coupon of 8% paid semi-annually, hence USD 4 per coupon, and 12 years remaining from the previous coupon date. The timeline records a previous coupon on 18 November, purchase today on 1 April, the next coupon on 18 May, and the after-next coupon on 18 November. It displays a June delivery month, initial full spot price $S_0=99.13$, initial clean futures quotation $F_0=88.19$, and financing rate $r=6\%$. These values belong to the delivery example, not the earlier $91.38\to91.23$ closing trade. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 10]]

![[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Bond_Delivery_Timeline.png]]

*The original delivery timeline keeps coupon dates, full spot price and clean futures quotation visible. Its displayed day counts are source assumptions; related inconsistencies are discussed below. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 10]]*

## Conversion factor: price at the contract's reference yield

A bond's conversion factor $CF$ is its **clean price per one unit of face value when valued at the contract's 7% reference yield**. It is dimensionless. The exchange calculates a factor for the first day of each delivery month and keeps that factor constant during the delivery cycle, using its specified rounding conventions. The source's adjusted clean delivery price is

$$P_{\mathrm{delivery,clean}}=CF\times FP,$$

where $FP$ is the contract's futures quotation. Accrued coupon must then be added to obtain the full invoice price. A factor above one increases the clean invoice relative to $FP$; a factor below one reduces it. In the source's valuation example, a coupon above the 7% reference yield gives $CF>1$, and one below it gives $CF<1$. This is a reference-yield adjustment, rather than a claim that different eligible bonds have identical current market prices or implied repo rates. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 11]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 14]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 15]]

### Follow the source's valuation steps

The coupon is USD 4 every half year and the reference half-year yield is $0.07/2=0.035$. On the after-next coupon date, the source values 22 remaining coupon payments and the final principal:

$$P_{AN}=\sum_{t=1}^{22}\frac{4}{(1.035)^t}+\frac{100}{(1.035)^{22}}
\approx107.584.$$

Here $t$ counts half-year periods. Each payment is discounted to that coupon date. To obtain the full price at the beginning of June, the source adds the USD 4 coupon due at the later valuation date, then discounts back a fractional half-year. Its printed formula is

$$P_F=\frac{107.584+4}{(1.035)^{171/182.5}}=108.065\quad\text{(source's displayed equality)}.$$

It subtracts accrued coupon for 14 days to obtain a clean price:

$$P_C=108.065-\frac{14}{182.5}(4)=107.758,$$

and divides by 100 face value to give $CF=1.07758$. The cash-flow reasoning is: discount future full value, remove accrued coupon, normalize by face value. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 11]]

### The conversion-factor example has a day-count error

The printed formula's **171** days disagree with the **170** days on the source timeline and with its numerical result. Evaluating the printed expression gives approximately $108.044$ for $P_F$, $107.737$ for the clean price, and $CF\approx1.077373$. Using **170/182.5** gives $108.065$, $107.758$ and $1.07758$, matching the displayed results. These are agent recomputations from the original source formula and data. The note preserves both the printed formula and its discrepancy, rather than treating the stated factor as a verified consequence of 171 days. Use an explicitly supplied consistent factor for later calculations, or state a consistent day-count choice. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 10]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 11]]

![[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Conversion_Factor_Example.png]]

*Source conversion-factor definition, coupon timeline and printed calculations. The 171-day exponent and 170-day diagram are both visible. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 11]]*

## The short's cost-of-carry transaction

The short borrows in the money market, uses the loan to pay the full bond purchase price, and acquires the bond. During the holding period, the bond produces coupon income while the loan produces a financing cost. At delivery, the short transfers the bond to the long, receives the invoice price, and repays the loan. The source calls

$$\mathrm{carry}=\mathrm{carry\ revenue}-\mathrm{carry\ expenditure}.$$

It uses accrued coupon as carry revenue and interest on the financed full purchase price as carry expenditure. This sign convention matters: positive carry means that continuing to hold the financed bond earns more than it costs. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 12]]

![[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Cost_of_Carry_Flows.png]]

*The six labeled flows show borrowing, bond acquisition, delivery, payment and loan repayment. The diagram links cash financing to the physical delivery obligation. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 12]]*

## Delivery timing under the source's carry rule

The source's rule chooses the last business day of the delivery month when daily carry is positive, and the first business day when it is negative. Its example computes, per USD 100 face value,

$$\mathrm{daily\ revenue}=\frac{0.08(100)}{365}=0.02192,$$

$$\mathrm{daily\ financing\ cost}=\frac{99.13(0.06)}{365}=0.01630,$$

so daily carry is approximately USD 0.00562. Continuing to hold adds positive carry, giving the source's choice of the last business day. With negative carry, waiting instead erodes the transaction's return. This is the lecture's simplified constant daily-carry rule. Its stronger sentence that in reality only the first or last business day is chosen is retained as a source assertion, not expanded into a universal market rule beyond the illustration. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 13]]

## What to carry forward

The contract quotation, full bond purchase price and full invoice price have different roles. Conversion factors adjust the clean delivery amount for a chosen bond, while accrued coupon completes the invoice. Carry links the bond's income to the financing cost and determines the source's delivery-date choice. [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/Implied_Repo_Rate_and_Cheapest_to_Deliver.md|Implied repo rate and cheapest to deliver]] develops the next question: which eligible bond gives the greatest return from purchase to delivery? [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 11]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 12]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 13]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 14]]
