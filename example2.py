def get_difficulty_settings():
    print("\nChoose a difficulty level:")
    print("1. Easy   (1–50, 10 attempts)")
    print("2. Medium (1–100, 7 attempts)")
    print("3. Hard   (1–200, 5 attempts)")
    print("4. Custom")
    print("5.. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        return 50, 10
    elif choice == "2":
        return 100, 7
    elif choice == "3":
        return 200, 5
    elif choice == "4":
        custom_range = int(input("Enter the range (1–200): "))
        custom_attempts = int(input("Enter the number of attempts: "))
        return custom_range, custom_attempts
    elif choice == "5":
        print("exiting...")
        return
    else:
        print("Invalid choice. Defaulting to Medium.")
        return 200, 9