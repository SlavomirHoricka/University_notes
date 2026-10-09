---
course: JEB105
topic: "Least Squares Estimation"
source: "00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_08_Point_Estimation.pdf"
tags: [JEB105, statistics, least-squares, LSE, regression, estimation]
created: 2026-04-19
---

Parent: [[JEB105_Statistics_main]]
Source: [[00_Materials/2025_2026/Winter_Semester/JEB105_Statistics/Statistics_2025_08_Point_Estimation.pdf]]
Related: [[Point_Estimation]], [[Maximum_Likelihood_Estimation]], [[Method_of_Moments]], [[Expected_Value]]

---

## Least Squares Estimation

### Setup

The least squares framework allows a slightly different data structure from the i.i.d. assumption. We observe pairs $(u_i, Y_{ij})$ where:
- $U$ is an independent variable with observed values $u_1, \ldots, u_k$.
- $Y_{ij}$ is the $j$-th observation of the dependent variable $Y$ at value $u_i$.
- The relationship between $Y$ and $U$ is:

$$Y = Q(u) + \varepsilon,$$

where $Q(u)$ is the **regression function** of $Y$ on $U$, and $\varepsilon$ is a random error with $E[\varepsilon] = 0$ and $\text{Var}(\varepsilon) = \sigma^2$.

### Parametric Regression

In the parametric case, $Q(u) = \varphi(u; \theta_1, \ldots, \theta_r)$ for some known function $\varphi$ and unknown parameters $\theta_1, \ldots, \theta_r$.

**Linear regression model:** When $Q(u) = \alpha + \beta u$, we have the classical simple linear regression.

### The Least Squares Criterion

The **least squares estimates** $\hat{\theta}_1, \ldots, \hat{\theta}_r$ minimise:

$$S(\theta_1, \ldots, \theta_r) = \sum_{i=1}^k \sum_{j=1}^{n_i} (y_{ij} - \varphi(u_i; \theta_1, \ldots, \theta_r))^2,$$

where $y_{ij}$ is the $j$-th observation of $Y$ for the value $u_i$.

The minimisation is done by solving the **normal equations**:

$$\frac{\partial S}{\partial \theta_i} = 0, \quad i = 1, \ldots, r.$$

### Connection to MLE

Under the assumption $\varepsilon \sim N(0, \sigma^2)$, the LSE coincides with the MLE:

$$L(\theta; y) = \prod_{i,j} \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(y_{ij} - \varphi(u_i,\theta))^2}{2\sigma^2}\right).$$

Maximising $L$ is equivalent to minimising $S(\theta)$. Hence, under normality of errors, the least squares estimator and the MLE are identical.

### Simple Linear Regression

For the linear model $Q(u) = \alpha + \beta u$ with pairs $(u_i, Y_i)$, the normal equations give the closed-form solutions:

$$\hat{\beta} = \frac{\sum_{i=1}^n (u_i - \bar{u})(Y_i - \bar{Y})}{\sum_{i=1}^n (u_i - \bar{u})^2}, \qquad \hat{\alpha} = \bar{Y} - \hat{\beta}\bar{u}.$$

These are also the formulas for the [[Covariance_and_Correlation]]-based regression coefficient.

### Interpretation

The least squares method seeks the parameter values that minimise the total squared deviation of observed responses from their fitted values. This geometric interpretation — finding the projection of $Y$ onto the column space of the design matrix — generalises naturally to multiple regression.

The equivalence to MLE under normal errors explains why least squares estimators inherit the optimality properties of MLEs in the linear regression context (e.g., the Gauss-Markov theorem states that OLS estimators are BLUE — Best Linear Unbiased Estimators — even without normality).

In the JEB105 context, least squares connects statistical estimation to the econometric methods developed in [[JEB109_Econometrics_I_main]].
