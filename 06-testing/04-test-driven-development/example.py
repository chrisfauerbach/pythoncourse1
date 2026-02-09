"""
Test-Driven Development — Example Code
========================================

Run this file:
    python3 example.py

This is a complete TDD walkthrough — building a Stack class from scratch.
We'll go through every RED, GREEN, and REFACTOR phase so you can see TDD
in action.

A Stack is a "last in, first out" (LIFO) data structure. Think of a stack
of plates: you add to the top, and you take from the top.

Operations we want:
  - push(item)  — add an item to the top
  - pop()       — remove and return the top item
  - peek()      — look at the top item without removing it
  - is_empty()  — check if the stack has no items
  - size()      — how many items are on the stack
"""

import unittest


# =============================================================================
# THE FINAL IMPLEMENTATION
# =============================================================================
#
# This is what we end up with after all the TDD cycles below. In real TDD,
# you'd build this up gradually — but since this is one file, here's the
# finished product. The tests below tell the story of how we got here.
# =============================================================================

class Stack:
    """A simple stack data structure, built entirely through TDD."""

    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack")
        return self._items[-1]

    def size(self):
        return len(self._items)


# =============================================================================
# THE TDD JOURNEY — Each test class represents one Red-Green-Refactor cycle
# =============================================================================
#
# Read these in order. Each one shows:
#   RED:      The failing test we wrote first
#   GREEN:    The minimal code that made it pass
#   REFACTOR: Any cleanup we did (if applicable)
#
# In practice, you'd write one test, run it, see it fail, write code, run it,
# see it pass, then clean up. Here we show the final passing state of each
# cycle with comments explaining the journey.
# =============================================================================


class TestCycle1_NewStackIsEmpty(unittest.TestCase):
    """
    CYCLE 1: A new stack should be empty.

    RED phase:
        We write a test that creates a Stack and checks is_empty().
        It fails because the Stack class doesn't exist yet!

        >>> s = Stack()
        >>> s.is_empty()   # NameError: name 'Stack' is not defined

    GREEN phase:
        We create the Stack class with just enough code:

        class Stack:
            def is_empty(self):
                return True

        That's it! The simplest thing that could possibly work.
        The test passes. We resist the urge to add anything else.

    REFACTOR phase:
        Nothing to clean up yet — the code is already minimal.
    """

    def test_new_stack_is_empty(self):
        # Arrange
        s = Stack()

        # Act & Assert
        self.assertTrue(s.is_empty())


class TestCycle2_PushMakesStackNonEmpty(unittest.TestCase):
    """
    CYCLE 2: After pushing an item, the stack should NOT be empty.

    RED phase:
        We write a test that pushes something and checks is_empty().
        It fails because push() doesn't exist yet!

        >>> s = Stack()
        >>> s.push("hello")   # AttributeError: 'Stack' has no attribute 'push'

    GREEN phase:
        We add push() and update is_empty():

        class Stack:
            def __init__(self):
                self._items = []

            def is_empty(self):
                return len(self._items) == 0

            def push(self, item):
                self._items.append(item)

        Now both tests pass. Notice we had to add __init__ with a list
        to track items. That's fine — the test demanded storage.

    REFACTOR phase:
        We changed is_empty() from "return True" to checking the list.
        Previous test still passes. Good.
    """

    def test_push_makes_stack_non_empty(self):
        # Arrange
        s = Stack()

        # Act
        s.push("hello")

        # Assert
        self.assertFalse(s.is_empty())


class TestCycle3_PopReturnsLastPushedItem(unittest.TestCase):
    """
    CYCLE 3: Popping should return the last item that was pushed.

    RED phase:
        >>> s = Stack()
        >>> s.push("hello")
        >>> s.pop()   # AttributeError: 'Stack' has no attribute 'pop'

    GREEN phase:
        def pop(self):
            return self._items.pop()

        One line. That's all we need to make the test pass.

    REFACTOR phase:
        Nothing to clean up. Code is clean.
    """

    def test_pop_returns_last_pushed_item(self):
        # Arrange
        s = Stack()
        s.push("hello")

        # Act
        result = s.pop()

        # Assert
        self.assertEqual(result, "hello")

    def test_pop_returns_items_in_lifo_order(self):
        """We add another test to verify LIFO ordering — still cycle 3."""
        # Arrange
        s = Stack()
        s.push("first")
        s.push("second")
        s.push("third")

        # Act & Assert — items come out in reverse order
        self.assertEqual(s.pop(), "third")
        self.assertEqual(s.pop(), "second")
        self.assertEqual(s.pop(), "first")


