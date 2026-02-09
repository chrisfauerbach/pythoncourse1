"""
Working with Paths — Example Code
===================================

Run this file:
    python3 example.py

This file demonstrates how to use Python's pathlib module for all your
file path needs. We'll create a temporary playground directory, do a bunch
of path operations, and clean everything up at the end.
"""

from pathlib import Path
import shutil

# We'll do all our work inside a temporary directory so we don't litter
PLAYGROUND = Path("_path_playground")

# -----------------------------------------------------------------------------
# 1. Creating Path objects
# -----------------------------------------------------------------------------

print("=" * 60)
print("1. CREATING PATH OBJECTS")
print("=" * 60)

# From a string
p = Path("my_folder/my_file.txt")
print(f"From string:       {p}")

# Current working directory
cwd = Path.cwd()
print(f"Current directory:  {cwd}")

# User's home directory
home = Path.home()
print(f"Home directory:     {home}")

# From multiple parts — pathlib joins them with the right separator
p = Path("my_folder", "subfolder", "file.txt")
print(f"From parts:         {p}")

print()

# -----------------------------------------------------------------------------
# 2. Path components — taking paths apart
# -----------------------------------------------------------------------------

print("=" * 60)
print("2. PATH COMPONENTS")
print("=" * 60)

p = Path("/home/alice/projects/report.csv")
print(f"Full path:  {p}")
print(f"  .name     {p.name}")       # "report.csv"
print(f"  .stem     {p.stem}")       # "report"
print(f"  .suffix   {p.suffix}")     # ".csv"
print(f"  .parent   {p.parent}")     # "/home/alice/projects"
print(f"  .parts    {p.parts}")      # ("/", "home", "alice", ...)
print(f"  .anchor   {p.anchor}")     # "/"

# Works great for files with multiple extensions too
p2 = Path("archive.tar.gz")
print(f"\nDouble extension:  {p2}")
print(f"  .suffix   {p2.suffix}")    # ".gz" (last extension only)
print(f"  .suffixes {p2.suffixes}")  # [".tar", ".gz"] (all of them)
print(f"  .stem     {p2.stem}")      # "archive.tar"

print()

# -----------------------------------------------------------------------------
# 3. Building paths with the / operator
# -----------------------------------------------------------------------------

print("=" * 60)
print("3. BUILDING PATHS WITH /")
print("=" * 60)

# The / operator joins path segments — clean and readable
base = Path("/home/alice")
full = base / "projects" / "report.csv"
print(f"Built path: {full}")

# You can chain as many segments as you want
data_file = Path("data") / "2025" / "january" / "sales.csv"
print(f"Data file:  {data_file}")

# Works with variables too
folder_name = "downloads"
file_name = "photo.jpg"
combined = Path.home() / folder_name / file_name
print(f"Combined:   {combined}")

print()

# -----------------------------------------------------------------------------
# 4. Setting up our playground directory
# -----------------------------------------------------------------------------

print("=" * 60)
print("4. CREATING DIRECTORIES AND FILES")
print("=" * 60)

# Clean up any previous run
if PLAYGROUND.exists():
    shutil.rmtree(PLAYGROUND)

# Create nested directories in one go with parents=True
docs_dir = PLAYGROUND / "docs"
src_dir = PLAYGROUND / "src" / "utils"
data_dir = PLAYGROUND / "data"

docs_dir.mkdir(parents=True, exist_ok=True)
src_dir.mkdir(parents=True, exist_ok=True)
data_dir.mkdir(parents=True, exist_ok=True)

print(f"Created: {docs_dir}")
print(f"Created: {src_dir}")
print(f"Created: {data_dir}")

# Create some files using write_text()
(docs_dir / "readme.txt").write_text("This is the README.\n")
(docs_dir / "notes.txt").write_text("Some notes here.\n")
(docs_dir / "guide.md").write_text("# User Guide\n\nWelcome!\n")
(src_dir / "helpers.py").write_text("def greet():\n    return 'hello'\n")
(src_dir / "math_utils.py").write_text("def add(a, b):\n    return a + b\n")
(PLAYGROUND / "src" / "main.py").write_text("print('Hello from main!')\n")
(data_dir / "sales.csv").write_text("month,amount\nJan,1000\nFeb,1500\n")
(data_dir / "config.json").write_text('{"debug": true}\n')

print(f"Created 8 sample files inside {PLAYGROUND}/")

print()

# -----------------------------------------------------------------------------
# 5. Checking paths — exists, is_file, is_dir
# -----------------------------------------------------------------------------

print("=" * 60)
print("5. CHECKING PATHS")
print("=" * 60)

readme = docs_dir / "readme.txt"
fake = PLAYGROUND / "nonexistent.txt"

print(f"{readme.name}:")
print(f"  .exists()   {readme.exists()}")    # True
print(f"  .is_file()  {readme.is_file()}")   # True
print(f"  .is_dir()   {readme.is_dir()}")    # False

print(f"\n{docs_dir.name}/:")
print(f"  .exists()   {docs_dir.exists()}")  # True
print(f"  .is_file()  {docs_dir.is_file()}")  # False
print(f"  .is_dir()   {docs_dir.is_dir()}")  # True

print(f"\n{fake.name}:")
print(f"  .exists()   {fake.exists()}")      # False

print()

# -----------------------------------------------------------------------------
# 6. Listing directory contents — iterdir, glob, rglob
# -----------------------------------------------------------------------------

print("=" * 60)
print("6. LISTING DIRECTORY CONTENTS")
print("=" * 60)

