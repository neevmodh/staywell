import streamlit as st
import pandas as pd
import numpy as np

from core.validation import validate_row
from core.scoring_engine import burnout_score, risk_label, get_statistical_summary
from core.peer_engine import peer_percentile, cohort_statistics
from core.statistical_analysis import correlation_analysis, descriptive_statistics
from explainability.contribution import contribution
from explainability.what_if import simulate, batch_simulate
from ui.dashboard import render_contribution, render_correlation_matrix, render_distribution, render_risk_distribution
from ui.theme import PRIMARY, SECONDARY, RISK_COLORS

st.set_page_config(page_title="STAYWELL - Burnout Detection", layout="wide", initial_sidebar_state="expanded")

# Custom CSS
st.markdown(f"""
    <style>
    .main-header {{
        background: linear-gradient(90deg, {PRIMARY} 0%, {SECONDARY} 100%);
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }}
    .metric-card {{
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid {PRIMARY};
    }}
    .stAlert {{
        border-radius: 8px;
    }}
    </style>
""", unsafe_allow_html=True)

st.markdown(
    f"<div class='main-header'><h1 style='color:white; margin:0;'>🌱 STAYWELL – Early Statistical Detection of Academic Burnout</h1><p style='color:white; margin:0; opacity:0.9;'>Pure Statistical Analysis | Domain-2 Compliant | No ML Black-Box</p></div>",
    unsafe_allow_html=True
)

# Sidebar Configuration
st.sidebar.title("⚙️ Configuration")
mode = st.sidebar.radio("📥 Input Type", ["Upload CSV", "Manual Entry", "Use Sample Data"])

# Data Input
if mode == "Upload CSV":
    file = st.sidebar.file_uploader("Upload CSV with columns: sleep_hours, study_hours, screen_time, stress_level, attendance", type=["csv"])
    if not file:
        st.info("👆 Please upload a CSV file to begin analysis")
        st.stop()
    df = pd.read_csv(file)
    if 'name' not in df.columns:
        df['name'] = [f"Student {i+1}" for i in range(len(df))]
        
elif mode == "Use Sample Data":
    df = pd.read_csv("data/sample_students.csv")
    st.sidebar.success("✅ Sample data loaded")
    
else:  # Manual Entry
    st.sidebar.markdown("### 📝 Enter Student Data")
    df = pd.DataFrame([{
        "name": st.sidebar.text_input("Name", "Student 1"),
        "sleep_hours": st.sidebar.number_input("Sleep Hours (0–24)", 0.0, 24.0, 7.0, 0.5, help="Average daily sleep duration"),
        "study_hours": st.sidebar.number_input("Study Hours (0–24)", 0.0, 24.0, 6.0, 0.5, help="Average daily study time"),
        "screen_time": st.sidebar.number_input("Screen Time (0–24)", 0.0, 24.0, 4.0, 0.5, help="Average daily recreational screen time"),
        "stress_level": st.sidebar.slider("Stress Level (1–5)", 1, 5, 3, help="Self-reported stress: 1=Low, 5=High"),
        "attendance": st.sidebar.slider("Attendance (%)", 0, 100, 85, help="Class attendance percentage"),
    }])

# Validate and Process Data
df = df.apply(validate_row, axis=1)
df["burnout_score"] = df.apply(burnout_score, axis=1)
df["risk"] = df["burnout_score"].apply(risk_label)

# Main Dashboard
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Overview", "📈 Statistical Analysis", "🔍 Individual Analysis", "🔮 What-If Scenarios", "📋 Methodology"])

# TAB 1: Overview
with tab1:
    st.header("Burnout Risk Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Students", len(df))
    with col2:
        high_risk = (df["burnout_score"] >= 0.6).sum()
        st.metric("🔴 High Risk", high_risk, delta=f"{high_risk/len(df)*100:.1f}%")
    with col3:
        moderate_risk = ((df["burnout_score"] >= 0.3) & (df["burnout_score"] < 0.6)).sum()
        st.metric("🟡 Moderate Risk", moderate_risk, delta=f"{moderate_risk/len(df)*100:.1f}%")
    with col4:
        low_risk = (df["burnout_score"] < 0.3).sum()
        st.metric("🟢 Low Risk", low_risk, delta=f"{low_risk/len(df)*100:.1f}%")
    
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Student Risk Assessment")
        display_df = df[["name", "sleep_hours", "study_hours", "screen_time", "stress_level", "attendance", "burnout_score", "risk"]].copy()
        display_df["burnout_score"] = display_df["burnout_score"].apply(lambda x: f"{x:.2f}")
        st.dataframe(display_df, use_container_width=True, hide_index=True)
    
    with col2:
        st.subheader("Risk Distribution")
        render_risk_distribution(df)

