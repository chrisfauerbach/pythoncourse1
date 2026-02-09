# Dataclasses

## Objective

Learn how Python's `dataclasses` module eliminates boilerplate code when creating classes that mainly hold data, and understand when to use them over regular classes or named tuples.

## Concepts Covered

- The problem dataclasses solve (boilerplate `__init__`, `__repr__`, `__eq__`)
- The `@dataclass` decorator
- Type annotations in dataclasses
- Default values and field ordering
- The `field()` function and `default_factory`
- Frozen dataclasses for immutability
- Post-init processing with `__post_init__`
- Inheritance with dataclasses
- Converting to dict/tuple with `asdict()` and `astuple()`
- Comparison and ordering with `order=True`
- Slots for memory efficiency (`slots=True`)
- Dataclass vs namedtuple vs regular class

## Prerequisites

- [Classes and Objects](../01-classes-and-objects/)
- [Inheritance](../02-inheritance/)
- [Magic Methods](../03-magic-methods/)
- Basic understanding of type annotations

## Lesson

### The Problem: So Much Boilerplate

Let's say you want a class to represent a point in 2D space. With a regular class, you'd write something like this:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y
```

That's 10 lines of code for a class that just stores two numbers. And you haven't even added things like hashing, ordering, or conversion to dictionaries yet. Multiply this by every data-holding class in your project, and you've got a lot of repetitive code.

This is the exact problem dataclasses solve.

### Basic @dataclass Usage

The `dataclasses` module (built into Python 3.7+) lets you write the same thing like this:

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
```

That's it. Four lines. Python automatically generates `__init__`, `__repr__`, and `__eq__` for you. You get all of this for free:

```python
p = Point(3.0, 4.0)
print(p)            # Point(x=3.0, y=4.0)
print(p == Point(3.0, 4.0))  # True
```

### Type Annotations in Dataclasses

Notice the `x: float` and `y: float` syntax. Dataclasses **require** type annotations for every field — that's how Python knows which fields to include. But here's the important part: **the types are not enforced at runtime.** They're just hints.

```python
@dataclass
class Point:
    x: float
    y: float

p = Point("hello", [1, 2, 3])  # No error! Python doesn't check types at runtime
```

The annotations are documentation for you and your tools (like mypy or your IDE). Python itself won't stop you from passing the wrong type.

If you need a field without a meaningful type, you can use `typing.Any`:

```python
from typing import Any

@dataclass
class Container:
    value: Any
```

### Default Values and Field Ordering

You can give fields default values, just like function arguments:

```python
@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0
    on_sale: bool = False
```

There's one important rule: **fields with defaults must come after fields without defaults.** This is the same rule as function parameters — you can't have a required argument after an optional one.

```python
# This WORKS — non-defaults first, then defaults
@dataclass
class Product:
    name: str        # required
    price: float     # required
    quantity: int = 0     # optional
    on_sale: bool = False # optional

# This FAILS — TypeError
@dataclass
class BadProduct:
    name: str = "Unknown"  # default
    price: float           # no default — can't come after a default!
```

### The field() Function — Mutable Defaults

Here's a classic Python trap. You should **never** use a mutable object (like a list or dict) as a default value:

```python
# DON'T DO THIS — Python will actually block this with a TypeError!
@dataclass
class BadInventory:
    items: list = []
```

Python's dataclasses are smart enough to stop you. Instead, use `field()` with `default_factory`:

```python
from dataclasses import dataclass, field

@dataclass
class Inventory:
    items: list = field(default_factory=list)
    metadata: dict = field(default_factory=dict)
```

`default_factory` takes a callable (like `list`, `dict`, or any function) and calls it fresh for each new instance. So every `Inventory` gets its own empty list.

The `field()` function has other useful parameters too:

```python
@dataclass
class User:
    name: str
    email: str
    _login_count: int = field(default=0, repr=False)   # hidden from repr
    _id: str = field(default="", compare=False)         # ignored in == checks
```

### Frozen Dataclasses (Immutability)

Sometimes you want objects that can't be changed after creation. Use `frozen=True`:

```python
@dataclass(frozen=True)
class Coordinate:
    latitude: float
    longitude: float

c = Coordinate(40.7128, -74.0060)
c.latitude = 0  # FrozenInstanceError! Can't modify frozen dataclass
```

Frozen dataclasses are also automatically hashable, so you can use them as dictionary keys or put them in sets:

