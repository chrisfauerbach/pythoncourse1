"""
Working with Paths — Exercises
===============================

Practice problems to test your understanding of pathlib and path handling.
Try to solve each exercise before looking at the solutions below!

Run this file:
    python3 exercises.py

Each exercise creates its own temporary directory and cleans up after itself,
so you can run this file as many times as you like.
"""

from pathlib import Path
import shutil


# =============================================================================
# Exercise 1: Path inspector
#
# Given the path string "/home/alice/documents/report_final.pdf":
#   - Create a Path object from it
#   - Print the file name (just "report_final.pdf")
#   - Print the file stem (just "report_final")
#   - Print the file extension (just ".pdf")
#   - Print the parent directory
#   - Print all the individual parts as a tuple
#
# Expected output:
#   Name:      report_final.pdf
#   Stem:      report_final
#   Extension: .pdf
#   Parent:    /home/alice/documents
#   Parts:     ('/', 'home', 'alice', 'documents', 'report_final.pdf')
#
# =============================================================================

def exercise_1():
    path_string = "/home/alice/documents/report_final.pdf"
    # YOUR CODE HERE
    pass


# =============================================================================
# Exercise 2: Find all Python files
#
# A temp directory has been set up at _ex2_temp/ with some files scattered
# in subdirectories. Use .rglob() to find all .py files and print their
# paths relative to the temp directory.
#
# Hint: Use .relative_to() to get relative paths.
# Print each file on its own line, sorted alphabetically.
#
# Expected output (order of files matters):
#   Found 3 Python files:
#   main.py
#   utils/helpers.py
#   utils/math.py
#
# =============================================================================

def exercise_2():
    # --- Setup (don't modify) ---
    tmp = Path("_ex2_temp")
    if tmp.exists():
        shutil.rmtree(tmp)
    (tmp / "utils").mkdir(parents=True)
    (tmp / "main.py").write_text("print('main')\n")
    (tmp / "utils" / "helpers.py").write_text("# helpers\n")
    (tmp / "utils" / "math.py").write_text("# math\n")
    (tmp / "readme.txt").write_text("Read me!\n")
    (tmp / "data.csv").write_text("a,b\n1,2\n")
    # --- End setup ---

    # YOUR CODE HERE
    pass

    # --- Cleanup (don't modify) ---
    shutil.rmtree(tmp)


# =============================================================================
# Exercise 3: Create a nested directory structure
#
# Using pathlib, create this directory structure inside _ex3_temp/:
#
#   _ex3_temp/
#   └── project/
#       ├── src/
#       │   └── app.py        (contents: "# app code")
#       ├── tests/
#       │   └── test_app.py   (contents: "# test code")
#       └── docs/
#           └── index.md      (contents: "# Documentation")
#
# After creating it, verify that all three files exist by checking
# .is_file() on each one. Print the result for each file.
#
# Expected output:
#   project/src/app.py exists: True
#   project/tests/test_app.py exists: True
#   project/docs/index.md exists: True
#
# =============================================================================

def exercise_3():
    tmp = Path("_ex3_temp")
    if tmp.exists():
        shutil.rmtree(tmp)

    # YOUR CODE HERE
    pass

    # --- Cleanup ---
    if tmp.exists():
        shutil.rmtree(tmp)


# =============================================================================
# Exercise 4: Find the largest file
#
# A temp directory has been set up with several files of different sizes.
# Find and print the name of the largest file and its size in bytes.
#
# Hint: Use .stat().st_size to get a file's size.
#       Use .iterdir() or .glob() to list the files.
#
# Expected output (the largest file is big.txt at 5000 bytes):
#   Largest file: big.txt (5000 bytes)
#
# =============================================================================

def exercise_4():
    # --- Setup (don't modify) ---
    tmp = Path("_ex4_temp")
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir()
    (tmp / "small.txt").write_text("x" * 100)
    (tmp / "medium.txt").write_text("y" * 2500)
    (tmp / "big.txt").write_text("z" * 5000)
    (tmp / "tiny.txt").write_text("a" * 10)
    # --- End setup ---

    # YOUR CODE HERE
    pass

    # --- Cleanup ---
    shutil.rmtree(tmp)


