# 📚 STAYWELL Documentation Index

Complete guide to all project documentation and resources.

---

## 🚀 Getting Started

### For First-Time Users
1. **[INSTALL.md](INSTALL.md)** - Installation and setup instructions
2. **[QUICKSTART.md](QUICKSTART.md)** - Quick start guide (3 steps)
3. **[README.md](README.md)** - Project overview and features

### For Evaluators/Reviewers
1. **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Executive summary
2. **[SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md)** - Deliverables verification
3. **[METHODOLOGY.md](METHODOLOGY.md)** - Statistical methodology report

---

## 📖 Documentation Files

### Essential Documentation

| File | Purpose | Audience | Length |
|------|---------|----------|--------|
| **README.md** | Project overview, features, setup | Everyone | ~400 lines |
| **METHODOLOGY.md** | Statistical methodology report | Evaluators, Technical | ~300 lines |
| **QUICKSTART.md** | Quick start guide | New users | ~150 lines |
| **INSTALL.md** | Installation instructions | Developers | ~250 lines |

### Supplementary Documentation

| File | Purpose | Audience | Length |
|------|---------|----------|--------|
| **PROJECT_SUMMARY.md** | Executive summary | Evaluators | ~250 lines |
| **SUBMISSION_CHECKLIST.md** | Deliverables checklist | Evaluators | ~200 lines |
| **UI_GUIDE.md** | User interface guide | Users | ~300 lines |
| **INDEX.md** | This file - documentation index | Everyone | ~150 lines |

---

## 💻 Source Code Files

### Core Application

| File | Purpose | Lines | Key Functions |
|------|---------|-------|---------------|
| **app.py** | Main Streamlit application | ~300 | Main dashboard, tabs, UI |
| **config.py** | Model configuration | ~15 | Weights, limits |
| **analysis_script.py** | CLI analysis tool | ~100 | Batch analysis |
| **test_system.py** | System tests | ~150 | Validation tests |

### Core Engine (`core/`)

| File | Purpose | Lines | Key Functions |
|------|---------|-------|---------------|
| **validation.py** | Input validation | ~20 | validate_row() |
| **scoring_engine.py** | Burnout scoring | ~60 | burnout_score(), risk_label() |
| **peer_engine.py** | Peer comparison | ~30 | peer_percentile(), cohort_statistics() |
| **statistical_analysis.py** | Statistical functions | ~80 | correlation_analysis(), descriptive_statistics() |

### Explainability (`explainability/`)

| File | Purpose | Lines | Key Functions |
|------|---------|-------|---------------|
| **contribution.py** | Factor contribution | ~30 | contribution() |
| **what_if.py** | Scenario simulation | ~40 | simulate(), batch_simulate() |

### UI Components (`ui/`)

| File | Purpose | Lines | Key Functions |
|------|---------|-------|---------------|
| **dashboard.py** | Visualizations | ~120 | render_contribution(), render_correlation_matrix() |
| **theme.py** | UI theme | ~10 | Color definitions |

---

## 📊 Data Files

### Sample Data (`data/`)

| File | Purpose | Records | Columns |
|------|---------|---------|---------|
| **sample_students.csv** | Sample dataset | 20 | 6 (name + 5 factors) |
| **sample_students_results.csv** | Analysis results | 20 | 8 (+ score + risk) |

### CSV Format
```csv
name,sleep_hours,study_hours,screen_time,stress_level,attendance
Student Name,6.5,8,5,4,90
```

---

## 📋 Quick Reference

### Installation
```bash
cd staywell
pip install -r requirements.txt
python test_system.py
streamlit run app.py
```

### CLI Analysis
```bash
python analysis_script.py data/sample_students.csv
```

### Testing
```bash
python test_system.py
```

---

## 🎯 Documentation by Use Case

### "I want to install and run the app"
→ Read: **INSTALL.md** → **QUICKSTART.md**

### "I want to understand the statistical model"
→ Read: **METHODOLOGY.md** → **README.md** (Section 3)

### "I want to evaluate the project"
→ Read: **PROJECT_SUMMARY.md** → **SUBMISSION_CHECKLIST.md** → **METHODOLOGY.md**

### "I want to use the application"
→ Read: **QUICKSTART.md** → **UI_GUIDE.md**

### "I want to modify the code"
→ Read: **README.md** (Section 10) → Source code comments

### "I want to understand the UI"
→ Read: **UI_GUIDE.md** → Try the app

---

## 📐 Statistical Methodology

### Key Concepts Documented

1. **Model Specification** (METHODOLOGY.md, Section 3)
   - Weighted linear regression
   - Factor normalization
   - Score calculation

