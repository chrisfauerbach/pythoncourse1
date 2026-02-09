"""
Visualization — Exercises
==========================

Practice problems to test your understanding of matplotlib.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py

NOTE: Requires matplotlib. Install it with: pip install matplotlib

All plots are saved to temporary files and cleaned up automatically,
so you won't end up with stray image files lying around.
"""

import os
import math
import random

# Track temp files for cleanup
_temp_files = []

try:
    import matplotlib
    matplotlib.use("Agg")  # Non-GUI backend — saves to files, no windows
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("=" * 60)
    print("matplotlib is not installed!")
    print("Install it with:  pip install matplotlib")
    print("=" * 60)


def save_and_cleanup(filename):
    """Helper: save figure, close it, and track for cleanup."""
    plt.savefig(filename, dpi=100, bbox_inches="tight")
    plt.close()
    _temp_files.append(filename)
    print(f"  Saved: {filename}")


# =============================================================================
# Exercise 1: Weekly temperature line plot
#
# Create a line plot showing daily temperatures for a week.
# Data:
#   days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#   temps = [68, 71, 74, 72, 69, 75, 80]
#
# Requirements:
#   - Blue line with circle markers
#   - Title: "Daily Temperature"
#   - X label: "Day", Y label: "Temperature (F)"
#   - Show a grid
#   - Save to "ex1_line.png"
#
# =============================================================================

def exercise_1():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Programming language bar chart
#
# Create a bar chart comparing programming language popularity.
# Data:
#   languages = ["Python", "JavaScript", "Java", "C#", "Go"]
#   users_millions = [15.7, 17.4, 12.2, 8.5, 3.7]
#
# Requirements:
#   - Use a different color for each bar
#   - Title: "Programming Language Users (Millions)"
#   - Y label: "Users (millions)"
#   - Save to "ex2_bar.png"
#
# =============================================================================

def exercise_2():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 3: Height vs weight scatter plot
#
# Create a scatter plot showing the relationship between height and weight.
# Data (generate it yourself):
#   - Use random.seed(42) for reproducibility
#   - Generate 40 random heights between 58 and 78 inches
#   - For each height, generate a weight: height * 2.3 + random noise
#     (Hint: use random.gauss(0, 8) for noise)
#
# Requirements:
#   - Green dots with black edges, semi-transparent (alpha=0.6)
#   - Title: "Height vs Weight"
#   - X label: "Height (inches)", Y label: "Weight (lbs)"
#   - Grid on
#   - Save to "ex3_scatter.png"
#
# =============================================================================

def exercise_3():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 4: Test score histogram
#
# Create a histogram of test scores.
# Data:
#   - Use random.seed(7) for reproducibility
#   - Generate 150 scores using random.gauss(72, 14)
#   - Clamp each score between 0 and 100: min(100, max(0, score))
#   - Round each score to an integer
#
# Requirements:
#   - Use 12 bins with a "skyblue" fill and black edges
#   - Add a vertical dashed red line at the mean score
#   - Title: "Test Score Distribution"
#   - X label: "Score", Y label: "Frequency"
#   - Add a legend showing the mean value
#   - Save to "ex4_histogram.png"
#
# =============================================================================

def exercise_4():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 5: Four subplots in one figure
#
# Create a 2x2 grid of subplots showing different chart types:
#
#   Top-left:     Line plot of y = sin(x) for x from 0 to 10 (use 50 points)
#   Top-right:    Bar chart — categories ["A","B","C","D"], values [25,40,15,30]
#   Bottom-left:  Scatter of 30 random points (x: 0-10, y: 0-10), seed=88
#   Bottom-right: Pie chart — slices ["Email","Social","Search","Direct"]
#                 with values [35, 30, 25, 10]
#
# Requirements:
#   - Figure size: (10, 8)
#   - Each subplot gets a title
#   - Use plt.tight_layout()
#   - Save to "ex5_subplots.png"
#
# =============================================================================

def exercise_5():
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 6: Styled multi-series line chart
#
# Create a polished chart showing quarterly revenue for three products.
# Data:
#   quarters = ["Q1", "Q2", "Q3", "Q4"]
#   product_a = [120, 145, 160, 175]
#   product_b = [90, 105, 98, 130]
#   product_c = [60, 80, 95, 110]
#
# Requirements:
#   - Use the "ggplot" style (via plt.style.context)
#   - Figure size: (10, 6)
#   - Three lines with different colors, markers, and line styles:
#       Product A: solid line, circle markers
#       Product B: dashed line, square markers
#       Product C: dotted line, triangle markers
#   - Linewidth of 2.5 for all lines
#   - Title: "Quarterly Revenue by Product" (fontsize=16, bold)
#   - X label: "Quarter", Y label: "Revenue ($k)"
#   - Legend in the upper-left corner
#   - Grid on
#   - Annotate the highest value on Product A's line with an arrow
#   - Save to "ex6_styled.png"
#
# =============================================================================

def exercise_6():
    # YOUR CODE HERE
    pass


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    temps = [68, 71, 74, 72, 69, 75, 80]

    plt.figure(figsize=(8, 5))
    plt.plot(days, temps, color="steelblue", marker="o", linewidth=2)
    plt.title("Daily Temperature")
    plt.xlabel("Day")
    plt.ylabel("Temperature (F)")
    plt.grid(True, linestyle="--", alpha=0.7)
    save_and_cleanup("ex1_line.png")


def solution_2():
    languages = ["Python", "JavaScript", "Java", "C#", "Go"]
    users_millions = [15.7, 17.4, 12.2, 8.5, 3.7]
    colors = ["#3776AB", "#F7DF1E", "#ED8B00", "#68217A", "#00ADD8"]

    plt.figure(figsize=(8, 5))
    plt.bar(languages, users_millions, color=colors, edgecolor="black", linewidth=0.5)
    plt.title("Programming Language Users (Millions)")
    plt.ylabel("Users (millions)")
    save_and_cleanup("ex2_bar.png")


