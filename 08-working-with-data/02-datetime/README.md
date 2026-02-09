# Datetime

## Objective

Learn how to work with dates, times, and durations in Python using the `datetime` module. You'll be able to create dates, format them, parse them from strings, do date math, and handle timezones.

## Concepts Covered

- The `datetime` module — `date`, `time`, `datetime`, `timedelta`
- Creating date and datetime objects
- Getting current date/time with `date.today()`, `datetime.now()`, `datetime.utcnow()`
- Formatting dates with `strftime()` (common format codes)
- Parsing strings to dates with `strptime()`
- Date arithmetic with `timedelta`
- Comparing dates
- Timezones with `timezone` and `zoneinfo`
- Timestamps: `datetime.timestamp()` and `datetime.fromtimestamp()`
- The `calendar` module (brief intro)
- Common patterns: age calculation, days until event, date ranges

## Prerequisites

- Basic Python syntax (variables, strings, f-strings)
- Functions and imports

## Lesson

### The datetime Module

Python's `datetime` module is your toolbox for anything date- or time-related. It lives in the standard library, so there's nothing to install. It gives you four main types:

```python
from datetime import date, time, datetime, timedelta
```

| Type        | What It Represents              | Example                  |
|-------------|----------------------------------|--------------------------|
| `date`      | A calendar date (year, month, day) | `date(2025, 3, 15)`    |
| `time`      | A time of day (hour, minute, second) | `time(14, 30, 0)`    |
| `datetime`  | A date AND time combined         | `datetime(2025, 3, 15, 14, 30)` |
| `timedelta` | A duration (difference between two dates/times) | `timedelta(days=7)` |

You'll use `datetime` and `timedelta` the most. The `date` type is handy when you only care about the calendar date and not the clock time.

### Creating Date and Datetime Objects

You create them by passing in the parts you need:

```python
from datetime import date, time, datetime

# Just a date — year, month, day
birthday = date(1990, 6, 15)
print(birthday)  # 1990-06-15

# Just a time — hour, minute, second (all optional after hour)
lunch = time(12, 30)
print(lunch)  # 12:30:00

# Date + time combined
appointment = datetime(2025, 3, 15, 14, 30, 0)
print(appointment)  # 2025-03-15 14:30:00
```

You can also pull the individual parts back out:

```python
print(birthday.year)    # 1990
print(birthday.month)   # 6
print(birthday.day)     # 15
print(appointment.hour) # 14
```

### Getting the Current Date and Time

This is probably the most common thing you'll do:

```python
from datetime import date, datetime

# Today's date (no time info)
today = date.today()
print(today)  # e.g., 2025-02-09

# Right now, with time included
now = datetime.now()
print(now)  # e.g., 2025-02-09 14:30:45.123456

# UTC time (no timezone offset applied)
utc_now = datetime.utcnow()
print(utc_now)
```

**Heads up:** `datetime.utcnow()` gives you a "naive" datetime — it has no timezone info attached. For timezone-aware code, you'll want `datetime.now(timezone.utc)` instead. More on that below.

### Formatting Dates with strftime()

`strftime()` stands for "string format time." It turns a date or datetime into a string using format codes:

```python
from datetime import datetime

now = datetime.now()

print(now.strftime("%Y-%m-%d"))          # 2025-02-09
print(now.strftime("%B %d, %Y"))         # February 09, 2025
print(now.strftime("%A, %B %d"))         # Sunday, February 09
print(now.strftime("%I:%M %p"))          # 02:30 PM
print(now.strftime("%Y-%m-%d %H:%M:%S")) # 2025-02-09 14:30:45
```

Here are the format codes you'll use the most:

| Code | Meaning             | Example    |
|------|----------------------|------------|
| `%Y` | 4-digit year        | `2025`     |
| `%m` | Month (zero-padded) | `02`       |
| `%d` | Day (zero-padded)   | `09`       |
| `%H` | Hour (24-hour)      | `14`       |
| `%I` | Hour (12-hour)      | `02`       |
| `%M` | Minute              | `30`       |
| `%S` | Second              | `45`       |
| `%A` | Full weekday name   | `Sunday`   |
| `%a` | Short weekday name  | `Sun`      |
| `%B` | Full month name     | `February` |
| `%b` | Short month name    | `Feb`      |
| `%p` | AM/PM               | `PM`       |

### Parsing Strings to Dates with strptime()

`strptime()` is the reverse — it takes a string and a format, and gives you a datetime:

```python
from datetime import datetime

# Parse a date string
date_str = "2025-03-15"
parsed = datetime.strptime(date_str, "%Y-%m-%d")
print(parsed)  # 2025-03-15 00:00:00

# Parse a more complex format
date_str2 = "March 15, 2025 at 2:30 PM"
parsed2 = datetime.strptime(date_str2, "%B %d, %Y at %I:%M %p")
print(parsed2)  # 2025-03-15 14:30:00
```

