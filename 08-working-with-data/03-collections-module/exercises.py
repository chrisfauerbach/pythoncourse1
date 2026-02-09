"""
The Collections Module — Exercises
====================================

Practice problems to test your understanding of the collections module.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py
"""

from collections import Counter, defaultdict, namedtuple, deque, ChainMap


# =============================================================================
# Exercise 1: Word frequency counter
#
# Given the paragraph below, use Counter to:
#   1. Count how many times each word appears (lowercase everything first)
#   2. Print the 5 most common words and their counts
#   3. Print the total number of unique words
#
# Expected output format:
#   Top 5 words:
#     'the': 4
#     'python': 3
#     ...
#   Unique words: 25
#
# Hint: Use .split() to get words and .lower() to normalize case
# =============================================================================

def exercise_1():
    paragraph = (
        "Python is a great programming language and Python is easy to learn "
        "The Python community is welcoming and the documentation is excellent "
        "Many developers choose Python because the syntax is clean and the "
        "libraries are powerful"
    )
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Group words by first letter
#
# Given the list of words below, use defaultdict to group them by their
# first letter (lowercase). Print each letter and its words sorted
# alphabetically.
#
# Expected output format:
#   a: ['algorithm', 'apple', 'avocado']
#   b: ['banana', 'binary', 'boolean']
#   ...
#
# Hint: defaultdict(list) is your friend here
# =============================================================================

def exercise_2():
    words = [
        "apple", "banana", "algorithm", "binary", "cherry", "compile",
        "data", "avocado", "boolean", "debug", "cache", "deploy",
        "abstract", "buffer", "dict", "class",
    ]
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: RGB color with hex conversion
#
# Create a namedtuple called 'RGB' with fields 'red', 'green', 'blue'.
# Then write a function rgb_to_hex(color) that takes an RGB namedtuple
# and returns the hex string like '#FF00FF'.
#
# Create these colors and print each with its hex value:
#   - white  = RGB(255, 255, 255)  ->  #FFFFFF
#   - black  = RGB(0, 0, 0)        ->  #000000
#   - coral  = RGB(255, 127, 80)   ->  #FF7F50
#
# Then use _replace() to create 'dark_coral' by setting red to 200,
# and print its hex value too.
#
# Hint: Use f"{value:02X}" to format a number as 2-digit uppercase hex
# =============================================================================

def exercise_3():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: Sliding window average
#
# Given a list of temperature readings, compute the sliding window average
# using a deque with maxlen.
#
# Use a window size of 4. For each reading, print:
#   - The current reading
#   - The contents of the window
#   - The average of the values in the window
#
# Expected output format:
#   Reading: 72 | Window: [72]           | Avg: 72.0
#   Reading: 75 | Window: [72, 75]       | Avg: 73.5
#   Reading: 71 | Window: [72, 75, 71]   | Avg: 72.7
#   Reading: 78 | Window: [72, 75, 71, 78] | Avg: 74.0
#   Reading: 73 | Window: [75, 71, 78, 73] | Avg: 74.2  <- 72 dropped!
#   ...
# =============================================================================

def exercise_4():
    temperatures = [72, 75, 71, 78, 73, 80, 69, 74, 77, 82]
    window_size = 4
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Recent history buffer
#
# Simulate a browser's "recently visited" feature using a deque with maxlen=5.
#
# Process the list of page visits below. After each visit, print the
# current history. The buffer should only keep the 5 most recent pages.
#
# After processing all visits, print the history in reverse order
# (most recent first) — that's how a user would expect to see it.
#
# Expected output format:
#   Visit 'home'     -> History: ['home']
#   Visit 'about'    -> History: ['home', 'about']
#   ...
#
#   Recently visited (newest first):
#     1. pricing
#     2. signup
#     ...
# =============================================================================