def solution_3():
    random.seed(42)
    heights = [random.uniform(58, 78) for _ in range(40)]
    weights = [h * 2.3 + random.gauss(0, 8) for h in heights]

    plt.figure(figsize=(8, 5))
    plt.scatter(heights, weights, color="green", edgecolors="black", alpha=0.6, s=60)
    plt.title("Height vs Weight")
    plt.xlabel("Height (inches)")
    plt.ylabel("Weight (lbs)")
    plt.grid(True, linestyle="--", alpha=0.5)
    save_and_cleanup("ex3_scatter.png")


def solution_4():
    random.seed(7)
    scores = [min(100, max(0, round(random.gauss(72, 14)))) for _ in range(150)]
    mean_score = sum(scores) / len(scores)

    plt.figure(figsize=(8, 5))
    plt.hist(scores, bins=12, color="skyblue", edgecolor="black")
    plt.axvline(mean_score, color="red", linestyle="--", linewidth=2,
                label=f"Mean: {mean_score:.1f}")
    plt.title("Test Score Distribution")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.legend()
    save_and_cleanup("ex4_histogram.png")


def solution_5():
    fig, axes = plt.subplots(2, 2, figsize=(10, 8))

    # Top-left: sine wave
    x = [i * 0.2 for i in range(51)]
    y = [math.sin(v) for v in x]
    axes[0, 0].plot(x, y, color="steelblue", linewidth=2)
    axes[0, 0].set_title("sin(x)")

    # Top-right: bar chart
    axes[0, 1].bar(["A", "B", "C", "D"], [25, 40, 15, 30],
                   color="salmon", edgecolor="black")
    axes[0, 1].set_title("Category Values")

    # Bottom-left: scatter
    random.seed(88)
    sx = [random.uniform(0, 10) for _ in range(30)]
    sy = [random.uniform(0, 10) for _ in range(30)]
    axes[1, 0].scatter(sx, sy, color="teal", edgecolors="black", alpha=0.7)
    axes[1, 0].set_title("Random Points")

    # Bottom-right: pie
    axes[1, 1].pie([35, 30, 25, 10],
                   labels=["Email", "Social", "Search", "Direct"],
                   autopct="%1.0f%%", startangle=90)
    axes[1, 1].set_title("Traffic Sources")

    plt.tight_layout()
    save_and_cleanup("ex5_subplots.png")


def solution_6():
    quarters = ["Q1", "Q2", "Q3", "Q4"]
    product_a = [120, 145, 160, 175]
    product_b = [90, 105, 98, 130]
    product_c = [60, 80, 95, 110]

    with plt.style.context("ggplot"):
        plt.figure(figsize=(10, 6))

        plt.plot(quarters, product_a, "o-", color="steelblue",
                 label="Product A", linewidth=2.5, markersize=8)
        plt.plot(quarters, product_b, "s--", color="tomato",
                 label="Product B", linewidth=2.5, markersize=8)
        plt.plot(quarters, product_c, "^:", color="forestgreen",
                 label="Product C", linewidth=2.5, markersize=8)

        # Annotate the peak of Product A
        best_idx = product_a.index(max(product_a))
        plt.annotate(
            f"Peak: ${max(product_a)}k",
            xy=(best_idx, max(product_a)),
            xytext=(best_idx - 1, max(product_a) + 15),
            fontsize=11, fontweight="bold", color="darkblue",
            arrowprops=dict(arrowstyle="->", color="darkblue", lw=1.5)
        )

        plt.title("Quarterly Revenue by Product", fontsize=16, fontweight="bold")
        plt.xlabel("Quarter")
        plt.ylabel("Revenue ($k)")
        plt.legend(loc="upper left")
        plt.grid(True)

        save_and_cleanup("ex6_styled.png")


# =============================================================================
# Cleanup helper
# =============================================================================

def cleanup():
    """Remove all temporary plot files."""
    cleaned = 0
    for f in _temp_files:
        if os.path.exists(f):
            os.remove(f)
            cleaned += 1
    if cleaned:
        print(f"\nCleaned up {cleaned} temporary plot file(s).")


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    if not HAS_MATPLOTLIB:
        print("\nCan't run the exercises without matplotlib.")
        print("Install it with:  pip install matplotlib")
        raise SystemExit(0)

    exercises = [
        ("Weekly temperature line plot", exercise_1),
        ("Programming language bar chart", exercise_2),
        ("Height vs weight scatter plot", exercise_3),
        ("Test score histogram", exercise_4),
        ("Four subplots in one figure", exercise_5),
        ("Styled multi-series line chart", exercise_6),
    ]

    solutions = [
        ("Weekly temperature line plot", solution_1),
        ("Programming language bar chart", solution_2),
        ("Height vs weight scatter plot", solution_3),
        ("Test score histogram", solution_4),
        ("Four subplots in one figure", solution_5),
        ("Styled multi-series line chart", solution_6),
    ]

    try:
        print("=" * 50)
        print("EXERCISES (your code goes here)")
        print("=" * 50)
        for i, (title, func) in enumerate(exercises, 1):
            print(f"\nExercise {i}: {title}")
            func()

        print()
        print("=" * 50)
        print("SOLUTIONS (compare your output)")
        print("=" * 50)
        for i, (title, func) in enumerate(solutions, 1):
            print(f"\nSolution {i}: {title}")
            func()
    finally:
        cleanup()

    print()
    print("-" * 50)
    print("Done! Fill in the exercises and compare with the solutions.")
