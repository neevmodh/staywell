# 🌱 STAYWELL

## Early Detection of Academic Burnout Through Statistical Analysis

**A Statistical Risk Assessment Platform Powered by Pure Mathematical Modeling**

---

## 📊 STATUS & FOCUS

![Status](https://img.shields.io/badge/STATUS-PRODUCTION%20READY-brightgreen?style=for-the-badge)
![Focus](https://img.shields.io/badge/FOCUS-BURNOUT%20DETECTION-blue?style=for-the-badge)
![Math](https://img.shields.io/badge/MATH-STATISTICAL%20MODELS-purple?style=for-the-badge)

![Frontend](https://img.shields.io/badge/FRONTEND-STREAMLIT-orange?style=for-the-badge)
![Backend](https://img.shields.io/badge/BACKEND-PYTHON-green?style=for-the-badge)
![Visualization](https://img.shields.io/badge/VISUALIZATION-MATPLOTLIB-blue?style=for-the-badge)

---

## 🎯 Overview

STAYWELL is an evidence-based early warning system designed to identify academic burnout risk among students using transparent statistical analysis. Unlike black-box machine learning approaches, our system employs **pure mathematical modeling** with full explainability and ethical compliance.

### The Problem

Academic burnout affects student mental health, performance, and well-being. Early detection enables timely intervention and support.

### Our Solution

A statistical risk assessment platform that analyzes measurable lifestyle indicators:
- 🛏️ Sleep patterns
- 📚 Study load
- 📱 Screen time
- 😰 Stress levels
- 📊 Academic engagement

---

## ✨ Key Features

### 📥 Multiple Input Methods
- **CSV Upload**: Batch analysis for entire cohorts
- **Manual Entry**: Individual student assessment with real-time validation
- **Sample Data**: Pre-loaded demonstration dataset

### 📊 Comprehensive Analytics
- **Risk Overview**: Distribution analysis and summary statistics
- **Statistical Analysis**: Correlations, distributions, descriptive statistics
- **Individual Assessment**: Per-student risk breakdown with factor contributions
- **Scenario Simulation**: What-if analysis for intervention planning
- **Full Transparency**: Complete methodology documentation

### 🎨 Visual Intelligence
- Risk distribution bar charts
- Time allocation visualizations
- Factor contribution breakdowns
- Correlation heatmaps
- Distribution histograms
- Color-coded risk indicators

### 🔍 Explainability First
- Transparent calculations
- Factor contribution analysis
- Statistical justifications
- Clear risk thresholds
- No black-box models

---

## 🔬 Statistical Methodology

### Burnout Score Model

**Weighted Linear Regression:**
```
Burnout Score = Σ (Weight_i × Normalized_Factor_i)
```

### Risk Factors & Weights

| Factor | Weight | Rationale |
|--------|--------|-----------|
| Sleep Deficit | 30% | Most critical for mental health and cognitive function |
| Stress Level | 20% | Direct indicator of psychological strain |
| Screen Time | 20% | Proxy for digital fatigue and time management |
| Study Hours | 15% | Excessive studying can lead to burnout |
| Attendance | 15% | Low attendance indicates disengagement |

### Normalization Techniques

1. **Sleep Deficit**: `max(0, (7 - sleep_hours) / 7)`
2. **Stress Level**: `stress_level / 5`
3. **Screen Time**: `screen_time / 10`
4. **Study Hours**: `study_hours / 10`
5. **Attendance**: `(100 - attendance) / 100`

### Risk Classification

- 🟢 **Low Risk**: Score < 0.30
- 🟡 **Moderate Risk**: 0.30 ≤ Score < 0.60
- 🔴 **Elevated Risk**: Score ≥ 0.60

### Statistical Techniques

1. **Descriptive Statistics**: Mean, median, standard deviation, variance
2. **Correlation Analysis**: Pearson correlation coefficients
3. **Percentile Analysis**: Peer comparison using empirical distribution
4. **Sensitivity Analysis**: What-if scenario testing
5. **Factor Decomposition**: Proportional risk contribution

---

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.8+
pip package manager
```

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd staywell

# Install dependencies
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

Access at: **http://localhost:8501**

---

## 📁 Project Architecture

```
staywell/
│
├── app.py                          # Main Streamlit application
├── config.py                       # Model configuration & weights
├── requirements.txt                # Python dependencies
│
├── core/                           # Statistical Engine
│   ├── validation.py              # Input validation & constraints
│   ├── scoring_engine.py          # Burnout score calculation
│   ├── peer_engine.py             # Peer comparison statistics
│   └── statistical_analysis.py    # Statistical analysis functions
│
├── explainability/                 # Explainability Modules
│   ├── contribution.py            # Factor contribution analysis
│   └── what_if.py                 # Scenario simulation engine
│
├── ui/                            # User Interface
│   ├── dashboard.py               # Visualization components
│   └── theme.py                   # UI theme configuration
│
└── data/                          # Data Files
    ├── sample_students.csv        # Sample dataset
    └── test_invalid.csv           # Validation test data
```

---

## 📊 Data Format

### CSV Structure

```csv
name,sleep_hours,study_hours,screen_time,stress_level,attendance
Alice Johnson,7.0,6.0,4.0,3,90
Bob Smith,8.0,5.0,3.0,2,95
Charlie Brown,6.0,7.0,5.0,4,82
```

### Column Specifications

| Column | Type | Range | Description |
|--------|------|-------|-------------|
| `name` | String | - | Student identifier (optional) |
| `sleep_hours` | Float | 0-24 | Average daily sleep duration |
| `study_hours` | Float | 0-24 | Average daily study time |
| `screen_time` | Float | 0-24 | Average daily recreational screen time |
| `stress_level` | Integer | 1-5 | Self-reported stress (1=Low, 5=High) |
| `attendance` | Integer | 0-100 | Class attendance percentage |

### ⚠️ Important Constraint

**24-Hour Rule**: `sleep_hours + study_hours + screen_time ≤ 24`

Records violating this constraint are automatically filtered with notification.

---

## 🎯 Use Cases

### For Educators
- Monitor cohort mental health trends
- Identify at-risk students early
- Plan targeted interventions
- Track effectiveness of support programs

### For Counselors
- Prioritize student outreach
- Understand risk factor patterns
- Simulate intervention impacts
- Support evidence-based counseling

### For Administrators
- Assess institutional wellness
- Allocate support resources
- Evaluate policy effectiveness
- Generate statistical reports

### For Researchers
- Analyze burnout patterns
- Study factor correlations
- Test intervention strategies
- Validate statistical models

---

## 🔒 Ethical Framework

### Core Principles

1. **Transparency**: All calculations are fully explainable
2. **Privacy**: Confidential data handling required
3. **Support-Focused**: Results guide help, not punishment
4. **Human Oversight**: Professional judgment essential
5. **Not Diagnostic**: Early warning only, not clinical diagnosis

### Responsible Use

- ✅ Use for early identification and support
- ✅ Combine with professional counseling
- ✅ Maintain student privacy
- ✅ Focus on intervention, not labeling
- ❌ Do not use as sole diagnostic tool
- ❌ Do not stigmatize high-risk students
- ❌ Do not share results without consent

---

## 🛠️ Customization

### Adjust Risk Weights

Edit `config.py`:

```python
WEIGHTS = {
    "sleep": 0.30,      # Sleep deficit weight
    "stress": 0.20,     # Stress level weight
    "screen": 0.20,     # Screen time weight
    "study": 0.15,      # Study hours weight
    "attendance": 0.15  # Attendance weight
}
```

### Modify Risk Thresholds

Edit `core/scoring_engine.py`:

```python
def risk_label(score):
    if score < 0.3:     # Low risk threshold
        return "🟢 Low Risk"
    elif score < 0.6:   # Moderate risk threshold
        return "🟡 Moderate Risk"
    return "🔴 Elevated Risk"
```

### Customize Visualizations

Edit `ui/dashboard.py` to modify charts, colors, and layouts.

---

## 📈 Domain-2 Compliance

✅ **Pure Statistical Modeling** - No machine learning black boxes  
✅ **Descriptive Analysis** - Comprehensive statistical summaries  
✅ **Correlation Analysis** - Factor relationship identification  
✅ **Regression-Based Scoring** - Weighted linear model  
✅ **Clear Risk Thresholds** - Statistically justified classifications  
✅ **Full Documentation** - Complete methodology report  
✅ **Explainable Results** - Transparent calculations  
✅ **Source Code Provided** - Open and auditable  

---

## 🧪 Testing

### Test with Invalid Data

```bash
# Upload data/test_invalid.csv to see validation in action
# Contains records that violate 24-hour constraint
```

### Manual Entry Testing

1. Select "Manual Entry" mode
2. Adjust time values to exceed 24 hours
3. Observe real-time validation feedback
4. Correct values to see risk assessment

---

## 📚 Documentation

- **METHODOLOGY.md** - Detailed statistical methodology
- **AI_USAGE_SUMMARY.md** - AI assistance documentation
- **SIMPLE_UPDATE.md** - Recent updates and changes
- **Inline Comments** - Code-level documentation

---

## 🤝 Contributing

This project is developed for educational purposes. Suggestions for improvements:

1. Additional risk factors
2. Enhanced visualizations
3. Export functionality
4. Multi-language support
5. Mobile responsiveness

---

## 📄 License

Educational project developed for Domain 2: Data & Statistical Modelling.

---

## 🙏 Acknowledgments

- Statistical methods based on psychological research
- Risk factors from academic burnout literature
- Ethical guidelines from mental health best practices
- UI/UX inspired by modern data platforms

---

## 📞 Support

For questions, issues, or suggestions:
- Review inline code documentation
- Check METHODOLOGY.md for detailed explanations
- Examine sample data for format examples

---

## ⚠️ Disclaimer

**STAYWELL is an early warning system, not a diagnostic tool.**

Always involve qualified mental health professionals for student support. This system provides statistical guidance to complement, not replace, professional judgment.

---

<div align="center">

**Built with ❤️ for Student Wellness**

*Empowering Early Intervention Through Statistical Intelligence*

</div>
