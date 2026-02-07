"""
Statistical Analysis Module
Pure statistical techniques for burnout analysis - No ML
"""
import pandas as pd
import numpy as np

def correlation_analysis(df):
    """
    Calculate Pearson correlation coefficients between variables
    Returns correlation matrix for key variables
    """
    variables = ['sleep_hours', 'study_hours', 'screen_time', 'stress_level', 'attendance', 'burnout_score']
    available_vars = [v for v in variables if v in df.columns]
    
    if len(available_vars) < 2:
        return pd.DataFrame()
    
    corr_matrix = df[available_vars].corr()
    return corr_matrix

def descriptive_statistics(df):
    """
    Calculate descriptive statistics for all numeric variables
    """
    variables = ['sleep_hours', 'study_hours', 'screen_time', 'stress_level', 'attendance', 'burnout_score']
    available_vars = [v for v in variables if v in df.columns]
    
    if not available_vars:
        return pd.DataFrame()
    
    stats = df[available_vars].describe().T
    stats['variance'] = df[available_vars].var()
    stats['median'] = df[available_vars].median()
    
    # Reorder columns for better readability
    column_order = ['count', 'mean', 'median', 'std', 'variance', 'min', '25%', '50%', '75%', 'max']
    stats = stats[[col for col in column_order if col in stats.columns]]
    
    return stats.round(2)

def regression_analysis(df):
    """
    Simple linear regression analysis to understand factor relationships
    Returns coefficients showing impact of each factor on burnout score
    """
    if len(df) < 3:
        return None
    
    X_vars = ['sleep_hours', 'study_hours', 'screen_time', 'stress_level', 'attendance']
    available_X = [v for v in X_vars if v in df.columns]
    
    if 'burnout_score' not in df.columns or not available_X:
        return None
    
    # Calculate simple correlation coefficients as regression indicators
    coefficients = {}
    for var in available_X:
        corr = df[var].corr(df['burnout_score'])
        coefficients[var] = round(corr, 3)
    
    return coefficients

def distribution_analysis(df, variable):
    """
    Analyze distribution of a specific variable
    Returns quartiles, IQR, and outlier bounds
    """
    if variable not in df.columns:
        return None
    
    data = df[variable]
    q1 = data.quantile(0.25)
    q2 = data.quantile(0.50)  # median
    q3 = data.quantile(0.75)
    iqr = q3 - q1
    
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    return {
        'Q1': round(q1, 2),
        'Q2 (Median)': round(q2, 2),
        'Q3': round(q3, 2),
        'IQR': round(iqr, 2),
        'Lower Bound': round(lower_bound, 2),
        'Upper Bound': round(upper_bound, 2),
        'Outliers': len(data[(data < lower_bound) | (data > upper_bound)])
    }
