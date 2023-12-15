from .apihandler import APIHandler
from .api_options import Options

class APIMenu:
    def __init__(self,api_url, api_key):
        self.running = True
        self.options = Options(api_key, api_url)

    def display_menu(self):
        print("===== Menu =====")
        print("1. List all existing monitors")
        print("2. Get a monitor's availability summary")
        print("3. List incidents from 5 days")
        print("4. List incident timeline events")
        print("5. Show history")
        print("6. Exit")

    def run_menu(self):
        while self.running:
            self.display_menu()
            choice = input("Enter your choice (1-6): ")
            self.process_choice(choice)

    def process_choice(self, choice):
        if choice == '1':
            self.options.list_all_monitors()
        elif choice == '2':
            self.options.get_monitor_availability_summary()
        elif choice == '3':
            self.options.list_incidents()
        elif choice == '4':
            self.options.list_incident_timeline_events()
        elif choice == '5':
            self.options.track_operation_history()
        elif choice == '6':
            self.exit_menu()
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


    def exit_menu(self):
        print("Exiting the menu.")
        self.running = False