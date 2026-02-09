# SQLite Databases in Python

Welcome to the world of databases! SQLite is the perfect place to start learning about databases because it's simple, lightweight, and already included in Python's standard library.

## Objective

Learn to work with SQLite databases in Python, including creating tables, inserting data, querying records, and understanding when to use databases in your applications.

## Concepts Covered

- Creating databases and tables
- CRUD operations (Create, Read, Update, Delete)
- Parameterized queries (SQL injection prevention)
- JOINs and relationships between tables
- Aggregation (COUNT, SUM, AVG, GROUP BY)
- Context managers for safe database handling
- SQLite data types
- When to use SQLite vs other databases

## Prerequisites

- [Section 02: Data Structures](../../02-data-structures/)
- [Section 05: Functions](../../05-functions/)

## What is SQLite?

SQLite is a **self-contained, serverless database engine** that stores data in a single file (or in memory). Unlike bigger databases like PostgreSQL or MySQL, you don't need to install or configure a separate server—just import `sqlite3` and you're ready to go!

### Why SQLite is Great for Learning

- **Zero setup**: Already in Python's stdlib, no installation needed
- **Simple**: Just one file (or use `:memory:` for temporary databases)
- **Fast**: Perfect for small to medium-sized applications
- **Portable**: The database file can be copied anywhere
- **Full-featured**: Supports most SQL features you'll need

## Creating Databases and Tables

```python
import sqlite3

# Create a database file (or use ':memory:' for in-memory)
conn = sqlite3.connect('my_database.db')  # Creates file
# or
conn = sqlite3.connect(':memory:')  # Temporary, in RAM

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        age INTEGER
    )
''')

# Always commit your changes!
conn.commit()
conn.close()
```

## SQLite Data Types

SQLite uses a simplified type system:

- **NULL**: Missing value
- **INTEGER**: Whole numbers (1, 42, -5)
- **REAL**: Floating-point numbers (3.14, -0.5)
- **TEXT**: Strings ('hello', 'foo@bar.com')
- **BLOB**: Binary data (images, files)

Unlike other databases, SQLite is **dynamically typed**—you can store any type in any column (though you shouldn't!).

## CRUD Operations

CRUD stands for **Create, Read, Update, Delete**—the four basic operations you'll do constantly.

### INSERT - Creating Records

```python
# Insert a single record
cursor.execute('''
    INSERT INTO users (name, email, age)
    VALUES ('Alice', 'alice@example.com', 30)
''')

# Insert multiple records
users = [
    ('Bob', 'bob@example.com', 25),
    ('Charlie', 'charlie@example.com', 35)
]
cursor.executemany('''
    INSERT INTO users (name, email, age) VALUES (?, ?, ?)
''', users)

conn.commit()
```

### SELECT - Reading Records

```python
# Get all records
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Get one record
cursor.execute('SELECT * FROM users WHERE name = ?', ('Alice',))
user = cursor.fetchone()

# Filter and sort
cursor.execute('''
    SELECT name, age FROM users
    WHERE age > 25
    ORDER BY age DESC
''')
```

### UPDATE - Modifying Records

```python
cursor.execute('''
    UPDATE users
    SET age = 31
    WHERE name = 'Alice'
''')
conn.commit()
```

### DELETE - Removing Records

```python
cursor.execute('DELETE FROM users WHERE age < 25')
conn.commit()
```

## Parameterized Queries (Stay Safe!)

**NEVER** build SQL queries with string formatting or concatenation—it opens you up to SQL injection attacks!

```python
# BAD - SQL injection vulnerable!
name = "Alice'; DROP TABLE users; --"
cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")  # DANGER!

# GOOD - Use parameterized queries
cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
```

The `?` placeholder is automatically escaped, keeping your database safe from malicious input.

## JOINs - Connecting Tables

Real-world data is spread across multiple tables. JOINs let you combine them:

```python
# Create related tables
cursor.execute('''
    CREATE TABLE orders (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        product TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
''')

# Join them
cursor.execute('''
    SELECT users.name, orders.product
    FROM users
    JOIN orders ON users.id = orders.user_id
''')
```

### Types of JOINs

- **INNER JOIN**: Only matching rows from both tables
- **LEFT JOIN**: All rows from left table, matching from right (or NULL)
- **RIGHT JOIN**: Not supported in SQLite (use LEFT JOIN instead)
- **CROSS JOIN**: Cartesian product (every combination)

## Aggregation and Grouping

```python
# Count records
cursor.execute('SELECT COUNT(*) FROM users')
total = cursor.fetchone()[0]

# Group by and aggregate
cursor.execute('''
    SELECT age, COUNT(*) as count
    FROM users
    GROUP BY age
    ORDER BY count DESC
''')

# Other aggregate functions: SUM, AVG, MIN, MAX
```

## Using Context Managers (Best Practice!)

Always use `with` statements to ensure connections are properly closed:

```python
with sqlite3.connect(':memory:') as conn:
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE test (id INTEGER, name TEXT)')
    cursor.execute('INSERT INTO test VALUES (1, "Alice")')
    conn.commit()
# Connection automatically closed, even if an error occurs!
```

## Getting Results as Dictionaries

By default, rows come back as tuples. For more readable code, use `Row`:

```python
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute('SELECT * FROM users')

for row in cursor.fetchall():
    print(row['name'], row['email'])  # Access by column name!
```

## When to Use SQLite vs Other Databases

### Use SQLite when:
- Building small to medium applications
- You need a simple embedded database
- Your app runs on a single machine
- You want zero configuration
- You're prototyping or learning

### Use PostgreSQL/MySQL when:
- You need multiple concurrent writers
- Building large-scale web applications
- You need advanced features (full-text search, geospatial data)
- You have heavy write traffic
- You need strict user permissions

## Common Gotchas

1. **Forgetting to commit**: Changes aren't saved until you call `conn.commit()`
2. **Not closing connections**: Use `with` statements or always call `conn.close()`
3. **SQL injection**: Always use parameterized queries with `?` placeholders
4. **Type confusion**: Remember SQLite is dynamically typed—be careful!
5. **Concurrent writes**: SQLite locks the entire database on writes

## Quick Reference

```python
import sqlite3

# Connect
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create
cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')

# Insert
cursor.execute('INSERT INTO users (name) VALUES (?)', ('Alice',))

# Select
cursor.execute('SELECT * FROM users WHERE name = ?', ('Alice',))
rows = cursor.fetchall()

# Update
cursor.execute('UPDATE users SET name = ? WHERE id = ?', ('Bob', 1))

# Delete
cursor.execute('DELETE FROM users WHERE id = ?', (1,))

# Always commit and close
conn.commit()
conn.close()
```

## Next Steps

Now that you know SQLite basics, you can:
- Learn about database normalization (organizing data efficiently)
- Explore ORMs like SQLAlchemy (write Python instead of SQL)
- Try other databases like PostgreSQL
- Build real applications with persistent data storage

## Code Example

Check out [`example.py`](example.py) for a complete working example.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.
