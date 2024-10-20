import random
import string  # Import the 'string' module to get all letters

chars = string.ascii_letters  # Use 'string.ascii_letters' to get all letters

length = int(input("Enter the password length: "))
password = ""

for _ in range(length):
    password += random.choice(chars)  # Use 'random.choice' to pick a random character

print(password)