**Common gotcha:** The format string must match the input *exactly*. If your string has a comma somewhere, the format string needs a comma in the same spot. If the match fails, you get a `ValueError`.

### Date Arithmetic with timedelta

`timedelta` represents a duration — a span of time. You can add or subtract them from dates:

```python
from datetime import datetime, timedelta

now = datetime.now()

# Add 7 days
next_week = now + timedelta(days=7)

# Subtract 30 days
last_month = now - timedelta(days=30)

# More granular durations
shift = timedelta(hours=8, minutes=30)
end_time = now + shift

# Subtracting two datetimes gives you a timedelta
start = datetime(2025, 1, 1)
end = datetime(2025, 12, 31)
duration = end - start
print(duration)        # 364 days, 0:00:00
print(duration.days)   # 364
```

You can create `timedelta` with any combination of: `days`, `seconds`, `microseconds`, `milliseconds`, `minutes`, `hours`, `weeks`.

### Comparing Dates

Dates support all the comparison operators you'd expect:

```python
from datetime import date

birthday = date(1990, 6, 15)
today = date.today()

print(today > birthday)   # True — today is after the birthday
print(today == birthday)  # False (unless it's your birthday!)
print(today < birthday)   # False

# Useful for "is this date in the past/future?"
deadline = date(2025, 12, 31)
if today < deadline:
    print("Still have time!")
else:
    print("Deadline passed!")
```

### Timezones

Timezones are tricky, but Python 3.9+ makes them much easier with the `zoneinfo` module:

```python
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

# UTC time (timezone-aware)
utc_now = datetime.now(timezone.utc)
print(utc_now)  # 2025-02-09 19:30:00+00:00

# Specific timezone
eastern = ZoneInfo("America/New_York")
ny_time = datetime.now(eastern)
print(ny_time)  # 2025-02-09 14:30:00-05:00

# Convert between timezones
tokyo_time = ny_time.astimezone(ZoneInfo("Asia/Tokyo"))
print(tokyo_time)  # 2025-02-10 04:30:00+09:00
```

**Naive vs. Aware:**
- A **naive** datetime has no timezone info (what you get from `datetime.now()` by default).
- An **aware** datetime knows its timezone. Always prefer aware datetimes when your code deals with multiple timezones.

### Timestamps

A timestamp is a number — the number of seconds since January 1, 1970 (the "Unix epoch"). It's how computers usually store time under the hood:

```python
from datetime import datetime

now = datetime.now()

# Convert datetime to timestamp (float)
ts = now.timestamp()
print(ts)  # e.g., 1739125845.123456

# Convert timestamp back to datetime
restored = datetime.fromtimestamp(ts)
print(restored)

# UTC version
from datetime import timezone
utc_restored = datetime.fromtimestamp(ts, tz=timezone.utc)
```

Timestamps are super useful when working with APIs, databases, or log files.

### The calendar Module

Python also has a `calendar` module for calendar-related utilities:

```python
import calendar

# Is it a leap year?
print(calendar.isleap(2024))  # True
print(calendar.isleap(2025))  # False

# How many days in a month?
print(calendar.monthrange(2025, 2))  # (5, 28) — starts on Saturday, 28 days

# What day of the week? (0=Monday, 6=Sunday)
print(calendar.weekday(2025, 2, 9))  # 6 (Sunday)

# Print a month
calendar.prmonth(2025, 2)
```

### Common Patterns

Here are some patterns you'll reach for again and again:

**Age calculation:**

```python
from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    # Subtract 1 if birthday hasn't happened yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age
```

**Days until an event:**

```python
from datetime import date

event = date(2025, 12, 25)
days_left = (event - date.today()).days
print(f"{days_left} days until Christmas!")
```

**Generating a date range:**

```python
from datetime import date, timedelta

start = date(2025, 1, 1)
end = date(2025, 1, 7)
current = start
while current <= end:
    print(current)
    current += timedelta(days=1)
```

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- Use `date` for calendar dates, `datetime` when you need time too, and `timedelta` for durations
- `strftime()` formats dates into strings; `strptime()` parses strings into dates — "f" for format, "p" for parse
- Date arithmetic is intuitive: add/subtract `timedelta` from dates, or subtract two dates to get a `timedelta`
- Dates support `>`, `<`, `==` for comparisons
- Use `zoneinfo.ZoneInfo` (Python 3.9+) for timezone-aware datetimes
- `datetime.timestamp()` and `datetime.fromtimestamp()` convert to/from Unix timestamps
- The `calendar` module has handy utilities like `isleap()` and `monthrange()`
- Always prefer timezone-aware datetimes when your code crosses timezone boundaries
