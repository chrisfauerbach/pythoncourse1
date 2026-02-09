"""
SQLAlchemy — Exercises
=======================

Practice problems to test your understanding of SQLAlchemy ORM.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""

import sys

try:
    from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, func, and_, or_
    from sqlalchemy.orm import declarative_base, Session, relationship
except ImportError:
    print("SQLAlchemy is not installed. Run: pip install sqlalchemy")
    print("Then try again!")
    sys.exit(0)


# =============================================================================
# Exercise 1: Define a Product model
#
# Create a Product model with the following columns:
#   - id (Integer, primary key)
#   - name (String, required)
#   - price (Float, required)
#   - stock (Integer, default=0)
#
# Then:
#   1. Create an in-memory database and tables
#   2. Add 3 products: ("Laptop", 999.99, 10), ("Mouse", 24.99, 50), ("Keyboard", 79.99, 30)
#   3. Print all products
#   4. Query products with price > 50
#   5. Update the laptop stock to 8
#   6. Delete the mouse
#   7. Print remaining products
# =============================================================================

def exercise_1():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Filtering and ordering
#
# Using the same Product model from Exercise 1, create a database with these products:
#   ("Monitor", 299.99, 15)
#   ("Webcam", 89.99, 25)
#   ("Headphones", 149.99, 40)
#   ("USB Cable", 9.99, 100)
#   ("Desk Lamp", 34.99, 20)
#
# Then:
#   1. Find all products priced between 30 and 150 (inclusive)
#   2. Find products with stock > 30, ordered by price (descending)
#   3. Count how many products have stock >= 20
#   4. Calculate the average price of all products
#   5. Find the most expensive product
# =============================================================================

def exercise_2():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: One-to-many relationship
#
# Create two models:
#   - Customer: id, name, email
#   - Order: id, order_number, total, customer_id (foreign key)
#
# Set up a one-to-many relationship (one customer, many orders).
#
# Then:
#   1. Create 2 customers
#   2. Create 3 orders for customer 1 and 2 orders for customer 2
#   3. Print each customer and their orders
#   4. Find the customer with the most orders
#   5. Calculate total revenue per customer
# =============================================================================

def exercise_3():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: Complex queries
#
# Using the Customer/Order models from Exercise 3, add more data:
#   - Customer "Alice" with orders: 150.00, 200.00, 75.50
#   - Customer "Bob" with orders: 300.00, 125.00
#   - Customer "Carol" with orders: 50.00
#
# Then:
#   1. Find customers who have placed more than 2 orders
#   2. Find customers with total spending > 200
#   3. Find the average order value across all customers
#   4. List customers ordered by total spending (descending)
#   5. Find customers with any order > 250
# =============================================================================

def exercise_4():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Many-to-many relationship
#
# Create a many-to-many relationship between Student and Course:
#   - Student: id, name
#   - Course: id, title, credits
#   - Association table: student_courses
#
# Then:
#   1. Create 3 students: Alice, Bob, Carol
#   2. Create 4 courses: Python (3), Databases (4), Web Dev (3), AI (4)
#   3. Enroll:
#      - Alice in Python, Databases, AI
#      - Bob in Python, Web Dev
#      - Carol in all courses
#   4. Print each student with their courses
#   5. Find students taking more than 3 courses
#   6. Calculate total credits for each student
#   7. Find courses with more than 2 students
# =============================================================================

def exercise_5():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: Complete inventory system
#
# Build a complete inventory system with:
#   - Category: id, name
#   - Product: id, name, price, stock, category_id
#   - Supplier: id, name, email
#   - ProductSupplier (many-to-many): product_id, supplier_id, cost
#
# Create:
#   - 2 categories: Electronics, Office
#   - 4 products in various categories
#   - 2 suppliers
#   - Link products to suppliers with costs
#
# Then query:
#   1. All products in "Electronics"
#   2. Products that need restocking (stock < 20)
#   3. Total inventory value per category (stock * price)
#   4. Suppliers for a specific product
#   5. Most expensive product
#   6. Average stock across all products
# =============================================================================

def exercise_6():
    # YOUR CODE HERE
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    Base = declarative_base()

    class Product(Base):
        __tablename__ = "products"
        id = Column(Integer, primary_key=True)
        name = Column(String, nullable=False)
        price = Column(Float, nullable=False)
        stock = Column(Integer, default=0)

        def __repr__(self):
            return f"<Product(name='{self.name}', price={self.price}, stock={self.stock})>"

    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    session = Session(engine)

    # Add products
    products = [
        Product(name="Laptop", price=999.99, stock=10),
        Product(name="Mouse", price=24.99, stock=50),
        Product(name="Keyboard", price=79.99, stock=30),
    ]
    session.add_all(products)
    session.commit()

    print("All products:")
    for p in session.query(Product).all():
        print(f"  {p}")

    print("\nProducts > $50:")
    for p in session.query(Product).filter(Product.price > 50).all():
        print(f"  {p}")

    # Update laptop stock
    laptop = session.query(Product).filter(Product.name == "Laptop").first()
    laptop.stock = 8
    session.commit()
    print(f"\nUpdated laptop stock to {laptop.stock}")

    # Delete mouse
    mouse = session.query(Product).filter(Product.name == "Mouse").first()
    session.delete(mouse)
    session.commit()

    print("\nRemaining products:")
    for p in session.query(Product).all():
        print(f"  {p}")

    session.close()


def solution_2():
    Base = declarative_base()

    class Product(Base):
        __tablename__ = "products"
        id = Column(Integer, primary_key=True)
        name = Column(String, nullable=False)
        price = Column(Float, nullable=False)
        stock = Column(Integer, default=0)

        def __repr__(self):
            return f"<Product(name='{self.name}', ${self.price}, stock={self.stock})>"

    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    session = Session(engine)

    products = [
        Product(name="Monitor", price=299.99, stock=15),
        Product(name="Webcam", price=89.99, stock=25),
        Product(name="Headphones", price=149.99, stock=40),
        Product(name="USB Cable", price=9.99, stock=100),
        Product(name="Desk Lamp", price=34.99, stock=20),
    ]
    session.add_all(products)
    session.commit()

    # 1. Products between $30 and $150
    print("Products $30-$150:")
    results = session.query(Product).filter(
        and_(Product.price >= 30, Product.price <= 150)
    ).all()
    for p in results:
        print(f"  {p}")

    # 2. Stock > 30, ordered by price descending
    print("\nHigh stock (>30), by price:")
    results = session.query(Product).filter(
        Product.stock > 30
    ).order_by(Product.price.desc()).all()
    for p in results:
        print(f"  {p}")

    # 3. Count products with stock >= 20
    count = session.query(Product).filter(Product.stock >= 20).count()
    print(f"\nProducts with stock >= 20: {count}")

    # 4. Average price
    avg = session.query(func.avg(Product.price)).scalar()
    print(f"Average price: ${avg:.2f}")

    # 5. Most expensive
    most_expensive = session.query(Product).order_by(Product.price.desc()).first()
    print(f"Most expensive: {most_expensive}")

    session.close()


def solution_3():
    Base = declarative_base()

    class Customer(Base):
        __tablename__ = "customers"
        id = Column(Integer, primary_key=True)
        name = Column(String)
        email = Column(String)
        orders = relationship("Order", back_populates="customer")

        def __repr__(self):
            return f"<Customer(name='{self.name}')>"

    class Order(Base):
        __tablename__ = "orders"
        id = Column(Integer, primary_key=True)
        order_number = Column(String)
        total = Column(Float)
        customer_id = Column(Integer, ForeignKey("customers.id"))
        customer = relationship("Customer", back_populates="orders")

        def __repr__(self):
            return f"<Order(#{self.order_number}, ${self.total})>"

    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    session = Session(engine)

    # Create customers
    customer1 = Customer(name="John", email="john@example.com")
    customer2 = Customer(name="Jane", email="jane@example.com")

    # Create orders
    customer1.orders = [
        Order(order_number="ORD001", total=150.00),
        Order(order_number="ORD002", total=200.00),
        Order(order_number="ORD003", total=75.50),
    ]

    customer2.orders = [
        Order(order_number="ORD004", total=300.00),
        Order(order_number="ORD005", total=125.00),
    ]

    session.add_all([customer1, customer2])
    session.commit()

    # Print customers and their orders
    print("Customers and orders:")
    for customer in session.query(Customer).all():
        print(f"{customer.name} ({len(customer.orders)} orders):")
        for order in customer.orders:
            print(f"  {order}")

    # Find customer with most orders
    customers = session.query(Customer).all()
    most_orders = max(customers, key=lambda c: len(c.orders))
    print(f"\nMost orders: {most_orders.name} with {len(most_orders.orders)} orders")

    # Total revenue per customer
    print("\nRevenue per customer:")
    for customer in customers:
        total = sum(order.total for order in customer.orders)
        print(f"  {customer.name}: ${total:.2f}")

    session.close()


def solution_4():
    Base = declarative_base()

    class Customer(Base):
        __tablename__ = "customers"
        id = Column(Integer, primary_key=True)
        name = Column(String)
        email = Column(String)
        orders = relationship("Order", back_populates="customer")

    class Order(Base):
        __tablename__ = "orders"
        id = Column(Integer, primary_key=True)
        order_number = Column(String)
        total = Column(Float)
        customer_id = Column(Integer, ForeignKey("customers.id"))
        customer = relationship("Customer", back_populates="orders")

    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    session = Session(engine)

    # Add data
    alice = Customer(name="Alice", email="alice@example.com")
    alice.orders = [
        Order(order_number="A1", total=150.00),
        Order(order_number="A2", total=200.00),
        Order(order_number="A3", total=75.50),
    ]

    bob = Customer(name="Bob", email="bob@example.com")
    bob.orders = [
        Order(order_number="B1", total=300.00),
        Order(order_number="B2", total=125.00),
    ]

    carol = Customer(name="Carol", email="carol@example.com")
    carol.orders = [Order(order_number="C1", total=50.00)]

    session.add_all([alice, bob, carol])
    session.commit()

    # 1. Customers with > 2 orders
    print("Customers with > 2 orders:")
    customers = session.query(Customer).all()
    for c in customers:
        if len(c.orders) > 2:
            print(f"  {c.name}: {len(c.orders)} orders")

    # 2. Customers with total spending > 200
    print("\nCustomers with spending > $200:")
    for c in customers:
        total = sum(o.total for o in c.orders)
        if total > 200:
            print(f"  {c.name}: ${total:.2f}")

    # 3. Average order value
    all_orders = session.query(Order).all()
    avg = sum(o.total for o in all_orders) / len(all_orders)
    print(f"\nAverage order value: ${avg:.2f}")

    # 4. Customers by total spending
    print("\nCustomers by spending:")
    spending = [(c, sum(o.total for o in c.orders)) for c in customers]
    spending.sort(key=lambda x: x[1], reverse=True)
    for c, total in spending:
        print(f"  {c.name}: ${total:.2f}")

    # 5. Customers with any order > 250
    print("\nCustomers with order > $250:")
    for c in customers:
        if any(o.total > 250 for o in c.orders):
            print(f"  {c.name}")

    session.close()


def solution_5():
    from sqlalchemy import Table

    Base = declarative_base()

    # Association table
    student_courses = Table(
        "student_courses",
        Base.metadata,
        Column("student_id", ForeignKey("students.id")),
        Column("course_id", ForeignKey("courses.id")),
    )

    class Student(Base):
        __tablename__ = "students"
        id = Column(Integer, primary_key=True)
        name = Column(String)
        courses = relationship("Course", secondary=student_courses, back_populates="students")

        def __repr__(self):
            return f"<Student(name='{self.name}')>"

    class Course(Base):
        __tablename__ = "courses"
        id = Column(Integer, primary_key=True)
        title = Column(String)
        credits = Column(Integer)
        students = relationship("Student", secondary=student_courses, back_populates="courses")

        def __repr__(self):
            return f"<Course(title='{self.title}', {self.credits} credits)>"

    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    session = Session(engine)

    # Create students
    alice = Student(name="Alice")
    bob = Student(name="Bob")
    carol = Student(name="Carol")

    # Create courses
    python = Course(title="Python", credits=3)
    databases = Course(title="Databases", credits=4)
    webdev = Course(title="Web Dev", credits=3)
    ai = Course(title="AI", credits=4)

    # Enroll students
    alice.courses = [python, databases, ai]
    bob.courses = [python, webdev]
    carol.courses = [python, databases, webdev, ai]

    session.add_all([alice, bob, carol])
    session.commit()

    # Print students and courses
    print("Students and their courses:")
    for student in session.query(Student).all():
        print(f"{student.name}:")
        for course in student.courses:
            print(f"  - {course.title} ({course.credits} credits)")
        print()

    # Students taking > 3 courses
    print("Students taking > 3 courses:")
    for s in session.query(Student).all():
        if len(s.courses) > 3:
            print(f"  {s.name}: {len(s.courses)} courses")

    # Total credits per student
    print("\nTotal credits per student:")
    for s in session.query(Student).all():
        total = sum(c.credits for c in s.courses)
        print(f"  {s.name}: {total} credits")

    # Courses with > 2 students
    print("\nCourses with > 2 students:")
    for c in session.query(Course).all():
        if len(c.students) > 2:
            print(f"  {c.title}: {len(c.students)} students")

    session.close()


def solution_6():
    from sqlalchemy import Table

    Base = declarative_base()

    # Many-to-many association table with extra data
    product_suppliers = Table(
        "product_suppliers",
        Base.metadata,
        Column("product_id", ForeignKey("products.id")),
        Column("supplier_id", ForeignKey("suppliers.id")),
        Column("cost", Float),
    )

    class Category(Base):
        __tablename__ = "categories"
        id = Column(Integer, primary_key=True)
        name = Column(String)
        products = relationship("Product", back_populates="category")

    class Product(Base):
        __tablename__ = "products"
        id = Column(Integer, primary_key=True)
        name = Column(String)
        price = Column(Float)
        stock = Column(Integer)
        category_id = Column(Integer, ForeignKey("categories.id"))
        category = relationship("Category", back_populates="products")

        def __repr__(self):
            return f"<Product(name='{self.name}', ${self.price}, stock={self.stock})>"

    class Supplier(Base):
        __tablename__ = "suppliers"
        id = Column(Integer, primary_key=True)
        name = Column(String)
        email = Column(String)

    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    session = Session(engine)

    # Create categories
    electronics = Category(name="Electronics")
    office = Category(name="Office")

    # Create products
    products_data = [
        Product(name="Laptop", price=999.99, stock=15, category=electronics),
        Product(name="Monitor", price=299.99, stock=25, category=electronics),
        Product(name="Desk", price=199.99, stock=10, category=office),
        Product(name="Chair", price=149.99, stock=8, category=office),
    ]
    session.add_all(products_data)

    # Create suppliers
    supplier1 = Supplier(name="TechCorp", email="tech@example.com")
    supplier2 = Supplier(name="OfficeSupply", email="office@example.com")
    session.add_all([supplier1, supplier2])
    session.commit()

    # Queries
    print("1. Products in Electronics:")
    for p in session.query(Product).join(Category).filter(Category.name == "Electronics").all():
        print(f"  {p}")

    print("\n2. Products needing restock (< 20):")
    for p in session.query(Product).filter(Product.stock < 20).all():
        print(f"  {p}")

    print("\n3. Total inventory value per category:")
    categories = session.query(Category).all()
    for cat in categories:
        total = sum(p.price * p.stock for p in cat.products)
        print(f"  {cat.name}: ${total:.2f}")

    print("\n4. Most expensive product:")
    expensive = session.query(Product).order_by(Product.price.desc()).first()
    print(f"  {expensive}")

    print("\n5. Average stock:")
    avg_stock = session.query(func.avg(Product.stock)).scalar()
    print(f"  {avg_stock:.1f} units")

    session.close()


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Define a Product model and basic CRUD", exercise_1),
        ("Filtering and ordering", exercise_2),
        ("One-to-many relationship", exercise_3),
        ("Complex queries", exercise_4),
        ("Many-to-many relationship", exercise_5),
        ("Complete inventory system", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
