# Modules and Packages

## Objective

Learn how to organize Python code across multiple files, use the standard library, and install third-party packages. This is how real-world Python projects are structured.

## Concepts Covered

- What modules are and how to import them
- `import`, `from...import`, `import...as`
- The module search path (`sys.path`)
- `__name__` and the `if __name__ == "__main__"` pattern
- What packages are (directories with `__init__.py`)
- Relative vs absolute imports
- `__init__.py` — what it does and what to put in it
- `__all__` — controlling what gets exported
- The standard library — useful built-in modules
- Third-party packages and `pip` basics

## Prerequisites

- [Functions](../../01-fundamentals/06-functions/)

## Lesson

### What Is a Module?

Here's the simplest way to think about it: **any `.py` file is a module**. That's it. If you have a file called `helpers.py`, you've already created a module called `helpers`.

When you write code in one file and want to use it in another, you *import* it. This is how you avoid copying and pasting code everywhere.

```python
# helpers.py
def greet(name):
    return f"Hello, {name}!"
```

```python
# main.py
import helpers

print(helpers.greet("Alice"))  # Hello, Alice!
```

Python comes with hundreds of modules already built in — the **standard library**. You've probably already used some of them without thinking much about it.

### Importing Modules

There are several ways to import, and each has its place.

#### Basic import

```python
import math

print(math.sqrt(16))   # 4.0
print(math.pi)         # 3.141592653589793
```

This imports the whole module. You access its contents with `module.thing`. This is the most common and usually the best approach — it keeps things explicit.

#### from...import — grab specific things

```python
from math import sqrt, pi

print(sqrt(16))  # 4.0
print(pi)        # 3.141592653589793
```

Now `sqrt` and `pi` are available directly — no `math.` prefix needed. This is convenient when you only need a few things from a module.

#### import...as — give it a nickname

```python
import datetime as dt

today = dt.date.today()
```

This is handy for modules with long names. You'll see common conventions like `import numpy as np` and `import pandas as pd` in the data science world.

You can also alias specific imports:

```python
from collections import Counter as WordCounter
```

#### The star import (use sparingly)

```python
from math import *  # Imports EVERYTHING from math
```

This dumps all of the module's public names into your namespace. It's generally **discouraged** because you can't tell where names came from, and you might accidentally overwrite something. The one exception is in interactive Python sessions where convenience matters more.

### The Module Search Path

When you write `import something`, Python looks for it in this order:

1. **The current directory** (the folder your script is in)
2. **Directories in the `PYTHONPATH` environment variable** (if set)
3. **The standard library** directories
4. **Site-packages** (where `pip` installs third-party packages)

You can see the full search path:

```python
import sys
print(sys.path)
```

This is why naming your file `random.py` or `math.py` is a bad idea — Python would find *your* file before the standard library one, and things would break in confusing ways.

### `__name__` and `if __name__ == "__main__"`

This is one of those patterns you'll see in virtually every Python project. Here's what's going on.

Every module has a special variable called `__name__`. Its value depends on *how* the file is being used:

- If you **run the file directly** (`python3 myfile.py`), `__name__` is set to `"__main__"`
- If you **import the file** from another module, `__name__` is set to the module's name (like `"myfile"`)

This lets you write code that only runs when the file is executed directly:

```python
# converter.py

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

# This block only runs if you execute: python3 converter.py
# It does NOT run if someone does: import converter
if __name__ == "__main__":
    print(celsius_to_fahrenheit(100))  # 212.0
    print("Converter module running as a script!")
```

Why is this useful? It lets a file be **both** a reusable module and a standalone script. The `if __name__ == "__main__"` block is where you put test code, demos, or a CLI interface.

### What Are Packages?

A **package** is simply a directory that contains Python modules and a special `__init__.py` file. Packages let you organize related modules into a folder hierarchy.

```
myproject/
    __init__.py
    utils/
        __init__.py
        strings.py
        math_helpers.py
    models/
        __init__.py
        user.py
        product.py
```

You import from packages using dot notation:

```python
from myproject.utils.strings import clean_text
from myproject.models.user import User
```

### `__init__.py` — What It Does

The `__init__.py` file tells Python "this directory is a package." It runs whenever the package is imported.

It can be empty — and often is! But you can also use it to:

**1. Set up a convenient public API:**

```python
# myproject/utils/__init__.py
from .strings import clean_text, slugify
from .math_helpers import round_up, clamp
```

Now users can do `from myproject.utils import clean_text` instead of the longer `from myproject.utils.strings import clean_text`.

**2. Run package initialization code:**

```python
# myproject/__init__.py
print("myproject package loaded!")
__version__ = "1.0.0"
```

**3. Control what `from package import *` exports** (see `__all__` below).

A good rule of thumb: start with an empty `__init__.py` and only add to it when you want to simplify your public API.

### Relative vs Absolute Imports

Inside a package, you have two ways to import from sibling modules.

