"""
Number Guessing Game — Starter Code
======================================

Run this file:
    python3 starter.py

Fill in the functions below to build a working number guessing game.
Start with get_guess() and play_round(), then add play_again() and main().
"""

import random


def get_guess(attempt_number):
    """Ask the player for a guess and return it as an integer.

    Should display the attempt number in the prompt (e.g., "Guess #3: ").
    If the player enters something that isn't a number, print a friendly
    message and ask again.

    Args:
        attempt_number: Which guess this is (1, 2, 3, ...)

    Returns:
        The player's guess as an integer.
    """
    # YOUR CODE HERE
    pass


def play_round(low=1, high=100):
    """Play one round of the guessing game.

    1. Pick a random number between low and high
    2. Loop: ask for guesses until the player gets it right
    3. After each wrong guess, print "Too high!" or "Too low!"
    4. When correct, print a congratulations message with the attempt count

    Args:
        low: Lower bound of the range (inclusive)
        high: Upper bound of the range (inclusive)

    Returns:
        The number of guesses it took.
    """
    # YOUR CODE HERE
    pass


def play_again():
    """Ask the player if they want to play again.

    Returns:
        True if they want to play again, False otherwise.
    """
    # YOUR CODE HERE
    pass


def main():
    """Main game loop.

    1. Print a welcome message
    2. Play rounds until the player wants to stop
    3. Print a goodbye message
    """
    # YOUR CODE HERE
    pass


if __name__ == "__main__":
    main()
