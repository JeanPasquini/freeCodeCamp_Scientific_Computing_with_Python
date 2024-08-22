def add_time(start, duration, start_day=None):
    
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    start_hour, start_minute = map(int, start[:-3].split(':'))
    period = start[-2:]

    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0

    duration_hour, duration_minute = map(int, duration.split(':'))

    end_minute = start_minute + duration_minute
    extra_hour = end_minute // 60
    end_minute %= 60
    end_hour = start_hour + duration_hour + extra_hour
    days_later = end_hour // 24
    end_hour %= 24

    if end_hour == 0:
        final_hour = 12
        final_period = "AM"
    elif end_hour < 12:
        final_hour = end_hour
        final_period = "AM"
    elif end_hour == 12:
        final_hour = 12
        final_period = "PM"
    else:
        final_hour = end_hour - 12
        final_period = "PM"

    if start_day:
        day_index = days_of_week.index(start_day.capitalize())
        new_day_index = (day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        day_output = f", {new_day}"
    else:
        day_output = ""

    if days_later == 1:
        days_output = " (next day)"
    elif days_later > 1:
        days_output = f" ({days_later} days later)"
    else:
        days_output = ""

    new_time = f"{final_hour}:{end_minute:02d} {final_period}{day_output}{days_output}"
    return new_time

