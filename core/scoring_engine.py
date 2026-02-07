from config import WEIGHTS

def burnout_score(row):
    # Handle both dictionary-style (CSV) and attribute-style (manual) access
    sleep_hours = row['sleep_hours'] if isinstance(row, dict) or 'sleep_hours' in row.index else row.sleep_hours
    stress_level = row['stress_level'] if isinstance(row, dict) or 'stress_level' in row.index else row.stress_level
    screen_time = row['screen_time'] if isinstance(row, dict) or 'screen_time' in row.index else row.screen_time
    study_hours = row['study_hours'] if isinstance(row, dict) or 'study_hours' in row.index else row.study_hours
    attendance = row['attendance'] if isinstance(row, dict) or 'attendance' in row.index else row.attendance
    
    sleep_deficit = max(0, (7 - sleep_hours) / 7)
    stress = stress_level / 5
    screen = screen_time / 10
    study = study_hours / 10
    attendance_risk = (100 - attendance) / 100

    score = (
        WEIGHTS["sleep"] * sleep_deficit +
        WEIGHTS["stress"] * stress +
        WEIGHTS["screen"] * screen +
        WEIGHTS["study"] * study +
        WEIGHTS["attendance"] * attendance_risk
    )

    return round(min(score, 1), 2)

def risk_label(score):
    """
    Risk threshold definitions based on statistical distribution:
    - Low Risk: < 0.30 (Bottom tertile)
    - Moderate Risk: 0.30 - 0.60 (Middle tertile)
    - Elevated Risk: >= 0.60 (Top tertile)
    """
    if score < 0.3:
        return "🟢 Low Risk"
    elif score < 0.6:
        return "🟡 Moderate Risk"
    return "🔴 Elevated Risk"

def get_statistical_summary():
    """Return model configuration for transparency"""
    return {
        "weights": WEIGHTS,
        "thresholds": {
            "low_risk": "< 0.30",
            "moderate_risk": "0.30 - 0.60",
            "elevated_risk": ">= 0.60"
        },
        "normalization": {
            "sleep": "max(0, (7 - sleep_hours) / 7)",
            "stress": "stress_level / 5",
            "screen": "screen_time / 10",
            "study": "study_hours / 10",
            "attendance": "(100 - attendance) / 100"
        }
    }
