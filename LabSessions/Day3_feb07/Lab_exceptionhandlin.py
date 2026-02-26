import json

file_path = "C://Users//KIIT01//PycharmProjects//seleniumPythonProject//dataformats//nestedjson.json"

try:
    with open(file_path, "r") as file:
        data = json.load(file)
        print(data)

except FileNotFoundError:
    print("File not found.")


while True:
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)
        print(f"You entered: {number}")
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

import random
import string

random_char = random.choice(string.ascii_letters)
print(random_char)

random_length = random.randint(1, 10)
random_str = ""
for _ in range(random_length):
    random_str += random.choice(string.ascii_letters)
print(random_str)

fixed_length = 8
fixed_str = ""
for _ in range(fixed_length):
    fixed_str += random.choice(string.ascii_letters)
print(fixed_str)

