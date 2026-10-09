# Trust and cooperation games

Why do people invest in others or cooperate when keeping money for themselves seems individually attractive? The trust game and the prisoner's dilemma make the conflict between private monetary incentives and a larger joint payoff precise. They also show how beliefs about others and social preferences can change behavior. This note develops the lecture's game rules, its self-regarding benchmarks, and the conditions under which its proposed explanations support cooperation. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=24|Social Preferences, physical PDF pp. 24–37]]

Back to [[01_Notes/2026_2027/Winter_Semester/Behavioral_Economics/Behavioral_Economics_main.md#Week 1|Behavioral Economics — Week 1]]. The [[01_Notes/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/Models_of_Social_Preferences.md|models of social preferences]] explain the motivations used here. The [[01_Notes/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/Ultimatum_and_Dictator_Games.md|ultimatum and dictator games]] provide complementary evidence about giving and rejection; unlike the dictator game, the trust game lets the recipient respond to the initial transfer.

## The trust game: creating a surplus before deciding its division

The **trustor**, also called the investor, starts with a monetary endowment $X$. The trustor first chooses a transfer $Y$, with $0\leq Y\leq X$. The transfer is multiplied by a factor $\alpha>1$ before reaching the **trustee**, also called the agent. The trustee then chooses a back-transfer $Z$, with $0\leq Z\leq\alpha Y$. Thus the trustee can return none, some, or all of the multiplied receipt. The interaction occurs once. Here $\alpha$ denotes the lecture's multiplication factor; it is dimensionless, while $X,Y,Z$ use the same monetary units. The final monetary payoffs are

$$
x_{\mathrm{trustor}}=X-Y+Z,
\qquad
x_{\mathrm{trustee}}=\alpha Y-Z.
$$

The trustor keeps the uninvested amount $X-Y$ and receives $Z$; the trustee keeps the multiplied receipt after subtracting the return. The lecture calls $Y$ **trust** and $Z$ **trustworthiness**. These names describe choices in this experimental game; interpreting the choices as pure measures of one underlying motive requires further care. The lecture presents the setup as a simplified principal–agent problem: an investor creates an opportunity for an agent, whose subsequent action determines whether the investor recovers the investment. Its analogy to commission-taking or stealing is an interpretation of the payoff arrangement, rather than an additional enforced contractual rule. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=24|Social Preferences, physical PDF p. 24]]

**Agent unpacking of the lecture's payoff equations:** adding the two payoffs gives

$$
\begin{aligned}
x_{\mathrm{trustor}}+x_{\mathrm{trustee}}
&=(X-Y+Z)+(\alpha Y-Z)\\
&=X+(\alpha-1)Y.
\end{aligned}
$$

The back-transfer $Z$ cancels because it redistributes existing money between the players. The initial transfer creates a joint monetary surplus $(\alpha-1)Y$ because the experimental rules multiply it. Since $\alpha>1$, a larger $Y$ raises their combined monetary payoff, and $Y=X$ maximizes that sum within this setup. This is the sense in which cooperation can create surplus. A larger monetary sum does not by itself establish that each player's utility rises: distribution and the players' preferences still matter. The calculation uses the game's stated multiplication rule and includes no separate production cost. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=24|Social Preferences, physical PDF p. 24; algebraic interpretation]]

### The self-regarding prediction by backward induction

The lecture attributes the first experimental implementation to Berg, Dickhaut and McCabe (1995), using $X=\$10$ and $\alpha=3$. It asks for a **subgame-perfect equilibrium**, an equilibrium in which the prescribed choices remain optimal in every continuation of the game, including continuations that would not occur on the equilibrium path. The classroom poll on PDF p. 26 contains a question, but the supplied file displays no poll results. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=25|Social Preferences, physical PDF pp. 25–26]]

Under the lecture's benchmark, both players maximize their own monetary payoff and the trustor expects the trustee to do so. **Agent unpacking:** start with the last decision. For any positive $Y$, the trustee's payoff $\alpha Y-Z$ decreases one-for-one with $Z$, so the trustee chooses $Z=0$. Anticipating this, the trustor expects $X-Y$, which is maximized at $Y=0$. With no initial transfer, the trustee's feasible return is also zero. The prediction is therefore no initial transfer and no return, despite the potential joint surplus. The logic requires the self-regarding preferences and corresponding expectations; it is not a prediction for every possible preference model. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=27|Social Preferences, physical PDF p. 27]]

### Observed transfers and what they reveal

