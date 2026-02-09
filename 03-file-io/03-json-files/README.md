# JSON Files

## Objective

Learn how to read, write, and manipulate JSON data in Python using the built-in `json` module. By the end of this lesson you'll be comfortable serializing Python objects to JSON and deserializing JSON back into Python objects.

## Concepts Covered

- What JSON is and why it matters
- Python's `json` module
- Serialization with `json.dumps()` and `json.dump()`
- Deserialization with `json.loads()` and `json.load()`
- Pretty printing with the `indent` parameter
- Python-to-JSON type mapping
- Handling non-serializable types
- Common patterns: config files, API responses

## Prerequisites

- [Reading and Writing Text](../01-reading-writing-text/) and [Dictionaries](../../02-data-structures/02-dictionaries/)

## Lesson

### What Is JSON?

JSON stands for **JavaScript Object Notation**. Despite the name, it has nothing to do with writing JavaScript — it's just a lightweight text format for storing and exchanging data. Think of it as the **lingua franca** of data exchange on the internet.

Every time you hit an API, load a config file for a modern tool, or pass data between services, there's a very good chance JSON is involved. It looks like this:

```json
{
    "name": "Alice",
    "age": 30,
    "languages": ["Python", "JavaScript"],
    "active": true
}
```

If that looks a lot like a Python dictionary — you're right. That's exactly why JSON and Python get along so well.

### Python's `json` Module

Python ships with a `json` module in the standard library. No `pip install` needed:

```python
import json
```

This module gives you four main functions. They come in pairs — one pair works with **strings**, the other works with **files**.

### Serialization: Python Object to JSON

**"Serialization"** is a fancy word for "turn a Python object into a JSON string."

#### `json.dumps()` — to a string

The `s` in `dumps` stands for "string." It takes a Python object and returns a JSON-formatted string:

```python
import json

user = {"name": "Alice", "age": 30, "active": True}
json_string = json.dumps(user)

print(json_string)    # {"name": "Alice", "age": 30, "active": true}
print(type(json_string))  # <class 'str'>
```

Notice that Python's `True` became JSON's `true`. We'll cover the full type mapping below.

#### `json.dump()` — directly to a file

Same idea, but it writes straight to a file object instead of returning a string:

```python
user = {"name": "Alice", "age": 30, "active": True}

with open("user.json", "w") as f:
    json.dump(user, f)
```

That's it — one line and your data is saved to disk.

### Deserialization: JSON to Python Object

**"Deserialization"** is the reverse — turning a JSON string back into a Python object.

#### `json.loads()` — from a string

```python
json_string = '{"name": "Alice", "age": 30, "active": true}'
user = json.loads(json_string)

print(user)           # {'name': 'Alice', 'age': 30, 'active': True}
print(type(user))     # <class 'dict'>
print(user["name"])   # Alice
```

JSON's `true` becomes Python's `True` automatically.

#### `json.load()` — directly from a file

```python
with open("user.json", "r") as f:
    user = json.load(f)

print(user["name"])   # Alice
```

### Quick Summary of the Four Functions

| Function        | Direction           | Works with |
|-----------------|---------------------|------------|
| `json.dumps()`  | Python -> JSON      | Strings    |
| `json.dump()`   | Python -> JSON file | Files      |
| `json.loads()`  | JSON -> Python      | Strings    |
| `json.load()`   | JSON file -> Python | Files      |

Memory trick: the ones with the **`s`** work with **s**trings. The ones without the `s` work with files.

### Pretty Printing with `indent`

By default, `json.dumps()` gives you one long line. Pass `indent` to make it human-readable:

```python
data = {"users": [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]}

# Compact (default)
print(json.dumps(data))

# Pretty-printed with 2-space indent
print(json.dumps(data, indent=2))
```

The pretty version looks like:

```json
{
  "users": [
    {
      "name": "Alice",
      "age": 30
    },
    {
      "name": "Bob",
      "age": 25
    }
  ]
}
```

You can also use `indent` with `json.dump()` when writing to a file. Your future self will thank you.

### Python-to-JSON Type Mapping

Not every Python type has a JSON equivalent. Here's the complete mapping:

| Python            | JSON      | Example Python | Example JSON |
|-------------------|-----------|----------------|--------------|
| `dict`            | object    | `{"a": 1}`     | `{"a": 1}`   |
| `list`, `tuple`   | array     | `[1, 2, 3]`    | `[1, 2, 3]`  |
| `str`             | string    | `"hello"`       | `"hello"`     |
| `int`             | number    | `42`            | `42`          |
| `float`           | number    | `3.14`          | `3.14`        |
| `True`            | `true`    | `True`          | `true`        |
| `False`           | `false`   | `False`         | `false`       |
| `None`            | `null`    | `None`          | `null`        |

That's the full list. Anything not on this list (like `datetime`, `set`, or custom objects) will raise a `TypeError` if you try to serialize it directly.

### Handling Non-Serializable Types

What happens when you try to serialize something JSON doesn't understand?

```python
from datetime import datetime

data = {"event": "login", "timestamp": datetime.now()}
json.dumps(data)  # TypeError: Object of type datetime is not JSON serializable
```

You have a few options:

#### Option 1: The `default` parameter

Pass a function that converts unknown types to something JSON *can* handle:

```python
def json_default(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

data = {"event": "login", "timestamp": datetime.now()}
print(json.dumps(data, default=json_default))
# {"event": "login", "timestamp": "2025-01-15T10:30:00.123456"}
```

#### Option 2: Custom JSONEncoder class

For more control, subclass `json.JSONEncoder`:

```python
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

print(json.dumps(data, cls=CustomEncoder))
```

#### Option 3: Convert before serializing

Sometimes the simplest approach is just to transform your data before passing it to `json.dumps()`:

```python
data = {
    "event": "login",
    "timestamp": datetime.now().isoformat()  # Convert upfront
}
print(json.dumps(data))  # Works fine
```

### Common Patterns

#### Config files

JSON is great for storing application configuration:

```python
# Save config
config = {
    "database": {"host": "localhost", "port": 5432},
    "debug": True,
    "max_retries": 3
}
with open("config.json", "w") as f:
    json.dump(config, f, indent=2)

# Load config
with open("config.json", "r") as f:
    config = json.load(f)

print(config["database"]["host"])  # localhost
```

#### Parsing API responses

When you call a web API, the response is almost always JSON:

```python
import json

# Imagine this came back from an API call
response_text = '{"status": "ok", "results": [{"id": 1, "title": "First Post"}]}'

data = json.loads(response_text)
for result in data["results"]:
    print(f"{result['id']}: {result['title']}")
```

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- JSON is a text-based format for data exchange — it's everywhere
- `json.dumps()` / `json.loads()` work with strings; `json.dump()` / `json.load()` work with files
- Use `indent` to make JSON human-readable
- Python dicts, lists, strings, numbers, booleans, and `None` all map cleanly to JSON
- For non-serializable types like `datetime`, use the `default` parameter or a custom encoder
- Always use `with open(...)` when reading/writing JSON files
