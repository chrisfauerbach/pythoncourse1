"""
Classes and Objects — Example Code
====================================

Run this file:
    python3 example.py

This file demonstrates how to define classes, create objects, and use all the
key features of Object-Oriented Programming in Python.
"""

# -----------------------------------------------------------------------------
# 1. A simple class — defining a Dog
# -----------------------------------------------------------------------------

# A class is a blueprint. Here we define what every Dog should have.

class Dog:
    # Class attribute — shared by ALL dogs
    species = "Canis familiaris"

    def __init__(self, name, breed, age):
        # Instance attributes — unique to each dog
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        """Dogs bark. This is an instance method."""
        print(f"{self.name} says: Woof!")

    def describe(self):
        """Print a summary of this dog."""
        print(f"{self.name} is a {self.age}-year-old {self.breed}")


# Create two separate Dog objects (instances)
rex = Dog("Rex", "German Shepherd", 5)
bella = Dog("Bella", "Golden Retriever", 3)

print("--- 1. A Simple Class ---")
rex.bark()                     # Rex says: Woof!
bella.bark()                   # Bella says: Woof!
rex.describe()                 # Rex is a 5-year-old German Shepherd
bella.describe()               # Bella is a 3-year-old Golden Retriever
print(f"Species: {rex.species}")   # Canis familiaris (class attribute)
print(f"Species: {Dog.species}")   # Same — accessed on the class itself

# -----------------------------------------------------------------------------
# 2. The __init__ constructor and self
# -----------------------------------------------------------------------------

