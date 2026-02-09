# SQLAlchemy

## Objective

Work with databases using Python's most popular ORM (Object-Relational Mapping) library.

## Concepts Covered

- What an ORM is and why you'd use one
- SQLAlchemy Core vs ORM
- Defining database models as Python classes
- Creating engines and sessions
- CRUD operations (Create, Read, Update, Delete)
- Relationships between tables (one-to-many, many-to-many)
- Querying with filters, ordering, and joins
- Database migrations with Alembic

## Prerequisites

- [Section 04: Object-Oriented Programming](../../04-oop/)
- [11-databases/01-sqlite](../01-sqlite/)

## What is an ORM?

An ORM (Object-Relational Mapping) is a technique that lets you interact with databases using your programming language's objects instead of writing SQL. Instead of:

```sql
SELECT * FROM users WHERE age > 21;
```

You write:

```python
session.query(User).filter(User.age > 21).all()
```

The ORM translates your Python code into SQL behind the scenes. This gives you:

- **Type safety** — your editor can autocomplete field names
- **Less SQL** — no need to write raw queries for common operations
- **Portability** — switch databases (SQLite → PostgreSQL) with minimal code changes
- **Relationships** — easily navigate between related objects (users → posts → comments)

## SQLAlchemy: Core vs ORM

SQLAlchemy has two main APIs:

1. **Core** — Lower-level SQL expression language. You build queries programmatically but still think in SQL terms (tables, columns, joins).

2. **ORM** — Higher-level object-oriented API. You define models as Python classes and work with objects. The ORM uses Core under the hood.

Most projects use the ORM because it's more Pythonic and easier to work with. We'll focus on the ORM in this lesson.

## Basic Workflow

Here's the typical SQLAlchemy workflow:

1. **Define models** — Create classes that represent database tables
2. **Create an engine** — Connection to your database
3. **Create tables** — Generate the schema from your models
4. **Create a session** — A workspace for database operations
5. **CRUD operations** — Add, query, update, delete records
6. **Commit** — Save your changes to the database

## Defining Models

Models are Python classes that inherit from `Base` (created by `declarative_base()`). Each class represents a table, and each attribute represents a column:

```python
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    age = Column(Integer)
```

Common column types:
- `Integer`, `Float`, `String`, `Boolean`
- `DateTime`, `Date`, `Time`
- `Text` (for long strings)
- `JSON` (stores JSON data)

Column options:
- `primary_key=True` — Makes this the primary key
- `nullable=False` — Field is required
- `unique=True` — Value must be unique
- `default=value` — Default value for new records

## Creating the Engine and Session

The **engine** manages the database connection:

```python
from sqlalchemy import create_engine

# SQLite in-memory (great for testing)
engine = create_engine("sqlite:///:memory:")

# SQLite file
engine = create_engine("sqlite:///myapp.db")

# PostgreSQL
engine = create_engine("postgresql://user:pass@localhost/dbname")
```

The **session** is your workspace for database operations:

```python
from sqlalchemy.orm import Session

session = Session(engine)
```

Create the tables:

```python
Base.metadata.create_all(engine)
```

## CRUD Operations

**Create** — Add new records:

```python
user = User(name="Alice", email="alice@example.com", age=30)
session.add(user)
session.commit()  # Save to database
```

**Read** — Query records:

```python
# Get all users
users = session.query(User).all()

# Get first matching user
user = session.query(User).filter(User.name == "Alice").first()

# Filter by multiple conditions
adults = session.query(User).filter(User.age >= 18).all()

# Get by primary key
user = session.get(User, 1)
```

**Update** — Modify records:

```python
user = session.query(User).filter(User.name == "Alice").first()
user.age = 31
session.commit()
```

**Delete** — Remove records:

```python
user = session.query(User).filter(User.name == "Alice").first()
session.delete(user)
session.commit()
```

## Relationships

SQLAlchemy makes it easy to define relationships between tables.

**One-to-Many** (e.g., a user has many posts):

```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    posts = relationship("Post", back_populates="author")

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
```

Now you can navigate relationships:

```python
user = session.query(User).first()
for post in user.posts:
    print(post.title)

post = session.query(Post).first()
print(f"Written by: {post.author.name}")
```

**Many-to-Many** (e.g., students and courses):

```python
from sqlalchemy import Table

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

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("Student", secondary=student_courses, back_populates="courses")
```

## Advanced Querying

**Ordering**:

```python
# Ascending
users = session.query(User).order_by(User.name).all()

# Descending
users = session.query(User).order_by(User.age.desc()).all()
```

**Limiting**:

```python
# First 10 users
users = session.query(User).limit(10).all()
```

**Counting**:

```python
count = session.query(User).count()
```

**Aggregates**:

```python
from sqlalchemy import func

avg_age = session.query(func.avg(User.age)).scalar()
max_age = session.query(func.max(User.age)).scalar()
```

**Joins**:

```python
# Join users and posts
results = session.query(User, Post).join(Post).all()

# Filter on joined table
users_with_posts = session.query(User).join(Post).filter(Post.title.contains("Python")).all()
```

**Combining Filters**:

```python
from sqlalchemy import and_, or_

# AND
adults_named_alice = session.query(User).filter(
    and_(User.name == "Alice", User.age >= 18)
).all()

# OR
users = session.query(User).filter(
    or_(User.name == "Alice", User.name == "Bob")
).all()
```

## Database Migrations

As your app evolves, you'll need to change your database schema (add columns, rename tables, etc.). Writing migration scripts manually is error-prone.

**Alembic** is the migration tool for SQLAlchemy. It tracks schema changes and generates migration scripts automatically.

Install:
```bash
pip install alembic
```

Initialize:
```bash
alembic init migrations
```

Generate a migration:
```bash
alembic revision --autogenerate -m "Add email column"
```

Apply migrations:
```bash
alembic upgrade head
```

Alembic compares your models to the database and generates the SQL needed to sync them. This is crucial for production apps where you can't just delete and recreate tables.

## Best Practices

1. **Use sessions properly** — Always commit or rollback. Use context managers:
   ```python
   with Session(engine) as session:
       user = User(name="Alice")
       session.add(user)
       session.commit()
   ```

2. **Avoid N+1 queries** — Use `joinedload()` to eager-load relationships:
   ```python
   from sqlalchemy.orm import joinedload
   users = session.query(User).options(joinedload(User.posts)).all()
   ```

3. **Use indexes** — Add indexes to frequently queried columns:
   ```python
   email = Column(String, index=True)
   ```

4. **Close sessions** — Call `session.close()` when done, or use context managers.

5. **Use environment variables for connection strings** — Never hardcode credentials.

## When to Use SQLAlchemy

**Use it when:**
- Building web apps with complex data models
- You want type safety and autocomplete for database queries
- You need to support multiple databases
- Your app has lots of relationships between tables

**Skip it when:**
- You're doing simple one-off scripts (raw SQL might be easier)
- You need maximum performance (raw SQL is faster)
- Your queries are extremely complex (sometimes raw SQL is clearer)

## Further Reading

- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [SQLAlchemy ORM Tutorial](https://docs.sqlalchemy.org/en/20/orm/tutorial.html)
- [Alembic Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

## Code Example

Check out [`example.py`](example.py) for a complete working example demonstrating all these concepts.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.
