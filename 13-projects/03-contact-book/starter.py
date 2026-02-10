"""
Contact Book — Starter Code
==============================

Run this file:
    python3 starter.py

Fill in the classes and functions below to build a working contact book.
Start with the Contact class, then ContactBook, then the menu functions.
"""

import json
import os

# File where contacts are stored
CONTACTS_FILE = "contacts.json"


class Contact:
    """Represents a single contact."""

    def __init__(self, name, phone="", email=""):
        """Initialize a contact with a name and optional phone/email.

        Args:
            name: Contact's full name.
            phone: Phone number (string).
            email: Email address (string).
        """
        # YOUR CODE HERE
        pass

    def to_dict(self):
        """Convert this contact to a dictionary for JSON serialization.

        Returns:
            Dict with 'name', 'phone', and 'email' keys.
        """
        # YOUR CODE HERE
        pass

    @classmethod
    def from_dict(cls, data):
        """Create a Contact from a dictionary (loaded from JSON).

        Args:
            data: Dict with 'name', 'phone', 'email' keys.

        Returns:
            A new Contact instance.
        """
        # YOUR CODE HERE
        pass

    def __str__(self):
        """Return a readable string representation of the contact.

        Format: "Name | Phone | Email"
        """
        # YOUR CODE HERE
        pass


class ContactBook:
    """Manages a collection of contacts with save/load functionality."""

    def __init__(self, filename=CONTACTS_FILE):
        """Initialize the contact book and load existing contacts.

        Args:
            filename: Path to the JSON file for persistence.
        """
        # YOUR CODE HERE — store filename and load contacts
        pass

    def load(self):
        """Load contacts from the JSON file.

        Sets self.contacts to a list of Contact objects.
        If the file doesn't exist, starts with an empty list.
        """
        # YOUR CODE HERE
        pass

    def save(self):
        """Save all contacts to the JSON file."""
        # YOUR CODE HERE
        pass

    def add(self, contact):
        """Add a contact to the book and save.

        Args:
            contact: A Contact instance to add.
        """
        # YOUR CODE HERE
        pass

    def list_all(self):
        """Return all contacts.

        Returns:
            List of Contact objects.
        """
        # YOUR CODE HERE
        pass

    def search(self, query):
        """Search contacts by name (case-insensitive partial match).

        Args:
            query: Search string to match against contact names.

        Returns:
            List of matching Contact objects.
        """
        # YOUR CODE HERE
        pass

    def delete(self, name):
        """Delete a contact by exact name (case-insensitive).

        Args:
            name: Name of the contact to delete.

        Returns:
            True if a contact was deleted, False if not found.
        """
        # YOUR CODE HERE
        pass


def get_input(prompt, required=True):
    """Get user input with optional required validation.

    Args:
        prompt: The prompt to display.
        required: If True, keep asking until non-empty input is given.

    Returns:
        The user's input string (stripped of whitespace).
    """
    # YOUR CODE HERE
    pass


def add_contact_menu(book):
    """Prompt the user for contact details and add to the book."""
    # YOUR CODE HERE
    pass


def list_contacts_menu(book):
    """Display all contacts."""
    # YOUR CODE HERE
    pass


def search_contacts_menu(book):
    """Prompt for a search query and display matching contacts."""
    # YOUR CODE HERE
    pass


def delete_contact_menu(book):
    """Prompt for a name and delete the matching contact."""
    # YOUR CODE HERE
    pass


def main():
    """Main menu loop.

    Display a menu with options to add, list, search, delete, and quit.
    Keep looping until the user chooses to quit.
    """
    # YOUR CODE HERE
    pass


if __name__ == "__main__":
    main()
