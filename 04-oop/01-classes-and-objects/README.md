# Classes and Objects

## Objective

Understand the foundation of Object-Oriented Programming in Python — how to define classes, create objects, and bundle data with behavior into clean, reusable structures.

## Concepts Covered

- What OOP is and why it matters
- Defining a class with the `class` keyword
- The `__init__` method (constructor)
- `self` — what it is and why every method needs it
- Instance attributes vs class attributes
- Instance methods
- Creating objects (instantiation)
- Accessing attributes and calling methods (dot notation)
- The `__str__` and `__repr__` methods
- Private by convention: `_single_underscore` and `__double_underscore`
- Properties with `@property`
- Class methods (`@classmethod`) and static methods (`@staticmethod`)

## Prerequisites

- [Section 01: Fundamentals](../../01-fundamentals/) — especially functions

## Lesson

### What Is OOP and Why Does It Matter?

Object-Oriented Programming is about bundling **data** and **behavior** together into a single unit called an **object**. Instead of having loose variables and functions floating around, you group related things together.

Think about a bank account. Without OOP, you'd have:

```python
# Scattered data and functions — hard to manage
account_name = "Alice"
account_balance = 1000.0

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    return balance - amount
```

With OOP, everything about a bank account lives in one place:

```python
account = BankAccount("Alice", 1000.0)
account.deposit(500)
account.withdraw(200)
print(account.balance)  # 1300.0
```

The data (name, balance) and the behavior (deposit, withdraw) are bundled together. That's the core idea.

### Defining a Class

A class is a **blueprint** for creating objects. You define it with the `class` keyword:

```python
class Dog:
    pass  # An empty class — valid but not useful yet
```

By convention, class names use **PascalCase** (capitalize each word, no underscores): `Dog`, `BankAccount`, `StudentRecord`.

### The `__init__` Method (Constructor)

When you create a new object, Python calls the `__init__` method automatically. This is where you set up the object's initial state:

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
```

`__init__` is called the **constructor**. It runs every time you create a new Dog. Those double underscores on each side are called "dunder" (double-under) — you'll see a few of these special methods throughout the course.

### `self` — What It Is and Why Every Method Needs It

`self` is a reference to **the specific object** that's calling the method. Every instance method must have `self` as its first parameter. Python passes it automatically — you never pass it yourself:

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name    # self.name belongs to THIS specific dog
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")

# When you call rex.bark(), Python translates it to Dog.bark(rex)
rex = Dog("Rex", "German Shepherd")
rex.bark()  # Rex says: Woof!
```

The name `self` is just a convention — you *could* call it anything — but always use `self`. Everyone expects it, and breaking that convention will confuse every Python developer who reads your code.

### Instance Attributes vs Class Attributes

**Instance attributes** belong to a specific object. They're set on `self`, usually inside `__init__`:

```python
class Dog:
    def __init__(self, name):
        self.name = name  # Instance attribute — different for each dog
```

**Class attributes** are shared by ALL instances. They're defined directly in the class body:

```python
class Dog:
    species = "Canis familiaris"  # Class attribute — same for every dog

    def __init__(self, name):
        self.name = name  # Instance attribute — unique to each dog

rex = Dog("Rex")
print(rex.species)    # Canis familiaris
print(Dog.species)    # Canis familiaris — you can access it on the class too
```

Class attributes are great for constants or defaults that apply to every instance.

### Instance Methods

Any function defined inside a class that takes `self` as its first parameter is an **instance method**. It can access and modify the object's data:

```python
class Dog:
    def __init__(self, name, energy=100):
        self.name = name
        self.energy = energy

    def play(self, minutes):
        self.energy -= minutes * 2
        print(f"{self.name} played for {minutes} min. Energy: {self.energy}")

    def rest(self, minutes):
        self.energy += minutes
        print(f"{self.name} rested for {minutes} min. Energy: {self.energy}")
```

### Creating Objects (Instantiation)

You create an object by calling the class like a function. This is called **instantiation** — you're creating an **instance** of the class:

```python
rex = Dog("Rex")
bella = Dog("Bella")
```

`rex` and `bella` are two separate objects. Each has its own `name` and `energy`. Changing one doesn't affect the other.

