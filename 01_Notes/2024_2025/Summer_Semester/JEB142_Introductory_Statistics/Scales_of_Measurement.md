---
course: JEB142
topic: Scales of Measurement
source: 00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_3_Descriptive_Statistics.pdf
tags: [JEB142, statistics, measurement-scales, nominal, ordinal, interval, ratio]
created: 2026-04-19
---
Parent: [[JEB142_Introductory_Statistics_main]]
Source: [[00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_3_Descriptive_Statistics.pdf]]
Related: [[Data_Types_and_Variables]], [[Measures_of_Central_Tendency]], [[Measures_of_Dispersion]]

# Scales of Measurement

## Overview

The scale of measurement of a variable determines which mathematical operations are meaningful and, consequently, which statistical summaries may be computed. There are four scales in ascending order of information content: **nominal → ordinal → interval → ratio**.

## The Four Scales

### 1. Nominal Scale
- Observations are assigned to mutually exclusive, unordered **categories** (labels).
- No meaningful ordering, no differences, no ratios.
- *Examples:* gender, nationality, brand preference, occupation.
- **Permissible statistics:** mode only; frequency counts and relative frequencies.

### 2. Ordinal Scale
- Categories have a **natural ordering**, but the gaps between adjacent categories are not necessarily equal and are not quantifiable.
- Differences and ratios of category codes are meaningless.
- *Examples:* Likert-scale survey responses (strongly agree, agree, …), academic grades (A, B, C, …), finishing position in a race.
- **Permissible statistics:** mode, median, percentiles, interquartile range.

### 3. Interval Scale
- Numerical values where **differences** are meaningful and constant, but **there is no absolute zero** (zero is an arbitrary reference point).
- Ratios are not interpretable.
- *Examples:* temperature in °C or °F, calendar year, IQ scores.
- **Permissible statistics:** mode, median, mean, range, standard deviation; ratios of values are not valid.

### 4. Ratio Scale
- Numerical values with **meaningful differences, a true absolute zero**, and **meaningful ratios**.
- All arithmetic operations are valid.
- *Examples:* annual salary, distance, mass, age, number of items.
- **Permissible statistics:** all statistical measures — mode, median, mean, range, variance, standard deviation, coefficient of variation, geometric mean.

## Summary Table

| Scale | Order | Equal intervals | True zero | Permissible measures |
|-------|-------|-----------------|-----------|----------------------|
| Nominal | No | No | No | Mode |
| Ordinal | Yes | No | No | Mode, Median, IQR |
| Interval | Yes | Yes | No | Mode, Median, Mean, SD, Range |
| Ratio | Yes | Yes | Yes | All measures |

## Why the Scale Matters

Applying an inappropriate statistic to a lower-scale variable produces results that are at best uninterpretable and at worst misleading. For instance, computing the mean of an ordinal variable (e.g., averaging letter grades as numbers) implicitly assumes equal spacing between categories — an assumption the ordinal scale does not support.

See [[Measures_of_Central_Tendency]] and [[Measures_of_Dispersion]] for a discussion of how each measure fits within this hierarchy.
