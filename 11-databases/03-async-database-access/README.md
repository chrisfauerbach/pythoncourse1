# Async Database Access

## Objective

Learn to perform non-blocking database operations using async patterns in Python, making your database-heavy applications more efficient and responsive.

## Concepts Covered

- Blocking vs non-blocking database calls
- Using `asyncio.to_thread()` with standard library sqlite3
- Native async database libraries (aiosqlite)
- Async transactions and connection management
- Connection pooling concepts
- When to use async vs sync database access

## Prerequisites

- [SQLite Basics](../01-sqlite-basics/)
- [Async Python](../../07-async-python/)

## Lesson

### Why Async Database Access?

Database operations are I/O bound—your program spends most of the time waiting for the database to respond, not computing. In traditional synchronous code, this means your entire program blocks while waiting for a query to complete.

**Synchronous (blocking) approach:**
```python
def fetch_user(user_id):
    conn = sqlite3.connect("users.db")
    result = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    # Program waits here, can't do anything else
    return result.fetchone()

# If this takes 100ms, you can only do 10 requests per second
```

**Async (non-blocking) approach:**
```python
async def fetch_user(user_id):
    # While waiting for DB, other tasks can run
    result = await db.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return await result.fetchone()

# Can handle many concurrent requests during that 100ms
```

### Blocking vs Non-Blocking Database Calls

**Blocking calls** stop your entire program:
- Simple to understand and debug
- One operation at a time
- Perfect for scripts, CLI tools, simple apps
- Limited throughput under concurrent load

**Non-blocking calls** let other work happen:
- More complex code structure
- Many operations can wait simultaneously
- Great for web servers, APIs, real-time systems
- Higher throughput under concurrent load

Think of it like a restaurant:
- **Blocking**: One waiter serves one table completely before taking the next order
- **Non-blocking**: One waiter takes multiple orders, delivers them as the kitchen finishes

### Two Approaches to Async Database in Python

#### 1. asyncio.to_thread() with Standard Library sqlite3

**Pros:**
- No external dependencies
- Works with any blocking code
- Easy to adopt incrementally
- Great for learning

**Cons:**
- Uses thread pool (some overhead)
- Not "true" async (still blocks a thread)
- Limited to what threading can handle

```python
import asyncio
import sqlite3

async def query_database():
    conn = sqlite3.connect(":memory:")
    # Run blocking call in thread pool
    result = await asyncio.to_thread(
        conn.execute, "SELECT * FROM users"
    )
    rows = await asyncio.to_thread(result.fetchall)
    return rows
```

#### 2. Native Async Libraries (aiosqlite, asyncpg, motor)

**Pros:**
- True async I/O (no threads)
- Better performance at scale
- Designed for async patterns
- Clean async/await syntax

**Cons:**
- External dependencies
- Library-specific APIs
- May not support all features

```python
import aiosqlite  # pip install aiosqlite

async def query_database():
    async with aiosqlite.connect(":memory:") as db:
        async with db.execute("SELECT * FROM users") as cursor:
            rows = await cursor.fetchall()
            return rows
```

### Connection Pooling

When handling many concurrent requests, you don't want to open a new database connection for each one. Connection pooling reuses a fixed number of connections:

```python
# Concept: Pool maintains N connections
# Request 1 → borrows connection A
# Request 2 → borrows connection B
# Request 3 → waits if all connections busy
# Request 1 finishes → returns connection A to pool
# Request 3 → borrows connection A
```

For SQLite, connection pooling is less critical since it's file-based, but for client-server databases (PostgreSQL, MySQL), it's essential.

### Async Transactions

Transactions ensure multiple operations complete atomically (all or nothing):

```python
async def transfer_money(from_id, to_id, amount):
    async with db.transaction():  # Starts transaction
        # Deduct from sender
        await db.execute(
            "UPDATE accounts SET balance = balance - ? WHERE id = ?",
            (amount, from_id)
        )
        # Add to receiver
        await db.execute(
            "UPDATE accounts SET balance = balance + ? WHERE id = ?",
            (amount, to_id)
        )
        # If any error occurs, both operations roll back
    # If we reach here, transaction commits
```

### When Do You Actually Need Async Database Access?

**Use async when:**
- Building web APIs handling many concurrent requests
- Real-time systems (chat, notifications, live dashboards)
- Microservices with high throughput requirements
- You're already using async (aiohttp, FastAPI, etc.)
- Multiple database operations can happen independently

**Stick with sync when:**
- Writing scripts, CLI tools, batch jobs
- Low concurrency requirements (< 10 simultaneous users)
- Simple CRUD applications
- Team isn't familiar with async patterns
- The complexity isn't worth the benefit

**Reality check:** Most applications don't need async databases. Start with sync, measure, and only add async complexity if you have a proven bottleneck.

### Common Patterns

**Pattern 1: Concurrent Queries**
```python
# Fetch multiple users in parallel
async def fetch_users(user_ids):
    tasks = [fetch_user(uid) for uid in user_ids]
    return await asyncio.gather(*tasks)
```

**Pattern 2: Background Worker**
```python
# Process queue items without blocking
async def process_queue():
    while True:
        item = await db.fetch_next_item()
        if item:
            await process_item(item)
        else:
            await asyncio.sleep(1)  # Poll every second
```

**Pattern 3: Parallel Read + Write**
```python
# Read from multiple tables at once
async def get_dashboard_data(user_id):
    user, orders, stats = await asyncio.gather(
        fetch_user(user_id),
        fetch_orders(user_id),
        fetch_statistics(user_id)
    )
    return {"user": user, "orders": orders, "stats": stats}
```

### Best Practices

1. **Don't mix sync and async code**: If using async, commit fully. Mixing causes confusion.

2. **Use connection context managers**: Always ensure connections close properly.

3. **Handle errors gracefully**: Database errors should not crash your event loop.

4. **Set reasonable timeouts**: Don't let slow queries block forever.

5. **Monitor connection pool size**: Too small = requests wait, too large = resource waste.

6. **Test with realistic concurrency**: Async benefits only appear under load.

### Common Pitfalls

- **Forgetting await**: Database calls won't execute if you forget `await`
- **Blocking the event loop**: Putting heavy CPU work in async functions
- **Connection leaks**: Not closing connections in error cases
- **Over-engineering**: Adding async when sync would work fine

## Code Example

Check out [`example.py`](example.py) for a complete working example showing:
- Basic async database operations
- Concurrent queries
- Transaction handling
- Connection management
- Practical task queue implementation

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Further Reading

- [aiosqlite documentation](https://aiosqlite.omnilib.dev/)
- [asyncpg for PostgreSQL](https://magicstack.github.io/asyncpg/)
- [SQLAlchemy async support](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)
- [asyncio documentation](https://docs.python.org/3/library/asyncio.html)

## Key Takeaways

- Async database access lets your program handle many operations concurrently
- Use `asyncio.to_thread()` with sqlite3 for no-dependency learning
- Native async libraries like aiosqlite offer better performance
- Connection pooling is crucial for client-server databases
- Most applications don't need async—measure before optimizing
- Async shines in high-concurrency scenarios (web APIs, real-time systems)
