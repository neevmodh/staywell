import numpy as np

def peer_percentile(scores, value):
    """
    Calculate percentile rank of a value within a distribution
    Returns percentage of scores below the given value
    """
    return round((scores < value).mean() * 100, 1)

def cohort_statistics(df):
    """
    Calculate comprehensive statistics for the entire cohort
    """
    scores = df['burnout_score']
    
    return {
        'mean': round(scores.mean(), 3),
        'median': round(scores.median(), 3),
        'std': round(scores.std(), 3),
        'variance': round(scores.var(), 3),
        'min': round(scores.min(), 3),
        'max': round(scores.max(), 3),
        'range': round(scores.max() - scores.min(), 3),
        'q1': round(scores.quantile(0.25), 3),
        'q3': round(scores.quantile(0.75), 3),
        'iqr': round(scores.quantile(0.75) - scores.quantile(0.25), 3)
    }
