"""
String Operations — Exercises
==============================

Practice problems to test your understanding of string operations.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""


# =============================================================================
# Exercise 1: Count words in a sentence
#
# Write a function that takes a sentence string and returns the number of
# words in it.
#
# Example:
#   count_words("the quick brown fox")  -> 4
#   count_words("hello")                -> 1
#   count_words("  lots   of   spaces") -> 3
#
# Hint: split() handles extra whitespace for you!
# =============================================================================

def exercise_1(sentence):
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Extract initials from a full name
#
# Write a function that takes a full name and returns the initials
# as uppercase letters separated by dots.
#
# Example:
#   get_initials("Alice Bob Carter")  -> "A.B.C"
#   get_initials("john doe")          -> "J.D"
#   get_initials("Madonna")           -> "M"
#
# Hint: split the name, grab the first character of each part, then join.
# =============================================================================

def exercise_2(full_name):
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: Basic email validator
#
# Write a function that checks if a string is a *plausible* email address.
# Return True if ALL of these conditions are met:
#   - Contains exactly one "@" symbol
#   - Has at least one character before the "@"
#   - Has a "." after the "@"
#   - Doesn't contain spaces
#
# This is NOT production-grade validation — just practice with string methods.
#
# Example:
#   is_valid_email("alice@example.com")  -> True
#   is_valid_email("bob@site.org")       -> True
#   is_valid_email("noatsign.com")       -> False
#   is_valid_email("@nodomain.com")      -> False
#   is_valid_email("has space@x.com")    -> False
#   is_valid_email("two@@signs.com")     -> False
#
# Hint: Use .count(), .find(), .split(), and " " in email
# =============================================================================

def exercise_3(email):
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: Reverse the words in a sentence
#
# Write a function that reverses the ORDER of words in a sentence,
# but keeps each word itself intact.
#
# Example:
#   reverse_words("hello world")        -> "world hello"
#   reverse_words("the quick brown fox") -> "fox brown quick the"
#   reverse_words("Python")             -> "Python"
#
# Hint: split, reverse the list (or use slicing), then join.
# =============================================================================

def exercise_4(sentence):
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Title case converter
#
# Write a function that capitalizes the first letter of each word in a
# string. Don't use the built-in .title() method — build it yourself
# using split, string concatenation or slicing, and join.
#
# Example:
#   title_case("hello world")       -> "Hello World"
#   title_case("python is fun")     -> "Python Is Fun"
#   title_case("ALREADY LOUD")      -> "Already Loud"
#
# Hint: For each word, take word[0].upper() + word[1:].lower()
# =============================================================================

def exercise_5(text):
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: Caesar cipher
#
# Write a function that shifts each letter in a string by N positions
# in the alphabet. Non-letter characters (spaces, punctuation) stay
# unchanged. Wrap around: shifting 'z' by 1 gives 'a'.
#
# Example:
#   caesar("abc", 1)         -> "bcd"
#   caesar("xyz", 3)         -> "abc"
#   caesar("Hello, World!", 5) -> "Mjqqt, Btwqi!"
#
# Hint:
#   - ord('a') gives 97, chr(97) gives 'a'
#   - For a lowercase letter: new = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
#   - Handle uppercase the same way using ord('A')
# =============================================================================

def exercise_6(text, shift):
    # YOUR CODE HERE
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1(sentence):
    words = sentence.split()
    return len(words)


def solution_2(full_name):
    parts = full_name.split()
    initials = [part[0].upper() for part in parts]
    return ".".join(initials)


def solution_3(email):
    # Check for spaces
    if " " in email:
        return False
    # Check for exactly one @
    if email.count("@") != 1:
        return False
    # Split into local and domain parts
    at_index = email.find("@")
    local = email[:at_index]
    domain = email[at_index + 1:]
    # Must have something before @
    if len(local) == 0:
        return False
    # Must have a dot in the domain
    if "." not in domain:
        return False
    return True


def solution_4(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)


def solution_5(text):
    words = text.split()
    capitalized = []
    for word in words:
        new_word = word[0].upper() + word[1:].lower()
        capitalized.append(new_word)
    return " ".join(capitalized)


def solution_6(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            # Determine the base: 'a' for lowercase, 'A' for uppercase
            base = ord("a") if ch.islower() else ord("A")
            shifted = chr((ord(ch) - base + shift) % 26 + base)
            result.append(shifted)
        else:
            result.append(ch)
    return "".join(result)


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Count words in a sentence", [
            ("exercise_1", exercise_1, ("the quick brown fox",)),
            ("solution_1", solution_1, ("the quick brown fox",)),
        ]),
        ("Extract initials from a name", [
            ("exercise_2", exercise_2, ("Alice Bob Carter",)),
            ("solution_2", solution_2, ("Alice Bob Carter",)),
        ]),
        ("Basic email validator", [
            ("exercise_3", exercise_3, ("alice@example.com",)),
            ("solution_3", solution_3, ("alice@example.com",)),
        ]),
        ("Reverse words in a sentence", [
            ("exercise_4", exercise_4, ("the quick brown fox",)),
            ("solution_4", solution_4, ("the quick brown fox",)),
        ]),
        ("Title case converter", [
            ("exercise_5", exercise_5, ("python is fun",)),
            ("solution_5", solution_5, ("python is fun",)),
        ]),
        ("Caesar cipher", [
            ("exercise_6", exercise_6, ("Hello, World!", 5)),
            ("solution_6", solution_6, ("Hello, World!", 5)),
        ]),
    ]

    for i, (title, funcs) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        for label, func, args in funcs:
            result = func(*args)
            print(f"  {label}{args} = {result!r}")
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
    print("When your exercise functions return the same values")
    print("as the solution functions, you've nailed it!")
