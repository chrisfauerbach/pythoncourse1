"""
Regular Expressions — Example Code
====================================

Run this file:
    python3 example.py

A complete tour of Python's re module. Every major feature is demonstrated
with practical, real-world-ish examples so you can see how regex actually
works — not just in theory, but in running code.
"""

import re

# -----------------------------------------------------------------------------
# 1. Raw strings — why they matter
# -----------------------------------------------------------------------------

# Regular string: Python interprets \b as a backspace character
bad_pattern = "\bcat\b"
print("1. Raw strings")
print(f"   Without raw string: repr is {bad_pattern!r}")

# Raw string: \b is passed through as literal characters for the regex engine
good_pattern = r"\bcat\b"
print(f"   With raw string:    repr is {good_pattern!r}")

# The raw version actually works as a word-boundary match
text = "the cat sat on the caterpillar"
match = re.search(good_pattern, text)
print(f"   Searching '{text}'")
print(f"   Found: '{match.group()}' (only 'cat', not 'caterpillar')")
print()

# -----------------------------------------------------------------------------
# 2. Basic patterns: literal text, . (dot), ^ (start), $ (end)
# -----------------------------------------------------------------------------

print("2. Basic patterns")

# Literal match
result = re.search(r"hello", "say hello to regex")
print(f"   Literal search for 'hello': {result.group()}")

# . (dot) matches any character except newline
matches = re.findall(r"h.t", "hat hit hot hut h\nt")
print(f"   Pattern 'h.t' in 'hat hit hot hut': {matches}")

# ^ matches start of string
print(f"   '^Hello' in 'Hello world': {re.search(r'^Hello', 'Hello world') is not None}")
print(f"   '^Hello' in 'Say Hello':   {re.search(r'^Hello', 'Say Hello') is not None}")

# $ matches end of string
print(f"   'world$' in 'Hello world':  {re.search(r'world$', 'Hello world') is not None}")
print(f"   'world$' in 'world class':  {re.search(r'world$', 'world class') is not None}")
print()

# -----------------------------------------------------------------------------
# 3. Character classes
# -----------------------------------------------------------------------------

print("3. Character classes")

text = "The 3 cats ate 12 fish at 7pm"

# [0-9] or \d — digits
print(f"   Text: '{text}'")
print("   All digits [0-9]:     ", re.findall(r'[0-9]', text))
print("   All digits (\\d):      ", re.findall(r'\d', text))

# \d+ — one or more digits (a full number)
print("   Full numbers (\\d+):   ", re.findall(r'\d+', text))

# \w — word characters (letters, digits, underscore)
print("   Word chars (\\w+):     ", re.findall(r'\w+', text))

# \s — whitespace
print("   Whitespace count:     ", len(re.findall(r'\s', text)))

# Custom class — vowels only
print("   Vowels [aeiou]:       ", re.findall(r'[aeiou]', text.lower()))

# Negated class — non-digits
print("   Non-digits (\\D+):     ", re.findall(r'\D+', text))
print()

# -----------------------------------------------------------------------------
# 4. Quantifiers: *, +, ?, {n}, {n,m}
# -----------------------------------------------------------------------------

print("4. Quantifiers")

# * — zero or more
print(f"   'ab*c' matches 'ac':    {re.fullmatch(r'ab*c', 'ac') is not None}")
print(f"   'ab*c' matches 'abc':   {re.fullmatch(r'ab*c', 'abc') is not None}")
print(f"   'ab*c' matches 'abbbc': {re.fullmatch(r'ab*c', 'abbbc') is not None}")

# + — one or more
print(f"   'ab+c' matches 'ac':    {re.fullmatch(r'ab+c', 'ac') is not None}")
print(f"   'ab+c' matches 'abc':   {re.fullmatch(r'ab+c', 'abc') is not None}")

# ? — zero or one (optional)
print(f"   'colou?r' matches 'color':  {re.fullmatch(r'colou?r', 'color') is not None}")
print(f"   'colou?r' matches 'colour': {re.fullmatch(r'colou?r', 'colour') is not None}")

# {n} — exactly n
result = re.search(r'\d{3}', 'ab123cd')
print(f"   '\\d{{3}}' in 'ab123cd':   {result.group()}")

