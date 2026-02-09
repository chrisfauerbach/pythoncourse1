"""
String Operations — Example Code
==================================

Run this file:
    python3 example.py

This file demonstrates how to index, slice, search, modify, and format
strings in Python. Strings are one of the most-used types, so get
comfortable with these operations!
"""

# -----------------------------------------------------------------------------
# 1. Strings are sequences — indexing with []
# -----------------------------------------------------------------------------

print("--- 1. Indexing ---")
s = "Python"

# Each character has a position, starting at 0
print(f"String: {s!r}")
print(f"s[0] = {s[0]!r}")    # P (first character)
print(f"s[1] = {s[1]!r}")    # y
print(f"s[5] = {s[5]!r}")    # n (last character)
print(f"Length: {len(s)}")    # 6 characters total
print()

# -----------------------------------------------------------------------------
# 2. Negative indexing — count from the end
# -----------------------------------------------------------------------------

print("--- 2. Negative Indexing ---")
s = "Python"

print(f"s[-1] = {s[-1]!r}")   # n (last character)
print(f"s[-2] = {s[-2]!r}")   # o (second to last)
print(f"s[-6] = {s[-6]!r}")   # P (same as s[0])

# Super useful when you just want the last character of any string
filename = "report.pdf"
extension = filename[-3:]
print(f"Extension of {filename!r}: {extension!r}")
print()

# -----------------------------------------------------------------------------
# 3. Slicing — grab chunks of a string
# -----------------------------------------------------------------------------

print("--- 3. Slicing ---")
s = "Hello, World!"

# Basic slicing: s[start:stop] (stop is NOT included)
print(f"s[0:5]  = {s[0:5]!r}")     # 'Hello'
print(f"s[7:12] = {s[7:12]!r}")    # 'World'

# Omit start or stop
print(f"s[:5]   = {s[:5]!r}")      # 'Hello' (from beginning)
print(f"s[7:]   = {s[7:]!r}")      # 'World!' (to the end)
print(f"s[:]    = {s[:]!r}")       # 'Hello, World!' (full copy)

# Slicing with a step: s[start:stop:step]
alphabet = "abcdefghij"
print(f"Every 2nd: {alphabet[::2]!r}")     # 'acegi'
print(f"Every 3rd: {alphabet[::3]!r}")     # 'adgj'

# The classic — reverse a string
print(f"Reversed: {s[::-1]!r}")            # '!dlroW ,olleH'
print()

# -----------------------------------------------------------------------------
# 4. String methods — Case
# -----------------------------------------------------------------------------

print("--- 4. Case Methods ---")
s = "hello, world"

print(f"Original:    {s!r}")
print(f".upper():    {s.upper()!r}")        # 'HELLO, WORLD'
print(f".lower():    {s.lower()!r}")        # 'hello, world'
print(f".title():    {s.title()!r}")        # 'Hello, World'
print(f".capitalize(): {s.capitalize()!r}") # 'Hello, world'
print(f".swapcase(): {s.swapcase()!r}")     # 'HELLO, WORLD'

mixed = "hElLo WoRlD"
print(f"Swapcase of {mixed!r}: {mixed.swapcase()!r}")  # 'HeLlO wOrLd'
print()

# -----------------------------------------------------------------------------
# 5. String methods — Search
# -----------------------------------------------------------------------------

print("--- 5. Search Methods ---")
s = "the quick brown fox jumps over the lazy dog"

# find() returns index of first match, or -1 if not found
print(f"find('fox'):  {s.find('fox')}")     # 16
print(f"find('cat'):  {s.find('cat')}")     # -1 (not found)

# index() is like find(), but raises an error if not found
print(f"index('fox'): {s.index('fox')}")    # 16

# count() — how many times does a substring appear?
print(f"count('the'): {s.count('the')}")    # 2
print(f"count('o'):   {s.count('o')}")      # 4

# startswith() and endswith()
print(f"startswith('the'): {s.startswith('the')}")   # True
print(f"endswith('dog'):   {s.endswith('dog')}")     # True
print(f"endswith('cat'):   {s.endswith('cat')}")     # False
print()

# -----------------------------------------------------------------------------
# 6. String methods — Modify (strip, replace)
# -----------------------------------------------------------------------------

print("--- 6. Modify Methods ---")

# strip() removes leading/trailing whitespace
messy = "   hello, world   "
print(f"Original:  {messy!r}")
print(f".strip():  {messy.strip()!r}")      # 'hello, world'
print(f".lstrip(): {messy.lstrip()!r}")     # 'hello, world   '
print(f".rstrip(): {messy.rstrip()!r}")     # '   hello, world'

# Strip specific characters
dashes = "---hello---"
print(f"Strip dashes: {dashes.strip('-')!r}")   # 'hello'

# replace() swaps one substring for another
s = "I like cats and cats like me"
print(f"Original: {s!r}")
print(f"Replace cats->dogs: {s.replace('cats', 'dogs')!r}")
print(f"Replace first only:  {s.replace('cats', 'dogs', 1)!r}")
print()

