def check_in_range(n, start, end):
    # range(start, end + 1) includes the 'end' number
    if n in range(start, end + 1):
        return True
    else:
        return False

# Example usage:
print(f"Is 5 in range 1-10? {check_in_range(5, 1, 10)}")


def print_evens():
    # range(start, stop, step)
    for num in range(2, 51, 2):
        print(num, end=" ")
    print() # Newline

print_evens()


def sum_numbers():
    total = sum(range(1, 101))
    return total

print(f"The sum is: {sum_numbers()}")


print("Numbers divisible by 5:")
for num in range(5, 101, 5):
    print(num, end=" ")
print()

# range(50, 101, 5) starts at 50, goes up to 100, stepping by 5
num_list = list(range(50, 101, 5))

print(f"Generated List: {num_list}")


print("Squares from 1 to 10:")
for num in range(1, 11):
    square = num ** 2
    print(f"{num}^2 = {square}")

print("Numbers from -10 to 10:")
# We go to 11 to ensure positive 10 is included
for num in range(-10, 11):
    print(num, end=" ")
print()