The lecture reports that most studies find about **45% of the endowment sent** and **around 33% transferred back**, characterizing the latter as around zero return to trust. These are the lecture's approximate summary figures, not results from the empty classroom poll or from one identified sample. PDF p. 27 does not explicitly define the denominator of the 33% figure. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=27|Social Preferences, physical PDF p. 27]]

**Conditional agent interpretation:** if the return proportion means $Z/(\alpha Y)$, then returning exactly one third of the trustee's receipt when $\alpha=3$ gives $Z=Y$. The trustor ends with $X-Y+Y=X$, a zero net monetary gain on the investment, while a positive initial transfer still creates a joint surplus. Using the rounded value 0.33 gives $Z=0.99Y$, approximately the same conclusion. This explains how the lecture's phrase can be consistent with its example, but it does not resolve the unspecified denominator. If 33% instead meant a proportion of the original endowment or of $Y$, the calculation would differ. Nor can multiplying separately reported averages reconstruct an average individual investment return without the underlying data. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=27|Social Preferences, physical PDF p. 27; conditional calculation]]

The lecture typically attributes back-transfers to reciprocal preferences: the trustee responds to the trustor's prior action. Initial transfers can reflect beliefs that the trustee will return money, altruism toward the trustee, or a concern for increasing the joint payoff. A positive $Y$ therefore does not uniquely identify a belief in repayment, and a back-transfer alone does not identify reciprocity separately from every other possible motivation. The game's role is to make these motivations visible and distinguish its behavior from the stated selfish benchmark. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=27|Social Preferences, physical PDF p. 27]]

### Reading the cross-country table

![[01_Notes/2026_2027/Winter_Semester/Behavioral_Economics/assets/Social_Preferences_p28_Trust_Country_Table.png]]

*Full source slide: Table 3, “Descriptive statistics by country,” lists 35 countries, the number of studies, total sample size, average fraction sent, and average proportion returned. The image preserves every country row and the missing return entry for Vietnam.* [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=28|Social Preferences, physical PDF p. 28]]

The columns separate evidence quantity from transfer behavior. For example, the United States row reports 46 studies, a total sample of 4,552, an average fraction sent of 0.51, and an average proportion returned of 0.34. South Korea reports one study and 52 observations, with 0.67 sent and 0.29 returned. Vietnam reports two studies, 194 observations, 0.33 sent, and “n/a” for returned. The missing entry is not a zero. The table visibly shows variation in reported transfers and very different amounts of evidence across rows. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=28|Social Preferences, physical PDF p. 28, table rows and headings]]

**Source limitation:** this slide supplies no author/year attribution for Table 3, sampling or pooling procedure, experimental-design controls, uncertainty intervals, or explicit denominator for the return column. The earlier citation to the original trust-game experiment does not establish the provenance of this later table. These descriptive averages therefore support a comparison of the displayed observations; they do not establish a causal effect of country, a representative ranking of national trust, or statistical significance of any difference. No underlying studies or external references were consulted to fill those gaps. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=28|Social Preferences, physical PDF p. 28; interpretation limits]]

## The prisoner's dilemma: a simultaneous conflict

In the lecture's **prisoner's dilemma**, two anonymous players cannot communicate and choose **cooperate** or **defect** simultaneously. Simultaneous means each chooses without knowing the other's current action. The first number in each payoff pair belongs to Player A, who chooses the row; the second belongs to Player B, who chooses the column. The monetary units are not specified on the numerical slide. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=29|Social Preferences, physical PDF pp. 29–31]]

| Player A's action | B cooperates | B defects |
|---|---|---|
| Cooperate | $(16,16)$ | $(8,20)$ |
| Defect | $(20,8)$ | $(12,12)$ |

![[01_Notes/2026_2027/Winter_Semester/Behavioral_Economics/assets/Social_Preferences_p32_Prisoners_Dilemma.png]]

*The full source slide preserves the numerical matrix and the lecture's dominant-strategy and Nash-equilibrium claims.* [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=32|Social Preferences, physical PDF p. 32]]

### Dominance and Nash equilibrium

A **strictly dominant strategy** gives a player a higher payoff than the alternative for every action of the other player. **Agent unpacking of the matrix:** if B cooperates, A gets 20 from defecting rather than 16 from cooperating; if B defects, A gets 12 rather than 8. Defection is therefore strictly dominant for A. By symmetry, it is strictly dominant for B too. A **Nash equilibrium** is a pair of strategies in which neither player benefits from changing their own choice while holding the other's fixed. Because each player's strict best response is always defection, $(D,D)$ is the unique Nash equilibrium under self-regarding preferences. The classroom question on PDF p. 30 has no displayed poll results. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=32|Social Preferences, physical PDF pp. 29–32]]

