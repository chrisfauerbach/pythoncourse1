"""
JSON Files — Example Code
============================

Run this file:
    python3 example.py

Learn how to read, write, and manipulate JSON data in Python. This file is
completely self-contained — it creates its own sample files and cleans up
after itself.
"""

import json
import os
from datetime import datetime

# -----------------------------------------------------------------------------
# 1. json.dumps() — Python object to JSON string (serialization)
# -----------------------------------------------------------------------------

# Start with a regular Python dictionary
user = {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com",
    "active": True,
    "bio": None,             # None becomes null in JSON
    "scores": [95, 87, 92],  # Lists become JSON arrays
}

# Convert to a JSON string
json_string = json.dumps(user)
print("1. json.dumps() — Python to JSON string")
print(f"   Type: {type(json_string)}")
print(f"   Result: {json_string}")
print()

# -----------------------------------------------------------------------------
# 2. json.loads() — JSON string to Python object (deserialization)
# -----------------------------------------------------------------------------

# Start with a JSON string (imagine this came from an API or a file)
raw_json = '{"city": "Portland", "population": 652503, "sunny": false}'

# Convert back to a Python dictionary
city_data = json.loads(raw_json)
print("2. json.loads() — JSON string to Python")
print(f"   Type: {type(city_data)}")
print(f"   City: {city_data['city']}")
print(f"   Population: {city_data['population']:,}")
print(f"   Sunny: {city_data['sunny']}")  # JSON false -> Python False
print()

# -----------------------------------------------------------------------------
# 3. Pretty printing with indent
# -----------------------------------------------------------------------------

# Without indent — one long line, hard to read
compact = json.dumps(user)

# With indent=2 — nicely formatted, great for humans
pretty = json.dumps(user, indent=2)

# sort_keys puts keys in alphabetical order — handy for diffs
sorted_pretty = json.dumps(user, indent=2, sort_keys=True)

print("3. Pretty printing with indent")
print(f"   Compact:  {compact[:60]}...")
print()
print("   Pretty (indent=2):")
for line in pretty.split("\n"):
    print(f"   {line}")
print()
print("   With sort_keys=True:")
for line in sorted_pretty.split("\n"):
    print(f"   {line}")
print()

# -----------------------------------------------------------------------------
# 4. json.dump() — write directly to a file
# -----------------------------------------------------------------------------

# Create a sample config dictionary
config = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp_db"
    },
    "debug": True,
    "max_retries": 3,
    "allowed_origins": ["http://localhost:3000", "https://myapp.com"]
}

# Write it to a file — use indent so the file is readable
config_file = "temp_config.json"
with open(config_file, "w") as f:
    json.dump(config, f, indent=2)

print("4. json.dump() — write to file")
print(f"   Wrote config to '{config_file}'")

# Let's peek at what the file looks like
with open(config_file, "r") as f:
    contents = f.read()
print("   File contents:")
for line in contents.split("\n"):
    print(f"   {line}")
print()

# -----------------------------------------------------------------------------
# 5. json.load() — read directly from a file
# -----------------------------------------------------------------------------

# Read the config back in
with open(config_file, "r") as f:
    loaded_config = json.load(f)

print("5. json.load() — read from file")
print(f"   Type: {type(loaded_config)}")
print(f"   App: {loaded_config['app_name']} v{loaded_config['version']}")
print(f"   DB host: {loaded_config['database']['host']}")
print(f"   Debug: {loaded_config['debug']}")
print(f"   Origins: {loaded_config['allowed_origins']}")
print()

# -----------------------------------------------------------------------------
# 6. Python <-> JSON type mapping
# -----------------------------------------------------------------------------

# Let's see every type conversion in action
type_demo = {
    "string": "hello",          # str    -> string
    "integer": 42,              # int    -> number
    "float": 3.14,              # float  -> number
    "bool_true": True,          # True   -> true
    "bool_false": False,        # False  -> false
    "null_value": None,         # None   -> null
    "list": [1, 2, 3],          # list   -> array
    "nested_dict": {"a": 1},    # dict   -> object
    "tuple_to_array": (4, 5),   # tuple  -> array (tuples become arrays!)
}

