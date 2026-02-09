"""
Visualization — Example Code
==============================

Run this file:
    python3 example.py

This file demonstrates how to create various chart types with matplotlib.
All plots are saved to temporary files and cleaned up automatically.

NOTE: Requires matplotlib. Install it with: pip install matplotlib
"""

import os
import math
import random

# We'll collect any files we create so we can clean them up at the end
_temp_files = []

try:
    import matplotlib
    matplotlib.use("Agg")  # Use non-GUI backend — saves to files instead of opening windows
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("=" * 60)
    print("matplotlib is not installed!")
    print("Install it with:  pip install matplotlib")
    print("=" * 60)


def save_and_report(filename):
    """Helper: save the current figure, report it, and track for cleanup."""
    plt.savefig(filename, dpi=100, bbox_inches="tight")
    plt.close()
    _temp_files.append(filename)
    print(f"  Saved: {filename}")


# -----------------------------------------------------------------------------
# 1. Simple line plot
# -----------------------------------------------------------------------------

def line_plot():
    print("1. Line Plot — Weekly Temperature")

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    temps = [72, 75, 71, 68, 74, 78, 82]

    plt.figure(figsize=(8, 5))
    plt.plot(days, temps, marker="o", color="steelblue", linewidth=2)
    plt.title("Temperature This Week")
    plt.xlabel("Day")
    plt.ylabel("Temperature (F)")
    plt.grid(True, linestyle="--", alpha=0.7)

    save_and_report("example_line_plot.png")


# -----------------------------------------------------------------------------
# 2. Multi-line plot with legend
# -----------------------------------------------------------------------------

def multi_line_plot():
    print("2. Multi-Line Plot — Two Cities")

    days = list(range(1, 8))
    city_a = [72, 75, 71, 68, 74, 78, 82]
    city_b = [65, 63, 67, 70, 72, 68, 64]

    plt.figure(figsize=(8, 5))
    plt.plot(days, city_a, marker="o", label="Phoenix", color="tomato", linewidth=2)
    plt.plot(days, city_b, marker="s", label="Seattle", color="dodgerblue", linewidth=2)
    plt.title("Weekly Temperature Comparison")
    plt.xlabel("Day of Week")
    plt.ylabel("Temperature (F)")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.7)

    save_and_report("example_multi_line.png")


# -----------------------------------------------------------------------------
# 3. Bar chart
# -----------------------------------------------------------------------------

def bar_chart():
    print("3. Bar Chart — Programming Language Popularity")

    languages = ["Python", "JavaScript", "Java", "C++", "Go", "Rust"]
    popularity = [30, 25, 18, 12, 8, 7]
    colors = ["#3776AB", "#F7DF1E", "#ED8B00", "#00599C", "#00ADD8", "#DEA584"]

    plt.figure(figsize=(8, 5))
    plt.bar(languages, popularity, color=colors, edgecolor="black", linewidth=0.5)
    plt.title("Programming Language Popularity")
    plt.xlabel("Language")
    plt.ylabel("Popularity (%)")

    save_and_report("example_bar_chart.png")


# -----------------------------------------------------------------------------
# 4. Horizontal bar chart
# -----------------------------------------------------------------------------

def horizontal_bar_chart():
    print("4. Horizontal Bar Chart — Fruit Sales")

    fruits = ["Strawberries", "Blueberries", "Raspberries", "Blackberries", "Cherries"]
    sales = [85, 72, 58, 43, 91]

    plt.figure(figsize=(8, 5))
    plt.barh(fruits, sales, color="mediumseagreen", edgecolor="black", linewidth=0.5)
    plt.title("Weekly Fruit Sales")
    plt.xlabel("Units Sold")

    save_and_report("example_barh_chart.png")


# -----------------------------------------------------------------------------
# 5. Scatter plot
# -----------------------------------------------------------------------------

def scatter_plot():
    print("5. Scatter Plot — Height vs Weight")

    # Generate some correlated data using plain Python
    random.seed(42)
    heights = [random.gauss(68, 4) for _ in range(50)]
    weights = [h * 2.5 + random.gauss(0, 10) for h in heights]

    plt.figure(figsize=(8, 5))
    plt.scatter(heights, weights, color="coral", edgecolors="black", alpha=0.7, s=60)
    plt.title("Height vs Weight")
    plt.xlabel("Height (inches)")
    plt.ylabel("Weight (lbs)")
    plt.grid(True, linestyle="--", alpha=0.5)

    save_and_report("example_scatter.png")


# -----------------------------------------------------------------------------
# 6. Histogram
# -----------------------------------------------------------------------------

def histogram():
    print("6. Histogram — Test Score Distribution")

    random.seed(123)
    scores = [min(100, max(0, int(random.gauss(75, 12)))) for _ in range(200)]

    plt.figure(figsize=(8, 5))
    plt.hist(scores, bins=15, color="mediumpurple", edgecolor="black", alpha=0.8)
    plt.title("Test Score Distribution (200 Students)")
    plt.xlabel("Score")
    plt.ylabel("Number of Students")
    plt.axvline(sum(scores) / len(scores), color="red", linestyle="--",
                label=f"Mean: {sum(scores) / len(scores):.1f}")
    plt.legend()

    save_and_report("example_histogram.png")


# -----------------------------------------------------------------------------
# 7. Pie chart
# -----------------------------------------------------------------------------

