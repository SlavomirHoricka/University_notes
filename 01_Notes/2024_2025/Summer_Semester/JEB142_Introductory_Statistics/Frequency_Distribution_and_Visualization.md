---
course: JEB142
topic: Frequency Distribution and Data Visualization
source: 00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_3_Descriptive_Statistics.pdf
tags: [JEB142, statistics, frequency-distribution, histogram, visualization, descriptive-statistics]
created: 2026-04-19
---
Parent: [[JEB142_Introductory_Statistics_main]]
Source: [[00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_3_Descriptive_Statistics.pdf]]
Related: [[Data_Types_and_Variables]], [[Scales_of_Measurement]], [[Measures_of_Central_Tendency]], [[Measures_of_Dispersion]]

# Frequency Distribution and Data Visualization

## Frequency Distribution

A **frequency distribution** summarises raw data by recording how often each value (or range of values) occurs.

### Absolute Frequency
The count $n_i$ of observations falling in class $i$.

### Relative Frequency
$$f_i = \frac{n_i}{n}$$
where $n = \sum_i n_i$ is the total number of observations. Relative frequencies sum to 1.

### Cumulative Frequency
The sum of absolute (or relative) frequencies up to and including class $i$:
$$F_i = \sum_{j \le i} n_j, \quad \text{or } \quad CF_i = \sum_{j \le i} f_j.$$

### Constructing Class Intervals (for continuous data)
1. Choose the number of classes $k$ (rule of thumb: $k \approx \sqrt{n}$ or $k = 1 + \lfloor \log_2 n \rfloor$).
2. Set class width $w = \frac{\max - \min}{k}$, rounding up for convenience.
3. Define non-overlapping, exhaustive intervals $[a_i, a_{i+1})$.

## Graphical Displays

### Histogram
- Bar chart where each bar spans one class interval and its **height equals the frequency** (or relative frequency, or frequency density).
- Bars touch — the horizontal axis is continuous.
- Reveals the **shape** of the distribution: symmetric, skewed right, skewed left, unimodal, bimodal.

### Ogive (Cumulative Frequency Curve)
- Plot of cumulative relative frequency $CF_i$ against the upper boundary of each class.
- Useful for reading off percentiles graphically.

### Stem-and-Leaf Plot
- Preserves individual data values while showing distribution shape.
- Useful for small-to-medium datasets.

### Box Plot (Box-and-Whisker)
- Displays five-number summary: minimum, $Q_1$, median ($Q_2$), $Q_3$, maximum.
- Whiskers extend to the most extreme non-outlier observation.
- Outliers (beyond $1.5 \times \text{IQR}$ from the box) are plotted individually.
- Particularly useful for comparing distributions across groups.

### Scatter Plot (Bivariate)
- Each observation plotted as a point $(x_i, y_i)$ in two-dimensional space.
- Reveals the direction and rough strength of the association between $x$ and $y$.
- Quadrant analysis: dividing at $(\bar{x}, \bar{y})$ identifies four quadrants (I: above-average both; II: above-average $y$, below-average $x$; III: below-average both; IV: above-average $x$, below-average $y$). This motivates the [[Measures_of_Association#Sample Covariance|sample covariance]].

## Relationship to Descriptive Statistics

Visual summaries are complementary to numerical summaries in [[Measures_of_Central_Tendency]] and [[Measures_of_Dispersion]]. A histogram answers "what shape does the distribution have?"; a box plot answers "where is the bulk of the data and how spread out is it?"
