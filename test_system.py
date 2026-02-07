"""
System Test Script
Validates all components are working correctly
"""
import pandas as pd
import sys

def test_imports():
    """Test all imports"""
    print("Testing imports...")
    try:
        from core.validation import validate_row
        from core.scoring_engine import burnout_score, risk_label, get_statistical_summary
        from core.peer_engine import peer_percentile, cohort_statistics
        from core.statistical_analysis import correlation_analysis, descriptive_statistics
        from explainability.contribution import contribution
        from explainability.what_if import simulate, batch_simulate
        from ui.dashboard import render_contribution, render_correlation_matrix
        from ui.theme import PRIMARY, SECONDARY, RISK_COLORS
        print("✅ All imports successful")
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False

def test_data_loading():
    """Test sample data loading"""
    print("\nTesting data loading...")
    try:
        df = pd.read_csv("data/sample_students.csv")
        print(f"✅ Loaded {len(df)} students")
        return True, df
    except Exception as e:
        print(f"❌ Data loading error: {e}")
        return False, None

def test_validation(df):
    """Test validation"""
    print("\nTesting validation...")
    try:
        from core.validation import validate_row
        df_validated = df.apply(validate_row, axis=1)
        print("✅ Validation successful")
        return True, df_validated
    except Exception as e:
        print(f"❌ Validation error: {e}")
        return False, None

def test_scoring(df):
    """Test scoring"""
    print("\nTesting scoring...")
    try:
        from core.scoring_engine import burnout_score, risk_label
        df["burnout_score"] = df.apply(burnout_score, axis=1)
        df["risk"] = df["burnout_score"].apply(risk_label)
        print(f"✅ Scoring successful - Mean score: {df['burnout_score'].mean():.3f}")
        return True, df
    except Exception as e:
        print(f"❌ Scoring error: {e}")
        return False, None

def test_statistics(df):
    """Test statistical analysis"""
    print("\nTesting statistical analysis...")
    try:
        from core.statistical_analysis import correlation_analysis, descriptive_statistics
        from core.peer_engine import cohort_statistics
        
        corr = correlation_analysis(df)
        desc = descriptive_statistics(df)
        cohort = cohort_statistics(df)
        
        print(f"✅ Statistics successful")
        print(f"   - Correlation matrix: {corr.shape}")
        print(f"   - Descriptive stats: {desc.shape}")
        print(f"   - Cohort mean: {cohort['mean']:.3f}")
        return True
    except Exception as e:
        print(f"❌ Statistics error: {e}")
        return False

def test_explainability(df):
    """Test explainability features"""
    print("\nTesting explainability...")
    try:
        from explainability.contribution import contribution
        from explainability.what_if import simulate, batch_simulate
        
        row = df.iloc[0]
        contrib = contribution(row)
        sim_score = simulate(row, sleep_delta=1)
        batch = batch_simulate(row)
        
        print(f"✅ Explainability successful")
        print(f"   - Top contributor: {max(contrib, key=contrib.get)}")
        print(f"   - Simulation scenarios: {len(batch)}")
        return True
    except Exception as e:
        print(f"❌ Explainability error: {e}")
        return False

def test_model_config():
    """Test model configuration"""
    print("\nTesting model configuration...")
    try:
        from core.scoring_engine import get_statistical_summary
        summary = get_statistical_summary()
        
        print(f"✅ Model config successful")
        print(f"   - Weights: {list(summary['weights'].keys())}")
        print(f"   - Thresholds: {list(summary['thresholds'].keys())}")
        return True
    except Exception as e:
        print(f"❌ Model config error: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("STAYWELL SYSTEM TEST")
    print("=" * 60)
    
    results = []
    
    # Test imports
    results.append(test_imports())
    
    # Test data loading
    success, df = test_data_loading()
    results.append(success)
    if not success:
        print("\n❌ Cannot continue without data")
        sys.exit(1)
    
    # Test validation
    success, df = test_validation(df)
    results.append(success)
    if not success:
        print("\n❌ Cannot continue without validation")
        sys.exit(1)
    
    # Test scoring
    success, df = test_scoring(df)
    results.append(success)
    if not success:
        print("\n❌ Cannot continue without scoring")
        sys.exit(1)
    
    # Test statistics
    results.append(test_statistics(df))
    
    # Test explainability
    results.append(test_explainability(df))
    
    # Test model config
    results.append(test_model_config())
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("\n✅ ALL TESTS PASSED - System is ready!")
        return 0
    else:
        print(f"\n❌ {total - passed} test(s) failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())
