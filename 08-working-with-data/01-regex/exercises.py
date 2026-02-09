"""
Regular Expressions — Exercises
================================

Practice problems to test your understanding of regex.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""

import re


# =============================================================================
# Exercise 1: Extract email addresses
#
# Given the block of text below, use re.findall() to extract ALL email
# addresses. Return them as a list.
#
# Expected output:
#   ['alice@example.com', 'bob.smith@company.co.uk', 'charlie+news@gmail.com']
#
# Hint: Email pattern — letters, digits, dots, +, - before @,
#       then domain parts separated by dots.
# =============================================================================

def exercise_1():
    text = """
    Contact alice@example.com for general inquiries.
    For business: bob.smith@company.co.uk
    Newsletter signup: charlie+news@gmail.com
    This is not an email: @missing or broken@
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Validate phone numbers
#
# Write a function that checks if a string is a valid US phone number.
# It should accept these formats:
#   555-123-4567
#   (555) 123-4567
#   555.123.4567
#   5551234567
#
# Use re.fullmatch() and print whether each test number is valid or not.
#
# Expected output:
#   555-123-4567   VALID
#   (555) 123-4567 VALID
#   555.123.4567   VALID
#   5551234567     VALID
#   55-12-456      INVALID
#   abc-def-ghij   INVALID
# =============================================================================

def exercise_2():
    test_numbers = [
        "555-123-4567",
        "(555) 123-4567",
        "555.123.4567",
        "5551234567",
        "55-12-456",
        "abc-def-ghij",
    ]
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: Extract dates from text
#
# Find all dates in the text below. Dates appear in two formats:
#   MM/DD/YYYY   (like 02/09/2025)
#   YYYY-MM-DD   (like 2025-02-09)
#
# Use re.findall() and print each date found.
#
# Expected output:
#   Found date: 02/09/2025
#   Found date: 2025-12-25
#   Found date: 07/04/1776
#   Found date: 2000-01-01
#
# Hint: You can use the | (or) operator in regex to match either format.
# =============================================================================

def exercise_3():
    text = """
    The report was filed on 02/09/2025 and is due by 2025-12-25.
    Independence Day was 07/04/1776. The Y2K bug was feared on 2000-01-01.
    Random numbers like 99/99/9999 should probably match the pattern too
    (we're not validating actual calendar dates, just the format).
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: Mask credit card numbers
#
# Given a block of text, find all credit card numbers (sequences of
# exactly 16 digits, possibly separated by dashes or spaces in groups of 4)
# and replace them with "****-****-****-XXXX" where XXXX is the last 4 digits.
#
# Use re.sub() with a function as the replacement.
#
# Expected output:
#   Card: ****-****-****-5678
#   Another: ****-****-****-8765
#   Not a card: 12345
#
# Hint: The replacement argument to re.sub() can be a function that
#       receives a Match object and returns the replacement string.
# =============================================================================

def exercise_4():
    text = """Card: 1234-5678-9012-5678
Another: 1111 2222 3333 8765
Not a card: 12345"""
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Parse a log file
#
# Each line in the log below has this format:
#   [TIMESTAMP] LEVEL: Message text here
#
# Use re.finditer() with named groups to extract the timestamp, level,
# and message from each line. Print them in a readable format.
#
# Expected output:
#   Time: 2025-02-09 10:23:01 | Level: INFO  | Msg: Server started on port 8080
#   Time: 2025-02-09 10:23:05 | Level: DEBUG | Msg: Loading configuration file
#   Time: 2025-02-09 10:24:12 | Level: WARN  | Msg: Disk usage above 80%
#   Time: 2025-02-09 10:25:00 | Level: ERROR | Msg: Connection refused to database
#
# Hint: Named groups use (?P<name>pattern) syntax.
# =============================================================================

def exercise_5():
    log = """[2025-02-09 10:23:01] INFO: Server started on port 8080