```python
locations = {Coordinate(40.7128, -74.0060): "New York City"}
```

### Post-Init Processing with __post_init__

What if you need to validate data or compute a field after initialization? That's what `__post_init__` is for. It runs right after the auto-generated `__init__`:

```python
@dataclass
class Color:
    r: int
    g: int
    b: int

    def __post_init__(self):
        for name, value in [("r", self.r), ("g", self.g), ("b", self.b)]:
            if not 0 <= value <= 255:
                raise ValueError(f"{name} must be 0-255, got {value}")
```

You can also use it to compute derived fields. Use `field(init=False)` for fields that shouldn't be constructor arguments:

```python
@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)  # calculated, not passed in

    def __post_init__(self):
        self.area = self.width * self.height
```

### Inheritance with Dataclasses

Dataclasses support inheritance. The child class gets all the parent's fields, plus its own:

```python
@dataclass
class Person:
    name: str
    age: int

@dataclass
class Employee(Person):
    company: str
    salary: float

emp = Employee(name="Alice", age=30, company="Acme", salary=85000)
print(emp)  # Employee(name='Alice', age=30, company='Acme', salary=85000)
```

Watch out for the default-ordering rule with inheritance. If the parent has fields with defaults, the child's fields (without defaults) would break the ordering rule. Plan your field defaults carefully.

### Converting to dict and tuple

The `asdict()` and `astuple()` functions convert dataclass instances into plain Python data structures:

```python
from dataclasses import asdict, astuple

@dataclass
class Point:
    x: float
    y: float

p = Point(3.0, 4.0)
print(asdict(p))    # {'x': 3.0, 'y': 4.0}
print(astuple(p))   # (3.0, 4.0)
```

This is incredibly handy for serialization — turning your objects into JSON, saving to a database, or passing data to functions that expect plain dicts.

### Comparison and Ordering

By default, dataclasses generate `__eq__` (equality comparison). If you also want `<`, `<=`, `>`, and `>=`, add `order=True`:

```python
@dataclass(order=True)
class Version:
    major: int
    minor: int
    patch: int

print(Version(2, 0, 0) > Version(1, 9, 9))  # True
```

Ordering compares fields in the order they're defined — so `major` is compared first, then `minor`, then `patch`. It works like tuple comparison.

### Slots (Python 3.10+)

By default, Python objects store their attributes in a dictionary (`__dict__`). For dataclasses with many instances, you can save memory with `slots=True`:

```python
@dataclass(slots=True)
class Point:
    x: float
    y: float
```

Slots are more memory-efficient and slightly faster for attribute access. The tradeoff is that you can't add new attributes to the instance after creation (but for data classes, that's usually fine).

### Dataclass vs Namedtuple vs Regular Class

When should you use what? Here's a quick guide:

| Feature | `@dataclass` | `NamedTuple` | Regular class |
|---|---|---|---|
| Mutable by default | Yes | No (immutable) | Yes |
| Can add methods | Yes | Yes (limited) | Yes |
| Inheritance | Full support | Limited | Full support |
| Default values | Yes | Yes | Yes |
| Type annotations | Required | Required | Optional |
| Memory efficient | With `slots=True` | Yes (tuple-based) | No |
| Dict/JSON conversion | `asdict()` | `_asdict()` | Manual |
| Best for | Most data classes | Simple immutable records | Complex behavior + data |

**Use `@dataclass`** when you need a class that's primarily about storing data, especially if you want mutability, inheritance, or validation.

**Use `NamedTuple`** when you need a lightweight, immutable record and want tuple compatibility (unpacking, indexing).

**Use a regular class** when the class has complex behavior that goes well beyond storing data — like managing resources, complex state machines, or when you need fine-grained control over every magic method.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- `@dataclass` auto-generates `__init__`, `__repr__`, and `__eq__` from type-annotated fields
- Type annotations are required for dataclass fields but **not enforced** at runtime
- Fields with defaults must come after fields without defaults — same rule as function parameters
- Use `field(default_factory=list)` for mutable defaults — never use `[]` or `{}` directly
- `frozen=True` makes instances immutable and hashable
- `__post_init__` lets you validate data or compute derived fields after initialization
- `asdict()` and `astuple()` convert instances to plain dicts and tuples
- `order=True` enables comparison operators based on field order
- `slots=True` (Python 3.10+) saves memory for classes with many instances
- Dataclasses hit the sweet spot between namedtuples (too simple) and full classes (too much boilerplate)
