# Inheritance

## Objective

Understand how classes can inherit from other classes — reusing code, extending behavior, and building clean hierarchies.

## Concepts Covered

- What inheritance is (parent/child, base/derived, superclass/subclass)
- Basic inheritance syntax: `class Child(Parent)`
- What gets inherited (methods, attributes)
- Overriding methods
- `super()` — calling the parent's methods
- The `__init__` chain — extending the parent constructor
- `isinstance()` and `issubclass()`
- Multiple inheritance and Method Resolution Order (MRO)
- Abstract base classes with the `abc` module
- Composition vs inheritance — "has-a" vs "is-a"

## Prerequisites

- Classes, instances, `__init__`, methods (see [01-classes-and-objects](../01-classes-and-objects/))

## Lesson

### What Is Inheritance?

Inheritance lets you create a new class based on an existing one. The new class **inherits** all the methods and attributes of the original, and you can add or change whatever you need.

The terminology comes up a lot, and it all means the same thing:

| Parent term     | Child term     |
|-----------------|----------------|
| Parent class    | Child class    |
| Base class      | Derived class  |
| Superclass      | Subclass       |

Think of it like genetics — a child gets traits from a parent but can develop its own unique traits too.

### Basic Syntax

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

# Dog inherits from Animal
class Dog(Animal):
    pass
```

That `pass` means Dog doesn't add anything new yet — but it already has everything Animal has:

```python
buddy = Dog("Buddy")
print(buddy.name)       # Buddy
print(buddy.speak())    # Buddy makes a sound
```

The parentheses in `class Dog(Animal)` are what tell Python "Dog inherits from Animal."

### What Gets Inherited

When a child class inherits from a parent, it gets:

- **All methods** — instance methods, class methods, static methods
- **All attributes** set in `__init__` (assuming you call the parent's `__init__`)
- **All class-level attributes**

Basically, if the parent has it, the child has it — unless the child explicitly overrides it.

### Overriding Methods

Overriding means defining a method in the child class with the **same name** as one in the parent. The child's version replaces the parent's:

```python
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):          # Overrides Animal.speak()
        return "Woof!"

class Cat(Animal):
    def speak(self):          # Overrides Animal.speak()
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.speak())   # Woof!
print(cat.speak())   # Meow!
```

This is **polymorphism** in action — same method name, different behavior depending on the object's type.

### super() — Calling the Parent's Methods

Sometimes you don't want to completely replace the parent's method — you want to **extend** it. That's where `super()` comes in. It gives you a reference to the parent class:

```python
class Animal:
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):
        parent_says = super().speak()        # Call Animal.speak()
        return f"{parent_says}... actually, Woof!"
```

You'll use `super()` all the time, especially in `__init__`.

### The __init__ Chain

This is the most common use of `super()`. When a child class needs its own `__init__`, you almost always want to call the parent's `__init__` first:

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")   # Call Animal's __init__
        self.breed = breed              # Add something new

buddy = Dog("Buddy", "Golden Retriever")
print(buddy.name)      # Buddy       (from Animal)
print(buddy.species)   # Dog         (from Animal)
print(buddy.breed)     # Golden Retriever (from Dog)
```

If you forget to call `super().__init__()`, the parent's attributes won't be set, and you'll get `AttributeError` when you try to access them.

### isinstance() and issubclass()

Python gives you two functions to check inheritance relationships at runtime:

```python
buddy = Dog("Buddy", "Golden Retriever")

# isinstance() — is this object an instance of this class (or its parents)?
print(isinstance(buddy, Dog))      # True
print(isinstance(buddy, Animal))   # True  (Dog IS an Animal)
print(isinstance(buddy, str))      # False

# issubclass() — is this class a subclass of another?
print(issubclass(Dog, Animal))     # True
print(issubclass(Animal, Dog))     # False (Animal is NOT a Dog)
print(issubclass(Dog, Dog))        # True  (a class is its own subclass)
```

