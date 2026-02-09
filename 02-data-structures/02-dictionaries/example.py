"""
Dictionaries — Example Code
=============================

Run this file:
    python3 example.py

A complete tour of Python dictionaries — creating them, reading from them,
modifying them, and all the handy tricks you'll use every day.
"""

# -----------------------------------------------------------------------------
# 1. Creating dictionaries
# -----------------------------------------------------------------------------

# Literal syntax — the most common way
person = {"name": "Alice", "age": 30, "city": "Portland"}
print("Literal syntax:", person)

# dict() constructor with keyword arguments
person2 = dict(name="Bob", age=25, city="Seattle")
print("dict() constructor:", person2)

# From a list of tuples
person3 = dict([("name", "Carol"), ("age", 28), ("city", "Denver")])
print("From tuples:", person3)

# From two lists using zip()
keys = ["name", "age", "city"]
values = ["Dave", 35, "Austin"]
person4 = dict(zip(keys, values))
print("From zip():", person4)

# Empty dictionary
empty = {}
print("Empty dict:", empty, "— length:", len(empty))

# -----------------------------------------------------------------------------
# 2. Accessing values: [] vs .get()
# -----------------------------------------------------------------------------

user = {"name": "Alice", "age": 30, "email": "alice@example.com"}

# Square brackets — fast and direct, but crashes on missing keys
print("\nuser['name']:", user["name"])
print("user['email']:", user["email"])

# .get() — returns None if the key is missing (no crash!)
print("user.get('name'):", user.get("name"))
print("user.get('phone'):", user.get("phone"))           # None
print("user.get('phone', 'N/A'):", user.get("phone", "N/A"))  # Custom default

# This would crash: user["phone"] — uncomment to see the KeyError
# print(user["phone"])

# -----------------------------------------------------------------------------
# 3. Adding, updating, and deleting entries
# -----------------------------------------------------------------------------

print("\n--- Adding and updating ---")
inventory = {"apples": 5, "bananas": 3}
print("Starting inventory:", inventory)

# Add a new key
inventory["oranges"] = 8
print("After adding oranges:", inventory)

# Update an existing key
inventory["apples"] = 10
print("After updating apples:", inventory)

# del — removes a key entirely
del inventory["bananas"]
print("After deleting bananas:", inventory)

# .pop() — removes a key and gives you the value back
orange_count = inventory.pop("oranges")
print(f"Popped oranges ({orange_count}):", inventory)

# .pop() with a default — no crash if key is missing
missing = inventory.pop("grapes", 0)
print(f"Popped grapes (default {missing}):", inventory)

# .popitem() — removes and returns the last inserted pair
inventory["pears"] = 4
inventory["kiwis"] = 6
print("Before popitem():", inventory)
last_item = inventory.popitem()
print(f"popitem() returned: {last_item}")
print("After popitem():", inventory)

# -----------------------------------------------------------------------------
# 4. Checking membership with `in`
# -----------------------------------------------------------------------------

print("\n--- Membership checking ---")
colors = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}

# `in` checks KEYS, not values
print("'red' in colors:", "red" in colors)         # True
print("'yellow' in colors:", "yellow" in colors)    # False
print("'#FF0000' in colors:", "#FF0000" in colors)  # False — that's a value!

# To check values, use .values()
print("'#FF0000' in colors.values():", "#FF0000" in colors.values())  # True

# -----------------------------------------------------------------------------
# 5. Iterating: .keys(), .values(), .items()
# -----------------------------------------------------------------------------

print("\n--- Iterating ---")
scores = {"Alice": 92, "Bob": 85, "Carol": 97}

# Iterating over keys (default behavior)
print("Keys:")
for name in scores:
    print(f"  {name}")

# Iterating over values
print("Values:")
for score in scores.values():
    print(f"  {score}")

# Iterating over key-value pairs — the most useful one!
print("Items (key-value pairs):")
for name, score in scores.items():
    print(f"  {name} scored {score}")

# You can also get these as lists
print("Keys as list:", list(scores.keys()))
print("Values as list:", list(scores.values()))

# -----------------------------------------------------------------------------
# 6. Useful methods: .update() and .setdefault()
# -----------------------------------------------------------------------------

print("\n--- .update() ---")
defaults = {"color": "blue", "size": "medium", "theme": "light"}
user_prefs = {"color": "red", "font": "mono"}
print("Defaults:", defaults)
print("User prefs:", user_prefs)

defaults.update(user_prefs)
print("After update:", defaults)
# "color" was overwritten, "font" was added, others stayed the same

print("\n--- .setdefault() ---")
config = {"debug": True}
print("Starting config:", config)

