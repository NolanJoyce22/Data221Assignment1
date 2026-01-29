def seconds_past_midnight_to_hours_minutes_and_seconds(seconds_past):
    #Initialize boundaries
    if seconds_past < 0 or seconds_past >= 86400:
        return "Invalid input"

    #Convert to the desired units using seconds
    hours = seconds_past // 3600
    minutes = (seconds_past % 3600) // 60
    seconds = seconds_past % 60

    #Initialize AM or PM
    if hours < 12:
        am_pm = "AM"

    else:
        am_pm = "PM"

    hours = hours % 12
    if hours == 0:
        hours = 12

    return f"{hours:02d}:{minutes:02d}:{seconds:02d} {am_pm}"

print(seconds_past_midnight_to_hours_minutes_and_seconds(3661))



