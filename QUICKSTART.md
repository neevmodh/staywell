# 🚀 Quick Start Guide - STAYWELL

## Get Started in 3 Steps

### Step 1: Install Dependencies

```bash
cd staywell
pip install -r requirements.txt
```

### Step 2: Run the Application

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

### Step 3: Choose Your Input Method

**Option A: Use Sample Data**
1. Select "Use Sample Data" in the sidebar
2. Explore the pre-loaded dataset of 20 students

**Option B: Upload Your CSV**
1. Select "Upload CSV" in the sidebar
2. Upload a CSV file with these columns:
   - `sleep_hours` (0-24)
   - `study_hours` (0-24)
   - `screen_time` (0-24)
   - `stress_level` (1-5)
   - `attendance` (0-100)
   - `name` (optional)

**Option C: Manual Entry**
1. Select "Manual Entry" in the sidebar
2. Fill in the form with student data
3. View instant results

---

## 📊 Exploring the Dashboard

### Tab 1: Overview
- See total students and risk distribution
- View all students in a table
- Check risk level pie chart

### Tab 2: Statistical Analysis
- Descriptive statistics for all variables
- Correlation matrix and heatmap
- Distribution plots
- Cohort statistics

### Tab 3: Individual Analysis
- Select a specific student
- View their burnout score and risk level
- See factor contribution breakdown
- Check peer percentile ranking
- Review risk indicators

### Tab 4: What-If Scenarios
- Test lifestyle changes
- Adjust sleep hours or screen time
- See predicted impact on burnout score
- Compare multiple scenarios

### Tab 5: Methodology
- Read full statistical methodology
- Understand risk thresholds
- Review model transparency
- Check Domain-2 compliance

---

## 📝 CSV Template

Create a CSV file like this:

```csv
name,sleep_hours,study_hours,screen_time,stress_level,attendance
Student 1,6.5,8,5,4,90
Student 2,7,6,3,2,95
Student 3,5,10,7,5,75
```

Save it and upload through the app!

---

## 🎯 Understanding Results

### Burnout Score
- **0.00 - 0.29**: 🟢 Low Risk - Healthy patterns
- **0.30 - 0.59**: 🟡 Moderate Risk - Some concerns
- **0.60 - 1.00**: 🔴 Elevated Risk - Multiple risk factors

### Factor Contributions
Shows which factors contribute most to the risk score:
- Higher percentage = bigger impact
- Focus interventions on top contributors

### What-If Scenarios
- **Negative change**: Good! Risk decreases
- **Positive change**: Bad! Risk increases
- **Near zero**: Minimal impact

---

## 💡 Tips

1. **Start with sample data** to understand the interface
2. **Upload multiple students** to see statistical analysis
3. **Use what-if scenarios** to plan interventions
4. **Check methodology tab** for full transparency
5. **Export results** by taking screenshots or copying data

---

## ❓ Troubleshooting

**App won't start?**
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version: 3.8 or higher required

**CSV upload fails?**
- Verify column names match exactly (case-sensitive)
- Check that values are in valid ranges
- Ensure no missing data

**Charts not showing?**
- Refresh the page
- Check browser console for errors
- Try a different browser

---

## 📞 Need Help?

- Read the full README.md for detailed documentation
- Check METHODOLOGY.md for statistical details
- Review inline code comments for technical details

---

**Ready to start? Run `streamlit run app.py` and explore!** 🌱
