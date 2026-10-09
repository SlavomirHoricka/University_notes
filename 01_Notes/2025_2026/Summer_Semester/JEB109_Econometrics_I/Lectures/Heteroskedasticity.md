---
course: "JEB109"
topic: "Heteroskedasticity"
source: "00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_10_JEB109_2026.pdf"
tags: [JEB109, econometrics, heteroskedasticity, WLS, FGLS, robust-standard-errors, Breusch-Pagan, White-test]
created: 2026-04-28
---

Parent: [[JEB109_Econometrics_I_main]]
Source: [[00_Materials/2025_2026/Summer_Semester/JEB109_Econometrics_I/Lectures/Lecture_10_JEB109_2026.pdf]]
Related: [[MLR_Assumptions_and_OLS_Unbiasedness]], [[Variance_of_OLS_Estimator]], [[Gauss_Markov_Theorem]], [[F_Test_and_Multiple_Restrictions]], [[Linear_Probability_Model]], [[OLS_Consistency_and_Asymptotics]]

---

# Heteroskedasticity

## Definition

**MLR.5 (Homoskedasticity):** The error $u$ has the same variance for any value of the independent variables:

$$\text{Var}(u \mid x_1, \ldots, x_k) = \sigma^2 \mathbf{I}$$

**Heteroskedasticity** is the violation of MLR.5: the error variance is observation-specific,

$$\text{Var}(u_i \mid \mathbf{X}) = \sigma_i^2,$$

so the variance changes systematically with the regressors (or with observation-level characteristics). Typical empirical examples: residual spread widening with income, firm size, or the level of a variable.

---

## Consequences for OLS

### What is preserved (MLR.1–4 sufficient)

1. **Unbiasedness**: $\mathbb{E}(\hat{\boldsymbol\beta}^{\text{OLS}}) = \boldsymbol\beta$ — coefficient estimates are correct on average.
2. **Consistency**: plim $\hat{\boldsymbol\beta}^{\text{OLS}} = \boldsymbol\beta$ — estimates converge to the truth.
3. **$R^2$ and $\bar{R}^2$** are unaffected as measures of fit.

### What breaks

4. **Efficiency**: OLS is **no longer BLUE** — it is not the minimum-variance linear unbiased estimator; WLS dominates (see §4).
5. **True variance of $\hat\beta_j$ increases**: because the heteroskedastic error explains more variation in $y$, OLS estimators are more dispersed than under homoskedasticity.
6. **Estimated variance of $\hat\beta_j$ is biased** (typically downward when $\sigma_i^2$ is positively correlated with $(x_{ij} - \bar{x}_j)^2$): OLS masks the higher dispersion by attributing error variation to the regressors.

**Critical implication:** standard $t$ statistics, $F$ statistics, confidence intervals, and LM statistics are **invalid even asymptotically**. Inference requires correction.

### Derivation of the heteroskedastic variance (SLR case)

For $y_i = \beta_0 + \beta_1 x_i + u_i$ with $\text{Var}(u_i \mid x_i) = \sigma_i^2$, using the OLS slope formula:

$$\hat\beta_1 = \beta_1 + \frac{\sum_{i=1}^n u_i (x_i - \bar{x})}{\sum_{i=1}^n (x_i - \bar{x})^2}$$

the true variance is:

$$\text{Var}(\hat\beta_1) = \frac{\sum_{i=1}^n \sigma_i^2 (x_i - \bar{x})^2}{\text{SST}_x^2}$$

which reduces to $\sigma^2 / \text{SST}_x$ only when all $\sigma_i^2 = \sigma^2$ (homoskedasticity).

---

## Heteroskedasticity-Robust Standard Errors (White / Huber-Eicker-White)

### Motivation

In the 1980s, **Halbert White** (building on Eicker 1963 and Huber 1967) derived an estimator of $\text{Var}(\hat\beta_j)$ that is asymptotically valid under any form of heteroskedasticity, requiring only MLR.1–MLR.4.

### Formula

For the SLR estimator, the robust variance estimator is:

$$\widehat{\text{Var}}(\hat\beta_1) = \frac{\sum_{i=1}^n \hat{u}_i^2 (x_i - \bar{x})^2}{\text{SST}_x^2}$$

For the general MLR case (the full "sandwich" formula):

$$\widehat{\text{Var}}(\hat\beta_j) = \frac{\sum_{i=1}^n \hat{u}_i^2 \hat{r}_{ij}^2}{\text{SSR}_j^2} = \frac{\sum_{i=1}^n \hat{u}_i^2 \hat{r}_{ij}^2}{\left[\text{SST}_j (1 - R_j^2)\right]^2}$$

