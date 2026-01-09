# Password Generator using Python

import random
import string

print("Password Generator")

while True:
    length = int(input("\nEnter password length: "))

    if length <= 0:
        print("Please enter a valid length")
        continue

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password = password + random.choice(characters)

    print("Generated Password:", password)

    again = input("Do you want to generate another password? (yes/no): ")
    if again != "yes":
        break

print("Program ended")