### Accessing Attributes and Calling Methods (Dot Notation)

Use a dot `.` to access an object's attributes and call its methods:

```python
print(rex.name)     # Access attribute: Rex
print(rex.energy)   # Access attribute: 100
rex.play(20)        # Call method: Rex played for 20 min. Energy: 60
```

You can also modify attributes directly:

```python
rex.name = "T-Rex"  # This works, but be careful — see Properties below
```

### The `__str__` and `__repr__` Methods

These dunder methods control how your object appears as text. We'll cover magic methods in depth in a later lesson, but here's the quick version:

- **`__str__`** is for a nice, human-readable string. Called by `print()` and `str()`.
- **`__repr__`** is for an unambiguous, developer-friendly string. Called in the REPL and by `repr()`.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"{self.name} the {self.breed}"

    def __repr__(self):
        return f"Dog(name='{self.name}', breed='{self.breed}')"

rex = Dog("Rex", "German Shepherd")
print(rex)        # Rex the German Shepherd  (__str__)
print(repr(rex))  # Dog(name='Rex', breed='German Shepherd')  (__repr__)
```

A good rule of thumb: always define `__repr__`. Define `__str__` too if you want a friendlier display. If only `__repr__` is defined, Python uses it for `print()` as well.

### Private by Convention: `_single` and `__double` Underscore

Python doesn't have truly private attributes like Java or C++. Instead, it uses **naming conventions**:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance      # "Private by convention" — please don't touch
        self.__secret = "hidden"     # Name-mangled by Python
```

**Single underscore `_balance`**: A polite hint to other developers — "this is internal, don't access it directly." Nothing actually prevents access, but it signals intent.

**Double underscore `__secret`**: Python performs **name mangling** — it renames it to `_BankAccount__secret` behind the scenes. This prevents accidental name collisions in subclasses. It's NOT for security — it's a mechanism for avoiding attribute name conflicts.

```python
acct = BankAccount(1000)
print(acct._balance)             # Works — just a convention
# print(acct.__secret)           # AttributeError!
print(acct._BankAccount__secret) # Works — but you really shouldn't do this
```

### Properties with `@property`

Properties let you use method logic behind a clean attribute-style syntax. They're the Pythonic way to do getters and setters:

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        """Get the temperature in Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Set the temperature, with validation."""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Get the temperature in Fahrenheit (read-only)."""
        return self._celsius * 9 / 5 + 32

temp = Temperature(100)
print(temp.celsius)      # 100  — calls the getter
print(temp.fahrenheit)   # 212.0
temp.celsius = 25        # Calls the setter with validation
# temp.celsius = -300    # Would raise ValueError
```

Notice how the user interacts with `temp.celsius` as if it were a simple attribute, but behind the scenes there's validation logic. That's the beauty of properties.

### Class Methods and Static Methods

**`@classmethod`** receives the **class** as its first argument (called `cls` by convention) instead of an instance. Great for alternative constructors:

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    @classmethod
    def from_string(cls, dog_string):
        """Create a Dog from a string like 'Rex - German Shepherd'"""
        name, breed = dog_string.split(" - ")
        return cls(name, breed)  # cls(...) creates a new instance

rex = Dog.from_string("Rex - German Shepherd")
```

**`@staticmethod`** doesn't receive the instance or the class. It's just a regular function that lives inside the class for organizational purposes:

```python
class MathHelper:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

print(MathHelper.is_even(4))  # True
```

Use `@staticmethod` when the method doesn't need access to the instance (`self`) or the class (`cls`) but logically belongs with the class.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- A **class** is a blueprint; an **object** is an instance of that blueprint
- `__init__` sets up the initial state of a new object
- `self` refers to the current instance — every instance method needs it as the first parameter
- **Instance attributes** (`self.x`) are unique to each object; **class attributes** are shared by all
- Use `__str__` for human-friendly output and `__repr__` for developer-friendly output
- Prefix attributes with `_` to signal "internal use" — it's a convention, not a lock
- `@property` lets you add logic (like validation) while keeping clean attribute-style syntax
- `@classmethod` is for alternative constructors; `@staticmethod` is for utility functions that belong to the class
