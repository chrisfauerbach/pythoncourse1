# Project 1: Number Guessing Game

## What You'll Build

A command-line game where the computer picks a random number and the player tries to guess it. The game gives hints ("too high" / "too low") after each guess and tracks how many attempts it took.

## Skills Practiced

- Variables and user input
- Loops (`while`)
- Conditionals (`if`/`elif`/`else`)
- Random number generation
- String formatting
- Basic input validation

## Features to Implement

### Core (start here)
1. Generate a random number between 1 and 100
2. Ask the player to guess
3. Tell them if the guess is too high, too low, or correct
4. Count the number of guesses
5. When they get it right, show the number of attempts

### Stretch Goals (once the core works)
- Let the player choose the range (e.g., 1-50 or 1-1000)
- Add a maximum number of guesses (e.g., 7 tries)
- Track and display a high score (fewest guesses)
- Add a play-again loop
- Handle non-numeric input gracefully

## Example Session

```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Guess #1: 50
Too high! Try lower.

Guess #2: 25
Too low! Try higher.

Guess #3: 37
Too low! Try higher.

Guess #4: 42
Correct! You got it in 4 guesses!

Play again? (y/n): n
Thanks for playing!
```

## Hints

- `random.randint(1, 100)` gives you a random integer between 1 and 100
- Use a `while True` loop and `break` when they guess correctly
- `input()` always returns a string — you'll need `int()` to convert it
- Wrap `int(input(...))` in a `try/except ValueError` to handle bad input

## Files

- **`starter.py`** — skeleton code with function signatures and structure
- **`solution.py`** — complete working implementation
