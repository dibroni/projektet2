class MathHelper:
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)

    def fibonacci(self, n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]
        fib_series = self.fibonacci(n - 1)
        fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

    def sum_list(self, numbers):
        return sum(numbers)

    def average_list(self, numbers):
        return self.sum_list(numbers) / len(numbers) if numbers else 0

    def sort_numbers(self, numbers):
        return sorted(numbers)

class InputValidator:
    def validate_input(self, prompt, type_func=int):
        while True:
            try:
                return type_func(input(prompt))
            except ValueError:
                print("Input i pavlefshëm, ju lutem provoni përsëri.")

class Menu:
    def __init__(self):
        self.math_helper = MathHelper()
        self.validator = InputValidator()

    def main_menu(self):
        while True:
            print("\nMath Helper - Zgjidh një opsion:")
            print("1. Llogarit Faktorialin")
            print("2. Gjenero Serinë Fibonacci")
            print("3. Llogarit Shumën e Listës")
            print("4. Llogarit Mesataren e Listës")
            print("5. Rendit Listën")
            print("6. Dalje")
            
            choice = self.validator.validate_input("Zgjedhja juaj: ")
            
            if choice == 1:
                num = self.validator.validate_input("Jep një numër: ")
                print("Faktoriali:", self.math_helper.factorial(num))
            elif choice == 2:
                num = self.validator.validate_input("Jep numrin e termave: ")
                print("Seria Fibonacci:", self.math_helper.fibonacci(num))
            elif choice == 3:
                numbers = list(map(int, input("Jep numrat e ndarë me hapësirë: ").split()))
                print("Shuma:", self.math_helper.sum_list(numbers))
            elif choice == 4:
                numbers = list(map(int, input("Jep numrat e ndarë me hapësirë: ").split()))
                print("Mesatarja:", self.math_helper.average_list(numbers))
            elif choice == 5:
                numbers = list(map(int, input("Jep numrat e ndarë me hapësirë: ").split()))
                print("Lista e renditur:", self.math_helper.sort_numbers(numbers))
            elif choice == 6:
                print("Dalje nga programi...")
                break
            else:
                print("Zgjedhje e pavlefshme, provo përsëri.")

if __name__ == "__main__":
    menu = Menu()
    menu.main_menu()
