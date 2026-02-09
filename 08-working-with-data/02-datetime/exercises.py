"""
Datetime — Exercises
=====================

Practice problems to test your understanding of dates and times in Python.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""

from datetime import date, datetime, timedelta, timezone


# =============================================================================
# Exercise 1: Age in days
#
# Given the birth date below, calculate and print:
#   - The person's age in complete years
#   - The person's age in total days
#
# Expected output format:
#   Age: 34 years
#   Age: 12654 days
#
# Hint: Subtract two date objects to get a timedelta, then use .days
# =============================================================================

def exercise_1():
    birth_date = date(1990, 6, 15)
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Format dates in different styles
#
# Given the date March 15, 2025, print it in all three formats:
#
#   US format:       03/15/2025
#   European format: 15-03-2025
#   ISO format:      2025-03-15
#   Long format:     Saturday, March 15, 2025
#
# Hint: Use strftime() with the right format codes
# =============================================================================

def exercise_2():
    d = date(2025, 3, 15)
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: Parse dates from multiple string formats
#
# You've received dates as strings in different formats (this happens a lot
# in real-world data). Parse each one into a datetime object and print the
# result in ISO format (YYYY-MM-DD).
#
# Input strings:
#   "2025-03-15"
#   "03/15/2025"
#   "15 March, 2025"
#   "Mar 15 2025 2:30PM"
#
# Expected output:
#   2025-03-15
#   2025-03-15
#   2025-03-15
#   2025-03-15 14:30:00
#
# Hint: Each string needs its own format string for strptime()
# =============================================================================

def exercise_3():
    date_strings = [
        ("2025-03-15", None),       # Replace None with the format string
        ("03/15/2025", None),
        ("15 March, 2025", None),
        ("Mar 15 2025 2:30PM", None),
    ]
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: Business days between two dates
#
# Write a function that counts the number of business days (Monday-Friday)
# between two dates (inclusive of start, exclusive of end).
#
# Test it with:
#   start = date(2025, 3, 1)   # Saturday
#   end   = date(2025, 3, 15)  # Saturday
#
# Expected output:
#   Business days from 2025-03-01 to 2025-03-15: 10
#
# Hint: Use a loop with timedelta(days=1) and check .weekday() < 5
# =============================================================================

def exercise_4():
    start = date(2025, 3, 1)
    end = date(2025, 3, 15)
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Countdown timer
#
# Create a countdown to New Year's Day 2026. Calculate and print:
#   - Days remaining
#   - Weeks and remaining days
#   - A breakdown: X months, Y weeks, Z days (approximate — assume 30 days/month)
#
# Expected output format:
#   Days until 2026-01-01: 319
#   That's 45 weeks and 4 days
#   Roughly 10 months, 2 weeks, and 3 days
#
# (Your numbers will vary based on when you run this!)
#
# Hint: Use integer division (//) and modulo (%) to break down the days
# =============================================================================

def exercise_5():
    target = date(2026, 1, 1)
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: Meeting scheduler
#
# Given a list of existing meetings (start_time, end_time) and a desired
# meeting duration, find all available 30-minute slots during business
# hours (9:00 AM to 5:00 PM) on a given day.
#
# Existing meetings:
#   9:00-10:00, 11:30-12:30, 14:00-15:30
#
# Find available slots for a 30-minute meeting.
#
# Expected output:
#   Available 30-min slots on 2025-03-15:
#     10:00 - 10:30
#     10:30 - 11:00
#     11:00 - 11:30
#     12:30 - 13:00
#     13:00 - 13:30
#     13:30 - 14:00
#     15:30 - 16:00
#     16:00 - 16:30
#     16:30 - 17:00
#
# Hint: Loop through the day in 30-minute increments using timedelta.
#       For each slot, check if it overlaps with any existing meeting.
# =============================================================================

def exercise_6():
    meeting_day = date(2025, 3, 15)

    # Existing meetings as (start_hour, start_min, end_hour, end_min)
    existing_meetings = [
        (9, 0, 10, 0),
        (11, 30, 12, 30),
        (14, 0, 15, 30),
    ]

    meeting_duration = timedelta(minutes=30)
    # YOUR CODE HERE
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    birth_date = date(1990, 6, 15)
    today = date.today()

    # Age in years (accounting for whether birthday has passed)
    age_years = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age_years -= 1

    # Age in days — just subtract the dates
    age_days = (today - birth_date).days

    print(f"Age: {age_years} years")
    print(f"Age: {age_days} days")


def solution_2():
    d = date(2025, 3, 15)
    print(f"US format:       {d.strftime('%m/%d/%Y')}")
    print(f"European format: {d.strftime('%d-%m-%Y')}")
    print(f"ISO format:      {d.strftime('%Y-%m-%d')}")
    print(f"Long format:     {d.strftime('%A, %B %d, %Y')}")


def solution_3():
    date_strings = [
        ("2025-03-15", "%Y-%m-%d"),
        ("03/15/2025", "%m/%d/%Y"),
        ("15 March, 2025", "%d %B, %Y"),
        ("Mar 15 2025 2:30PM", "%b %d %Y %I:%M%p"),
    ]
    for date_str, fmt in date_strings:
        parsed = datetime.strptime(date_str, fmt)
        # Use date() for date-only strings, full datetime otherwise
        if parsed.hour == 0 and parsed.minute == 0 and parsed.second == 0:
            print(parsed.strftime("%Y-%m-%d"))
        else:
            print(parsed.strftime("%Y-%m-%d %H:%M:%S"))


def solution_4():
    start = date(2025, 3, 1)
    end = date(2025, 3, 15)

    business_days = 0
    current = start
    while current < end:
        # weekday(): 0=Monday, 4=Friday, 5=Saturday, 6=Sunday
        if current.weekday() < 5:
            business_days += 1
        current += timedelta(days=1)

    print(f"Business days from {start} to {end}: {business_days}")


def solution_5():
    target = date(2026, 1, 1)
    today = date.today()
    total_days = (target - today).days

    weeks = total_days // 7
    remaining_days = total_days % 7

    months = total_days // 30
    after_months = total_days % 30
    approx_weeks = after_months // 7
    approx_days = after_months % 7

    print(f"Days until {target}: {total_days}")
    print(f"That's {weeks} weeks and {remaining_days} days")
    print(f"Roughly {months} months, {approx_weeks} weeks, and {approx_days} days")


def solution_6():
    meeting_day = date(2025, 3, 15)

    # Existing meetings as (start_hour, start_min, end_hour, end_min)
    existing_meetings = [
        (9, 0, 10, 0),
        (11, 30, 12, 30),
        (14, 0, 15, 30),
    ]

    # Convert to datetime objects for easier comparison
    booked = []
    for sh, sm, eh, em in existing_meetings:
        start = datetime(meeting_day.year, meeting_day.month, meeting_day.day, sh, sm)
        end = datetime(meeting_day.year, meeting_day.month, meeting_day.day, eh, em)
        booked.append((start, end))

    meeting_duration = timedelta(minutes=30)
    day_start = datetime(meeting_day.year, meeting_day.month, meeting_day.day, 9, 0)
    day_end = datetime(meeting_day.year, meeting_day.month, meeting_day.day, 17, 0)

    print(f"Available 30-min slots on {meeting_day}:")

    slot_start = day_start
    while slot_start + meeting_duration <= day_end:
        slot_end = slot_start + meeting_duration

        # Check if this slot overlaps with any existing meeting
        is_available = True
        for booked_start, booked_end in booked:
            # Overlap if slot starts before meeting ends AND slot ends after meeting starts
            if slot_start < booked_end and slot_end > booked_start:
                is_available = False
                break

        if is_available:
            print(f"  {slot_start.strftime('%H:%M')} - {slot_end.strftime('%H:%M')}")

        slot_start += meeting_duration


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Age in days", exercise_1),
        ("Format dates in different styles", exercise_2),
        ("Parse dates from multiple formats", exercise_3),
        ("Business days between two dates", exercise_4),
        ("Countdown timer", exercise_5),
        ("Meeting scheduler", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
