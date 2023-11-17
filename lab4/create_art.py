from alphabet import return_aplhabet
from termcolor import COLORS, colored

class ArtCreator:

    def __init__(self, text, color, size, symbol) -> None:
        self.text = text.upper()
        self.color = color
        self.size = size
        self.symbol = symbol
        self.alphabet = return_aplhabet()

    def vertical_to_horisontal(self):
        letters = []
        symbols = []
        alphbet = self.alphabet
        alphbet_list = []
        text = self.text

        for char in text:
            alphbet_list.append(alphbet[char])

        for j in range(5):
            for i in range(len(text)):
                letters.append(alphbet_list[i][j])

        for i in letters:
            for x in i:
                symbols.append(x)
            symbols.append(0)      
        
        return symbols
    
    def create_msg(self):
        arr = self.vertical_to_horisontal()
        char = self.symbol
        text = self.text
        res = ""
        for i in range(len(arr)):
            if(i % (6*len(text)) == 0):
                res += '\n'
            if arr[i] != " ":
                res += char
            else: 
                res += ' '
        return res
    
    def create_art(self):
        art = self.create_msg()
        with open("text.txt", 'w') as file:
            file.write(art)

        res = ""

        with open("text.txt", 'r') as f:
            for line in f:
                output = "".join([self.size * c for c in line.strip() ])
                for _ in range(self.size):
                    res = res + output+ '\n'

        if self.symbol != ' ':
            modification = ''
            for letter in res:
                if letter == ' ' or letter == '\n':
                    modification += letter
                else:
                    modification += self.symbol
            res = modification
        
        return colored(res, self.color)

        
         

