# Test-Driven Development

## Objective

Learn how to write tests *before* you write code, and understand why this backwards-sounding approach actually leads to better software.

## Concepts Covered

- What TDD is and why developers swear by it
- The Red-Green-Refactor cycle
- Uncle Bob's Three Rules of TDD
- A complete TDD walkthrough — building a feature step by step
- TDD vs testing after the fact
- Common test patterns (Arrange-Act-Assert, Given-When-Then)
- Test coverage — what it means and why 100% isn't always the goal
- Tips for writing good tests

## Prerequisites

- [unittest Basics](../01-unittest-basics/)
- [pytest Basics](../02-pytest-basics/)
- [Mocking](../03-mocking/)

## Lesson

### What Is TDD?

Test-Driven Development is exactly what it sounds like — you let tests *drive* your development. Instead of writing code first and then testing it, you flip the process:

1. **Write a test** for functionality that doesn't exist yet
2. **Watch it fail** (because you haven't written the code)
3. **Write just enough code** to make the test pass
4. **Clean up** your code while keeping the tests green
5. **Repeat**

That's it. It feels weird at first — you're writing tests for code that doesn't exist! But once it clicks, you'll wonder how you ever coded without it.

### The Red-Green-Refactor Cycle

This is the heartbeat of TDD. Three phases, over and over:

```
    ┌──────────┐
    │   RED    │  Write a failing test
    │  (fail)  │
    └────┬─────┘
         │
         ▼
    ┌──────────┐
    │  GREEN   │  Write the minimum code to pass
    │  (pass)  │
    └────┬─────┘
         │
         ▼
    ┌──────────┐
    │ REFACTOR │  Clean up without changing behavior
    │ (improve)│
    └────┬─────┘
         │
         └──────→ Back to RED
```

**RED** — Write a test that describes what you *want* the code to do. Run it. It should fail. If it passes, either the test is wrong or the feature already exists. A failing test is *good* here — it proves the test is actually checking something.

**GREEN** — Write the simplest, ugliest, most minimal code that makes the test pass. Don't over-engineer. Don't add features the test doesn't ask for. Just make it green.

**REFACTOR** — Now clean up. Remove duplication, rename variables, extract functions — whatever makes the code better. Run the tests after every change to make sure you haven't broken anything. The tests are your safety net.

### Why TDD Works

It sounds like more work, but TDD actually saves time in the long run. Here's why:

**It forces you to think about design first.** Before you write any code, you have to think about *how it will be used*. What does the function take? What does it return? What happens with bad input? You answer these questions upfront instead of discovering them later.

**It catches bugs immediately.** Since you run tests constantly, bugs are caught within minutes of being introduced — not days or weeks later when you've forgotten what you were doing.

**Tests become living documentation.** Your test suite shows exactly what the code is supposed to do, with concrete examples. New team members can read the tests to understand the system.

**It prevents scope creep.** You only write code that a test demands. No "I might need this later" features that add complexity for nothing.

**It makes refactoring safe.** Want to restructure your code? Go ahead — if the tests still pass, you haven't broken anything.

### A Complete TDD Walkthrough

Let's build a `FizzBuzz` function using strict TDD. The rules: given a number, return `"Fizz"` for multiples of 3, `"Buzz"` for multiples of 5, `"FizzBuzz"` for multiples of both, and the number as a string otherwise.

**Step 1: RED — Test the simplest case**

```python
import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_returns_string_of_number(self):
        self.assertEqual(fizzbuzz(1), "1")

# Run it — NameError: name 'fizzbuzz' is not defined
```

**Step 2: GREEN — Minimal code to pass**

```python
def fizzbuzz(n):
    return str(n)
```

That's it. The test passes. Yes, it only handles one case — that's the point.

**Step 3: RED — Add the next test**

```python
def test_returns_fizz_for_multiples_of_3(self):
    self.assertEqual(fizzbuzz(3), "Fizz")
    self.assertEqual(fizzbuzz(6), "Fizz")
```

This fails — `fizzbuzz(3)` returns `"3"`, not `"Fizz"`.

**Step 4: GREEN — Make it pass**

```python
def fizzbuzz(n):
    if n % 3 == 0:
        return "Fizz"
    return str(n)
```

**Step 5: RED — Test for Buzz**

```python
def test_returns_buzz_for_multiples_of_5(self):
    self.assertEqual(fizzbuzz(5), "Buzz")
    self.assertEqual(fizzbuzz(10), "Buzz")
```

**Step 6: GREEN — Make it pass**

```python
def fizzbuzz(n):
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)
```

**Step 7: RED — Test for FizzBuzz**

```python
def test_returns_fizzbuzz_for_multiples_of_3_and_5(self):
    self.assertEqual(fizzbuzz(15), "FizzBuzz")
    self.assertEqual(fizzbuzz(30), "FizzBuzz")
```

**Step 8: GREEN — Make it pass**

```python
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)
```

**Step 9: REFACTOR — Clean up**

```python
def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)
```

We replaced `n % 3 == 0 and n % 5 == 0` with `n % 15 == 0`. Run the tests — still green. Done!

Notice the rhythm: tiny test, tiny code, tiny cleanup. Each cycle takes maybe 2 minutes.

### Uncle Bob's Three Rules of TDD

Robert C. Martin ("Uncle Bob") boiled TDD down to three strict rules:

1. **You are not allowed to write any production code unless it is to make a failing test pass.** No code without a failing test first.

2. **You are not allowed to write any more of a test than is sufficient to fail.** Write one assertion, see it fail, then stop writing the test. (A compilation/import error counts as a failure.)

3. **You are not allowed to write any more production code than is sufficient to pass the one failing test.** Don't add extra logic "just in case." Only write what the test demands.

These rules keep the cycles tiny — often under a minute each. That might sound extreme, but it creates an incredibly tight feedback loop.

### When TDD Makes Sense (And When It Might Not)

**TDD shines when:**
- You're building business logic with clear rules (calculators, validators, parsers)
- You're working on a team and need reliable code
- The requirements are well understood
- You're building an API or library that others will use
- You want to refactor with confidence

**TDD might not be the best fit when:**
- You're prototyping or exploring an idea (you'll throw the code away)
- You're working with UI layout or visual design (hard to test meaningfully)
- You're writing one-off scripts you'll run once
- The problem is so simple that a test would be longer than the code
- You're integrating with external systems where mocking setup would be 90% of the work

