---
course: Econometrics_II
course_id: 2026_2027/Winter_Semester/Econometrics_II
week: 2
sources:
  - 00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf
  - 00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf
---

# Trends, detrending, and seasonality

When two economic series both rise over time, how much of their apparent relationship is merely a shared time pattern? Week 2 treats this as a specification question. Omitting a relevant trend can put systematic influences in the disturbance that are correlated with a regressor. Including an appropriate time trend or removing the same trend from every modeled variable can isolate the relationship between their deviations from trend. Repeating seasonal patterns require a related calendar adjustment. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=26|Lecture 2, PDF pp. 26–30]]

Back to [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Econometrics_II_main#Week 2|Econometrics II — Week 2]]. [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_2/Time_Series_OLS_and_Strict_Exogeneity|Time-series OLS and strict exogeneity]] supplies the zero-conditional-mean condition and no-perfect-collinearity rule needed when introducing trend or seasonal regressors.

## What the source's three trend plots show

![[01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/lecture2_p32_GDP_against_productivity.png]]

*Original embedded image: GDP against productivity, Lecture 2, PDF p. 32. The connected observations show a strong positive association in levels; the axes provide variable names and numeric scales but no units or country/sample provenance.* [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=32|Lecture 2, PDF p. 32]]

![[01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/lecture2_p33_GDP_over_time.png]]

*Original embedded image: GDP against Year, Lecture 2, PDF p. 33. GDP generally increases over the displayed years, with a pause or decline around the late 2000s.* [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=33|Lecture 2, PDF p. 33]]

![[01_Notes/2026_2027/Winter_Semester/Econometrics_II/assets/lecture2_p34_productivity_over_time.png]]

*Original embedded image: productivity against Year, Lecture 2, PDF p. 34. Productivity also generally increases over the displayed years.* [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=34|Lecture 2, PDF p. 34]]

Together the plots make the lecture's concern concrete: the positive relationship in the first image is observed between two variables that both trend in time. They do not establish that the entire relationship is spurious, nor do they provide detrended estimates or a causal test. The missing units and dataset provenance prevent a numerical slope interpretation from these figures alone. Their role is to motivate controlling the time pattern rather than treating the raw association as decisive evidence. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=26|Lecture 2, PDF pp. 26, 32–34]]

## Choose a time form that matches the comparison

A linear trend $y_t=a_0+a_1t+e_t$ has expected level $E[y_t]=a_0+a_1t$ when $E[e_t]=0$; $a_1$ is an average level change per period. A constant average percentage growth rate instead suggests a linear trend in the logarithm, $\log y_t=b_0+b_1t+e_t$ for $y_t>0$, with small-change growth approximately $100b_1\%$ per period. A quadratic trend adds $a_2t^2$ to allow curvature. These are alternative representations of a deterministic time pattern, not interchangeable instructions to apply the same linear trend to every original series. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=392|Wooldridge, 5th ed., PDF p. 392 (printed p. 364)]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=393|Wooldridge, 5th ed., PDF p. 393 (printed p. 365)]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=394|Wooldridge, 5th ed., PDF p. 394 (printed p. 366)]]

The textbook cautions against adding enough polynomial terms merely to track every movement: a simple broad time pattern serves the substantive model better than an arbitrarily flexible curve. A trend can coexist with correlated deviations around it, so trending variables do not automatically violate the classical assumptions if the model properly includes the relevant pattern. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=394|Wooldridge, 5th ed., PDF p. 394 (printed p. 366)]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=396|Wooldridge, 5th ed., PDF p. 396 (printed p. 368)]]

## Shared trends as an omitted-variable problem

The lecture calls a relationship **spurious correlation** when the apparent association arises simply because both variables grow over time. Its explanation is that trending influences on $y_t$ are omitted and correlated with an explanatory variable. This can violate zero conditional mean, the condition required by the time-series unbiasedness proof. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=26|Lecture 2, PDF pp. 26–27]]

**Agent algebraic illustration of that mechanism.** Suppose the intended specification is

$$
y_t=\beta_0+\beta_1x_t+\gamma t+\varepsilon_t.
$$

If we omit $t$, the short-model disturbance becomes $u_t=\gamma t+\varepsilon_t$. If $x_t$ also trends, its values can be correlated with this omitted component. The short-model slope then absorbs some common time pattern rather than isolating the relationship conditional on time. A large raw $R^2$ does not demonstrate that the substantive regressor accounts for the movement independently of trend. This example explains the source's omitted-variable interpretation; it is not an estimated equation for its GDP/productivity figures. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=26|Lecture 2, PDF pp. 26–28]]

## Include an appropriate time trend

