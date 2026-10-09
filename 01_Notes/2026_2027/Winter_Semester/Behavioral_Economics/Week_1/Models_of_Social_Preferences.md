---
course: Behavioral_Economics
course_id: 2026_2027/Winter_Semester/Behavioral_Economics
week: 1
sources:
  - 00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf
---

# Models of social preferences

What changes in an economic model when a person cares about someone else's payoff, relative inequality, or how that person behaved? Social-preference models specify these concerns in utility rather than treating every departure from monetary selfishness as the same phenomenon. This presentation introduces a two-person payoff model, then adds a simple reciprocity term. The purpose is to generate different predictions that can be compared with games such as the ultimatum, dictator and trust games. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=12|Social Preferences, physical PDF pp. 12–14, 22–24]]

Return to [[01_Notes/2026_2027/Winter_Semester/Behavioral_Economics/Behavioral_Economics_main.md#Week 1|Behavioral Economics — Week 1]]. [[01_Notes/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/Ultimatum_and_Dictator_Games.md|Ultimatum and dictator games]] explains the evidence motivating a broader set of motivations.

## Two assumptions that the lecture brings into question

The lecture contrasts broader motivations with two traditional assumptions. **Selfish preferences** make utility a function only of one's own payoff; without reputation-building, the benchmark does not add concern for another person's treatment or fairness. **Exogenous preferences** treat motivations as largely fixed traits, unresponsive to personal experiences or environmental factors. These are distinct claims: including another person's payoff changes the content of utility, while allowing preferences to respond to experience concerns where preferences come from. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=13|Social Preferences, physical PDF p. 13]]

The presentation develops the first issue through payoff weights and behavior-dependent reciprocity. It does not estimate how preferences evolve over a lifetime or provide a formal preference-formation model. Its motivation is that social preferences can support cooperation and economic surplus, linked in the lecture to social capital. “Can” matters: some broader motivations, such as spite or negative reciprocity, also permit costly harm. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=13|Social Preferences, physical PDF pp. 13, 18–19, 22, 37]]

## A piecewise utility function for two people

Let $x_1$ be person 1's monetary payoff and $x_2$ person 2's payoff, measured in the same monetary units. $U_1$ describes person 1's preferences over the pair. The lecture presents the following example under the heading Charness and Rabin (2002):

$$
U_1(x_1,x_2)=
\begin{cases}
\rho x_2+(1-\rho)x_1,& x_1\ge x_2,\\
\sigma x_2+(1-\sigma)x_1,& x_1<x_2.
\end{cases}
$$

The dimensionless parameter $\rho$ weights the other person's payoff when person 1 is at least as well off; $\sigma$ applies when person 1 is behind. The coefficient on one's own payoff is correspondingly $1-\rho$ or $1-\sigma$. The conditions refer to monetary payoffs, not to a comparison of the two people's utilities. The lecture supplies this simplified example; it is not a reproduction of the full cited paper. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=14|Social Preferences, physical PDF pp. 14–18, 20]]

**Algebraic unpacking:** when $x_1\ge x_2$, write utility as $x_1-\rho(x_1-x_2)$; when $x_1<x_2$, write it as $x_1+\sigma(x_2-x_1)$. At equality both expressions give $U_1(x,x)=x$, so the pieces meet. Their slopes can differ at the equality line. Changing $\rho$ or $\sigma$ changes how person 1 trades off own income against the other person's outcome. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=14|Social Preferences, physical PDF pp. 14, 20–21]]

## How to read the indifference curves

An **indifference curve** joins payoff pairs giving the same utility to person 1. In the source figures the vertical axis is $x_1$ and the horizontal axis is $x_2$. The gray diagonal marks equal monetary payoffs. Do not reverse the axes when interpreting the curve's slope. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=15|Social Preferences, physical PDF pp. 15, 17, 19, 21]]

Within either regime, let $w$ stand for its active weight, $\rho$ or $\sigma$, and fix utility at $k$. **Derived from the displayed function**, for $w\ne1$,

$$
w x_2+(1-w)x_1=k
\quad\Rightarrow\quad
x_1=\frac{k-wx_2}{1-w},
\qquad
\frac{dx_1}{dx_2}=-\frac{w}{1-w}.
$$

