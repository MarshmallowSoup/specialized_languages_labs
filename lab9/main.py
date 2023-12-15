from classes.facade import Facade 
class App:

    def __init__(self):
        self.facade = Facade()

    def run_menu(self):
        while True:
            print("\n=== Main Menu ===")
            print("1. Run Calculator Menu")
            print("2. Run API Menu")
            print("3. Run Figures Menu")
            print("4. Run CSV Parse")
            print("5. Run Art Menu")
            print("0. Exit")
            
            choice = input("Enter your choice: ")

            if choice == '1':
                self.facade.run_calculator()
            elif choice == '2':
                self.facade.run_api()
            elif choice == '3':
                self.facade.run_figures()
            elif choice == '4':
                self.facade.run_csv_parse()
            elif choice == '5':
                self.facade.run_art_menu()
            elif choice == '0':
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = App()
    app.run_menu()