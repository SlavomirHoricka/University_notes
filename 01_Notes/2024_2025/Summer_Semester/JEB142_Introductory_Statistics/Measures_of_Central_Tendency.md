---
course: JEB142
topic: Measures of Central Tendency
source: 00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_3_Descriptive_Statistics.pdf
tags: [JEB142, statistics, mean, median, mode, central-tendency, descriptive-statistics]
created: 2026-04-19
---
Parent: [[JEB142_Introductory_Statistics_main]]
Source: [[00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_3_Descriptive_Statistics.pdf]]
Related: [[Scales_of_Measurement]], [[Measures_of_Dispersion]], [[Measures_of_Association]], [[Frequency_Distribution_and_Visualization]]

# Measures of Central Tendency

Measures of central tendency locate the "centre" of a distribution. Which measure is appropriate depends on the [[Scales_of_Measurement]] of the variable.

## 1. Mode

The **mode** is the value (or class) that occurs most frequently.

- Applicable to **all** measurement scales (the only central tendency measure valid for nominal data).
- A distribution may be **unimodal**, **bimodal**, or **multimodal**.
- For grouped data, the **modal class** is the class with the highest frequency.

## 2. Median

The **median** $\tilde{x}$ is the middle value when data are sorted in ascending order.

For $n$ observations sorted as $x_{(1)} \le x_{(2)} \le \dots \le x_{(n)}$:

$$\tilde{x} = \begin{cases} x_{(m+1)} & \text{if } n = 2m+1 \text{ (odd)} \\ \dfrac{x_{(m)} + x_{(m+1)}}{2} & \text{if } n = 2m \text{ (even)} \end{cases}$$

- Valid for **ordinal, interval, and ratio** scales.
- **Robust to outliers**: extreme values do not affect the median.
- The median is the 50th percentile ($Q_2$).

## 3. (Arithmetic) Mean

The **sample mean** $\bar{x}$ is the arithmetic average:

$$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$$

- Valid only for **interval and ratio** scales (requires meaningful differences).
- **Not robust**: a single extreme observation can shift $\bar{x}$ substantially.
- **Algebraically tractable**: the mean is the unique value $c$ that minimises $\sum (x_i - c)^2$.

### Weighted Mean
When observations carry different weights $w_i > 0$:

$$\bar{x}_w = \frac{\sum_{i=1}^{n} w_i x_i}{\sum_{i=1}^{n} w_i}$$

Useful for grouped frequency tables where $w_i = n_i$ (class frequency) and $x_i$ is the class midpoint.

## Comparing Mean and Median: Skewness

| Distribution shape | Relationship |
|-------------------|--------------|
| Symmetric | $\bar{x} \approx \tilde{x} \approx \text{mode}$ |
| Right-skewed (long right tail) | $\text{mode} < \tilde{x} < \bar{x}$ |
| Left-skewed (long left tail) | $\bar{x} < \tilde{x} < \text{mode}$ |

In income distributions (typically right-skewed), the median is preferred as a summary of "typical" income because the mean is pulled upward by high earners.

## Percentiles and Quartiles

The **$p$-th percentile** $L_p$ is the value below which $p\%$ of observations fall.

$$L_p = \frac{p}{100}(n+1)\text{-th ordered value}$$

(with linear interpolation if this is not an integer).

The **quartiles** divide the data into four equal parts:
- $Q_1 = L_{25}$ (lower quartile / 25th percentile)
- $Q_2 = L_{50}$ (median)
- $Q_3 = L_{75}$ (upper quartile / 75th percentile)

Quartiles feed directly into the [[Measures_of_Dispersion#Interquartile Range|interquartile range]] and the box plot in [[Frequency_Distribution_and_Visualization]].
