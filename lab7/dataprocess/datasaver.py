import json
from .dataparser import JSONParser

class DataSaver:
    def __init__(self, json_parser):
        self.json_parser = json_parser

    def save_data(self, filename="output"):
        try:
            save_format = input("Choose save format ('json', 'table'): ").lower()
            if save_format == "json":
                json_filename = f"{filename}.json"
                json_data = json.dumps(self.json_parser.json_data, indent=2)
                with open(json_filename, 'w') as json_file:
                    json_file.write(json_data)
                print(f"Data saved as JSON in {json_filename}")

            elif save_format == "table":
                table_filename = f"{filename}.txt"
                table_data = self.json_parser.dict_to_table(self.json_parser.json_data)
                with open(table_filename, 'w') as table_file:
                    table_file.write(table_data)
                print(f"Data saved as a table in {table_filename}")
            else:
                print("Invalid save format. Please choose 'json' or 'table'.")
        except Exception as e:
            print(f"Error saving data: {e}")
