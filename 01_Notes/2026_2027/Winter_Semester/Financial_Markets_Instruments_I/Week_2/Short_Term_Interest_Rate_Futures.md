[[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Financial_Markets_Instruments_I_main.md#Week 2|Back to Financial Markets Instruments I — Week 2]]

# Short-term interest rate futures

Why can a long interest-rate futures position gain when an interest rate falls, and how can a future deposit earn an opening rate agreed earlier? The tutorial contract quotes **100 minus an annual interest rate expressed in percent**. Its price therefore moves in the opposite direction from that rate. Its tick value converts a one-basis-point annual rate change into the interest on a three-month EUR 500,000 deposit. These are hypothetical specifications, rather than current exchange terms. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 2]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 7]]

## Quotation, tick value and the deposit period

The **Three-Month Euro Interest Rate Futures Tutorial (IRF3T)** has EUR 500,000 principal. With $i_{\%}$ the annual interest rate in percentage points,

$$F=100-i_{\%}.$$

Thus $F=90.50$ corresponds to a 9.50% annual rate for a three-month deposit. A one-basis-point change is 0.01 percentage point, or 0.0001 as a decimal annual rate. The source fixes the tick value using a quarter-year accrual:

$$v=500{,}000(0.0001)\frac{3}{12}=\text{EUR }12.50.$$

A higher quotation corresponds to a lower implied rate. The long's positive futures gain can then offset the smaller interest earned on a future deposit. The source calls the long the buyer of a certificate of deposit (CD), hence the lender, and the short the CD seller/borrower. For physical delivery, the long places EUR 500,000 in a three-month deposit at an eligible bank arranged by the short. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 7]]

![[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Short_Rate_Specification.png]]

*The complete specification includes the borrower/lender labels and the quarter-year tick derivation. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 7]]*

Initial margin is EUR 500, 0.1% of principal. Delivery months are March, June, September and December. The last trading day is the third Wednesday of the delivery month at 11:00 a.m.; delivery follows on the next business day. The source's specification describes EDSP as the three-month spot rate: the exchange samples 16 banks, removes the three highest and three lowest rates, and averages the remaining ten. The worked settlement example instead writes **EDSP as a futures quotation**, $91.25=100-8.75$, so the underlying spot deposit rate is 8.75%. Keep rate units and quoted-price units distinct despite this source-label difference. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 7]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 8]]

## Closing the futures before the deposit begins

The long buys one contract at $F_0=90.50$ and closes two weeks later at $F_{14}=90.55$. The five-tick rise represents a five-basis-point fall in the implied rate, from 9.50% to 9.45%. Its profit is

$$\Pi=(9055-9050)(12.5)=\text{EUR }62.50.$$

Using the source's opening-margin denominator, the 14-day return is $62.5/500=12.5\%$. Simple annual scaling gives $0.125\times365/14\approx3.26=326\%$. This closed position has no later delivery obligation. The result belongs to the margin trade, not a 12.5% interest return on EUR 500,000. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 8]]

## Cash settlement and the effective deposit rate

If the original position instead remains open to settlement, EDSP is shown as 91.25. Its 75-tick gain is

$$\Pi_T=(9125-9050)(12.5)=\text{EUR }937.50.$$

The accompanying spot deposit rate is 8.75%. A gain in euros can be expressed as an additional annual rate by dividing by principal and deposit-year fraction. For a principal $L$ and deposit duration $\tau$ years,

$$i_{\mathrm{effective}}=i_{\mathrm{spot}}+\frac{\Pi_T}{L\tau}.$$

This is the source's accounting interpretation: combine deposit interest with the settled futures gain. With the tick's own quarter-year convention, $\tau=1/4$, the gain adds $937.5/(500000/4)=0.0075$, or 0.75 percentage point. The effective annual rate is then $8.75\%+0.75\%=9.50\%=100-F_0$. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 7]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 8]]

### The slide's day-count and payment-timing qualification

Slide 8 converts the same EUR 937.50 using $\tau=91/365$, rather than the $3/12$ used for the tick value on slide 7. Its expression gives

$$0.0875+\frac{937.5}{500000}\frac{365}{91}
=0.0950206\approx9.50206\%.$$

The slide reports this as 9.5%, so exact equality to the opening rate depends on keeping a consistent year fraction or accepting rounding. This difference is a source convention mismatch, not an extra market gain. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 7]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 8]]

The source also displays both $500000\,r(91/365)=937.5$, giving $r\approx0.00752$, and a discounted version

$$\frac{500000\,r(91/365)}{1+r(91/365)}=937.5,$$

giving $r\approx0.00753$. The first treats the amount as interest over the period; the second treats it as a discounted amount. Slide 8 does not supply a full funding/timing convention reconciling these alternatives with daily marking to market. They should not be presented as one exact universal deposit-hedge identity. The reliable general result is the direction of the hedge and its unit conversion under an explicitly fixed accrual convention. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 8]]

## Physical delivery and compensation for a lower deposit rate

The source's physical example lets the short arrange a deposit at 8.70%, which is five basis points below the 8.75% EDSP spot rate. It compensates the long for that difference:

$$0.0005(500000)\frac{91}{365}=\text{EUR }62.33.$$

The five-basis-point compensation bridges the arranged rate to the benchmark. The opening-to-delivery futures gain bridges the benchmark to the opening futures rate. Both components are needed for the lecture's intended 9.5% deposit-rate interpretation, subject to the quarter-year versus 91/365 and payment-timing qualifications above. The diagram separates the futures trading period from the subsequent three-month deposit period, preventing those periods from being confused. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 8]]

![[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_Short_Rate_Settlement.png]]

*The source gives three alternative exit paths and uses two accrual/payment conventions in its effective-rate illustration. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 8]]*

## What to carry forward

With this quotation, a long gains when the implied rate falls. Tick value depends on principal, the annual rate increment and the deposit duration. A deposit hedge combines the deposit's actual interest with futures gains and any delivery-rate compensation, using consistent units and day counts. [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/Stock_Index_and_Currency_Futures.md|Stock index and currency futures]] develops the common tick and margin-return calculation. The deposit application adds an interest-accrual period distinct from the futures holding period. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 7]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 8]]
