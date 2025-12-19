# gamefeatures.py

import random

def get_random_number(low, high):
    """Return a random number within the selected range."""
    return random.randint(low, high)

def get_difficulty_range(choice):
    """Return (min, max) values based on difficulty choice."""
    if choice == 1:
        return (1, 5)      # Easy
    elif choice == 2:
        return (1, 10)     # Medium
    elif choice == 3:
        return (1, 20)     # Hard

def check_guess(guess, target):
    """Compare guess to target and return a message."""
    if guess < target:
        return "⬇️ Too low!"
    elif guess > target:
        return "⬆️ Too high!"
    else:
        return "🎉 Correct!"
