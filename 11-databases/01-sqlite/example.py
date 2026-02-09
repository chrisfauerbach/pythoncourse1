"""
SQLite Database Examples
========================

This file demonstrates working with SQLite databases in Python.
All examples use in-memory databases so no files are left behind.

Run this file:
    python3 example.py
"""

import sqlite3

# ===== 1. Creating a Database and Table =====
print("=" * 60)
print("1. CREATING A DATABASE AND TABLE")
print("=" * 60)

# Connect to an in-memory database (temporary, no file created)
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create a table with various data types
cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        age INTEGER,
        balance REAL
    )
''')
print("Created 'users' table with columns: id, name, email, age, balance")
print()


# ===== 2. INSERT - Adding Records =====
print("=" * 60)
print("2. INSERT - ADDING RECORDS")
print("=" * 60)

# Insert a single record
cursor.execute('''
    INSERT INTO users (name, email, age, balance)
    VALUES ('Alice', 'alice@example.com', 30, 1000.50)
''')
print("Inserted Alice")

# Insert another record
cursor.execute('''
    INSERT INTO users (name, email, age, balance)
    VALUES ('Bob', 'bob@example.com', 25, 750.25)
''')
print("Inserted Bob")

# Insert multiple records at once (more efficient!)
users_data = [
    ('Charlie', 'charlie@example.com', 35, 2500.00),
    ('Diana', 'diana@example.com', 28, 1800.75),
    ('Eve', 'eve@example.com', 42, 3200.50)
]
cursor.executemany('''
    INSERT INTO users (name, email, age, balance)
    VALUES (?, ?, ?, ?)
''', users_data)
print("Inserted Charlie, Diana, and Eve using executemany()")

# IMPORTANT: Always commit your changes!
conn.commit()
print("\nAll changes committed to database")
print()


# ===== 3. SELECT - Querying Data =====
print("=" * 60)
print("3. SELECT - QUERYING DATA")
print("=" * 60)

# Get all users
cursor.execute('SELECT * FROM users')
all_users = cursor.fetchall()
print("All users:")
for user in all_users:
    print(f"  {user}")

# Get just names and ages
cursor.execute('SELECT name, age FROM users')
names_ages = cursor.fetchall()
print("\nNames and ages:")
for name, age in names_ages:
    print(f"  {name} is {age} years old")

# Get one specific user
cursor.execute('SELECT * FROM users WHERE name = ?', ('Alice',))
alice = cursor.fetchone()
print(f"\nFound Alice: {alice}")
print()


# ===== 4. SELECT with Filtering and Sorting =====
print("=" * 60)
print("4. SELECT WITH FILTERING AND SORTING")
print("=" * 60)

# Users older than 30
cursor.execute('SELECT name, age FROM users WHERE age > 30')
older_users = cursor.fetchall()
print("Users older than 30:")
for name, age in older_users:
    print(f"  {name} ({age})")

# Users sorted by balance (descending)
cursor.execute('SELECT name, balance FROM users ORDER BY balance DESC')
by_balance = cursor.fetchall()
print("\nUsers by balance (highest first):")
for name, balance in by_balance:
    print(f"  {name}: ${balance:.2f}")

# Multiple conditions
cursor.execute('''
    SELECT name, age, balance
    FROM users
    WHERE age >= 30 AND balance > 1500
    ORDER BY age
''')
filtered = cursor.fetchall()
print("\nUsers 30+ with balance > $1500:")
for name, age, balance in filtered:
    print(f"  {name} ({age}): ${balance:.2f}")
print()


# ===== 5. UPDATE - Modifying Records =====
print("=" * 60)
print("5. UPDATE - MODIFYING RECORDS")
print("=" * 60)

# Update a single user
cursor.execute('''
    UPDATE users
    SET balance = balance + 500
    WHERE name = 'Alice'
''')
print("Added $500 to Alice's balance")

# Update multiple users at once
cursor.execute('''
    UPDATE users
    SET balance = balance * 1.05
    WHERE age > 30
