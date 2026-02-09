"""
SQLAlchemy — Example Code
==========================

Run this file:
    python3 example.py

A comprehensive tour of SQLAlchemy's ORM. Each section demonstrates a key
concept with real output so you can see exactly how it works.
"""

import sys

try:
    from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Table, func, and_, or_
    from sqlalchemy.orm import declarative_base, Session, relationship
except ImportError:
    print("SQLAlchemy is not installed. Run: pip install sqlalchemy")
    print("Then try again!")
    sys.exit(0)


# =============================================================================
# 1. Setting up SQLAlchemy — engine and base
# =============================================================================

print("=" * 70)
print("1. SETTING UP SQLALCHEMY")
print("=" * 70)

# Create a declarative base — all models inherit from this
Base = declarative_base()

# Create an in-memory SQLite database (no files left behind)
engine = create_engine("sqlite:///:memory:", echo=False)
print("Created engine: sqlite:///:memory:")
print("(echo=False means we won't see SQL queries printed)")
print()


# =============================================================================
# 2. Defining models — tables as Python classes
# =============================================================================

print("=" * 70)
print("2. DEFINING MODELS")
print("=" * 70)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', age={self.age})>"

print("Defined User model:")
print(f"  Table name: {User.__tablename__}")
print(f"  Columns: id, name, email, age")
print()


# =============================================================================
# 3. Creating tables from models
# =============================================================================

print("=" * 70)
print("3. CREATING TABLES")
print("=" * 70)

# This creates all tables defined in our models
Base.metadata.create_all(engine)
print("Created all tables in the database")
print()


# =============================================================================
# 4. Creating a session — your workspace
# =============================================================================

print("=" * 70)
print("4. CREATING A SESSION")
print("=" * 70)

session = Session(engine)
print("Created session — this is where we'll do our database work")
print()


# =============================================================================
# 5. Adding records — CREATE operation
# =============================================================================

print("=" * 70)
print("5. ADDING RECORDS (CREATE)")
print("=" * 70)

# Create user objects
alice = User(name="Alice", email="alice@example.com", age=30)
bob = User(name="Bob", email="bob@example.com", age=25)
carol = User(name="Carol", email="carol@example.com", age=35)

print("Created user objects (not yet in database):")
print(f"  {alice}")
print(f"  {bob}")
print(f"  {carol}")
print()

# Add to session
session.add(alice)
session.add(bob)
# Or add multiple at once
session.add_all([carol])

print("Added users to session (staged but not committed)")
print()

# Commit to database
session.commit()
print("Committed! Users are now in the database.")
print()


# =============================================================================
# 6. Querying records — READ operation
# =============================================================================

print("=" * 70)
print("6. QUERYING RECORDS (READ)")
print("=" * 70)

# Get all users
all_users = session.query(User).all()
print(f"All users ({len(all_users)}):")
for user in all_users:
    print(f"  {user}")
print()

# Get first user
first_user = session.query(User).first()
print(f"First user: {first_user}")
print()

# Filter by name
alice_query = session.query(User).filter(User.name == "Alice").first()
print(f"User named Alice: {alice_query}")
print()

# Filter by age
adults = session.query(User).filter(User.age >= 30).all()
print(f"Users age 30+: {adults}")
print()

# Get by primary key
user_1 = session.get(User, 1)
print(f"User with id=1: {user_1}")
print()


# =============================================================================
# 7. Updating records — UPDATE operation
# =============================================================================

print("=" * 70)
print("7. UPDATING RECORDS (UPDATE)")
print("=" * 70)

# Query and modify
alice = session.query(User).filter(User.name == "Alice").first()
print(f"Before: {alice}")

alice.age = 31
session.commit()

alice = session.query(User).filter(User.name == "Alice").first()
print(f"After:  {alice}")
print()


# =============================================================================
# 8. Deleting records — DELETE operation
# =============================================================================