**Absolute imports** use the full path from the project root:

```python
# Inside myproject/utils/strings.py
from myproject.utils.math_helpers import round_up
```

**Relative imports** use dots to mean "current package" or "parent package":

```python
# Inside myproject/utils/strings.py
from .math_helpers import round_up       # . means "same package"
from ..models.user import User           # .. means "parent package"
```

Both work fine, but the Python community generally **prefers absolute imports** — they're easier to read and less fragile when you move files around. Relative imports are fine within a tightly coupled package, but don't overdo them.

### `__all__` — Controlling Star Imports

The `__all__` variable is a list that defines what gets exported when someone does `from module import *`:

```python
# mymodule.py
__all__ = ["public_function", "PublicClass"]

def public_function():
    return "I'm public!"

def _private_helper():
    return "I'm private by convention"

class PublicClass:
    pass

class _InternalClass:
    pass
```

Without `__all__`, a star import grabs everything that doesn't start with an underscore. With `__all__`, only the names in the list are exported. It's a way to explicitly declare your module's public interface.

You'll also see `__all__` in `__init__.py` files to control what a package exports.

### The Standard Library — Your Built-in Toolkit

Python's motto is "batteries included." The standard library is massive, and knowing what's in it saves you from reinventing the wheel. Here are some highlights:

| Module | What It Does | Quick Example |
|--------|-------------|---------------|
| `os` | Operating system interface (env vars, process info) | `os.environ["HOME"]` |
| `sys` | System-specific parameters and functions | `sys.argv`, `sys.path` |
| `math` | Mathematical functions | `math.sqrt(16)`, `math.pi` |
| `random` | Random number generation | `random.randint(1, 6)` |
| `datetime` | Dates and times | `datetime.datetime.now()` |
| `collections` | Specialized container types | `Counter`, `defaultdict`, `namedtuple` |
| `itertools` | Iterator building blocks | `chain`, `combinations`, `groupby` |
| `pathlib` | Object-oriented filesystem paths | `Path("data") / "file.txt"` |
| `json` | JSON encoding and decoding | `json.loads()`, `json.dumps()` |
| `re` | Regular expressions | `re.findall(r"\d+", text)` |
| `functools` | Higher-order functions | `lru_cache`, `partial`, `reduce` |
| `os.path` | File path manipulation (older style) | `os.path.join()`, `os.path.exists()` |
| `csv` | CSV file reading and writing | `csv.reader()`, `csv.DictReader()` |
| `string` | String constants and templates | `string.ascii_letters`, `string.digits` |
| `typing` | Type hints | `List[int]`, `Optional[str]` |

You don't need to memorize all of these. Just know they exist, and when you find yourself thinking "surely Python has something for this" — it probably does. Check the [standard library docs](https://docs.python.org/3/library/).

### Third-Party Packages and pip

The standard library is great, but the real magic of Python is its ecosystem. There are over 400,000 packages on [PyPI](https://pypi.org/) (the Python Package Index).

#### Installing packages with pip

```bash
# Install a package
pip install requests

# Install a specific version
pip install requests==2.31.0

# Install multiple packages
pip install requests flask pandas

# Uninstall a package
pip uninstall requests

# See what's installed
pip list

# Show info about a package
pip show requests
```

#### requirements.txt — tracking dependencies

A `requirements.txt` file lists all the packages your project needs:

```
requests==2.31.0
flask>=3.0.0
pandas~=2.1.0
```

Install everything in one go:

```bash
pip install -r requirements.txt
```

Generate one from your current environment:

```bash
pip freeze > requirements.txt
```

#### Virtual Environments — keeping projects isolated

Different projects might need different versions of the same package. Virtual environments solve this by creating isolated Python installations per project:

```bash
# Create a virtual environment
python3 -m venv myenv

# Activate it (macOS/Linux)
source myenv/bin/activate

# Activate it (Windows)
myenv\Scripts\activate

# Now pip installs go into this environment only
pip install requests

# Deactivate when you're done
deactivate
```

Always use virtual environments for real projects. It's a habit that will save you from "it works on my machine" headaches.

## Code Example

Check out [`example.py`](example.py) for a complete working example that demonstrates everything above.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding.

## Key Takeaways

- Any `.py` file is a module — you import it with `import filename` (without the `.py`)
- Use `import module`, `from module import thing`, or `import module as alias` depending on what's clearest
- Don't name your files after standard library modules (`random.py`, `math.py`, etc.)
- `if __name__ == "__main__"` lets a file work as both an importable module and a standalone script
- A package is a directory with an `__init__.py` file — it groups related modules together
- Prefer absolute imports over relative imports for clarity
- `__all__` controls what gets exported with `from module import *`
- The standard library is huge — check it before writing something from scratch
- Use `pip` to install third-party packages and virtual environments to keep projects isolated
- Always put dependencies in a `requirements.txt` so others can reproduce your setup
