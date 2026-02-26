class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        print(f"[Car] Instance created: {self.brand} {self.model}")

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_grade(self):
        grade = "A" if self.marks >= 90 else "B" if self.marks >= 75 else "C" if self.marks >= 50 else "F"
        print(f"[Student] {self.name}'s Grade: {grade}")

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        print(f"[Bank] Account opened. Initial Balance: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"[Bank] Deposited ${amount}. Current Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"[Bank] Withdrew ${amount}. Remaining: ${self.balance}")
        else:
            print("[Bank] Alert: Insufficient funds!")

# Execution
c = Car("Honda", "Civic", 22000)
s = Student("Alice", 88)
s.get_grade()
acc = BankAccount(500)
acc.deposit(150)
acc.withdraw(100)