print("6. Python <-> JSON type mapping")
json_output = json.dumps(type_demo, indent=2)
for line in json_output.split("\n"):
    print(f"   {line}")

# Important: tuples become arrays, and when you load them back, they stay lists!
roundtrip = json.loads(json_output)
print()
print(f"   Original tuple: {type_demo['tuple_to_array']} (type: {type(type_demo['tuple_to_array']).__name__})")
print(f"   After roundtrip: {roundtrip['tuple_to_array']} (type: {type(roundtrip['tuple_to_array']).__name__})")
print()

# -----------------------------------------------------------------------------
# 7. Handling non-serializable types with `default`
# -----------------------------------------------------------------------------

print("7. Handling non-serializable types")

# This would crash: json.dumps({"timestamp": datetime.now()})
# Let's fix it with a default function

def json_default(obj):
    """Convert non-serializable types to something JSON can handle."""
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, set):
        return sorted(list(obj))  # Convert sets to sorted lists
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

event = {
    "action": "user_login",
    "timestamp": datetime(2025, 6, 15, 10, 30, 0),
    "tags": {"important", "auth", "security"},  # sets aren't serializable!
}

json_output = json.dumps(event, default=json_default, indent=2)
print("   Event with datetime and set:")
for line in json_output.split("\n"):
    print(f"   {line}")
print()

# -----------------------------------------------------------------------------
# 8. Custom JSONEncoder class
# -----------------------------------------------------------------------------

print("8. Custom JSONEncoder class")

class CustomEncoder(json.JSONEncoder):
    """A reusable encoder that handles datetime and set objects."""
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, set):
            return sorted(list(obj))
        return super().default(obj)

# Now you can use cls= instead of default=
json_output = json.dumps(event, cls=CustomEncoder, indent=2)
print("   Same result using cls=CustomEncoder:")
for line in json_output.split("\n"):
    print(f"   {line}")
print()

# -----------------------------------------------------------------------------
# 9. Common pattern: working with a list of records
# -----------------------------------------------------------------------------

print("9. Common pattern: list of records")

# A list of dictionaries — very common when working with APIs or databases
users = [
    {"id": 1, "name": "Alice", "role": "admin"},
    {"id": 2, "name": "Bob", "role": "editor"},
    {"id": 3, "name": "Charlie", "role": "viewer"},
]

# Write all users to a file
users_file = "temp_users.json"
with open(users_file, "w") as f:
    json.dump(users, f, indent=2)

# Read them back
with open(users_file, "r") as f:
    loaded_users = json.load(f)

print(f"   Loaded {len(loaded_users)} users from '{users_file}':")
for u in loaded_users:
    print(f"   - {u['name']} ({u['role']})")
print()

# -----------------------------------------------------------------------------
# 10. Common pattern: parsing an API response
# -----------------------------------------------------------------------------

print("10. Common pattern: parsing an API response")

# Simulate a typical JSON API response
api_response = json.dumps({
    "status": "success",
    "count": 3,
    "data": {
        "users": [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"},
            {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
        ]
    },
    "meta": {
        "page": 1,
        "total_pages": 5
    }
})

# Parse the response
data = json.loads(api_response)

# Navigate the nested structure
if data["status"] == "success":
    for user in data["data"]["users"]:
        print(f"   {user['name']}: {user['email']}")
    print(f"   (Page {data['meta']['page']} of {data['meta']['total_pages']})")
print()

# -----------------------------------------------------------------------------
# 11. Cleanup — remove the temp files we created
# -----------------------------------------------------------------------------

print("11. Cleanup")
for temp_file in [config_file, users_file]:
    if os.path.exists(temp_file):
        os.remove(temp_file)
        print(f"   Removed '{temp_file}'")
print()

# -----------------------------------------------------------------------------
# 12. Putting it all together
# -----------------------------------------------------------------------------

print("=" * 50)
print("   JSON FILES EXAMPLE COMPLETE!")
print("=" * 50)
print()
print("Remember:")
print("  dumps/loads = strings  (s for string)")
print("  dump/load   = files")
print("  indent=2    = pretty printing")
print("  default=    = handle custom types")
