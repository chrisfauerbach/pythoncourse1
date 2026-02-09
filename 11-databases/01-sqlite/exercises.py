"""
SQLite Exercises
================

Practice problems to test your understanding of SQLite in Python.
Try to solve each exercise before looking at the solutions below.

Run this file:
    python3 exercises.py
"""

import sqlite3


# =============================================================================
# EXERCISE 1: Create a Book Database
# Create a table called 'books' with columns: id, title, author, year, rating
# Insert at least 3 books and display all of them.
# =============================================================================

def exercise_1():
    """Create a book database and display all books"""
    # Your code here
    pass


# =============================================================================
# EXERCISE 2: Filter and Sort Books
# Using the books table from exercise 1, write queries to:
# 1. Find all books published after 2000
# 2. Find books with a rating >= 4.0
# 3. Display books sorted by rating (highest first)
# =============================================================================

def exercise_2():
    """Query books with filters and sorting"""
    # Your code here
    pass


# =============================================================================
# EXERCISE 3: Update and Delete Operations
# Using a products database:
# 1. Create a 'products' table with: id, name, price, stock
# 2. Insert several products
# 3. Update the price of one product (increase by 10%)
# 4. Delete products that are out of stock (stock = 0)
# 5. Display the remaining products
# =============================================================================

def exercise_3():
    """Practice UPDATE and DELETE operations"""
    # Your code here
    pass


# =============================================================================
# EXERCISE 4: JOIN Tables (Students and Courses)
# Create two tables:
# - students: id, name, age
# - enrollments: id, student_id, course_name, grade
# Insert data and write a JOIN query to show each student's courses and grades.
# =============================================================================

def exercise_4():
    """Practice JOIN operations with students and courses"""
    # Your code here
    pass


# =============================================================================
# EXERCISE 5: Aggregation Functions
# Create a 'sales' table with: id, product, quantity, price
# Insert several sales records and calculate:
# 1. Total revenue (SUM of quantity * price)
# 2. Average sale price
# 3. Number of sales per product (GROUP BY)
# 4. The best-selling product (highest total quantity)
# =============================================================================

def exercise_5():
    """Practice aggregation with SUM, AVG, COUNT, GROUP BY"""
    # Your code here
    pass


# =============================================================================
# EXERCISE 6: Build a Simple TODO List Manager
# Create a complete TODO list system with:
# - A 'tasks' table: id, title, description, completed (0 or 1), created_at
# - Functions to:
#   1. Add a new task
#   2. Mark a task as completed
#   3. List all incomplete tasks
#   4. List all completed tasks
#   5. Delete a task
# Use parameterized queries and proper error handling!
# =============================================================================

def exercise_6():
    """Build a complete TODO list manager"""
    # Your code here
    pass


# =============================================================================
# SOLUTIONS (no peeking until you've tried!)
# =============================================================================

def solution_1():
    """Solution: Create a book database and display all books"""
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Create table
    cursor.execute('''
        CREATE TABLE books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER,
            rating REAL
        )
    ''')

    # Insert books
    books = [
        ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 4.2),
        ('To Kill a Mockingbird', 'Harper Lee', 1960, 4.5),
        ('1984', 'George Orwell', 1949, 4.7),
        ('Pride and Prejudice', 'Jane Austen', 1813, 4.3)
    ]
    cursor.executemany('''
        INSERT INTO books (title, author, year, rating)
        VALUES (?, ?, ?, ?)
    ''', books)
    conn.commit()

    # Display all books
    cursor.execute('SELECT * FROM books')
    all_books = cursor.fetchall()
    print("All books:")
    for book in all_books:
        book_id, title, author, year, rating = book
        print(f"  {title} by {author} ({year}) - Rating: {rating}")

    conn.close()