# =============================================================================
# Exercise 5: Organize files by extension
#
# A temp directory has a flat list of mixed files. Organize them by moving
# each file into a subdirectory named after its extension (without the dot).
#
# For example:
#   report.pdf    -> pdf/report.pdf
#   data.csv      -> csv/data.csv
#   photo.jpg     -> jpg/photo.jpg
#
# After organizing, print each subdirectory and the files it contains.
#
# Hint: Use .suffix to get the extension, .mkdir() to create folders,
#       and .rename() to move files.
#
# Expected output (order may vary):
#   csv/
#     data.csv
#     sales.csv
#   jpg/
#     photo.jpg
#   pdf/
#     report.pdf
#   txt/
#     notes.txt
#     readme.txt
#
# =============================================================================

def exercise_5():
    # --- Setup (don't modify) ---
    tmp = Path("_ex5_temp")
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir()
    (tmp / "report.pdf").write_text("PDF content")
    (tmp / "data.csv").write_text("a,b\n1,2")
    (tmp / "photo.jpg").write_bytes(b"\xff\xd8fake jpg")
    (tmp / "notes.txt").write_text("some notes")
    (tmp / "readme.txt").write_text("read me")
    (tmp / "sales.csv").write_text("month,total\nJan,100")
    # --- End setup ---

    # YOUR CODE HERE
    pass

    # --- Cleanup ---
    shutil.rmtree(tmp)


# =============================================================================
# Exercise 6: Directory tree printer
#
# Write a function that prints a directory tree, similar to the Unix `tree`
# command. It should use box-drawing characters for a nice visual display.
#
# Use these characters:
#   "├── " for items that have siblings below them
#   "└── " for the last item in a directory
#   "│   " for vertical lines continuing from above
#   "    " for blank spacing
#
# Expected output:
#   _ex6_temp
#   └── myproject
#       ├── docs
#       │   └── guide.md
#       ├── src
#       │   ├── app.py
#       │   └── utils.py
#       └── README.md
#
# Hint: You'll need a recursive function. Sort entries so directories
#       come before files (for cleaner output). Use .is_dir() to check.
# =============================================================================

def exercise_6():
    # --- Setup (don't modify) ---
    tmp = Path("_ex6_temp")
    if tmp.exists():
        shutil.rmtree(tmp)
    project = tmp / "myproject"
    (project / "src").mkdir(parents=True)
    (project / "docs").mkdir(parents=True)
    (project / "src" / "app.py").write_text("# app\n")
    (project / "src" / "utils.py").write_text("# utils\n")
    (project / "docs" / "guide.md").write_text("# guide\n")
    (project / "README.md").write_text("# readme\n")
    # --- End setup ---

    # YOUR CODE HERE — define a print_tree() function and call it on `tmp`
    pass

    # --- Cleanup ---
    shutil.rmtree(tmp)


# =============================================================================
# Solutions (no peeking until you've tried!)
# =============================================================================

def solution_1():
    path_string = "/home/alice/documents/report_final.pdf"
    p = Path(path_string)
    print(f"Name:      {p.name}")
    print(f"Stem:      {p.stem}")
    print(f"Extension: {p.suffix}")
    print(f"Parent:    {p.parent}")
    print(f"Parts:     {p.parts}")


def solution_2():
    tmp = Path("_ex2_temp")
    if tmp.exists():
        shutil.rmtree(tmp)
    (tmp / "utils").mkdir(parents=True)
    (tmp / "main.py").write_text("print('main')\n")
    (tmp / "utils" / "helpers.py").write_text("# helpers\n")
    (tmp / "utils" / "math.py").write_text("# math\n")
    (tmp / "readme.txt").write_text("Read me!\n")
    (tmp / "data.csv").write_text("a,b\n1,2\n")

    py_files = sorted(tmp.rglob("*.py"))
    print(f"Found {len(py_files)} Python files:")
    for f in py_files:
        print(f"  {f.relative_to(tmp)}")

    shutil.rmtree(tmp)


