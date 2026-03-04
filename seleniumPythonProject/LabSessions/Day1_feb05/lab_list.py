numbers = [10, 5, 20, 8, 99, 4]


largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(f"List: {numbers}")
print(f"Largest number: {largest}")


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = []

for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)

print(f"Original List: {numbers}")
print(f"List without evens: {odd_numbers}")


numbers = [2, 3, 4, 5]

product = 1

for num in numbers:
    product = product * num

print(f"List: {numbers}")
print(f"Product of all items: {product}")