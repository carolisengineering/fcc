def toggle_label(label):
    if label == "AM":
        return "PM"
    if label == "PM":
        return "AM"

def add_time(start, duration, day=None):
    days_later = 0
    new_day = ""
    day_of_week = ""
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    days_upper = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]

    if duration == "0:00":
        return start

    start_time_parts = start.split()
    time = start_time_parts[0]
    label = start_time_parts[1]

    time_parts = time.split(":")
    hour = int(time_parts[0])
    minute = int(time_parts[1])

    duration_parts = duration.split(":")
    duration_hours = int(duration_parts[0])
    duration_minutes = int(duration_parts[1])

    new_minute = minute + duration_minutes
    if new_minute >= 60:
        new_minute = new_minute - 60
        hour += 1

    new_hour = hour + duration_hours
    while new_hour >= 12:
        new_hour = new_hour - 12
        label = toggle_label(label)
        if label == "AM":
            days_later += 1
    
    if new_hour == 0:
        new_hour = 12

    if day:
        current_index = days_upper.index(day.upper())
        new_index = (current_index + days_later) % 7
        day_of_week = days[new_index]


    if days_later == 1:
        new_day = " (next day)"
    elif days_later > 1:
        new_day = f" ({days_later} days later)"

    if new_minute < 10:
        new_minute = f"0{new_minute}"

    if day_of_week != "":
        new_time = str(new_hour) + ":" + str(new_minute) + f" {label}" + f", {day_of_week}" + new_day
    else:
        new_time = str(new_hour) + ":" + str(new_minute) + f" {label}" + new_day
    

    return new_time