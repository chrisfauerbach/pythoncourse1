"""
Dataclasses — Exercises
========================

Practice problems to test your understanding of dataclasses.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""

from dataclasses import dataclass, field, asdict


# =============================================================================
# Exercise 1: Basic Product dataclass
#
# Create a dataclass called `Product` with these fields:
#   - name (str) — required
#   - price (float) — required
#   - quantity (int) — defaults to 0
#
# Add a method `total_value` that returns price * quantity.
#
# Create two products and print them:
#   Product(name='Laptop', price=999.99, quantity=5) -> total: 4999.95
#   Product(name='Mouse', price=24.99, quantity=0) -> total: 0.0
#
# =============================================================================

def exercise_1():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: RGB Color with validation
#
# Create a dataclass called `Color` with fields r, g, b (all int).
#
# Use __post_init__ to validate that each value is between 0 and 255.
# Raise a ValueError with a descriptive message if any value is out of range.
#
# Test it by creating:
#   Color(255, 128, 0)   -> should work
#   Color(300, 0, 0)     -> should raise ValueError
#
# Print the valid color, and catch/print the error for the invalid one.
#
# =============================================================================

def exercise_2():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: Immutable Coordinate
#
# Create a FROZEN dataclass called `Coordinate` with:
#   - latitude (float)
#   - longitude (float)
#
# Create a coordinate for Paris (48.8566, 2.3522).
# Print it.
# Try to change latitude to 0.0 — catch the error and print it.
# Prove it's hashable by adding two coordinates to a set and printing the set.
#
# =============================================================================

def exercise_3():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: Inventory with default_factory
#
# Create a dataclass called `Inventory` with:
#   - name (str) — required
#   - items (list) — defaults to empty list using field(default_factory=...)
#
# Add a method `add_item(item: str)` that appends to items.
# Add a method `summary()` that returns a string like:
#   "Warehouse has 3 items"
#
# Create two separate inventories, add different items to each.
# Print both to prove they have independent item lists.
#
# =============================================================================

def exercise_4():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Dataclass hierarchy (Person -> Employee)
#
# Create a dataclass `Person` with:
#   - name (str)
#   - age (int)
#
# Create a dataclass `Employee` that inherits from Person and adds:
#   - company (str)
#   - salary (float)
#   - active (bool) — defaults to True
#
# Create an Employee and print it.
# Show that isinstance(employee, Person) is True.
# Convert it to a dict using asdict() and print the dict.
#
# =============================================================================

def exercise_5():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: Sortable TodoItem with asdict
#
# Create a dataclass with order=True called `TodoItem` with:
#   - priority (int) — used for ordering (lower number = higher priority)
#   - title (str) — NOT used for ordering (use field(compare=False))
#   - done (bool) — defaults to False, NOT used for ordering
#
# Create this list of todos:
#   TodoItem(3, "Buy groceries")
#   TodoItem(1, "Fix critical bug")
#   TodoItem(2, "Write tests")
#   TodoItem(1, "Reply to urgent email")
#
# Sort the list, then convert each item to a dict using asdict().
# Print the sorted list of dicts.
#
# Expected: items with priority 1 come first, then 2, then 3.
#
# =============================================================================

def exercise_6():
    # YOUR CODE HERE
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    @dataclass
    class Product:
        name: str
        price: float
        quantity: int = 0

        def total_value(self):
            return self.price * self.quantity

    laptop = Product("Laptop", 999.99, 5)
    mouse = Product("Mouse", 24.99)
    print(f"{laptop} -> total: {laptop.total_value():.2f}")
    print(f"{mouse} -> total: {mouse.total_value():.1f}")


def solution_2():
    @dataclass
    class Color:
        r: int
        g: int
        b: int

        def __post_init__(self):
            for name, value in [("r", self.r), ("g", self.g), ("b", self.b)]:
                if not 0 <= value <= 255:
                    raise ValueError(f"{name} must be 0-255, got {value}")

    valid = Color(255, 128, 0)
    print(f"Valid color: {valid}")

    try:
        bad = Color(300, 0, 0)
    except ValueError as e:
        print(f"Caught error: {e}")


def solution_3():
    @dataclass(frozen=True)
    class Coordinate:
        latitude: float
        longitude: float

    paris = Coordinate(48.8566, 2.3522)
    print(f"Paris: {paris}")

    try:
        paris.latitude = 0.0
    except AttributeError as e:
        print(f"Can't modify frozen: {e}")

    coords = {Coordinate(48.8566, 2.3522), Coordinate(40.7128, -74.0060)}
    print(f"Set of coordinates: {coords}")


def solution_4():
    @dataclass
    class Inventory:
        name: str
        items: list = field(default_factory=list)

        def add_item(self, item: str):
            self.items.append(item)

        def summary(self):
            return f"{self.name} has {len(self.items)} items"

    warehouse = Inventory("Warehouse")
    store = Inventory("Store")

    warehouse.add_item("Laptop")
    warehouse.add_item("Mouse")
    warehouse.add_item("Keyboard")
    store.add_item("Phone")

    print(f"{warehouse} -> {warehouse.summary()}")
    print(f"{store} -> {store.summary()}")


def solution_5():
    @dataclass
    class Person:
        name: str
        age: int

    @dataclass
    class Employee(Person):
        company: str
        salary: float
        active: bool = True

    emp = Employee("Alice", 30, "Acme Corp", 85000.0)
    print(f"Employee: {emp}")
    print(f"Is a Person? {isinstance(emp, Person)}")
    print(f"As dict: {asdict(emp)}")


def solution_6():
    @dataclass(order=True)
    class TodoItem:
        priority: int
        title: str = field(compare=False)
        done: bool = field(default=False, compare=False)

    todos = [
        TodoItem(3, "Buy groceries"),
        TodoItem(1, "Fix critical bug"),
        TodoItem(2, "Write tests"),
        TodoItem(1, "Reply to urgent email"),
    ]

    sorted_todos = sorted(todos)
    print("Sorted todos as dicts:")
    for todo in sorted_todos:
        print(f"  {asdict(todo)}")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Basic Product dataclass", exercise_1),
        ("RGB Color with validation", exercise_2),
        ("Immutable Coordinate", exercise_3),
        ("Inventory with default_factory", exercise_4),
        ("Dataclass hierarchy", exercise_5),
        ("Sortable TodoItem with asdict", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
