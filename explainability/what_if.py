from core.scoring_engine import burnout_score
import pandas as pd

def simulate(row, sleep_delta=0, screen_delta=0):
    """
    Simulate impact of lifestyle changes on burnout score
    """
    # Create a copy to avoid modifying original
    if isinstance(row, pd.Series):
        row_copy = row.copy()
        row_copy['sleep_hours'] = max(0, min(24, row_copy['sleep_hours'] + sleep_delta))
        row_copy['screen_time'] = max(0, min(24, row_copy['screen_time'] + screen_delta))
    else:
        row_copy = row.copy()
        row_copy.sleep_hours = max(0, min(24, row_copy.sleep_hours + sleep_delta))
        row_copy.screen_time = max(0, min(24, row_copy.screen_time + screen_delta))
    return burnout_score(row_copy)

def batch_simulate(row):
    """
    Run multiple what-if scenarios and return results
    """
    current_score = burnout_score(row)
    
    scenarios = [
        {"scenario": "Current State", "sleep_delta": 0, "screen_delta": 0},
        {"scenario": "+1 hour sleep", "sleep_delta": 1, "screen_delta": 0},
        {"scenario": "+2 hours sleep", "sleep_delta": 2, "screen_delta": 0},
        {"scenario": "-1 hour screen time", "sleep_delta": 0, "screen_delta": -1},
        {"scenario": "-2 hours screen time", "sleep_delta": 0, "screen_delta": -2},
        {"scenario": "+1 sleep, -1 screen", "sleep_delta": 1, "screen_delta": -1},
        {"scenario": "+2 sleep, -2 screen", "sleep_delta": 2, "screen_delta": -2},
    ]
    
    results = []
    for s in scenarios:
        new_score = simulate(row, s["sleep_delta"], s["screen_delta"])
        results.append({
            "scenario": s["scenario"],
            "new_score": round(new_score, 2),
            "change": round(new_score - current_score, 2)
        })
    
    return pd.DataFrame(results)
