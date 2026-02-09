"""
Async Database Access — Example Code
======================================

This example demonstrates async database operations using:
1. asyncio.to_thread() with stdlib sqlite3 (works without any installs)
2. Commented-out aiosqlite code for reference

Run this file:
    python3 example.py
"""

import asyncio
import sqlite3
import time
from typing import List, Tuple, Optional

# If you have aiosqlite installed (pip install aiosqlite), uncomment to try it:
# import aiosqlite


# ===== Helper: Database Connection =====

class AsyncSQLiteDB:
    """Wrapper for async sqlite3 operations using asyncio.to_thread()"""

    def __init__(self, database: str = ":memory:"):
        self.database = database
        self.conn = None

    async def connect(self):
        """Connect to database"""
        # check_same_thread=False allows connection to be used across threads
        self.conn = await asyncio.to_thread(
            sqlite3.connect, self.database, check_same_thread=False
        )
        # Enable row factory for dict-like access
        self.conn.row_factory = sqlite3.Row
        return self

    async def execute(self, query: str, params: tuple = ()):
        """Execute a query"""
        cursor = await asyncio.to_thread(self.conn.execute, query, params)
        return cursor

    async def executemany(self, query: str, params_list: List[tuple]):
        """Execute a query with multiple parameter sets"""
        cursor = await asyncio.to_thread(self.conn.executemany, query, params_list)
        return cursor

    async def commit(self):
        """Commit transaction"""
        await asyncio.to_thread(self.conn.commit)

    async def rollback(self):
        """Rollback transaction"""
        await asyncio.to_thread(self.conn.rollback)

    async def fetchall(self, cursor) -> List[sqlite3.Row]:
        """Fetch all rows from cursor"""
        return await asyncio.to_thread(cursor.fetchall)

    async def fetchone(self, cursor) -> Optional[sqlite3.Row]:
        """Fetch one row from cursor"""
        return await asyncio.to_thread(cursor.fetchone)

    async def close(self):
        """Close connection"""
        if self.conn:
            await asyncio.to_thread(self.conn.close)


# ===== 1. Basic Async Database Setup =====

async def example_basic_setup():
    """Creating and connecting to an async database"""
    print("\n1. BASIC ASYNC DATABASE SETUP")
    print("-" * 50)

    # Using asyncio.to_thread() with sqlite3
    db = AsyncSQLiteDB(":memory:")
    await db.connect()
    print("✓ Connected to in-memory database using asyncio.to_thread()")

    await db.close()
    print("✓ Connection closed")

    # With aiosqlite (commented out - requires: pip install aiosqlite):
    # async with aiosqlite.connect(":memory:") as db:
    #     print("✓ Connected using aiosqlite")


# ===== 2. Async CREATE TABLE =====

