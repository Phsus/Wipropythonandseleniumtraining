class Employee:
    def __init__(self, name, emp_id, salary):
        self.name, self.id, self.salary = name, emp_id, salary
        print(f"[Employee] Record initialized for {self.name}")


class ObjectCounter:
    count = 0  # Class variable

    def __init__(self):
        ObjectCounter.count += 1
        print(f"[Counter] Object #{ObjectCounter.count} created")


class Company:
    company_name = "Logic Solutions"

    @staticmethod
    def validate_email(email):
        valid = "@" in email and "." in email
        print(f"[Static] Validating '{email}': {'Passed' if valid else 'Failed'}")


# Execution
emp = Employee("Bob", 102, 60000)
obj1 = ObjectCounter()
obj2 = ObjectCounter()
Company.validate_email("hr@logicsolutions.com")