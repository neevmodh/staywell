"""
Standalone Analysis Script
Run burnout analysis from command line without Streamlit UI
"""
import pandas as pd
import sys
from core.validation import validate_row
from core.scoring_engine import burnout_score, risk_label
from core.statistical_analysis import correlation_analysis, descriptive_statistics
from core.peer_engine import cohort_statistics

def analyze_csv(filepath):
    """Analyze a CSV file and print results"""
    print("=" * 60)
    print("STAYWELL - Burnout Analysis Report")
    print("=" * 60)
    print()
    
    # Load data
    try:
        df = pd.read_csv(filepath)
        print(f"✓ Loaded {len(df)} students from {filepath}")
    except Exception as e:
        print(f"✗ Error loading file: {e}")
        return
    
    # Add name column if missing
    if 'name' not in df.columns:
        df['name'] = [f"Student {i+1}" for i in range(len(df))]
    
    # Validate and score
    df = df.apply(validate_row, axis=1)
    df["burnout_score"] = df.apply(burnout_score, axis=1)
    df["risk"] = df["burnout_score"].apply(risk_label)
    
    print()
    print("-" * 60)
    print("RISK DISTRIBUTION")
    print("-" * 60)
    risk_counts = df['risk'].value_counts()
    for risk, count in risk_counts.items():
        pct = count / len(df) * 100
        print(f"{risk}: {count} students ({pct:.1f}%)")
    
    print()
    print("-" * 60)
    print("COHORT STATISTICS")
    print("-" * 60)
    stats = cohort_statistics(df)
    for key, value in stats.items():
        print(f"{key.upper()}: {value}")
    
    print()
    print("-" * 60)
    print("TOP 5 HIGHEST RISK STUDENTS")
    print("-" * 60)
    top_risk = df.nlargest(5, 'burnout_score')[['name', 'burnout_score', 'risk']]
    print(top_risk.to_string(index=False))
    
    print()
    print("-" * 60)
    print("DESCRIPTIVE STATISTICS")
    print("-" * 60)
    desc = descriptive_statistics(df)
    print(desc.to_string())
    
    print()
    print("-" * 60)
    print("CORRELATION WITH BURNOUT SCORE")
    print("-" * 60)
    corr = correlation_analysis(df)
    if 'burnout_score' in corr.columns:
        burnout_corr = corr['burnout_score'].drop('burnout_score')
        for var, corr_val in burnout_corr.items():
            print(f"{var}: {corr_val:.3f}")
    
    print()
    print("=" * 60)
    print("Analysis Complete!")
    print("=" * 60)
    
    # Save results
    output_file = filepath.replace('.csv', '_results.csv')
    df.to_csv(output_file, index=False)
    print(f"\n✓ Results saved to: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analysis_script.py <path_to_csv>")
        print("Example: python analysis_script.py data/sample_students.csv")
        sys.exit(1)
    
    analyze_csv(sys.argv[1])
