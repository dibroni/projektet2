class ATM:
    def __init__(self):
        self.balance = 10000  
    
    def menu(self):
        while True:
            print("\n--- Meni i ATM-së ---")
            print("1. Kontrolloni Bilancin")
            print("2. Tërheqeni Paratë")
            print("3. Depozitoni Para")
            print("4. Dilni")
            choice = input("Zgjedhni një mundësi (1/2/3/4): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.withdraw_money()
            elif choice == '3':
                self.deposit_money()
            elif choice == '4':
                print("Po dilni... Faleminderit që përdorët ATM-në!")
                break
            else:
                print("Zgjedhje e gabuar. Ju lutemi, zgjidhni përsëri.")
    
    def check_balance(self):
        print(f"Bilanci juaj aktual është: ${self.balance}")
    
    def withdraw_money(self):
        amount = float(input("Sa para dëshironi të tërhiqni? $"))
        if amount <= self.balance:
            self.balance -= amount
            print(f"Tërheqja ishte e suksesshme! Keni tërhequr ${amount}.")
        else:
            print("Nuk keni mjaftueshëm balancë. Nuk mund të tërhiqni këtë shumë.")
    
    def deposit_money(self):
        amount = float(input("Sa para dëshironi të depozitoni? $"))
        self.balance += amount
        print(f"Depozita ishte e suksesshme! Keni depozituar ${amount}.")
    


atm = ATM()
atm.menu()
