from .art_text import create_ascii_art
def main_menu():
    while True:
        print("\nMain menu:")
        print("1. Create ASCII art")
        print("2. Exit")
        choice = input("Select an option (1 or 2): ")

        if choice == '1':
            create_ascii_art()
        elif choice == '2':
            break
        else:
            print("Incorrect choice. Please try again.")
