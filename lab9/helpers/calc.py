import math


def calculate(operation, decimals):
    
    first_number, second_number, operator = operation

    try:
        if operator == "+":
            operation.append(first_number + second_number)
        elif operator == "-":
            operation.append(first_number - second_number)
        elif operator == "*":
            operation.append(first_number * second_number)
        elif operator == "/":
            operation.append(first_number / second_number)
        elif operator == "^":
            operation.append(first_number**second_number)
        elif operator == "%":
            operation.append(first_number % second_number)
        elif operator == "sqrt":
            print("Warning: Square root function takes only first number")
            operation.pop(1)
            operation.append(math.sqrt(first_number))
        print("Result: " + str(round(operation[-1], decimals)))
        return operation
    except ZeroDivisionError:
        print("error: you can not divide by zero")


def check():
    operation = []
    while True:
        try:
            first_number = float(input("Enter the first number: "))
            second_number = float(input("Enter the second number: "))
            if not (
                isinstance(first_number, (int, float))
                and isinstance(second_number, (int, float))
            ):
                raise ValueError("Both inputs must be numbers (int or float).")
            operation = [first_number, second_number]
        except ValueError as e:
            print(f"Error: {e}")
            continue
        while len(operation) == 2:
            try:
                operator = input("Enter the operator (+, -, /, *, ^, %, sqrt): ")
                if operator not in ("+", "-", "/", "*", "^", "%", "sqrt"):
                    raise ValueError(
                        "Invalid operator. Please enter one of: +, -, /, *, ^, %, sqrt"
                    )

                operation.append(operator)
                return operation

            except ValueError as e:
                print(f"Error: {e}")
                continue


def calculator(decimals):
    operation = check()
    result = calculate(operation, decimals)

    return result


def get_operation(history, decimals):
    while True:
        try:
            index = int(input("Insert number of operation from history: "))
            if index < 1 or index > len(history):
                print("Error: Index is out of range. Please enter a valid index.")
                continue
            operation = history[index - 1]
            if len(operation) == 3:
                print(
                    f"{index}. {operation[1]} {round(operation[0], decimals)} = {round(operation[-1], decimals)}"
                )
            else:
                print(
                    f"{index}. {round(operation[0], decimals)} {operation[2]} {round(operation[1], decimals)} = {round(operation[-1], decimals)}"
                )
            return 0
        except ValueError as e:
            print(f"Error: {e}")
            continue


def append_history(history, operation, history_limit):
    history.append(operation)
    if len(history) > history_limit:
        history = history[-history_limit:]
    return history


def print_history(history):
    print("Calculations history:")
    indexes = [0, 2, 1]
    index_number = 1
    for item in history:
        if len(item) == 3:
            print(f"{index_number}. {item[1]} {item[0]} = {item[-1]}")
        elif len(item) == 4:
            formatted_item = " ".join([str(item[i]) for i in indexes])
            print(f"{index_number}. {formatted_item} = {item[-1]};")
            index_number += 1


def settings(history_limit, decimals):
    while True:
        print(
            f"""
          ===SETTINGS===
          1 - Set history limit             | Current: {history_limit}
          2 - Set number of decimal digits  | Current: {decimals}
          0 - Exit to the menu
          """
        )
        choice = input("Insert a value: ")
        if choice == "1":
            # Set history limit
            history_limit = int(input("Enter history limit: "))
            print(f"History limit set to {history_limit}")
        elif choice == "2":
            # Set number of decimal digits
            decimals = int(input("Enter the number of decimal digits: "))
            print(f"Decimal digits set to {decimals}")
        elif choice == "0":
            break
        else:
            print("Choose a correct option.")
    return decimals, history_limit


def menu():
    # default settings
    decimals = 1
    history_limit = 10
    history = []
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
            operation = calculator(decimals)
            history = append_history(history, operation, history_limit)
        elif choice == "2":
            print_history(history)
        elif choice == "3":
            get_operation(history, decimals)
        elif choice == "4":
            decimals, history_limit = settings(history_limit, decimals)
        elif choice == "0":
            return 0
        else:
            print("Choose a correct option.")


if __name__ == "__main__":
    menu()
