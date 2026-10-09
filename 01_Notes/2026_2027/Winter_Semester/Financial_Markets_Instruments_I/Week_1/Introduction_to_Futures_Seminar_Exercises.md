[[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Financial_Markets_Instruments_I_main.md#Week 1|Back to Financial Markets Instruments I — Week 1]]

# Introduction to futures — seminar exercises

These exercises turn the Week 1 definitions into cash calculations. The supplied PDF calls itself “Seminar 2” and is dated 29 September 2026, but it is present in the authorized Week_1 folder and covers futures basics. All 22 pages were inspected. The worked solutions below are **agent-derived explanations**, obtained from the source questions and the lecture/handout definitions; the seminar provides questions and an empty table rather than an answer key. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=1|02_seminar.pdf, PDF p. 1]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=17|02_seminar.pdf, PDF p. 17–22]]

Read [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/Margins_and_Marking_to_Market.md|Margins and marking to market]] first for the distinction between daily profit, deposits and account balances. [[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/Spot_Forward_and_Futures_Contracts.md|Spot, forward and futures contracts]] explains the matching contract needed to close a position. For calculations below, a margin call occurs **below** maintenance, and a withdrawal is allowed only from funds above the chosen required retained balance; alternative broker rules would change that withdrawal condition. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 5–7]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=13|02_seminar.pdf, PDF p. 13]]

## Problem 1: offsetting contracts

John buys ten June Nasdaq 100 futures contracts on 9 January and wants to close them on 16 April. He sells ten equivalent **June Nasdaq 100** contracts on 16 April. Matching the underlying, delivery month and number cancels his existing long position; daily settlement fixes his cumulative gain/loss as ten times the multiplier times closing minus opening futures price. Jane opens a short September S&P 500 contract in early August and closes it a week later by buying one equivalent **September S&P 500** contract. A contract of another maturity would create a different position rather than be the matching offset. The question supplies no opening or closing prices, so it cannot determine a numerical profit. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=17|02_seminar.pdf, PDF p. 17]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 6–7]]

## Problem 2: a short wheat contract

The company shorts 5,000 bushels at 250 cents per bushel, with $3,000 initial and $2,000 maintenance margin. Convert the quoted price to dollars: $F_0=2.50$ dollars per bushel. A price increase harms the short. Before other deposits or withdrawals its balance at a new settlement price F is

$$A=3000+5000(2.50-F).$$

A call occurs when $A<2000$, so

$$5000(F-2.50)>1000\quad\Longrightarrow\quad F>2.70.$$

Thus an increase of **more than 20 cents per bushel**, beyond 270 cents, breaches maintenance. Exactly 270 cents leaves $2,000, at the threshold under the stated strict-below rule. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=18|02_seminar.pdf, PDF p. 18]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 5–6]]

For a $1,500 withdrawal while retaining the initial $3,000, the account must first reach $4,500. The short needs a gain of $1,500, which requires a fall of $1500/5000=0.30$ dollars per bushel. F must be **220 cents or lower**. If only maintenance must remain after withdrawal, $A\ge3500$ suffices, so F must be **240 cents or lower**. The question does not specify which withdrawal rule applies; both conditional results are retained. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=18|02_seminar.pdf, PDF p. 18]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 5]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=13|02_seminar.pdf, PDF p. 13]]

## Problem 3: copper and maximum loss

One long November contract covers 25,000 pounds at $0.78 per pound. Its normalized cumulative result at a closing/settlement price F is

$$\Pi^{\mathrm{long}}=25000(F-0.78).$$

**If one additionally assumes F cannot be negative**, the largest loss is $25000\times0.78=\$19,500$, reached at F=0. The question itself does not state a lower price bound, so $19,500$ is a conditional result rather than a bound implied by futures margin. If the model admits arbitrarily negative F, the long formula has no finite loss bound. For the short, $\Pi^{\mathrm{short}}=25000(0.78-F)$: with no upper price bound, an arbitrarily high F gives an arbitrarily large loss. The initial margin is never a maximum-loss guarantee. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=19|02_seminar.pdf, PDF p. 19]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/FI01(Futures Contracts).doc|FI01(Futures Contracts).doc, Ch. I, LibreOffice-rendered p. 8]]

## Problem 4: a daily margin table

There are 20 long contracts quoted directly in dollars per contract, with prices 82, 84, 78, 81 and 79. Total initial margin is $20\times5=100$ and total maintenance is $20\times2=40$. The original blank table is retained because its settlement-price column is visual content absent from native text extraction. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=20|02_seminar.pdf, PDF p. 20]]

![[01_Notes/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/assets/Week_1_Seminar_Problem_4_Table.png]]

*Source table: day 0 is the opening at 82; days 1–4 settle at 84, 78, 81 and 79. The table requests opening balance, deposits, price change, gain/loss and ending balance.* [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=20|02_seminar.pdf, PDF p. 20]]

The completed explanation assumes no voluntary withdrawals and tops up **to initial margin immediately after a below-maintenance settlement**. The “deposit” column below follows that order, rather than assuming funds arrive before that day's price movement:

