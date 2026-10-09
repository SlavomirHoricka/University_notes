---
course: JEB142
topic: Data Types and Variables
source: 00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_2_Data_and_Statistics.pdf
tags: [JEB142, statistics, data-types, variables, measurement]
created: 2026-04-19
---
Parent: [[JEB142_Introductory_Statistics_main]]
Source: [[00_Materials/2024_2025/Summer_Semester/JEB142_Introductory_Statistics/Introductory_Statistics_2025_2_Data_and_Statistics.pdf]]
Related: [[Scales_of_Measurement]], [[Descriptive_Statistics_Overview]], [[Frequency_Distribution_and_Visualization]]

# Data Types and Variables

## Definition

A **variable** is any characteristic that can take different values across observations. Variables are classified first by whether they are **quantitative** or **qualitative**, and then further by their [[Scales_of_Measurement]].

## Classification of Variables

### Quantitative Variables
Quantitative variables take numerical values for which arithmetic operations are meaningful.

- **Interval variables**: values have meaningful differences but no true zero point. Ratios of values are not interpretable.
  - *Example:* Temperature in °C — the difference between 20°C and 10°C is 10°C, but 20°C is not "twice as hot" as 10°C.
- **Ratio variables**: values have meaningful differences **and** a true absolute zero. All arithmetic operations are valid.
  - *Example:* Annual salary, weight, number of children.

### Qualitative (Categorical) Variables
Qualitative variables record categories or labels, not numerical magnitudes.

- **Nominal variables**: categories with no natural ordering.
  - *Example:* Occupation (teacher, doctor, engineer), marital status, eye colour.
- **Ordinal variables**: categories with a natural ordering, but differences between categories are not quantifiable.
  - *Example:* Education level (primary < secondary < tertiary), survey responses (agree, neutral, disagree).

## Types of Data by Structure

| Type | Description | Example |
|------|-------------|---------|
| **Cross-sectional** | Multiple subjects observed at a single point in time | GDP per capita for 50 countries in 2024 |
| **Time series** | Single subject observed across multiple time periods | CPI monthly 2000–2024 |
| **Panel (longitudinal)** | Multiple subjects observed across multiple time periods | Eurostat country data 2000–2024 |

## Sources of Data

- **Existing data**: administrative records, published datasets, surveys already conducted — cheapest but may not fit the research question exactly.
- **Experimental studies**: researcher randomly assigns subjects to treatments; causal inference is possible.
- **Observational studies**: researcher observes without intervention; association can be established but causal claims require caution.

## Implications for Analysis

The type of variable determines which statistical operations are valid. See [[Scales_of_Measurement]] for a full table of permissible operations by measurement level. In particular:
- Only **ratio** variables support all standard descriptive statistics.
- **Ordinal** data support median and mode but **not** the arithmetic mean.
- **Nominal** data support only the mode among measures of central tendency.