def solution_2():
    """Solution: Query books with filters and sorting"""
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Setup (same as solution_1)
    cursor.execute('''
        CREATE TABLE books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER,
            rating REAL
        )
    ''')
    books = [
        ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 4.2),
        ('To Kill a Mockingbird', 'Harper Lee', 1960, 4.5),
        ('1984', 'George Orwell', 1949, 4.7),
        ('The Hunger Games', 'Suzanne Collins', 2008, 4.3),
        ('Harry Potter', 'J.K. Rowling', 1997, 4.8)
    ]
    cursor.executemany('''
        INSERT INTO books (title, author, year, rating)
        VALUES (?, ?, ?, ?)
    ''', books)
    conn.commit()

    # Query 1: Books after 2000
    cursor.execute('SELECT title, year FROM books WHERE year > 2000')
    recent = cursor.fetchall()
    print("Books published after 2000:")
    for title, year in recent:
        print(f"  {title} ({year})")

    # Query 2: Books with rating >= 4.0
    cursor.execute('SELECT title, rating FROM books WHERE rating >= 4.0')
    highly_rated = cursor.fetchall()
    print("\nBooks with rating >= 4.0:")
    for title, rating in highly_rated:
        print(f"  {title} - {rating}")

    # Query 3: Sorted by rating
    cursor.execute('SELECT title, rating FROM books ORDER BY rating DESC')
    sorted_books = cursor.fetchall()
    print("\nBooks sorted by rating (highest first):")
    for title, rating in sorted_books:
        print(f"  {title} - {rating}")

    conn.close()


def solution_3():
    """Solution: Practice UPDATE and DELETE operations"""
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Create products table
    cursor.execute('''
        CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL,
            stock INTEGER DEFAULT 0
        )
    ''')

    # Insert products
    products = [
        ('Laptop', 999.99, 10),
        ('Mouse', 29.99, 50),
        ('Keyboard', 79.99, 0),
        ('Monitor', 299.99, 5),
        ('Webcam', 89.99, 0),
        ('Headphones', 149.99, 20)
    ]
    cursor.executemany('''
        INSERT INTO products (name, price, stock)
        VALUES (?, ?, ?)
    ''', products)
    conn.commit()

    print("Initial products:")
    cursor.execute('SELECT name, price, stock FROM products')
    for name, price, stock in cursor.fetchall():
        print(f"  {name}: ${price:.2f} (stock: {stock})")

    # Update price (increase Monitor by 10%)
    cursor.execute('''
        UPDATE products
        SET price = price * 1.10
        WHERE name = 'Monitor'
    ''')
    conn.commit()
    print("\nIncreased Monitor price by 10%")

    # Delete out-of-stock products
    cursor.execute('DELETE FROM products WHERE stock = 0')
    deleted = cursor.rowcount
    conn.commit()
    print(f"Deleted {deleted} out-of-stock products")

    # Display remaining products
    print("\nRemaining products:")
    cursor.execute('SELECT name, price, stock FROM products')
    for name, price, stock in cursor.fetchall():
        print(f"  {name}: ${price:.2f} (stock: {stock})")

    conn.close()


