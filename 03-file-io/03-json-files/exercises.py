"""
JSON Files — Exercises
========================

Practice problems to test your understanding of JSON in Python.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""

import json
import os
from datetime import datetime, date


# =============================================================================
# Exercise 1: Config round-trip
#
# Create a dictionary called `config` with these keys:
#   - "theme" set to "dark"
#   - "font_size" set to 14
#   - "auto_save" set to True
#   - "recent_files" set to an empty list
#
# Write it to a file called "temp_ex1_config.json" with an indent of 2.
# Then read it back into a variable called `loaded` and print:
#   Theme: dark
#   Font size: 14
#   Auto-save: True
#
# Don't forget to clean up the file when you're done!
# =============================================================================

def exercise_1():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Pretty printer
#
# Given the nested data structure below, convert it to a pretty-printed JSON
# string with 4-space indentation and sorted keys, then print the result.
#
# =============================================================================

def exercise_2():
    data = {
        "school": "Greendale",
        "courses": [
            {"name": "Python 101", "students": 30, "active": True},
            {"name": "Data Science", "students": 25, "active": True},
            {"name": "Underwater Basket Weaving", "students": 5, "active": False},
        ],
        "founded": 1974,
        "mascot": None
    }
    # YOUR CODE HERE — pretty-print the data as JSON
    pass


# =============================================================================
# Exercise 3: List of records round-trip
#
# Create a list of 3 dictionaries, each representing a book with keys:
#   "title", "author", "year", "available"
#
# Convert the list to a JSON string with json.dumps(), then convert it back
# with json.loads(). Print each book in this format:
#   "Title" by Author (Year) - Available/Checked out
#
# =============================================================================

def exercise_3():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: Merge two JSON files
#
# Create two dictionaries:
#   defaults = {"color": "blue", "size": "medium", "verbose": False, "retries": 3}
#   overrides = {"color": "red", "verbose": True, "timeout": 30}
#
# Write each to a separate temp JSON file. Then read BOTH files back in and
# merge them so that overrides take priority over defaults (the final dict
# should have all keys, with overrides winning on conflicts).
#
# Print the merged result as pretty JSON.
# Clean up both temp files.
#
# Hint: dict.update() or {**dict1, **dict2}
# =============================================================================

def exercise_4():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Extract fields from a nested API response
#
# Given the simulated API response below, extract and print:
#   1. The total number of results (from "meta")
#   2. Each product's name and price, formatted as:
#        - Widget A: $9.99
#        - Widget B: $19.99
#        ...
#   3. The names of products that are in stock (in_stock is true)
#
# =============================================================================

def exercise_5():
    api_response = '''
    {
        "meta": {
            "status": "ok",
            "total_results": 4,
            "page": 1
        },
        "products": [
            {"id": 1, "name": "Widget A", "price": 9.99, "in_stock": true},
            {"id": 2, "name": "Widget B", "price": 19.99, "in_stock": false},
            {"id": 3, "name": "Gadget X", "price": 49.99, "in_stock": true},
            {"id": 4, "name": "Gadget Y", "price": 29.99, "in_stock": true}
        ]
    }
    '''
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: Custom JSON encoder for dates
#
# Create a custom JSONEncoder subclass called DateEncoder that:
#   - Converts datetime objects to ISO format strings
#   - Converts date objects to ISO format strings (just the date part)
#   - Falls back to the default behavior for anything else
#
# Test it with the data below and print the pretty JSON output.
# =============================================================================

def exercise_6():
    data = {
        "event": "Python Meetup",
        "created_at": datetime(2025, 3, 15, 18, 30, 0),
        "event_date": date(2025, 4, 1),
        "attendees": ["Alice", "Bob", "Charlie"],
        "virtual": False
    }
    # YOUR CODE HERE — define DateEncoder and use it
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    config = {
        "theme": "dark",
        "font_size": 14,
        "auto_save": True,
        "recent_files": []
    }

    filename = "temp_ex1_config.json"

    # Write to file
    with open(filename, "w") as f:
        json.dump(config, f, indent=2)

    # Read it back
    with open(filename, "r") as f:
        loaded = json.load(f)

    print(f"Theme: {loaded['theme']}")
    print(f"Font size: {loaded['font_size']}")
    print(f"Auto-save: {loaded['auto_save']}")

    # Clean up
    os.remove(filename)


def solution_2():
    data = {
        "school": "Greendale",
        "courses": [
            {"name": "Python 101", "students": 30, "active": True},
            {"name": "Data Science", "students": 25, "active": True},
            {"name": "Underwater Basket Weaving", "students": 5, "active": False},
        ],
        "founded": 1974,
        "mascot": None
    }
    pretty = json.dumps(data, indent=4, sort_keys=True)
    print(pretty)


def solution_3():
    books = [
        {"title": "Dune", "author": "Frank Herbert", "year": 1965, "available": True},
        {"title": "Neuromancer", "author": "William Gibson", "year": 1984, "available": False},
        {"title": "Snow Crash", "author": "Neal Stephenson", "year": 1992, "available": True},
    ]

    # Convert to JSON string and back
    json_string = json.dumps(books, indent=2)
    loaded_books = json.loads(json_string)

    for book in loaded_books:
        status = "Available" if book["available"] else "Checked out"
        print(f'"{book["title"]}" by {book["author"]} ({book["year"]}) - {status}')


def solution_4():
    defaults = {"color": "blue", "size": "medium", "verbose": False, "retries": 3}
    overrides = {"color": "red", "verbose": True, "timeout": 30}

    defaults_file = "temp_ex4_defaults.json"
    overrides_file = "temp_ex4_overrides.json"

    # Write both to files
    with open(defaults_file, "w") as f:
        json.dump(defaults, f)
    with open(overrides_file, "w") as f:
        json.dump(overrides, f)

    # Read both back
    with open(defaults_file, "r") as f:
        loaded_defaults = json.load(f)
    with open(overrides_file, "r") as f:
        loaded_overrides = json.load(f)

    # Merge — overrides win on conflicts
    merged = {**loaded_defaults, **loaded_overrides}
    print(json.dumps(merged, indent=2))

    # Clean up
    os.remove(defaults_file)
    os.remove(overrides_file)


def solution_5():
    api_response = '''
    {
        "meta": {
            "status": "ok",
            "total_results": 4,
            "page": 1
        },
        "products": [
            {"id": 1, "name": "Widget A", "price": 9.99, "in_stock": true},
            {"id": 2, "name": "Widget B", "price": 19.99, "in_stock": false},
            {"id": 3, "name": "Gadget X", "price": 49.99, "in_stock": true},
            {"id": 4, "name": "Gadget Y", "price": 29.99, "in_stock": true}
        ]
    }
    '''
    data = json.loads(api_response)

    # 1. Total results
    print(f"Total results: {data['meta']['total_results']}")

    # 2. Each product's name and price
    print("\nAll products:")
    for product in data["products"]:
        print(f"  - {product['name']}: ${product['price']:.2f}")

    # 3. Products in stock
    in_stock = [p["name"] for p in data["products"] if p["in_stock"]]
    print(f"\nIn stock: {', '.join(in_stock)}")


def solution_6():
    class DateEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            if isinstance(obj, date):
                return obj.isoformat()
            return super().default(obj)

    data = {
        "event": "Python Meetup",
        "created_at": datetime(2025, 3, 15, 18, 30, 0),
        "event_date": date(2025, 4, 1),
        "attendees": ["Alice", "Bob", "Charlie"],
        "virtual": False
    }

    result = json.dumps(data, cls=DateEncoder, indent=2)
    print(result)


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Config round-trip", exercise_1),
        ("Pretty printer", exercise_2),
        ("List of records round-trip", exercise_3),
        ("Merge two JSON files", exercise_4),
        ("Extract fields from API response", exercise_5),
        ("Custom JSON encoder for dates", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
