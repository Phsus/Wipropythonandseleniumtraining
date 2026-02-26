class BankAccountSecure:
    def __init__(self, balance):
        self.__balance = balance # Private attribute

    def get_balance(self):
        print(f"[Secure] Viewing private balance: ${self.__balance}")

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
            print(f"[Secure] Balance updated to ${self.__balance}")
        else:
            print("[Secure] Error: Balance cannot be negative")

class SalaryManager:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            print("[Property] Rejected: Negative salary is invalid")
        else:
            self._salary = value
            print(f"[Property] Salary updated to ${self._salary}")

# Execution
sec_acc = BankAccountSecure(1000)
sec_acc.set_balance(1200)
sal_man = SalaryManager(5000)
sal_man.salary = -100  # Will trigger error print
sal_man.salary = 5500  # Will succeed