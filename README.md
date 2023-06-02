# Description

Descriptive Statistics is a wide range topic in the world of Statistics

Especially when we encounter with High-Volume data, It would be better to come up with summarized version of it.

# Constraints:

- Features(Attributes/Columns): Needs to be of Integer/Float datatype

# Functionalities

- Measures of Central Tendency
  - Mean
  - Median
  - Mode
- Measures of Dispersion
  - Range
  - Quartiles
    - Q1
    - Q2
    - Q3
    - Adjusted Q1
    - Adjusted Q2
  - Outliers
    - Z-Score method
    - IQR method
  - Variance
  - Standard Deviation
  - Coefficient of Variation
- Measures of Symmetry
  - Skew
    - Left Skew
    - Right Skew
    - Symmetric
  - Kurtosis
    - Leptokurtic
    - Mesokurtic
    - Platykurtic
- Measures of Association
  - Covariance
  - Correlation
- Normal Distribution (Empirical Rule)
  - P68
  - P95
  - P97
- Multicollinearity
  - VIF (Variance Inflation Factor)
- Misc
  - Minimum
  - Maximum
  - Sum
  - Count
  - Missing

# Output

<img src='./snaps/Desc_stats.png'>

# How to import

    pip install desc_stats

# How to Use

    from desc_stats import desc_stats

    desc_stats(df, features)

# Contribute

    pip install -e .[dev]
