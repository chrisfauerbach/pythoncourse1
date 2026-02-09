"""
Async Database Access — Exercises
==================================

Practice problems to test your understanding.
Try to solve each exercise before looking at the solutions below.

Run this file:
    python3 exercises.py
"""

import asyncio
import sqlite3
import time
from typing import List, Optional


# Helper class (same as in example.py)
class AsyncSQLiteDB:
    """Wrapper for async sqlite3 operations using asyncio.to_thread()"""

    def __init__(self, database: str = ":memory:"):
        self.database = database
        self.conn = None

    async def connect(self):
        # check_same_thread=False allows connection to be used across threads
        self.conn = await asyncio.to_thread(
            sqlite3.connect, self.database, check_same_thread=False
        )
        self.conn.row_factory = sqlite3.Row
        return self

    async def execute(self, query: str, params: tuple = ()):
        cursor = await asyncio.to_thread(self.conn.execute, query, params)
        return cursor

    async def executemany(self, query: str, params_list: List[tuple]):
        cursor = await asyncio.to_thread(self.conn.executemany, query, params_list)
        return cursor

    async def commit(self):
        await asyncio.to_thread(self.conn.commit)

    async def rollback(self):
        await asyncio.to_thread(self.conn.rollback)

    async def fetchall(self, cursor) -> List[sqlite3.Row]:
        return await asyncio.to_thread(cursor.fetchall)

    async def fetchone(self, cursor) -> Optional[sqlite3.Row]:
        return await asyncio.to_thread(cursor.fetchone)

    async def close(self):
        if self.conn:
            await asyncio.to_thread(self.conn.close)


# =============================================================================
# EXERCISE 1: Basic Async Database Operations
# Create an async function that sets up a "books" table and inserts 3 books.
# Table should have: id, title, author, year
# =============================================================================

async def exercise_1():
    """
    TODO: Implement this function
    1. Create an AsyncSQLiteDB instance and connect
    2. Create a 'books' table with columns: id, title, author, year
    3. Insert at least 3 books
    4. Query and print all books
    5. Close the database
    """
    print("TODO: Implement exercise 1")
    pass


# =============================================================================
# EXERCISE 2: Concurrent Queries
# Write a function that fetches multiple records concurrently and measures
# the time difference between sequential and concurrent approaches.
# =============================================================================

async def exercise_2():
    """
    TODO: Implement this function
    1. Set up a database with a 'customers' table
    2. Insert 5 customers
    3. Create an async function that fetches one customer (with a small delay)
    4. Fetch all 5 customers sequentially and measure time
    5. Fetch all 5 customers concurrently using asyncio.gather() and measure time
    6. Print the time difference
    """
    print("TODO: Implement exercise 2")
    pass


# =============================================================================
# EXERCISE 3: Async Transaction with Rollback
# Implement a money transfer function that uses transactions and handles errors.
# =============================================================================

async def exercise_3():
    """
    TODO: Implement this function
    1. Create a 'wallets' table with: id, username, balance
    2. Insert two wallets: Alice with $500, Bob with $300
    3. Implement an async transfer function that:
       - Deducts from sender
       - Adds to receiver
       - Commits if successful, rolls back if sender has insufficient funds
    4. Test with a valid transfer ($100 Alice -> Bob)
    5. Test with an invalid transfer ($600 Alice -> Bob)
    6. Print final balances to verify rollback worked
    """
    print("TODO: Implement exercise 3")
    pass


# =============================================================================
# EXERCISE 4: Async Bulk Operations
# Write a function that efficiently inserts many records using executemany
# and then updates them asynchronously.
# =============================================================================

async def exercise_4():
    """
    TODO: Implement this function
    1. Create a 'products' table with: id, name, price, stock
    2. Use executemany to insert 10 products at once
    3. Use an async function to update stock for multiple products
    4. Query and print products with stock < 50
    """
    print("TODO: Implement exercise 4")
    pass


# =============================================================================
# EXERCISE 5: Simple Message Queue
# Build a simple async message queue system using SQLite.
# =============================================================================