The source's first remedy is to include the missing time variable in the regression. In the illustrative linear-trend model above, $t$ counts periods, $\gamma$ measures the systematic change per period, and $\beta_1$ compares $y$ and $x$ after holding this time component fixed. The trend is an additional regressor, so it must satisfy the design's full-rank requirement. If $x$ is exactly a linear function of the intercept and $t$, its separate slope cannot be identified; if it is nearly so, the coefficient may be imprecise. This is an agent application of TS3 to the source's remedy. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=28|Lecture 2, PDF p. 28]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=12|Full rank, PDF p. 12]]

The advantage is a simple single regression. The source warns that its overall $R^2$ can be high because the trend explains much of the original outcome variation. That $R^2$ measures the fit of **all included regressors**, including time; it does not isolate the explanatory contribution of the substantive variable. Page 28 describes the difficulty as being unable to tell what portion is explained by explanatory variables when time is not counted as a substantive explanatory variable. Read this as a warning about interpreting the overall $R^2$, rather than a statement that no conditional comparison is possible. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=28|Lecture 2, PDF p. 28, pros and cons]]

**Qualification of the source's remedy:** pp. 28–29 say that adding a trend or detrending eliminates the problem. The appropriate claim is conditional: removing a correctly specified common deterministic trend addresses that omitted component. Merely adding some trend does not prove exogeneity or remove every possible time-series specification problem. The uploaded slides provide no formal result guaranteeing that a linear trend cures arbitrary trending processes. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=28|Lecture 2, PDF pp. 28–29]]

The textbook also distinguishes deterministic trend from strong persistence. Its next-week discussion shows that a process can have a trending mean without strong persistence, or strong persistence without an obvious trend; fitting a deterministic trend is therefore not a universal treatment for all persistent processes. Only this limitation is carried into Week 2; random-walk derivations and transformation methods remain next-week material. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=422|Wooldridge, 5th ed., PDF p. 422 (printed p. 394)]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=423|Wooldridge, 5th ed., PDF p. 423 (printed p. 395)]]

## Detrend every variable using the same time form

The second remedy regresses each modeled variable on time and uses the residuals in the substantive regression. **Agent expansion of the source's linear-trend procedure:** first estimate

$$
y_t=a_y+b_yt+\tilde y_t,
\qquad
x_t=a_x+b_xt+\tilde x_t
$$

by OLS over the same sample, including an intercept in both detrending regressions. The residual $\tilde y_t$ is the outcome's deviation from its fitted time trend, and $\tilde x_t$ is the corresponding regressor deviation. Then regress $\tilde y_t$ on $\tilde x_t$. With multiple substantive regressors, detrend each one against the same intercept/trend columns and sample. The source stresses using the same form of time trend for all variables; changing the form or rows changes what is being removed. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=29|Lecture 2, PDF p. 29]]

Wooldridge explicitly confirms this residualization procedure and its equal-slope interpretation for the same sample and trend controls, including polynomial trends. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=397|Wooldridge, 5th ed., PDF p. 397 (printed p. 369)]]

### Why the slope agrees with including the trend

The source gives no board-work derivation. The following is an **agent derivation** from OLS normal equations that makes the proposed method executable. In the full regression of $y$ on an intercept, $t$, and $x$, let $e_t$ be the fitted residual. It is orthogonal to the intercept and time: $\sum_te_t=\sum_tte_t=0$. It is also orthogonal to $x$: $\sum_tx_te_t=0$. Since $x_t=a_x+b_xt+\tilde x_t$, these equations imply $\sum_t\tilde x_te_t=0$.

The detrended variables are themselves orthogonal to the intercept and time. Substituting the two detrending decompositions into the full model and multiplying by $\tilde x_t$, the intercept/time terms drop out of the summed equation. Therefore

$$
\hat\beta_1
=\frac{\sum_t\tilde x_t\tilde y_t}
{\sum_t\tilde x_t^2},
$$

which is exactly the residual-regression slope, provided the denominator is positive. This shows why detrending both variables with identical controls isolates the same slope as including those controls in the full OLS regression. It does not supply an exogeneity assumption; it is a sample algebraic identity. The reasoning extends to several substantive regressors by their joint normal equations. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=29|Lecture 2, PDF p. 29, detrending procedure]]; [[01_Notes/2026_2027/Winter_Semester/Econometrics_II/Week_1/OLS_Estimator_and_Assumptions#How OLS chooses the line|OLS normal equations]]

Because the detrended residuals have zero mean, the residual regression has fitted intercept zero when an intercept is included. Its $R^2$ can be written as

$$
R^2_{detrended}=1-\frac{\sum_t e_t^2}{\sum_t\tilde y_t^2}.
$$

The denominator is outcome variation **remaining after removal of the fitted trend**, not the original outcome's total variation. Its interpretation is the fraction of that remaining variation fitted by the detrended substantive regressors. If $y$ is perfectly explained by the trend, this denominator is zero and the detrended $R^2$ is undefined. The source's claim that this $R^2$ is informative should be read with its changed denominator in view. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=29|Lecture 2, PDF p. 29, $R^2$ interpretation]]

