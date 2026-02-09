"""
Dataclasses — Example Code
============================

Run this file:
    python3 example.py

Dataclasses eliminate the boilerplate of writing __init__, __repr__, and __eq__
for classes that primarily hold data. This file walks through everything you
need to know.
"""

from dataclasses import dataclass, field, asdict, astuple

# -----------------------------------------------------------------------------
# 1. The problem — look at all this boilerplate!
# -----------------------------------------------------------------------------

# Without dataclasses, a simple Point class looks like this:

class OldPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"OldPoint(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return isinstance(other, OldPoint) and self.x == other.x and self.y == other.y

print("--- 1. The boilerplate problem ---")
p1 = OldPoint(3, 4)
p2 = OldPoint(3, 4)
print(f"p1 = {p1}")
print(f"p1 == p2: {p1 == p2}")
print("That works, but it took 10 lines of code for two fields!")

# -----------------------------------------------------------------------------
# 2. Basic @dataclass — the same thing in 4 lines
# -----------------------------------------------------------------------------

@dataclass
class Point:
    x: float
    y: float

print("\n--- 2. Basic @dataclass ---")
p1 = Point(3.0, 4.0)
p2 = Point(3.0, 4.0)
p3 = Point(1.0, 2.0)

print(f"p1 = {p1}")              # Auto-generated __repr__
print(f"p1 == p2: {p1 == p2}")   # Auto-generated __eq__ — True
print(f"p1 == p3: {p1 == p3}")   # Different values — False

# You can access fields normally
print(f"p1.x = {p1.x}, p1.y = {p1.y}")

# And modify them (dataclasses are mutable by default)
p1.x = 10.0
print(f"After modification: p1 = {p1}")

# -----------------------------------------------------------------------------
# 3. Type annotations — required but not enforced
# -----------------------------------------------------------------------------

print("\n--- 3. Type annotations ---")

# The annotations are just hints — Python won't stop you from doing this:
weird_point = Point("hello", [1, 2, 3])
print(f"Weird but valid: {weird_point}")
print("Python doesn't enforce types at runtime — that's for tools like mypy.")

# -----------------------------------------------------------------------------
# 4. Default values and field ordering
# -----------------------------------------------------------------------------

@dataclass
class Product:
    name: str             # required (no default)
    price: float          # required (no default)
    quantity: int = 0     # optional (has default)
    on_sale: bool = False # optional (has default)

print("\n--- 4. Default values ---")

# You can provide all fields
laptop = Product("Laptop", 999.99, 50, True)
print(f"Full:    {laptop}")

# Or rely on defaults for the optional ones
book = Product("Python Book", 29.99)
print(f"Minimal: {book}")

# Remember: non-defaults MUST come before defaults!
# This would fail:
#   @dataclass
#   class Bad:
#       name: str = "Unknown"
#       price: float           # Error! No default after a field with default

# -----------------------------------------------------------------------------
# 5. field() function — mutable defaults and more
# -----------------------------------------------------------------------------

@dataclass
class ShoppingCart:
    owner: str
    items: list = field(default_factory=list)      # Each instance gets its own list
    coupons: dict = field(default_factory=dict)     # Each instance gets its own dict
    _total_visits: int = field(default=0, repr=False)  # Hidden from repr output

print("\n--- 5. field() function ---")

cart1 = ShoppingCart("Alice")
cart2 = ShoppingCart("Bob")

# Each cart has its own independent list
cart1.items.append("Laptop")
cart1.items.append("Mouse")
cart2.items.append("Keyboard")

print(f"cart1: {cart1}")
print(f"cart2: {cart2}")
print("Notice _total_visits is hidden from repr!")
print(f"But it's still there: cart1._total_visits = {cart1._total_visits}")

# Using a custom factory function
def default_tags():
    return ["new", "unreviewed"]

@dataclass
class Article:
    title: str
    tags: list = field(default_factory=default_tags)

article = Article("Python Tips")
print(f"\nCustom factory: {article}")

# -----------------------------------------------------------------------------
# 6. Frozen dataclasses — immutability
# -----------------------------------------------------------------------------

@dataclass(frozen=True)
class Coordinate:
    latitude: float
    longitude: float

print("\n--- 6. Frozen dataclasses ---")

nyc = Coordinate(40.7128, -74.0060)
print(f"NYC: {nyc}")

# Trying to modify a frozen dataclass raises an error
try:
    nyc.latitude = 0.0
except AttributeError as e:
    print(f"Can't modify frozen dataclass: {e}")

# Frozen dataclasses are hashable — great for sets and dict keys!
locations = {
    Coordinate(40.7128, -74.0060): "New York",
    Coordinate(51.5074, -0.1278): "London",
    Coordinate(35.6762, 139.6503): "Tokyo",
}
print(f"Locations: {locations}")

# -----------------------------------------------------------------------------
# 7. Post-init processing with __post_init__
# -----------------------------------------------------------------------------

# Validation example
@dataclass
class Color:
    r: int
    g: int
    b: int

    def __post_init__(self):
        for name, value in [("r", self.r), ("g", self.g), ("b", self.b)]:
            if not 0 <= value <= 255:
                raise ValueError(f"{name} must be 0-255, got {value}")

print("\n--- 7. __post_init__ ---")

red = Color(255, 0, 0)
print(f"Valid color: {red}")

try:
    bad_color = Color(300, 0, 0)
except ValueError as e:
    print(f"Validation caught: {e}")

# Computed fields example
@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)       # Not a constructor argument
    perimeter: float = field(init=False)  # Computed automatically

    def __post_init__(self):
        self.area = self.width * self.height
        self.perimeter = 2 * (self.width + self.height)

