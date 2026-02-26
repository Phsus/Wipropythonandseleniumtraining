
class BankAccount:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"[Deposit] {amount} deposited. New Balance: {self.balance}")
        else:
            print("Invalid deposit amount")


class SavingsAccount(BankAccount):

    def add_interest(self, rate):
        interest = self.balance * (rate / 100)
        self.balance += interest
        print(f"[Interest] Added {interest} (Rate: {rate}%).")
        print(f"Final Savings Balance: {self.balance}")



saver = SavingsAccount("Rahul", 1000)
saver.deposit(500)
saver.add_interest(5)


#multilevel

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f" Deposited {amount}. Balance: {self.balance}")


class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        interest = self.balance * (rate / 100)
        self.balance += interest
        print(f" Interest Added: {interest}. New Balance: {self.balance}")


class PremiumSavingsAccount(SavingsAccount):
    def add_welcome_bonus(self, bonus):
        self.balance += bonus
        print(f" Welcome Bonus: {bonus}. Final Balance: {self.balance}")



user = PremiumSavingsAccount("Harsha", 5000)




user.deposit(1000)


user.add_interest(5)


user.add_welcome_bonus(500)