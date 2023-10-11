from calculator import Calculator, Substraction, Sum, Multiplication, Division, SquareRoot, Power

class Menu():

    def __init__(self):
        self.history = []
    
    def append_history(self, calculation):
        self.history.append(calculation)
        return self.history

    def calc_input():
        operator = input("Enter the operator (+, -, /, *, ^, %, sqrt): ")
        if operator not in ("+", "-", "/", "*", "^", "%", "sqrt"):
            raise ValueError(
                "Invalid operator. Please enter one of: +, -, /, *, ^, %, sqrt"
            )
        if operator != "sqrt":
            try:
                first_number = float(input("Enter the first number: "))
                second_number = float(input("Enter the second number: "))
                if not (
                    isinstance(first_number, (int, float))
                    and isinstance(second_number, (int, float))
                ):
                    raise ValueError("Both inputs must be numbers (int or float).")   
            except ValueError as e:
                print(f"Error: {e}")
            
        return 0

    def menu():
        while True:
            print(
                """
                Welcome to calculator!
                Menu: 
                1 - Make a calculation
                2 - Show history
                3 - Show specific operation from history
                4 - Settings
                0 - Exit
                """
            )
            choice = input("Insert a value: ")
            if choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "0":
                return 0
            else:
                print("Choose a correct option.")

        