A concrete textbook example explains why the denominator matters. For 42 annual U.S. housing observations (1947–1988), the estimated log-price elasticity of real per-capita housing investment is $1.241$ (standard error $0.382$) without a trend, but $-0.381$ (standard error $0.679$) with a linear trend. The trend-model overall $R^2$ is $0.341$, while the version that first nets the trend out of the outcome has $R^2=0.008$. The substantive price variable explains very little of the deviations around trend in that fitted model. The book cautions that separate trend-regression standard errors may be unreliable because of serial correlation; these are reported textbook estimates, not independent data re-estimates or proof of no economic price effect. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=395|Wooldridge, 5th ed., PDF p. 395 (printed p. 367)]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=399|Wooldridge, 5th ed., PDF p. 399 (printed p. 371)]]

The same source confirms $1-SSR/\sum_t\tilde y_t^2$ and the need to preserve full-model degrees of freedom. For a classical $F$ test computed using an $R^2$ formula, use the usual full/restricted-model $R^2$ values, not a substitute detrended goodness-of-fit measure. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=398|Wooldridge, 5th ed., PDF p. 398 (printed p. 370)]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=399|Wooldridge, 5th ed., PDF p. 399 (printed p. 371)]]

**Inference bookkeeping:** equal slopes do not license naive degrees of freedom from a second-stage software printout. In the example with an intercept, one time trend, and one substantive regressor, the full model estimates three coefficients, so conventional residual degrees of freedom are $T-3$. Use the full regression for its standard errors, or preserve the full-model degrees of freedom and assumptions when calculating them from residualized data. This is an agent implication of the p. 18 degrees-of-freedom formula. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=18|Lecture 2, PDF p. 18]]

## Seasonality is a repeating calendar pattern

Monthly or quarterly data may have regular within-year differences. The source's example is retail sales tending to jump in the fourth quarter. Such a pattern differs from a trend: a trend describes systematic movement over time, whereas seasonality repeats with calendar position. It may be represented by seasonal dummy variables or removed before substantive regression by seasonal adjustment. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=30|Lecture 2, PDF p. 30]]

**Agent expansion of the seasonal-dummy method:** for quarterly data, include an intercept and three indicators, taking quarter 1 as reference:

$$
y_t=\beta_0+\beta_1x_t+\lambda_2Q_{2t}
+\lambda_3Q_{3t}+\lambda_4Q_{4t}+u_t.
$$

Here $Q_{jt}=1$ if date $t$ lies in quarter $j$, otherwise zero. Coefficient $\lambda_4$ is the fourth-quarter intercept difference relative to quarter 1, holding $x_t$ fixed. Including all four indicators alongside an intercept would make the intercept their exact sum and violate TS3. Likewise, a model with monthly indicators and an intercept uses eleven independent indicators and one reference month. These designs assume stable additive seasonal differences; writing them does not prove that this is the appropriate adjustment for every dataset. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=30|Lecture 2, PDF p. 30]]; [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=12|TS3, PDF p. 12]]

The textbook extends the same partialling-out logic to seasonality: regress the outcome and every substantive regressor on the same intercept and seasonal indicators, then regress their residuals on each other. Their slopes agree with the model that includes those seasonal indicators. A series may contain both a trend and seasonal pattern, so the residualization can include both sets of controls together. This is a simple regression-based adjustment, not a claim that it reproduces every statistical agency's seasonal-adjustment procedure. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Dump/textbook.pdf#page=401|Wooldridge, 5th ed., PDF p. 401 (printed p. 373)]]

The supplied lecture gives no numerical seasonal regression or seasonal-adjustment algorithm. It introduces the choice between explicit calendar controls and adjustment of the series before regression; it does not authorize inferring that a supplied series has already been adjusted. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=30|Lecture 2, PDF p. 30]]

## What the adjustments establish

Including a trend or consistently detrending variables changes the comparison from a raw association in levels to a relationship conditional on the chosen time pattern. Seasonal indicators similarly separate stable calendar differences. These are specification tools whose usefulness depends on the relevant time pattern being represented appropriately. They do not by themselves establish causal identification, strict exogeneity, or no serial correlation. The source's unprovided board examples remain unavailable; the algebra here is explicitly agent-created explanation of the uploaded methods. [[00_Materials/2026_2027/Winter_Semester/Econometrics_II/Week_2/2026_Lecture2_print.pdf#page=27|Lecture 2, PDF pp. 27–30]]