| Day | Beginning balance ($) | Settlement ($/contract) | Price change ($/contract) | Daily gain/loss ($) | Deposit after settlement ($) | Ending balance ($) |
|---|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 82 | — | — | 100 initial | 100 |
| 1 | 100 | 84 | +2 | +40 | 0 | 140 |
| 2 | 140 | 78 | −6 | −120 | 80 | 100 |
| 3 | 100 | 81 | +3 | +60 | 0 | 160 |
| 4 | 160 | 79 | −2 | −40 | 0 | 120 |

Day 2 has an unadjusted balance of $140-120=20$, below maintenance 40. Restoring initial 100 requires 80. The ending balance 120 is not a profit of 20: deposits were 180, so the trading loss is 60, matching $20(79-82)=-60$. If the call instead restores maintenance, the day-2 deposit is 20 and later balances are 40, 100 and 60, still leaving the same −60 trading result relative to total deposits of 120. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=20|02_seminar.pdf, PDF p. 20]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 5–6]]

## Problem 5: clearing a larger long position

The member begins with 85 long contracts settled at $42,500 and initial margin $2,000 per contract. It adds 15 long contracts at $43,750. All contracts end the new day at $43,000. Existing contracts gain

$$85(43000-42500)=\$42,500,$$

while new contracts lose

$$15(43000-43750)=-\$11,250.$$

Net daily settlement is **+$31,250**. The 15 new positions require $15\times2000=\$30,000$ additional initial margin. If the initial account holds exactly $85\times2000=\$170,000$, the new requirement for 100 contracts is $200,000$, while after settlement the account has $201,250. On an end-of-day net basis, **no additional net cash is needed**; $1,250 exceeds the new initial requirement. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=21|02_seminar.pdf, PDF p. 21]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=11|02_seminar.pdf, PDF p. 11–13]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 6]]

The required incremental initial margin is still $30,000. If it must be posted when the new positions are entered, before the day's $31,250 credit is available, it requires $30,000 of temporary funding. The PDF asks for total including initial margin but does not specify intraday sequencing, beginning excess balance or withdrawal rules. The answer therefore distinguishes the new margin obligation from net end-of-day funding rather than assuming their timing is identical. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=21|02_seminar.pdf, PDF p. 21]]

## Problem 6: two orange-juice contracts

Two long contracts each cover 15,000 pounds, so total exposure is 30,000 pounds. Opening price is 160 cents ($1.60) per pound. Total initial margin is $12,000 and total maintenance is $9,000. A price fall creates a loss of $300$ for each one-cent fall because $30000\times0.01=300$. Before top-ups,

$$A=12000+30000(F-1.60),$$

with F in dollars per pound. Maintenance is breached when

$$30000(1.60-F)>3000\quad\Longrightarrow\quad F<1.50.$$

The call therefore follows a fall of **more than 10 cents per pound**, below 150 cents. Exactly 150 cents leaves the account at maintenance under the strict-below convention. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=22|02_seminar.pdf, PDF p. 22]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 5–6]]

To withdraw $2,000 while retaining total initial margin, the account must gain $2,000. This requires a price rise of

$$\frac{2000}{30000}=0.066\overline6\ \text{dollars per pound}
=6.\overline6\ \text{cents per pound}.$$

Thus F must be at least $1.666\overline6$ ($166.\overline6$ cents), subject to the contract's allowed ticks, which the question does not specify. If retaining only maintenance is allowed, the original $12,000 already exceeds $9,000 by $3,000, so a $2,000 withdrawal is possible immediately. More generally the condition is $A\ge11000$, or $F\ge1.566\overline6$. The two results reflect different retained-balance rules rather than different futures gains. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=22|02_seminar.pdf, PDF p. 22]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/L10(EssentialsOfFuturesTrading).pptx|L10(EssentialsOfFuturesTrading).pptx, slide 5]] [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=13|02_seminar.pdf, PDF p. 13]]

## The seminar's film illustration

Page 15 supplies a short-trade illustration: 450,000 pounds sold at $1.42 and bought back at $0.29, a difference of $1.13 per pound. Its multiplication is $450000\times1.13=\$508,500$, corresponding to 30 contracts of 15,000 pounds each. This is the supplied illustration's trading gain before costs, not an explanation of its margin-account path. The PDF also contains external video links and the phrase “Eddie Murphy Rule”; the selected slide does not define the rule, and the videos were not opened. No legal claim is inferred from that label. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=15|02_seminar.pdf, PDF p. 15]]

## What to carry forward

Identify the direction of the position, convert the quote into consistent units, multiply the price change by total contract exposure, and separate gain/loss from funding. Margin-call thresholds and withdrawals also require an explicit account rule. These steps explain why a short can face a call after a price rise, a long after a fall, and a profitable aggregate daily settlement can fund new initial margin. [[00_Materials/2026_2027/Winter_Semester/Financial_Markets_Instruments_I/Week_1/02_seminar.pdf#page=18|02_seminar.pdf, PDF p. 18–22]]