print("=" * 70)
print("8. DELETING RECORDS (DELETE)")
print("=" * 70)

# Add a temporary user
temp = User(name="Temporary", email="temp@example.com", age=99)
session.add(temp)
session.commit()

print(f"Added: {temp}")
count = session.query(User).count()
print(f"Total users: {count}")
print()

# Delete it
session.delete(temp)
session.commit()

print("Deleted temporary user")
count = session.query(User).count()
print(f"Total users now: {count}")
print()


# =============================================================================
# 9. Relationships — one-to-many
# =============================================================================

print("=" * 70)
print("9. RELATIONSHIPS (ONE-TO-MANY)")
print("=" * 70)

# Define new models with relationships
class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", back_populates="author")

    def __repr__(self):
        return f"<Author(name='{self.name}')>"

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")

    def __repr__(self):
        return f"<Book(title='{self.title}')>"

# Create tables
Base.metadata.create_all(engine)

# Add authors and books
author1 = Author(name="Isaac Asimov")
author1.books = [
    Book(title="Foundation"),
    Book(title="I, Robot"),
    Book(title="The Gods Themselves"),
]

author2 = Author(name="Ursula K. Le Guin")
author2.books = [
    Book(title="The Left Hand of Darkness"),
    Book(title="The Dispossessed"),
]

session.add_all([author1, author2])
session.commit()

print("Added authors and books")
print()

# Query and navigate relationships
all_authors = session.query(Author).all()
for author in all_authors:
    print(f"{author.name} wrote {len(author.books)} books:")
    for book in author.books:
        print(f"  - {book.title}")
    print()

# Navigate from book to author
foundation = session.query(Book).filter(Book.title == "Foundation").first()
print(f"'{foundation.title}' was written by {foundation.author.name}")
print()


# =============================================================================
# 10. Advanced queries — filtering and ordering
# =============================================================================

print("=" * 70)
print("10. ADVANCED QUERIES")
print("=" * 70)

# Add more users for querying
more_users = [
    User(name="Dave", email="dave@example.com", age=28),
    User(name="Eve", email="eve@example.com", age=22),
    User(name="Frank", email="frank@example.com", age=45),
]
session.add_all(more_users)
session.commit()

# Order by age (ascending)
print("Users ordered by age (ascending):")
users = session.query(User).order_by(User.age).all()
for user in users:
    print(f"  {user.name}: {user.age}")
print()

# Order by age (descending)
print("Users ordered by age (descending):")
users = session.query(User).order_by(User.age.desc()).all()
for user in users:
    print(f"  {user.name}: {user.age}")
print()

# Limit results
print("Top 3 oldest users:")
users = session.query(User).order_by(User.age.desc()).limit(3).all()
for user in users:
    print(f"  {user.name}: {user.age}")
print()

# Count
count = session.query(User).count()
print(f"Total users: {count}")
print()


# =============================================================================
# 11. Aggregations and functions
# =============================================================================

print("=" * 70)
print("11. AGGREGATIONS")
print("=" * 70)

avg_age = session.query(func.avg(User.age)).scalar()
print(f"Average age: {avg_age:.1f}")

min_age = session.query(func.min(User.age)).scalar()
max_age = session.query(func.max(User.age)).scalar()
print(f"Age range: {min_age} - {max_age}")

# Count by condition
adults = session.query(User).filter(User.age >= 30).count()
print(f"Users 30+: {adults}")
print()


# =============================================================================
# 12. Complex filters with AND/OR
# =============================================================================

print("=" * 70)
print("12. COMPLEX FILTERS")
print("=" * 70)

# AND — both conditions must be true
young_bobs = session.query(User).filter(
    and_(User.name == "Bob", User.age < 30)
).all()
print(f"Users named Bob under 30: {young_bobs}")

