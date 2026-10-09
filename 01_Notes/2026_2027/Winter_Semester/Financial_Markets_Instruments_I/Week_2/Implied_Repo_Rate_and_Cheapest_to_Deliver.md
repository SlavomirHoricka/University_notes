[[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Financial_Markets_Instruments_I_main.md#Week 2|Back to Financial Markets Instruments I — Week 2]]

# Implied repo rate and cheapest to deliver

Which bond should a short select when several bonds are eligible for delivery into the same futures contract? The lecture identifies the **cheapest-to-deliver (CTD)** bond as the eligible bond with the highest **implied repo rate (IRR)**. IRR measures the annualized return implied by buying a bond at its full spot price and realizing the delivery invoice and any intervening coupon. Here IRR means implied repo rate throughout; it does not refer to a generic project internal rate of return. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 14]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 15]]

[[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/Bond_Futures_Conversion_Factors_and_Delivery.md|Bond futures, conversion factors and delivery]] explains the conversion-factor and accrued-coupon inputs. Selecting the lowest unadjusted clean market price would ignore the different delivery proceeds and coupon cash flows. The CTD comparison must consider the complete transaction on a consistent day-count and quotation basis. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 14]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 15]]

## Why the return resembles a repo loan

The source compares an actual repo, in which cash is advanced against a bond and returned with interest, with a purchase-to-futures-delivery transaction. Buying the bond creates an initial cash outflow. Delivering the bond into the futures contract creates a later cash inflow. These flows can be described as an **implied loan**: the purchase amount is the advance and the delivery proceeds are its repayment. The bond may also pay a coupon before delivery, which the source assumes can be reinvested at the same implied rate until delivery. The short's actual money-market borrowing is a separate financing leg. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 14]]

The initial outflow includes the clean market price and accrued coupon paid to the bond seller. The terminal inflow includes the conversion-adjusted clean futures price and accrued coupon paid by the receiver at delivery. If a coupon arrives before delivery, its reinvested amount also contributes to the terminal value. Thus IRR compares a complete stream of purchase and delivery cash flows, rather than comparing the futures quotation directly with the clean market price. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 14]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 15]]

## Notation, units and assumptions

Use all prices on the same face-value basis, such as dollars per USD 100 face value. Define:

| Symbol | Meaning |
|---|---|
| $PP$ | Full purchasing price today |
| $MP$ | Clean market purchasing price today |
| $IP$ | Full invoice price at delivery |
| $FP$ | Contract's clean futures quotation |
| $CF$ | Deliverable bond's dimensionless conversion factor |
| $C$ | One periodic coupon payment |
| $n_{T,DL}$ | Days from today ($T$) to delivery ($DL$) |
| $n_{NC,DL}$ | Days from the next coupon ($NC$) to delivery |
| $AC_{PC,T}$ | Coupon accrued from previous coupon ($PC$) to today |
| $AC_{NC,DL}$ | Coupon accrued from next coupon to delivery |
| $AC_{PC,DL}$ | Coupon accrued from previous coupon to delivery |
| $AC_{T,DL}$ | Coupon accrued from today to delivery when no coupon intervenes |

The source formulas use simple annual rate accrual with day fractions $n/365$. In the one-coupon case, they assume that coupon is reinvested at IRR. There are no fees or taxes in the displayed cash-flow equations. IRR is an implied transaction yield. Compare it with actual financing separately when discussing whether the financed transaction is profitable. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 14]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 15]]

## One coupon before delivery

The purchase is $PP=MP+AC_{PC,T}$. After the intervening coupon, accrued coupon restarts, so the delivery invoice is

$$IP=FP\,CF+AC_{NC,DL}.$$

The purchase amount accumulated to delivery must equal the invoice plus the coupon accumulated from its own payment date:

$$PP\left(1+IRR\frac{n_{T,DL}}{365}\right)
=IP+C\left(1+IRR\frac{n_{NC,DL}}{365}\right).$$

The right-hand coupon interest covers fewer days because the coupon arrives after the bond purchase. Expanding and collecting the $IRR$ terms gives

$$\frac{IRR}{365}\left(PP\,n_{T,DL}-C\,n_{NC,DL}\right)=IP+C-PP,$$

and therefore