# {n,m} — between n and m
result = re.findall(r'\d{2,4}', '1 12 123 1234 12345')
print(f"   '\\d{{2,4}}' in '1 12 123 1234 12345': {result}")
print()

# -----------------------------------------------------------------------------
# 5. Greedy vs lazy quantifiers
# -----------------------------------------------------------------------------

print("5. Greedy vs lazy")

html = "<b>bold</b> and <i>italic</i>"
print(f"   Text: '{html}'")

greedy = re.findall(r"<.*>", html)
print(f"   Greedy '<.*>':  {greedy}")

lazy = re.findall(r"<.*?>", html)
print(f"   Lazy   '<.*?>': {lazy}")
print()

# -----------------------------------------------------------------------------
# 6. re.search() vs re.match() vs re.fullmatch()
# -----------------------------------------------------------------------------

print("6. search() vs match() vs fullmatch()")

text = "say hello to regex"

print(f"   Text: '{text}'")
print(f"   search('hello'):      {re.search(r'hello', text) is not None}  (anywhere)")
print(f"   match('hello'):       {re.match(r'hello', text) is not None}  (beginning only)")
print(f"   match('say'):         {re.match(r'say', text) is not None}  (beginning only)")
print(f"   fullmatch('hello'):   {re.fullmatch(r'hello', text) is not None} (entire string)")
print(f"   fullmatch(full text): {re.fullmatch(r'say hello to regex', text) is not None}  (entire string)")
print()

# -----------------------------------------------------------------------------
# 7. re.findall() — get all matches as a list
# -----------------------------------------------------------------------------

print("7. findall()")

text = "My numbers are 123-456-7890 and 987-654-3210"
print(f"   Text: '{text}'")

# Without groups — returns list of strings
all_digits = re.findall(r"\d+", text)
print(f"   All digit sequences: {all_digits}")

# With groups — returns list of tuples
text2 = "eggs=12, spam=7, ham=3"
pairs = re.findall(r"(\w+)=(\d+)", text2)
print(f"   Key-value pairs from '{text2}': {pairs}")
print()

# -----------------------------------------------------------------------------
# 8. re.finditer() — iterate with Match objects
# -----------------------------------------------------------------------------

print("8. finditer()")

text = "Call 555-1234 or 555-5678 today"
print(f"   Text: '{text}'")

for match in re.finditer(r"\d{3}-\d{4}", text):
    print(f"   Found '{match.group()}' at position {match.start()}-{match.end()}")
print()

# -----------------------------------------------------------------------------
# 9. re.sub() — search and replace
# -----------------------------------------------------------------------------

print("9. sub() — search and replace")

# Simple replacement
text = "I like cats and cats like me"
result = re.sub(r"cats", "dogs", text)
print(f"   '{text}'")
print(f"   -> '{result}'")

# Using groups in replacement — reformat a date
date_text = "Date: 2025-02-09"
result = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\2/\3/\1", date_text)
print(f"   '{date_text}' -> '{result}'")

# Using a function as replacement — uppercase every word after a period
text = "hello. world. python is great."
result = re.sub(r"(?<=\. )\w", lambda m: m.group().upper(), text)
print(f"   Capitalize after period: '{result}'")
print()

# -----------------------------------------------------------------------------
# 10. re.split() — split by pattern
# -----------------------------------------------------------------------------

print("10. split()")

# Split on multiple delimiters at once
text = "one, two; three   four"
result = re.split(r"[,;\s]+", text)
print(f"   '{text}'")
print(f"   Split on [,;\\s]+: {result}")

# Split on camelCase boundaries (lookahead/lookbehind — bonus!)
text = "camelCaseVariableName"
result = re.split(r"(?<=[a-z])(?=[A-Z])", text)
print(f"   Split camelCase '{text}': {result}")
print()

# -----------------------------------------------------------------------------
# 11. Groups — capturing parts of a match
# -----------------------------------------------------------------------------

print("11. Groups")

# Basic numbered groups
match = re.search(r"(\d{3})-(\d{3})-(\d{4})", "Call 555-123-4567 now")
if match:
    print(f"   Full match:  {match.group()}")
    print(f"   Area code:   {match.group(1)}")
    print(f"   Prefix:      {match.group(2)}")
    print(f"   Line:        {match.group(3)}")

# Named groups — much more readable
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
match = re.search(pattern, "Today is 2025-02-09, enjoy!")
if match:
    print(f"   Named groups: year={match.group('year')}, "
          f"month={match.group('month')}, day={match.group('day')}")

