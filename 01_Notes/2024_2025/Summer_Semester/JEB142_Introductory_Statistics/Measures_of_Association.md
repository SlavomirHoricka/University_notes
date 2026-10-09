---
course: JEB142
topic: Measures of Association
source: 00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_3_Descriptive_Statistics.pdf
tags: [JEB142, statistics, covariance, correlation, association, descriptive-statistics]
created: 2026-04-19
---
Parent: [[JEB142_Introductory_Statistics_main]]
Source: [[00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_3_Descriptive_Statistics.pdf]]
Related: [[Measures_of_Central_Tendency]], [[Measures_of_Dispersion]], [[Frequency_Distribution_and_Visualization]], [[Scales_of_Measurement]]

# Measures of Association

Measures of association quantify the **strength and direction of the linear relationship** between two variables. The two principal measures — sample covariance and sample correlation coefficient — extend the univariate descriptive framework to the bivariate case.

## Sample Covariance

### Definition

$$s_{xy} = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})$$

### Interpretation

- **Positive** $s_{xy} > 0$: $x$ and $y$ tend to move in the **same direction** — observations above $\bar{x}$ tend to be paired with observations above $\bar{y}$ (quadrants I and III of the scatter plot dominate).
- **Negative** $s_{xy} < 0$: $x$ and $y$ tend to move in **opposite directions** (quadrants II and IV dominate).
- $s_{xy} = 0$: no linear association detectable in the sample.

### Limitation

The magnitude of $s_{xy}$ depends on the **units of measurement** of $x$ and $y$. It is therefore not directly comparable across different variable pairs, motivating the standardised version below.

### Example (Stereo Store)
For number of TV commercials ($x$) and sales volume in \$10,000s ($y$), the sample covariance $s_{xy} = 11$, indicating a positive linear relationship.

## Sample Correlation Coefficient (Pearson)

### Definition

$$r_{xy} = \frac{s_{xy}}{s_x \, s_y}$$

where $s_x$ and $s_y$ are the sample standard deviations of $x$ and $y$ respectively.

### Derivation

Dividing by $s_x s_y$ standardises the covariance so that the result is **dimensionless**:

$$r_{xy} = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^n (x_i - \bar{x})^2} \cdot \sqrt{\sum_{i=1}^n (y_i - \bar{y})^2}}$$

### Properties

1. $r_{xy} \in [-1, 1]$ always.
2. $r_{xy} = +1$: perfect positive linear relationship (all points on a line with positive slope).
3. $r_{xy} = -1$: perfect negative linear relationship.
4. $r_{xy} = 0$: no **linear** association (nonlinear association may still exist).
5. $r_{xy} = r_{yx}$ (symmetry).
6. $r_{xy}$ is invariant to linear transformations of $x$ or $y$ (e.g., changing units does not change $r$).

### Interpretation

| $|r_{xy}|$ | Informal label |
|------------|---------------|
| 0.00–0.19 | Negligible |
| 0.20–0.39 | Weak |
| 0.40–0.59 | Moderate |
| 0.60–0.79 | Strong |
| 0.80–1.00 | Very strong |

### Example (Stereo Store cont.)
With $s_{xy} = 11$, $s_x \approx 1.549$, $s_y \approx 7.681$:

$$r_{xy} = \frac{11}{1.549 \times 7.681} \approx 0.93$$

A value of $0.93$ indicates a very strong positive linear relationship between advertising frequency and sales.

## Scale Requirements

Both $s_{xy}$ and $r_{xy}$ require variables on at least an **interval scale** (so that differences $x_i - \bar{x}$ and $y_i - \bar{y}$ are meaningful). For ordinal data, **Spearman's rank correlation** is the appropriate alternative (covered in JEB105).

## Caution: Correlation ≠ Causation

A large $|r_{xy}|$ indicates linear co-movement but does not establish that $x$ causes $y$. Confounders, reverse causality, or spurious correlation may all produce a high $r_{xy}$ without any causal mechanism. Causal inference requires experimental design or econometric methods (see [[JEB109_Econometrics_I_main]]).
