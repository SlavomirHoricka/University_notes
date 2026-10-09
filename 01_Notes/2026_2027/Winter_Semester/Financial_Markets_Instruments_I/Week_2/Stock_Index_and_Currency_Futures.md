[[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Financial_Markets_Instruments_I_main.md#Week 2|Back to Financial Markets Instruments I — Week 2]]

# Stock index and currency futures

How does a futures quotation become a money gain or loss, and what happens if a position survives until delivery? These examples apply the Week 1 position and marking-to-market rules to two different underlying assets. The index contract converts index points into euros and settles in cash. The currency contract exchanges euros for dollars and can deliver currency physically. The lecture expressly uses **hypothetical tutorial contracts**, whose terms need not match any currently traded contract. Exchanges may introduce, delete or amend contracts, so all specifications below belong to the uploaded examples. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 2]]

## Read the contract before calculating

A quotation alone has no monetary meaning until the unit of trading and minimum price increment are known. Let $N$ be the number of contracts, $\delta$ the tick size in quotation units and $v$ the money value of one tick. The change from opening quotation $F_0$ to closing quotation $F_t$ is $(F_t-F_0)/\delta$ ticks. Thus, before fees and financing effects,

$$
\Pi_{\mathrm{long}}=N\frac{F_t-F_0}{\delta}v,
\qquad
\Pi_{\mathrm{short}}=-\Pi_{\mathrm{long}}.
$$

This is a unit conversion: quotation change divided by quotation units per tick, multiplied by currency per tick. The long benefits when the quotation rises. The short benefits when it falls. The lecture's index and currency calculations use the same rule, even though their quoted units and settlement currencies differ. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 4]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 6]]

[[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/Margins_and_Marking_to_Market.md|Margins and marking to market]] explains why daily transfers telescope to the opening-to-closing difference. Initial margin is a deposit supporting the position, rather than the value of the underlying asset. The tutorial return convention is

$$
R_{\mathrm{period}}=\frac{\Pi}{N M_0},\qquad
R_{\mathrm{annual,simple}}=R_{\mathrm{period}}\frac{365}{d},
$$

where $M_0$ is initial margin per contract and $d$ is the holding period in days. This convention explains the large quoted returns: the denominator is margin, not the contract's full exposure. The annual figure linearly rescales the particular trade; it does not establish a repeatable annual investment outcome. In calculations using this convention, subsequent margin calls, withdrawals, fees and financing are outside the displayed denominator. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 4]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 6]]

## SIFT 500: index points become euros

The tutorial **Stock Index Futures Tutorial 500 (SIFT 500)** uses an index composed of share prices of the 500 largest companies by market capitalization. Its multiplier is EUR 10 per index point. A quote of 5,433 therefore represents EUR 54,330 of contract value. One tick is half an index point, worth $0.5\times10=\text{EUR }5$; two ticks are one point. Initial margin is EUR 1,000, about 1.8% of EUR 54,330 in the source's example. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 3]]

![[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Index_Specification.png]]

*Tutorial specifications and footnotes, including the multiplier and final settlement averaging rule. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 3]]*

Delivery months are March, June, September and December. The last trading day is the last business day of that month, at 10:30 a.m.; delivery is the next business day. The **exchange delivery settlement price (EDSP)** averages underlying-index observations every 15 seconds from 10:10 through 10:30 a.m., discarding the 12 highest and 12 lowest values. This procedure aims to smooth excessive fluctuations shortly before maturity. It defines a final settlement benchmark rather than simply using the final observed index value. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 3]]

### Closing after five days

The long buys 20 contracts at $F_0=5825.0$ and sells 20 matching contracts five days later at $F_5=5812.5$. The quotation falls by 12.5 index points, equal to $-12.5/0.5=-25$ ticks. Therefore,

$$
\Pi=20(-25)(5)=-\text{EUR }2{,}500.
$$

The return on opening margin is $-2500/(20\times1000)=-12.5\%$. Simple annual scaling gives $-0.125\times365/5=-9.125$, approximately the source's displayed $-912\%$. A scaled return below $-100\%$ reflects the short holding period and the chosen margin denominator; the observed five-day loss itself remains EUR 2,500. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 4]]

