# ASCII-арт для літер A-Z та чисел 0-9
# ASCII-арт для літер A-Z та чисел 0-9
import re


ascii_art = {
    "A": ["  A  ", " A A ", "AAAAA", "A   A", "A   A"],
    "B": ["BBB  ", "B  B ", "BBB  ", "B  B ", "BBB  "],
    "C": [" CCC ", "C   C", "C    ", "C   C", " CCC "],
    "D": ["DDDD ", "D   D", "D   D", "D   D", "DDDD "],
    "E": ["EEEE ", "E    ", "EEE  ", "E    ", "EEEE "],
    "F": ["FFFF ", "F    ", "FFF  ", "F    ", "F    "],
    "G": [" GGG ", "G    ", "G  GG", "G   G", " GGG "],
    "H": ["H   H", "H   H", "HHHHH", "H   H", "H   H"],
    "I": [" III ", "  I  ", "  I  ", "  I  ", " III "],
    "J": ["  J  ", "   J ", "   J ", "J  J ", " JJ  "],
    "K": ["K  K ", "K K  ", "KK   ", "K K  ", "K  K "],
    "L": ["L    ", "L    ", "L    ", "L    ", "LLLLL"],
    "M": ["M   M", "MM MM", "M M M", "M   M", "M   M"],
    "N": ["N   N", "NN  N", "N N N", "N  NN", "N   N"],
    "O": [" OOO ", "O   O", "O   O", "O   O", " OOO "],
    "P": ["PPP  ", "P   P", "PPP  ", "P    ", "P    "],
    "Q": [" QQQ ", "Q   Q", "Q Q Q", "Q  QQ", " QQ Q"],
    "R": ["RRR  ", "R   R", "RRR  ", "R R  ", "R  RR"],
    "S": [" SSS ", "S    ", " SSS ", "    S", " SSS "],
    "T": ["TTTTT", "  T  ", "  T  ", "  T  ", "  T  "],
    "U": ["U   U", "U   U", "U   U", "U   U", " UUU "],
    "V": ["V   V", "V   V", "V   V", " V V ", "  V  "],
    "W": ["W   W", "W   W", "W W W", "WW WW", "W   W"],
    "X": ["X   X", "X   X", " X X ", "X   X", "X   X"],
    "Y": ["Y   Y", "Y   Y", " YYY ", "   Y  ", "   Y  "],
    "Z": ["ZZZZZ", "   Z ", "  Z  ", " Z   ", "ZZZZZ"],
    "0": [" 000 ", "0   0", "0 0 0", "0   0", " 000 "],
    "1": ["  1  ", " 11  ", "  1  ", "  1  ", "1111 "],
    "2": [" 222 ", "2   2", "   2 ", "  2  ", "2222 "],
    "3": ["3333 ", "   3 ", " 33  ", "   3 ", "3333 "],
    "4": ["4  4 ", "4  4 ", "4444 ", "   4 ", "   4 "],
    "5": ["5555 ", "5    ", "555  ", "   5 ", "555  "],
    "6": [" 666 ", "6    ", "666  ", "6   6", " 666 "],
    "7": ["77777", "   7 ", "  7  ", " 7   ", " 7   "],
    "8": [" 888 ", "8   8", " 888 ", "8   8", " 888 "],
    "9": [" 999 ", "9   9", " 9999", "    9", "    9", " 999"],
}


# Функція для генерації ASCII-арту з вирівнюванням і кольоровими опціями

def replace_character(input_string):
    character = input("Input a symbol to replace in ASCII art (e.g., @, #, *): ")
    if character == " " or "\n":
        return input_string
    else:
        if (len(input_string)):
            pattern = r'\S'
            replaced = re.sub(pattern, character, input_string)
            return replaced
        else:
            return input_string

# Функція для отримання розмірів ASCII-арту в межах допустимого діапазону
def get_art_size():
    while True:
        try:
            width = int(input("Введіть ширину ASCII-арту (від 1 до 100): "))
            height = int(input("Введіть висоту ASCII-арту (від 1 до 100): "))
            if 1 <= width <= 100 and 1 <= height <= 100:
                return width, height
            else:
                print("Розміри повинні бути в межах допустимого діапазону.")
        except ValueError:
            print("Будь ласка, введіть числа.")


# Функція для отримання вирівнювання тексту в ASCII-арті
def get_alignment():
    while True:
        alignment = (
            input("Виберіть вирівнювання тексту (left, center, right): ")
            .strip()
            .lower()
        )
        if alignment in ["left", "center", "right"]:
            return alignment
        else:
            print("Введіть допустимий варіант вирівнювання (left, center, right).")


# Функція для вибору палітри кольорів
def get_color_palette():
    while True:
        color_palette = (
            input("Виберіть палітру кольорів (чорно-білий, відтінки сірого): ")
            .strip()
            .lower()
        )
        if color_palette in ["чорно-білий", "відтінки сірого"]:
            return color_palette
        else:
            print("Введіть допустиму палітуру кольорів (чорно-білий, відтінки сірого).")


# Функція для збереження ASCII-арту у файл
def save_ascii_art_to_file(art, filename):
    with open(filename, "w") as file:
        file.write(art)


# Функція для попереднього перегляду ASCII-арту
def preview_ascii_art(art):
    print("Попередній перегляд вашого ASCII-арту:")
    print(art)
    input("Натисніть Enter для продовження...")

# Функція для виводу алфавіту
def print_alphabet():
    for letter in ascii_art:
        print(letter)
        for line in ascii_art[letter]:
            print(line)
        print()

# Виклик функції для виводу алфавіту
print_alphabet()
# Запитуємо користувача, чи він хоче зберегти ASCII-арт у файл
# save_to_file = input("Зберегти ASCII-арт у файл? (Так/Ні): ").strip().lower()
# if save_to_file == "так":
#     filename = input("Введіть ім'я файлу для збереження (наприклад, ascii_art.txt): ")
#     save_ascii_art_to_file(shaded_ascii_art_text, filename)
#     print(f"ASCII-арт збережено у файлі '{filename}'")
