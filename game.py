# game.py

from gamefeatures import get_random_number, check_guess

def play_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10...")

    target = get_random_number()
    attempts = 0

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
            print(f"You guessed it in {attempts} attempts!")
            break

if __name__ == "__main__":
    play_game()
