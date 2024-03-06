import itertools
import pyfiglet

toolname=pyfiglet.figlet_format("Shanawaz Numeric Password Wordlist Generator")

print(toolname)

def generate_number_password_wordlist(min_length, max_length):
    if min_length < 1 or max_length < min_length:
        raise ValueError("Invalid length parameters")

    digits = [str(i) for i in range(10)]
    password_wordlist = []

    for length in range(min_length, max_length + 1):
        combinations = itertools.product(digits, repeat=length)
        password_wordlist.extend([''.join(combination) for combination in combinations])

    return password_wordlist

def save_to_file(passwords, filename):
    with open(filename, 'w') as file:
        for password in passwords:
            file.write(password + '\n')

# User input for minimum and maximum lengths
min_length = int(input("Enter minimum password length: "))
max_length = int(input("Enter maximum password length: "))

# User input for the filename
filename = input("Enter the filename for the generated password list: ")

# Generate password wordlist
passwords = generate_number_password_wordlist(min_length, max_length)

# Save the password wordlist to the specified file
save_to_file(passwords, filename)

print(f"Password wordlist generated and saved to {filename}.")
