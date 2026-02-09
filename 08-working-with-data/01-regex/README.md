# Regular Expressions

## Objective

Learn how to use regular expressions (regex) to search, match, and manipulate text with powerful pattern-matching syntax. By the end of this lesson, you'll be able to validate input, extract data from strings, and do search-and-replace operations that would be painful (or impossible) with basic string methods.

## Concepts Covered

- What regex is and when to use it
- The `re` module — Python's built-in regex engine
- Basic patterns: literal characters, `.`, `^`, `$`
- Character classes: `[abc]`, `[a-z]`, `\d`, `\w`, `\s` and their negations
- Quantifiers: `*`, `+`, `?`, `{n}`, `{n,m}`, greedy vs lazy
- `re.search()` vs `re.match()` vs `re.fullmatch()`
- `re.findall()` and `re.finditer()`
- `re.sub()` — search and replace
- `re.split()` — split by pattern
- Groups and named groups
- Raw strings `r""` — why they matter
- `re.compile()` — compiling patterns for reuse
- Common flags: `re.IGNORECASE`, `re.MULTILINE`, `re.DOTALL`
- Practical examples: email validation, phone numbers, URL parsing

## Prerequisites

- Strings and string methods
- Basic Python functions
- Loops and iteration

## Lesson

### What Is Regex and When Should You Use It?

A **regular expression** (regex) is a special sequence of characters that defines a search pattern. Think of it as a mini-language for describing text patterns.

When should you reach for regex?

- **Validating input** — Does this string look like an email address? A phone number?
- **Extracting data** — Pull all the URLs out of a web page, or dates out of a log file.
- **Search and replace** — Replace every phone number in a document with `[REDACTED]`.
- **Splitting strings** — Split text on complex delimiters, not just a single character.

When should you *not* use regex? If a simple string method like `str.startswith()`, `str.split()`, or `"x" in string` does the job, use that instead. Regex is powerful, but it's harder to read and debug.

### The re Module

Python's regex engine lives in the `re` module:

```python
import re
```

That's it. No installs needed — it's part of the standard library.

### Raw Strings — Why They Matter for Regex

Before we dive into patterns, let's talk about **raw strings**. In a regular Python string, the backslash `\` is an escape character — `\n` means newline, `\t` means tab. But regex uses backslashes all over the place (`\d`, `\w`, `\s`...).

Raw strings (prefixed with `r`) tell Python "don't interpret backslashes":

```python
# Without raw string — Python sees \b as a backspace character
pattern = "\bword\b"    # NOT what you want

# With raw string — Python passes \b directly to the regex engine
pattern = r"\bword\b"   # Correct! Matches "word" as a whole word
```

**Rule of thumb:** Always use raw strings for regex patterns. Just always prefix with `r`.

### Basic Patterns

The simplest regex is just literal text:

```python
import re
result = re.search(r"hello", "say hello to regex")
print(result.group())  # "hello"
```

Special characters give you more power:

| Pattern | Meaning | Example |
|---------|---------|---------|
| `.` | Any character (except newline) | `r"h.t"` matches "hat", "hit", "hot" |
| `^` | Start of string | `r"^Hello"` matches "Hello world" but not "Say Hello" |
| `$` | End of string | `r"world$"` matches "Hello world" but not "world class" |
| `\` | Escape a special character | `r"\."` matches a literal dot |

### Character Classes

Character classes let you match *any one character* from a set:

```python
r"[aeiou]"     # Any vowel
r"[a-z]"       # Any lowercase letter
r"[A-Za-z]"    # Any letter (upper or lower)
r"[0-9]"       # Any digit
r"[^aeiou]"    # Any character EXCEPT a vowel (^ inside [] means NOT)
```

Python also provides shorthand character classes:

| Shorthand | Meaning | Equivalent |
|-----------|---------|------------|
| `\d` | Any digit | `[0-9]` |
| `\D` | Any NON-digit | `[^0-9]` |
| `\w` | Any "word" character | `[a-zA-Z0-9_]` |
| `\W` | Any NON-word character | `[^a-zA-Z0-9_]` |
| `\s` | Any whitespace | `[ \t\n\r\f\v]` |
| `\S` | Any NON-whitespace | `[^ \t\n\r\f\v]` |

The uppercase versions are always the **negation** of the lowercase ones.

### Quantifiers

Quantifiers control *how many times* a pattern repeats:

| Quantifier | Meaning | Example |
|------------|---------|---------|
| `*` | Zero or more | `r"ab*c"` matches "ac", "abc", "abbc" |
| `+` | One or more | `r"ab+c"` matches "abc", "abbc" but NOT "ac" |
| `?` | Zero or one (optional) | `r"colou?r"` matches "color" and "colour" |
| `{n}` | Exactly n times | `r"\d{3}"` matches exactly three digits |
| `{n,m}` | Between n and m times | `r"\d{2,4}"` matches 2, 3, or 4 digits |
| `{n,}` | n or more times | `r"\d{2,}"` matches 2 or more digits |

**Greedy vs lazy:** By default, quantifiers are *greedy* — they match as much as possible. Add `?` after a quantifier to make it *lazy* (match as little as possible):

```python
text = "<b>bold</b> and <i>italic</i>"

re.findall(r"<.*>", text)    # Greedy: ['<b>bold</b> and <i>italic</i>']
re.findall(r"<.*?>", text)   # Lazy:   ['<b>', '</b>', '<i>', '</i>']
```

### re.search() vs re.match() vs re.fullmatch()

These three functions all look for a pattern, but they differ in *where* they look:

```python
text = "say hello to regex"

