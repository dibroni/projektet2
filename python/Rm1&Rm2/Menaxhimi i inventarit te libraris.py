class Book:
    def __init__(self, title, author, year, copies):
        """Inicializon informacionin e një libri."""
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def display_info(self):
        """Shfaq informacionin për një libër."""
        print(f"Titulli: {self.title}, Autori: {self.author}, Viti: {self.year}, Kopje: {self.copies}")

class Library:
    def __init__(self):
        """Inicializon librarinë me një listë të pashfaqur librash."""
        self.books = []

    def add_book(self, title, author, year, copies):
        """Regjistron një libër në bibliotekë."""
        new_book = Book(title, author, year, copies)
        self.books.append(new_book)
        print(f"Libri '{title}' u regjistrua me sukses!")

    def display_books(self):
        """Shfaq të gjitha librat në bibliotekë që kanë kopje të disponueshme."""
        if not self.books:
            print("Nuk ka libra të regjistruar!")
        else:
            for book in self.books:
                if book.copies > 0:  
                    book.display_info()

    def search_books(self, search_term):
        """Kërkon librat sipas titullit ose autorit."""
        found = False
        for book in self.books:
            if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower():
                book.display_info()
                found = True
        if not found:
            print("Libri nuk u gjet!")

def main():
    library = Library()
    
    while True:
        print("\n--- MENU ---")
        print("1. Regjistro një libër")
        print("2. Shfaq librat në inventar")
        print("3. Kërko një libër")
        print("4. Dalje")

        choice = input("Zgjedh një opsion: ")

        if choice == "1":
            title = input("Shkruaj titullin e librit: ")
            author = input("Shkruaj autorin e librit: ")
            year = input("Shkruaj vitin e publikimit: ")
            while True:
                try:
                    copies = int(input("Shkruaj numrin e kopjeve: "))
                    break
                except ValueError:
                    print("Ju lutem jepni një numër të vlefshëm për kopjet!")
            library.add_book(title, author, year, copies)

        elif choice == "2":
            print("\nLibrat në inventar:")
            library.display_books()

        elif choice == "3":
            search_term = input("Shkruaj titullin ose autorin për kërkim: ")
            print(f"\nKërkimi për '{search_term}':")
            library.search_books(search_term)

        elif choice == "4":
            print("Faleminderit që përdorët sistemin! Mirupafshim!")
            break

        else:
            print("Zgjedhje e pavlefshme! Provoni përsëri.")

if __name__ == "__main__":
    main()
