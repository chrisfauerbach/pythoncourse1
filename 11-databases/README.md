# Section 11: Databases

Most real applications need to store data persistently. This section covers working with databases in Python — from the simple built-in SQLite to full-featured ORMs, including async database access for high-performance applications.

## Lessons

| # | Lesson | Description |
|---|--------|-------------|
| 01 | [SQLite](01-sqlite/) | Python's built-in database — no setup required |
| 02 | [SQLAlchemy](02-sqlalchemy/) | The most popular Python ORM |
| 03 | [Async Database Access](03-async-database-access/) | Non-blocking database operations |

## Setup

```bash
# SQLite is built into Python — no install needed!
# For SQLAlchemy and async:
pip install sqlalchemy aiosqlite
```

## What You'll Be Able to Do After This Section

- Create, query, and manage SQLite databases
- Use an ORM to work with databases using Python objects
- Perform async database operations for web applications

## Prerequisites

- [Section 04: OOP](../04-oop/) — essential for SQLAlchemy
- [Section 05: Intermediate](../05-intermediate/) — context managers
- [Section 07: Async Python](../07-async-python/) — for the async lesson