re.search(r"hello", text)      # Searches ANYWHERE in the string — match!
re.match(r"hello", text)       # Only checks the BEGINNING — no match!
re.match(r"say", text)         # Checks the beginning — match!
re.fullmatch(r"hello", text)   # Must match the ENTIRE string — no match!
re.fullmatch(r"say hello to regex", text)  # Entire string — match!
```

All three return a **Match object** on success, or `None` on failure. You'll usually use `re.search()` — it's the most flexible.

### re.findall() — Find All Matches

`re.findall()` returns a list of all non-overlapping matches:

```python
text = "My numbers are 123-456-7890 and 987-654-3210"
re.findall(r"\d+", text)
# ['123', '456', '7890', '987', '654', '3210']
```

If the pattern contains groups (parentheses), `findall` returns the group contents instead:

```python
text = "eggs=12, spam=7, ham=3"
re.findall(r"(\w+)=(\d+)", text)
# [('eggs', '12'), ('spam', '7'), ('ham', '3')]
```

### re.finditer() — Iterate Over Match Objects

`re.finditer()` is like `findall()`, but gives you full **Match objects** so you can access positions, groups, and more:

```python
text = "Call 555-1234 or 555-5678"
for match in re.finditer(r"\d{3}-\d{4}", text):
    print(f"Found '{match.group()}' at position {match.start()}-{match.end()}")
```

### re.sub() — Search and Replace

`re.sub()` replaces all matches with a replacement string:

```python
text = "Hello World"
re.sub(r"World", "Python", text)     # "Hello Python"

# Use \1, \2 etc. to reference groups in the replacement
text = "2025-02-09"
re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\2/\3/\1", text)  # "02/09/2025"
```

### re.split() — Split by Pattern

`re.split()` splits a string at each match, like `str.split()` on steroids:

```python
text = "one, two;  three   four"
re.split(r"[,;\s]+", text)
# ['one', 'two', 'three', 'four']
```

### Groups

Parentheses `()` create **capturing groups**, letting you extract specific parts of a match:

```python
match = re.search(r"(\d{3})-(\d{4})", "Call 555-1234")
match.group()    # "555-1234"   — the full match
match.group(1)   # "555"        — first group
match.group(2)   # "1234"       — second group
```

**Named groups** use `(?P<name>pattern)` so you can refer to groups by name instead of number:

```python
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
match = re.search(pattern, "Today is 2025-02-09")
match.group("year")    # "2025"
match.group("month")   # "02"
match.group("day")     # "09"
```

### re.compile() — Compiling Patterns for Reuse

If you're using the same pattern over and over, compile it first. This creates a reusable pattern object and avoids re-parsing the regex each time:

```python
email_pattern = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")

email_pattern.search("mail me at alice@example.com")
email_pattern.findall("alice@one.com and bob@two.com")
```

The compiled object has all the same methods: `.search()`, `.match()`, `.findall()`, `.sub()`, etc.

### Common Flags

Flags modify how the regex engine behaves. Pass them as the `flags` argument:

```python
# re.IGNORECASE (or re.I) — case-insensitive matching
re.search(r"python", "I love Python", re.IGNORECASE)   # Match!

# re.MULTILINE (or re.M) — ^ and $ match start/end of each LINE, not just the string
text = "line 1\nline 2\nline 3"
re.findall(r"^line \d", text, re.MULTILINE)  # ['line 1', 'line 2', 'line 3']

# re.DOTALL (or re.S) — makes . match newlines too
text = "start\nmiddle\nend"
re.search(r"start.*end", text, re.DOTALL)    # Match! (without DOTALL, . doesn't match \n)
```

You can combine flags with the `|` operator: `re.IGNORECASE | re.MULTILINE`.

### Practical Examples

**Simple email validation:**

```python
pattern = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"
re.fullmatch(pattern, "alice@example.com")    # Match!
re.fullmatch(pattern, "not-an-email")          # None
```

**Phone number matching:**

```python
pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
numbers = ["555-123-4567", "(555) 123-4567", "555.123.4567", "5551234567"]
for num in numbers:
    if re.fullmatch(pattern, num):
        print(f"{num} is valid")
```

**URL parsing:**

```python
pattern = r"(?P<protocol>https?)://(?P<domain>[\w.-]+)(?P<path>/[\w./%-]*)?"
match = re.search(pattern, "Visit https://www.example.com/path/to/page")
match.group("protocol")  # "https"
match.group("domain")    # "www.example.com"
match.group("path")      # "/path/to/page"
```

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- Regular expressions are patterns that describe text — use them for validation, extraction, and replacement
- Always use raw strings `r""` for regex patterns to avoid backslash headaches
- `re.search()` finds a match anywhere, `re.match()` checks the start, `re.fullmatch()` checks the whole string
- `re.findall()` gets all matches as a list; `re.finditer()` gives you Match objects
- `re.sub()` is regex-powered search-and-replace; `re.split()` is regex-powered splitting
- Use groups `()` to extract specific parts of a match, and named groups `(?P<name>...)` for readability
- `re.compile()` saves time when you reuse the same pattern repeatedly
- Quantifiers are greedy by default — append `?` to make them lazy
- When a simple string method does the job, prefer it over regex — save regex for the complex stuff
