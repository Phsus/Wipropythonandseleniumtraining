import json

# --- PART 1: READING JSON ---
print("--- 1. Reading Nested JSON ---")

# Fix: Added parentheses () around open and used r"" for safe path handling
file_path_1 = r"C:\Users\KIIT01\PycharmProjects\seleniumPythonProject\dataformats\nestedjson.json"

try:
    with open(file_path_1, 'r') as file:
        data = json.load(file)
        print("Full Data:", data)
        # Check if 'name' exists before printing to avoid errors
        print("Name:", data.get("name"))
except FileNotFoundError:
    print(f"Error: File not found at {file_path_1}")

print("\n--- 2. Reading Employee JSON (Nested) ---")
file_path_2 = r"C:\Users\KIIT01\PycharmProjects\seleniumPythonProject\dataformats\employee.json"

try:
    with open(file_path_2, 'r') as file:
        emp_data = json.load(file)

        # Access nested data safely
        # Ensure the structure matches your JSON file
        email = emp_data["user"]["profile"]["email"]
        print(f"Email found: {email}")

except (FileNotFoundError, KeyError) as e:
    print(f"Error reading employee file: {e}")

# --- PART 3: WRITING NEW JSON FILE ---
print("\n--- 3. Writing to a New JSON File ---")
new_data = {
    "name": "Harsha",
    "role": "QA Automation",
    "skills": ["Python", "Selenium", "API Testing"]
}

output_path = r"C:\Users\KIIT01\PycharmProjects\seleniumPythonProject\dataformats\new_output.json"

with open(output_path, 'w') as file:
    # indent=4 makes the file readable (pretty print)
    json.dump(new_data, file, indent=4)
    print(f"Successfully wrote data to {output_path}")

# --- PART 4: UPDATING AN EXISTING JSON FILE ---
print("\n--- 4. Updating the JSON File ---")

# 1. Read the file first
with open(output_path, 'r') as file:
    current_data = json.load(file)

# 2. Modify the data (Update logic)
current_data["name"] = "Harsha Vardhan"  # Update existing key
current_data["experience"] = "5 Years"  # Add new key

# 3. Write it back to the file
with open(output_path, 'w') as file:
    json.dump(current_data, file, indent=4)
    print("Successfully updated the JSON file.")