Each receives 12 in equilibrium, although mutual cooperation would give each 16. The difference is a conflict between the individually attractive deviation and the jointly preferable cooperative outcome. From $(C,C)$, either player can gain 4 by defecting alone. From $(D,D)$, switching alone to cooperation loses 4. Thus joint improvement does not make unilateral cooperation individually optimal. This illustrates the lecture's argument that privately costly cooperation can increase social welfare while a private incentive points toward defection. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=31|Social Preferences, physical PDF pp. 31–32; payoff interpretation]]

### General payoffs and finite repetition

The lecture's general symmetric matrix has $c>a>b>d$:

| Player A's action | B cooperates | B defects |
|---|---|---|
| Cooperate | $(a,a)$ | $(d,c)$ |
| Defect | $(c,d)$ | $(b,b)$ |

Here $c$ is the payoff from defecting against cooperation, $a$ the mutual-cooperation payoff, $b$ the mutual-defection payoff, and $d$ the payoff from cooperating against defection. The inequalities $c>a$ and $b>d$ make defection strictly dominant; $a>b$ makes mutual cooperation better for both than mutual defection. These inequalities alone do not state that mutual cooperation maximizes the sum among every possible cell, since no condition comparing $2a$ with $c+d$ is given. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=33|Social Preferences, physical PDF pp. 33–34; matrix interpretation]]

The lecture states that the unique subgame-perfect equilibrium of a finitely repeated prisoner's dilemma is defection in every period. **Agent unpacking of the required benchmark:** take a fixed pair of rational, self-regarding players, a commonly known finite final period, the same stage game in every period, and payoffs given by the sum of the stage payoffs, possibly discounted by positive weights. In the last period there is no future reward or punishment left, so both defect after every possible preceding history. In the penultimate period, last-period defection will occur regardless of today's choices, so the current dominant-strategy logic again gives defection. Repeating this argument backward establishes defection at every stage and after every history. This is stronger than just specifying the actions on one realized path. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=34|Social Preferences, physical PDF p. 34; backward-induction explanation]]

The result is conditional on that benchmark, especially the known finite horizon and self-regarding preferences. A chance to meet again does not by itself overturn the backward-induction argument. The argument presented here does not cover an uncertain or indefinite horizon, uncertainty about the other player's preferences, or the social-preference changes introduced next. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=34|Social Preferences, physical PDF pp. 34–36; scope of the prediction]]

## A warm-glow premium can change best responses

The lecture observes that many subjects cooperate to some extent even in finitely repeated or one-shot versions. It proposes altruism or efficiency-seeking as one explanation, represented by a **warm-glow premium** $\delta$ for Player 1's act of cooperating. The premium is measured in money-equivalent utility units and is added to Player 1's payoff whenever Player 1 cooperates, regardless of Player 2's action. Player 2 remains selfish. In this illustration Player 1 is A, the row player. This particular additive model captures a benefit from the act of cooperation; it is not the same formula as directly weighting the other person's payoff in the social-preference model. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=35|Social Preferences, physical PDF p. 35]]

![[01_Notes/2026_2027/Winter_Semester/Behavioral_Economics/assets/Social_Preferences_p35_Warm_Glow_Payoffs.png]]

*Full source slide: only A's cooperative-row payoffs acquire $\delta$. The source's classification and its final cooperation assertion remain visible; the assertion is qualified below.* [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=35|Social Preferences, physical PDF p. 35]]

### Deriving the two thresholds

**Agent unpacking of the lecture's altered matrix:** when B cooperates, A compares $a+\delta$ with $c$. Cooperation is strictly preferred when

$$
a+\delta>c
\quad\Longleftrightarrow\quad
\delta>c-a.
$$

When B defects, A compares $d+\delta$ with $b$, giving

$$
d+\delta>b
\quad\Longleftrightarrow\quad
\delta>b-d.
$$

The two positive thresholds are the monetary costs of choosing cooperation in the two situations. If $\delta<\min(c-a,b-d)$, neither cost is compensated and A strictly prefers defection against either action. The lecture labels this player an **egoist** in its behavioral classification, even though a small positive premium may be present. If $\delta>\max(c-a,b-d)$, both costs are compensated and cooperation is strictly dominant: the lecture calls this a **dominant-strategy altruist**. At equality with either threshold, A is indifferent in the corresponding comparison, so the strict classifications do not apply there. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=35|Social Preferences, physical PDF p. 35; threshold derivation]]

