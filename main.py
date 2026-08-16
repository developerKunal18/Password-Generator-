from password_generator import generate_password


def get_yes_no(message):
    while True:
        choice = input(message).strip().lower()

        if choice in ["y", "yes"]:
            return True
        elif choice in ["n", "no"]:
            return False

        print("Please enter y or n.")


def main():
    print("=" * 45)
    print("          PASSWORD GENERATOR")
    print("=" * 45)

    while True:
        try:
            length = int(input("\nEnter password length: "))

            if length < 4:
                print("Password length must be at least 4.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    use_uppercase = get_yes_no("Include uppercase letters? (y/n): ")
    use_numbers = get_yes_no("Include numbers? (y/n): ")
    use_symbols = get_yes_no("Include symbols? (y/n): ")

    password = generate_password(
        length,
        use_uppercase,
        use_numbers,
        use_symbols
    )

    print("\n" + "=" * 45)
    print("Generated Password:")
    print(password)
    print("=" * 45)


if __name__ == "__main__":
    main()