With $w=0$ the curve is horizontal. With $0<w<1$ it slopes downward: more income for person 2 can compensate for less own income. With $w<0$ it slopes upward: when the other person's gain lowers utility, own income must rise to compensate. These slope descriptions use the source figures' positive own-payoff coefficient. The lecture's general positive-weight statement does not itself impose an upper bound on every altruistic weight; if $w=1$, own payoff drops out and the curve is vertical, while $w>1$ changes the own-payoff sign. These boundary cases are algebraic qualifications, not additional empirical claims. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=14|Social Preferences, physical PDF pp. 14–19]]

## Selfishness, altruism and spitefulness

### Selfish preferences

Setting $\rho=\sigma=0$ gives $U_1=x_1$. The other person's monetary payoff has no direct effect on person 1's utility. This is the benchmark used to solve the anonymous games by monetary incentives alone. A horizontal indifference curve means that any $x_2$ is equally attractive when $x_1$ is unchanged; the upward arrow in the source shows preference for more own income. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=15|Social Preferences, physical PDF p. 15]]

![[01_Notes/2026_2027/Winter_Semester/Behavioral_Economics/assets/Social_Preferences_p15_Selfish_Indifference.png]]

*Source slide 15: own payoff is vertical, the other person's payoff horizontal. With both social weights zero, the horizontal curves preserve own payoff, and higher curves are preferred.* [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=15|Social Preferences, physical PDF p. 15]]

### Altruism

The lecture calls $\rho>0$ and $\sigma>0$ **pure altruism**: the other person's payoff enters utility positively whether person 1 is ahead or behind. It sometimes adds $0<\sigma<\rho$, meaning greater weight on the other person when that person has less than one's own payoff. In that case, the weight changes at equality even though both weights remain positive. Do not confuse the larger ahead-regime weight with a negative behind-regime weight. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=16|Social Preferences, physical PDF pp. 16–17]]

![[01_Notes/2026_2027/Winter_Semester/Behavioral_Economics/assets/Social_Preferences_p17_Altruism_Indifference.png]]

*Source slide 17: downward-sloping segments show willingness to trade own income against the other person's income in the plotted positive-own-weight case. A change of slope at the equality diagonal represents different weights across the two regimes. The figure supplies no numerical parameter estimate.* [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=17|Social Preferences, physical PDF p. 17]]

### Spitefulness

For **spiteful preferences**, $\rho<0$ and $\sigma<0$. Increasing the other person's payoff while holding one's own fixed lowers utility in either regime. This is different from being selfish: a selfish person is indifferent to that change, while a spiteful person dislikes it. The own-payoff coefficient is then greater than one, and the indifference segments slope upward. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=18|Social Preferences, physical PDF pp. 18–19]]

![[01_Notes/2026_2027/Winter_Semester/Behavioral_Economics/assets/Social_Preferences_p19_Spite_Indifference.png]]

*Source slide 19: upward-sloping curves show that a higher other-person payoff requires extra own income to maintain utility. The preference arrow points toward more own income and less income for the other person; the gray equality line locates the payoff regimes.* [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=19|Social Preferences, physical PDF p. 19]]

## Inequality aversion changes sign across equality

**Inequality aversion** dislikes disparities between own and another person's monetary payoff. The lecture labels its discussion Fehr and Schmidt (02) and specifies

$$
0<\rho<1,\qquad \sigma<0,\qquad \sigma<-\rho<0.
$$

When person 1 is ahead, the positive $\rho$ means that increasing the poorer person's payoff at fixed own income reduces the disparity and raises utility. When person 1 is behind, the negative $\sigma$ means that increasing the richer person's payoff at fixed own income widens the disparity and lowers utility. The last inequality says $-\sigma>\rho$: the disadvantageous-inequality penalty is stronger than the advantageous-inequality penalty. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=20|Social Preferences, physical PDF pp. 20–21]]

The rewritten function makes the penalties explicit:

$$
U_1=
\begin{cases}
x_1-\rho(x_1-x_2),&x_1\ge x_2,\\
x_1-(-\sigma)(x_2-x_1),&x_1<x_2.
\end{cases}
$$

