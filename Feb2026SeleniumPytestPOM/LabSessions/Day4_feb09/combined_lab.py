import math
from datetime import date

# ==========================================
# 1. Circle Class (Area and Perimeter)
# ==========================================
print("\n--- Question 1: Circle Area & Perimeter ---")

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

# Execution
c = Circle(5)
print(f"Radius: {c.radius}")
print(f"Area: {c.calculate_area():.2f}")
print(f"Perimeter: {c.calculate_perimeter():.2f}")


# ==========================================
# 2. Person Class (Age Calculation)
# ==========================================
print("\n--- Question 2: Person Age Calculation ---")

class Person:
    def __init__(self, name, country, dob_year):
        self.name = name
        self.country = country
        self.dob_year = dob_year

    def determine_age(self):
        current_year = date.today().year
        return current_year - self.dob_year

# Execution
p = Person("Alice", "USA", 1995)
print(f"Name: {p.name}, Country: {p.country}")
print(f"Age: {p.determine_age()} years")


# ==========================================
# 3. Shape Class with Subclasses
# ==========================================
print("\n--- Question 3: Shape Subclasses ---")

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class ShapeCircle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return (math.sqrt(3) / 4) * (self.side ** 2)
    def perimeter(self):
        return 3 * self.side

# Execution
shapes = [ShapeCircle(5), Square(4), Triangle(6)]
for s in shapes:
    # Uses Polymorphism (same method name, different behavior)
    print(f"Shape: {type(s).__name__} | Area: {s.area():.2f} | Perimeter: {s.perimeter():.2f}")


# ==========================================
# 4. Bus Inheriting from Vehicle
# ==========================================
print("\n--- Question 4: Bus Inheriting Vehicle ---")

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display_info(self):
        print(f"Vehicle: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}")

# Child class inheriting from Vehicle
class Bus(Vehicle):
    pass

# Execution
school_bus = Bus("Volvo", 180, 12)
school_bus.display_info()


# ==========================================
# 5. Empty Vehicle Class
# ==========================================
print("\n--- Question 5: Empty Vehicle Class ---")

class EmptyVehicle:
    pass

# Execution
obj = EmptyVehicle()
print("Empty object created successfully:", obj)