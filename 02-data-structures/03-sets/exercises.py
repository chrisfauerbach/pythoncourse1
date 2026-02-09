"""
Sets — Exercises
==================

Practice problems to test your understanding of sets.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""


# =============================================================================
# Exercise 1: Remove duplicates from a list
#
# Given the list below, use a set to remove duplicates.
# Then convert the result back to a sorted list and print it.
#
# Expected output:
#   [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# =============================================================================

def exercise_1():
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4]
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Find common elements
#
# Given two lists of favorite movies, find which movies both people like.
# Print the common movies sorted alphabetically.
#
# Expected output:
#   Common favorites: ['Inception', 'The Matrix']
#
# =============================================================================

def exercise_2():
    alice_movies = ["The Matrix", "Inception", "Interstellar", "Arrival"]
    bob_movies = ["Inception", "The Dark Knight", "The Matrix", "Memento"]
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: Find unique-to-each elements
#
# Using the same movie lists from Exercise 2, find movies that are
# unique to each person — movies that ONLY Alice likes or ONLY Bob likes
# (not both). Use symmetric difference.
#
# Print the result sorted alphabetically.
#
# Expected output:
#   Unique to one person: ['Arrival', 'Interstellar', 'Memento', 'The Dark Knight']
#
# =============================================================================

def exercise_3():
    alice_movies = ["The Matrix", "Inception", "Interstellar", "Arrival"]
    bob_movies = ["Inception", "The Dark Knight", "The Matrix", "Memento"]
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: Password validator
#
# Write a function that checks if a password contains at least:
#   - One uppercase letter
#   - One lowercase letter
#   - One digit
#
# Hint: Use set intersection with sets of characters.
#       For example: uppercase = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#
# Test with these passwords and print results like:
#   'hello'   -> Missing: digit, uppercase
#   'HELLO'   -> Missing: digit, lowercase
#   'Hello1'  -> Valid!
#   '12345'   -> Missing: lowercase, uppercase
#
# =============================================================================

def exercise_4():
    passwords = ["hello", "HELLO", "Hello1", "12345"]
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Unique words across sentences
#
# Given a list of sentences, find ALL unique words across every sentence.
# Convert to lowercase so "The" and "the" count as the same word.
# Print the total count and the sorted list of unique words.
#
# Expected output:
#   Total unique words: 10
#   Words: ['a', 'cat', 'dog', 'is', 'mat', 'on', 'pet', 'sat', 'the', 'too']
#
# Hint: Use .lower() and .split() on each sentence, and build up a set.
# =============================================================================

def exercise_5():
    sentences = [
        "The cat sat on the mat",
        "The dog sat on a mat too",
        "A cat is a pet",
    ]
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: Tag-based search
#
# You have a collection of blog posts, each with a set of tags.
# Implement two searches:
#   1. find_any: return titles that have ANY of the given tags
#   2. find_all: return titles that have ALL of the given tags
#
# Test searches:
#   find_any(posts, {"python", "ai"})
#   find_all(posts, {"python", "tutorial"})
#
# Expected output:
#   Posts with ANY of {'python', 'ai'}:
#     - Intro to Python
#     - Python Sets Deep Dive
#     - Machine Learning 101
#   Posts with ALL of {'python', 'tutorial'}:
#     - Intro to Python
#     - Python Sets Deep Dive
#
# Hint: For "any", check if the intersection is non-empty.
#       For "all", check if the search tags are a subset of the post's tags.
# =============================================================================

def exercise_6():
    posts = [
        {"title": "Intro to Python", "tags": {"python", "beginner", "tutorial"}},
        {"title": "Python Sets Deep Dive", "tags": {"python", "sets", "tutorial"}},
        {"title": "Machine Learning 101", "tags": {"ai", "beginner", "math"}},
        {"title": "CSS Grid Layout", "tags": {"css", "web", "frontend"}},
        {"title": "JavaScript Async", "tags": {"javascript", "web", "async"}},
    ]
    # YOUR CODE HERE
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4]
    unique = sorted(set(numbers))
    print(unique)


def solution_2():
    alice_movies = ["The Matrix", "Inception", "Interstellar", "Arrival"]
    bob_movies = ["Inception", "The Dark Knight", "The Matrix", "Memento"]
    common = sorted(set(alice_movies) & set(bob_movies))
    print(f"Common favorites: {common}")


def solution_3():
    alice_movies = ["The Matrix", "Inception", "Interstellar", "Arrival"]
    bob_movies = ["Inception", "The Dark Knight", "The Matrix", "Memento"]
    unique_to_one = sorted(set(alice_movies) ^ set(bob_movies))
    print(f"Unique to one person: {unique_to_one}")


def solution_4():
    passwords = ["hello", "HELLO", "Hello1", "12345"]

    uppercase = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lowercase = set("abcdefghijklmnopqrstuvwxyz")
    digits = set("0123456789")

    for pw in passwords:
        pw_chars = set(pw)
        missing = []
        if not pw_chars & digits:
            missing.append("digit")
        if not pw_chars & lowercase:
            missing.append("lowercase")
        if not pw_chars & uppercase:
            missing.append("uppercase")

        if missing:
            print(f"'{pw}' -> Missing: {', '.join(missing)}")
        else:
            print(f"'{pw}' -> Valid!")


def solution_5():
    sentences = [
        "The cat sat on the mat",
        "The dog sat on a mat too",
        "A cat is a pet",
    ]

    all_words = set()
    for sentence in sentences:
        words = sentence.lower().split()
        all_words.update(words)

    print(f"Total unique words: {len(all_words)}")
    print(f"Words: {sorted(all_words)}")


def solution_6():
    posts = [
        {"title": "Intro to Python", "tags": {"python", "beginner", "tutorial"}},
        {"title": "Python Sets Deep Dive", "tags": {"python", "sets", "tutorial"}},
        {"title": "Machine Learning 101", "tags": {"ai", "beginner", "math"}},
        {"title": "CSS Grid Layout", "tags": {"css", "web", "frontend"}},
        {"title": "JavaScript Async", "tags": {"javascript", "web", "async"}},
    ]

    def find_any(posts, search_tags):
        return [p["title"] for p in posts if p["tags"] & search_tags]

    def find_all(posts, search_tags):
        return [p["title"] for p in posts if search_tags <= p["tags"]]

    any_tags = {"python", "ai"}
    all_tags = {"python", "tutorial"}

    print(f"Posts with ANY of {any_tags}:")
    for title in find_any(posts, any_tags):
        print(f"  - {title}")

    print(f"Posts with ALL of {all_tags}:")
    for title in find_all(posts, all_tags):
        print(f"  - {title}")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Remove duplicates from a list", exercise_1),
        ("Find common elements", exercise_2),
        ("Find unique-to-each elements", exercise_3),
        ("Password validator", exercise_4),
        ("Unique words across sentences", exercise_5),
        ("Tag-based search", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