This is derived from the source's function, not an extra estimated model. The first penalty subtracts a fraction of the amount by which person 1 is ahead; the second subtracts a positive weight times the amount by which person 1 is behind. The model still values own income. It does not imply that any equal allocation is always preferred to every unequal allocation regardless of the amount of money involved. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=14|Social Preferences, physical PDF pp. 14, 20–21]]

![[01_Notes/2026_2027/Winter_Semester/Behavioral_Economics/assets/Social_Preferences_p21_Inequality_Indifference.png]]

*Source slide 21: each curve slopes down in the ahead region above the equality diagonal, then up in the behind region below it. The kink reflects a change from positive to negative weight on the other person's payoff. Higher-own-payoff curves represent higher utility; the picture is qualitative, not an estimate of the two penalty parameters.* [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=21|Social Preferences, physical PDF p. 21]]

This distinction helps interpret ultimatum rejection: a receiver may prefer both players receiving zero to accepting a strongly disadvantageous positive split if the inequality penalty is sufficiently large. The relevant comparison is utility, not only money. Whether rejection occurs depends on the person's parameters and offered allocation; the lecture's aggregate rejection rates do not identify those parameters for each individual. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=3|Social Preferences, physical PDF pp. 3, 8, 20–21]]

## Reciprocity responds to prior treatment

**Reciprocity** means kindness toward someone who acted kindly and hostility toward someone who acted unkindly. The source adds $q=1$ for person 2's kind action and $q=-1$ for misbehavior, with sensitivity $\theta>0$:

$$
U_1(x_1,x_2)=(\rho+\theta q)x_2+(1-\rho-\theta q)x_1.
$$

Define the effective social weight $w(q)=\rho+\theta q$. A kind action gives $w(1)=\rho+\theta$; misbehavior gives $w(-1)=\rho-\theta$. Thus treatment changes the weight on the other person's payoff by $2\theta$ between these two states. A negative response weight follows if $\theta>\rho$; $\theta>0$ alone does not ensure that the total weight becomes negative. These comparisons unpack the supplied equation. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=22|Social Preferences, physical PDF p. 22]]

Reciprocity therefore differs from unconditional altruism and from payoff inequality alone. Two identical monetary allocations can have different utility if prior treatment changes $q$. The lecture defines the two kindness states but supplies no detailed rule for measuring perceived intentions or estimating $\theta$. The displayed equation is a simple illustration, not a full solution of every strategic game or a replacement of the earlier two-regime function in all contexts. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=22|Social Preferences, physical PDF pp. 22, 27, 36]]

## Efficiency-seeking and the welfare connection

The lecture names **efficiency-seeking** alongside the other social preferences and lists it as a possible reason for trustor transfers. Its relevant intuition is concern for the total monetary surplus that cooperation can create. The presentation does not give a separate complete efficiency-seeking utility function or identify it from one observed transfer. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=12|Social Preferences, physical PDF pp. 12, 27, 35, 37]]

**Agent-created illustration using the displayed model:** $\rho=\sigma=1/2$ yields $U_1=(x_1+x_2)/2$, so maximizing this particular utility is equivalent to maximizing total monetary payoff. This illustrates how the existing payoff weights can value a larger total; it is not a claim that the lecture estimates those parameters or that all efficiency-seeking preferences take this exact form. Concern about totals, distribution and kind treatment can produce similar choices in some games, making the experimental comparison important. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=14|Social Preferences, physical PDF pp. 14, 27]]

[[01_Notes/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/Trust_and_Cooperation_Games.md|Trust and cooperation games]] develops the distinction between splitting a fixed pie and expanding monetary surplus. Social preferences can encourage the latter, while beliefs and incentives still determine whether cooperation occurs. The central result of these models is a set of distinct mechanisms—positive payoff weights, negative payoff weights, disparity penalties and treatment-dependent weights—not a single universal “unselfish” preference. [[00_Materials/2026_2027/Winter_Semester/Behavioral_Economics/Week_1/L2 BE_SocPrefs IES 2026.pdf#page=23|Social Preferences, physical PDF pp. 23–24, 35–37]]
