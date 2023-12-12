import json
from tabulate import tabulate

class JSONParser:
    def __init__(self, json_data):
        self.json_data = json_data

    def parse_and_display(self):
        try:
            # Load JSON data
            data = json.loads(self.json_data)
            
            # Check if the JSON data is a list of dictionaries
            if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                # Display each dictionary as a table
                for idx, item in enumerate(data, start=1):
                    table = self.dict_to_table(item)
                    print(f"Table {idx}:\n{table}\n")
            else:
                # Display the entire JSON data as a table
                table = self.dict_to_table(data)
                print(f"Table 1:\n{table}\n")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

    def dict_to_table(self, dictionary):
        # Convert dictionary to a list of (key, value) pairs
        table_data = [(key, value) for key, value in dictionary.items()]
        
        # Display the table using tabulate
        table = tabulate(table_data, headers=["Key", "Value"], tablefmt="fancy_grid")
        return table
    
