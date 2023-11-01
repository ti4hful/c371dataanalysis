# Cintia Biro-Hajnal 25/10/23

import random
import string

class PasswordGenerator:
    def __init__(self):
        self.a = 100

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > 999:
            raise StopIteration
        password = ""
        for _ in range(15):
            # Generate a random character from letters (both lowercase and uppercase) and special characters
            random_char = random.choice(string.ascii_letters + string.digits + string.punctuation)
            password += random_char
        self.a += 1
        return password

# Create an instance of the PasswordGenerator class
passwords = PasswordGenerator()

# Create a list of at least five randomly-generated passwords
generated_passwords = [password for password in passwords]

# Display the list of generated passwords
print("Generated Passwords:")
for i, password in enumerate(generated_passwords, 1):
    print(f"{i}: {password}")

# Allow the user to select a password from the list
while True:
    try:
        selected_index = int(input("Select a password (enter the password number): "))
        if 1 <= selected_index <= len(generated_passwords):
            selected_password = generated_passwords[selected_index - 1]
            print(f"Selected Password: {selected_password}")
            break
        else:
            print("Invalid input. Please enter a valid password number.")
    except ValueError:
        print("Invalid input. Please enter a valid password number.")