class TestCycle4_PopFromEmptyStackRaisesError(unittest.TestCase):
    """
    CYCLE 4: Popping from an empty stack should raise an error.

    RED phase:
        >>> s = Stack()
        >>> s.pop()   # This actually raises IndexError from list.pop()
                      # ...but we want a CLEAR error message.

        We write a test that checks for IndexError with a helpful message.
        It fails because our pop() just does self._items.pop() which gives
        a generic "pop from empty list" message.

    GREEN phase:
        def pop(self):
            if self.is_empty():
                raise IndexError("Cannot pop from an empty stack")
            return self._items.pop()

    REFACTOR phase:
        Nothing to clean up. The guard clause is clean and readable.
    """

    def test_pop_from_empty_stack_raises_error(self):
        s = Stack()

        with self.assertRaises(IndexError) as context:
            s.pop()

        self.assertIn("empty stack", str(context.exception))


class TestCycle5_Peek(unittest.TestCase):
    """
    CYCLE 5: Peeking should return the top item WITHOUT removing it.

    RED phase:
        >>> s = Stack()
        >>> s.push("hello")
        >>> s.peek()   # AttributeError: 'Stack' has no attribute 'peek'

    GREEN phase:
        def peek(self):
            if self.is_empty():
                raise IndexError("Cannot peek at an empty stack")
            return self._items[-1]

        We added the empty check right away this time — we learned from
        cycle 4 that we need to handle that case. (Some TDD purists would
        say we should write the empty-peek test first, but being practical
        is fine too.)

    REFACTOR phase:
        Nothing to clean up.
    """

    def test_peek_returns_top_item(self):
        # Arrange
        s = Stack()
        s.push("bottom")
        s.push("top")

        # Act
        result = s.peek()

        # Assert
        self.assertEqual(result, "top")

    def test_peek_does_not_remove_item(self):
        """This is the key difference from pop — peek leaves the item."""
        # Arrange
        s = Stack()
        s.push("hello")

        # Act
        s.peek()

        # Assert — stack should NOT be empty after peek
        self.assertFalse(s.is_empty())
        self.assertEqual(s.size(), 1)

    def test_peek_on_empty_stack_raises_error(self):
        s = Stack()

        with self.assertRaises(IndexError) as context:
            s.peek()

        self.assertIn("empty stack", str(context.exception))


class TestCycle6_Size(unittest.TestCase):
    """
    CYCLE 6: The stack should report its size.

    RED phase:
        >>> s = Stack()
        >>> s.size()   # AttributeError: 'Stack' has no attribute 'size'

    GREEN phase:
        def size(self):
            return len(self._items)

    REFACTOR phase:
        We look at the whole Stack class and realize... it's already clean!
        Each method is small, clear, and does one thing. The TDD process
        naturally led us to clean code.

        Final version:
            __init__   — creates empty list
            is_empty   — checks if list is empty
            push       — appends to list
            pop        — removes from end (with guard)
            peek       — reads from end (with guard)
            size       — returns length

        Six methods, each one demanded by a test. No dead code, no
        over-engineering. That's the power of TDD.
    """

    def test_new_stack_has_size_zero(self):
        s = Stack()
        self.assertEqual(s.size(), 0)

    def test_size_increases_with_push(self):
        s = Stack()
        s.push("a")
        self.assertEqual(s.size(), 1)
        s.push("b")
        self.assertEqual(s.size(), 2)
        s.push("c")
        self.assertEqual(s.size(), 3)

    def test_size_decreases_with_pop(self):
        s = Stack()
        s.push("a")
        s.push("b")
        s.pop()
        self.assertEqual(s.size(), 1)

    def test_push_and_pop_back_to_empty(self):
        """Full round trip — push items, pop them all, verify empty."""
        s = Stack()
        s.push("x")
        s.push("y")
        s.pop()
        s.pop()
        self.assertTrue(s.is_empty())
        self.assertEqual(s.size(), 0)


# =============================================================================
# Summary
# =============================================================================

class TestStackIntegration(unittest.TestCase):
    """
    After all 6 TDD cycles, we have a fully working Stack.

    This integration test exercises the whole thing together — something you
    might write at the end to verify the pieces work as a whole.
    """

    def test_full_stack_workflow(self):
        s = Stack()

        # Start empty
        self.assertTrue(s.is_empty())
        self.assertEqual(s.size(), 0)

        # Push some items
        s.push(10)
        s.push(20)
        s.push(30)
        self.assertEqual(s.size(), 3)
        self.assertFalse(s.is_empty())

        # Peek at the top
        self.assertEqual(s.peek(), 30)
        self.assertEqual(s.size(), 3)  # peek doesn't remove

        # Pop items in LIFO order
        self.assertEqual(s.pop(), 30)
        self.assertEqual(s.pop(), 20)
        self.assertEqual(s.pop(), 10)

        # Back to empty
        self.assertTrue(s.is_empty())

        # Popping again should raise
        with self.assertRaises(IndexError):
            s.pop()


# =============================================================================
# Run it!
# =============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("TDD Example: Building a Stack Class")
    print("=" * 60)
    print()
    print("Each test class below represents one TDD cycle.")
    print("Read the docstrings to follow the RED-GREEN-REFACTOR journey.")
    print()
    print("-" * 60)

    # Run with some verbosity so you can see each test name
    unittest.main(verbosity=2)
