"""
Number Guessing Game — Solution
=================================

Run this file:
    python3 solution.py

A complete number guessing game with input validation, configurable range,
and a play-again loop.
"""

import random


def get_guess(attempt_number):
    """Ask the player for a guess and return it as an integer."""
    while True:
        try:
            return int(input(f"Guess #{attempt_number}: "))
        except ValueError:
            print("That's not a number! Try again.")


def play_round(low=1, high=100):
    """Play one round of the guessing game."""
    secret = random.randint(low, high)
    print(f"I'm thinking of a number between {low} and {high}.")
    print()

    attempts = 0

    while True:
        attempts += 1
        guess = get_guess(attempts)

        if guess < low or guess > high:
            print(f"Please guess between {low} and {high}!")
        elif guess < secret:
            print("Too low! Try higher.")
        elif guess > secret:
            print("Too high! Try lower.")
        else:
            print(f"Correct! You got it in {attempts} guess{'es' if attempts != 1 else ''}!")
            return attempts

        print()


def play_again():
    """Ask the player if they want to play again."""
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter 'y' or 'n'.")


def main():
    """Main game loop."""
    print("=" * 40)
    print("  Welcome to the Number Guessing Game!")
    print("=" * 40)
    print()

    best_score = None

    while True:
        attempts = play_round()

        if best_score is None or attempts < best_score:
            best_score = attempts
            print(f"New best score: {best_score}!")
        else:
            print(f"Your best score is still {best_score}.")

        print()
        if not play_again():
            break
        print()

    print()
    print(f"Thanks for playing! Best score: {best_score} guess{'es' if best_score != 1 else ''}.")


if __name__ == "__main__":
    main()
