# Definimi i klasës BankAccount
class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Duke depozituar ${amount:.2f}...")
        else:
            print("Gabim: Shuma për depozitë duhet të jetë pozitive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Gabim: Fondet jo të mjaftueshme. Transaksioni u anulua.")
        elif amount <= 0:
            print("Gabim: Shuma për tërheqje duhet të jetë pozitive.")
        else:
            self.balance -= amount
            print(f"Duke tërhequr ${amount:.2f}...")

    def display_balance(self):
        print(f"Bilanci aktual për {self.account_holder}: ${self.balance:.2f}")

# Testimi i klasës BankAccount
def main():
    account = BankAccount("Eduart", 1000.0)
    print(f"Pronar i Llogarisë: {account.account_holder}")
    account.display_balance()

    # Depozitimi
    account.deposit(500.0)
    account.display_balance()

    # Tërheqja
    account.withdraw(200.0)
    account.display_balance()

    # Tërheqje e dështuar
    account.withdraw(1500.0)
    account.display_balance()

if __name__ == "__main__":
    main()

# Nënklasa SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0.0, interest_rate=0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interesi prej {self.interest_rate * 100:.2f}% u aplikua. Bilanci i ri: ${self.balance:.2f}")

# Testimi i SavingsAccount
def test_savings_account():
    savings = SavingsAccount("Eduart", 1000.0, 0.05)
    savings.display_balance()

    # Depozitimi
    savings.deposit(500.0)
    savings.display_balance()

    # Tërheqja
    savings.withdraw(200.0)
    savings.display_balance()

    # Aplikimi i interesit
    savings.apply_interest()
    savings.display_balance()

if __name__ == "__main__":
    test_savings_account()
