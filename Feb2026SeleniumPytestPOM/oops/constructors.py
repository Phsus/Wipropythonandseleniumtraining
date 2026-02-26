class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name, self.salary)

# --- INDENTATION FIXED BELOW ---
# These lines must be outside the class to work
e1 = Employee("Harsha", 50000)
e2 = Employee("Ravi", 656776)

e1.display()
e2.display()

class parent:
    def __init__(self):
        print("i am the parent contructor")


class child1(parent):
    def __init__(self):
       super().__init__()
       print("i am the child1 constructor")

c = child1()
