import random
from settings import get_difficulty_settings

def show_welcome():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.\n")

def get_user_guess(max_number):
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if 1 <= guess <= max_number:
                return guess
            else:
                print(f"Please enter a number between 1 and {max_number}.")
        except ValueError:
            print("Invalid input. Enter a valid number.")

def play_game():
    max_number, max_attempts = get_difficulty_settings()
    number = random.randint(1, max_number)
    attempts = 0

    show_welcome(max_number, max_attemptsw)

    while attempts < max_attempts:
        guess = get_user_guess(max_number)
        attempts += 1

        if guess < number:
            print("Too low!\n")
        elif guess > number:
            print("Too high!\n")
        else:
            print(f"✅ You guessed it in {attempts} attempts!")
            return

    print(f"❌ Game Over! The number was {number}.")

def main():
    play_game()
    print("Thanks for playing!")

if __name__ == "__main__":
    main()


print("lets learn git today wassup!")
print("additional instructions for the game: ")