async def exercise_5():
    """
    TODO: Implement this function
    1. Create a 'messages' table with: id, content, status (pending/processed), created_at
    2. Add 5 messages with status 'pending'
    3. Create an async function that processes messages (simulates work with sleep)
    4. Process all pending messages concurrently
    5. Mark them as 'processed'
    6. Count and print how many messages were processed
    """
    print("TODO: Implement exercise 5")
    pass


# =============================================================================
# EXERCISE 6: Async Search and Filter
# Create a function that performs multiple search queries concurrently
# and combines the results.
# =============================================================================

async def exercise_6():
    """
    TODO: Implement this function
    1. Create an 'articles' table with: id, title, category, views
    2. Insert at least 8 articles across different categories
    3. Create async functions to:
       - Search by category
       - Search by minimum views
       - Get top N articles by views
    4. Run all three searches concurrently
    5. Print the results of each search
    """
    print("TODO: Implement exercise 6")
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

async def solution_1():
    """Solution: Basic async database operations"""
    db = AsyncSQLiteDB()
    await db.connect()

    # Create table
    await db.execute("""
        CREATE TABLE books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER
        )
    """)
    await db.commit()

    # Insert books
    books = [
        ("1984", "George Orwell", 1949),
        ("To Kill a Mockingbird", "Harper Lee", 1960),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925),
    ]

    await db.executemany(
        "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
        books
    )
    await db.commit()

    # Query and print
    cursor = await db.execute("SELECT * FROM books")
    all_books = await db.fetchall(cursor)

    print("Books in database:")
    for book in all_books:
        print(f"  {book['id']}. {book['title']} by {book['author']} ({book['year']})")

    await db.close()


async def solution_2():
    """Solution: Concurrent queries"""
    db = AsyncSQLiteDB()
    await db.connect()

    # Setup
    await db.execute("""
        CREATE TABLE customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    """)

    customers = [
        ("Alice", "alice@example.com"),
        ("Bob", "bob@example.com"),
        ("Charlie", "charlie@example.com"),
        ("Diana", "diana@example.com"),
        ("Eve", "eve@example.com"),
    ]

    await db.executemany(
        "INSERT INTO customers (name, email) VALUES (?, ?)",
        customers
    )
    await db.commit()

    # Async fetch function with delay
    async def fetch_customer(customer_id: int):
        await asyncio.sleep(0.1)  # Simulate slow query
        cursor = await db.execute(
            "SELECT * FROM customers WHERE id = ?",
            (customer_id,)
        )
        return await db.fetchone(cursor)

    # Sequential
    print("Sequential fetching:")
    start = time.time()
    for cid in range(1, 6):
        await fetch_customer(cid)
    sequential_time = time.time() - start
    print(f"  Time: {sequential_time:.2f}s")

    # Concurrent
    print("\nConcurrent fetching:")
    start = time.time()
    tasks = [fetch_customer(cid) for cid in range(1, 6)]
    results = await asyncio.gather(*tasks)
    concurrent_time = time.time() - start
    print(f"  Time: {concurrent_time:.2f}s")

    print(f"\nSpeedup: {sequential_time/concurrent_time:.1f}x faster")
    print("Customers fetched:")
    for customer in results:
        if customer:
            print(f"  - {customer['name']} ({customer['email']})")

    await db.close()


