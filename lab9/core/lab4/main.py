from create_art import ArtCreator
from menu import Menu

def main():
    user_input = Menu()
    text, color, size, symbol = user_input.run_menu()
    art = ArtCreator(text, color, size, symbol)
    result = art.create_art()
    print(result)
    
    with open("text_output.txt", "w") as f:
        f.write(result)

if __name__ == "__main__":
    main()