# iterdir() — list everything in one directory (not recursive)
print("Everything in docs_dir (iterdir):")
for item in sorted(docs_dir.iterdir()):
    tag = "[FILE]" if item.is_file() else "[DIR] "
    print(f"  {tag} {item.name}")

# glob() — find matching files in one directory
print("\nAll .txt files in docs_dir (glob):")
for txt_file in sorted(docs_dir.glob("*.txt")):
    print(f"  {txt_file.name}")

# rglob() — find matching files RECURSIVELY (all subdirectories)
print("\nAll .py files anywhere in playground (rglob):")
for py_file in sorted(PLAYGROUND.rglob("*.py")):
    # .relative_to() shows the path relative to the playground
    print(f"  {py_file.relative_to(PLAYGROUND)}")

# You can also use ** in glob for recursive matching
print("\nAll files in data/ using glob('*.*'):")
for f in sorted(data_dir.glob("*.*")):
    print(f"  {f.name}")

print()

# -----------------------------------------------------------------------------
# 7. Reading and writing shortcuts
# -----------------------------------------------------------------------------

print("=" * 60)
print("7. READING AND WRITING SHORTCUTS")
print("=" * 60)

# write_text() — write a string to a file (creates or overwrites)
greeting_file = PLAYGROUND / "greeting.txt"
greeting_file.write_text("Hello from pathlib!\nThis is easy.\n")
print(f"Wrote to: {greeting_file.name}")

# read_text() — read the entire file as a string
content = greeting_file.read_text()
print(f"Read back:\n{content}")

# write_bytes() / read_bytes() — for binary data
binary_file = PLAYGROUND / "data.bin"
binary_file.write_bytes(b"\x00\x01\x02\x03\xff")
raw = binary_file.read_bytes()
print(f"Binary data: {list(raw)}")

print()

# -----------------------------------------------------------------------------
# 8. Renaming and deleting
# -----------------------------------------------------------------------------

print("=" * 60)
print("8. RENAMING AND DELETING")
print("=" * 60)

# Rename a file
old_path = PLAYGROUND / "greeting.txt"
new_path = PLAYGROUND / "hello.txt"
old_path.rename(new_path)
print(f"Renamed: greeting.txt -> hello.txt")
print(f"  Old exists? {old_path.exists()}")   # False
print(f"  New exists? {new_path.exists()}")   # True

# Delete a file with unlink()
binary_file.unlink()
print(f"\nDeleted: {binary_file.name}")
print(f"  Still exists? {binary_file.exists()}")  # False

# unlink with missing_ok=True — won't crash if file is already gone
binary_file.unlink(missing_ok=True)
print("  Called unlink again with missing_ok=True — no error!")

print()

# -----------------------------------------------------------------------------
# 9. os.path vs pathlib — side by side
# -----------------------------------------------------------------------------

print("=" * 60)
print("9. os.path vs pathlib COMPARISON")
print("=" * 60)

import os.path

filepath = "/home/alice/projects/report.csv"
p = Path(filepath)

# Joining paths
old_way = os.path.join("/home/alice", "projects", "report.csv")
new_way = Path("/home/alice") / "projects" / "report.csv"
print(f"Join paths:")
print(f"  os.path:  {old_way}")
print(f"  pathlib:  {new_way}")

# Getting the filename
old_way = os.path.basename(filepath)
new_way = p.name
print(f"\nGet filename:")
print(f"  os.path:  {old_way}")
print(f"  pathlib:  {new_way}")

# Getting the extension
old_way = os.path.splitext(filepath)[1]
new_way = p.suffix
print(f"\nGet extension:")
print(f"  os.path:  {old_way}")
print(f"  pathlib:  {new_way}")

# Getting the parent directory
old_way = os.path.dirname(filepath)
new_way = p.parent
print(f"\nGet parent:")
print(f"  os.path:  {old_way}")
print(f"  pathlib:  {new_way}")

print("\npathlib is almost always cleaner and more readable!")

print()

# -----------------------------------------------------------------------------
# 10. Common pattern — walk a directory tree
# -----------------------------------------------------------------------------

print("=" * 60)
print("10. COMMON PATTERN: DIRECTORY TREE")
print("=" * 60)


def show_tree(directory, prefix=""):
    """Print a directory tree, similar to the `tree` command."""
    path = Path(directory)
    entries = sorted(path.iterdir(), key=lambda e: (e.is_file(), e.name))

    for i, entry in enumerate(entries):
        # Use box-drawing characters for a nice tree display
        is_last = (i == len(entries) - 1)
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{entry.name}")

        if entry.is_dir():
            extension = "    " if is_last else "│   "
            show_tree(entry, prefix + extension)


print(f"Tree of {PLAYGROUND}:")
show_tree(PLAYGROUND)

print()

# -----------------------------------------------------------------------------
# 11. Cleanup — remove our playground
# -----------------------------------------------------------------------------

print("=" * 60)
print("11. CLEANUP")
print("=" * 60)

# shutil.rmtree() removes an entire directory tree
# (pathlib's .rmdir() only works on EMPTY directories)
shutil.rmtree(PLAYGROUND)
print(f"Removed {PLAYGROUND}/ and all its contents")
print(f"  Still exists? {PLAYGROUND.exists()}")

print()
print("=" * 60)
print("   WORKING WITH PATHS COMPLETE!")
print("=" * 60)
print()
print("The key lesson: use pathlib.Path for all your path operations.")
print("It's cleaner, cross-platform, and the modern Python way!")
