---
course: Econometrics_II
course_id: 2026_2027/Winter_Semester/Econometrics_II
week: 1
sources:
  - 00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf
---

# OLS estimator and assumptions

How does a regression coefficient relate an observed sample to the population relationship we want to study? Week 1 revises ordinary least squares (OLS), then asks which assumptions make its coefficients trustworthy. The formula is a sample calculation; unbiasedness, consistency, and efficiency are properties that require a model of how the data were generated. This distinction prepares the course's later extensions to other data structures. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=10|Lecture 1, PDF pp. 10–11]]

Back to [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Econometrics_II_main#Week 1|Econometrics II — Week 1]].

## Population model, sample, and notation

The lecture uses the simple population regression

$$
y_i=\beta_0+\beta_1x_i+u_i,\qquad i=1,\ldots,n.
$$

Here $i$ labels an observation, $n$ is the sample size, $y_i$ is the dependent variable, and $x_i$ is one explanatory variable. The population parameters $\beta_0$ and $\beta_1$ describe the intercept and slope. The disturbance $u_i$ collects the variation in $y_i$ that the specified systematic part does not explain. A hat indicates a sample estimator or its realized estimate, so $\hat\beta_1$ differs conceptually from the fixed population parameter $\beta_1$. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=14|Lecture 1, PDF pp. 14–15]]

The slope measures the change in the systematic part of $y$ associated with a one-unit change in $x$. Its units are units of $y$ per unit of $x$. The intercept is the systematic value at $x=0$; interpreting it substantively requires that zero be meaningful and relevant to the data. A causal interpretation of the slope requires appropriate assumptions about the disturbance and regressor; the existence of a fitted line by itself does not establish causation. These interpretations unpack the model used in the lecture and the units-and-parameters task in the seminar. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=14|Lecture 1, PDF p. 14]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=1|Seminar 1, PDF p. 1, Problem 1(ii)]]

## How OLS chooses the line

**Algebraic explanation of the lecture's estimator.** OLS selects coefficients $b_0,b_1$ to minimize the sum of squared residuals,

$$
Q(b_0,b_1)=\sum_{i=1}^n(y_i-b_0-b_1x_i)^2.
$$

Differentiating with respect to $b_0$ and $b_1$ gives the two normal equations: $\sum_i(y_i-b_0-b_1x_i)=0$ and $\sum_ix_i(y_i-b_0-b_1x_i)=0$. The first equation implies $b_0=\bar y-b_1\bar x$. Substituting this into the second equation produces the centered formula shown in the lecture:

$$
\hat\beta_1=\frac{S_{xy}}{S_{xx}}
=\frac{\sum_{i=1}^n(x_i-\bar x)(y_i-\bar y)}
{\sum_{i=1}^n(x_i-\bar x)^2},
\qquad
\hat\beta_0=\bar y-\hat\beta_1\bar x.
$$

The bars denote sample means. The numerator measures how $x$ and $y$ vary together around their means; the denominator measures the sample variation available in $x$. The slope therefore compares co-movement with regressor variation. If every $x_i$ is identical, $S_{xx}=0$, so the data cannot distinguish the slope from the intercept. The minimization steps are an agent explanation of the displayed source formula, rather than additional lecture slides. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=15|Lecture 1, PDF p. 15]]

The fitted value is $\hat y_i=\hat\beta_0+\hat\beta_1x_i$ and the residual is $\hat u_i=y_i-\hat y_i$. Residuals are observable after estimation; population disturbances are generally unobserved. With an intercept, the normal equations ensure $\sum_i\hat u_i=0$ and $\sum_ix_i\hat u_i=0$. These are fitting identities and do **not** establish the population exogeneity assumption $E[u_i\mid x_i]=0$. The seminar asks for residuals precisely because they can be calculated from the observed data and fitted line. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=1|Seminar 1, PDF p. 1, Problem 1(iv)]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=18|Lecture 1, PDF p. 18]]

## The assumption ladder

