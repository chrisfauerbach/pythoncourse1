# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Description

Self-paced Python learning repository with 12 sections progressing from beginner (fundamentals) to advanced (machine learning). ~51 lessons total.

## Running Code

```bash
# Run any example or exercise file directly
python3 <section>/<lesson>/example.py
python3 <section>/<lesson>/exercises.py

# Run tests in the testing section
python3 -m unittest <section>/<lesson>/example.py -v
```

No build system, linter, or test runner configured at the project level. Each `.py` file is standalone and self-contained.

## Repository Structure

Each of the 12 numbered sections (`01-fundamentals/` through `12-machine-learning/`) contains:
- `README.md` — section overview with lesson table
- Numbered lesson folders, each with:
  - `README.md` — concept explanation in plain language
  - `example.py` — runnable demonstration code
  - `exercises.py` — practice problems with solutions at the bottom

## Content Conventions

- **Tone**: Casual, friendly, encouraging. Write like you're explaining to a friend, not writing a textbook.
- **README.md format**: Sections are Objective, Concepts Covered, Prerequisites, Lesson (with subsections), Code Example (links to example.py), Exercises (links to exercises.py), Key Takeaways.
- **example.py format**: Module docstring with run command, numbered sections separated by `# ---` comment banners, inline comments explaining each concept. Prints labeled output so learners see results when run.
- **exercises.py format**: Module docstring, numbered exercises as `exercise_N()` functions with `# YOUR CODE HERE` / `pass` placeholder, followed by matching `solution_N()` functions. `if __name__ == "__main__":` block at the bottom runs all exercises with labeled headers.
- **Advanced sections** (09-12) use `try/except ImportError` guards for third-party packages (numpy, pandas, requests, etc.) with a helpful install message and `sys.exit(0)`.
- Python 3.8+ compatibility target.

## Commit Style

Commit messages describe completed content by section, e.g., "Complete Section 01 Fundamentals with remaining 5 lessons".
