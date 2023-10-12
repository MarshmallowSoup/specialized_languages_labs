import math
class Calculator:

    def __init__(self, operation=None, first_number=None, second_number=None):
        if not (isinstance(first_number, (int, float, type(None)))):
            raise ValueError("first_number must be int, float, or None")
        if not (isinstance(second_number, (int, float, type(None)))):
            raise ValueError("second_number must be int, float, or None")
        if operation not in ("+", "-", "/", "*", "^", "√"):
            raise ValueError("Invalid operator. Please enter one of: +, -, /, *, ^, √")
        else:
            self.operation = operation
            self.first_number = first_number
            self.second_number = second_number
            self.result = None

class Sum(Calculator):

    def __init__(self, first_number=None, second_number=None):
        super().__init__('+', first_number, second_number)
    
    def calculate(self):
        self.result = self.first_number + self.second_number
        return self.result


class Subtraction(Calculator):

    def __init__(self, first_number=None, second_number=None):
        super().__init__('-', first_number, second_number)
    
    def calculate(self):
        self.result = self.first_number - self.second_number
        return self.result

class Multiplication(Calculator):

    def __init__(self, first_number=None, second_number=None):
        super().__init__('*', first_number, second_number)
    
    def calculate(self):
        self.result = self.first_number * self.second_number
        return self.result

class Division(Calculator):

    def __init__(self, first_number=None, second_number=None):
        super().__init__('/', first_number, second_number)
    
    def calculate(self):
        try:
            self.result = self.first_number / self.second_number
        except ZeroDivisionError:
            print("error: you can not divide by zero")
        return self.result

class Power(Calculator):

    def __init__(self, first_number=None, second_number=None):
        super().__init__('^', first_number, second_number)
    
    def calculate(self):
        self.result = self.first_number ** self.second_number
        return self.result
    

class SquareRoot(Calculator):

    def __init__(self, first_number=None, second_number=None):
        print(first_number)
        super().__init__('√', first_number, second_number)
    
    def calculate(self):
        self.result = math.sqrt(self.first_number)
        return self.result
