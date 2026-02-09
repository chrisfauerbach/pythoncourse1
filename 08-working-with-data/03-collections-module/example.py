"""
The Collections Module — Example Code
=======================================

Run this file:
    python3 example.py

Python's collections module gives you specialized containers that go beyond
the built-in dict, list, set, and tuple. This file walks through each one
with practical, real-world-ish examples.
"""

from collections import Counter, defaultdict, namedtuple, deque, OrderedDict, ChainMap

# -----------------------------------------------------------------------------
# 1. Counter — counting things the easy way
# -----------------------------------------------------------------------------

print("=" * 60)
print("1. COUNTER")
print("=" * 60)

# Count word frequencies in a sentence
sentence = "the quick brown fox jumps over the lazy dog and the fox"
words = sentence.split()
word_counts = Counter(words)
print(f"Word counts: {word_counts}")

# most_common() gives you the top N
print(f"Top 2 words: {word_counts.most_common(2)}")

# Count characters in a string
letter_counts = Counter("mississippi")
print(f"Letters in 'mississippi': {letter_counts}")

# Counter arithmetic — combine two inventories
store_a = Counter(apples=10, bananas=5, oranges=8)
store_b = Counter(apples=3, bananas=12, grapes=6)

combined = store_a + store_b
print(f"\nStore A: {store_a}")
print(f"Store B: {store_b}")
print(f"Combined inventory: {combined}")

# Subtraction drops zero and negative counts
sold = Counter(apples=7, bananas=2)
remaining = store_a - sold
print(f"After selling {dict(sold)}: {remaining}")

print()

# -----------------------------------------------------------------------------
# 2. defaultdict — no more KeyError headaches
# -----------------------------------------------------------------------------

print("=" * 60)
print("2. DEFAULTDICT")
print("=" * 60)

# Group students by their grade letter
students = [
    ("Alice", "A"), ("Bob", "B"), ("Charlie", "A"),
    ("Diana", "C"), ("Eve", "B"), ("Frank", "A"),
]

# With defaultdict(list), missing keys automatically get an empty list
by_grade = defaultdict(list)
for name, grade in students:
    by_grade[grade].append(name)

print("Students grouped by grade:")
for grade in sorted(by_grade):
    print(f"  {grade}: {by_grade[grade]}")

# defaultdict(int) — great for counting
print("\nWord frequency with defaultdict(int):")
text = "to be or not to be that is the question"
freq = defaultdict(int)
for word in text.split():
    freq[word] += 1
for word, count in sorted(freq.items(), key=lambda x: -x[1]):
    print(f"  '{word}': {count}")

# defaultdict(set) — collect unique items by key
print("\nUnique skills by department:")
employees = [
    ("Engineering", "Python"), ("Engineering", "Go"),
    ("Engineering", "Python"),  # duplicate — set handles this
    ("Marketing", "Excel"), ("Marketing", "Photoshop"),
    ("Marketing", "Excel"),  # duplicate
]
dept_skills = defaultdict(set)
for dept, skill in employees:
    dept_skills[dept].add(skill)
for dept, skills in dept_skills.items():
    print(f"  {dept}: {skills}")

print()

# -----------------------------------------------------------------------------
# 3. namedtuple — tuples that make sense
# -----------------------------------------------------------------------------

print("=" * 60)
print("3. NAMEDTUPLE")
print("=" * 60)

# Create a Point type with named fields
Point = namedtuple("Point", ["x", "y"])
origin = Point(0, 0)
p = Point(3, 7)

print(f"Origin: {origin}")
print(f"Point: {p}")
print(f"X coordinate: {p.x}")
print(f"Y coordinate: {p.y}")

# They're still tuples — unpacking works
x, y = p
print(f"Unpacked: x={x}, y={y}")

# _replace() creates a modified copy (namedtuples are immutable)
moved = p._replace(x=10)
print(f"After _replace(x=10): {moved}")
print(f"Original unchanged: {p}")

