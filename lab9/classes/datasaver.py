import pandas as pd
from pandas import json_normalize
from pathlib import Path
import json
from .dataparser import JSONParser

class DataSaver:
    def __init__(self, json_parser):
        self.json_parser = json_parser

    def save_data(self):
        try:
            save_format = input("Choose save format ('json', 'csv'): ").lower()
            filename = input("Choose filename: ").lower()
            
            if save_format == "json":
                json_filename = f"{filename}.json"
                json_data = json.dumps(self.json_parser.json_data, indent=2)
                with open(json_filename, 'w') as json_file:
                    json_file.write(json_data)
                print(f"Data saved as JSON in {json_filename}")

            elif save_format == "csv":
                csv_filename = f"{filename}.csv"
                json_data = self.json_parser.json_data  # Assuming this is a dictionary

                # Flatten the nested dictionary
                flat_data = json_normalize(json_data)

                # Save as CSV
                flat_data.to_csv(f'{csv_filename}', encoding='utf-8', index=False)
                print(f"Data saved as a table in {csv_filename}")

            else:
                print("Invalid save format. Please choose 'json' or 'csv'.")
        except Exception as e:
            print(f"Error saving data: {e}")