rect = Rectangle(5.0, 3.0)
print(f"Rectangle: {rect}")
print(f"  area={rect.area}, perimeter={rect.perimeter}")

# -----------------------------------------------------------------------------
# 8. Inheritance with dataclasses
# -----------------------------------------------------------------------------

@dataclass
class Person:
    name: str
    age: int

@dataclass
class Employee(Person):
    company: str
    salary: float

@dataclass
class Manager(Employee):
    department: str
    team_size: int = 0

print("\n--- 8. Inheritance ---")

emp = Employee(name="Alice", age=30, company="Acme Corp", salary=85000.0)
print(f"Employee: {emp}")

mgr = Manager("Bob", 45, "Acme Corp", 120000.0, "Engineering", 12)
print(f"Manager:  {mgr}")

# isinstance still works as expected
print(f"Manager is a Person? {isinstance(mgr, Person)}")
print(f"Manager is an Employee? {isinstance(mgr, Employee)}")

# -----------------------------------------------------------------------------
# 9. Converting to dict and tuple
# -----------------------------------------------------------------------------

print("\n--- 9. asdict() and astuple() ---")

@dataclass
class User:
    name: str
    email: str
    age: int

user = User("Charlie", "charlie@example.com", 28)

# Convert to a dictionary — great for JSON serialization
user_dict = asdict(user)
print(f"As dict:  {user_dict}")
print(f"Type:     {type(user_dict)}")

# Convert to a tuple — useful for database inserts, CSV rows, etc.
user_tuple = astuple(user)
print(f"As tuple: {user_tuple}")
print(f"Type:     {type(user_tuple)}")

# Works with nested dataclasses too!
@dataclass
class Address:
    street: str
    city: str

@dataclass
class Customer:
    name: str
    address: Address

customer = Customer("Dana", Address("123 Main St", "Springfield"))
print(f"\nNested:   {customer}")
print(f"As dict:  {asdict(customer)}")
# Note: nested dataclasses become nested dicts!

# -----------------------------------------------------------------------------
# 10. Comparison and ordering
# -----------------------------------------------------------------------------

@dataclass(order=True)
class Version:
    major: int
    minor: int
    patch: int

print("\n--- 10. Ordering ---")

v1 = Version(1, 9, 9)
v2 = Version(2, 0, 0)
v3 = Version(1, 10, 0)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v3 = {v3}")
print(f"v2 > v1:  {v2 > v1}")   # True — major version is higher
print(f"v3 > v1:  {v3 > v1}")   # True — same major, higher minor

# Sorting a list of versions — just works!
versions = [Version(2, 1, 0), Version(1, 0, 0), Version(1, 9, 5), Version(2, 0, 0)]
print(f"Sorted:   {sorted(versions)}")

# You can control WHAT gets compared using field(compare=False)
@dataclass(order=True)
class Student:
    gpa: float                                        # Compared first (it's first)
    name: str = field(compare=False)                  # Ignored in comparisons

print(f"\nStudents sorted by GPA only:")
students = [Student(3.5, "Alice"), Student(3.9, "Bob"), Student(3.5, "Charlie")]
for s in sorted(students):
    print(f"  {s.name}: {s.gpa}")

# -----------------------------------------------------------------------------
# 11. Slots — memory efficiency (Python 3.10+)
# -----------------------------------------------------------------------------

@dataclass(slots=True)
class SlimPoint:
    x: float
    y: float

print("\n--- 11. Slots ---")

sp = SlimPoint(1.0, 2.0)
print(f"SlimPoint: {sp}")

# With slots, you CAN'T add arbitrary new attributes
try:
    sp.z = 3.0  # type: ignore
except AttributeError as e:
    print(f"Can't add new attributes with slots: {e}")

# Without slots, you can (but probably shouldn't)
regular_point = Point(1.0, 2.0)
regular_point.z = 3.0  # type: ignore  # This works on regular dataclasses
print(f"Regular point got a new attribute: z={regular_point.z}")  # type: ignore

# -----------------------------------------------------------------------------
# 12. Putting it all together — a real-world example
# -----------------------------------------------------------------------------

print("\n--- 12. Real-world example ---")

@dataclass(order=True)
class Task:
    # Priority is first so ordering sorts by priority (lower = more important)
    priority: int
    title: str = field(compare=False)
    done: bool = field(default=False, compare=False)
    tags: list = field(default_factory=list, compare=False, repr=False)

    def complete(self):
        self.done = True

    def __str__(self):
        status = "x" if self.done else " "
        return f"[{status}] (P{self.priority}) {self.title}"

# Create some tasks
tasks = [
    Task(3, "Buy groceries", tags=["personal"]),
    Task(1, "Fix production bug", tags=["work", "urgent"]),
    Task(2, "Write unit tests", tags=["work"]),
    Task(1, "Call the doctor", tags=["personal", "health"]),
]

# Complete one task
tasks[0].complete()

# Sort by priority and display
print("Task list (sorted by priority):")
for task in sorted(tasks):
    print(f"  {task}")

# Convert to dicts for JSON serialization
print("\nAs JSON-ready dicts:")
for task in sorted(tasks):
    print(f"  {asdict(task)}")

# -----------------------------------------------------------------------------
# Done!
# -----------------------------------------------------------------------------

print()
print("=" * 50)
print("  DATACLASSES EXAMPLE COMPLETE!")
print("=" * 50)
print()
print("Dataclasses take the tedium out of data-holding classes.")
print("Try modifying the examples above and run this file again!")
