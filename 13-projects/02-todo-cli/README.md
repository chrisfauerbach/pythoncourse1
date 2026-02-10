# Project 2: Todo CLI

## What You'll Build

A command-line to-do list manager that saves tasks to a JSON file. You can add tasks, list them, mark them as done, and delete them — all from the terminal using argparse subcommands.

## Skills Practiced

- File I/O (reading/writing JSON)
- argparse (subcommands, flags, positional arguments)
- Lists and dictionaries
- Functions and program structure
- Error handling
- Working with dates

## Features to Implement

### Core (start here)
1. **`add <task>`** — add a new task with a description
2. **`list`** — show all tasks with their status (done/pending) and ID
3. **`done <id>`** — mark a task as complete
4. **`delete <id>`** — remove a task
5. Tasks persist in a `todos.json` file between runs

### Stretch Goals (once the core works)
- Add `--priority` flag to `add` (low/medium/high)
- Add `--filter` flag to `list` (pending/done/all)
- Add timestamps (created date, completed date)
- Add colored output (green for done, yellow for pending)
- Add a `clear` subcommand to remove all completed tasks

## Example Session

```bash
$ python3 starter.py add "Buy groceries"
Added: Buy groceries (ID: 1)

$ python3 starter.py add "Write README"
Added: Write README (ID: 2)

$ python3 starter.py add "Call dentist"
Added: Call dentist (ID: 3)

$ python3 starter.py list
  ID  Status   Task
  --  ------   ----
   1  [ ]      Buy groceries
   2  [ ]      Write README
   3  [ ]      Call dentist

$ python3 starter.py done 2
Marked as done: Write README

$ python3 starter.py list
  ID  Status   Task
  --  ------   ----
   1  [ ]      Buy groceries
   2  [x]      Write README
   3  [ ]      Call dentist

$ python3 starter.py delete 1
Deleted: Buy groceries
```

## Hints

- Store tasks as a list of dicts: `{"id": 1, "task": "...", "done": False}`
- Use `json.dump()` and `json.load()` for persistence
- Give each task an auto-incrementing ID (find the max existing ID + 1)
- For `list`, use f-string formatting to align columns
- Use `argparse` with subparsers for the `add`, `list`, `done`, `delete` commands
- Wrap file reads in `try/except FileNotFoundError` to handle the first run

## Files

- **`starter.py`** — skeleton code with function signatures and argparse structure
- **`solution.py`** — complete working implementation
