def choose_size():
    while True:
        try:
            width = input("Enter the width of the ASCII art: ")
            if width == " ":
                int(width)
                return width
            else:
                return 0
        except ValueError:
            print("Invalid input. Enter integers for the size.")


def choose_font():
   
    fonts = ["standard", "xcourbi","thin", "asc_____", "alphabet" ]
    print("Available fonts:")
    for index, font in enumerate(fonts, 1):
        print(f"{index}. {font}")

    while True:
        try:
            font_choice = int(input("Choose a font number: "))
            if 1 <= font_choice <= len(fonts):
                return fonts[font_choice - 1]
            else:
                print("Incorrect choice. Please try again.")
        except ValueError:
            print("Invalid input. Enter a font number.")

def choose_color():
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

    print("Available colors:")
    for index, color in enumerate(colors, 1):
        print(f"{index}. {color}")

    while True:
        try:
            color_choice = int(input("Choose a color number: "))
            if 1 <= color_choice <= len(colors):
                return colors[color_choice - 1]
            else:
                print("Incorrect choice. Please try again.")
        except ValueError:
            print("Invalid input. Enter a color number.")