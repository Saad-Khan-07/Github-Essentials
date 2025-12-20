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
    elif guess < target:
        return "Low!"
    elif guess > target:
        return "High!"
    else:
        return "🎉 Correct!"

def calculate_score(attempts, difficulty_choice):
    """
    Calculate score based on attempts and difficulty:
    - Easy:    10 points minus 1 per attempt
    - Medium:  20 points minus 2 per attempt
    - Hard:    40 points minus 3 per attempt
    Score cannot go below zero.
    """
    if difficulty_choice == 1:
        base = 10
        penalty = 1
    elif difficulty_choice == 2:
        base = 20
        penalty = 2
    else:
        base = 40
        penalty = 3

    score = base - (attempts * penalty)
    return max(score, 0)