async def example_create_table():
    """Creating tables asynchronously"""
    print("\n2. ASYNC CREATE TABLE")
    print("-" * 50)

    db = AsyncSQLiteDB()
    await db.connect()

    # Create users table
    await db.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Create posts table
    await db.execute("""
        CREATE TABLE posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT NOT NULL,
            content TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    await db.commit()
    print("✓ Created users and posts tables")

    await db.close()

    # With aiosqlite:
    # async with aiosqlite.connect(":memory:") as db:
    #     await db.execute("CREATE TABLE users (...)")
    #     await db.commit()


# ===== 3. Async INSERT Operations =====

async def example_insert_operations():
    """Inserting data asynchronously"""
    print("\n3. ASYNC INSERT OPERATIONS")
    print("-" * 50)

    db = AsyncSQLiteDB()
    await db.connect()

    # Setup table
    await db.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)
    await db.commit()

    # Single insert
    cursor = await db.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        ("Alice", "alice@example.com")
    )
    await db.commit()
    print(f"✓ Inserted single user (row id: {cursor.lastrowid})")

    # Bulk insert using executemany
    users_data = [
        ("Bob", "bob@example.com"),
        ("Charlie", "charlie@example.com"),
        ("Diana", "diana@example.com"),
        ("Eve", "eve@example.com"),
    ]

    await db.executemany(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        users_data
    )
    await db.commit()
    print(f"✓ Bulk inserted {len(users_data)} users")

    # Verify count
    cursor = await db.execute("SELECT COUNT(*) as count FROM users")
    row = await db.fetchone(cursor)
    print(f"✓ Total users in database: {row['count']}")

    await db.close()

    # With aiosqlite:
    # async with aiosqlite.connect(":memory:") as db:
    #     await db.execute("INSERT INTO users VALUES (?, ?)", ("Alice", "alice@example.com"))
    #     await db.executemany("INSERT INTO users VALUES (?, ?)", users_data)
    #     await db.commit()


# ===== 4. Async SELECT Queries =====

async def example_select_queries():
    """Querying data asynchronously"""
    print("\n4. ASYNC SELECT QUERIES")
    print("-" * 50)

    db = AsyncSQLiteDB()
    await db.connect()

    # Setup
    await db.execute("""
        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price REAL,
            category TEXT
        )
    """)

    products = [
        ("Laptop", 999.99, "Electronics"),
        ("Mouse", 29.99, "Electronics"),
        ("Desk", 299.99, "Furniture"),
        ("Chair", 199.99, "Furniture"),
        ("Keyboard", 79.99, "Electronics"),
    ]

    await db.executemany(
        "INSERT INTO products (name, price, category) VALUES (?, ?, ?)",
        products
    )
    await db.commit()

    # Fetch all
    cursor = await db.execute("SELECT * FROM products")
    all_products = await db.fetchall(cursor)
    print(f"✓ Fetched all products: {len(all_products)} items")

    # Fetch with WHERE clause
    cursor = await db.execute(
        "SELECT * FROM products WHERE category = ?",
        ("Electronics",)
    )
    electronics = await db.fetchall(cursor)
    print(f"✓ Electronics: {len(electronics)} items")
    for product in electronics:
        print(f"  - {product['name']}: ${product['price']}")

    # Fetch one
    cursor = await db.execute(
        "SELECT * FROM products WHERE price > ? ORDER BY price DESC LIMIT 1",
        (500,)
    )
    most_expensive = await db.fetchone(cursor)
    if most_expensive:
        print(f"✓ Most expensive item: {most_expensive['name']} (${most_expensive['price']})")

    await db.close()

    # With aiosqlite:
    # async with aiosqlite.connect(":memory:") as db:
    #     async with db.execute("SELECT * FROM products") as cursor:
    #         rows = await cursor.fetchall()


# ===== 5. Async UPDATE and DELETE =====

async def example_update_delete():
    """Updating and deleting data asynchronously"""
    print("\n5. ASYNC UPDATE AND DELETE")
    print("-" * 50)

    db = AsyncSQLiteDB()
    await db.connect()

    # Setup
    await db.execute("""
        CREATE TABLE inventory (
            id INTEGER PRIMARY KEY,
            item TEXT,
            quantity INTEGER
        )
    """)

    items = [("Apples", 100), ("Bananas", 150), ("Oranges", 75)]
    await db.executemany(
        "INSERT INTO inventory (item, quantity) VALUES (?, ?)",
        items
    )
    await db.commit()

    print("Initial inventory:")
    cursor = await db.execute("SELECT * FROM inventory")
    for row in await db.fetchall(cursor):
        print(f"  {row['item']}: {row['quantity']}")

    # Update
    cursor = await db.execute(
        "UPDATE inventory SET quantity = quantity - ? WHERE item = ?",
        (20, "Apples")
    )
    await db.commit()
    print(f"\n✓ Updated Apples quantity (rows affected: {cursor.rowcount})")

    # Delete
    cursor = await db.execute(
        "DELETE FROM inventory WHERE quantity < ?",
        (100,)
    )
    await db.commit()
    print(f"✓ Deleted items with quantity < 100 (rows affected: {cursor.rowcount})")

    print("\nFinal inventory:")
    cursor = await db.execute("SELECT * FROM inventory")
    for row in await db.fetchall(cursor):
        print(f"  {row['item']}: {row['quantity']}")

    await db.close()

    # With aiosqlite:
    # async with aiosqlite.connect(":memory:") as db:
    #     await db.execute("UPDATE inventory SET quantity = ?", (50,))
    #     await db.commit()


# ===== 6. Running Multiple Queries Concurrently =====

async def fetch_user_by_id(db: AsyncSQLiteDB, user_id: int):
    """Fetch a single user (simulating slow query)"""
    await asyncio.sleep(0.1)  # Simulate network latency
    cursor = await db.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return await db.fetchone(cursor)


async def example_concurrent_queries():
    """Running multiple queries at the same time"""
    print("\n6. CONCURRENT QUERIES")
    print("-" * 50)

    db = AsyncSQLiteDB()
    await db.connect()

    # Setup
    await db.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        )
    """)

    users = [
        ("Alice", "alice@example.com"),
        ("Bob", "bob@example.com"),
        ("Charlie", "charlie@example.com"),
        ("Diana", "diana@example.com"),
        ("Eve", "eve@example.com"),
    ]

    await db.executemany(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        users
    )
    await db.commit()

    # Sequential approach (slow)
    print("\nSequential fetching:")
    start = time.time()
    for user_id in [1, 2, 3, 4, 5]:
        user = await fetch_user_by_id(db, user_id)
        # print(f"  Fetched: {user['name']}")
    sequential_time = time.time() - start
    print(f"✓ Fetched 5 users sequentially in {sequential_time:.2f}s")

    # Concurrent approach (fast!)
    print("\nConcurrent fetching:")
    start = time.time()
    tasks = [fetch_user_by_id(db, user_id) for user_id in [1, 2, 3, 4, 5]]
    users_result = await asyncio.gather(*tasks)
    concurrent_time = time.time() - start
    print(f"✓ Fetched 5 users concurrently in {concurrent_time:.2f}s")
    print(f"✓ Speedup: {sequential_time/concurrent_time:.1f}x faster!")

    for user in users_result:
        if user:
            print(f"  - {user['name']} ({user['email']})")

    await db.close()


