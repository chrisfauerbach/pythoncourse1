"""
Hello World — Example Code
============================

Run this file:
    python3 example.py

Your very first Python program! This file demonstrates the print() function
and all the different ways you can use it.
"""

# -----------------------------------------------------------------------------
# 1. The basics — just print something!
# -----------------------------------------------------------------------------

print("Hello, World!")
print('Hello, World!')  # Single quotes work exactly the same way

# -----------------------------------------------------------------------------
# 2. Printing multiple items
# -----------------------------------------------------------------------------

# Separate items with commas — Python adds spaces automatically
print("My", "name", "is", "Python")

# You can mix strings and numbers
print("Python version:", 3)
print("Pi is approximately", 3.14159)

# -----------------------------------------------------------------------------
# 3. Comments — notes for humans, ignored by Python
# -----------------------------------------------------------------------------

# This entire line is a comment — Python skips it
print("This line runs")  # This comment is at the end of a line

# Use comments to explain WHY, not WHAT:
# Bad:  # print the greeting
# Good: # Greet the user so they know the program started successfully
print("Welcome to the program!")

# -----------------------------------------------------------------------------
# 4. Special characters in strings
# -----------------------------------------------------------------------------

# Newline (\n) — start a new line inside a string
print("Line 1\nLine 2\nLine 3")

# Tab (\t) — add a tab for alignment
print("Name:\tAlice")
print("Age:\t30")

# Backslash (\\) — print a literal backslash
print("File path: C:\\Users\\Alice")

# Quotes inside strings — a few options:
print('She said "hello!"')          # Single outside, double inside
print("It's a beautiful day")       # Double outside, single inside
print("She said \"hello!\"")        # Escape with backslash

# -----------------------------------------------------------------------------
# 5. print() formatting tricks
# -----------------------------------------------------------------------------

# sep: change what goes between items (default is a space)
print("2025", "02", "09", sep="-")       # Output: 2025-02-09
print("alice", "example.com", sep="@")   # Output: alice@example.com
print("usr", "local", "bin", sep="/")    # Output: usr/local/bin

# end: change what goes at the end (default is a newline)
print("Loading", end="... ")
print("Done!")  # These two prints appear on the same line

# Combining sep and end
print("A", "B", "C", sep=" -> ", end=" [COMPLETE]\n")

# Print a blank line
print()

# -----------------------------------------------------------------------------
# 6. Multi-line strings (a preview — we'll cover these more later)
# -----------------------------------------------------------------------------

# Triple quotes let you write strings across multiple lines
print("""
  Welcome to Learn Python!
  ========================
  This is a multi-line string.
  It preserves line breaks and spacing.
""")

# -----------------------------------------------------------------------------
# 7. Putting it all together
# -----------------------------------------------------------------------------

print("=" * 40)            # Repeat a string with *
print("   HELLO WORLD COMPLETE!")
print("=" * 40)
print()
print("You just ran your first Python file.")
print("Try changing some of the print statements above and run it again!")
