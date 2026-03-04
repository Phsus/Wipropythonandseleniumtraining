import math

class Shape:
    def area(self): pass

class Circle(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self):
        print(f"[Poly] Circle Area: {math.pi * self.radius**2:.2f}")

class Rectangle(Shape):
    def __init__(self, l, b): self.l, self.b = l, b
    def area(self):
        print(f"[Poly] Rectangle Area: {self.l * self.b}")

class Overloader:
    def add(self, a, b, c=0):
        print(f"[Overload] Adding {a}+{b}+{c} = {a+b+c}")

class Point:
    def __init__(self, x): self.x = x
    def __add__(self, other):
        print(f"[Operator] Combining Point({self.x}) and Point({other.x})")
        return Point(self.x + other.x)

# Execution
shapes = [Circle(10), Rectangle(5, 4)]
for s in shapes: s.area()

ov = Overloader()
ov.add(5, 10)
ov.add(5, 10, 15)

p1, p2 = Point(50), Point(100)
p3 = p1 + p2