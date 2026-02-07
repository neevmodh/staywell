from config import WEIGHTS

def contribution(row):
    # Handle both dictionary-style (CSV) and attribute-style (manual) access
    sleep_hours = row['sleep_hours'] if isinstance(row, dict) or 'sleep_hours' in row.index else row.sleep_hours
    stress_level = row['stress_level'] if isinstance(row, dict) or 'stress_level' in row.index else row.stress_level
    screen_time = row['screen_time'] if isinstance(row, dict) or 'screen_time' in row.index else row.screen_time
    study_hours = row['study_hours'] if isinstance(row, dict) or 'study_hours' in row.index else row.study_hours
    attendance = row['attendance'] if isinstance(row, dict) or 'attendance' in row.index else row.attendance
    
    factors = {
        "Sleep": WEIGHTS["sleep"] * max(0, (7 - sleep_hours) / 7),
        "Stress": WEIGHTS["stress"] * (stress_level / 5),
        "Screen": WEIGHTS["screen"] * (screen_time / 10),
        "Study": WEIGHTS["study"] * (study_hours / 10),
        "Attendance": WEIGHTS["attendance"] * ((100 - attendance) / 100),
    }
    total = sum(factors.values())
    return {k: round(v / total * 100, 1) for k, v in factors.items()}
