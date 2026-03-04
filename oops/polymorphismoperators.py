#operator polymorphism means
# the same operators behaves differently for different data types
# + add numbers
# + joins the strings
#+ merges the lists
# operator overloading in python
#python
'''

__add__()
__sub__()
__mul__()
__eq__()
'''

class Number:
    def __init__(self, value):
        self.value = value

    # Addition (+)
    def __add__(self, other):
        return self.value + other.value

    # Subtraction (-)
    def __sub__(self, other):
        return self.value - other.value

    # Multiplication (*)
    def __mul__(self, other):
        return self.value * other.value

    # Equality (==)
    def __eq__(self, other):
        return self.value == other.value

    # Less than (<)
    def __lt__(self, other):
        return self.value < other.value

    # Greater than (>)
    def __gt__(self, other):
        return self.value > other.value

# --- Testing the code ---
n1 = Number(10)
n2 = Number(20)

print(f"Addition (n1 + n2): {n1 + n2}")       # Output: 30
print(f"Subtraction (n1 - n2): {n1 - n2}")    # Output: -10
print(f"Multiplication (n1 * n2): {n1 * n2}") # Output: 200
print(f"Equality (n1 == n2): {n1 == n2}")     # Output: False
print(f"Less Than (n1 < n2): {n1 < n2}")      # Output: True
print(f"Greater Than (n1 > n2): {n1 > n2}")   # Output: False