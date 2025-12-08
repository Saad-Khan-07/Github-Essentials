import random

def show_welcome():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.\n")

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Enter a valid number.")

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    show_welcome()

    while True:
        guess = get_user_guess()
        attempts += 1

        if guess < number:
            print("Too low! Try again.\n")
        elif guess > number:
            print("Too high! Try again.\n")
        else:
            print(f"✅ Correct! You guessed the number in {attempts} attempts.")
            break

def main():
    play_game()
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