# .setdefault() only sets the value if the key doesn't already exist
config.setdefault("debug", False)    # Does nothing — "debug" is already True
config.setdefault("verbose", False)  # Adds "verbose" since it's not there yet
print("After setdefault():", config)

# It also returns the value (existing or newly set)
level = config.setdefault("log_level", "INFO")
print(f"setdefault returned: '{level}'")
print("Final config:", config)

# -----------------------------------------------------------------------------
# 7. Dictionary unpacking with **
# -----------------------------------------------------------------------------

print("\n--- Unpacking with ** ---")

# Merging two dicts into a new one (originals unchanged)
base = {"color": "blue", "size": "medium"}
extras = {"color": "red", "font": "mono"}
merged = {**base, **extras}
print("Base:", base)
print("Extras:", extras)
print("Merged:", merged)  # "color" comes from extras (last one wins)

# The | operator does the same thing (Python 3.9+)
merged2 = base | extras
print("Merged with |:", merged2)

# Unpacking into function arguments
def make_greeting(name, style="formal"):
    if style == "formal":
        return f"Good day, {name}."
    return f"Hey, {name}!"

params = {"name": "Alice", "style": "casual"}
print(make_greeting(**params))

# -----------------------------------------------------------------------------
# 8. Nested dictionaries
# -----------------------------------------------------------------------------

print("\n--- Nested dictionaries ---")

gradebook = {
    "Alice": {"math": 92, "english": 88, "science": 95},
    "Bob":   {"math": 78, "english": 85, "science": 80},
    "Carol": {"math": 90, "english": 91, "science": 87},
}

# Access nested values by chaining keys
print(f"Alice's math score: {gradebook['Alice']['math']}")

# Iterate over the nested structure
for student, grades in gradebook.items():
    average = sum(grades.values()) / len(grades)
    print(f"  {student}: average = {average:.1f}")

# Update a nested value
gradebook["Bob"]["math"] = 82
print(f"Bob's updated math score: {gradebook['Bob']['math']}")

# Add a new student
gradebook["Dave"] = {"math": 88, "english": 76, "science": 93}
print(f"New student Dave: {gradebook['Dave']}")

# -----------------------------------------------------------------------------
# 9. Dictionary ordering (insertion order guaranteed since Python 3.7)
# -----------------------------------------------------------------------------

print("\n--- Insertion order ---")
ordered = {}
ordered["first"] = 1
ordered["second"] = 2
ordered["third"] = 3
ordered["fourth"] = 4

# Items always come out in the order they were inserted
print("Keys in order:", list(ordered.keys()))
# Output: ['first', 'second', 'third', 'fourth']

# Updating a value does NOT change its position
ordered["second"] = 99
print("After updating 'second':", list(ordered.items()))
# 'second' stays in its original position

# -----------------------------------------------------------------------------
# 10. What can be a key? (hashable types only)
# -----------------------------------------------------------------------------

print("\n--- Valid key types ---")
mixed_keys = {
    "name": "a string key",
    42: "an integer key",
    3.14: "a float key",
    True: "a boolean key",
    (1, 2): "a tuple key",
}

for key, value in mixed_keys.items():
    print(f"  {key!r:>12} ({type(key).__name__:>5}) -> {value}")

# These would fail — uncomment to see the errors:
# bad = {[1, 2]: "nope"}      # TypeError: unhashable type: 'list'
# bad = {{"a": 1}: "nope"}    # TypeError: unhashable type: 'dict'

# -----------------------------------------------------------------------------
# 11. Common patterns
# -----------------------------------------------------------------------------

# --- Counting occurrences ---
print("\n--- Pattern: counting ---")
sentence = "the cat sat on the mat and the cat saw the dog"
words = sentence.split()
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

print(f"Words: {sentence}")
print("Counts:", word_counts)

# --- Grouping items ---
print("\n--- Pattern: grouping ---")
animals = ["ant", "bear", "cat", "antelope", "cobra", "beaver", "crow"]
by_letter = {}
for animal in animals:
    first = animal[0]
    by_letter.setdefault(first, []).append(animal)

print("Grouped by first letter:")
for letter, group in sorted(by_letter.items()):
    print(f"  {letter}: {group}")

# --- Inverting a dictionary ---
print("\n--- Pattern: inverting ---")
country_codes = {"US": 1, "UK": 44, "DE": 49, "JP": 81}
code_to_country = {code: country for country, code in country_codes.items()}
print("Original:", country_codes)
print("Inverted:", code_to_country)

# -----------------------------------------------------------------------------
# 12. Putting it all together
# -----------------------------------------------------------------------------

print()
print("=" * 50)
print("   DICTIONARIES EXAMPLE COMPLETE!")
print("=" * 50)
print()
print("Try modifying this file and run it again to experiment!")
