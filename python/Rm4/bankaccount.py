class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        """Inicializon një llogari bankare me emrin e pronarit dhe bilancin fillestar."""
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """Shton një shumë në bilancin e llogarisë."""
        if amount > 0:
            self.balance += amount
            print(f"{amount:.2f} u depozitua. Bilanci i ri: {self.balance:.2f}")
        else:
            print("Shuma për depozitë duhet të jetë pozitive!")

    def withdraw(self, amount):
        """Zbrit një shumë nga bilanci nëse ka fonde të mjaftueshme."""
        if amount > self.balance:
            print("Fondet e pamjaftueshme! Tërheqja dështoi.")
        elif amount <= 0:
            print("Shuma për tërheqje duhet të jetë pozitive!")
        else:
            self.balance -= amount
            print(f"{amount:.2f} u tërhoq. Bilanci i ri: {self.balance:.2f}")

    def display_balance(self):
        """Shfaq bilancin aktual të llogarisë."""
        print(f"Llogaria e {self.account_holder}: Bilanci aktual është {self.balance:.2f}")

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0.0, interest_rate=0.05):
        """Inicializon një llogari kursimi me një normë interesi."""
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        """Llogarit dhe shton interesin vjetor në bilanc."""
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interesi prej {interest:.2f} u aplikua. Bilanci i ri: {self.balance:.2f}")

def main():
    print("Mirësevini në sistemin e menaxhimit të llogarisë bankare!")
    
    name = input("Shkruani emrin tuaj: ")
    
    while True:
        try:
            balance = float(input("Vendosni bilancin fillestar: "))
            break
        except ValueError:
            print("Ju lutem jepni një numër të vlefshëm!")

    account_type = input("Dëshironi një llogari kursimi? (po/jo): ").strip().lower()
    
    if account_type == "po":
        while True:
            try:
                interest_rate = float(input("Vendosni normën e interesit (p.sh. 0.03 për 3%): "))
                break
            except ValueError:
                print("Ju lutem jepni një numër të vlefshëm!")
        account = SavingsAccount(name, balance, interest_rate)
    else:
        account = BankAccount(name, balance)

    while True:
        print("\n--- MENU ---")
        print("1. Shfaq Bilancin")
        print("2. Depozito Para")
        print("3. Tërhiq Para")
        if isinstance(account, SavingsAccount):
            print("4. Apliko Interesin")
        print("5. Dalje")

        choice = input("Zgjedhni një opsion: ")

        if choice == "1":
            account.display_balance()
        elif choice == "2":
            try:
                amount = float(input("Shkruani shumën për depozitë: "))
                account.deposit(amount)
            except ValueError:
                print("Ju lutem jepni një numër të vlefshëm!")
        elif choice == "3":
            try:
                amount = float(input("Shkruani shumën për tërheqje: "))
                account.withdraw(amount)
            except ValueError:
                print("Ju lutem jepni një numër të vlefshëm!")
        elif choice == "4" and isinstance(account, SavingsAccount):
            account.apply_interest()
        elif choice == "5":
            print("Faleminderit që përdorët sistemin tonë! Mirupafshim!")
            break
        else:
            print("Zgjedhje e pavlefshme! Ju lutem provoni përsëri.")

if __name__ == "__main__":
    main()
