import pyfiglet
from termcolor import colored
from settings import choose_font, choose_color, choose_size
import re

def preview_and_save_art(ascii_art, width):
    lines = ascii_art.split('\n')
    formatted_art = '\n'.join(line.ljust(width) for line in lines)
    print("\nPreview of the ASCII art:")
    print(formatted_art)
    file_save = input("Do you want to save it in a file? (y/n): ")
    if file_save == 'y':
        file_name = input("Enter the file name to save the ASCII art: ")
        with open('./arts/'+ file_name + ".ascii", 'w') as file:
            file.write(formatted_art)
        print(f'ASCII art has been saved in the file {file_name}')
        return 0
    else:
        return 0


def create_ascii_art():
    user_input = input("Enter a word or phrase to transform into ASCII art: ")
    selected_font = choose_font()
    selected_color = choose_color()
    width = choose_size()
    if width == 0:
        ascii_art = pyfiglet.figlet_format(user_input, font=selected_font)
    else:
        ascii_art = pyfiglet.figlet_format(user_input, font=selected_font, width=width)
    character = replace_character(ascii_art)
    colored_ascii_art = colored(character, color=selected_color)
    preview_and_save_art(colored_ascii_art, width)


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