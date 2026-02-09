# Visualization with Matplotlib

## Objective

Learn how to turn data into charts and graphs using matplotlib, Python's most popular plotting library. You'll create line plots, bar charts, scatter plots, histograms, pie charts, and more.

## Concepts Covered

- What matplotlib is and why visualization matters
- The `pyplot` interface
- Line plots, bar charts, scatter plots, histograms, and pie charts
- Customizing plots with titles, labels, legends, colors, and styles
- Creating multiple subplots in one figure
- Saving figures to files
- Built-in themes with `plt.style.use()`
- Brief overview of alternative libraries (seaborn, plotly)

## Prerequisites

- Basic Python (lists, loops, functions)
- Familiarity with data concepts (the earlier lessons in this section help, but aren't strictly required)
- matplotlib installed (`pip install matplotlib`)

## Lesson

### Why Visualization Matters

Numbers in a list are hard to interpret. A chart tells the story instantly. Visualization helps you:

- **Spot patterns** — trends, clusters, outliers jump out visually
- **Communicate findings** — a chart is worth a thousand rows of data
- **Debug your data** — weird data shows up fast when you plot it
- **Explore before analyzing** — always plot your data before running fancy statistics

### What is Matplotlib?

Matplotlib is Python's foundational plotting library. It's been around since 2003 and virtually every other Python visualization tool builds on top of it. It can produce publication-quality charts in a wide variety of formats.

To install it:

```bash
pip install matplotlib
```

### The pyplot Interface

Matplotlib has a lot of layers, but you'll almost always use the `pyplot` interface. By convention, everyone imports it as `plt`:

```python
import matplotlib.pyplot as plt
```

The basic workflow is always the same:

1. Create some data
2. Call a plotting function (`plt.plot()`, `plt.bar()`, etc.)
3. Customize it (titles, labels, colors)
4. Show it (`plt.show()`) or save it (`plt.savefig()`)

### Line Plots: `plt.plot()`

The most basic chart. Great for showing trends over time:

```python
days = [1, 2, 3, 4, 5, 6, 7]
temperatures = [72, 75, 71, 68, 74, 78, 82]

plt.plot(days, temperatures)
plt.title("Weekly Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature (F)")
plt.savefig("line_plot.png")
plt.close()
```

You can plot multiple lines on the same chart:

```python
plt.plot(days, city_a_temps, label="City A")
plt.plot(days, city_b_temps, label="City B")
plt.legend()  # Shows which line is which
```

### Bar Charts: `plt.bar()` and `plt.barh()`

Perfect for comparing categories:

```python
languages = ["Python", "JavaScript", "Java", "C++"]
popularity = [30, 25, 20, 15]

plt.bar(languages, popularity)
plt.title("Language Popularity")
plt.ylabel("Popularity (%)")
plt.savefig("bar_chart.png")
plt.close()
```

Use `plt.barh()` for horizontal bars — handy when your category labels are long:

```python
plt.barh(languages, popularity)
```

### Scatter Plots: `plt.scatter()`

Shows the relationship between two variables. Each point is one observation:

```python
heights = [62, 65, 68, 70, 72, 74, 67, 71]
weights = [130, 150, 165, 180, 190, 200, 155, 175]

plt.scatter(heights, weights)
plt.title("Height vs Weight")
plt.xlabel("Height (inches)")
plt.ylabel("Weight (lbs)")
plt.savefig("scatter_plot.png")
plt.close()
```

You can control the size and color of each point with the `s` and `c` parameters:

```python
plt.scatter(heights, weights, s=100, c="coral", alpha=0.7)
```

### Histograms: `plt.hist()`

Shows the distribution of a single variable — how often values fall into different ranges (bins):

```python
scores = [88, 92, 78, 95, 67, 82, 90, 85, 73, 91, 88, 76, 94, 81, 87]

plt.hist(scores, bins=5, edgecolor="black")
plt.title("Test Score Distribution")
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.savefig("histogram.png")
plt.close()
```

The `bins` parameter controls how many bars you get. More bins = more detail.

### Pie Charts: `plt.pie()`

Shows parts of a whole. Use sparingly — bar charts are usually easier to read, but pie charts work well for simple breakdowns:

```python
activities = ["Sleep", "Work", "Commute", "Leisure", "Eating"]
hours = [8, 9, 1.5, 4, 1.5]

plt.pie(hours, labels=activities, autopct="%1.0f%%", startangle=90)
plt.title("How I Spend My Day")
plt.savefig("pie_chart.png")
plt.close()
```

- `autopct` adds percentage labels to each slice
- `startangle` rotates the starting position

### Customizing Your Plots

Matplotlib gives you control over almost everything. Here are the most common tweaks:

```python
# Colors — use names, hex codes, or RGB tuples
plt.plot(x, y, color="coral")
plt.plot(x, y, color="#FF6347")
plt.plot(x, y, color=(0.2, 0.4, 0.6))

# Line styles
plt.plot(x, y, linestyle="--")    # Dashed
plt.plot(x, y, linestyle=":")     # Dotted
plt.plot(x, y, linestyle="-.")    # Dash-dot

# Markers — highlight data points
plt.plot(x, y, marker="o")       # Circles
plt.plot(x, y, marker="s")       # Squares
plt.plot(x, y, marker="^")       # Triangles

# Shorthand — combine color, marker, and line in one string
plt.plot(x, y, "ro--")  # Red circles with dashed line

# Titles and labels
plt.title("My Chart", fontsize=16, fontweight="bold")
plt.xlabel("X Axis", fontsize=12)
plt.ylabel("Y Axis", fontsize=12)

# Grid
plt.grid(True, linestyle="--", alpha=0.7)

# Annotations — point out something specific
plt.annotate("Peak!", xy=(5, 95), fontsize=12,
             arrowprops=dict(arrowstyle="->"))
```

### Subplots: Multiple Plots in One Figure

When you want to compare several charts side by side, use `plt.subplots()`:

```python
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# axes is a 2x2 array — access each subplot by row and column
axes[0, 0].plot(x, y)
axes[0, 0].set_title("Line Plot")

axes[0, 1].bar(categories, values)
axes[0, 1].set_title("Bar Chart")

axes[1, 0].scatter(x, y)
axes[1, 0].set_title("Scatter Plot")

axes[1, 1].hist(data, bins=10)
axes[1, 1].set_title("Histogram")

plt.tight_layout()  # Prevents overlap
plt.savefig("subplots.png")
plt.close()
```

Notice that with subplots, you call methods on the `axes` objects (like `axes[0, 0].set_title()`) instead of on `plt` directly. This trips people up at first — just remember: `plt` controls the whole figure, `axes` control individual subplots.

### Saving Figures: `plt.savefig()`

You can save to PNG, PDF, SVG, and more. The format is determined by the file extension:

```python
plt.savefig("chart.png")              # PNG (raster, good for web)
plt.savefig("chart.pdf")              # PDF (vector, good for papers)
plt.savefig("chart.svg")              # SVG (vector, good for web)
plt.savefig("chart.png", dpi=300)     # Higher resolution
plt.savefig("chart.png", bbox_inches="tight")  # Trim whitespace
```

Always call `plt.savefig()` **before** `plt.show()` or `plt.close()` — those functions clear the figure.

### Built-in Themes: `plt.style.use()`

Matplotlib comes with several built-in themes that change the overall look of your plots:

```python
plt.style.use("ggplot")           # R-inspired style
plt.style.use("seaborn-v0_8")    # Clean and modern
plt.style.use("dark_background")  # Dark mode
plt.style.use("fivethirtyeight")  # News-style charts
```

You can list all available styles with:

```python
print(plt.style.available)
```

To temporarily use a style without changing your default:

```python
with plt.style.context("ggplot"):
    plt.plot(x, y)
    plt.savefig("styled.png")
```

### Alternative Libraries Worth Knowing

Matplotlib is the foundation, but there are libraries that build on it or take a different approach:

- **seaborn** — Built on top of matplotlib. Makes statistical charts (heatmaps, violin plots, pair plots) much easier. Great default styles. Install with `pip install seaborn`.

- **plotly** — Creates interactive charts that you can zoom, pan, and hover over. Runs in the browser. Great for dashboards and presentations. Install with `pip install plotly`.

- **pandas built-in plotting** — If you have a DataFrame, you can call `df.plot()` directly. It uses matplotlib under the hood but saves you some typing.

You don't need to learn these right now — matplotlib is the essential one. But when you find yourself writing a lot of boilerplate for a specific chart type, check if seaborn or plotly makes it easier.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- matplotlib is Python's most popular plotting library — `import matplotlib.pyplot as plt`
- The workflow is always: create data, plot it, customize it, save/show it
- `plt.plot()`, `plt.bar()`, `plt.scatter()`, `plt.hist()`, and `plt.pie()` cover most chart types
- Customize with `plt.title()`, `plt.xlabel()`, `plt.ylabel()`, `plt.legend()`, and `plt.grid()`
- Use `plt.subplots()` to put multiple charts in one figure
- Use `plt.savefig()` to export your charts to PNG, PDF, SVG, etc.
- `plt.style.use()` gives you quick theme changes with zero effort
- Always call `plt.close()` when you're done with a figure to free memory
- seaborn and plotly are great next steps once you're comfortable with matplotlib
