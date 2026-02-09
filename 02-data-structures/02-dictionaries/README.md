# Dictionaries

## Objective

Learn how to use Python's most versatile data structure — the dictionary. Dictionaries let you store and retrieve data using meaningful keys instead of numeric indices.

## Concepts Covered

- Creating dictionaries (literal syntax, `dict()`, from `zip()`)
- Accessing values: `[]` vs `.get()`
- Adding, updating, and deleting entries
- Checking membership with `in`
- Iterating over keys, values, and items
- Useful methods: `.update()`, `.setdefault()`
- Dictionary unpacking with `**`
- Nested dictionaries
- Dictionary ordering (insertion order since Python 3.7)
- What can be a key? (hashable types only)
- Common patterns: counting, grouping, inverting

## Prerequisites

- [Lists and Tuples](../01-lists-and-tuples/)

## Lesson

### What Is a Dictionary?

A dictionary is a collection of **key-value pairs**. Think of it like a real dictionary — you look up a word (the key) and get its definition (the value). In Python, dictionaries are written with curly braces `{}`:

```python
person = {"name": "Alice", "age": 30, "city": "Portland"}
```

Each entry has a **key** (like `"name"`) and a **value** (like `"Alice"`), separated by a colon. Entries are separated by commas.

### Creating Dictionaries

There are several ways to create a dictionary:

```python
# 1. Literal syntax — the most common way
user = {"name": "Alice", "age": 30}

# 2. The dict() constructor with keyword arguments
user = dict(name="Alice", age=30)

# 3. From a list of tuples
user = dict([("name", "Alice"), ("age", 30)])

# 4. From two lists using zip()
keys = ["name", "age", "city"]
values = ["Alice", 30, "Portland"]
user = dict(zip(keys, values))

# 5. Empty dictionary
empty = {}
empty = dict()
```

All of these produce the same result. Use whichever reads best in context — literal syntax `{}` is by far the most common.

### Accessing Values: `[]` vs `.get()`

You access values by their key, not by an index number:

```python
person = {"name": "Alice", "age": 30, "city": "Portland"}

# Square brackets — raises KeyError if the key doesn't exist
print(person["name"])    # Alice
print(person["phone"])   # KeyError!

# .get() — returns None (or a default) if the key doesn't exist
print(person.get("name"))          # Alice
print(person.get("phone"))        # None
print(person.get("phone", "N/A")) # N/A
```

