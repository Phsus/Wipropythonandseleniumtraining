import time

print("--- 1. Fetching values at index ---")
a = range(5)
print(f"a[1]: {a[1]}")
print(f"a[3]: {a[3]}")

# 'a1 = range' assigns the function, not a range object.
# We must call it, e.g., range(10)
a1 = range(10)
print(f"a1[1]: {a1[1]}")


print("\n--- 2. Forward and Reverse Loops ---")
a = range(2, 5)
for i in a:
    print(i)

# This loop was originally indented inside the previous one (logic error).
# It is now un-indented to run separately.
print("Now printing reverse:")
a_reverse = range(15, 2, -1)
for i in a_reverse:
    print(i)


print("\n--- 3. PIN Logic ---")
for attempt in range(3):
    pin = input('Enter the pin (use 1234): ')
    if pin == "1234":
        print("Access granted")
        break
    else:
        print('Try again')


print("\n--- 4. Price Calculation ---")
prices = [100, 200, 300, 400]

# Fixed typo: 'rane' -> 'range'
for i in range(len(prices)):
    if i % 2 == 0:
        # Fixed formatting: used f-string to show the actual item price
        print(f"Discount applied on item with price: {prices[i]}")


print("\n--- 5. Timer ---")
for second in range(10):
    # Fixed string: added 'f' before the quote to format the variable {second}
    print(f'Checking the status at {second} sec')
    time.sleep(1)