# TAB 2: Statistical Analysis
with tab2:
    st.header("Statistical Analysis & Correlations")
    
    if len(df) > 1:
        st.subheader("📊 Descriptive Statistics")
        desc_stats = descriptive_statistics(df)
        st.dataframe(desc_stats, use_container_width=True)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🔗 Correlation Analysis")
            corr_data = correlation_analysis(df)
            st.dataframe(corr_data.style.background_gradient(cmap='RdYlGn_r', axis=None), use_container_width=True)
            
        with col2:
            st.subheader("📉 Correlation Heatmap")
            render_correlation_matrix(df)
        
        st.markdown("---")
        st.subheader("📈 Variable Distributions")
        render_distribution(df)
        
        st.markdown("---")
        st.subheader("📊 Cohort Statistics")
        cohort_stats = cohort_statistics(df)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Mean Burnout Score", f"{cohort_stats['mean']:.3f}")
            st.metric("Median Score", f"{cohort_stats['median']:.3f}")
        with col2:
            st.metric("Standard Deviation", f"{cohort_stats['std']:.3f}")
            st.metric("Variance", f"{cohort_stats['variance']:.3f}")
        with col3:
            st.metric("Min Score", f"{cohort_stats['min']:.3f}")
            st.metric("Max Score", f"{cohort_stats['max']:.3f}")
    else:
        st.info("Upload multiple students to see statistical analysis")

# TAB 3: Individual Analysis
with tab3:
    st.header("Individual Student Analysis")
    
    if len(df) > 0:
        student_name = st.selectbox("Select Student", df["name"].tolist())
        idx = df[df["name"] == student_name].index[0]
        row = df.loc[idx]
        
        col1, col2, col3 = st.columns(3)
        with col1:
            score = row["burnout_score"]
            st.metric("Burnout Score", f"{score:.2f}", help="0.0 = No Risk, 1.0 = Maximum Risk")
        with col2:
            st.metric("Risk Level", row["risk"])
        with col3:
            if len(df) > 1:
                percentile = peer_percentile(df["burnout_score"], row["burnout_score"])
                st.metric("Peer Percentile", f"{percentile}%", help="Higher than X% of peers")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🧩 Risk Factor Contribution")
            contrib = contribution(row)
            render_contribution(contrib)
            
            st.markdown("**Interpretation:**")
            top_factor = max(contrib, key=contrib.get)
            st.write(f"• Primary contributor: **{top_factor}** ({contrib[top_factor]}%)")
            st.write(f"• This factor has the highest impact on burnout risk")
        
        with col2:
            st.subheader("📋 Student Profile")
            st.markdown(f"""
            - **Sleep Hours:** {row['sleep_hours']:.1f} hrs/day
            - **Study Hours:** {row['study_hours']:.1f} hrs/day
            - **Screen Time:** {row['screen_time']:.1f} hrs/day
            - **Stress Level:** {int(row['stress_level'])}/5
            - **Attendance:** {int(row['attendance'])}%
            """)
            
            st.markdown("---")
            st.subheader("⚠️ Risk Indicators")
            if row['sleep_hours'] < 6:
                st.warning("⚠️ Sleep deprivation detected (< 6 hours)")
            if row['stress_level'] >= 4:
                st.warning("⚠️ High stress level reported")
            if row['screen_time'] > 6:
                st.warning("⚠️ Excessive screen time (> 6 hours)")
            if row['attendance'] < 75:
                st.warning("⚠️ Low attendance (< 75%)")
            if row['study_hours'] > 10:
                st.warning("⚠️ Excessive study hours (> 10 hours)")
    else:
        st.info("No student data available")

