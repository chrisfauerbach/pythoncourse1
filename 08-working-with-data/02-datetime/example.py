"""
Datetime — Example Code
=========================

Run this file:
    python3 example.py

This file walks through Python's datetime module — creating dates, formatting
them, parsing strings, doing date math, working with timezones, and more.
"""

from datetime import date, time, datetime, timedelta, timezone
from zoneinfo import ZoneInfo
import calendar

# -----------------------------------------------------------------------------
# 1. Creating date and datetime objects
# -----------------------------------------------------------------------------

# A date is just year, month, day
birthday = date(1990, 6, 15)
print("Birthday:", birthday)  # 1990-06-15

# A time is hour, minute, second (minute and second are optional)
lunch = time(12, 30)
alarm = time(7, 0, 0)
print("Lunch time:", lunch)   # 12:30:00
print("Alarm:", alarm)        # 07:00:00

# A datetime combines both date and time
appointment = datetime(2025, 3, 15, 14, 30, 0)
print("Appointment:", appointment)  # 2025-03-15 14:30:00

# You can access individual parts of any date or datetime
print("Year:", birthday.year)     # 1990
print("Month:", birthday.month)   # 6
print("Day:", birthday.day)       # 15
print("Hour:", appointment.hour)  # 14

# -----------------------------------------------------------------------------
# 2. Getting the current date and time
# -----------------------------------------------------------------------------

# Today's date — no time information
today = date.today()
print("\nToday's date:", today)

# Current date AND time (local timezone, but "naive" — no tz info attached)
now = datetime.now()
print("Right now:", now)

# Current UTC time — timezone-aware (the recommended way)
utc_now = datetime.now(timezone.utc)
print("UTC now:", utc_now)

# You can extract the date or time from a datetime
print("Date part:", now.date())
print("Time part:", now.time())

# -----------------------------------------------------------------------------
# 3. Formatting dates with strftime() — "string format time"
# -----------------------------------------------------------------------------

print("\n--- Formatting dates ---")

# ISO format: YYYY-MM-DD
print(now.strftime("%Y-%m-%d"))

# Human-readable: "February 09, 2025"
print(now.strftime("%B %d, %Y"))

# Day of week: "Sunday, February 09"
print(now.strftime("%A, %B %d"))

# 12-hour clock: "02:30 PM"
print(now.strftime("%I:%M:%S %p"))

# Full timestamp: "2025-02-09 14:30:45"
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Short month and weekday names
print(now.strftime("%a, %b %d"))  # e.g., "Sun, Feb 09"

# You can mix in any text you want
print(now.strftime("Today is %A and the month is %B"))

# -----------------------------------------------------------------------------
# 4. Parsing strings to dates with strptime() — "string parse time"
# -----------------------------------------------------------------------------

print("\n--- Parsing strings to dates ---")

# Parse an ISO date string
date_str = "2025-03-15"
parsed = datetime.strptime(date_str, "%Y-%m-%d")
print(f"Parsed '{date_str}' -> {parsed}")

# Parse a US-style date
us_date = "03/15/2025"
parsed_us = datetime.strptime(us_date, "%m/%d/%Y")
print(f"Parsed '{us_date}' -> {parsed_us}")

# Parse a European-style date
eu_date = "15-03-2025"
parsed_eu = datetime.strptime(eu_date, "%d-%m-%Y")
print(f"Parsed '{eu_date}' -> {parsed_eu}")

# Parse a date with time
full_str = "March 15, 2025 at 2:30 PM"
parsed_full = datetime.strptime(full_str, "%B %d, %Y at %I:%M %p")
print(f"Parsed '{full_str}' -> {parsed_full}")

# Parse and re-format — a very common pattern
raw = "20250315"
reformatted = datetime.strptime(raw, "%Y%m%d").strftime("%B %d, %Y")
print(f"Reformatted '{raw}' -> '{reformatted}'")

