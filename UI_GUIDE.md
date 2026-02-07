# 🎨 UI Guide - STAYWELL Dashboard

## Interface Overview

The STAYWELL application features a modern, intuitive interface with 5 main tabs for comprehensive burnout analysis.

---

## Main Header

```
🌱 STAYWELL – Early Statistical Detection of Academic Burnout
Pure Statistical Analysis | Domain-2 Compliant | No ML Black-Box
```

**Features**:
- Gradient header (green to blue)
- Clear project title
- Compliance badges

---

## Sidebar Configuration

### Input Type Selection
Three radio button options:
1. **Upload CSV** - Batch analysis
2. **Manual Entry** - Single student
3. **Use Sample Data** - Demo mode

### Manual Entry Form (when selected)
- Name (text input)
- Sleep Hours (0-24, step 0.5)
- Study Hours (0-24, step 0.5)
- Screen Time (0-24, step 0.5)
- Stress Level (1-5 slider)
- Attendance (0-100% slider)

---

## Tab 1: 📊 Overview

### Top Metrics Row
Four metric cards displaying:
- **Total Students**: Count
- **🔴 High Risk**: Count + percentage
- **🟡 Moderate Risk**: Count + percentage
- **🟢 Low Risk**: Count + percentage

### Student Risk Assessment Table
Columns:
- Name
- Sleep Hours
- Study Hours
- Screen Time
- Stress Level
- Attendance
- Burnout Score
- Risk Level (with emoji indicators)

### Risk Distribution Chart
- Pie chart showing percentage breakdown
- Color-coded: Green (Low), Yellow (Moderate), Red (High)
- Percentage labels on each slice

---

## Tab 2: 📈 Statistical Analysis

### Descriptive Statistics Table
Full statistical summary for all variables:
- Count, Mean, Median
- Standard Deviation, Variance
- Min, Q1, Q2, Q3, Max

### Correlation Analysis
**Left Column**: Correlation matrix table
- Numerical correlation values
- Color gradient (red = negative, green = positive)

**Right Column**: Correlation heatmap
- Visual representation
- Annotated with values
- Color-coded intensity

### Variable Distributions
Grid of histograms (2x3 layout):
- One histogram per variable
- Mean line (red dashed)
- Median line (blue dashed)
- Frequency on Y-axis

### Cohort Statistics
Three columns of metrics:
- Mean, Median
- Standard Deviation, Variance
- Min, Max

---

## Tab 3: 🔍 Individual Analysis

### Student Selection
Dropdown menu to select specific student

### Top Metrics Row
Three key metrics:
- **Burnout Score**: 0.00-1.00 scale
- **Risk Level**: Color-coded emoji
- **Peer Percentile**: Comparison ranking

### Two-Column Layout

**Left Column - Risk Factor Contribution**:
- Bar chart showing factor percentages
- Color-coded bars
- Value labels on top
- Interpretation text below

**Right Column - Student Profile**:
- Bullet list of all input values
- Risk indicators section
- Warning messages for concerning values:
  - ⚠️ Sleep deprivation (< 6 hours)
  - ⚠️ High stress (≥ 4)
  - ⚠️ Excessive screen time (> 6 hours)
  - ⚠️ Low attendance (< 75%)
  - ⚠️ Excessive study (> 10 hours)

---

## Tab 4: 🔮 What-If Scenarios

### Student Selection
Dropdown for scenario testing

### Current Score Display
Large metric showing baseline burnout score

### Two-Column Adjustment Panel

**Left Column - Sleep Adjustment**:
- Slider: -3 to +3 hours
- New score metric
- Delta indicator (positive/negative)
- Impact message (positive/negative/minimal)

**Right Column - Screen Time Adjustment**:
- Slider: -3 to +3 hours
- New score metric
- Delta indicator
- Impact message

### Batch Scenario Testing
Table showing multiple scenarios:
- Scenario description
- New score
- Change from baseline
- Best scenario highlighted

---

## Tab 5: 📋 Methodology

### Comprehensive Documentation
Sections include:
1. **Statistical Model**
   - Formula and approach
   - Risk factors table
   - Normalization methods

2. **Risk Thresholds**
   - Three-tier system
   - Threshold values
   - Rationale

3. **Statistical Techniques**
   - Descriptive statistics
   - Correlation analysis
   - Percentile analysis
   - Sensitivity analysis
   - Factor contribution

4. **Validation & Constraints**
   - Input validation
   - Model validation
   - Ethical considerations

5. **Domain-2 Compliance**
   - Checklist of requirements
   - Compliance verification

6. **Current Model Statistics**
   - JSON display of weights
   - JSON display of thresholds

---

## Color Scheme

### Primary Colors
- **Primary Green**: #0F9D58 (main brand color)
- **Secondary Blue**: #1A73E8 (accent color)

### Risk Colors
- **Low Risk**: 🟢 #0F9D58 (Green)
- **Moderate Risk**: 🟡 #F4B400 (Yellow)
- **Elevated Risk**: 🔴 #DB4437 (Red)

### Chart Colors
- Bar charts: Multi-color palette
- Heatmaps: Red-Yellow-Green gradient
- Histograms: Green with transparency

---

## Interactive Elements

### Buttons & Controls
- Radio buttons for input type
- File uploader for CSV
- Number inputs with step controls
- Sliders with real-time updates
- Dropdown selectors
- Tab navigation

### Dynamic Updates
- Instant calculation on input change
- Real-time chart updates
- Responsive layout
- Smooth transitions

---

## Responsive Design

### Wide Layout
- Full-width tables
- Multi-column layouts
- Side-by-side comparisons
- Expanded visualizations

### Mobile Considerations
- Streamlit handles responsive design
- Tables scroll horizontally
- Charts resize automatically
- Sidebar collapses on mobile

---

## Footer

```
🌱 STAYWELL - Domain 2: Data & Statistical Modelling
Pure Statistical Analysis | No ML Black-Box | Ethical & Explainable
```

---

## User Experience Features

### Visual Feedback
- ✅ Success messages (green)
- ⚠️ Warning indicators (yellow)
- ❌ Error messages (red)
- ℹ️ Info boxes (blue)

### Data Visualization
- Clean, professional charts
- Clear axis labels
- Value annotations
- Legend when needed
- Grid lines for readability

### Navigation
- Clear tab labels with emojis
- Logical information flow
- Consistent layout across tabs
- Easy-to-find controls

### Accessibility
- High contrast colors
- Clear typography
- Descriptive labels
- Help text on inputs
- Emoji indicators for quick scanning

---

## Performance

### Loading Speed
- Instant calculations
- Fast chart rendering
- Efficient data processing
- No lag on interactions

### Data Handling
- Supports 1-1000+ students
- Efficient pandas operations
- Cached computations
- Optimized visualizations

---

## Best Practices Implemented

✅ **Clarity**: Clear labels and descriptions
✅ **Consistency**: Uniform design across tabs
✅ **Feedback**: Immediate visual responses
✅ **Simplicity**: Intuitive navigation
✅ **Professional**: Clean, modern aesthetic
✅ **Informative**: Rich data presentation
✅ **Accessible**: Easy to understand
✅ **Responsive**: Adapts to screen size

---

## Tips for Best Experience

1. **Start with Overview tab** to see big picture
2. **Explore Statistical Analysis** for deeper insights
3. **Select individual students** for detailed breakdown
4. **Test what-if scenarios** to plan interventions
5. **Review methodology** for transparency
6. **Use sample data** to learn the interface
7. **Upload your CSV** for real analysis

---

**The UI is designed to be intuitive, informative, and professional - perfect for academic presentations and real-world use!** 🎨
