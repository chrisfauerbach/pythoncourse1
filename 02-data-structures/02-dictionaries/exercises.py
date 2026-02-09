"""
Dictionaries — Exercises
=========================

Practice problems to test your understanding of dictionaries.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""


# =============================================================================
# Exercise 1: Word frequency counter
#
# Write a function that takes a sentence (string) and returns a dictionary
# mapping each word to the number of times it appears.
#
# Example:
#   word_frequencies("the cat sat on the mat")
#   -> {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}
#
# Hint: Use .split() to break the sentence into words, and .get() to count.
# Bonus: Convert words to lowercase so "The" and "the" count as the same word.
# =============================================================================

def exercise_1():
    sentence = "To be or not to be that is the question"
    # YOUR CODE HERE — build a frequency dict and print it
    pass


# =============================================================================
# Exercise 2: Merge two dictionaries with conflict resolution
#
# You have two dictionaries representing inventory from two warehouses.
# Merge them into a single dictionary. If both warehouses have the same item,
# ADD the quantities together (don't just overwrite).
#
# Example:
#   warehouse_a = {"apples": 5, "bananas": 3, "oranges": 7}
#   warehouse_b = {"bananas": 4, "oranges": 2, "grapes": 6}
#   -> {"apples": 5, "bananas": 7, "oranges": 9, "grapes": 6}
#
# Hint: Start with a copy of one dict, then iterate over the other.
# =============================================================================

def exercise_2():
    warehouse_a = {"apples": 5, "bananas": 3, "oranges": 7}
    warehouse_b = {"bananas": 4, "oranges": 2, "grapes": 6}
    # YOUR CODE HERE — merge with summed quantities and print the result
    pass


# =============================================================================
# Exercise 3: Invert a dictionary
#
# Write code that swaps the keys and values of a dictionary.
#
# Example:
#   original = {"a": 1, "b": 2, "c": 3}
#   -> {1: "a", 2: "b", 3: "c"}
#
# Use the `capitals` dict below. Print the inverted version.
# =============================================================================

def exercise_3():
    capitals = {"France": "Paris", "Japan": "Tokyo", "Brazil": "Brasilia"}
    # YOUR CODE HERE — invert the dict so cities are keys and countries are values
    pass


# =============================================================================
# Exercise 4: Student grade book (nested dictionaries)
#
# Given the grade book below, do the following:
#   a) Print Alice's science grade
#   b) Calculate and print each student's average grade
#   c) Find and print the student with the highest average
#
# =============================================================================

def exercise_4():
    gradebook = {
        "Alice": {"math": 92, "english": 88, "science": 95},
        "Bob":   {"math": 78, "english": 85, "science": 80},
        "Carol": {"math": 90, "english": 91, "science": 87},
        "Dave":  {"math": 65, "english": 72, "science": 70},
    }
    # YOUR CODE HERE
    # a) Print Alice's science grade
    # b) Print each student's average
    # c) Print the name of the student with the highest average
    pass


# =============================================================================
# Exercise 5: Group words by first letter
#
# Given a list of words, create a dictionary that groups them by their first
# letter. Each key should be a letter, and each value should be a list of
# words starting with that letter.
#
# Example:
#   ["apple", "avocado", "banana", "blueberry", "cherry"]
#   -> {"a": ["apple", "avocado"], "b": ["banana", "blueberry"], "c": ["cherry"]}
#
# Hint: .setdefault() makes this really clean.
# =============================================================================

def exercise_5():
    words = ["python", "java", "javascript", "perl", "php", "ruby", "rust", "go", "julia"]
    # YOUR CODE HERE — group by first letter and print the result
    pass


# =============================================================================
# Exercise 6: Simple phone book
#
# Build a phone book using a dictionary. Implement three operations as
# separate functions:
#   - add_contact(phone_book, name, number) — add or update a contact
#   - lookup_contact(phone_book, name) — return the number or "Not found"
#   - delete_contact(phone_book, name) — remove a contact, return True/False
#
# Then use them to:
#   1. Add three contacts
#   2. Look up an existing contact
#   3. Look up a missing contact
#   4. Delete a contact
#   5. Print the final phone book
# =============================================================================

def exercise_6():
    # YOUR CODE HERE — define the three helper functions, then use them
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    sentence = "To be or not to be that is the question"
    words = sentence.lower().split()
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    print("Sentence:", sentence)
    print("Frequencies:", frequencies)


def solution_2():
    warehouse_a = {"apples": 5, "bananas": 3, "oranges": 7}
    warehouse_b = {"bananas": 4, "oranges": 2, "grapes": 6}

    merged = dict(warehouse_a)  # Start with a copy of warehouse_a
    for item, qty in warehouse_b.items():
        merged[item] = merged.get(item, 0) + qty

    print("Warehouse A:", warehouse_a)
    print("Warehouse B:", warehouse_b)
    print("Merged:", merged)


def solution_3():
    capitals = {"France": "Paris", "Japan": "Tokyo", "Brazil": "Brasilia"}
    inverted = {city: country for country, city in capitals.items()}
    print("Original:", capitals)
    print("Inverted:", inverted)


def solution_4():
    gradebook = {
        "Alice": {"math": 92, "english": 88, "science": 95},
        "Bob":   {"math": 78, "english": 85, "science": 80},
        "Carol": {"math": 90, "english": 91, "science": 87},
        "Dave":  {"math": 65, "english": 72, "science": 70},
    }

    # a) Alice's science grade
    print(f"Alice's science grade: {gradebook['Alice']['science']}")

    # b) Each student's average
    averages = {}
    for student, grades in gradebook.items():
        avg = sum(grades.values()) / len(grades)
        averages[student] = avg
        print(f"  {student}: average = {avg:.1f}")

    # c) Student with the highest average
    best = max(averages, key=averages.get)
    print(f"Highest average: {best} ({averages[best]:.1f})")


def solution_5():
    words = ["python", "java", "javascript", "perl", "php", "ruby", "rust", "go", "julia"]
    groups = {}
    for word in words:
        groups.setdefault(word[0], []).append(word)

    print("Words:", words)
    print("Grouped by first letter:")
    for letter, group in sorted(groups.items()):
        print(f"  {letter}: {group}")


def solution_6():
    def add_contact(phone_book, name, number):
        phone_book[name] = number
        print(f"  Added: {name} -> {number}")

    def lookup_contact(phone_book, name):
        return phone_book.get(name, "Not found")

    def delete_contact(phone_book, name):
        if name in phone_book:
            del phone_book[name]
            print(f"  Deleted: {name}")
            return True
        print(f"  Not found: {name}")
        return False

    phone_book = {}

    # 1. Add three contacts
    add_contact(phone_book, "Alice", "555-1234")
    add_contact(phone_book, "Bob", "555-5678")
    add_contact(phone_book, "Carol", "555-9012")

    # 2. Look up an existing contact
    print(f"  Lookup Alice: {lookup_contact(phone_book, 'Alice')}")

    # 3. Look up a missing contact
    print(f"  Lookup Dave: {lookup_contact(phone_book, 'Dave')}")

    # 4. Delete a contact
    delete_contact(phone_book, "Bob")

    # 5. Print the final phone book
    print("  Final phone book:")
    for name, number in phone_book.items():
        print(f"    {name}: {number}")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Word frequency counter", exercise_1),
        ("Merge dictionaries with conflict resolution", exercise_2),
        ("Invert a dictionary", exercise_3),
        ("Student grade book (nested dicts)", exercise_4),
        ("Group words by first letter", exercise_5),
        ("Simple phone book", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