# -----------------------------------------------------------------------------
# 5. Date arithmetic with timedelta
# -----------------------------------------------------------------------------

print("\n--- Date arithmetic ---")

# Add days to a date
one_week_later = today + timedelta(days=7)
print(f"One week from today: {one_week_later}")

# Subtract days
thirty_days_ago = today - timedelta(days=30)
print(f"30 days ago: {thirty_days_ago}")

# More granular: hours, minutes, seconds
meeting_start = datetime(2025, 3, 15, 9, 0, 0)
meeting_end = meeting_start + timedelta(hours=1, minutes=30)
print(f"Meeting: {meeting_start.strftime('%H:%M')} - {meeting_end.strftime('%H:%M')}")

# Weeks work too
two_weeks = timedelta(weeks=2)
print(f"Two weeks from today: {today + two_weeks}")

# Subtracting two dates gives you a timedelta
new_year = date(2025, 1, 1)
new_year_eve = date(2025, 12, 31)
year_span = new_year_eve - new_year
print(f"Days in 2025 (Jan 1 to Dec 31): {year_span.days}")

# You can get total seconds from a timedelta
work_shift = timedelta(hours=8, minutes=30)
print(f"Work shift: {work_shift}")
print(f"That's {work_shift.total_seconds()} seconds")
print(f"Or {work_shift.total_seconds() / 3600:.1f} hours")

# -----------------------------------------------------------------------------
# 6. Comparing dates
# -----------------------------------------------------------------------------

print("\n--- Comparing dates ---")

date_a = date(2025, 1, 1)
date_b = date(2025, 6, 15)
date_c = date(2025, 1, 1)

print(f"{date_a} < {date_b}?  {date_a < date_b}")   # True
print(f"{date_a} > {date_b}?  {date_a > date_b}")   # False
print(f"{date_a} == {date_c}? {date_a == date_c}")   # True

# A practical example: is a deadline in the future?
deadline = date(2025, 12, 31)
if today <= deadline:
    days_remaining = (deadline - today).days
    print(f"Deadline is in {days_remaining} days — still on track!")
else:
    days_overdue = (today - deadline).days
    print(f"Deadline passed {days_overdue} days ago!")

# Sorting a list of dates
dates = [date(2025, 12, 25), date(2025, 1, 1), date(2025, 7, 4), date(2025, 2, 14)]
sorted_dates = sorted(dates)
print("Sorted:", [d.strftime("%b %d") for d in sorted_dates])

# -----------------------------------------------------------------------------
# 7. Timezones with timezone and zoneinfo (Python 3.9+)
# -----------------------------------------------------------------------------

print("\n--- Timezones ---")

# UTC — the reference timezone, offset of +00:00
utc_time = datetime.now(timezone.utc)
print(f"UTC:      {utc_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")

# Specific timezones using ZoneInfo
eastern = ZoneInfo("America/New_York")
pacific = ZoneInfo("America/Los_Angeles")
london = ZoneInfo("Europe/London")
tokyo = ZoneInfo("Asia/Tokyo")

# Get current time in different cities
print(f"New York: {datetime.now(eastern).strftime('%Y-%m-%d %H:%M:%S %Z')}")
print(f"Pacific:  {datetime.now(pacific).strftime('%Y-%m-%d %H:%M:%S %Z')}")
print(f"London:   {datetime.now(london).strftime('%Y-%m-%d %H:%M:%S %Z')}")
print(f"Tokyo:    {datetime.now(tokyo).strftime('%Y-%m-%d %H:%M:%S %Z')}")

# Convert between timezones — schedule a meeting in NY, what time in Tokyo?
ny_meeting = datetime(2025, 3, 15, 10, 0, tzinfo=eastern)
tokyo_meeting = ny_meeting.astimezone(tokyo)
print(f"\nMeeting at {ny_meeting.strftime('%I:%M %p %Z')}"
      f" = {tokyo_meeting.strftime('%I:%M %p %Z')} (next day: {tokyo_meeting.day != ny_meeting.day})")

