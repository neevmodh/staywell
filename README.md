# 🌱 STAYWELL - Early Statistical Detection of Academic Burnout

## Domain 2: Data & Statistical Modelling

A pure statistical analysis system for early detection of academic burnout among students. This project uses **transparent statistical techniques** without machine learning black-box models, ensuring full explainability and ethical compliance.

---

## 🎯 Project Overview

Academic burnout is a growing concern affecting student mental health and academic performance. STAYWELL provides an early warning system using measurable lifestyle indicators:

- Sleep duration
- Study hours
- Screen time
- Stress levels
- Attendance percentage

---

## 📊 Statistical Methodology

### Burnout Score Calculation

The system uses a **weighted linear regression model**:

```
Burnout Score = Σ (Weight_i × Normalized_Factor_i)
```

### Risk Factors & Weights

| Factor | Weight | Rationale |
|--------|--------|-----------|
| Sleep Deficit | 30% | Most critical for mental health |
| Stress Level | 20% | Direct psychological strain indicator |
| Screen Time | 20% | Digital fatigue proxy |
| Study Hours | 15% | Excessive studying risk |
| Attendance | 15% | Engagement indicator |

### Normalization Methods

1. **Sleep Deficit**: `max(0, (7 - sleep_hours) / 7)`
   - Based on 7-hour optimal sleep recommendation
   - Higher deficit = higher risk

2. **Stress Level**: `stress_level / 5`
   - Linear normalization from 1-5 scale

3. **Screen Time**: `screen_time / 10`
   - Normalized against 10-hour reference

4. **Study Hours**: `study_hours / 10`
   - Normalized against 10-hour reference

5. **Attendance**: `(100 - attendance) / 100`
   - Inverted: lower attendance = higher risk

### Risk Thresholds

Based on statistical distribution analysis:

- **🟢 Low Risk**: Score < 0.30
- **🟡 Moderate Risk**: 0.30 ≤ Score < 0.60
- **🔴 Elevated Risk**: Score ≥ 0.60

---

## 🔬 Statistical Techniques Used

1. **Descriptive Statistics**
   - Mean, median, standard deviation, variance
   - Quartile analysis (Q1, Q2, Q3, IQR)
   - Range and distribution analysis

2. **Correlation Analysis**
   - Pearson correlation coefficients
   - Correlation matrix visualization
   - Factor relationship identification

3. **Percentile Analysis**
   - Peer comparison using empirical distribution
   - Cohort-based ranking

4. **Sensitivity Analysis**
   - What-if scenario testing
   - Factor impact simulation
   - Intervention effectiveness prediction

5. **Factor Contribution Analysis**
   - Proportional decomposition of risk score
   - Individual factor impact quantification

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

```bash
# Clone the repository
cd staywell

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

---

## 📁 Project Structure

```
staywell/
├── app.py                          # Main Streamlit application
├── config.py                       # Model configuration & weights
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── METHODOLOGY.md                  # Detailed methodology report
│
├── core/                           # Core statistical engine
│   ├── validation.py              # Input validation
│   ├── scoring_engine.py          # Burnout score calculation
│   ├── peer_engine.py             # Peer comparison statistics
│   └── statistical_analysis.py    # Statistical analysis functions
│
├── explainability/                 # Explainability modules
│   ├── contribution.py            # Factor contribution analysis
│   └── what_if.py                 # Scenario simulation
│
├── ui/                            # User interface components
│   ├── dashboard.py               # Visualization functions
│   └── theme.py                   # UI theme configuration
│
└── data/                          # Data files
    └── sample_students.csv        # Sample dataset
```

---

## 📊 Features

### 1. Multiple Input Methods
- **CSV Upload**: Batch analysis of multiple students
- **Manual Entry**: Single student assessment
- **Sample Data**: Pre-loaded example dataset

### 2. Comprehensive Analysis
- **Overview Dashboard**: Risk distribution and summary statistics
- **Statistical Analysis**: Correlations, distributions, descriptive stats
- **Individual Analysis**: Per-student risk assessment and factor breakdown
- **What-If Scenarios**: Intervention impact simulation
- **Methodology Documentation**: Full transparency of calculations

### 3. Visualizations
- Risk distribution pie charts
- Factor contribution bar charts
- Correlation heatmaps
- Variable distribution histograms
- Peer comparison metrics

### 4. Explainability
- Clear factor contributions
- Transparent calculations
- Statistical justifications
- Risk threshold rationale

---

## 📋 CSV Format

Your CSV file should contain the following columns:

```csv
name,sleep_hours,study_hours,screen_time,stress_level,attendance
Alice,6.5,8,5,4,90
Bob,7,6,3,2,95
Charlie,5,10,7,5,75
```

**Column Specifications:**
- `name` (optional): Student identifier
- `sleep_hours`: 0-24 (average daily sleep)
- `study_hours`: 0-24 (average daily study time)
- `screen_time`: 0-24 (average daily recreational screen time)
- `stress_level`: 1-5 (self-reported stress)
- `attendance`: 0-100 (class attendance percentage)

---

## ✅ Domain-2 Compliance Checklist

- ✅ Pure statistical modeling (no ML)
- ✅ Descriptive analysis included
- ✅ Correlation analysis implemented
- ✅ Regression-based scoring
- ✅ Clear risk threshold definitions
- ✅ Full methodology documentation
- ✅ Explainable and transparent
- ✅ Source code provided
- ✅ Statistical model report included

---

## 🔒 Ethical Considerations

1. **Not a Diagnostic Tool**: This is an early warning system for guidance only
2. **Human Oversight Required**: Professional counseling should follow any high-risk identification
3. **Privacy**: All data should be handled confidentially
4. **No Labeling**: Results should support students, not stigmatize them
5. **Transparency**: All calculations are fully explainable and auditable

---

## 📈 Expected Deliverables

### 1. Statistical Model ✅
- Weighted linear regression model
- Factor normalization methods
- Risk score calculation

### 2. Methodology Report ✅
- See `METHODOLOGY.md` for detailed report
- Statistical techniques documented
- Threshold definitions explained

### 3. Risk Threshold Logic ✅
- Three-tier risk classification
- Statistical distribution-based thresholds
- Clear rationale provided

### 4. Source Code ✅
- Fully commented Python code
- Modular architecture
- Easy to understand and modify

---

## 🛠️ Customization

### Adjusting Weights

Edit `config.py` to modify factor weights:

```python
WEIGHTS = {
    "sleep": 0.30,    # Adjust as needed
    "stress": 0.20,
    "screen": 0.20,
    "study": 0.15,
    "attendance": 0.15
}
```

### Changing Risk Thresholds

Edit `core/scoring_engine.py` in the `risk_label()` function:

```python
def risk_label(score):
    if score < 0.3:  # Adjust threshold
        return "🟢 Low Risk"
    elif score < 0.6:  # Adjust threshold
        return "🟡 Moderate Risk"
    return "🔴 Elevated Risk"
```

---

## 📞 Support

For questions or issues, please refer to the methodology documentation or review the inline code comments.

---

## 📄 License

This project is developed for educational purposes as part of Domain 2: Data & Statistical Modelling challenge.

---

## 🙏 Acknowledgments

- Statistical methods based on established psychological research
- Risk factors identified from academic burnout literature
- Ethical guidelines following mental health best practices

---

**Remember**: This tool provides early guidance only, not clinical diagnosis. Always involve qualified professionals for student mental health support.