# ===== 7. Async Transactions =====

async def example_transactions():
    """Handling transactions asynchronously"""
    print("\n7. ASYNC TRANSACTIONS")
    print("-" * 50)

    db = AsyncSQLiteDB()
    await db.connect()

    # Setup
    await db.execute("""
        CREATE TABLE accounts (
            id INTEGER PRIMARY KEY,
            name TEXT,
            balance REAL
        )
    """)

    await db.executemany(
        "INSERT INTO accounts (name, balance) VALUES (?, ?)",
        [("Alice", 1000.0), ("Bob", 500.0)]
    )
    await db.commit()

    print("Initial balances:")
    cursor = await db.execute("SELECT * FROM accounts")
    for row in await db.fetchall(cursor):
        print(f"  {row['name']}: ${row['balance']}")

    # Transaction: Transfer money from Alice to Bob
    print("\nTransferring $200 from Alice to Bob...")

    try:
        # Start transaction (automatic in sqlite3)
        await db.execute(
            "UPDATE accounts SET balance = balance - ? WHERE name = ?",
            (200, "Alice")
        )

        await db.execute(
            "UPDATE accounts SET balance = balance + ? WHERE name = ?",
            (200, "Bob")
        )

        # Commit transaction
        await db.commit()
        print("✓ Transaction committed")

    except Exception as e:
        await db.rollback()
        print(f"✗ Transaction failed: {e}")
        print("✓ Rolled back")

    print("\nFinal balances:")
    cursor = await db.execute("SELECT * FROM accounts")
    for row in await db.fetchall(cursor):
        print(f"  {row['name']}: ${row['balance']}")

    # Example of failed transaction
    print("\n\nAttempting invalid transaction (will fail)...")
    try:
        # This will fail - Alice doesn't have $2000
        await db.execute(
            "UPDATE accounts SET balance = balance - ? WHERE name = ?",
            (2000, "Alice")
        )

        # Check if balance went negative (business logic)
        cursor = await db.execute("SELECT balance FROM accounts WHERE name = ?", ("Alice",))
        alice_balance = await db.fetchone(cursor)

        if alice_balance['balance'] < 0:
            raise ValueError("Insufficient funds!")

        await db.execute(
            "UPDATE accounts SET balance = balance + ? WHERE name = ?",
            (2000, "Bob")
        )

        await db.commit()

    except Exception as e:
        await db.rollback()
        print(f"✗ Transaction failed: {e}")
        print("✓ Rolled back - balances unchanged")

    await db.close()

    # With aiosqlite:
    # async with aiosqlite.connect(":memory:") as db:
    #     async with db.execute("BEGIN TRANSACTION"):
    #         await db.execute("UPDATE accounts SET balance = ?", (900,))
    #         await db.commit()


