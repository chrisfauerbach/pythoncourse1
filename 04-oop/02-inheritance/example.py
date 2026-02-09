"""
Inheritance — Example Code
============================

Run this file:
    python3 example.py

This file demonstrates class inheritance in Python — from the basics
all the way through abstract classes and composition.
"""

from abc import ABC, abstractmethod

# -----------------------------------------------------------------------------
# 1. Basic inheritance — a child class gets everything from the parent
# -----------------------------------------------------------------------------

class Animal:
    """A simple base class representing any animal."""

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f"{self.name} makes a sound"

    def describe(self):
        return f"{self.name} is a {self.species}"


# Dog inherits from Animal — it gets __init__, speak(), and describe() for free
class Dog(Animal):
    pass


# Let's see it in action
print("=" * 50)
print("1. BASIC INHERITANCE")
print("=" * 50)

buddy = Dog("Buddy", "Dog")
print(buddy.speak())       # Inherited from Animal
print(buddy.describe())    # Inherited from Animal
print()

# -----------------------------------------------------------------------------
# 2. Overriding methods — giving the child its own version
# -----------------------------------------------------------------------------

class Cat(Animal):
    """Cat overrides speak() to say something cat-like."""

    def speak(self):
        # This REPLACES Animal.speak() for all Cat instances
        return f"{self.name} says Meow!"


class Dog2(Animal):
    """Dog2 overrides speak() to say something dog-like."""

    def speak(self):
        return f"{self.name} says Woof!"


print("=" * 50)
print("2. OVERRIDING METHODS")
print("=" * 50)

cat = Cat("Whiskers", "Cat")
dog = Dog2("Rex", "Dog")

print(cat.speak())     # Cat's version: Whiskers says Meow!
print(dog.speak())     # Dog2's version: Rex says Woof!
print(cat.describe())  # Still uses Animal.describe() — not overridden
print()

# Polymorphism: same method name, different behavior
animals = [Cat("Luna", "Cat"), Dog2("Max", "Dog"), Cat("Milo", "Cat")]
for animal in animals:
    print(f"  {animal.speak()}")
print()

# -----------------------------------------------------------------------------
# 3. super() — extending the parent's __init__
# -----------------------------------------------------------------------------

class Pet(Animal):
    """Pet extends Animal with an owner attribute."""

    def __init__(self, name, species, owner):
        # Call Animal's __init__ to set name and species
        super().__init__(name, species)
        # Then set our own new attribute
        self.owner = owner

    def describe(self):
        # Extend the parent's describe() method
        base = super().describe()
        return f"{base}, owned by {self.owner}"


print("=" * 50)
print("3. super() — EXTENDING THE PARENT")
print("=" * 50)

pet = Pet("Goldie", "Fish", "Alice")
print(pet.name)        # From Animal (via super().__init__)
print(pet.species)     # From Animal (via super().__init__)
print(pet.owner)       # From Pet
print(pet.describe())  # Pet's extended version
print()

# -----------------------------------------------------------------------------
# 4. Multi-level inheritance — grandparent → parent → child
# -----------------------------------------------------------------------------

class GuideDog(Pet):
    """A guide dog is a specific kind of pet."""

    def __init__(self, name, owner, handler):
        super().__init__(name, "Dog", owner)
        self.handler = handler

    def describe(self):
        base = super().describe()
        return f"{base}, guided by {self.handler}"


print("=" * 50)
print("4. MULTI-LEVEL INHERITANCE")
print("=" * 50)

gd = GuideDog("Shadow", "Service Org", "Bob")
print(gd.describe())
print(f"  Name: {gd.name}, Species: {gd.species}, Owner: {gd.owner}, Handler: {gd.handler}")
print()

# -----------------------------------------------------------------------------
# 5. isinstance() and issubclass()
# -----------------------------------------------------------------------------

print("=" * 50)
print("5. isinstance() AND issubclass()")
print("=" * 50)

print(f"Is gd a GuideDog?  {isinstance(gd, GuideDog)}")    # True
print(f"Is gd a Pet?       {isinstance(gd, Pet)}")          # True
print(f"Is gd an Animal?   {isinstance(gd, Animal)}")       # True
print(f"Is gd a Cat?       {isinstance(gd, Cat)}")          # False
print()
print(f"Is GuideDog a subclass of Pet?    {issubclass(GuideDog, Pet)}")      # True
print(f"Is GuideDog a subclass of Animal? {issubclass(GuideDog, Animal)}")   # True
print(f"Is Animal a subclass of Pet?      {issubclass(Animal, Pet)}")        # False
print()