The lecture uses Wooldridge's numbering. State the assumptions by name as well as number, because different textbooks number them differently. The following notation makes the lecture's named assumptions explicit. For multiple regression let $x_i=(x_{i1},\ldots,x_{ik})$ contain the $k$ nonconstant regressors, and let $X$ denote the full sample design, including an intercept. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=18|Lecture 1, PDF p. 18]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=25|Lecture 1, PDF p. 25]]

| Assumption | Meaning and role |
|---|---|
| Linear in parameters (MLR.1) | $y_i=\beta_0+\sum_{j=1}^k\beta_jx_{ij}+u_i$. Linearity refers to the coefficients: a regressor can itself be a transformation, provided the specified model remains linear in its parameters. This supplies the decomposition used in the estimator proofs. |
| Random sampling (MLR.2) | Observations are independent draws from the population under study. The lecture emphasizes representativeness and independence. This justifies the cross-sectional sampling argument and the law-of-large-numbers reasoning used later. A convenience sample is not made representative by running OLS. |
| No perfect collinearity (MLR.3) | No regressor is an exact linear combination of the others, and each nonconstant regressor has variation. In simple regression this requires $S_{xx}>0$; in multiple regression it makes the design matrix full rank. Otherwise coefficients cannot be uniquely separated. |
| Zero conditional mean (MLR.4) | $E[u_i\mid x_{i1},\ldots,x_{ik}]=0$. Once the included regressors are fixed, the average disturbance is zero. Under the sampling assumptions this yields $E[u_i\mid X]=0$ in the source's conditional proof. |
| Homoskedasticity (MLR.5) | $\operatorname{Var}(u_i\mid x_i)=\sigma^2$, a constant finite variance. With the preceding assumptions, this establishes the Gauss–Markov efficiency result. |
| Normality (MLR.6) | The disturbance has a conditional normal distribution; together with the preceding assumptions, this gives normal conditional coefficient distributions and exact null $t$ and $F$ distributions. |

The lecture introduces the first four assumptions for unbiasedness, adds homoskedasticity for BLUE, and adds normality for classical finite-sample inference. The formal statements here explain that sequence; they should not be read as claims that the seminar data automatically satisfy it. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=16|Lecture 1, PDF pp. 16–19]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=23|Lecture 1, PDF pp. 23–26]]

## Why multiple regression uses matrix notation

The lecture asks why matrix notation is more convenient when there is more than one regressor. **Agent explanation:** write $y=X\beta+u$, where $y$ and $u$ are $n\times1$ vectors, $X$ is $n\times(k+1)$, and $\beta$ is $(k+1)\times1$. Its first column is ones. Minimizing $(y-Xb)'(y-Xb)$ yields $X'X\hat\beta=X'y$. If $X$ has full column rank,

$$
\hat\beta=(X'X)^{-1}X'y
=\beta+(X'X)^{-1}X'u.
$$

The prime means transpose. The inverse exists under no perfect collinearity. This single expression handles every coefficient jointly, instead of treating each regressor as a separate simple regression. Joint estimation matters because the slope for a regressor holds the other included regressors fixed; omitting them generally changes the comparison being made. This is the extension requested in the seminar's alternative-specification table. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/2026_Lecture1_print.pdf#page=15|Lecture 1, PDF p. 15, matrix-notation question]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_1/Seminar 1 OS/Seminar1.pdf#page=2|Seminar 1, PDF p. 2, Problem 1(vi)–(vii)]]

## What to carry forward

OLS always describes a calculation once the data and specification are fixed. The assumption ladder determines what can be concluded about repeated samples, large samples, relative precision, and hypothesis tests. [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_1/Unbiasedness_Consistency_and_Efficiency|Unbiasedness, consistency, and efficiency]] proves these distinctions using the estimator's disturbance term. [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_1/Transport_Demand_Regression_Seminar|The transport-demand seminar]] applies the calculation and shows why a change in controls can change the estimated price relationship.
