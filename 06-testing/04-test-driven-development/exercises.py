"""
Test-Driven Development — Exercises
====================================

These exercises flip the usual pattern: the TESTS are already written for you.
Your job is to write the CODE that makes them pass.

This is exactly what TDD feels like in practice — you read a failing test,
understand what it expects, and write just enough code to make it pass.

Run this file:
    python3 exercises.py

You'll see a bunch of failures at first. That's the RED phase! Your job is
to replace each `pass` with real code until everything is GREEN.

Each exercise has:
  - A stub function (with `pass`) — this is what you need to implement
  - A test class — these are already written, don't modify them
  - A solution at the bottom — no peeking until you've tried!
"""

import unittest
import re


# =============================================================================
# Exercise 1: Simple Calculator
#
# Make the tests pass by implementing add() and multiply().
# These are simple — just get your feet wet with the TDD mindset.
#
# =============================================================================

def add(a, b):
    # YOUR CODE HERE
    pass


def multiply(a, b):
    # YOUR CODE HERE
    pass


class TestExercise1_Calculator(unittest.TestCase):
    """Tests for add() and multiply(). Don't modify these!"""

    def test_add_two_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)

    def test_add_floats(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)

    def test_multiply_two_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(5, 0), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-2, 3), -6)

    def test_multiply_two_negatives(self):
        self.assertEqual(multiply(-2, -3), 6)


# =============================================================================
# Exercise 2: String Reverser
#
# Make the tests pass by implementing reverse_string().
# It should reverse the characters in a string.
#
# =============================================================================

def reverse_string(s):
    # YOUR CODE HERE
    pass


