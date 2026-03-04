import os


# 1.

class NumberIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.limit:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration



nums = NumberIterator(5)
for num in nums:
    print(num, end=" ")
print("\n")



# 2.

class EvenIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        if self.current <= self.limit:
            return self.current
        else:
            raise StopIteration



evens = EvenIterator(10)
for num in evens:
    print(num, end=" ")
print("\n")



# 3.

def number_generator(n):
    for i in range(1, n + 1):
        yield i



for num in number_generator(5):
    print(num, end=" ")
print("\n")



# 4.
def even_number_generator(n):
    for i in range(2, n + 1, 2):
        yield i



for num in even_number_generator(10):
    print(num, end=" ")
print("\n")



# 5.
def file_line_reader(filename):
    if not os.path.exists(filename):
        return
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()



filename = "test_gen.txt"
# Create dummy file
with open(filename, "w") as f:
    f.write("Line 1: Hello\nLine 2: World\nLine 3: Python")

# Read using generator
gen = file_line_reader(filename)
for line in gen:
    print(line)

# Cleanup
os.remove(filename)
print()



# 6.
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b



for num in fibonacci_generator(7):
    print(num, end=" ")
print("\n")



# 7.

def retry_generator():
    max_retries = 3
    for attempt in range(1, max_retries + 1):
        yield f"Attempt {attempt}/{max_retries}..."



for attempt in retry_generator():
    print(attempt)