# .groupdict() — get all named groups as a dictionary
if match:
    print(f"   As dict:      {match.groupdict()}")
print()

# -----------------------------------------------------------------------------
# 12. re.compile() — compile a pattern for reuse
# -----------------------------------------------------------------------------

print("12. compile()")

# Compile once, use many times
email_pattern = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")

texts = [
    "Contact alice@example.com for info",
    "Send to bob.smith@company.co.uk please",
    "No email here, sorry!",
    "Two emails: a@b.com and c@d.org",
]

for text in texts:
    found = email_pattern.findall(text)
    print(f"   '{text}'")
    print(f"   -> {found if found else 'No matches'}")
print()

# -----------------------------------------------------------------------------
# 13. Common flags
# -----------------------------------------------------------------------------

print("13. Flags")

# re.IGNORECASE — case doesn't matter
result = re.findall(r"python", "Python PYTHON python PyThOn", re.IGNORECASE)
print(f"   IGNORECASE: {result}")

# re.MULTILINE — ^ and $ work per-line
text = "first line\nsecond line\nthird line"
without = re.findall(r"^\w+ line", text)
with_multi = re.findall(r"^\w+ line", text, re.MULTILINE)
print(f"   Without MULTILINE: {without}")
print(f"   With MULTILINE:    {with_multi}")

# re.DOTALL — dot matches newlines too
text = "<div>\nHello\n</div>"
without = re.findall(r"<div>.*</div>", text)
with_dotall = re.findall(r"<div>.*</div>", text, re.DOTALL)
print(f"   Without DOTALL: {without}")
print(f"   With DOTALL:    {with_dotall}")

# Combining flags
result = re.findall(r"^hello.*world$", "Hello\nWorld", re.IGNORECASE | re.DOTALL)
print(f"   Combined I+S:   {result}")
print()

# -----------------------------------------------------------------------------
# 14. Practical example: email validation
# -----------------------------------------------------------------------------

print("14. Practical — email validation")

email_re = re.compile(r"^[\w.+-]+@[\w-]+\.[\w.-]+$")

test_emails = [
    "alice@example.com",
    "bob.smith+tag@company.co.uk",
    "not-an-email",
    "@missing-local.com",
    "missing-domain@",
    "spaces not@allowed.com",
]

for email in test_emails:
    status = "VALID" if email_re.fullmatch(email) else "INVALID"
    print(f"   {email:<35} {status}")
print()

# -----------------------------------------------------------------------------
# 15. Practical example: phone number matching
# -----------------------------------------------------------------------------

print("15. Practical — phone numbers")

phone_re = re.compile(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")

test_phones = [
    "555-123-4567",
    "(555) 123-4567",
    "555.123.4567",
    "5551234567",
    "(555)123-4567",
    "55-12-4567",       # Too few digits — should NOT match
]

for phone in test_phones:
    match = phone_re.fullmatch(phone)
    status = "MATCH" if match else "NO MATCH"
    print(f"   {phone:<20} {status}")
print()

# -----------------------------------------------------------------------------
# 16. Practical example: URL parsing
# -----------------------------------------------------------------------------

print("16. Practical — URL parsing")

url_pattern = re.compile(
    r"(?P<protocol>https?)://"
    r"(?P<domain>[\w.-]+)"
    r"(?P<path>/[\w./%-]*)?"
    r"(?:\?(?P<query>[\w=&%-]*))?"
)

test_urls = [
    "https://www.example.com/path/to/page",
    "http://api.example.org/v2/users?id=42&sort=name",
    "https://simple.com",
]

for url in test_urls:
    match = url_pattern.search(url)
    if match:
        print(f"   URL:      {url}")
        print(f"   Protocol: {match.group('protocol')}")
        print(f"   Domain:   {match.group('domain')}")
        print(f"   Path:     {match.group('path')}")
        print(f"   Query:    {match.group('query')}")
        print()

# -----------------------------------------------------------------------------
# 17. Putting it all together
# -----------------------------------------------------------------------------

print("=" * 50)
print("   REGULAR EXPRESSIONS COMPLETE!")
print("=" * 50)
print()
print("You've seen the full power of Python's re module.")
print("Now try the exercises to practice on your own!")