### Holding until cash settlement

Delivering every constituent share in the index's weights would create extremely high transaction costs, so the tutorial index contract settles in cash. If the position remains open, the final marking-to-market transfer compares EDSP with the previous day's closing futures quotation. The source gives EDSP $5810.0$ and an additional loss of $20(-5)(5)=-\text{EUR }500$. Its arithmetic treats $5812.5$ as that preceding settlement quotation. This is an alternative to the five-day closing trade, not an additional payment owed after that trade has already closed the position. With the same opening quotation, the total hold-to-settlement loss is $20(5810-5825)10=-\text{EUR }3{,}000$ (derived from the source's quotations). [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 4]]

![[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Index_Closing_and_Settlement.png]]

*The source timeline displays the closing quotation and final EDSP. Use the closing-out path and the maturity path as alternatives. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 4]]*

## ECFT: identify the traded and invoice currencies

The **Euro Currency Futures Tutorial (ECFT)** trades EUR 25,000 per contract against the US dollar. The euro is the underlying/traded/base currency. The dollar is the invoice/variable currency. A quotation of $1.2311\ \mathrm{USD/EUR}$ means that one euro costs 1.2311 dollars. The long receives euros and pays dollars at delivery; the short delivers euros and receives the dollar amount. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 5]]

One tick is USD 0.0001 per euro, which the source describes as one hundredth of a US cent per euro. Its monetary value is

$$
25{,}000\ \mathrm{EUR}\times0.0001\ \mathrm{USD/EUR}=\text{USD }2.50.
$$

The EUR units cancel. Initial margin is USD 1,000, about 3.5% of the contract value when the exchange rate is 1.1345 USD/EUR. Delivery months are the same four quarterly months. The last trading day is the third Wednesday of the delivery month at 10:30 a.m.; delivery is the next business day. EDSP averages the rates of 15 reference banks at 10:30 a.m., excluding the three highest and three lowest. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 5]]

![[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Currency_Specification.png]]

*The currency specification keeps quotation units, tick size and margin currency distinct. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 5]]*

### Closing after ten days

The long buys ten contracts at $F_0=1.2311$ and closes at $F_{10}=1.2383$. The rise is $0.0072/0.0001=72$ ticks, giving

$$
\Pi=10(72)(2.5)=\text{USD }1{,}800.
$$

The margin return is $1800/(10\times1000)=18\%$. Simple annual scaling yields $0.18\times365/10=6.57=657\%$. The gain is in dollars even though the underlying contract size is in euros. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 6]]

### Physical delivery fixes the effective purchase rate

If the ten contracts remain open until delivery, the long receives EUR 250,000. At EDSP $1.2401$, the invoice is $250000\times1.2401=\text{USD }310{,}025$. The opening-to-delivery gain is $10(2401-2311)(2.5)=\text{USD }2{,}250$. Combining the invoice and the futures gain gives

$$
\frac{310{,}025-2{,}250}{250{,}000}=1.2311\ \mathrm{USD/EUR}=F_0.
$$

The long pays the EDSP invoice but has already received offsetting futures gains. This is why the effective purchase price reproduces the opening futures rate in the source's matched delivery example. The ten-day USD 1,800 gain and the delivery USD 2,250 gain describe different exit times and must not be added together. The calculation leaves funding timing and transaction costs outside the illustration. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 6]]

![[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Currency_Closing_and_Delivery.png]]

*The source currency timeline and invoice calculation show the alternative closing and delivery paths. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 6]]*

## What to carry forward

Read the quotation units first, turn its change into ticks, and then convert ticks into money using the correct long/short sign. Cash settlement ends the index contract with a final transfer. Currency delivery exchanges principal at EDSP, with the futures gain or loss fixing the effective matched purchase rate. [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/Basis_Convergence_and_Futures_Hedging.md|Basis, convergence and futures hedging]] supplies the earlier general hedge identity; these are applications with specified settlement benchmarks and multipliers. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 3]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 4]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 5]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 6]]
