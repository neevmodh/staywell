def validate_row(row):
    # Handle both dictionary-style (CSV) and attribute-style (manual) access
    if isinstance(row.get('sleep_hours'), (int, float)):
        row['sleep_hours'] = min(max(row['sleep_hours'], 0), 24)
        row['study_hours'] = min(max(row['study_hours'], 0), 24)
        row['screen_time'] = min(max(row['screen_time'], 0), 24)
        row['stress_level'] = min(max(row['stress_level'], 1), 5)
        row['attendance'] = min(max(row['attendance'], 0), 100)
        
        # 24-hour constraint
        total_hours = row['sleep_hours'] + row['study_hours'] + row['screen_time']
        row['valid'] = total_hours <= 24
    else:
        row.sleep_hours = min(max(row.sleep_hours, 0), 24)
        row.study_hours = min(max(row.study_hours, 0), 24)
        row.screen_time = min(max(row.screen_time, 0), 24)
        row.stress_level = min(max(row.stress_level, 1), 5)
        row.attendance = min(max(row.attendance, 0), 100)
        
        # 24-hour constraint
        total_hours = row.sleep_hours + row.study_hours + row.screen_time
        row.valid = total_hours <= 24
    
    return row
