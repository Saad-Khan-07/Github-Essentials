# game.py

from gamefeatures import get_random_number, check_guess, get_difficulty_range, calculate_score
import time

start_time = time.time()

def play_game():
    print("🎮 Welcome to the Number Guessing Game! WASSUUUUPPPPPPP🔥🔥🔥🔥🔥🔥")
    print("New ranges from next week onwards. Try to sum up your points till then!!")
    print("Select a difficulty level:")
    print("1. Easy (1–5)")
    print("2. Medium (1–10)")
    print("3. Hard (1–20)")

    while True:
        try:
            difficulty_choice = int(input("Enter choice (1-3): "))
            if difficulty_choice not in [1, 2, 3]:
                raise ValueError
            break
        except ValueError:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

    low, high = get_difficulty_range(difficulty_choice)
    target = get_random_number(low, high)
    attempts = 0

    print(f"🌟 I am thinking of a number between {low} and {high}...")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        attempts += 1
        result = check_guess(guess, target)

        print(result)

        if result.startswith("🎉"):
            score = calculate_score(attempts, difficulty_choice)
            print(f"You guessed it in {attempts} attempts!")
            print(f"🏆 Your score: {score}")
            break

        while True:
            play_game()
            
            # Strip whitespace and handle empty inputs
            choice = input("\nPlay again? (y/n): ").strip().lower()
            
            if choice not in ('y', 'yes'):
                print("Thanks for playing. Goodbye!")
                break

    end_time = time.time()
    duration = round(end_time - start_time, 2)
    print(f"⏱️ You took {duration} seconds to win!")


if __name__ == "__main__":
    play_game()
