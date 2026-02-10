"""
Todo CLI — Solution
=====================

Run this file:
    python3 solution.py add "Buy groceries"
    python3 solution.py list
    python3 solution.py done 1
    python3 solution.py delete 1

A command-line to-do list manager that persists tasks in a JSON file.
"""

import argparse
import json
import os
from datetime import datetime

# File where tasks are stored (same directory as this script)
TODO_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "todos.json")


def load_todos():
    """Load tasks from the JSON file."""
    try:
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_todos(todos):
    """Save the task list to the JSON file."""
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)


def get_next_id(todos):
    """Get the next available task ID."""
    if not todos:
        return 1
    return max(t["id"] for t in todos) + 1


def add_task(args):
    """Add a new task."""
    todos = load_todos()
    new_id = get_next_id(todos)

    task = {
        "id": new_id,
        "task": args.task,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }

    todos.append(task)
    save_todos(todos)
    print(f"Added: {args.task} (ID: {new_id})")


def list_tasks(args):
    """Display all tasks in a formatted table."""
    todos = load_todos()

    if not todos:
        print("No tasks yet! Use 'add' to create one.")
        return

    print(f"  {'ID':>4}  {'Status':<8} {'Task'}")
    print(f"  {'--':>4}  {'------':<8} {'----'}")

    for t in todos:
        status = "[x]" if t["done"] else "[ ]"
        print(f"  {t['id']:>4}  {status:<8} {t['task']}")

    # Summary
    done_count = sum(1 for t in todos if t["done"])
    total = len(todos)
    print()
    print(f"  {done_count}/{total} completed")


def complete_task(args):
    """Mark a task as done."""
    todos = load_todos()

    for t in todos:
        if t["id"] == args.id:
            if t["done"]:
                print(f"Already done: {t['task']}")
            else:
                t["done"] = True
                t["completed"] = datetime.now().strftime("%Y-%m-%d %H:%M")
                save_todos(todos)
                print(f"Marked as done: {t['task']}")
            return

    print(f"Error: No task with ID {args.id}")


def delete_task(args):
    """Delete a task by ID."""
    todos = load_todos()

    for i, t in enumerate(todos):
        if t["id"] == args.id:
            removed = todos.pop(i)
            save_todos(todos)
            print(f"Deleted: {removed['task']}")
            return

    print(f"Error: No task with ID {args.id}")


def main():
    """Set up argparse with subcommands and run the appropriate function."""
    parser = argparse.ArgumentParser(
        description="A simple todo list manager",
        epilog="Examples: %(prog)s add 'Buy milk' | %(prog)s list | %(prog)s done 1"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # add
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", help="Task description")

    # list
    subparsers.add_parser("list", help="Show all tasks")

    # done
    done_parser = subparsers.add_parser("done", help="Mark a task as complete")
    done_parser.add_argument("id", type=int, help="Task ID to mark as done")

    # delete
    del_parser = subparsers.add_parser("delete", help="Remove a task")
    del_parser.add_argument("id", type=int, help="Task ID to delete")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return

    commands = {
        "add": add_task,
        "list": list_tasks,
        "done": complete_task,
        "delete": delete_task,
    }

    commands[args.command](args)


if __name__ == "__main__":
    main()
