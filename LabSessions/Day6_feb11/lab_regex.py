import re

# 1. Check if a string contains only digits
def contains_only_digits(s):
    return bool(re.fullmatch(r"^\d+$", s))

# 2. Match a 10-digit mobile number
def is_valid_mobile(s):
    return bool(re.fullmatch(r"^\d{10}$", s))

# 3. Find all lowercase letters
def find_lowercase(s):
    return re.findall(r"[a-z]", s)

# 4. Extract all uppercase letters
def find_uppercase(s):
    return re.findall(r"[A-Z]", s)

# 5. Match a string that starts with "Hello"
def starts_with_hello(s):
    return bool(re.match(r"^Hello", s))

# 6. Match a string that ends with "world"
def ends_with_world(s):
    return bool(re.search(r"world$", s))

# 7. Find all words separated by spaces
def find_words(s):
    return re.findall(r"\b\w+\b", s)

# 8. Match exactly 5 characters
def match_five_chars(s):
    return bool(re.fullmatch(r"^.{5}$", s))

# 9. Find all occurrences of "python" (case-sensitive)
def find_python(s):
    return re.findall(r"python", s)

# 10. Replace all spaces with underscores
def replace_spaces(s):
    return re.sub(r"\s", "_", s)


print(f"1. Only digits ('12345'): {contains_only_digits('12345')}")
print(f"2. Valid Mobile ('9876543210'): {is_valid_mobile('9876543210')}")
print(f"3. Lowercase in 'PyThOn': {find_lowercase('PyThOn')}")
print(f"4. Uppercase in 'PyThOn': {find_uppercase('PyThOn')}")
print(f"5. Starts with Hello ('Hello World'): {starts_with_hello('Hello World')}")
print(f"6. Ends with world ('Hello world'): {ends_with_world('Hello world')}")
print(f"7. Words in 'This is a test': {find_words('This is a test')}")
print(f"8. Exactly 5 chars ('abcde'): {match_five_chars('abcde')}")
print(f"9. Find 'python': {find_python('I love python and python works well')}")
print(f"10. Replace spaces: {replace_spaces('Hello World Python')}")