Random Password Generator
This is a Python script that generates random passwords with varying levels of complexity. The script allows the user to input the number of passwords they want to generate, the length of each password, and the special characters they want to include. The script uses Python's random and string libraries to generate random passwords.

Requirements
Python 3.6 or later
How to Use
Clone or download the code to your local machine.
Open a terminal or command prompt and navigate to the directory where the code is saved.
Run the script by entering the command python random_password_generator.py.
Follow the prompts to input the number of passwords, length of each password, and special characters to include.
The script will generate the specified number of random passwords and display their strength scores.
Functions
generate_random_password(length, special_characters)
This function generates a random password with the specified length and special characters. If the special_characters argument is set to 'all', the function will include all punctuation characters. Otherwise, it will only include the specified characters.

check_password_strength(password)
This function calculates the strength score of a password based on the number of characters, digits, uppercase letters, and special characters in the password.

get_valid_input(prompt, input_type)
This function prompts the user to input a valid value of the specified input_type (either 'number' or 'string') and validates the input. If the user enters 'exit', the function returns None.
