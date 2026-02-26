# 1. Variable Definitions
empty_list = []
numbers = [1, 2, 3, 4, 0, 8, 3]

# Fixed: Renamed to 'mixed_data' for consistency and readability
mixed_data = [1, "hello", True, 6.67, 1]

# Fixed: Changed outer {} to [] because you cannot have lists inside a set {}
nested = [[1, 2], [3, 4]]

print("--- Accessing Data ---")
# Fixed: Syntax print{...} -> print(...)
print(mixed_data[1])
print(mixed_data[2])

print("\n--- Modifying Data ---")
mixed_data[4] = 6
print(mixed_data)

mixed_data.insert(0, 10)
print(mixed_data)

mixed_data.append("john")
print(mixed_data)

mixed_data.remove("hello")
print(mixed_data)

mixed_data.pop()
print(mixed_data)

mixed_data.pop(1)
print(mixed_data)

print("\n--- Number Operations ---")
# Fixed: .sort() returns None. You must sort first, then print.
numbers.sort()
print(f"Sorted: {numbers}")

# Fixed: .reverse() returns None. You must reverse first, then print.
numbers.reverse()
print(f"Reversed: {numbers}")

# Fixed: Variable name 'numbers' (plural)
print(f"Count of 3: {numbers.count(3)}")
print(f"Index of 3: {numbers.index(3)}")

numbers.clear()
print(f"Cleared numbers: {numbers}")

print("\n--- Fruit Loops ---")
# Fixed: Replaced dot (.) with comma (,)
fruits = ["apple", "banana", "cherry"]

for item in fruits:
    print(item)

for i, fruit in enumerate(fruits):
    print(i, fruit)