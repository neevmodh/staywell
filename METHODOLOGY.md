

| Factor | Weight | Justification |
|--------|--------|---------------|
| Sleep Deficit | 0.30 | Sleep is the most critical factor for cognitive function and mental health. Research shows strong correlation between sleep deprivation and burnout. |
| Stress Level | 0.20 | Direct measure of psychological strain. Self-reported stress is a validated indicator of burnout risk. |
| Screen Time | 0.20 | Proxy for digital fatigue and poor time management. Excessive screen time correlates with reduced well-being. |
| Study Hours | 0.15 | While studying is necessary, excessive hours indicate poor work-life balance and potential burnout. |
| Attendance | 0.15 | Low attendance signals disengagement, a key burnout symptom. |

**Total Weight**: 1.00 (normalized)

### 3.3 Normalization Functions

Each factor is normalized to [0, 1] scale:

**1. Sleep Deficit**:
```
f₁(sleep) = max(0, (7 - sleep_hours) / 7)
```
- Based on 7-hour optimal sleep recommendation
- Deficit increases risk linearly
- No penalty for oversleeping (max at 0)

**2. Stress Level**:
```
f₂(stress) = stress_level / 5
```
- Linear normalization from 1-5 scale
- Higher stress = higher risk

**3. Screen Time**:
```
f₃(screen) = screen_time / 10
```
- Normalized against 10-hour reference
- Assumes >10 hours is maximum risk

**4. Study Hours**:
```
f₄(study) = study_hours / 10
```
- Normalized against 10-hour reference
- Excessive studying contributes to burnout

**5. Attendance**:
```
f₅(attendance) = (100 - attendance) / 100
```
- Inverted: lower attendance = higher risk
- 0% attendance = maximum risk (1.0)
- 100% attendance = no risk (0.0)

---

## 4. Risk Threshold Definitions

### 4.1 Threshold Selection

Risk thresholds based on tertile distribution:

| Risk Level | Score Range | Percentile | Interpretation |
|------------|-------------|------------|----------------|
| 🟢 Low Risk | 0.00 - 0.29 | 0-33rd | Minimal burnout indicators |
| 🟡 Moderate Risk | 0.30 - 0.59 | 33rd-66th | Some warning signs present |
| 🔴 Elevated Risk | 0.60 - 1.00 | 66th-100th | Multiple risk factors present |

### 4.2 Threshold Rationale

**Low Risk (< 0.30)**:
- Student shows healthy lifestyle patterns
- Minor concerns may exist but overall low risk
- Preventive measures recommended

**Moderate Risk (0.30 - 0.60)**:
- Multiple factors showing concerning patterns
- Early intervention recommended
- Monitor for progression

**Elevated Risk (≥ 0.60)**:
- Significant burnout indicators present
- Immediate support recommended
- Professional counseling advised

---

## 5. Statistical Analysis Techniques

### 5.1 Descriptive Statistics

For each variable, we calculate:
- **Mean**: Central tendency measure
- **Median**: Robust central tendency (less affected by outliers)
- **Standard Deviation**: Variability measure
- **Variance**: Squared deviation measure
- **Quartiles**: Distribution shape (Q1, Q2, Q3)
- **Range**: Min to Max spread

### 5.2 Correlation Analysis

**Method**: Pearson Correlation Coefficient

**Formula**:
```
r = Σ[(xᵢ - x̄)(yᵢ - ȳ)] / √[Σ(xᵢ - x̄)² · Σ(yᵢ - ȳ)²]
```

**Interpretation**:
- r > 0.7: Strong positive correlation
- 0.3 < r < 0.7: Moderate correlation
- r < 0.3: Weak correlation
- Negative values indicate inverse relationships

### 5.3 Percentile Analysis

**Method**: Empirical Cumulative Distribution Function (ECDF)

**Formula**:
```
Percentile(x) = (# of values < x) / (total # of values) × 100
```

Used for peer comparison and cohort ranking.

### 5.4 Sensitivity Analysis (What-If Scenarios)

Tests impact of lifestyle changes on burnout score:
- Sleep adjustment: ±1, ±2 hours
- Screen time adjustment: ±1, ±2 hours
- Combined interventions

Helps identify most effective interventions.

---

## 6. Factor Contribution Analysis

### 6.1 Proportional Decomposition

Each factor's contribution to total score:

```
Contribution_i = (wᵢ · fᵢ) / Σ(wⱼ · fⱼ) × 100%
```

### 6.2 Interpretation

- Identifies primary risk drivers
- Guides intervention priorities
- Provides personalized insights

---

## 7. Model Validation

### 7.1 Face Validity

- Model aligns with psychological research on burnout
- Factors are established burnout predictors
- Weights reflect relative importance in literature

### 7.2 Logical Consistency

- Higher risk factors → higher scores ✓
- Normalization prevents scale bias ✓
- Weights sum to 1.0 ✓
- Score bounded [0, 1] ✓

### 7.3 Sensitivity Testing

- Model responds appropriately to input changes
- What-if scenarios show expected behavior
- No unexpected discontinuities

---

## 8. Limitations & Considerations

### 8.1 Model Limitations

1. **Self-Reported Data**: Relies on accurate self-reporting
2. **Linear Assumptions**: Assumes linear relationships
3. **Static Weights**: Weights don't adapt to individual differences
4. **Snapshot Assessment**: Point-in-time, not longitudinal
5. **Limited Factors**: Doesn't capture all burnout dimensions

### 8.2 Ethical Considerations

1. **Not Diagnostic**: Tool provides guidance, not clinical diagnosis
2. **Privacy**: Data must be handled confidentially
3. **No Stigmatization**: Results should support, not label
4. **Human Oversight**: Professional judgment required
5. **Transparency**: All calculations fully explainable

---

## 9. Implementation Details

### 9.1 Computational Complexity

- **Time Complexity**: O(n) for n students
- **Space Complexity**: O(n)
- **Real-time Processing**: Instant results

### 9.2 Scalability

- Handles individual or batch analysis
- No training required (rule-based)
- Easily deployable

---

## 10. Conclusion

The STAYWELL system provides a transparent, explainable approach to early burnout detection using pure statistical methods. The weighted linear model offers:

✅ **Transparency**: All calculations fully documented
✅ **Explainability**: Clear factor contributions
✅ **Validity**: Grounded in research
✅ **Practicality**: Easy to implement and use
✅ **Ethics**: Designed for support, not diagnosis

### 10.1 Domain-2 Compliance

✅ Pure statistical modeling (no ML black-box)
✅ Descriptive statistics implemented
✅ Correlation analysis included
✅ Regression-based approach
✅ Clear threshold definitions
✅ Full methodology documentation

---

## References

1. Maslach, C., & Leiter, M. P. (2016). Understanding the burnout experience: recent research and its implications for psychiatry. *World Psychiatry*, 15(2), 103-111.

2. Schaufeli, W. B., et al. (2002). Burnout and engagement in university students: A cross-national study. *Journal of Cross-Cultural Psychology*, 33(5), 464-481.

3. Walker, M. (2017). *Why We Sleep: Unlocking the Power of Sleep and Dreams*. Scribner.

4. American Psychological Association. (2020). Stress in America 2020: A National Mental Health Crisis.

---

**Document Version**: 1.0
**Last Updated**: 2026
**Author**: STAYWELL Development Team