# OR — at least one condition must be true
alices_or_bobs = session.query(User).filter(
    or_(User.name == "Alice", User.name == "Bob")
).all()
print(f"Users named Alice or Bob: {[u.name for u in alices_or_bobs]}")

# Between ages
mid_range = session.query(User).filter(
    and_(User.age >= 25, User.age <= 35)
).all()
print(f"Users aged 25-35: {[f'{u.name}({u.age})' for u in mid_range]}")
print()


# =============================================================================
# 13. Joins — querying across relationships
# =============================================================================

print("=" * 70)
print("13. JOINS")
print("=" * 70)

# Find all authors who have books with "The" in the title
authors_with_the = session.query(Author).join(Book).filter(
    Book.title.contains("The")
).distinct().all()

print("Authors with 'The' in a book title:")
for author in authors_with_the:
    print(f"  {author.name}")
    the_books = [b for b in author.books if "The" in b.title]
    for book in the_books:
        print(f"    - {book.title}")
print()


# =============================================================================
# 14. Putting it all together — a mini blog system
# =============================================================================

print("=" * 70)
print("14. PUTTING IT ALL TOGETHER — MINI BLOG")
print("=" * 70)

class BlogUser(Base):
    __tablename__ = "blog_users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    posts = relationship("Post", back_populates="author")

    def __repr__(self):
        return f"<BlogUser(username='{self.username}')>"

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String)
    views = Column(Integer, default=0)
    author_id = Column(Integer, ForeignKey("blog_users.id"))
    author = relationship("BlogUser", back_populates="posts")
    comments = relationship("Comment", back_populates="post")

    def __repr__(self):
        return f"<Post(title='{self.title}', views={self.views})>"

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    post_id = Column(Integer, ForeignKey("posts.id"))
    post = relationship("Post", back_populates="comments")

    def __repr__(self):
        return f"<Comment(text='{self.text[:20]}...')>"

# Create tables
Base.metadata.create_all(engine)

# Create users
user1 = BlogUser(username="pythonista")
user2 = BlogUser(username="codewizard")

# Create posts
post1 = Post(
    title="Getting Started with SQLAlchemy",
    content="SQLAlchemy is an amazing ORM...",
    views=150,
    author=user1
)

post2 = Post(
    title="10 Python Tips",
    content="Here are my favorite Python tips...",
    views=230,
    author=user1
)

post3 = Post(
    title="Async Python Guide",
    content="Learn asyncio the right way...",
    views=180,
    author=user2
)

# Add comments
post1.comments = [
    Comment(text="Great tutorial!"),
    Comment(text="Very helpful, thanks!"),
]

post2.comments = [
    Comment(text="Tip #5 blew my mind"),
]

session.add_all([user1, user2])
session.commit()

print("Created blog with users, posts, and comments")
print()

# Query: Find most popular posts
print("Most popular posts:")
popular_posts = session.query(Post).order_by(Post.views.desc()).limit(3).all()
for post in popular_posts:
    print(f"  '{post.title}' by {post.author.username} — {post.views} views")
print()

# Query: Posts with comments
print("Posts with comments:")
posts_with_comments = session.query(Post).join(Comment).distinct().all()
for post in posts_with_comments:
    print(f"  '{post.title}' has {len(post.comments)} comment(s)")
    for comment in post.comments:
        print(f"    - {comment.text}")
print()

# Query: User activity
print("User activity:")
users = session.query(BlogUser).all()
for user in users:
    total_views = sum(post.views for post in user.posts)
    print(f"  {user.username}: {len(user.posts)} posts, {total_views} total views")
print()

# Close session
session.close()

print("=" * 70)
print("   SQLALCHEMY BASICS COMPLETE!")
print("=" * 70)
print()
print("You've seen:")
print("  - Model definition with relationships")
print("  - CRUD operations")
print("  - Querying with filters and ordering")
print("  - Aggregations and joins")
print("  - A complete mini application")
print()
print("Try modifying the examples and run the file again!")