''')
print("Gave 5% bonus to users over 30")

conn.commit()

# Verify the changes
cursor.execute('SELECT name, balance FROM users ORDER BY name')
updated_users = cursor.fetchall()
print("\nUpdated balances:")
for name, balance in updated_users:
    print(f"  {name}: ${balance:.2f}")
print()


# ===== 6. DELETE - Removing Records =====
print("=" * 60)
print("6. DELETE - REMOVING RECORDS")
print("=" * 60)

# First, let's see how many users we have
cursor.execute('SELECT COUNT(*) FROM users')
before_count = cursor.fetchone()[0]
print(f"Users before delete: {before_count}")

# Delete users with low balance
cursor.execute('DELETE FROM users WHERE balance < 1000')
deleted = cursor.rowcount
print(f"Deleted {deleted} users with balance < $1000")

conn.commit()

# Check how many remain
cursor.execute('SELECT COUNT(*) FROM users')
after_count = cursor.fetchone()[0]
print(f"Users after delete: {after_count}")

cursor.execute('SELECT name FROM users ORDER BY name')
remaining = cursor.fetchall()
print("Remaining users:", [name[0] for name in remaining])
print()


# ===== 7. Parameterized Queries (SQL Injection Prevention) =====
print("=" * 60)
print("7. PARAMETERIZED QUERIES (SAFE FROM SQL INJECTION)")
print("=" * 60)

# This is SAFE - always use parameterized queries!
search_name = "Alice"
cursor.execute('SELECT * FROM users WHERE name = ?', (search_name,))
result = cursor.fetchone()
print(f"Safe query for '{search_name}': {result}")

# What if someone tries SQL injection?
malicious_input = "Alice'; DROP TABLE users; --"
cursor.execute('SELECT * FROM users WHERE name = ?', (malicious_input,))
result = cursor.fetchone()
print(f"\nMalicious input '{malicious_input}' was safely handled")
print(f"Result: {result}  (None because no user has that name)")
print("The table is still safe!")

# Verify table still exists
cursor.execute('SELECT COUNT(*) FROM users')
count = cursor.fetchone()[0]
print(f"Table still has {count} users - SQL injection prevented!")
print()


# ===== 8. JOINs - Relating Multiple Tables =====
print("=" * 60)
print("8. JOINS - RELATING MULTIPLE TABLES")
print("=" * 60)

# Create an orders table
cursor.execute('''
    CREATE TABLE orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        product TEXT,
        price REAL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
''')
print("Created 'orders' table")

# Add some orders
orders_data = [
    (1, 'Laptop', 999.99),
    (1, 'Mouse', 29.99),
    (3, 'Keyboard', 79.99),
    (3, 'Monitor', 299.99),
    (4, 'Webcam', 89.99)
]
cursor.executemany('''
    INSERT INTO orders (user_id, product, price)
    VALUES (?, ?, ?)
''', orders_data)
conn.commit()
print("Added orders for users\n")

# INNER JOIN - only users who have orders
cursor.execute('''
    SELECT users.name, orders.product, orders.price
    FROM users
    INNER JOIN orders ON users.id = orders.user_id
    ORDER BY users.name, orders.product
''')
joined = cursor.fetchall()
print("Orders by user (INNER JOIN):")
for name, product, price in joined:
    print(f"  {name} ordered {product} for ${price:.2f}")

# LEFT JOIN - all users, even those without orders
cursor.execute('''
    SELECT users.name, orders.product
    FROM users
    LEFT JOIN orders ON users.id = orders.user_id
    ORDER BY users.name
''')
left_joined = cursor.fetchall()
print("\nAll users and their orders (LEFT JOIN):")
for name, product in left_joined:
    if product:
        print(f"  {name} -> {product}")
    else:
        print(f"  {name} -> (no orders)")
print()


# ===== 9. Aggregation - COUNT, SUM, AVG, GROUP BY =====
print("=" * 60)
print("9. AGGREGATION - COUNT, SUM, AVG, GROUP BY")
print("=" * 60)

# Count total orders
cursor.execute('SELECT COUNT(*) FROM orders')
total_orders = cursor.fetchone()[0]
print(f"Total orders: {total_orders}")

# Sum of all order prices
cursor.execute('SELECT SUM(price) FROM orders')
total_revenue = cursor.fetchone()[0]
print(f"Total revenue: ${total_revenue:.2f}")

# Average order price
cursor.execute('SELECT AVG(price) FROM orders')
avg_price = cursor.fetchone()[0]
print(f"Average order price: ${avg_price:.2f}")

# Group by user - how much did each user spend?
cursor.execute('''
    SELECT users.name, COUNT(orders.id) as order_count, SUM(orders.price) as total_spent
    FROM users
    INNER JOIN orders ON users.id = orders.user_id
    GROUP BY users.id
    ORDER BY total_spent DESC
