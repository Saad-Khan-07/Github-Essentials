# gamefeatures.py

import random

def get_random_number():
    """Return a random number between 1 and 10."""
    return random.randint(1, 10)

def check_guess(guess, target):
    """Compare guess to target and return a message."""
    if guess < target:
        return "⬇️ Too low!"
    elif guess > target:
        return "⬆️ Too high!"
    else:
        return "🎉 Correct!"