[2025-02-09 10:23:05] DEBUG: Loading configuration file
[2025-02-09 10:24:12] WARN: Disk usage above 80%
[2025-02-09 10:25:00] ERROR: Connection refused to database"""
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: Build a simple tokenizer
#
# Given a math expression as a string, break it into tokens. Each token is
# one of:
#   - NUMBER:   one or more digits (possibly with a decimal point)
#   - WORD:     one or more letters (function names like "sin", "cos")
#   - OP:       one of + - * / ^ ( )
#
# Use re.finditer() to scan the expression and classify each token.
# Skip whitespace.
#
# Input:  "sin(3.14) + 2 * (10 - 3) / 5.0"
#
# Expected output:
#   WORD:   sin
#   OP:     (
#   NUMBER: 3.14
#   OP:     )
#   OP:     +
#   NUMBER: 2
#   OP:     *
#   OP:     (
#   NUMBER: 10
#   OP:     -
#   NUMBER: 3
#   OP:     )
#   OP:     /
#   NUMBER: 5.0
#
# Hint: Use named groups for each token type in one big pattern, combined
#       with |. Something like (?P<NUMBER>\d+\.?\d*)|(?P<WORD>[a-zA-Z]+)|...
# =============================================================================

def exercise_6():
    expression = "sin(3.14) + 2 * (10 - 3) / 5.0"
    # YOUR CODE HERE
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    text = """
    Contact alice@example.com for general inquiries.
    For business: bob.smith@company.co.uk
    Newsletter signup: charlie+news@gmail.com
    This is not an email: @missing or broken@
    """
    emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)
    for email in emails:
        print(f"  {email}")


def solution_2():
    test_numbers = [
        "555-123-4567",
        "(555) 123-4567",
        "555.123.4567",
        "5551234567",
        "55-12-456",
        "abc-def-ghij",
    ]
    pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    for number in test_numbers:
        status = "VALID" if re.fullmatch(pattern, number) else "INVALID"
        print(f"  {number:<20} {status}")


def solution_3():
    text = """
    The report was filed on 02/09/2025 and is due by 2025-12-25.
    Independence Day was 07/04/1776. The Y2K bug was feared on 2000-01-01.
    Random numbers like 99/99/9999 should probably match the pattern too
    (we're not validating actual calendar dates, just the format).
    """
    dates = re.findall(r"\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2}", text)
    for date in dates:
        print(f"  Found date: {date}")


def solution_4():
    text = """Card: 1234-5678-9012-5678
Another: 1111 2222 3333 8765
Not a card: 12345"""

    def mask_card(match):
        # Get just the digits from the match
        digits = re.sub(r"[-\s]", "", match.group())
        last_four = digits[-4:]
        return f"****-****-****-{last_four}"

    pattern = r"\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}"
    result = re.sub(pattern, mask_card, text)
    print(result)


def solution_5():
    log = """[2025-02-09 10:23:01] INFO: Server started on port 8080
[2025-02-09 10:23:05] DEBUG: Loading configuration file
[2025-02-09 10:24:12] WARN: Disk usage above 80%
[2025-02-09 10:25:00] ERROR: Connection refused to database"""

    pattern = r"\[(?P<timestamp>[\d\s:-]+)\]\s+(?P<level>\w+):\s+(?P<message>.+)"
    for match in re.finditer(pattern, log):
        ts = match.group("timestamp")
        level = match.group("level")
        msg = match.group("message")
        print(f"  Time: {ts} | Level: {level:<5} | Msg: {msg}")


def solution_6():
    expression = "sin(3.14) + 2 * (10 - 3) / 5.0"

    token_pattern = re.compile(
        r"(?P<NUMBER>\d+\.?\d*)"
        r"|(?P<WORD>[a-zA-Z]+)"
        r"|(?P<OP>[+\-*/^()])"
        r"|(?P<SKIP>\s+)"
    )

    for match in token_pattern.finditer(expression):
        kind = match.lastgroup
        value = match.group()
        if kind == "SKIP":
            continue
        print(f"  {kind:<7} {value}")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Extract email addresses", exercise_1),
        ("Validate phone numbers", exercise_2),
        ("Extract dates from text", exercise_3),
        ("Mask credit card numbers", exercise_4),
        ("Parse a log file", exercise_5),
        ("Build a simple tokenizer", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