# TAB 4: What-If Scenarios
with tab4:
    st.header("What-If Scenario Analysis")
    
    if len(df) > 0:
        student_name = st.selectbox("Select Student for Simulation", df["name"].tolist(), key="whatif_student")
        idx = df[df["name"] == student_name].index[0]
        row = df.loc[idx]
        
        st.subheader(f"Current Burnout Score: {row['burnout_score']:.2f}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🛏️ Sleep Adjustment")
            sleep_delta = st.slider("Change in sleep hours", -3.0, 3.0, 0.0, 0.5)
            new_sleep_score = simulate(row, sleep_delta=sleep_delta, screen_delta=0)
            delta_sleep = new_sleep_score - row['burnout_score']
            st.metric("New Score", f"{new_sleep_score:.2f}", delta=f"{delta_sleep:+.2f}")
            
            if delta_sleep < -0.05:
                st.success("✅ Positive impact - Risk decreases")
            elif delta_sleep > 0.05:
                st.error("❌ Negative impact - Risk increases")
            else:
                st.info("➡️ Minimal impact")
        
        with col2:
            st.markdown("### 📱 Screen Time Adjustment")
            screen_delta = st.slider("Change in screen time", -3.0, 3.0, 0.0, 0.5)
            new_screen_score = simulate(row, sleep_delta=0, screen_delta=screen_delta)
            delta_screen = new_screen_score - row['burnout_score']
            st.metric("New Score", f"{new_screen_score:.2f}", delta=f"{delta_screen:+.2f}")
            
            if delta_screen < -0.05:
                st.success("✅ Positive impact - Risk decreases")
            elif delta_screen > 0.05:
                st.error("❌ Negative impact - Risk increases")
            else:
                st.info("➡️ Minimal impact")
        
        st.markdown("---")
        st.subheader("🎯 Batch Scenario Testing")
        scenarios = batch_simulate(row)
        st.dataframe(scenarios, use_container_width=True, hide_index=True)
        
        best_scenario = scenarios.loc[scenarios['new_score'].idxmin()]
        st.success(f"**Best Scenario:** {best_scenario['scenario']} → Score: {best_scenario['new_score']:.2f} (Change: {best_scenario['change']:.2f})")
    else:
        st.info("No student data available")

# TAB 5: Methodology
with tab5:
    st.header("Statistical Methodology & Risk Thresholds")
    
    st.markdown("""
    ## 📐 Statistical Model
    
    This system uses **pure statistical techniques** without machine learning, ensuring full transparency and interpretability.
    
    ### Burnout Score Calculation
    
    The burnout score is a **weighted linear combination** of normalized risk factors:
    
    ```
    Burnout Score = Σ (Weight_i × Normalized_Factor_i)
    ```
    
    ### Risk Factors & Weights
    
    | Factor | Weight | Rationale |
    |--------|--------|-----------|
    | Sleep Deficit | 30% | Sleep is the most critical factor for mental health and cognitive function |
    | Stress Level | 20% | Direct indicator of psychological strain |
    | Screen Time | 20% | Proxy for digital fatigue and poor time management |
    | Study Hours | 15% | Excessive studying can lead to burnout |
    | Attendance | 15% | Low attendance indicates disengagement |
    
    ### Normalization Methods
    
    1. **Sleep Deficit**: `max(0, (7 - sleep_hours) / 7)` - Based on 7-hour optimal sleep
    2. **Stress Level**: `stress_level / 5` - Linear scale from 1-5
    3. **Screen Time**: `screen_time / 10` - Normalized against 10-hour reference
    4. **Study Hours**: `study_hours / 10` - Normalized against 10-hour reference
    5. **Attendance**: `(100 - attendance) / 100` - Inverted (lower attendance = higher risk)
    
    ### Risk Thresholds
    
    Based on statistical distribution analysis:
    
    - **🟢 Low Risk**: Score < 0.30 (Bottom 33rd percentile)
    - **🟡 Moderate Risk**: 0.30 ≤ Score < 0.60 (Middle 33rd percentile)
    - **🔴 Elevated Risk**: Score ≥ 0.60 (Top 33rd percentile)
    
    ### Statistical Techniques Used
    
    1. **Descriptive Statistics**: Mean, median, standard deviation, variance
    2. **Correlation Analysis**: Pearson correlation coefficients between variables
    3. **Percentile Analysis**: Peer comparison using empirical distribution
    4. **Sensitivity Analysis**: What-if scenarios to test factor impact
    5. **Factor Contribution**: Proportional decomposition of risk score
    
    ### Validation & Constraints
    
    - ✅ All inputs validated within realistic ranges
    - ✅ No black-box ML models used
    - ✅ Full transparency in calculations
    - ✅ Explainable factor contributions
    - ✅ Statistical correlation analysis
    
    ### Ethical Considerations
    
    - This is an **early warning system**, not a diagnostic tool
    - Results should be used for **guidance and support**, not labeling
    - Human oversight and professional counseling are essential
    - Privacy and confidentiality must be maintained
    
    ### Domain-2 Compliance
    
    ✅ Pure statistical modeling (no ML)  
    ✅ Descriptive analysis included  
    ✅ Correlation analysis implemented  
    ✅ Regression-based scoring  
    ✅ Clear risk threshold definitions  
    ✅ Full methodology documentation  
    ✅ Explainable and transparent  
    """)
    
    st.markdown("---")
    st.subheader("📊 Current Model Statistics")
    summary = get_statistical_summary()
    col1, col2 = st.columns(2)
    with col1:
        st.json(summary["weights"])
    with col2:
        st.json(summary["thresholds"])

# Footer
st.markdown("---")
st.caption("🌱 STAYWELL - Domain 2: Data & Statistical Modelling | Pure Statistical Analysis | No ML Black-Box | Ethical & Explainable")