# -----------------------------------------------------------------------------
# 7. String methods — Check (is-methods)
# -----------------------------------------------------------------------------

print("--- 7. Check Methods ---")

# isdigit() — all digits?
print(f"'12345'.isdigit():  {'12345'.isdigit()}")    # True
print(f"'12.45'.isdigit():  {'12.45'.isdigit()}")    # False

# isalpha() — all letters?
print(f"'Hello'.isalpha():  {'Hello'.isalpha()}")    # True
print(f"'Hello!'.isalpha(): {'Hello!'.isalpha()}")   # False

# isalnum() — letters or digits?
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")   # True
print(f"'abc 12'.isalnum(): {'abc 12'.isalnum()}")   # False

# isspace() — all whitespace?
print(f"'   '.isspace():    {'   '.isspace()}")      # True
print(f"''.isspace():       {''.isspace()}")          # False
print()

# -----------------------------------------------------------------------------
# 8. String methods — Split and Join
# -----------------------------------------------------------------------------

print("--- 8. Split and Join ---")

# split() breaks a string into a list
sentence = "the quick brown fox"
words = sentence.split()
print(f"Split: {sentence!r} -> {words}")

# Split on a specific delimiter
date = "2025-02-09"
parts = date.split("-")
print(f"Split date: {date!r} -> {parts}")

csv_line = "Alice,30,Engineer"
fields = csv_line.split(",")
print(f"Split CSV: {csv_line!r} -> {fields}")

# join() glues a list back together
words = ["Hello", "World"]
print(f"Join with space: {' '.join(words)!r}")     # 'Hello World'
print(f"Join with dash:  {'-'.join(words)!r}")     # 'Hello-World'
print(f"Join with empty: {''.join(words)!r}")      # 'HelloWorld'

# The split -> modify -> join pattern
sentence = "python is awesome"
title_version = " ".join(word.capitalize() for word in sentence.split())
print(f"Capitalized words: {title_version!r}")     # 'Python Is Awesome'
print()

# -----------------------------------------------------------------------------
# 9. Strings are immutable — you can't change them in place
# -----------------------------------------------------------------------------

print("--- 9. Immutability ---")
s = "Hello"

# s[0] = "h"   # This would raise: TypeError: 'str' object does not support item assignment

# Instead, create a new string
new_s = "h" + s[1:]
print(f"Original: {s!r}")
print(f"New:      {new_s!r}")

# Methods don't change the original either
name = "alice"
upper_name = name.upper()
print(f"name is still: {name!r}")
print(f"upper_name:    {upper_name!r}")
print()

# -----------------------------------------------------------------------------
# 10. f-string formatting — alignment, padding, numbers
# -----------------------------------------------------------------------------

print("--- 10. f-string Formatting ---")

# Alignment: < (left), > (right), ^ (center)
print(f"|{'left':<15}|")       # |left           |
print(f"|{'right':>15}|")      # |          right|
print(f"|{'center':^15}|")     # |    center     |

# Fill character + alignment
print(f"{'hello':*^20}")       # *******hello********
print(f"{'hello':->20}")       # ---------------hello
print(f"{'hello':.>20}")       # ...............hello

# Zero-padded numbers
print(f"Order #{42:05d}")      # Order #00042
print(f"Code: {7:03d}")        # Code: 007

# Decimal precision
pi = 3.14159265
print(f"Pi (2 decimals): {pi:.2f}")    # 3.14
print(f"Pi (4 decimals): {pi:.4f}")    # 3.1416

# Thousands separator
big = 1_234_567
print(f"Population: {big:,}")          # Population: 1,234,567

# Percentages
ratio = 0.856
print(f"Score: {ratio:.1%}")           # Score: 85.6%

# Combining width and format
for item, price in [("Coffee", 4.5), ("Muffin", 3.25), ("Juice", 5.0)]:
    print(f"  {item:<10} ${price:>6.2f}")
print()

# -----------------------------------------------------------------------------
# 11. Raw strings — literal backslashes
# -----------------------------------------------------------------------------

print("--- 11. Raw Strings ---")

# Normal string: \t is a tab, \n is a newline
print("Normal:  hello\tworld")     # hello   world (tab in the middle)

# Raw string: backslashes are just backslashes
print(r"Raw:     hello\tworld")    # hello\tworld (literal characters)

# Useful for file paths (especially on Windows)
normal_path = "C:\\Users\\Alice\\Documents"
raw_path = r"C:\Users\Alice\Documents"
print(f"Normal path: {normal_path}")
print(f"Raw path:    {raw_path}")

# Useful for regex patterns
import re
pattern = r"\d{3}-\d{3}-\d{4}"
phone = "Call me at 555-123-4567 today"
match = re.search(pattern, phone)
if match:
    print(f"Found phone number: {match.group()}")
print()

# -----------------------------------------------------------------------------
# Done!
# -----------------------------------------------------------------------------

print("=" * 40)
print("  STRING OPERATIONS COMPLETE!")
print("=" * 40)