# ===== 8. Connection Pool Simulation =====

class SimpleConnectionPool:
    """Simple connection pool for demonstration"""

    def __init__(self, database: str, pool_size: int = 3):
        self.database = database
        self.pool_size = pool_size
        self.available = asyncio.Queue()
        self.all_connections = []

    async def initialize(self):
        """Create pool of connections"""
        for _ in range(self.pool_size):
            db = AsyncSQLiteDB(self.database)
            await db.connect()
            self.all_connections.append(db)
            await self.available.put(db)
        print(f"✓ Connection pool initialized with {self.pool_size} connections")

    async def acquire(self) -> AsyncSQLiteDB:
        """Acquire a connection from the pool"""
        return await self.available.get()

    async def release(self, db: AsyncSQLiteDB):
        """Return connection to pool"""
        await self.available.put(db)

    async def close_all(self):
        """Close all connections"""
        for db in self.all_connections:
            await db.close()


async def example_connection_pooling():
    """Using a connection pool"""
    print("\n8. CONNECTION POOLING")
    print("-" * 50)

    # Use a shared database file for pool (in-memory doesn't work well with pools)
    import tempfile
    import os
    db_file = tempfile.mktemp(suffix=".db")

    # Create pool
    pool = SimpleConnectionPool(db_file, pool_size=3)
    await pool.initialize()

    # Setup database
    db = await pool.acquire()
    await db.execute("""
        CREATE TABLE logs (
            id INTEGER PRIMARY KEY,
            message TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    await db.commit()
    await pool.release(db)

    # Function that uses pool
    async def log_message(pool: SimpleConnectionPool, message: str):
        db = await pool.acquire()
        try:
            await db.execute("INSERT INTO logs (message) VALUES (?)", (message,))
            await db.commit()
            await asyncio.sleep(0.1)  # Simulate work
        finally:
            await pool.release(db)

    # Multiple concurrent operations
    print("\nLogging 10 messages concurrently with pool of 3 connections...")
    start = time.time()

    tasks = [
        log_message(pool, f"Message {i}")
        for i in range(10)
    ]
    await asyncio.gather(*tasks)

    elapsed = time.time() - start
    print(f"✓ Logged 10 messages in {elapsed:.2f}s")
    print(f"  (Pool reused {pool.pool_size} connections instead of creating 10)")

    # Verify
    db = await pool.acquire()
    cursor = await db.execute("SELECT COUNT(*) as count FROM logs")
    row = await db.fetchone(cursor)
    print(f"✓ Total log entries: {row['count']}")
    await pool.release(db)

    await pool.close_all()

    # Clean up temp file
    try:
        os.unlink(db_file)
    except:
        pass


# ===== 9. Practical Example: Async Task Queue =====

class AsyncTaskQueue:
    """A simple async task queue backed by SQLite"""

    def __init__(self):
        self.db = AsyncSQLiteDB(":memory:")

    async def initialize(self):
        """Setup the task queue database"""
        await self.db.connect()
        await self.db.execute("""
            CREATE TABLE tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                result TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                completed_at TIMESTAMP
            )
        """)
        await self.db.commit()
        print("✓ Task queue initialized")

    async def add_task(self, name: str) -> int:
        """Add a task to the queue"""
        cursor = await self.db.execute(
            "INSERT INTO tasks (name) VALUES (?)",
            (name,)
        )
        await self.db.commit()
        return cursor.lastrowid

    async def get_pending_tasks(self) -> List[sqlite3.Row]:
        """Get all pending tasks"""
        cursor = await self.db.execute(
            "SELECT * FROM tasks WHERE status = 'pending' ORDER BY id"
        )
        return await self.db.fetchall(cursor)

    async def mark_completed(self, task_id: int, result: str):
        """Mark a task as completed"""
        await self.db.execute(
            """UPDATE tasks
               SET status = 'completed',
                   result = ?,
                   completed_at = CURRENT_TIMESTAMP
               WHERE id = ?""",
            (result, task_id)
        )
        await self.db.commit()

    async def get_stats(self) -> dict:
        """Get queue statistics"""
        cursor = await self.db.execute("""
            SELECT
                COUNT(*) as total,
                SUM(CASE WHEN status = 'pending' THEN 1 ELSE 0 END) as pending,
                SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) as completed
            FROM tasks
        """)
        row = await self.db.fetchone(cursor)
        return dict(row)

    async def close(self):
        """Close the database connection"""
        await self.db.close()


async def process_task(task: sqlite3.Row) -> str:
    """Simulate processing a task"""
    await asyncio.sleep(0.2)  # Simulate work
    return f"Processed: {task['name']}"


async def example_task_queue():
    """Complete example: async task queue"""
    print("\n9. PRACTICAL EXAMPLE: ASYNC TASK QUEUE")
    print("-" * 50)

    queue = AsyncTaskQueue()
    await queue.initialize()

    # Add tasks
    print("\nAdding tasks to queue...")
    task_names = [
        "Send welcome email",
        "Generate report",
        "Process payment",
        "Update search index",
        "Send notification",
    ]

    for name in task_names:
        task_id = await queue.add_task(name)
        print(f"  ✓ Added task {task_id}: {name}")

    # Show stats
    stats = await queue.get_stats()
    print(f"\nQueue stats: {stats['total']} total, {stats['pending']} pending")

    # Process tasks concurrently
    print("\nProcessing tasks...")
    pending = await queue.get_pending_tasks()

    # Process the "work" part concurrently, then update DB sequentially
    # (A single sqlite3 connection can't handle concurrent writes from threads)
    results = await asyncio.gather(*[process_task(task) for task in pending])

    for task, result in zip(pending, results):
        await queue.mark_completed(task['id'], result)
        print(f"  ✓ Completed task {task['id']}")

    # Final stats
    stats = await queue.get_stats()
    print(f"\nFinal stats: {stats['completed']} completed, {stats['pending']} pending")

    await queue.close()


# ===== Main Function =====

async def main():
    """Run all examples"""
    print("=" * 50)
    print("ASYNC DATABASE ACCESS EXAMPLES")
    print("=" * 50)
    print("\nUsing asyncio.to_thread() with sqlite3 (stdlib only)")
    print("For production, consider: pip install aiosqlite")

    await example_basic_setup()
    await example_create_table()
    await example_insert_operations()
    await example_select_queries()
    await example_update_delete()
    await example_concurrent_queries()
    await example_transactions()
    await example_connection_pooling()
    await example_task_queue()

    print("\n" + "=" * 50)
    print("All examples completed!")
    print("=" * 50)


if __name__ == "__main__":
    asyncio.run(main())