async def solution_3():
    """Solution: Async transaction with rollback"""
    db = AsyncSQLiteDB()
    await db.connect()

    # Setup
    await db.execute("""
        CREATE TABLE wallets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            balance REAL
        )
    """)

    await db.executemany(
        "INSERT INTO wallets (username, balance) VALUES (?, ?)",
        [("Alice", 500.0), ("Bob", 300.0)]
    )
    await db.commit()

    # Transfer function
    async def transfer(from_user: str, to_user: str, amount: float):
        try:
            # Get sender balance
            cursor = await db.execute(
                "SELECT balance FROM wallets WHERE username = ?",
                (from_user,)
            )
            sender = await db.fetchone(cursor)

            if not sender or sender['balance'] < amount:
                raise ValueError("Insufficient funds")

            # Perform transfer
            await db.execute(
                "UPDATE wallets SET balance = balance - ? WHERE username = ?",
                (amount, from_user)
            )

            await db.execute(
                "UPDATE wallets SET balance = balance + ? WHERE username = ?",
                (amount, to_user)
            )

            await db.commit()
            print(f"  ✓ Transferred ${amount} from {from_user} to {to_user}")

        except Exception as e:
            await db.rollback()
            print(f"  ✗ Transfer failed: {e}")

    # Print initial balances
    print("Initial balances:")
    cursor = await db.execute("SELECT * FROM wallets")
    for wallet in await db.fetchall(cursor):
        print(f"  {wallet['username']}: ${wallet['balance']}")

    # Valid transfer
    print("\nTransfer 1: $100 Alice -> Bob")
    await transfer("Alice", "Bob", 100.0)

    # Invalid transfer
    print("\nTransfer 2: $600 Alice -> Bob (should fail)")
    await transfer("Alice", "Bob", 600.0)

    # Final balances
    print("\nFinal balances:")
    cursor = await db.execute("SELECT * FROM wallets")
    for wallet in await db.fetchall(cursor):
        print(f"  {wallet['username']}: ${wallet['balance']}")

    await db.close()


async def solution_4():
    """Solution: Async bulk operations"""
    db = AsyncSQLiteDB()
    await db.connect()

    # Create table
    await db.execute("""
        CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL,
            stock INTEGER
        )
    """)
    await db.commit()

    # Bulk insert
    products = [
        ("Widget A", 19.99, 100),
        ("Widget B", 29.99, 45),
        ("Widget C", 39.99, 80),
        ("Widget D", 49.99, 30),
        ("Widget E", 59.99, 60),
        ("Widget F", 69.99, 25),
        ("Widget G", 79.99, 90),
        ("Widget H", 89.99, 40),
        ("Widget I", 99.99, 70),
        ("Widget J", 109.99, 20),
    ]

    await db.executemany(
        "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
        products
    )
    await db.commit()
    print(f"✓ Inserted {len(products)} products")

    # Update stock for multiple products
    async def reduce_stock(product_id: int, amount: int):
        await db.execute(
            "UPDATE products SET stock = stock - ? WHERE id = ?",
            (amount, product_id)
        )

    print("\nReducing stock for products 1, 3, 5...")
    await asyncio.gather(
        reduce_stock(1, 10),
        reduce_stock(3, 15),
        reduce_stock(5, 20)
    )
    await db.commit()

    # Query low stock items
    cursor = await db.execute("SELECT * FROM products WHERE stock < 50")
    low_stock = await db.fetchall(cursor)

    print(f"\nProducts with stock < 50:")
    for product in low_stock:
        print(f"  {product['name']}: {product['stock']} units (${product['price']})")

    await db.close()


