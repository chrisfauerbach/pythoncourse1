# Project 3: Contact Book

## What You'll Build

An object-oriented contact book that lets you add, search, edit, and delete contacts from the command line. Contacts are stored in a JSON file so they persist between sessions.

## Skills Practiced

- Classes and OOP (Contact class, ContactBook class)
- File I/O with JSON
- Error handling
- Searching and filtering
- Input validation
- Text-based menu interfaces

## Features to Implement

### Core (start here)
1. **Add** a contact (name, phone, email)
2. **List** all contacts
3. **Search** contacts by name (partial match)
4. **Delete** a contact by name
5. **Save/load** contacts to/from a JSON file

### Stretch Goals (once the core works)
- Edit an existing contact's details
- Add multiple phone numbers or emails per contact
- Sort contacts by name
- Export contacts to CSV
- Add categories/tags to contacts
- Input validation for phone numbers and email format

## Example Session

```
=== Contact Book ===

1. Add contact
2. List contacts
3. Search contacts
4. Delete contact
5. Quit

Choose an option: 1
Name: Alice Smith
Phone: 555-1234
Email: alice@example.com
Contact added!

Choose an option: 1
Name: Bob Jones
Phone: 555-5678
Email: bob@example.com
Contact added!

Choose an option: 3
Search: ali
Found 1 contact(s):
  Alice Smith | 555-1234 | alice@example.com

Choose an option: 2
All contacts:
  1. Alice Smith | 555-1234 | alice@example.com
  2. Bob Jones   | 555-5678 | bob@example.com

Choose an option: 5
Contacts saved. Goodbye!
```

## Hints

- Create a `Contact` class with `name`, `phone`, `email` attributes and a `to_dict()` method
- Create a `ContactBook` class that holds a list of `Contact` objects and handles load/save
- Use `json.dump()` / `json.load()` with `[contact.to_dict() for contact in contacts]`
- For search, use `if query.lower() in contact.name.lower()` for case-insensitive partial matching
- Use a `while True` loop for the menu, with `break` when the user chooses quit
- A `@classmethod` called `from_dict()` is a clean way to recreate Contact objects from JSON

## Files

- **`starter.py`** — skeleton code with class and method signatures
- **`solution.py`** — complete working implementation