def exercise_5():
    page_visits = [
        "home", "about", "products", "blog", "contact",
        "pricing", "signup", "docs",
    ]
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: Layered configuration with ChainMap
#
# Build a layered config system using ChainMap with three layers:
#
#   defaults (lowest priority):
#       host=localhost, port=8080, debug=False, log_level=WARNING, workers=4
#
#   user_config (medium priority):
#       port=3000, log_level=INFO
#
#   env_vars (highest priority):
#       debug=True
#
# Create the ChainMap so that env_vars overrides user_config, which
# overrides defaults.
#
# Print all 5 config values and show which layer each one comes from.
#
# Then add a "runtime" layer on top using new_child() that sets workers=1,
# and print the updated workers value.
#
# Expected output format:
#   host:      localhost (from defaults)
#   port:      3000 (from user_config)
#   debug:     True (from env_vars)
#   log_level: INFO (from user_config)
#   workers:   4 (from defaults)
#
#   After runtime override:
#   workers:   1 (from runtime)
#
# Hint: To figure out which layer a key comes from, loop through
#       config.maps and check if the key is in each dict
# =============================================================================

def exercise_6():
    # YOUR CODE HERE
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    paragraph = (
        "Python is a great programming language and Python is easy to learn "
        "The Python community is welcoming and the documentation is excellent "
        "Many developers choose Python because the syntax is clean and the "
        "libraries are powerful"
    )
    words = paragraph.lower().split()
    word_counts = Counter(words)

    print("Top 5 words:")
    for word, count in word_counts.most_common(5):
        print(f"  '{word}': {count}")
    print(f"Unique words: {len(word_counts)}")


def solution_2():
    words = [
        "apple", "banana", "algorithm", "binary", "cherry", "compile",
        "data", "avocado", "boolean", "debug", "cache", "deploy",
        "abstract", "buffer", "dict", "class",
    ]
    grouped = defaultdict(list)
    for word in words:
        grouped[word[0].lower()].append(word)

    for letter in sorted(grouped):
        print(f"  {letter}: {sorted(grouped[letter])}")


def solution_3():
    RGB = namedtuple("RGB", ["red", "green", "blue"])

    def rgb_to_hex(color):
        return f"#{color.red:02X}{color.green:02X}{color.blue:02X}"

    white = RGB(255, 255, 255)
    black = RGB(0, 0, 0)
    coral = RGB(255, 127, 80)

    print(f"  white: {white} -> {rgb_to_hex(white)}")
    print(f"  black: {black} -> {rgb_to_hex(black)}")
    print(f"  coral: {coral} -> {rgb_to_hex(coral)}")

    dark_coral = coral._replace(red=200)
    print(f"  dark_coral: {dark_coral} -> {rgb_to_hex(dark_coral)}")


def solution_4():
    temperatures = [72, 75, 71, 78, 73, 80, 69, 74, 77, 82]
    window_size = 4
    window = deque(maxlen=window_size)

    for temp in temperatures:
        window.append(temp)
        avg = sum(window) / len(window)
        print(f"  Reading: {temp} | Window: {str(list(window)):>20s} | Avg: {avg:.1f}")


def solution_5():
    page_visits = [
        "home", "about", "products", "blog", "contact",
        "pricing", "signup", "docs",
    ]
    history = deque(maxlen=5)

    for page in page_visits:
        history.append(page)
        print(f"  Visit '{page}'{' ' * (10 - len(page))}-> History: {list(history)}")

    print("\n  Recently visited (newest first):")
    for i, page in enumerate(reversed(history), 1):
        print(f"    {i}. {page}")


def solution_6():
    defaults = {
        "host": "localhost",
        "port": 8080,
        "debug": False,
        "log_level": "WARNING",
        "workers": 4,
    }
    user_config = {
        "port": 3000,
        "log_level": "INFO",
    }
    env_vars = {
        "debug": True,
    }

    config = ChainMap(env_vars, user_config, defaults)

    # Map names for display purposes
    layer_names = ["env_vars", "user_config", "defaults"]

    def find_source(key):
        for layer, name in zip(config.maps, layer_names):
            if key in layer:
                return name
        return "unknown"

    for key in ["host", "port", "debug", "log_level", "workers"]:
        source = find_source(key)
        print(f"  {key + ':':12s} {str(config[key]):>10s} (from {source})")

    # Add a runtime layer on top
    runtime = config.new_child({"workers": 1})
    print(f"\n  After runtime override:")
    print(f"  {'workers:':12s} {str(runtime['workers']):>10s} (from runtime)")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Word frequency counter", exercise_1),
        ("Group words by first letter", exercise_2),
        ("RGB color with hex conversion", exercise_3),
        ("Sliding window average", exercise_4),
        ("Recent history buffer", exercise_5),
        ("Layered config with ChainMap", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