where $\hat{r}_{ij}$ is the $i$th residual from regressing $x_j$ on all other independent variables (the "partialling-out" residual). The formula is called a **sandwich estimator** because $(\mathbf{X}'\mathbf{X})^{-1}$ surrounds a central matrix built from squared residuals.

The square root is the **heteroskedasticity-robust standard error** (also: White SE, Huber-White SE, robust SE).

### Properties

- **Asymptotically valid** for any heteroskedasticity form under MLR.1–MLR.4.
- Recommended when degrees of freedom $n - k - 1 \geq 120$ (large samples).
- In practice, robust SEs are typically **larger** than standard OLS SEs.
- $t$ statistics and confidence intervals constructed from robust SEs are asymptotically valid **without MLR.5–MLR.6**.
- Under the full CLM (MLR.1–6), standard OLS SEs yield exact finite-sample $t_{n-k-1}$ distributions — robust SEs are only approximate and do not dominate in small samples.

---

## Heteroskedasticity-Robust LM Test

The standard LM test statistic ($n R^2_{\tilde u}$) is also invalid under heteroskedasticity. A heteroskedasticity-robust version of the LM test for $q$ exclusion restrictions follows these steps:

1. **Estimate the restricted model** and save residuals $\tilde{u}$.
2. **Partial out**: for each of the $q$ excluded variables, regress it on all included variables; save $q$ sets of residuals $(\tilde{r}_1, \ldots, \tilde{r}_q)$.
3. **Construct interaction products**: form $\tilde{u}\tilde{r}_j$ for $j = 1, \ldots, q$.
4. **Auxiliary regression**: regress the constant **1** on $\tilde{u}\tilde{r}_1, \ldots, \tilde{u}\tilde{r}_q$ **without an intercept**; obtain $\text{SSR}_1$.
5. **Test statistic**:

$$\text{LM} = n - \text{SSR}_1 \overset{a}{\sim} \chi^2_q \quad \text{under } H_0$$

This procedure yields a test that is valid under heteroskedasticity of unknown form.

---

## Testing for Heteroskedasticity

Before applying robust SEs or GLS, it is good practice to formally test whether MLR.5 is violated. Both tests below assume MLR.1–MLR.4 hold.

### Breusch-Pagan (B-P) Test

**Idea:** if MLR.5 holds, the squared OLS residuals $\hat{u}^2$ should have no systematic linear relationship with the regressors.

**Procedure:**
1. Estimate OLS; save residuals $\hat{u}$.
2. Run the **auxiliary regression**:
   $$\hat{u}^2 = \delta_0 + \delta_1 x_1 + \cdots + \delta_k x_k + v \tag{1}$$
3. Test $H_0: \delta_1 = 0, \ldots, \delta_k = 0$ using either the $F$ statistic from (1) or the LM statistic $n R^2_{(1)} \overset{a}{\sim} \chi^2_k$.

Note: $\hat{u}^2$ cannot be normally distributed, so the exact $F$ distribution is unavailable; the test has asymptotic justification.

### White Test

**Idea:** heteroskedasticity may depend on squared regressors and cross-products, not only linear terms.

**Full White auxiliary regression** (for $k = 2$):

$$\hat{u}^2 = \delta_0 + \delta_1 x_1 + \delta_2 x_2 + \delta_3 x_1^2 + \delta_4 x_2^2 + \delta_5 x_1 x_2 + v$$

The number of parameters grows as $O(k^2)$, so an **adjusted White test** replaces all regressors with fitted values:

$$\hat{u}^2 = \delta_0 + \delta_1 \hat{y} + \delta_2 \hat{y}^2 + v$$

$H_0: \delta_1 = 0, \delta_2 = 0$ — the LM statistic $n R^2 \overset{a}{\sim} \chi^2_2$.

The B-P test is a special case of the White test (linear terms only). The White test is more general but uses more degrees of freedom.

---

## Weighted Least Squares (WLS)

### Motivation

WLS is older than robust SEs. When the **form** of heteroskedasticity is known — $\text{Var}(u \mid \mathbf{X}) = \sigma^2 h(\mathbf{X})$ — WLS exploits this knowledge to produce **BLUE** estimates under MLR.1–MLR.4. Robust SEs merely correct inference after OLS; WLS improves the estimates themselves.

### Transformed model

Divide every term in the population model by $\sqrt{h_i}$:

$$\frac{y_i}{\sqrt{h_i}} = \frac{\beta_0}{\sqrt{h_i}} + \beta_1 \frac{x_{i1}}{\sqrt{h_i}} + \cdots + \beta_k \frac{x_{ik}}{\sqrt{h_i}} + \frac{u_i}{\sqrt{h_i}}$$

or equivalently $y_i^* = \beta_0 x_{i0}^* + \beta_1 x_{i1}^* + \cdots + \beta_k x_{ik}^* + u_i^*$, where $x_{i0}^* = 1/\sqrt{h_i}$ (so there is no constant in the transformed model).

The transformed error satisfies:

$$\text{Var}\!\left(\frac{u_i}{\sqrt{h_i}}\right) = \frac{\mathbb{E}(u_i^2)}{h_i} = \frac{\sigma^2 h_i}{h_i} = \sigma^2$$

The transformed model satisfies MLR.1–MLR.5, so OLS on the transformed model is BLUE. In practice this means each observation is weighted by $1/\sqrt{h_i}$, giving **less weight** to observations with higher variance.

### Interpretation

The $\hat\beta_j$ from WLS are interpreted with respect to the **original** (untransformed) model. $R^2$ and $t$/$F$ statistics from the transformed model are valid for inference.

### LPM as a known heteroskedasticity example

For the [[Linear_Probability_Model]], $h_i = p(\mathbf{X}_i)(1 - p(\mathbf{X}_i))$ is known up to the parameters. Estimate $\hat{h}_i = \hat{y}_i(1-\hat{y}_i)$ from OLS fitted values, then apply WLS. Robust SEs are still recommended on top of WLS because $\hat{h}_i$ is an estimate, not the true weight.

---

## Feasible GLS (FGLS)

When $h(\mathbf{X})$ is **unknown**, it must be estimated from the data.

### Parametric form of $h$

Assume:

$$\text{Var}(u \mid \mathbf{X}) = \sigma^2 h(\mathbf{X}) = \sigma^2 \exp(\delta_0 + \delta_1 x_1 + \cdots + \delta_k x_k)$$

The exponential form guarantees $h > 0$ for all parameter values.

### Estimation procedure

1. Run OLS; compute $\hat{u}^2$.
2. Run the log-linear auxiliary regression:
   $$\log(\hat{u}^2) = a_0 + \delta_1 x_1 + \cdots + \delta_k x_k + e$$
3. Obtain fitted values $\widehat{\log(\hat{u}^2)}$ and transform:
   $$\hat{h}_i = \exp\!\left(\widehat{\log(\hat{u}^2_i)}\right)$$
4. Apply WLS with weights $1/\sqrt{\hat{h}_i}$.

The functional form inside the exponential can be adjusted freely (analogously to the White test). FGLS is also called **estimated GLS (EGLS)**.

---

## WLS vs. FGLS: Comparison

| | WLS (known $h$) | FGLS (unknown $h$) |
|---|---|---|
| $h_i$ | Known exactly | Estimated |
| Efficiency | **BLUE** under MLR.1–4 | Consistent + asymptotically efficient (better than OLS for large $n$) |
| Finite sample | Valid | **Biased** (requires large $n$) |
| Wrong $h$ form | Consistent but SEs invalid | Same |
| With robust SEs | Fixes wrong-$h$ SEs | Recommended (need large $n$ anyway) |

If the specified $h$ is wrong, WLS is still **consistent** under MLR.1–4, but its standard errors are no longer valid; combining WLS with heteroskedasticity-robust SEs solves this.

---

## Predictions Under Heteroskedasticity

- **Point prediction** from OLS remains unbiased and consistent; from WLS/FGLS it is consistent.
- **Individual prediction interval** must account for the heteroskedastic error variance at $\mathbf{X}^0$:

$$\text{se}(\hat{e}^0) = \sqrt{\hat\sigma^2 \, h(\mathbf{X}^0) + \text{Var}(\hat{y}^0)}$$

where WLS/FGLS replaces OLS in computing $\hat\sigma^2$ and $\text{Var}(\hat{y}^0)$.

---

## Practical Decision Guide

1. **Inspect residual plots** — does spread increase or decrease with $\hat{y}$ or a regressor?
2. **Formally test** with B-P and/or White tests.
3. **If homoskedastic**: proceed with standard OLS inference (exact under MLR.6; asymptotically valid without it).
4. **If heteroskedastic**:
   - *Form known?* → **WLS** (BLUE, valid for small and large samples). Check with Hausman test if specification is uncertain.
   - *Form unknown?* → **FGLS** (asymptotically efficient, needs large $n$); support with robust SEs.
   - *Default safe option*: apply **robust standard errors** to OLS — valid asymptotically for any heteroskedasticity form with $n - k - 1 \geq 120$.
