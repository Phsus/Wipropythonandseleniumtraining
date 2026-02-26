print(list(enumerate(['a', 'b', 'c'])))

for i, v in enumerate([10, 20, 30]):
    print(i, v)

colors = ['red', 'green', 'blue']
for i, color in enumerate(colors, start=1):
    print(i, color)

print(list(enumerate("PYTHON", start=1)))

nums = [10, 20, 30, 40, 50, 60]

for index, value in enumerate(nums):
    if value == 50:
        print(f"Value 50 found at index: {index}")
        break

for i, n in enumerate(range(10, 60, 10)):
    print(i, n)


data = ['apple', 'banana', 'cherry']

print("--- Using Enumerate ---")
for i, item in enumerate(data):
    print(i, item)

items = ['a', 'b', 'c']
for i in enumerate(items):
    print(i)

print(list(enumerate([], start=5)))

for i, v in enumerate([100, 200, 300], start=-1):
    print(i, v)


i, v = enumerate(['x', 'y', 'z'])



