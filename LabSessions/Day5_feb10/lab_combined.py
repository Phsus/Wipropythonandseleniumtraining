# Q 1
class Employee:
    def calculate_salary(self):
        return 50000

class Manager(Employee):
    def calculate_salary(self):
        base_salary = super().calculate_salary()
        return base_salary + 10000

e = Employee()
m = Manager()
print("Employee Salary:", e.calculate_salary())
print("Manager Salary:", m.calculate_salary())

# Q 2
class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

class Cow:
    def speak(self):
        return "Moo"

def animal_sound(obj):
    print(obj.speak())

d = Dog()
c = Cat()
cow = Cow()
animal_sound(d)
animal_sound(c)
animal_sound(cow)

# Q 3
class Vehicle:
    def fuel_type(self):
        print("Generic Fuel")

class Car(Vehicle):
    def fuel_type(self):
        print("Petrol/Diesel")

class ElectricCar(Car):
    def fuel_type(self):
        print("Electric Charge")

v = Vehicle()
c = Car()
e = ElectricCar()
v.fuel_type()
c.fuel_type()
e.fuel_type()

# Q 4
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance

    def __gt__(self, other):
        return self.balance > other.balance

acc1 = BankAccount(1000)
acc2 = BankAccount(2000)
print("Total Balance:", acc1 + acc2)
print("acc1 > acc2:", acc1 > acc2)

# Q 6
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

obj = D()
obj.show()
print(D.mro())

# Q 7
class Calculator:
    def divide(self, a, b):
        return a / b

class SafeCalculator(Calculator):
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero"

calc = SafeCalculator()
print(calc.divide(10, 2))
print(calc.divide(10, 0))

# Q 8
class Payment:
    def pay(self):
        print("Processing generic payment")

class CreditCard(Payment):
    def pay(self):
        print("Paying via Credit Card")

class UPI(Payment):
    def pay(self):
        print("Paying via UPI")

class NetBanking(Payment):
    def pay(self):
        print("Paying via NetBanking")

def process_payment(payment_obj):
    payment_obj.pay()

p1 = CreditCard()
p2 = UPI()
p3 = NetBanking()
process_payment(p1)
process_payment(p2)
process_payment(p3)