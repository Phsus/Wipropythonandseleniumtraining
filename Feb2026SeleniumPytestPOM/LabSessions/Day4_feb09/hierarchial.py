class Employee:
    def login(self):
        print("Employeee is logged in")


class Developer(Employee):
    def write_code(self):
        print("writing code")


class Tester(Employee):

    def Test_app(self):
        print("test the application")

dev = Developer()
test = Tester()