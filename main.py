import random
import string


def generate_random_password(length, special_characters):
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Length must be a positive integer.")
    if not isinstance(special_characters, str):
        raise ValueError("Special characters must be a string.")
    characters = string.ascii_letters + string.digits
    if special_characters.lower() == 'all':
        characters += string.punctuation
    else:
        characters += special_characters
    password = "".join(random.choice(characters) for _ in range(length))
    return password


def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1
    return score


def get_valid_input(prompt, input_type):
    validation_functions = {
        'number': (lambda x: x.isdigit() and int(x) > 0, int),
        'string': (lambda x: isinstance(x, str), str)
    }
    validate, convert = validation_functions[input_type]
    while True:
        user_input = input(prompt)
        if user_input.lower() == 'exit':
            return None
        elif validate(user_input):
            return convert(user_input)
        else:
            print(f"Invalid input. Please enter a valid {input_type}.")


while True:
    num_passwords = get_valid_input("How many passwords do you want to generate? (Enter 'exit' to quit) ", 'number')
    if num_passwords is None:
        break

    length = get_valid_input("How many characters do you want each password to have? ", 'number')
    if length is None:
        break

    special_characters = get_valid_input(
        "What special characters do you want to use in your password? (Enter 'all' to use all special characters) ",
        'string')
    if special_characters is None:
        break
    elif special_characters.lower() != 'all' and not all(char in string.punctuation for char in special_characters):
        print("Invalid input for special characters. Only punctuation characters are allowed.")
        continue

    for i in range(num_passwords):
        password = generate_random_password(length, special_characters)
        print(f"Password {i + 1}: {password}")
        strength = check_password_strength(password)
        print(f"Password strength score: {strength}/4.\n")