TDD is a tool, not a religion. Use it where it helps.

### TDD vs Testing After

| Aspect | TDD (Tests First) | Testing After |
|--------|-------------------|---------------|
| **Design** | Forces you to design before coding | Design happens during coding |
| **Coverage** | Naturally high — every line exists because a test demanded it | Often has gaps — easy to forget edge cases |
| **Speed** | Slower start, faster finish | Faster start, slower finish (bugs found later) |
| **Refactoring** | Safe — tests are already there | Risky unless you write tests first |
| **Mindset** | "What should this do?" | "Does what I wrote work?" |
| **Overtesting** | Rare — you test what matters | Common — you test what's easy to test |

Neither approach is "wrong." But TDD tends to produce code that's easier to test, easier to maintain, and has fewer bugs.

### Common Test Patterns

#### Arrange-Act-Assert (AAA)

The most common pattern for structuring a test. Three clear sections:

```python
def test_deposit_increases_balance(self):
    # Arrange — set up the objects and data
    account = BankAccount(balance=100)

    # Act — perform the action you're testing
    account.deposit(50)

    # Assert — verify the result
    self.assertEqual(account.balance, 150)
```

#### Given-When-Then

Same idea, different vocabulary (popular in BDD — Behavior-Driven Development):

```python
def test_deposit_increases_balance(self):
    # Given a bank account with $100
    account = BankAccount(balance=100)

    # When I deposit $50
    account.deposit(50)

    # Then the balance should be $150
    self.assertEqual(account.balance, 150)
```

Both patterns do the same thing — they keep your tests organized and readable.

### Test Coverage

**Test coverage** measures what percentage of your code gets executed when tests run. If your tests exercise 80 out of 100 lines, you have 80% coverage.

You can measure it with the `coverage` module:

```bash
pip install coverage
coverage run -m pytest
coverage report
```

**Why 100% coverage isn't always the goal:**

- Getting from 80% to 100% often means testing trivial code (getters, `__repr__`, etc.)
- 100% coverage doesn't mean your tests are *good* — you can hit every line without checking anything meaningful
- The last 20% takes disproportionate effort for diminishing returns
- Some code is genuinely hard to test (error handling for unlikely system failures, etc.)

**A reasonable target:** Aim for high coverage on business logic (90%+) and don't stress about 100% everywhere. Coverage is a tool to find *untested* code, not a score to maximize.

### Tips for Writing Good Tests

**One concept per test.** Each test should verify one behavior. If a test has five assertions checking five different things, split it into five tests. When a test fails, you should immediately know *what* broke.

**Use descriptive names.** Test names should read like sentences:

```python
# Bad
def test_1(self): ...
def test_calc(self): ...

# Good
def test_empty_cart_has_zero_total(self): ...
def test_adding_item_increases_count_by_one(self): ...
def test_discount_code_reduces_total_by_percentage(self): ...
```

**Test behavior, not implementation.** Don't test *how* the code works internally. Test *what* it does. If you refactor the internals, your tests shouldn't break.

```python
# Bad — testing implementation details
def test_sort_uses_quicksort(self):
    sorter = Sorter()
    sorter.sort([3, 1, 2])
    self.assertEqual(sorter._algorithm_used, "quicksort")

# Good — testing behavior
def test_sort_returns_elements_in_order(self):
    self.assertEqual(sort_list([3, 1, 2]), [1, 2, 3])
```

**Keep tests independent.** Tests shouldn't depend on each other or on execution order. Each test should set up its own data, run, and clean up. If test B only passes when test A runs first, something is wrong.

**Use test fixtures for repeated setup.** If every test creates the same objects, use `setUp()` (in unittest) or fixtures (in pytest) to avoid duplication.

**Test edge cases.** Empty inputs, zero, negative numbers, None, very large values, special characters. The edges are where bugs hide.

## Code Example

Check out [`example.py`](example.py) for a complete TDD walkthrough building a `Stack` class from scratch — showing every RED, GREEN, and REFACTOR phase.

## Exercises

Try the practice problems in [`exercises.py`](exercises.py) to test your understanding. These exercises flip the usual pattern — **the tests are already written for you**. Your job is to write the code that makes them pass. This is exactly what TDD feels like in practice!

## Key Takeaways

- TDD means writing tests *first*, then writing code to make them pass
- The Red-Green-Refactor cycle: failing test, minimal code, clean up, repeat
- TDD forces better design by making you think about usage before implementation
- The Three Rules: no production code without a failing test, only enough test to fail, only enough code to pass
- Use the Arrange-Act-Assert pattern to keep tests organized
- Test behavior, not implementation — your tests should survive refactoring
- Coverage is a useful metric but 100% isn't a practical goal for most projects
- TDD is a powerful tool — use it where it makes sense, skip it where it doesn't
