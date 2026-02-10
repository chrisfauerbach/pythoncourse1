"""
Todo CLI — Starter Code
==========================

Run this file:
    python3 starter.py add "Buy groceries"
    python3 starter.py list
    python3 starter.py done 1
    python3 starter.py delete 1

Fill in the functions below to build a working to-do list CLI.
Start with load_todos() and save_todos(), then build up the commands.
"""

import argparse
import json
import os

# File where tasks are stored
TODO_FILE = "todos.json"


def load_todos():
    """Load tasks from the JSON file.

    Returns an empty list if the file doesn't exist yet.

    Returns:
        A list of task dicts, e.g.:
        [{"id": 1, "task": "Buy groceries", "done": False}, ...]
    """
    # YOUR CODE HERE
    pass


def save_todos(todos):
    """Save the task list to the JSON file.

    Args:
        todos: List of task dicts to save.
    """
    # YOUR CODE HERE
    pass


def get_next_id(todos):
    """Get the next available task ID.

    Args:
        todos: Current list of tasks.

    Returns:
        The next integer ID (max existing ID + 1, or 1 if empty).
    """
    # YOUR CODE HERE
    pass


def add_task(args):
    """Add a new task.

    1. Load existing todos
    2. Create a new task dict with the next ID
    3. Append it and save
    4. Print confirmation

    Args:
        args: Parsed argparse namespace with args.task (string).
    """
    # YOUR CODE HERE
    pass


def list_tasks(args):
    """Display all tasks in a formatted table.

    Should show ID, status ([x] or [ ]), and task description.
    Print a message if there are no tasks.

    Args:
        args: Parsed argparse namespace (no extra args needed).
    """
    # YOUR CODE HERE
    pass


def complete_task(args):
    """Mark a task as done.

    1. Load todos
    2. Find the task with the matching ID
    3. Set done=True
    4. Save and print confirmation
    5. Print error if ID not found

    Args:
        args: Parsed argparse namespace with args.id (int).
    """
    # YOUR CODE HERE
    pass


def delete_task(args):
    """Delete a task by ID.

    1. Load todos
    2. Find and remove the task with the matching ID
    3. Save and print confirmation
    4. Print error if ID not found

    Args:
        args: Parsed argparse namespace with args.id (int).
    """
    # YOUR CODE HERE
    pass


def main():
    """Set up argparse with subcommands and run the appropriate function.

    Subcommands:
        add <task>    — add a new task
        list          — show all tasks
        done <id>     — mark a task as complete
        delete <id>   — remove a task
    """
    # YOUR CODE HERE — set up the argument parser with subcommands
    # parser = argparse.ArgumentParser(description="A simple todo list manager")
    # subparsers = parser.add_subparsers(dest="command")
    #
    # ... add subcommands ...
    #
    # args = parser.parse_args()
    #
    # ... call the right function based on args.command ...
    pass


if __name__ == "__main__":
    main()