# self refers to the specific object being created or used.
# Python passes it automatically — you just include it as the first parameter.

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []       # Start with an empty list of grades

    def add_grade(self, grade):
        """Add a grade (0-100) to this student's record."""
        self.grades.append(grade)

    def get_average(self):
        """Calculate the average grade."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)


print("\n--- 2. Constructor and self ---")
alice = Student("Alice", "S001")
alice.add_grade(92)
alice.add_grade(88)
alice.add_grade(95)
print(f"{alice.name} (ID: {alice.student_id})")
print(f"Grades: {alice.grades}")
print(f"Average: {alice.get_average():.1f}")

# -----------------------------------------------------------------------------
# 3. Instance attributes vs class attributes
# -----------------------------------------------------------------------------

class Car:
    # Class attribute — keeps count across all Car instances
    total_cars = 0

    def __init__(self, make, model):
        self.make = make       # Instance attribute
        self.model = model     # Instance attribute
        Car.total_cars += 1    # Modify the class attribute


print("\n--- 3. Instance vs Class Attributes ---")
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")
car3 = Car("Ford", "Mustang")

print(f"car1: {car1.make} {car1.model}")    # Toyota Camry
print(f"car2: {car2.make} {car2.model}")    # Honda Civic
print(f"Total cars created: {Car.total_cars}")  # 3

# -----------------------------------------------------------------------------
# 4. __str__ and __repr__
# -----------------------------------------------------------------------------

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """Human-readable — called by print() and str()."""
        return f'"{self.title}" by {self.author}'

    def __repr__(self):
        """Developer-readable — called by repr() and shown in the REPL."""
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"


print("\n--- 4. __str__ and __repr__ ---")
book = Book("1984", "George Orwell", 328)
print(book)            # "1984" by George Orwell  (uses __str__)
print(repr(book))      # Book(title='1984', author='George Orwell', pages=328)

# Handy in lists too — lists use __repr__ for their items
books = [
    Book("1984", "George Orwell", 328),
    Book("Dune", "Frank Herbert", 412),
]
print(books)  # Shows __repr__ for each book inside the list

# -----------------------------------------------------------------------------
# 5. Private by convention — underscores
# -----------------------------------------------------------------------------

class SecretKeeper:
    def __init__(self):
        self.public = "anyone can see this"
        self._internal = "please don't touch (convention)"
        self.__mangled = "name-mangled by Python"

    def reveal_mangled(self):
        """The class itself can access __mangled just fine."""
        return self.__mangled


print("\n--- 5. Private by Convention ---")
sk = SecretKeeper()
print(f"public:   {sk.public}")
print(f"_internal: {sk._internal}")        # Works, but signals "internal"
print(f"__mangled via method: {sk.reveal_mangled()}")
print(f"__mangled via name mangling: {sk._SecretKeeper__mangled}")
# print(sk.__mangled)  # This would raise AttributeError!

# -----------------------------------------------------------------------------
# 6. Properties with @property — getters and setters the Pythonic way
# -----------------------------------------------------------------------------

class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self._balance = initial_balance   # "Private" — use the property instead

    @property
    def balance(self):
        """Read the balance. This is the getter."""
        return self._balance

    @balance.setter
    def balance(self, amount):
        """Set the balance with validation. This is the setter."""
        if amount < 0:
            print("Error: Balance cannot be negative!")
            return
        self._balance = amount

    def deposit(self, amount):
        """Add money to the account."""
        if amount <= 0:
            print("Deposit amount must be positive!")
            return
        self._balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")

    def withdraw(self, amount):
        """Remove money from the account."""
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return
        if amount > self._balance:
            print(f"Insufficient funds! Balance: ${self._balance:.2f}")
            return
        self._balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")

    def __str__(self):
        return f"BankAccount({self.owner}: ${self._balance:.2f})"


print("\n--- 6. Properties (@property) ---")
acct = BankAccount("Alice", 1000)
print(f"Owner: {acct.owner}")
print(f"Balance: ${acct.balance:.2f}")    # Uses the @property getter

acct.deposit(500)                         # Deposited $500.00
acct.withdraw(200)                        # Withdrew $200.00
print(f"Final balance: ${acct.balance:.2f}")

# Try setting an invalid balance — the setter catches it
acct.balance = -100                       # Error: Balance cannot be negative!
print(f"Balance unchanged: ${acct.balance:.2f}")

# -----------------------------------------------------------------------------
# 7. @classmethod — alternative constructors
# -----------------------------------------------------------------------------

class Pet:
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age

    @classmethod
    def from_string(cls, pet_string):
        """Create a Pet from a string like 'Buddy - Dog - 5'."""
        name, animal_type, age = pet_string.split(" - ")
        return cls(name, animal_type, int(age))

    @classmethod
    def new_puppy(cls, name):
        """Shortcut to create a new puppy (always a Dog, age 0)."""
        return cls(name, "Dog", 0)

    def __str__(self):
        return f"{self.name} ({self.animal_type}, age {self.age})"


print("\n--- 7. @classmethod (Alternative Constructors) ---")

# Normal constructor
pet1 = Pet("Whiskers", "Cat", 4)
print(pet1)

# From a string — handy when parsing data from files or user input
pet2 = Pet.from_string("Buddy - Dog - 5")
print(pet2)

# Convenience constructor
pet3 = Pet.new_puppy("Max")
print(pet3)

# -----------------------------------------------------------------------------
# 8. @staticmethod — utility functions in a class
# -----------------------------------------------------------------------------

class DateHelper:
    """A collection of date-related utility methods."""

    @staticmethod
    def is_leap_year(year):
        """Check if a year is a leap year."""
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def days_in_month(month, year):
        """Return the number of days in a given month."""
        if month in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif month in (4, 6, 9, 11):
            return 30
        elif month == 2:
            return 29 if DateHelper.is_leap_year(year) else 28


print("\n--- 8. @staticmethod (Utility Functions) ---")
print(f"2024 is a leap year? {DateHelper.is_leap_year(2024)}")  # True
print(f"2023 is a leap year? {DateHelper.is_leap_year(2023)}")  # False
print(f"Days in Feb 2024: {DateHelper.days_in_month(2, 2024)}")  # 29
print(f"Days in Feb 2023: {DateHelper.days_in_month(2, 2023)}")  # 28

# -----------------------------------------------------------------------------
# 9. Putting it all together — a complete class
# -----------------------------------------------------------------------------

class ShoppingCart:
    """A shopping cart that demonstrates all the concepts together."""

    tax_rate = 0.08   # Class attribute — 8% tax for all carts

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self._items = []   # Private by convention — use methods to modify

    @property
    def total(self):
        """Calculate the total price of all items (read-only property)."""
        return sum(price * qty for _, price, qty in self._items)

    @property
    def total_with_tax(self):
        """Total including tax (read-only property)."""
        return self.total * (1 + self.tax_rate)

    @property
    def item_count(self):
        """How many individual items are in the cart."""
        return sum(qty for _, _, qty in self._items)

    def add_item(self, name, price, quantity=1):
        """Add an item to the cart."""
        self._items.append((name, price, quantity))
        print(f"  Added {quantity}x {name} @ ${price:.2f} each")

    def view_cart(self):
        """Display all items in the cart."""
        if not self._items:
            print("  Cart is empty!")
            return
        for name, price, qty in self._items:
            print(f"  {name:.<30} {qty} x ${price:.2f} = ${price * qty:.2f}")
        print(f"  {'Subtotal':.<30} ${self.total:.2f}")
        print(f"  {'Tax (' + f'{self.tax_rate:.0%}' + ')':.<30} ${self.total * self.tax_rate:.2f}")
        print(f"  {'TOTAL':.<30} ${self.total_with_tax:.2f}")

    @classmethod
    def with_tax_rate(cls, customer_name, tax_rate):
        """Create a cart with a custom tax rate."""
        cart = cls(customer_name)
        cart.tax_rate = tax_rate   # Override for this specific instance
        return cart

    @staticmethod
    def format_price(amount):
        """Format a number as a price string."""
        return f"${amount:,.2f}"

    def __str__(self):
        return f"ShoppingCart({self.customer_name}: {self.item_count} items, {self.format_price(self.total_with_tax)})"

    def __repr__(self):
        return f"ShoppingCart(customer_name='{self.customer_name}', items={len(self._items)})"


print("\n--- 9. Putting It All Together ---")
cart = ShoppingCart("Alice")
cart.add_item("Python Textbook", 49.99)
cart.add_item("Notebook", 4.99, quantity=3)
cart.add_item("Coffee Mug", 12.50)

print()
cart.view_cart()

print()
print(cart)         # Uses __str__
print(repr(cart))   # Uses __repr__

# -----------------------------------------------------------------------------
# Done!
# -----------------------------------------------------------------------------

print()
print("=" * 50)
print("  CLASSES AND OBJECTS COMPLETE!")
print("=" * 50)
print()
print("Now try the exercises in exercises.py!")
