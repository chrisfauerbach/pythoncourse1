"""
Classes and Objects — Exercises
================================

Practice problems to test your understanding of classes and objects.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""


# =============================================================================
# Exercise 1: Rectangle
#
# Create a Rectangle class with:
#   - __init__ that takes width and height
#   - An area() method that returns width * height
#   - A perimeter() method that returns 2 * (width + height)
#   - A __str__ method that returns "Rectangle(width=W, height=H)"
#
# Then create a 5x3 rectangle and print its area, perimeter, and string form.
#
# Expected output:
#   Rectangle(width=5, height=3)
#   Area: 15
#   Perimeter: 16
# =============================================================================

def exercise_1():
    # YOUR CODE HERE — define the Rectangle class and test it
    pass


# =============================================================================
# Exercise 2: Counter
#
# Create a Counter class with:
#   - __init__ that starts the count at 0
#   - increment() — adds 1
#   - decrement() — subtracts 1 (but never goes below 0)
#   - reset() — sets count back to 0
#   - A value property (read-only) that returns the current count
#
# Then demonstrate: increment 5 times, decrement 2 times, print value,
# reset, print value.
#
# Expected output:
#   After 5 increments and 2 decrements: 3
#   After reset: 0
# =============================================================================

def exercise_2():
    # YOUR CODE HERE — define the Counter class and test it
    pass


# =============================================================================
# Exercise 3: Temperature
#
# Create a Temperature class with:
#   - __init__ that takes a Celsius value
#   - A celsius property with a getter and setter
#     (setter should reject values below -273.15)
#   - A fahrenheit property (read-only) that converts C to F
#     Formula: F = C * 9/5 + 32
#   - A __str__ method like "Temperature(20.0°C / 68.0°F)"
#
# Test with: create at 100°C, print it, change to 0°C, print it,
# then try setting to -300 (should print an error message).
#
# Expected output:
#   Temperature(100.0°C / 212.0°F)
#   Temperature(0.0°C / 32.0°F)
#   Error: Temperature below absolute zero!
# =============================================================================

def exercise_3():
    # YOUR CODE HERE — define the Temperature class and test it
    pass


# =============================================================================
# Exercise 4: Book with @classmethod
#
# Create a Book class with:
#   - __init__ that takes title and author
#   - A @classmethod called from_string that parses "Title - Author"
#     and returns a new Book
#   - A __str__ method that returns '"Title" by Author'
#
# Test with both the normal constructor and from_string.
#
# Expected output:
#   "1984" by George Orwell
#   "Dune" by Frank Herbert
# =============================================================================

def exercise_4():
    # YOUR CODE HERE — define the Book class and test it
    pass


# =============================================================================
# Exercise 5: Student with GPA
#
# Create a Student class with:
#   - __init__ that takes name (grades list starts empty)
#   - add_grade(grade) — appends a grade (0.0 to 4.0 scale)
#     Reject grades outside this range with a printed error.
#   - A gpa property (read-only) that returns the average, or 0.0 if
#     no grades exist
#   - A __str__ method like "Student(Alice, GPA: 3.50)"
#
# Test: create a student, add grades 4.0, 3.5, 3.0, 3.7, then print.
#
# Expected output:
#   Added grade 4.0 for Alice
#   Added grade 3.5 for Alice
#   Added grade 3.0 for Alice
#   Added grade 3.7 for Alice
#   Student(Alice, GPA: 3.55)
# =============================================================================

def exercise_5():
    # YOUR CODE HERE — define the Student class and test it
    pass


# =============================================================================
# Exercise 6: BankAccount with transfer
#
# Create a BankAccount class with:
#   - __init__ that takes owner and optional initial_balance (default 0)
#   - A balance property (read-only — no setter, deposits/withdrawals only)
#   - deposit(amount) — adds to balance (reject non-positive amounts)
#   - withdraw(amount) — subtracts from balance (reject if insufficient funds
#     or non-positive amount)
#   - transfer_to(other_account, amount) — withdraw from self, deposit to other
#   - A __str__ method like "BankAccount(Alice: $1000.00)"
#
# Test: create two accounts, deposit, withdraw, transfer between them.
#
# Expected output:
#   BankAccount(Alice: $1000.00)
#   BankAccount(Bob: $500.00)
#   Alice deposits $500.00
#   Alice withdraws $200.00
#   Alice transfers $300.00 to Bob
#   BankAccount(Alice: $1000.00)
#   BankAccount(Bob: $800.00)
# =============================================================================

def exercise_6():
    # YOUR CODE HERE — define the BankAccount class and test it
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

        def perimeter(self):
            return 2 * (self.width + self.height)

        def __str__(self):
            return f"Rectangle(width={self.width}, height={self.height})"

    r = Rectangle(5, 3)
    print(r)
    print(f"Area: {r.area()}")
    print(f"Perimeter: {r.perimeter()}")


def solution_2():
    class Counter:
        def __init__(self):
            self._count = 0

        def increment(self):
            self._count += 1

        def decrement(self):
            if self._count > 0:
                self._count -= 1

        def reset(self):
            self._count = 0

        @property
        def value(self):
            return self._count

    c = Counter()
    for _ in range(5):
        c.increment()
    for _ in range(2):
        c.decrement()
    print(f"After 5 increments and 2 decrements: {c.value}")

    c.reset()
    print(f"After reset: {c.value}")


def solution_3():
    class Temperature:
        def __init__(self, celsius):
            self._celsius = celsius

        @property
        def celsius(self):
            return self._celsius

        @celsius.setter
        def celsius(self, value):
            if value < -273.15:
                print("Error: Temperature below absolute zero!")
                return
            self._celsius = value

        @property
        def fahrenheit(self):
            return self._celsius * 9 / 5 + 32

        def __str__(self):
            return f"Temperature({self._celsius:.1f}\u00b0C / {self.fahrenheit:.1f}\u00b0F)"

    t = Temperature(100)
    print(t)
    t.celsius = 0
    print(t)
    t.celsius = -300


def solution_4():
    class Book:
        def __init__(self, title, author):
            self.title = title
            self.author = author

        @classmethod
        def from_string(cls, book_string):
            title, author = book_string.split(" - ")
            return cls(title, author)

        def __str__(self):
            return f'"{self.title}" by {self.author}'

    book1 = Book("1984", "George Orwell")
    print(book1)

    book2 = Book.from_string("Dune - Frank Herbert")
    print(book2)


def solution_5():
    class Student:
        def __init__(self, name):
            self.name = name
            self._grades = []

        def add_grade(self, grade):
            if grade < 0.0 or grade > 4.0:
                print(f"Error: Grade {grade} is out of range (0.0 - 4.0)")
                return
            self._grades.append(grade)
            print(f"Added grade {grade} for {self.name}")

        @property
        def gpa(self):
            if not self._grades:
                return 0.0
            return sum(self._grades) / len(self._grades)

        def __str__(self):
            return f"Student({self.name}, GPA: {self.gpa:.2f})"

    s = Student("Alice")
    s.add_grade(4.0)
    s.add_grade(3.5)
    s.add_grade(3.0)
    s.add_grade(3.7)
    print(s)


def solution_6():
    class BankAccount:
        def __init__(self, owner, initial_balance=0):
            self.owner = owner
            self._balance = initial_balance

        @property
        def balance(self):
            return self._balance

        def deposit(self, amount):
            if amount <= 0:
                print("Deposit amount must be positive!")
                return
            self._balance += amount
            print(f"{self.owner} deposits ${amount:.2f}")

        def withdraw(self, amount):
            if amount <= 0:
                print("Withdrawal amount must be positive!")
                return
            if amount > self._balance:
                print(f"Insufficient funds! Balance: ${self._balance:.2f}")
                return
            self._balance -= amount
            print(f"{self.owner} withdraws ${amount:.2f}")

        def transfer_to(self, other, amount):
            if amount <= 0:
                print("Transfer amount must be positive!")
                return
            if amount > self._balance:
                print(f"Insufficient funds! Balance: ${self._balance:.2f}")
                return
            self._balance -= amount
            other._balance += amount
            print(f"{self.owner} transfers ${amount:.2f} to {other.owner}")

        def __str__(self):
            return f"BankAccount({self.owner}: ${self._balance:.2f})"

    alice = BankAccount("Alice", 1000)
    bob = BankAccount("Bob", 500)

    print(alice)
    print(bob)

    alice.deposit(500)
    alice.withdraw(200)
    alice.transfer_to(bob, 300)

    print(alice)
    print(bob)


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Rectangle", exercise_1),
        ("Counter", exercise_2),
        ("Temperature", exercise_3),
        ("Book with @classmethod", exercise_4),
        ("Student with GPA", exercise_5),
        ("BankAccount with transfer", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