$$\boxed{IRR=\frac{(IP+C-PP)365}{PP\,n_{T,DL}-C\,n_{NC,DL}}}.$$

The numerator is the undiscounted surplus, scaled to an annual rate. The denominator accounts for the amount and duration of invested cash, reduced by the coupon that arrives before delivery and can be reinvested. Both numerator and denominator use money times days, so the ratio is a dimensionless annual rate. The algebra requires a nonzero denominator. These intermediate steps are agent explanation of the source's displayed cash-flow identity, not extra empirical evidence. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 15]]

### Recompute the source's numerical example

The slide gives $PP=99.13$, $FP=88.19$, $CF=1.07758$, coupon $C=4$, $n_{T,DL}=89$ and $n_{NC,DL}=43$. The source's printed accrued coupon is $4(43/180)$. Substituting its numbers literally gives

$$IRR=\frac{\left(88.19(1.07758)+4\frac{43}{180}+4-99.13\right)365}
{99.13(89)-4(43)}
\approx0.0361742=3.61742\%.$$

**The slide reports 3.57%, which does not follow from those printed inputs.** Using $43/182.5$ instead gives about 3.56219%, close to its reported figure but still not identical. The preceding conversion-factor example also mixes a 170-day timeline with a 171-day exponent. These are source arithmetic/day-count inconsistencies. The generic cash-flow equation and its algebra are usable; the stated numerical example must not be taught as an exact verified answer. An exercise should give a consistent coupon day count and either a verified or explicitly assumed conversion factor. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 11]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 15]]

The diagram labels intervals of 46, 14 and 29 days, whereas the numerical formula uses 89 days from today to delivery and 43 days from the next coupon to delivery. Its printed calendar dates and displayed intervals should therefore be treated as the source's example conventions, rather than silently recalculated into a new calendar interpretation. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 10]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 15]]

![[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_2_L11_IRR_Formulas.png]]

*The source includes both IRR cases, the complete notation and the numerical expression. Its 3.57% label and mixed day-count inputs remain visible for checking. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 15]]*

## No coupon before delivery

Without an intervening coupon, the accumulated purchase amount equals the invoice:

$$PP\left(1+IRR\frac{n_{T,DL}}{365}\right)=IP,$$

where the invoice uses coupon accrued since the last payment,

$$IP=FP\,CF+AC_{PC,DL}.$$

Subtracting $PP$ and dividing by the initial amount and time fraction gives

$$\boxed{IRR=\frac{(IP-PP)365}{PP\,n_{T,DL}}}.$$

The distinction from the one-coupon formula follows from the cash flows: there is no coupon to reinvest, so no $C$ term enters the numerator or denominator. In the source's no-coupon setting, the short pays $AC_{PC,T}$ at purchase but receives $AC_{PC,DL}$ at delivery. The net accrued coupon is $AC_{T,DL}$, provided the same coupon-accrual convention applies across the whole interval. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 15]]

## Compare eligible bonds and choose CTD

For each eligible bond, determine the full purchase price, its conversion factor, the delivery invoice, coupon cash flows and applicable dates. Calculate IRR using the case that matches those cash flows. The source defines CTD as the eligible bond with **maximum IRR**, and says exchanges calculate and publish IRRs. This does not mean the highest-coupon bond or the lowest quoted-price bond must be CTD. The invoice adjustment and acquisition cost matter jointly. The uploaded lecture supplies one worked bond, rather than a table of several candidates, so no actual CTD security is identified here. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 14]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 15]]

The source's carrying illustration finances at 6%. Using its literal numerical IRR inputs gives an implied yield around 3.62%, below that financing rate. This comparison is an agent inference from the supplied figures: a positive IRR alone does not establish a positive financed profit. CTD remains a comparison among the eligible delivery alternatives. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 10]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 14]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 15]]

## What to carry forward

Start with the full purchase outflow and finish with the full invoice plus any intervening coupon. The reinvestment assumption determines the one-coupon denominator. The CTD criterion is the greatest implied transaction yield among eligible bonds under comparable conventions. Reliable practice can use the source's formulas and explicit assumptions; exact reproduction of its inconsistent example requires clarification. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 14]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_2/L11(ExamplesOfFinancialFutures).pptx|L11(ExamplesOfFinancialFutures).pptx, slide 15]]
