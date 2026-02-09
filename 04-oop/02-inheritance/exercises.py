"""
Inheritance — Exercises
========================

Practice problems to test your understanding of inheritance.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""

from abc import ABC, abstractmethod


# =============================================================================
# Exercise 1: Shape hierarchy
#
# Create a base class `Shape` with a method `area()` that returns 0.
# Then create two subclasses:
#   - `Circle` with an __init__ that takes `radius`
#     area() should return 3.14159 * radius ** 2
#   - `Rectangle` with an __init__ that takes `width` and `height`
#     area() should return width * height
#
# Create one of each and print their areas.
#
# Expected output:
#   Circle area: 78.53975
#   Rectangle area: 24
#
# =============================================================================

def exercise_1():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Employee hierarchy with super().__init__()
#
# Create a class hierarchy:
#   - `Employee` with __init__(self, name, salary)
#     and a method total_compensation() that returns salary
#   - `Manager` inherits from Employee, adds __init__(self, name, salary, bonus)
#     total_compensation() should return salary + bonus
#   - `Director` inherits from Manager, adds __init__(self, name, salary, bonus, stock_options)
#     total_compensation() should return salary + bonus + stock_options
#
# Use super().__init__() in each child class to call the parent's __init__.
#
# Create one of each and print their total compensation:
#   Alice (Employee): $70000
#   Bob (Manager): $105000
#   Carol (Director): $175000
#
# =============================================================================

def exercise_2():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: Override __str__
#
# Create a base class `Vehicle` with attributes `make` and `year`.
# Give it a __str__ that returns "year make" (e.g., "2024 Toyota").
#
# Create a subclass `Truck` that adds a `bed_size` attribute (e.g., "6ft").
# Override __str__ to return "year make (bed_size bed)" (e.g., "2024 Ford (6ft bed)").
#
# Use super().__init__() in Truck to call Vehicle's __init__.
#
# Create a Vehicle and a Truck, and print both.
#
# Expected output:
#   2024 Toyota
#   2024 Ford (6ft bed)
#
# =============================================================================

def exercise_3():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: isinstance() exploration
#
# Using the Vehicle/Truck classes (redefine them inside this function),
# create a Truck and then print the result of these checks:
#
#   Is truck a Truck?    True
#   Is truck a Vehicle?  True
#   Is Truck a subclass of Vehicle?  True
#   Is Vehicle a subclass of Truck?  False
#
# =============================================================================

def exercise_4():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Abstract base class
#
# Create an abstract base class `Appliance` (inheriting from ABC) with:
#   - An abstract method `turn_on()` that takes no arguments
#   - An abstract method `turn_off()` that takes no arguments
#   - A regular (non-abstract) method `status()` that returns
#     "I am a {class name}" using self.__class__.__name__
#
# Create two concrete subclasses:
#   - `WashingMachine` — turn_on() returns "Washing...", turn_off() returns "Spin cycle complete."
#   - `Microwave` — turn_on() returns "Heating...", turn_off() returns "Ding!"
#
# Create one of each. Print turn_on(), turn_off(), and status() for both.
#
# Expected output:
#   Washing...
#   Spin cycle complete.
#   I am a WashingMachine
#   Heating...
#   Ding!
#   I am a Microwave
#
# =============================================================================

def exercise_5():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: Composition — build a Computer
#
# Create three component classes:
#   - `CPU` with __init__(self, brand, cores) and a describe() method
#     that returns "CPU: brand, cores cores" (e.g., "CPU: Intel, 8 cores")
#   - `Memory` with __init__(self, size_gb) and a describe() method
#     that returns "Memory: size_gbGB" (e.g., "Memory: 16GB")
#   - `Storage` with __init__(self, size_gb, kind) and a describe() method
#     that returns "Storage: size_gbGB kind" (e.g., "Storage: 512GB SSD")
#
# Create a `Computer` class that takes all the parts in __init__
# and stores them as attributes. Give Computer a method `specs()` that
# prints each component's describe() output.
#
# Create a computer and print its specs:
#   My Computer Specs:
#   - CPU: AMD, 12 cores
#   - Memory: 32GB
#   - Storage: 1000GB SSD
#
# =============================================================================

def exercise_6():
    # YOUR CODE HERE
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    class Shape:
        def area(self):
            return 0

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.14159 * self.radius ** 2

    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

    c = Circle(5)
    r = Rectangle(4, 6)
    print(f"Circle area: {c.area()}")
    print(f"Rectangle area: {r.area()}")


def solution_2():
    class Employee:
        def __init__(self, name, salary):
            self.name = name
            self.salary = salary

        def total_compensation(self):
            return self.salary

    class Manager(Employee):
        def __init__(self, name, salary, bonus):
            super().__init__(name, salary)
            self.bonus = bonus

        def total_compensation(self):
            return self.salary + self.bonus

    class Director(Manager):
        def __init__(self, name, salary, bonus, stock_options):
            super().__init__(name, salary, bonus)
            self.stock_options = stock_options

        def total_compensation(self):
            return self.salary + self.bonus + self.stock_options

    emp = Employee("Alice", 70000)
    mgr = Manager("Bob", 90000, 15000)
    director = Director("Carol", 120000, 30000, 25000)

    print(f"{emp.name} (Employee): ${emp.total_compensation()}")
    print(f"{mgr.name} (Manager): ${mgr.total_compensation()}")
    print(f"{director.name} (Director): ${director.total_compensation()}")


def solution_3():
    class Vehicle:
        def __init__(self, make, year):
            self.make = make
            self.year = year

        def __str__(self):
            return f"{self.year} {self.make}"

    class Truck(Vehicle):
        def __init__(self, make, year, bed_size):
            super().__init__(make, year)
            self.bed_size = bed_size

        def __str__(self):
            return f"{self.year} {self.make} ({self.bed_size} bed)"

    v = Vehicle("Toyota", 2024)
    t = Truck("Ford", 2024, "6ft")
    print(v)
    print(t)


def solution_4():
    class Vehicle:
        def __init__(self, make, year):
            self.make = make
            self.year = year

    class Truck(Vehicle):
        def __init__(self, make, year, bed_size):
            super().__init__(make, year)
            self.bed_size = bed_size

    truck = Truck("Ford", 2024, "6ft")
    print(f"Is truck a Truck?    {isinstance(truck, Truck)}")
    print(f"Is truck a Vehicle?  {isinstance(truck, Vehicle)}")
    print(f"Is Truck a subclass of Vehicle?  {issubclass(Truck, Vehicle)}")
    print(f"Is Vehicle a subclass of Truck?  {issubclass(Vehicle, Truck)}")


def solution_5():
    class Appliance(ABC):
        @abstractmethod
        def turn_on(self):
            pass

        @abstractmethod
        def turn_off(self):
            pass

        def status(self):
            return f"I am a {self.__class__.__name__}"

    class WashingMachine(Appliance):
        def turn_on(self):
            return "Washing..."

        def turn_off(self):
            return "Spin cycle complete."

    class Microwave(Appliance):
        def turn_on(self):
            return "Heating..."

        def turn_off(self):
            return "Ding!"

    wm = WashingMachine()
    mw = Microwave()
    print(wm.turn_on())
    print(wm.turn_off())
    print(wm.status())
    print(mw.turn_on())
    print(mw.turn_off())
    print(mw.status())


def solution_6():
    class CPU:
        def __init__(self, brand, cores):
            self.brand = brand
            self.cores = cores

        def describe(self):
            return f"CPU: {self.brand}, {self.cores} cores"

    class Memory:
        def __init__(self, size_gb):
            self.size_gb = size_gb

        def describe(self):
            return f"Memory: {self.size_gb}GB"

    class Storage:
        def __init__(self, size_gb, kind):
            self.size_gb = size_gb
            self.kind = kind

        def describe(self):
            return f"Storage: {self.size_gb}GB {self.kind}"

    class Computer:
        def __init__(self, cpu, memory, storage):
            self.cpu = cpu
            self.memory = memory
            self.storage = storage

        def specs(self):
            print("My Computer Specs:")
            print(f"  - {self.cpu.describe()}")
            print(f"  - {self.memory.describe()}")
            print(f"  - {self.storage.describe()}")

    cpu = CPU("AMD", 12)
    mem = Memory(32)
    disk = Storage(1000, "SSD")
    pc = Computer(cpu, mem, disk)
    pc.specs()


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Shape hierarchy", exercise_1),
        ("Employee hierarchy with super()", exercise_2),
        ("Override __str__", exercise_3),
        ("isinstance() exploration", exercise_4),
        ("Abstract base class", exercise_5),
        ("Composition — build a Computer", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
