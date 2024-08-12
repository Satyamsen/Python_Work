# import random
# import string

# def generate_password(length, use_numbers=False, use_special_chars=False):
#     chars = string.ascii_letters
#     if use_numbers:
#         chars += string.digits
#     if use_special_chars:
#         chars += string.punctuation

#     password = ''.join(random.choice(chars) for _ in range(length))
#     return password

# def main():
#     print("Welcome to the Password Generator!")
#     length = int(input("Enter the length of the password: "))
#     use_numbers = input("Do you want to include numbers? (yes/no): ").lower().startswith('y')
#     use_special_chars = input("Do you want to include special characters? (yes/no): ").lower().startswith('y')

#     password = generate_password(length, use_numbers, use_special_chars)
#     print(f"Generated Password: {password}")

# if __name__ == "__main__":
#     main()
import random
import string

# Function to generate a password
def generate_password(length, use_numbers, use_special_chars):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    # Initialize the pool of characters based on user input
    pool = letters
    if use_numbers:
        pool += digits
    if use_special_chars:
        pool += special_chars

    # Generate password
    password = ''.join(random.choice(pool) for _ in range(length))
    return password

# Input from user
while True:
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

use_numbers = input("Do you want to include numbers? (yes/no): ").lower() in ['yes', 'y']
use_special_chars = input("Do you want to include special characters? (yes/no): ").lower() in ['yes', 'y']

# Generate and print password
password = generate_password(length, use_numbers, use_special_chars)
print(f"Your generated password is: {password}")