class TestExercise2_StringReverser(unittest.TestCase):
    """Tests for reverse_string(). Don't modify these!"""

    def test_reverse_simple_word(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_reverse_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_reverse_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_reverse_palindrome(self):
        self.assertEqual(reverse_string("racecar"), "racecar")

    def test_reverse_with_spaces(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_reverse_with_numbers(self):
        self.assertEqual(reverse_string("abc123"), "321cba")


# =============================================================================
# Exercise 3: FizzBuzz
#
# Make the tests pass by implementing fizzbuzz().
# Rules:
#   - Multiples of 3 -> "Fizz"
#   - Multiples of 5 -> "Buzz"
#   - Multiples of both 3 and 5 -> "FizzBuzz"
#   - Everything else -> the number as a string
#
# =============================================================================

def fizzbuzz(n):
    # YOUR CODE HERE
    pass


class TestExercise3_FizzBuzz(unittest.TestCase):
    """Tests for fizzbuzz(). Don't modify these!"""

    def test_regular_number(self):
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(2), "2")

    def test_fizz_for_multiples_of_3(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(6), "Fizz")
        self.assertEqual(fizzbuzz(9), "Fizz")

    def test_buzz_for_multiples_of_5(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")
        self.assertEqual(fizzbuzz(20), "Buzz")

    def test_fizzbuzz_for_multiples_of_15(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")
        self.assertEqual(fizzbuzz(45), "FizzBuzz")

    def test_large_number(self):
        self.assertEqual(fizzbuzz(97), "97")

    def test_large_fizzbuzz(self):
        self.assertEqual(fizzbuzz(300), "FizzBuzz")


# =============================================================================
# Exercise 4: Password Strength Checker
#
# Make the tests pass by implementing check_password().
# It should return a string: "weak", "medium", or "strong".
#
# Rules:
#   - "weak" if shorter than 8 characters
#   - "medium" if 8+ characters but missing uppercase, lowercase, or digit
#   - "strong" if 8+ characters AND has uppercase AND lowercase AND digit
#
# =============================================================================

def check_password(password):
    # YOUR CODE HERE
    pass


class TestExercise4_PasswordChecker(unittest.TestCase):
    """Tests for check_password(). Don't modify these!"""

    def test_short_password_is_weak(self):
        self.assertEqual(check_password("abc"), "weak")

    def test_seven_chars_is_still_weak(self):
        self.assertEqual(check_password("Abcde1!"), "weak")

    def test_long_but_only_lowercase_is_medium(self):
        self.assertEqual(check_password("abcdefgh"), "medium")

    def test_long_but_no_digit_is_medium(self):
        self.assertEqual(check_password("Abcdefgh"), "medium")

    def test_long_but_no_uppercase_is_medium(self):
        self.assertEqual(check_password("abcdefg1"), "medium")

    def test_long_but_no_lowercase_is_medium(self):
        self.assertEqual(check_password("ABCDEFG1"), "medium")

    def test_strong_password(self):
        self.assertEqual(check_password("Abcdefg1"), "strong")

    def test_another_strong_password(self):
        self.assertEqual(check_password("MyP4ssword"), "strong")

    def test_empty_password_is_weak(self):
        self.assertEqual(check_password(""), "weak")


# =============================================================================
# Exercise 5: Roman Numeral Converter (Subset)
#
# Make the tests pass by implementing to_roman().
# Convert an integer (1-50) to a Roman numeral string.
#
# Quick reference:
#   1=I, 4=IV, 5=V, 9=IX, 10=X, 40=XL, 50=L
#
# You only need to handle 1 through 50.
#
# =============================================================================

def to_roman(number):
    # YOUR CODE HERE
    pass


class TestExercise5_RomanNumerals(unittest.TestCase):
    """Tests for to_roman(). Don't modify these!"""

    def test_one(self):
        self.assertEqual(to_roman(1), "I")

    def test_three(self):
        self.assertEqual(to_roman(3), "III")

    def test_four(self):
        self.assertEqual(to_roman(4), "IV")

    def test_five(self):
        self.assertEqual(to_roman(5), "V")

    def test_nine(self):
        self.assertEqual(to_roman(9), "IX")

    def test_ten(self):
        self.assertEqual(to_roman(10), "X")

    def test_fourteen(self):
        self.assertEqual(to_roman(14), "XIV")

    def test_twenty_seven(self):
        self.assertEqual(to_roman(27), "XXVII")

    def test_forty(self):
        self.assertEqual(to_roman(40), "XL")

    def test_forty_four(self):
        self.assertEqual(to_roman(44), "XLIV")

    def test_fifty(self):
        self.assertEqual(to_roman(50), "L")


# =============================================================================
# Exercise 6: Markdown Bold/Italic Parser
#
# Make the tests pass by implementing parse_markdown().
# It should convert simple Markdown formatting to HTML:
#   - **text** -> <b>text</b>           (bold)
#   - *text*   -> <i>text</i>           (italic)
#   - Regular text passes through unchanged
#
# Hint: Bold (**) must be processed before italic (*), otherwise
# ** gets matched as two separate * patterns.
#
# =============================================================================

def parse_markdown(text):
    # YOUR CODE HERE
    pass


class TestExercise6_MarkdownParser(unittest.TestCase):
    """Tests for parse_markdown(). Don't modify these!"""

    def test_plain_text_unchanged(self):
        self.assertEqual(parse_markdown("hello world"), "hello world")

    def test_bold_text(self):
        self.assertEqual(parse_markdown("**bold**"), "<b>bold</b>")

    def test_italic_text(self):
        self.assertEqual(parse_markdown("*italic*"), "<i>italic</i>")

    def test_bold_in_sentence(self):
        self.assertEqual(
            parse_markdown("this is **important** stuff"),
            "this is <b>important</b> stuff"
        )

    def test_italic_in_sentence(self):
        self.assertEqual(
            parse_markdown("this is *emphasized* text"),
            "this is <i>emphasized</i> text"
        )

    def test_bold_and_italic_together(self):
        self.assertEqual(
            parse_markdown("**bold** and *italic*"),
            "<b>bold</b> and <i>italic</i>"
        )

    def test_empty_string(self):
        self.assertEqual(parse_markdown(""), "")

    def test_no_formatting(self):
        self.assertEqual(
            parse_markdown("just some plain text"),
            "just some plain text"
        )

    def test_multiple_bold(self):
        self.assertEqual(
            parse_markdown("**one** and **two**"),
            "<b>one</b> and <b>two</b>"
        )


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_add(a, b):
    return a + b


def solution_multiply(a, b):
    return a * b


def solution_reverse_string(s):
    return s[::-1]


def solution_fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def solution_check_password(password):
    if len(password) < 8:
        return "weak"
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    if has_upper and has_lower and has_digit:
        return "strong"
    return "medium"


def solution_to_roman(number):
    values = [
        (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
        (5, "V"), (4, "IV"), (1, "I"),
    ]
    result = ""
    for value, numeral in values:
        while number >= value:
            result += numeral
            number -= value
    return result


def solution_parse_markdown(text):
    # Bold first (**), then italic (*)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    return text


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("TDD Exercises: Make the Tests Pass!")
    print("=" * 60)
    print()
    print("Each exercise has tests already written. Your job is to")
    print("implement the stub functions so the tests go from RED to GREEN.")
    print()
    print("Failures are EXPECTED until you write your implementations.")
    print("That's the whole point of TDD — you start with failing tests!")
    print()
    print("-" * 60)

    # Run all the tests
    unittest.main(verbosity=2)
