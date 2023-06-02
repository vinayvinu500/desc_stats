# =============================== Libraries ====================================#
# Data Analysis 
import numpy as np
import pandas as pd

# Statistical Analysis
from scipy.stats import zscore
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Unwanted Character list
def char(s):
    """Function to check if a string contains special characters or not."""
    charlist = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '[', ']', '{', '}', '\\', '|',
                ';', ':', "'", '"', ',', '.', '<', '>', '/', '?']  # '_'
    counts = len([i for i in s if i in charlist])  # counts of unwanted symbols in the input string (s)
    return np.nan if counts == 0 else counts

# Descriptive Statistics
def desc_stats(df, *features):
    """
    Input:
    df : dataframe
    features : list of features or single feature

    Output:
    Mean, Median, Mode, Variance, Std_Dev, Coef_Var, Minimum, Maximum, Range, Q1, Q2, Q3, IQR, Adjusted_Q1, Adjusted_Q3, z_score_outliers, iqr_outliers, Skew, Left_Skewed, Right_Skewed, Symmetric, Kurtosis, Leptokurtic, Platykurtic, Mesokurtic, P68, P95, P99, VIF, Covariance, Correlation, Sum, Count, Missing, Unique, Symbols.

    Bugs (Handled):
    1. If feature is not numeric
    2. If features are one or more

    Benchmarks:
    One Feature: 3.23 s ± 214 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    Two or More Features: 4.37 s ± 427 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
    """

    # Features need to be numeric datatype
    if features is None:
        features = df.select_dtypes(include=['int64', 'float64']).columns.to_list()
    else:
        features = features[0] if len(features) == 1 else features
        features = [features] if type(features) == str else features
        features = [i for i in features if type(i) in (int, float)]


    # Measures of Central Tendency
    Mean = df[features].mean()
    Median = df[features].median()
    Mode = df[features].mode().iloc[0]

    # Measures of Dispersion
    Minimum = df[features].min()
    Maximum = df[features].max()
    Range = Maximum - Minimum
    Variance = df[features].var()
    Std_Dev = df[features].std()
    Coef_Var = Std_Dev / Mean

    # Quartiles
    Q1 = df[features].quantile(0.25)
    Q2 = df[features].quantile(0.50)
    Q3 = df[features].quantile(0.75)
    IQR = Q3 - Q1
    Adjusted_Q1 = Q1 - 1.5 * IQR
    Adjusted_Q3 = Q3 + 1.5 * IQR

    # Outliers
    z_score_outliers = df[features][(np.abs(zscore(df[features])) > 3.0)].dropna()
    iqr_outliers = df[df[features] < Adjusted_Q1].append(df[df[features] > Adjusted_Q3])  # more accurate in iqr

    # Measures of Symmetry
    Skew = df[
        features].skew()  # , np.array(list(map(lambda x: (x[0]-x[1])/x[2], zip(Mean, Variance, Std_Dev))))  # skew is accurate
    Left_Skewed = np.nan if len(Skew[Skew < 0]) == 0 else Skew[Skew < 0]
    Right_Skewed = np.nan if len(Skew[Skew > 0]) == 0 else Skew[Skew > 0]
    Symmetric = np.nan if len(Skew[Skew == 0]) == 0 else Skew[
        np.round(Skew) == 0]  # pd.Series(dict(list(Skew[np.round(Skew) == 0])))

    Kurtosis = df[features].kurtosis()
    Leptokurtic = np.nan if len(Kurtosis[Kurtosis > 0]) == 0 else Kurtosis[Kurtosis > 0]
    Platykurtic = np.nan if len(Kurtosis[Kurtosis < 0]) == 0 else Kurtosis[Kurtosis < 0]
    Mesokurtic = np.nan if len(Kurtosis[Kurtosis == 0]) == 0 else Kurtosis[Kurtosis == 0]

    # Miscellaneous
    Sum = df[features].sum()
    Count = df[features].count()
    Missing = (df[features].isna().sum())
    Symbols = df[features].apply(lambda x: char(x))
    Unique = df[features].nunique()

    # Normality of the data # mean = 0, std = 1
    Normal_dist = df[features].apply(zscore)
    P68 = Normal_dist[(Normal_dist[features] > (Normal_dist[features].mean() - 1 * Normal_dist[features].std()))
                      & (Normal_dist[features] < (Normal_dist[features].mean() + 1 * Normal_dist[
        features].std()))]  # one standard_deviation away from the mean (x-s, x+s)
    P95 = Normal_dist[(Normal_dist[features] > (Normal_dist[features].mean() - 2 * Normal_dist[features].std()))
                      & (Normal_dist[features] < (Normal_dist[features].mean() + 2 * Normal_dist[
        features].std()))]  # two standard_deviation away from the mean (x-2*s, x+2*s)
    P99 = Normal_dist[(Normal_dist[features] > (Normal_dist[features].mean() - 3 * Normal_dist[features].std()))
                      & (Normal_dist[features] < (Normal_dist[features].mean() + 3 * Normal_dist[
        features].std()))]  # three standard_deviation away from the mean (x-3*s, x+3*s)

    # Measures of Association
    Covariance = {i: pd.Series(j).index[0] for i, j in df[features].cov().items()} if len(features) <= 1 else {
        i: pd.Series(j).sort_values(ascending=False).iloc[[2]].index[0] for i, j in
        df.cov().to_dict().items()}  # second highest
    Correlation = {i: pd.Series(j).index[0] for i, j in df[features].cov().items()} if len(features) <= 1 else {
        i: pd.Series(j).sort_values(ascending=False).iloc[[2]].index[0] for i, j in
        df.corr().to_dict().items()}  # second highest

    # Multi-Collinearity (VIF)
    VIF = np.nan if len(features) <= 1 else pd.Series(
        [variance_inflation_factor(df[features].values, i) for i in range(df[features].shape[1])],
        index=df[features].columns)

    # =============================== Dataframe ====================================#
    # Descriptive Statistics
    stats = pd.DataFrame(data={'Mean': Mean,
                                    'Median': Median,
                                    'Mode': Mode,
                                    'Variance': Variance,
                                    'Std': Std_Dev,
                                    'Coef_Var': Coef_Var,
                                    'Min': Minimum,
                                    'Max': Maximum,
                                    'Range': Range,
                                    'Q1': Q1,
                                    'Q2': Q2,
                                    'Q3': Q3,
                                    'IQR': IQR,
                                    'Adjusted_Q1': Adjusted_Q1,
                                    'Adjusted_Q3': Adjusted_Q3,
                                    'Outliers (IQR)': pd.Series(
                                        data=[len(iqr_outliers[i].dropna().unique()) for i in features],
                                        index=features),
                                    'Outliers (Z-Score)': pd.Series(
                                        data=[len(z_score_outliers[i].dropna().unique()) for i in features],
                                        index=features),
                                    'Sum': Sum,
                                    'Count': Count,
                                    'Unique': Unique,
                                    'Missing': Missing,
                                    'Symbols': Symbols,
                                    'Skewness': Skew,
                                    'Left_Skewed': Left_Skewed,
                                    'Right_Skewed': Right_Skewed,
                                    'Symmetric': Symmetric,
                                    'Kurtosis': Kurtosis,
                                    'Leptokurtic': Leptokurtic,
                                    'Platykurtic': Platykurtic,
                                    'Mesokurtic': Mesokurtic,
                                    'P68': P68.count(),
                                    'P95': P95.count(),
                                    'P99': P99.count(),
                                    'VIF': VIF,
                                    'Covariance': Covariance,
                                    'Correlation': Correlation
                                    }).T
    return stats[df[features].columns]

# unittests
# desc_stats(df, 'Workdays', 'WorkMonths')
# desc_stats(df, 'Workdays')
# return desc_stats(df, Num) # elapsed time: 7.5s