''')
by_user = cursor.fetchall()
print("\nSpending by user:")
for name, count, total in by_user:
    print(f"  {name}: {count} orders, ${total:.2f} total")
print()


# ===== 10. Using Context Managers (Best Practice) =====
print("=" * 60)
print("10. USING CONTEXT MANAGERS (BEST PRACTICE)")
print("=" * 60)

# The 'with' statement ensures the connection is properly closed
with sqlite3.connect(':memory:') as temp_conn:
    temp_cursor = temp_conn.cursor()

    temp_cursor.execute('''
        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price REAL
        )
    ''')

    temp_cursor.execute('''
        INSERT INTO products (name, price) VALUES (?, ?)
    ''', ('Widget', 19.99))

    temp_conn.commit()

    temp_cursor.execute('SELECT * FROM products')
    products = temp_cursor.fetchall()
    print("Products from context manager:")
    for product in products:
        print(f"  {product}")

print("\nConnection automatically closed after 'with' block")
print()


# ===== 11. Getting Results as Dictionaries =====
print("=" * 60)
print("11. GETTING RESULTS AS DICTIONARIES")
print("=" * 60)

# Use Row factory for dict-like access
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute('SELECT name, email, age FROM users')
users_as_dicts = cursor.fetchall()

print("Users as dictionary-like objects:")
for user in users_as_dicts:
    # Access by column name instead of index!
    print(f"  {user['name']} ({user['age']}) - {user['email']}")
print()


# ===== 12. Complete Example: Simple Inventory System =====
print("=" * 60)
print("12. COMPLETE EXAMPLE: SIMPLE INVENTORY SYSTEM")
print("=" * 60)

# Create a new in-memory database for this example
inventory_conn = sqlite3.connect(':memory:')
inventory_conn.row_factory = sqlite3.Row
inv_cursor = inventory_conn.cursor()

# Create tables
inv_cursor.execute('''
    CREATE TABLE items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT,
        quantity INTEGER DEFAULT 0,
        price REAL
    )
''')

inv_cursor.execute('''
    CREATE TABLE transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_id INTEGER,
        change INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (item_id) REFERENCES items(id)
    )
''')

# Add initial inventory
items = [
    ('Laptop', 'Electronics', 10, 999.99),
    ('Mouse', 'Electronics', 50, 29.99),
    ('Desk', 'Furniture', 5, 299.99),
    ('Chair', 'Furniture', 8, 199.99),
    ('Notebook', 'Stationery', 100, 4.99)
]
inv_cursor.executemany('''
    INSERT INTO items (name, category, quantity, price)
    VALUES (?, ?, ?, ?)
''', items)
inventory_conn.commit()

print("Inventory System initialized with items\n")

# Show current inventory by category
inv_cursor.execute('''
    SELECT category, COUNT(*) as item_count, SUM(quantity) as total_units
    FROM items
    GROUP BY category
    ORDER BY category
''')
print("Inventory by category:")
for row in inv_cursor.fetchall():
    print(f"  {row['category']}: {row['item_count']} types, {row['total_units']} units")

# Show low stock items (less than 10 units)
inv_cursor.execute('''
    SELECT name, quantity, price
    FROM items
    WHERE quantity < 10
    ORDER BY quantity
''')
print("\nLow stock items (< 10 units):")
for row in inv_cursor.fetchall():
    print(f"  {row['name']}: {row['quantity']} left (${row['price']:.2f} each)")

# Calculate total inventory value
inv_cursor.execute('SELECT SUM(quantity * price) as total_value FROM items')
total_value = inv_cursor.fetchone()['total_value']
print(f"\nTotal inventory value: ${total_value:.2f}")

# Close the inventory connection
inventory_conn.close()
print("\nInventory system demo complete!")
print()


# ===== Cleanup =====
# Close the main database connection
conn.close()
print("=" * 60)
print("All examples completed successfully!")
print("=" * 60)