**When should you use which?**
- Use `[]` when you *know* the key exists (or you *want* the error if it doesn't).
- Use `.get()` when the key might be missing and you want a graceful fallback. This is the safer option in most cases.

### Adding, Updating, and Deleting Entries

Dictionaries are mutable — you can change them after creation:

```python
person = {"name": "Alice", "age": 30}

# Adding a new key-value pair
person["email"] = "alice@example.com"

# Updating an existing value
person["age"] = 31

# Deleting an entry with del
del person["email"]

# .pop() — removes a key and returns its value
age = person.pop("age")          # age = 31, key "age" is gone
missing = person.pop("phone", "N/A")  # returns "N/A", no error

# .popitem() — removes and returns the LAST inserted key-value pair
person["city"] = "Portland"
person["country"] = "USA"
last = person.popitem()  # ("country", "USA")
```

Note: `del` and `.pop()` both raise `KeyError` if the key doesn't exist (unless you give `.pop()` a default value).

### Checking Membership with `in`

The `in` keyword checks if a **key** exists in the dictionary — it does NOT check values:

```python
person = {"name": "Alice", "age": 30}

print("name" in person)     # True
print("phone" in person)    # False
print("Alice" in person)    # False — "Alice" is a value, not a key!

# To check if a value exists, search .values()
print("Alice" in person.values())  # True
```

### Iterating Over Dictionaries

Dictionaries give you three views to iterate over:

```python
person = {"name": "Alice", "age": 30, "city": "Portland"}

# .keys() — iterate over keys (this is also the default)
for key in person:              # same as: for key in person.keys()
    print(key)

# .values() — iterate over values only
for value in person.values():
    print(value)

# .items() — iterate over key-value pairs as tuples
for key, value in person.items():
    print(f"{key}: {value}")
```

`.items()` is the one you'll use most often, since you usually need both the key and the value.

### Useful Methods: `.update()` and `.setdefault()`

```python
# .update() — merge another dictionary into this one
defaults = {"color": "blue", "size": "medium", "theme": "light"}
user_prefs = {"color": "red", "font": "mono"}

defaults.update(user_prefs)
# defaults is now: {"color": "red", "size": "medium", "theme": "light", "font": "mono"}
# Notice "color" was overwritten by the incoming value

# .setdefault() — set a key only if it doesn't already exist
config = {"debug": True}
config.setdefault("debug", False)   # Does nothing — "debug" already exists
config.setdefault("verbose", False) # Adds "verbose": False
print(config)  # {"debug": True, "verbose": False}
```

`.setdefault()` is handy when you want to initialize a key without accidentally overwriting it.

### Dictionary Unpacking with `**`

The `**` operator "unpacks" a dictionary into key-value pairs. This is useful for merging dictionaries or passing them as function arguments:

```python
# Merging dictionaries (Python 3.5+)
defaults = {"color": "blue", "size": "medium"}
overrides = {"color": "red", "font": "mono"}
merged = {**defaults, **overrides}
# {"color": "red", "size": "medium", "font": "mono"}
# Later values win when keys conflict

# The | operator also works for merging (Python 3.9+)
merged = defaults | overrides  # Same result

# Passing dict entries as keyword arguments to a function
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

params = {"name": "Alice", "greeting": "Hey"}
greet(**params)  # Hey, Alice!
```

### Nested Dictionaries

Values can be anything — including other dictionaries:

```python
school = {
    "Alice": {"math": 92, "english": 88, "science": 95},
    "Bob":   {"math": 78, "english": 85, "science": 80},
}

# Access nested values by chaining keys
print(school["Alice"]["math"])  # 92

# Update a nested value
school["Bob"]["math"] = 82

# Add a new student
school["Carol"] = {"math": 90, "english": 91, "science": 87}
```

Be careful with deeply nested dicts — if you're nesting more than 2-3 levels deep, consider whether a class or different data structure might be clearer.

### Dictionary Ordering

Since **Python 3.7**, dictionaries are guaranteed to maintain **insertion order**. This means the order you put items in is the order they come out when you iterate:

```python
d = {}
d["first"] = 1
d["second"] = 2
d["third"] = 3

for key in d:
    print(key)  # Always prints: first, second, third
```

In older Python versions (3.6 and below), dictionaries had no guaranteed order. You don't need to worry about this if you're using modern Python, but you might see `OrderedDict` in older codebases — that was the workaround before 3.7.

### What Can Be a Key?

Dictionary keys must be **hashable** — meaning they're immutable and Python can compute a fixed hash value for them. In practice:

```python
# These work as keys (hashable)
d = {
    "name": "Alice",     # strings
    42: "the answer",    # integers
    3.14: "pi",          # floats
    True: "yes",         # booleans
    (1, 2): "a tuple",   # tuples (if they only contain hashable items)
}

# These do NOT work as keys (unhashable)
d = {[1, 2]: "nope"}       # TypeError — lists are mutable
d = {{}: "nope"}            # TypeError — dicts are mutable
d = {{1, 2}: "nope"}       # TypeError — sets are mutable
```

The rule of thumb: if you can change it, you can't use it as a key. Strings and numbers are the most common key types by far.

### Common Patterns

#### Counting occurrences

```python
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
# {"apple": 3, "banana": 2, "cherry": 1}
```

#### Grouping items

```python
words = ["apple", "avocado", "banana", "blueberry", "cherry"]
groups = {}
for word in words:
    first_letter = word[0]
    groups.setdefault(first_letter, []).append(word)
# {"a": ["apple", "avocado"], "b": ["banana", "blueberry"], "c": ["cherry"]}
```

#### Inverting a dictionary (swapping keys and values)

```python
original = {"a": 1, "b": 2, "c": 3}
inverted = {value: key for key, value in original.items()}
# {1: "a", 2: "b", 3: "c"}
```

Note: inverting only works cleanly when all values are unique. If two keys share a value, one will be lost.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- Dictionaries store **key-value pairs** — use them when you need to look things up by a meaningful name
- Use `.get()` instead of `[]` when a key might not exist — it won't crash your program
- `in` checks **keys**, not values — use `in d.values()` to search values
- `.items()` is your best friend for iterating — it gives you both key and value
- Keys must be hashable (strings, numbers, tuples) — lists and dicts can't be keys
- Since Python 3.7, dictionaries maintain insertion order
- Dictionary unpacking (`**`) and the `|` operator are clean ways to merge dicts
- Common patterns like counting and grouping are much easier with `.get()` and `.setdefault()`