def pie_chart():
    print("7. Pie Chart — How I Spend My Day")

    activities = ["Sleep", "Work", "Commute", "Leisure", "Eating", "Exercise"]
    hours = [8, 9, 1.5, 3, 1.5, 1]
    colors = ["#4E79A7", "#F28E2B", "#E15759", "#76B7B2", "#59A14F", "#EDC948"]
    explode = [0, 0.05, 0, 0, 0, 0]  # Slightly pull out "Work"

    plt.figure(figsize=(8, 6))
    plt.pie(hours, labels=activities, autopct="%1.0f%%", startangle=90,
            colors=colors, explode=explode, shadow=True)
    plt.title("How I Spend My Day")

    save_and_report("example_pie.png")


# -----------------------------------------------------------------------------
# 8. Subplots — four charts in one figure
# -----------------------------------------------------------------------------

def subplots_demo():
    print("8. Subplots — Four Charts in One Figure")

    fig, axes = plt.subplots(2, 2, figsize=(12, 9))

    # Top-left: Line plot
    x = list(range(1, 11))
    y = [v ** 2 for v in x]
    axes[0, 0].plot(x, y, "bo-", linewidth=2)
    axes[0, 0].set_title("Squares")
    axes[0, 0].set_xlabel("x")
    axes[0, 0].set_ylabel("x squared")
    axes[0, 0].grid(True, linestyle="--", alpha=0.5)

    # Top-right: Bar chart
    categories = ["A", "B", "C", "D", "E"]
    values = [23, 45, 12, 67, 34]
    axes[0, 1].bar(categories, values, color="salmon", edgecolor="black")
    axes[0, 1].set_title("Category Scores")

    # Bottom-left: Scatter plot
    random.seed(99)
    sx = [random.random() * 10 for _ in range(30)]
    sy = [v + random.gauss(0, 2) for v in sx]
    axes[1, 0].scatter(sx, sy, color="teal", alpha=0.7, edgecolors="black")
    axes[1, 0].set_title("Random Scatter")
    axes[1, 0].set_xlabel("x")
    axes[1, 0].set_ylabel("y")

    # Bottom-right: Histogram
    random.seed(55)
    data = [random.gauss(50, 15) for _ in range(300)]
    axes[1, 1].hist(data, bins=20, color="goldenrod", edgecolor="black")
    axes[1, 1].set_title("Normal Distribution")
    axes[1, 1].set_xlabel("Value")

    plt.tight_layout()
    save_and_report("example_subplots.png")


# -----------------------------------------------------------------------------
# 9. Customized plot with annotations
# -----------------------------------------------------------------------------

def customized_plot():
    print("9. Customized Plot — Monthly Sales with Annotations")

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sales = [120, 135, 148, 162, 155, 170, 195, 210, 185, 175, 190, 230]

    plt.figure(figsize=(10, 6))
    plt.plot(months, sales, marker="o", color="darkblue", linewidth=2.5,
             markersize=8, markerfacecolor="gold", markeredgecolor="darkblue")

    # Highlight the best month
    best_idx = sales.index(max(sales))
    plt.annotate(
        f"Best: ${max(sales)}k",
        xy=(best_idx, max(sales)),
        xytext=(best_idx - 2, max(sales) + 15),
        fontsize=11, fontweight="bold", color="darkred",
        arrowprops=dict(arrowstyle="->", color="darkred", lw=1.5)
    )

    plt.title("Monthly Sales Performance", fontsize=16, fontweight="bold")
    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Sales ($k)", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.ylim(100, 260)

    save_and_report("example_customized.png")


# -----------------------------------------------------------------------------
# 10. Using a built-in style
# -----------------------------------------------------------------------------

def styled_plot():
    print("10. Styled Plot — Using a Built-in Theme")

    # Show available styles
    print(f"  Available styles: {plt.style.available[:5]}... ({len(plt.style.available)} total)")

    x = list(range(1, 13))
    y1 = [math.sin(v * 0.5) * 10 + 50 for v in x]
    y2 = [math.cos(v * 0.5) * 10 + 50 for v in x]

    # Use a style temporarily with context manager
    with plt.style.context("ggplot"):
        plt.figure(figsize=(8, 5))
        plt.plot(x, y1, "o-", label="Series A", linewidth=2)
        plt.plot(x, y2, "s--", label="Series B", linewidth=2)
        plt.title("ggplot Style Demo")
        plt.xlabel("Month")
        plt.ylabel("Value")
        plt.legend()
        save_and_report("example_styled.png")


# -----------------------------------------------------------------------------
# Cleanup helper
# -----------------------------------------------------------------------------

def cleanup():
    """Remove all temporary plot files we created."""
    cleaned = 0
    for f in _temp_files:
        if os.path.exists(f):
            os.remove(f)
            cleaned += 1
    if cleaned:
        print(f"\nCleaned up {cleaned} temporary plot file(s).")


# -----------------------------------------------------------------------------
# Run it!
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    if not HAS_MATPLOTLIB:
        print("\nCan't run the examples without matplotlib.")
        print("Install it with:  pip install matplotlib")
        raise SystemExit(0)

    print("=" * 60)
    print("  MATPLOTLIB VISUALIZATION EXAMPLES")
    print("=" * 60)
    print()

    try:
        line_plot()
        print()
        multi_line_plot()
        print()
        bar_chart()
        print()
        horizontal_bar_chart()
        print()
        scatter_plot()
        print()
        histogram()
        print()
        pie_chart()
        print()
        subplots_demo()
        print()
        customized_plot()
        print()
        styled_plot()
    finally:
        # Always clean up, even if something fails
        cleanup()

    print()
    print("=" * 60)
    print("  All done! Every chart type was saved and cleaned up.")
    print("  Try modifying the code above and running it again!")
    print("=" * 60)
