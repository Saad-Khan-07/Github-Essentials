def get_difficulty_settings():
    print("\nChoose a difficulty level:")
    print("1. Easy   (1–50, 10 attempts)")
    print("2. Medium (1–100, 7 attempts)")
    print("3. Hard   (1–200, 5 attempts)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        return 50, 10
    elif choice == "2":
        return 100, 7
    elif choice == "3":
        return 200, 5
    else:
        print("Invalid choice. Defaulting to Medium.")
        return 100, 7
