"""
Contact Book — Solution
=========================

Run this file:
    python3 solution.py

An object-oriented contact book with JSON persistence, search, and a
text-based menu interface.
"""

import json
import os

# File where contacts are stored (same directory as this script)
CONTACTS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contacts.json")


class Contact:
    """Represents a single contact."""

    def __init__(self, name, phone="", email=""):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {"name": self.name, "phone": self.phone, "email": self.email}

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            phone=data.get("phone", ""),
            email=data.get("email", ""),
        )

    def __str__(self):
        parts = [self.name]
        if self.phone:
            parts.append(self.phone)
        if self.email:
            parts.append(self.email)
        return " | ".join(parts)


class ContactBook:
    """Manages a collection of contacts with save/load functionality."""

    def __init__(self, filename=CONTACTS_FILE):
        self.filename = filename
        self.contacts = []
        self.load()

    def load(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
            self.contacts = [Contact.from_dict(d) for d in data]
        except FileNotFoundError:
            self.contacts = []

    def save(self):
        with open(self.filename, "w") as f:
            json.dump([c.to_dict() for c in self.contacts], f, indent=2)

    def add(self, contact):
        self.contacts.append(contact)
        self.save()

    def list_all(self):
        return list(self.contacts)

    def search(self, query):
        query_lower = query.lower()
        return [c for c in self.contacts if query_lower in c.name.lower()]

    def delete(self, name):
        name_lower = name.lower()
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name_lower:
                self.contacts.pop(i)
                self.save()
                return True
        return False


def get_input(prompt, required=True):
    """Get user input with optional required validation."""
    while True:
        value = input(prompt).strip()
        if value or not required:
            return value
        print("This field is required. Please enter a value.")


def add_contact_menu(book):
    """Prompt the user for contact details and add to the book."""
    print()
    name = get_input("Name: ")
    phone = get_input("Phone: ", required=False)
    email = get_input("Email: ", required=False)

    contact = Contact(name, phone, email)
    book.add(contact)
    print(f"Contact added: {contact}")


def list_contacts_menu(book):
    """Display all contacts."""
    contacts = book.list_all()
    print()

    if not contacts:
        print("No contacts yet!")
        return

    print(f"All contacts ({len(contacts)}):")
    for i, contact in enumerate(contacts, 1):
        print(f"  {i}. {contact}")


def search_contacts_menu(book):
    """Prompt for a search query and display matching contacts."""
    print()
    query = get_input("Search: ")
    results = book.search(query)

    if not results:
        print(f"No contacts matching '{query}'.")
    else:
        print(f"Found {len(results)} contact(s):")
        for contact in results:
            print(f"  {contact}")


def delete_contact_menu(book):
    """Prompt for a name and delete the matching contact."""
    print()
    name = get_input("Name to delete: ")

    if book.delete(name):
        print(f"Deleted: {name}")
    else:
        print(f"No contact found with name '{name}'.")


def main():
    """Main menu loop."""
    book = ContactBook()

    menu = """
=== Contact Book ===

1. Add contact
2. List contacts
3. Search contacts
4. Delete contact
5. Quit
"""

    actions = {
        "1": add_contact_menu,
        "2": list_contacts_menu,
        "3": search_contacts_menu,
        "4": delete_contact_menu,
    }

    while True:
        print(menu)
        choice = input("Choose an option: ").strip()

        if choice == "5":
            book.save()
            print("Contacts saved. Goodbye!")
            break
        elif choice in actions:
            actions[choice](book)
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()