2. **Risk Thresholds** (METHODOLOGY.md, Section 4)
   - Three-tier classification
   - Threshold rationale
   - Clinical interpretation

3. **Statistical Techniques** (METHODOLOGY.md, Section 5)
   - Descriptive statistics
   - Correlation analysis
   - Percentile analysis
   - Sensitivity analysis

4. **Validation** (METHODOLOGY.md, Section 7)
   - Face validity
   - Logical consistency
   - Sensitivity testing

---

## 🔍 Finding Information

### By Topic

**Installation Issues**
- INSTALL.md → Troubleshooting section
- README.md → Getting Started section

**Statistical Questions**
- METHODOLOGY.md → Full methodology
- README.md → Statistical Methodology section
- app.py → Tab 5 (Methodology)

**Usage Questions**
- QUICKSTART.md → Step-by-step guide
- UI_GUIDE.md → Interface details
- README.md → Features section

**Code Questions**
- Source files → Inline comments
- README.md → Project Structure section
- test_system.py → Component tests

**Evaluation/Grading**
- PROJECT_SUMMARY.md → Overview
- SUBMISSION_CHECKLIST.md → Requirements
- METHODOLOGY.md → Technical details

---

## 📊 Project Statistics

### Documentation
- **Total documentation files**: 8
- **Total documentation lines**: ~2,000
- **Total words**: ~15,000

### Source Code
- **Total code files**: 12
- **Total code lines**: ~900
- **Total functions**: ~30

### Data
- **Sample students**: 20
- **Variables tracked**: 5
- **Output metrics**: 2 (score + risk)

---

## ✅ Completeness Checklist

### Documentation
- ✅ Installation guide
- ✅ Quick start guide
- ✅ User manual
- ✅ Technical methodology
- ✅ API/Code documentation
- ✅ UI guide
- ✅ Project summary
- ✅ Submission checklist

### Code
- ✅ Main application
- ✅ Core engine
- ✅ Statistical analysis
- ✅ Explainability
- ✅ Visualizations
- ✅ Tests
- ✅ CLI tools

### Data
- ✅ Sample dataset
- ✅ CSV template
- ✅ Results examples

---

## 🔗 Document Relationships

```
README.md (Start here)
├── INSTALL.md (Setup)
│   └── QUICKSTART.md (First use)
│       └── UI_GUIDE.md (Learn interface)
│
├── METHODOLOGY.md (Technical details)
│   └── PROJECT_SUMMARY.md (Overview)
│       └── SUBMISSION_CHECKLIST.md (Verification)
│
└── INDEX.md (This file - Navigation)
```

---

## 📞 Support Resources

### For Installation Help
1. INSTALL.md → Troubleshooting
2. test_system.py → Run diagnostics
3. README.md → Requirements

### For Usage Help
1. QUICKSTART.md → Basic usage
2. UI_GUIDE.md → Interface details
3. app.py → Tab 5 (in-app help)

### For Technical Questions
1. METHODOLOGY.md → Statistical details
2. Source code → Inline comments
3. PROJECT_SUMMARY.md → Overview

---

## 🎓 Learning Path

### Beginner Path
1. README.md (overview)
2. INSTALL.md (setup)
3. QUICKSTART.md (first use)
4. UI_GUIDE.md (learn interface)

### Technical Path
1. PROJECT_SUMMARY.md (overview)
2. METHODOLOGY.md (methodology)
3. Source code (implementation)
4. test_system.py (validation)

### Evaluator Path
1. PROJECT_SUMMARY.md (executive summary)
2. SUBMISSION_CHECKLIST.md (requirements)
3. METHODOLOGY.md (technical details)
4. Source code (verification)

---

## 📝 Document Formats

All documentation is in **Markdown (.md)** format:
- ✅ Easy to read in any text editor
- ✅ Renders beautifully on GitHub
- ✅ Converts easily to PDF/HTML
- ✅ Version control friendly

---

## 🔄 Document Updates

**Last Updated**: 2026
**Version**: 1.0
**Status**: Complete

All documentation is current and synchronized with code version 1.0.

---

## 📦 What to Read First

### If you're a...

**Student/User**:
1. README.md
2. QUICKSTART.md
3. UI_GUIDE.md

**Developer**:
1. README.md
2. INSTALL.md
3. Source code

**Evaluator/Grader**:
1. PROJECT_SUMMARY.md
2. SUBMISSION_CHECKLIST.md
3. METHODOLOGY.md

**Researcher**:
1. METHODOLOGY.md
2. README.md
3. Source code

---

**Navigate this documentation to find everything you need about STAYWELL!** 📚
