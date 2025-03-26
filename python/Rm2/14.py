balance = 10000

while True:
    print("\n--- ATM ---")
    print("1. Kontrolloni Bilancin")
    print("2. Tërheqeni Parate")
    print("3. Depozitoni Para")
    print("4. Dilni")

    choice = input("Zgjedhni një mundesi (1/2/3/4): ")

    if choice == '1':
        print(f"Bilanci juaj eshte: ${balance}")
        
    elif choice == '2':
        try:
            amount = float(input("Sa para deshironi te terhiqni? $"))
            if amount <= 0:
                print("Ju lutemi futni një shumë pozitive për tërheqjen.")
            elif amount <= balance:
                balance -= amount
                print(f"Keni terhequr ${amount}. Bilanci juaj eshte tani ${balance}.")
            else:
                print("Nuk keni mjaftueshëm para per te terhequr.")
        except ValueError:
            print("Ju lutemi futni një numër të vlefshëm për shumën që dëshironi të tërhiqni.")

    elif choice == '3':
        try:
            amount = float(input("Sa para deshironi te depozitoni? $"))
            if amount <= 0:
                print("Ju lutemi futni një shumë pozitive për depozitimin.")
            else:
                balance += amount
                print(f"Keni depozituar ${amount}. Bilanci juaj eshte tani ${balance}.")
        except ValueError:
            print("Ju lutemi futni një numër të vlefshëm për shumën që dëshironi të depozitoni.")

    elif choice == '4':
        print("Po dilni... Faleminderit qe perdoret ATM!")
        break
    else:
        print("Zgjedhje e gabuar. Ju lutemi zgjidhni perseri.")