async def solution_5():
    """Solution: Simple message queue"""
    db = AsyncSQLiteDB()
    await db.connect()

    # Create table
    await db.execute("""
        CREATE TABLE messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT,
            status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    await db.commit()

    # Add messages
    messages = [
        ("Welcome new user",),
        ("Process payment",),
        ("Send confirmation email",),
        ("Update inventory",),
        ("Generate report",),
    ]

    await db.executemany(
        "INSERT INTO messages (content) VALUES (?)",
        messages
    )
    await db.commit()
    print(f"✓ Added {len(messages)} messages to queue")

    # Simulate work function
    async def do_work(content: str):
        await asyncio.sleep(0.15)
        return f"Processed: {content}"

    # Get pending messages
    cursor = await db.execute(
        "SELECT * FROM messages WHERE status = 'pending'"
    )
    pending = await db.fetchall(cursor)

    print(f"\nProcessing {len(pending)} messages concurrently...")

    # Do the "work" concurrently, then update DB sequentially
    # (A single sqlite3 connection can't handle concurrent writes from threads)
    results = await asyncio.gather(*[
        do_work(msg['content']) for msg in pending
    ])

    for msg, result in zip(pending, results):
        await db.execute(
            "UPDATE messages SET status = 'processed' WHERE id = ?",
            (msg['id'],)
        )
        print(f"  ✓ {result}")
    await db.commit()

    # Count processed
    cursor = await db.execute(
        "SELECT COUNT(*) as count FROM messages WHERE status = 'processed'"
    )
    result = await db.fetchone(cursor)
    print(f"\n✓ Total processed messages: {result['count']}")

    await db.close()


async def solution_6():
    """Solution: Async search and filter"""
    db = AsyncSQLiteDB()
    await db.connect()

    # Create table
    await db.execute("""
        CREATE TABLE articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            category TEXT,
            views INTEGER
        )
    """)
    await db.commit()

    # Insert articles
    articles = [
        ("Python Best Practices", "Programming", 1500),
        ("Async/Await Guide", "Programming", 2200),
        ("Healthy Recipes", "Cooking", 800),
        ("Database Design", "Programming", 1800),
        ("Travel Tips", "Lifestyle", 1200),
        ("Quick Meals", "Cooking", 950),
        ("Web Development 101", "Programming", 3000),
        ("Meditation Guide", "Lifestyle", 1100),
    ]

    await db.executemany(
        "INSERT INTO articles (title, category, views) VALUES (?, ?, ?)",
        articles
    )
    await db.commit()

    # Search functions
    async def search_by_category(category: str):
        await asyncio.sleep(0.05)  # Simulate query time
        cursor = await db.execute(
            "SELECT * FROM articles WHERE category = ?",
            (category,)
        )
        return await db.fetchall(cursor)

    async def search_by_min_views(min_views: int):
        await asyncio.sleep(0.05)
        cursor = await db.execute(
            "SELECT * FROM articles WHERE views >= ?",
            (min_views,)
        )
        return await db.fetchall(cursor)

    async def get_top_articles(limit: int):
        await asyncio.sleep(0.05)
        cursor = await db.execute(
            "SELECT * FROM articles ORDER BY views DESC LIMIT ?",
            (limit,)
        )
        return await db.fetchall(cursor)

    # Run all searches concurrently
    print("Running concurrent searches...")
    start = time.time()

    programming_articles, popular_articles, top_articles = await asyncio.gather(
        search_by_category("Programming"),
        search_by_min_views(1500),
        get_top_articles(3)
    )

    elapsed = time.time() - start
    print(f"✓ Completed 3 searches in {elapsed:.2f}s\n")

    # Print results
    print("Programming articles:")
    for article in programming_articles:
        print(f"  - {article['title']} ({article['views']} views)")

    print("\nArticles with 1500+ views:")
    for article in popular_articles:
        print(f"  - {article['title']} ({article['views']} views)")

    print("\nTop 3 articles:")
    for i, article in enumerate(top_articles, 1):
        print(f"  {i}. {article['title']} ({article['views']} views)")

    await db.close()


# =============================================================================
# Async exercise runner
# =============================================================================

async def async_main():
    """Run all exercises with async support"""
    exercises = [
        ("Basic Async Database Operations", exercise_1),
        ("Concurrent Queries", exercise_2),
        ("Async Transaction with Rollback", exercise_3),
        ("Async Bulk Operations", exercise_4),
        ("Simple Message Queue", exercise_5),
        ("Async Search and Filter", exercise_6),
    ]

    solutions = [
        solution_1,
        solution_2,
        solution_3,
        solution_4,
        solution_5,
        solution_6,
    ]

    print("=" * 70)
    print("ASYNC DATABASE ACCESS - EXERCISES")
    print("=" * 70)
    print("\nTry implementing each exercise before running the solutions!\n")

    # Run exercises
    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 70)
        print(f"EXERCISE {i}: {title}")
        print("=" * 70)
        await func()
        print()

    # Offer to show solutions
    print("=" * 70)
    print("SOLUTIONS")
    print("=" * 70)
    print("\nRunning solutions...\n")

    for i, solution_func in enumerate(solutions, 1):
        print("=" * 70)
        print(f"SOLUTION {i}")
        print("=" * 70)
        await solution_func()
        print()

    print("=" * 70)
    print("All exercises and solutions completed!")
    print("=" * 70)


if __name__ == "__main__":
    asyncio.run(async_main())