For intermediate values, the lecture uses the name **best-response altruist**. There are two distinct orderings, and $c>a>b>d$ alone does not choose between them:

| Ordering and intermediate premium | A's best response if B cooperates | A's best response if B defects |
|---|---|---|
| $c-a<\delta<b-d$ | Cooperate | Defect |
| $b-d<\delta<c-a$ | Defect | Cooperate |

In the first case cooperation is conditional on B's cooperation; in the second, the premium covers the cost of cooperating against defection but not the cost of cooperating against cooperation. **Agent derivation with beliefs:** if A assigns probability $\pi$ to B cooperating, its expected utility advantage of cooperation is

$$
\begin{aligned}
\Delta U_A
&=\pi(a+\delta)+(1-\pi)(d+\delta)
 -\bigl[\pi c+(1-\pi)b\bigr]\\
&=\delta-\bigl[\pi(c-a)+(1-\pi)(b-d)\bigr].
\end{aligned}
$$

A strictly cooperates if this expression is positive, defects if it is negative, and is indifferent at zero. Thus an intermediate premium generally requires beliefs about B's action to predict A's choice. This calculation unpacks the displayed matrix; the lecture does not supply this expected-utility equation. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=35|Social Preferences, physical PDF p. 35; agent derivation]]

### The numerical threshold and a source qualification

In the numerical game, $c-a=20-16=4$ and $b-d=12-8=4$. Therefore $\delta<4$ makes defection strictly dominant for A, while $\delta>4$ makes cooperation strictly dominant. At $\delta=4$, A is indifferent between the actions against either choice of B. There is no nonempty intermediate interval in this particular matrix because the two thresholds coincide. Since B remains selfish and its own payoffs are unchanged, B continues to defect. Consequently a premium greater than 4 predicts A cooperating against B's defection, rather than mutual cooperation. These are agent calculations from the source's numerical and altered matrices. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=32|Social Preferences, physical PDF p. 32]] [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=35|Social Preferences, physical PDF p. 35]]

**Source assertion and limitation:** PDF p. 35 says that cooperation will be observed whenever players include dominant-strategy altruists or best-response altruists. The claim is broader than the displayed matrix supports without qualifications. A dominant-strategy altruist does cooperate. But a best-response altruist with $c-a<\delta<b-d$, correctly expecting the stipulated selfish B to defect, also defects. Conversely, a best-response altruist with $b-d<\delta<c-a$ cooperates against B's defection. The source statement is retained here as a statement from the lecture; the payoff ordering and beliefs must be specified before extending it to every player in the intermediate category. Merely having that category in a population does not guarantee observed cooperation or mutual cooperation. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=35|Social Preferences, physical PDF p. 35, final bullet]]

## Reciprocity needs an expectation about the other player

The lecture's second explanation is **positive reciprocity combined with the belief that the other person will cooperate**. It cites Dawes and Thaler (1988) beside the observation that cooperation occurs even with a finite number of interactions, sometimes only once; the uploaded slide does not supply the underlying study design, sample, or numerical cooperation rate. Positive reciprocity means wanting to respond kindly to perceived kindness. In a simultaneous game there is no observed current action to reciprocate at the moment of choice, so an expectation about the other's cooperation is part of this proposed explanation. The lecture does not specify a separate payoff formula or a quantitative belief threshold for this mechanism. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=36|Social Preferences, physical PDF p. 36]]

This differs from the trust game, where the trustee observes the initial transfer before returning money. It also differs from the unconditional warm-glow premium: a desire to reward kindness depends on how the other player's behavior is perceived or expected. The [[01_Notes/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/Models_of_Social_Preferences.md|reciprocity model]] makes this dependence explicit. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=22|Social Preferences, physical PDF p. 22]] [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=36|Social Preferences, physical PDF p. 36; connection between games]]

## What these games establish

The trust game separates surplus creation from its subsequent division; the prisoner's dilemma exposes a dominant individual incentive that conflicts with mutual gains. Their no-trust or defection benchmarks follow from specified self-regarding preferences and expectations, not from the game labels alone. The lecture's empirical descriptions motivate broader preferences, and its warm-glow matrix shows exactly how a sufficiently large nonmonetary benefit can change a best response. Intermediate benefits and reciprocity require attention to the other player's expected behavior. The lecture's final lesson is that many motivations extend beyond pure selfishness and that social preferences **can** increase social welfare, a possibility whose realization depends on the game, preferences, and beliefs. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=37|Social Preferences, physical PDF p. 37]]