def solution_3():
    tmp = Path("_ex3_temp")
    if tmp.exists():
        shutil.rmtree(tmp)

    files = {
        tmp / "project" / "src" / "app.py": "# app code",
        tmp / "project" / "tests" / "test_app.py": "# test code",
        tmp / "project" / "docs" / "index.md": "# Documentation",
    }

    for file_path, content in files.items():
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content)

    for file_path in files:
        relative = file_path.relative_to(tmp)
        print(f"{relative} exists: {file_path.is_file()}")

    shutil.rmtree(tmp)


def solution_4():
    tmp = Path("_ex4_temp")
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir()
    (tmp / "small.txt").write_text("x" * 100)
    (tmp / "medium.txt").write_text("y" * 2500)
    (tmp / "big.txt").write_text("z" * 5000)
    (tmp / "tiny.txt").write_text("a" * 10)

    largest = max(tmp.iterdir(), key=lambda f: f.stat().st_size)
    size = largest.stat().st_size
    print(f"Largest file: {largest.name} ({size} bytes)")

    shutil.rmtree(tmp)


def solution_5():
    tmp = Path("_ex5_temp")
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir()
    (tmp / "report.pdf").write_text("PDF content")
    (tmp / "data.csv").write_text("a,b\n1,2")
    (tmp / "photo.jpg").write_bytes(b"\xff\xd8fake jpg")
    (tmp / "notes.txt").write_text("some notes")
    (tmp / "readme.txt").write_text("read me")
    (tmp / "sales.csv").write_text("month,total\nJan,100")

    # Move files into subdirectories by extension
    for f in list(tmp.iterdir()):
        if f.is_file():
            ext = f.suffix.lstrip(".")  # ".csv" -> "csv"
            dest_dir = tmp / ext
            dest_dir.mkdir(exist_ok=True)
            f.rename(dest_dir / f.name)

    # Print the organized structure
    for subdir in sorted(tmp.iterdir()):
        if subdir.is_dir():
            print(f"{subdir.name}/")
            for f in sorted(subdir.iterdir()):
                print(f"  {f.name}")

    shutil.rmtree(tmp)


def solution_6():
    tmp = Path("_ex6_temp")
    if tmp.exists():
        shutil.rmtree(tmp)
    project = tmp / "myproject"
    (project / "src").mkdir(parents=True)
    (project / "docs").mkdir(parents=True)
    (project / "src" / "app.py").write_text("# app\n")
    (project / "src" / "utils.py").write_text("# utils\n")
    (project / "docs" / "guide.md").write_text("# guide\n")
    (project / "README.md").write_text("# readme\n")

    def print_tree(directory, prefix=""):
        path = Path(directory)
        # Sort: directories first, then files, alphabetically within each group
        entries = sorted(path.iterdir(), key=lambda e: (e.is_file(), e.name))

        for i, entry in enumerate(entries):
            is_last = (i == len(entries) - 1)
            connector = "└── " if is_last else "├── "
            print(f"{prefix}{connector}{entry.name}")

            if entry.is_dir():
                extension = "    " if is_last else "│   "
                print_tree(entry, prefix + extension)

    print(tmp.name)
    print_tree(tmp)

    shutil.rmtree(tmp)


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    exercises = [
        ("Path inspector", exercise_1),
        ("Find all Python files", exercise_2),
        ("Create a nested directory structure", exercise_3),
        ("Find the largest file", exercise_4),
        ("Organize files by extension", exercise_5),
        ("Directory tree printer", exercise_6),
    ]

    for i, (title, func) in enumerate(exercises, 1):
        print("=" * 50)
        print(f"EXERCISE {i}: {title}")
        print("=" * 50)
        func()
        print()

    print("-" * 50)
    print("Done! Compare your output with the solutions.")
