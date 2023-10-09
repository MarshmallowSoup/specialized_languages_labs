import math

class Calculator:
    def __init__(self):
        self.result = 0.0

    def add(self, x, y):
        self.result = x + y
        return self.result

    def subtract(self, x, y):
        self.result = x - y
        return self.result

    def multiply(self, x, y):
        self.result = x * y
        return self.result

    def divide(self, x, y):
        try:
            if y == 0:
                raise ZeroDivisionError("Division by zero is not allowed")
            self.result = x / y
            return self.result
        except ZeroDivisionError as e:
            return str(e)

    def power(self, x, y):
        self.result = x ** y
        return self.result

    def square_root(self, x):
        if x < 0:
            return "Negative numbers do not have a square root"
        self.result = math.sqrt(x)
        return self.result

    def modulus(self, x, y):
        if y == 0:
            return "Division by zero is not allowed"
        self.result = x % y
        return self.result

    def perform_operation(self):
        valid_operators = ('+', '-', '*', '/', '^', '√', '%')
        operation = input("Choose an operation (+, -, *, /, ^, √, %): ")

        if operation not in valid_operators:
            return "Invalid operator"

        if operation in ('+', '-', '*', '/', '^', '%'):
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if operation == '+':
                return self.add(num1, num2)
            elif operation == '-':
                return self.subtract(num1, num2)
            elif operation == '*':
                return self.multiply(num1, num2)
            elif operation == '/':
                return self.divide(num1, num2)
            elif operation == '^':
                return self.power(num1, num2)
            elif operation == '%':
                return self.modulus(num1, num2)
        else:
            num = float(input("Enter a number: "))

            if operation == '√':
                return self.square_root(num)

    def calculate(self):
        print("Welcome to the calculator!")

        while True:
            result = self.perform_operation()

            if isinstance(result, str):
                print("Error: ", result)
            else:
                print("Operation result: ", result)

            another_calculation = input("Do you want to perform another operation? (yes(y)/no(n)): ").lower()
            if another_calculation != 'yes' and another_calculation != 'y':
                print("Thank you for using the calculator. Goodbye!")
                break

# Example usage of the Calculator class:
calc = Calculator()
calc.calculate()