# -----------------------------------------------------------------------------
# 6. Multiple inheritance — inheriting from more than one parent
# -----------------------------------------------------------------------------

class Flyable:
    """Mixin class that adds flying ability."""

    def fly(self):
        return f"{self.name} takes to the sky!"


class Swimmable:
    """Mixin class that adds swimming ability."""

    def swim(self):
        return f"{self.name} dives into the water!"


class Duck(Animal, Flyable, Swimmable):
    """A duck is an animal that can fly AND swim."""

    def speak(self):
        return f"{self.name} says Quack!"


print("=" * 50)
print("6. MULTIPLE INHERITANCE")
print("=" * 50)

donald = Duck("Donald", "Duck")
print(donald.speak())      # From Duck (overridden)
print(donald.fly())        # From Flyable mixin
print(donald.swim())       # From Swimmable mixin
print(donald.describe())   # From Animal (inherited)
print()

# The MRO — the order Python searches for methods
print("Duck's MRO (Method Resolution Order):")
for cls in Duck.__mro__:
    print(f"  {cls.__name__}")
print()

# -----------------------------------------------------------------------------
# 7. Abstract base classes — enforcing a contract
# -----------------------------------------------------------------------------

class Shape(ABC):
    """Abstract base class. You can't create a Shape directly —
    you must create a subclass that implements area() and perimeter()."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass

    # Non-abstract methods are totally fine — children inherit these
    def describe(self):
        return f"{self.__class__.__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"


class Circle(Shape):
    """Circle must implement area() and perimeter()."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    """Rectangle must implement area() and perimeter()."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


print("=" * 50)
print("7. ABSTRACT BASE CLASSES")
print("=" * 50)

# This would raise TypeError:
# shape = Shape()  # Can't instantiate abstract class Shape

circle = Circle(5)
rect = Rectangle(4, 7)

print(circle.describe())   # Uses the inherited describe() method
print(rect.describe())

# Polymorphism with abstract classes — all Shapes have area() and perimeter()
shapes = [Circle(3), Rectangle(2, 5), Circle(10), Rectangle(8, 3)]
print("\nAll shapes:")
for shape in shapes:
    print(f"  {shape.describe()}")
print()

# -----------------------------------------------------------------------------
# 8. Composition — "has-a" instead of "is-a"
# -----------------------------------------------------------------------------

class Engine:
    """An engine component."""

    def __init__(self, horsepower):
        self.horsepower = horsepower
        self.running = False

    def start(self):
        self.running = True
        return f"Engine ({self.horsepower}hp) started"

    def stop(self):
        self.running = False
        return f"Engine ({self.horsepower}hp) stopped"


class GPS:
    """A GPS navigation component."""

    def __init__(self, brand):
        self.brand = brand

    def navigate(self, destination):
        return f"{self.brand} GPS: Navigating to {destination}"


class Car:
    """A car is COMPOSED of an engine and GPS — it HAS these parts.
    It doesn't inherit from Engine or GPS."""

    def __init__(self, make, model, horsepower, gps_brand):
        self.make = make
        self.model = model
        # Composition: Car HAS an Engine and HAS a GPS
        self.engine = Engine(horsepower)
        self.gps = GPS(gps_brand)

    def start(self):
        result = self.engine.start()
        return f"{self.make} {self.model}: {result}"

    def drive_to(self, destination):
        if not self.engine.running:
            return "Start the engine first!"
        return self.gps.navigate(destination)

    def stop(self):
        result = self.engine.stop()
        return f"{self.make} {self.model}: {result}"


print("=" * 50)
print("8. COMPOSITION — 'HAS-A' RELATIONSHIPS")
print("=" * 50)

car = Car("Toyota", "Camry", 203, "Garmin")
print(car.start())
print(car.drive_to("the beach"))
print(car.stop())
print()

# The benefit: you can easily swap components
car.gps = GPS("TomTom")   # Swap to a different GPS at runtime
print(car.start())
print(car.drive_to("the mountains"))
print(car.stop())
print()

# -----------------------------------------------------------------------------
# 9. Putting it all together
# -----------------------------------------------------------------------------

print("=" * 50)
print("9. PUTTING IT ALL TOGETHER")
print("=" * 50)
print()
print("Inheritance is one of the core pillars of OOP.")
print("Use it when there's a clear 'is-a' relationship.")
print("Use composition when there's a 'has-a' relationship.")
print("And remember: favor composition over inheritance when in doubt!")
print()
print("=" * 50)
print("   INHERITANCE EXAMPLE COMPLETE!")
print("=" * 50)