# Check if a datetime is naive or aware
naive_dt = datetime.now()
aware_dt = datetime.now(timezone.utc)
print(f"\nNaive (no tzinfo): {naive_dt.tzinfo}")
print(f"Aware (has tzinfo): {aware_dt.tzinfo}")

# -----------------------------------------------------------------------------
# 8. Timestamps — seconds since the Unix epoch (Jan 1, 1970)
# -----------------------------------------------------------------------------

print("\n--- Timestamps ---")

# Convert a datetime to a timestamp
now_dt = datetime.now()
ts = now_dt.timestamp()
print(f"Current datetime: {now_dt}")
print(f"As timestamp:     {ts}")

# Convert a timestamp back to a datetime
restored = datetime.fromtimestamp(ts)
print(f"Restored:         {restored}")

# You can also get a UTC datetime from a timestamp
restored_utc = datetime.fromtimestamp(ts, tz=timezone.utc)
print(f"Restored (UTC):   {restored_utc}")

# A well-known timestamp: the Unix epoch itself
epoch = datetime.fromtimestamp(0, tz=timezone.utc)
print(f"\nUnix epoch: {epoch}")

# How many seconds since the epoch right now?
print(f"Seconds since epoch: {datetime.now(timezone.utc).timestamp():,.0f}")

# -----------------------------------------------------------------------------
# 9. The calendar module
# -----------------------------------------------------------------------------

print("\n--- The calendar module ---")

# Leap year check
print(f"2024 leap year? {calendar.isleap(2024)}")  # True
print(f"2025 leap year? {calendar.isleap(2025)}")  # False

# monthrange returns (weekday of first day, number of days in month)
first_weekday, num_days = calendar.monthrange(2025, 2)
print(f"February 2025: starts on weekday {first_weekday} (0=Mon), has {num_days} days")

# What day of the week is a specific date? (0=Monday, 6=Sunday)
weekday = calendar.weekday(2025, 12, 25)
day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(f"Christmas 2025 falls on a {day_names[weekday]}")

# How many leap years in a range?
leap_count = calendar.leapdays(2000, 2025)  # from 2000 up to (not including) 2025
print(f"Leap years from 2000 to 2024: {leap_count}")

# Print a whole month
print()
calendar.prmonth(2025, 2)

# -----------------------------------------------------------------------------
# 10. Common patterns
# -----------------------------------------------------------------------------

print("\n--- Common patterns ---")

# Pattern 1: Calculate someone's age
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

sample_birthday = date(1990, 6, 15)
print(f"Born {sample_birthday} -> age {calculate_age(sample_birthday)}")

# Pattern 2: Days until an event
def days_until(target):
    delta = target - date.today()
    return delta.days

next_new_year = date(today.year + 1, 1, 1)
print(f"Days until New Year: {days_until(next_new_year)}")

# Pattern 3: Generate a date range
def date_range(start, end):
    """Yield each date from start through end (inclusive)."""
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)

print("\nFirst week of March 2025:")
for d in date_range(date(2025, 3, 1), date(2025, 3, 7)):
    print(f"  {d.strftime('%A, %B %d')}")

# Pattern 4: Find all Fridays in a month
def fridays_in_month(year, month):
    """Return a list of all Fridays in a given month."""
    _, num_days = calendar.monthrange(year, month)
    return [
        date(year, month, day)
        for day in range(1, num_days + 1)
        if date(year, month, day).weekday() == 4  # 4 = Friday
    ]

print("\nFridays in March 2025:")
for friday in fridays_in_month(2025, 3):
    print(f"  {friday.strftime('%B %d')}")

# -----------------------------------------------------------------------------
# 11. Putting it all together
# -----------------------------------------------------------------------------

print()
print("=" * 50)
print("  DATETIME LESSON COMPLETE!")
print("=" * 50)
print()
print("You now know how to create, format, parse,")
print("compare, and do math with dates in Python.")
print("Try the exercises next!")
