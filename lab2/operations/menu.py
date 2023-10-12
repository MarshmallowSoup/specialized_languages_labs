from .calculator import Calculator, Subtraction, Sum, Multiplication, Division, SquareRoot, Power

class Menu():

    def __init__(self):
        self.calculator = None
        self.calculations = []  # To store calculation history

    def select_operation(self):
        print("Select an operation:")
        print("1. Make Calculation")
        print("2. Show History")
        print("3. Show Specific Operation from History")
        print("0. Exit")

        choice = input("Enter your choice: ")
        return choice
    
    def make_calculation(self):
        first_number = float(input("Enter first number: "))            
        while True:
            operation = input("Enter the operator (+, -, /, *, ^, √): ")
            if operation not in ("+", "-", "/", "*", "^", "√"):
                print("Invalid operator. Please enter one of: +, -, /, *, ^, √")
            else:
                break
        if operation != '√':
            second_number = float(input("Enter second number: "))
            if operation == "+":
                calculation = Sum(first_number, second_number)
            elif operation == "-":
                calculation = Subtraction(first_number, second_number)
            elif operation == "*":
                calculation = Multiplication(first_number, second_number)
            elif operation == "/":
                calculation = Division(first_number, second_number)
            elif operation == "^":
                calculation = Power(first_number, second_number)
            else:
                raise ValueError("Invalid operator. Please enter one of: +, -, /, *, ^, √")
            result = calculation.calculate()
            print(f"{calculation.first_number} {calculation.operation} {calculation.second_number} = {calculation.result}")
            self.calculations.append(calculation)
            return result
        else:
            calculation = SquareRoot(first_number)
            calculation.calculate()
            print(f"{calculation.operation} ({calculation.first_number})  = {calculation.result}")
            self.calculations.append(calculation)
            result = calculation.result
            return result


    def show_history(self):
        if not self.calculations:
            print("No calculations in history.")
        else:
            for i in range(len(self.calculations)):
                print(f"{i + 1}. {self.calculations[i].first_number} {self.calculations[i].operation} {self.calculations[i].second_number} = {self.calculations[i].result}")

    def show_specific_operation(self):
        if not self.calculations:
            print("No calculations in history.")
            return
        choice = int(input("Enter the calculation number to show: "))
        i = choice - 1
        if i < len(self.calculations):
            if self.calculations[i].operation != '√':
                print(f"{choice}. {self.calculations[i].first_number} {self.calculations[i].operation} {self.calculations[i].second_number} = {self.calculations[i].result}")
            else:
                print(f"{choice}. {self.calculations[i].operation} {self.calculations[i].first_number} = {self.calculations[i].result}")

        else:
            print("Invalid choice. Please enter a valid number.")

    def run(self):
        while True:
            choice = self.select_operation()
            if choice == "0":
                print("Goodbye!")
                break
            elif choice == "1":
                pass
                self.make_calculation()
            elif choice == "2":
                self.show_history()
            elif choice == "3":
                self.show_specific_operation()
            elif choice == "0":
                return 0
            else:
                print("Invalid choice. Please try again.")