Prefer `isinstance()` over `type()` for type checking — it respects inheritance.

### Multiple Inheritance

Python lets a class inherit from multiple parents:

```python
class Flyer:
    def fly(self):
        return "I can fly!"

class Swimmer:
    def swim(self):
        return "I can swim!"

class Duck(Flyer, Swimmer):
    def quack(self):
        return "Quack!"

donald = Duck()
print(donald.fly())    # I can fly!
print(donald.swim())   # I can swim!
print(donald.quack())  # Quack!
```

#### Method Resolution Order (MRO)

When multiple parents have a method with the same name, Python needs to decide which one to call. It uses the **MRO** — a specific order it searches through classes. You can see it with `.__mro__` or `.mro()`:

```python
print(Duck.__mro__)
# (<class 'Duck'>, <class 'Flyer'>, <class 'Swimmer'>, <class 'object'>)
```

Python searches left to right through the parent list. So if both `Flyer` and `Swimmer` had a `move()` method, `Duck` would use `Flyer.move()` because `Flyer` is listed first.

A word of caution: multiple inheritance can get complicated fast. Many Python developers avoid deep multiple inheritance hierarchies. **Mixins** — small classes that add one specific behavior — are the most common and cleanest use case.

### Abstract Base Classes

Sometimes you want to define a parent class that says "every child **must** implement these methods" — but the parent itself can't provide a useful implementation. That's an abstract base class:

```python
from abc import ABC, abstractmethod

class Shape(ABC):                          # Inherit from ABC
    @abstractmethod                         # Mark as abstract
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# shape = Shape()  # TypeError! Can't instantiate an abstract class

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):                         # MUST implement this
        return 3.14159 * self.radius ** 2

    def perimeter(self):                    # MUST implement this
        return 2 * 3.14159 * self.radius
```

If a child class forgets to implement an abstract method, Python raises a `TypeError` when you try to create an instance. This is great for enforcing contracts — "if you're a Shape, you **must** have `area()` and `perimeter()`."

### Composition vs Inheritance

Inheritance models an **"is-a"** relationship:
- A Dog **is an** Animal
- A Circle **is a** Shape

Composition models a **"has-a"** relationship:
- A Car **has an** Engine
- A Computer **has a** CPU

```python
# Inheritance — "is-a"
class Animal:
    def breathe(self):
        return "Breathing..."

class Dog(Animal):    # Dog IS an Animal
    pass

# Composition — "has-a"
class Engine:
    def start(self):
        return "Vroom!"

class Car:
    def __init__(self):
        self.engine = Engine()    # Car HAS an Engine

    def start(self):
        return self.engine.start()
```

**When to prefer composition:**

- When the relationship is "has-a" rather than "is-a"
- When you want flexibility — you can swap components at runtime
- When inheritance would create awkward hierarchies (is a `DatabaseLogger` really a type of `Database`? Probably not)
- As a general rule of thumb: **favor composition over inheritance** unless inheritance is a natural and obvious fit

Composition tends to produce more flexible, easier-to-maintain code. Use inheritance when there's a clear, logical hierarchy. Use composition when you're assembling objects from parts.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- Inheritance lets a child class reuse and extend a parent class: `class Child(Parent)`
- Child classes inherit all methods and attributes from the parent
- Override a method by defining it again in the child class with the same name
- Use `super()` to call the parent's version of a method — especially in `__init__`
- `isinstance()` checks if an object is an instance of a class (respecting inheritance)
- Multiple inheritance is possible but use it sparingly — prefer mixins for clean design
- Abstract base classes (`ABC` + `@abstractmethod`) enforce that child classes implement required methods
- Composition ("has-a") is often better than inheritance ("is-a") — favor it when the relationship isn't a natural hierarchy
- When in doubt, ask: "Is this thing really a **type of** that thing?" If yes, inherit. If no, compose.