def solution_4():
    """Solution: Practice JOIN operations with students and courses"""
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
        CREATE TABLE students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE enrollments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            course_name TEXT,
            grade REAL,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    ''')

    # Insert students
    students = [
        ('Alice', 20),
        ('Bob', 22),
        ('Charlie', 21)
    ]
    cursor.executemany('INSERT INTO students (name, age) VALUES (?, ?)', students)

    # Insert enrollments
    enrollments = [
        (1, 'Mathematics', 95.5),
        (1, 'Physics', 88.0),
        (2, 'Mathematics', 78.5),
        (2, 'Chemistry', 92.0),
        (3, 'Physics', 85.5),
        (3, 'Chemistry', 90.0)
    ]
    cursor.executemany('''
        INSERT INTO enrollments (student_id, course_name, grade)
        VALUES (?, ?, ?)
    ''', enrollments)
    conn.commit()

    # JOIN query
    cursor.execute('''
        SELECT students.name, enrollments.course_name, enrollments.grade
        FROM students
        INNER JOIN enrollments ON students.id = enrollments.student_id
        ORDER BY students.name, enrollments.course_name
    ''')

    print("Student enrollments:")
    current_student = None
    for name, course, grade in cursor.fetchall():
        if name != current_student:
            print(f"\n{name}:")
            current_student = name
        print(f"  {course}: {grade}")

    conn.close()


def solution_5():
    """Solution: Practice aggregation with SUM, AVG, COUNT, GROUP BY"""
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Create sales table
    cursor.execute('''
        CREATE TABLE sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product TEXT,
            quantity INTEGER,
            price REAL
        )
    ''')

    # Insert sales records
    sales = [
        ('Laptop', 2, 999.99),
        ('Mouse', 10, 29.99),
        ('Laptop', 1, 999.99),
        ('Keyboard', 5, 79.99),
        ('Mouse', 8, 29.99),
        ('Monitor', 3, 299.99)
    ]
    cursor.executemany('''
        INSERT INTO sales (product, quantity, price)
        VALUES (?, ?, ?)
    ''', sales)
    conn.commit()

    # 1. Total revenue
    cursor.execute('SELECT SUM(quantity * price) as total_revenue FROM sales')
    total = cursor.fetchone()[0]
    print(f"Total revenue: ${total:.2f}")

    # 2. Average sale price
    cursor.execute('SELECT AVG(price) as avg_price FROM sales')
    avg = cursor.fetchone()[0]
    print(f"Average sale price: ${avg:.2f}")

    # 3. Number of sales per product
    cursor.execute('''
        SELECT product, COUNT(*) as sale_count, SUM(quantity) as total_quantity
        FROM sales
        GROUP BY product
        ORDER BY sale_count DESC
    ''')
    print("\nSales per product:")
    for product, count, total_qty in cursor.fetchall():
        print(f"  {product}: {count} sales, {total_qty} units")

    # 4. Best-selling product
    cursor.execute('''
        SELECT product, SUM(quantity) as total_quantity
        FROM sales
        GROUP BY product
        ORDER BY total_quantity DESC
        LIMIT 1
    ''')
    best_product, best_qty = cursor.fetchone()
    print(f"\nBest-selling product: {best_product} ({best_qty} units)")

    conn.close()


def solution_6():
    """Solution: Build a complete TODO list manager"""
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row  # For dict-like access
    cursor = conn.cursor()

    # Create tasks table
    cursor.execute('''
        CREATE TABLE tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed INTEGER DEFAULT 0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()

    def add_task(title, description=""):
        """Add a new task"""
        cursor.execute('''
            INSERT INTO tasks (title, description)
            VALUES (?, ?)
        ''', (title, description))
        conn.commit()
        print(f"Added task: {title}")

    def complete_task(task_id):
        """Mark a task as completed"""
        cursor.execute('''
            UPDATE tasks
            SET completed = 1
            WHERE id = ?
        ''', (task_id,))
        conn.commit()
        print(f"Marked task {task_id} as completed")

    def list_incomplete():
        """List all incomplete tasks"""
        cursor.execute('''
            SELECT id, title, description
            FROM tasks
            WHERE completed = 0
            ORDER BY created_at
        ''')
        tasks = cursor.fetchall()
        if tasks:
            print("\nIncomplete tasks:")
            for task in tasks:
                print(f"  [{task['id']}] {task['title']}")
                if task['description']:
                    print(f"      {task['description']}")
        else:
            print("\nNo incomplete tasks!")

    def list_completed():
        """List all completed tasks"""
        cursor.execute('''
            SELECT id, title
            FROM tasks
            WHERE completed = 1
            ORDER BY created_at
        ''')
        tasks = cursor.fetchall()
        if tasks:
            print("\nCompleted tasks:")
            for task in tasks:
                print(f"  [{task['id']}] {task['title']}")
        else:
            print("\nNo completed tasks yet!")

    def delete_task(task_id):
        """Delete a task"""
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        print(f"Deleted task {task_id}")

    # Demo the TODO list system
    print("TODO List Manager Demo\n")

    # Add tasks
    add_task("Buy groceries", "Milk, eggs, bread")
    add_task("Finish homework", "Math problems 1-20")
    add_task("Call mom")
    add_task("Workout", "30 min cardio")

    # List incomplete
    list_incomplete()

    # Complete some tasks
    print()
    complete_task(1)
    complete_task(3)

    # List both incomplete and completed
    list_incomplete()
    list_completed()

    # Delete a task
    print()
    delete_task(2)

    # Final status
    list_incomplete()
    list_completed()

    conn.close()


# =============================================================================
# Runner
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Create a Book Database", solution_1),
        ("Filter and Sort Books", solution_2),
        ("Update and Delete Operations", solution_3),
        ("JOIN Tables (Students and Courses)", solution_4),
        ("Aggregation Functions", solution_5),
        ("Build a Simple TODO List Manager", solution_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()
