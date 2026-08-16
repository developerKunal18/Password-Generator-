import secrets
import string


def generate_password(
    length,
    use_uppercase=True,
    use_numbers=True,
    use_symbols=True
):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    characters = lowercase
    required_characters = []

    required_characters.append(secrets.choice(lowercase))

    if use_uppercase:
        characters += uppercase
        required_characters.append(secrets.choice(uppercase))

    if use_numbers:
        characters += numbers
        required_characters.append(secrets.choice(numbers))

    if use_symbols:
        characters += symbols
        required_characters.append(secrets.choice(symbols))

    if length < len(required_characters):
        raise ValueError(
            "Password length is too short for the selected options."
        )

    remaining_length = length - len(required_characters)

    password = required_characters + [
        secrets.choice(characters)
        for _ in range(remaining_length)
    ]

    secrets.SystemRandom().shuffle(password)

    return "".join(password)
