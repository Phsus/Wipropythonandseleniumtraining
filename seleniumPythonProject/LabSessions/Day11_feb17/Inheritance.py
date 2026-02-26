class Vehicle:
    def move(self): print("[Vehicle] Moving forward")

class Bike(Vehicle):
    def move(self): print("[Bike] Balancing on 2 wheels and moving")

class Person:
    def info(self): print("Level: Person", end=" -> ")

class Staff(Person):
    def info(self):
        super().info()
        print("Level: Staff", end=" -> ")

class Manager(Staff):
    def info(self):
        super().info()
        print("Level: Manager")

# Execution
b = Bike()
b.move()  # Method overriding
mgr = Manager()
mgr.info()  # Multilevel inheritance using super()