# _asdict() converts to a regular dictionary
print(f"As dict: {p._asdict()}")

# A more practical example — representing a record
Book = namedtuple("Book", ["title", "author", "year", "pages"])
books = [
    Book("The Pragmatic Programmer", "Hunt & Thomas", 1999, 352),
    Book("Clean Code", "Robert C. Martin", 2008, 464),
    Book("Python Crash Course", "Eric Matthes", 2019, 544),
]

print("\nBook catalog:")
for book in books:
    print(f"  '{book.title}' by {book.author} ({book.year}) — {book.pages}pp")

# Default values using _make and defaults parameter
Color = namedtuple("Color", ["r", "g", "b", "alpha"], defaults=[255])
red = Color(255, 0, 0)         # alpha defaults to 255
transparent_red = Color(255, 0, 0, 128)
print(f"\nRed: {red}")
print(f"Transparent red: {transparent_red}")

print()

# -----------------------------------------------------------------------------
# 4. deque — fast from both ends
# -----------------------------------------------------------------------------

print("=" * 60)
print("4. DEQUE")
print("=" * 60)

# Basic operations
d = deque([1, 2, 3, 4, 5])
print(f"Starting deque: {d}")

d.append(6)            # Add to right
d.appendleft(0)        # Add to left
print(f"After append(6) and appendleft(0): {d}")

right = d.pop()        # Remove from right
left = d.popleft()     # Remove from left
print(f"Popped right={right}, left={left}: {d}")

# Rotation — rotate elements like a carousel
carousel = deque(["A", "B", "C", "D", "E"])
print(f"\nCarousel: {carousel}")
carousel.rotate(2)     # Rotate right by 2
print(f"Rotate right 2: {carousel}")
carousel.rotate(-2)    # Rotate back
print(f"Rotate left 2:  {carousel}")

# maxlen — fixed-size buffer (this is incredibly useful)
print("\nRecent commands (maxlen=4):")
recent_commands = deque(maxlen=4)
commands = ["ls", "cd docs", "cat readme.md", "git status", "git add .", "git commit"]
for cmd in commands:
    recent_commands.append(cmd)
    print(f"  Run '{cmd}' -> history: {list(recent_commands)}")

# Sliding window — keep only the last N items
print("\nSliding window average (window=3):")
data = [10, 20, 30, 40, 50, 60, 70]
window = deque(maxlen=3)
for value in data:
    window.append(value)
    avg = sum(window) / len(window)
    print(f"  Add {value:2d} -> window={list(window)}, avg={avg:.1f}")

print()

# -----------------------------------------------------------------------------
# 5. OrderedDict — when order matters for comparison
# -----------------------------------------------------------------------------

print("=" * 60)
print("5. ORDEREDDICT")
print("=" * 60)

# Regular dicts: order doesn't matter for equality
regular_1 = {"a": 1, "b": 2, "c": 3}
regular_2 = {"c": 3, "a": 1, "b": 2}
print(f"Regular dicts equal (different order)? {regular_1 == regular_2}")  # True

# OrderedDicts: order DOES matter for equality
ordered_1 = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
ordered_2 = OrderedDict([("c", 3), ("a", 1), ("b", 2)])
print(f"OrderedDicts equal (different order)? {ordered_1 == ordered_2}")  # False

# move_to_end() — rearrange without rebuilding
od = OrderedDict([("first", 1), ("second", 2), ("third", 3)])
print(f"\nOriginal: {list(od.keys())}")

od.move_to_end("first")               # Move to the end
print(f"move_to_end('first'):           {list(od.keys())}")

od.move_to_end("third", last=False)    # Move to the beginning
print(f"move_to_end('third', last=False): {list(od.keys())}")

