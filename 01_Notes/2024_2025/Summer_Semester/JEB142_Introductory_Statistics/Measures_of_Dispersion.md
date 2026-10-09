---
course: JEB142
topic: Measures of Dispersion
source: 00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_3_Descriptive_Statistics.pdf
tags: [JEB142, statistics, variance, standard-deviation, IQR, dispersion, descriptive-statistics]
created: 2026-04-19
---
Parent: [[JEB142_Introductory_Statistics_main]]
Source: [[00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_3_Descriptive_Statistics.pdf]]
Related: [[Measures_of_Central_Tendency]], [[Scales_of_Measurement]], [[Measures_of_Association]]

# Measures of Dispersion

Measures of dispersion quantify the **spread** of a distribution around its centre. The appropriate choice depends on the [[Scales_of_Measurement]] and whether robustness to outliers is required.

## 1. Range

$$\text{Range} = x_{\max} - x_{\min}$$

- Simplest measure; uses only two observations.
- Highly sensitive to outliers.
- Valid for **interval and ratio** scales.

## 2. Interquartile Range (IQR)

$$\text{IQR} = Q_3 - Q_1$$

- Measures the spread of the middle 50% of the data.
- **Robust to outliers** — unaffected by values outside the central half.
- Valid for **ordinal, interval, and ratio** scales.
- Forms the basis of the box plot (see [[Frequency_Distribution_and_Visualization]]).

## 3. Sample Variance

$$s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2$$

### Assumptions
- Variable must be at **interval or ratio** scale (differences must be meaningful).

### Derivation / Interpretation
Each term $(x_i - \bar{x})^2$ is the squared deviation of observation $i$ from the sample mean. Dividing by $n-1$ (not $n$) gives an **unbiased estimator** of the population variance $\sigma^2$: the divisor $n-1$ is the **degrees of freedom** — one degree of freedom is lost because $\bar{x}$ is estimated from the same data.

$$s^2 = \frac{1}{n-1}\left(\sum_{i=1}^n x_i^2 - n\bar{x}^2\right)$$

- Units: square of the original unit (e.g., $\text{USD}^2$).

## 4. Sample Standard Deviation

$$s = \sqrt{s^2} = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}$$

- Same units as the original variable — directly comparable to the mean.
- Most commonly reported measure of spread for ratio/interval data.
- Not robust: dominated by large deviations due to squaring.

## 5. Coefficient of Variation (CV)

$$CV = \frac{s}{\bar{x}} \times 100\%$$

- **Dimensionless**: allows comparison of spread across variables measured in different units or with very different means.
- Valid only for **ratio** scale (requires a meaningful zero so that the mean is positive and meaningful).
- *Example:* If salaries have $s = \$3{,}000$ and $\bar{x} = \$50{,}000$, then $CV = 6\%$.

## Summary: Scale vs. Permissible Dispersion Measure

| Scale | Range | IQR | Variance / SD | CV |
|-------|-------|-----|---------------|----|
| Nominal | No | No | No | No |
| Ordinal | No | Yes | No | No |
| Interval | Yes | Yes | Yes | No |
| Ratio | Yes | Yes | Yes | Yes |

## Relationship Between Measures

The standard deviation and IQR are related through the distribution's shape. For a perfectly normal distribution:
$$\text{IQR} \approx 1.35 \, s$$

This relationship is exploited in robust scale estimators and in detecting outliers via the **$1.5 \times \text{IQR}$** rule used in box plots.
