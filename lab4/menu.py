from termcolor import COLORS
class Menu:

    def __init__(self):
        self.text = "text"
        self.color = "red"
        self.size = 1
        self.symbol = '@'

    def run_menu(self):
        try:
            self.text = input("Enter text: ")
            self.color = input("Enter color: ")
            if self.color not in COLORS:
                raise ValueError
            self.size = int(input("Enter size: "))
            self.symbol = input("Enter symbol: ")
        except ValueError:
            self.text = "text"
            self.color = "red"
            self.size = 1
            self.symbol = '@'

        return self.text, self.color, self.size, self.symbol