# Practical use: LRU-style "most recently used" tracking
print("\nMost recently accessed (move to end on access):")
cache = OrderedDict([("page_a", "..."), ("page_b", "..."), ("page_c", "...")])
print(f"  Before: {list(cache.keys())}")
cache.move_to_end("page_a")  # "page_a" was just accessed
print(f"  Access page_a: {list(cache.keys())}")

print()

# -----------------------------------------------------------------------------
# 6. ChainMap — layered dictionary lookups
# -----------------------------------------------------------------------------

print("=" * 60)
print("6. CHAINMAP")
print("=" * 60)

# Classic config layering: defaults -> user -> environment
defaults = {
    "theme": "light",
    "language": "en",
    "font_size": 14,
    "debug": False,
}

user_settings = {
    "theme": "dark",
    "font_size": 18,
}

env_overrides = {
    "debug": True,
}

# ChainMap searches left-to-right — first match wins
config = ChainMap(env_overrides, user_settings, defaults)

print("Layered config (env > user > defaults):")
print(f"  theme:     {config['theme']}")       # "dark" from user_settings
print(f"  language:  {config['language']}")    # "en" from defaults
print(f"  font_size: {config['font_size']}")  # 18 from user_settings
print(f"  debug:     {config['debug']}")       # True from env_overrides

# You can see all keys across all layers
print(f"\nAll config keys: {list(config.keys())}")
print(f"All config values: {list(config.values())}")

# The .maps attribute shows the underlying dicts
print(f"\nNumber of layers: {len(config.maps)}")
for i, layer in enumerate(config.maps):
    print(f"  Layer {i}: {layer}")

# Changes go to the FIRST dict only
config["new_key"] = "hello"
print(f"\nAfter config['new_key'] = 'hello':")
print(f"  env_overrides: {env_overrides}")  # <-- new_key was added here

# new_child() adds a new layer on top
runtime = config.new_child({"debug": False, "verbose": True})
print(f"\nWith new_child layer:")
print(f"  debug: {runtime['debug']}")   # False — from the new child layer
print(f"  theme: {runtime['theme']}")   # "dark" — falls through to user_settings

print()

# -----------------------------------------------------------------------------
# 7. Putting it all together — a mini analytics pipeline
# -----------------------------------------------------------------------------

print("=" * 60)
print("7. PUTTING IT ALL TOGETHER")
print("=" * 60)

# Analyze a collection of log entries
LogEntry = namedtuple("LogEntry", ["timestamp", "level", "message"])

logs = [
    LogEntry("09:00", "INFO", "Server started"),
    LogEntry("09:05", "INFO", "User alice logged in"),
    LogEntry("09:07", "WARNING", "Disk usage at 80%"),
    LogEntry("09:10", "ERROR", "Failed to connect to database"),
    LogEntry("09:11", "INFO", "Retrying database connection"),
    LogEntry("09:12", "INFO", "Database connected"),
    LogEntry("09:15", "WARNING", "Disk usage at 85%"),
    LogEntry("09:20", "ERROR", "API timeout"),
    LogEntry("09:21", "INFO", "API recovered"),
]

# Count log levels with Counter
level_counts = Counter(entry.level for entry in logs)
print(f"Log level summary: {dict(level_counts)}")
print(f"Most common level: {level_counts.most_common(1)[0][0]}")

# Group messages by level with defaultdict
by_level = defaultdict(list)
for entry in logs:
    by_level[entry.level].append(f"[{entry.timestamp}] {entry.message}")

print("\nMessages by level:")
for level in ["ERROR", "WARNING", "INFO"]:
    print(f"\n  {level}:")
    for msg in by_level[level]:
        print(f"    {msg}")

# Keep only the last 3 log entries in a buffer
recent = deque(maxlen=3)
for entry in logs:
    recent.append(entry)
print(f"\nLast 3 entries: {[e.message for e in recent]}")

print()
print("=" * 60)
print("COLLECTIONS MODULE COMPLETE!")
print("=" * 60)
print()
print("Try modifying the examples above and run this file again!")
