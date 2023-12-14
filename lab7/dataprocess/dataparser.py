import json
from datetime import datetime

class JSONParser:
    def __init__(self, json_data):
        self.json_data = json_data

    def json_output(self, data=None, level=0):
        """
        Recursively formats and prints JSON data in a pretty way with dynamic indentation depth.

        Parameters:
            data (dict or list): The JSON data to format and print. If not provided, uses the data from the instance.
            level (int): Current indentation level.
        """
        data = data if data is not None else self.json_data
        indent = 2  # Default indentation width

        if level > 10:  # Add a limit to recursion depth to avoid infinite loops
            print("Warning: Maximum recursion depth reached.")
            return

        if isinstance(data, dict):
            # Print curly braces for dictionaries
            print("{")
            for key, value in data.items():
                # Indentation for each key-value pair
                print(" " * (level + 1) * indent + f'"{key}": ', end="")
                # Recursive call for nested structures
                self.json_output(value, level + 1)
                print(",")
            # Closing curly brace
            print(" " * level * indent + "}")
        elif isinstance(data, list):
            # Print square brackets for lists
            print("[")
            for item in data:
                # Indentation for each list item
                print(" " * (level + 1) * indent, end="")
                # Recursive call for nested structures
                self.json_output(item, level + 1)
                print(",")
            # Closing square bracket
            print(" " * level * indent + "]")
        else:
            # Print primitive values
            print(f'"{data}"' if isinstance(data, str) else str(data), end="")

    def parse_timeline_items(self):
        try:
            data = self.json_data.get("data", [])

            for item in data:
                item_id = item.get("id")
                item_type = item.get("type")
                attributes = item.get("attributes", {})
                item_type_attr = attributes.get("item_type")
                at = attributes.get("at")
                content = attributes.get("data", {}).get("content")
                links = attributes.get("data", {}).get("links")

                # Convert the timestamp to a datetime object
                at_datetime = datetime.strptime(at, "%Y-%m-%dT%H:%M:%S.%fZ")

                # Display or process the extracted information as needed
                print(f"Item ID: {item_id}")
                print(f"Item Type: {item_type}")
                print(f"Item Type Attribute: {item_type_attr}")
                print(f"At: {at_datetime}")
                print(f"Content: {content}")
                print(f"Links: {links}")
                print("\n")

        except Exception as e:
            print(f"Error parsing JSON: {e}")

    def parse_monitor_data(self):
        try:
            # Parse JSON data
            parsed_data = self.json_data

            # Extract monitors
            monitors = parsed_data.get('data', [])

            # Format and return readable output
            output = ""
            for monitor in monitors:
                attributes = monitor.get('attributes', {})
                monitor_id = monitor.get('id', '')
                monitor_type = attributes.get('monitor_type', '')
                status = attributes.get('status', '')
                url = attributes.get('url', '')

                output += f"Monitor ID: {monitor_id}\n"
                output += f"Monitor Type: {monitor_type}\n"
                output += f"Status: {status}\n"
                output += f"URL: {url}\n"
                output += "-" * 30 + "\n"
            
            print(output)        
            return output

        except json.JSONDecodeError as e:
            return f"Error decoding JSON: {e}"

    def parse_incidents(self):
        incidents = self.json_data.get("data", [])
        output = ""

        for incident in incidents:
            incident_id = incident.get("id", "N/A")
            incident_type = incident.get("type", "N/A")
            incident_attributes = incident.get("attributes", {})

            name = incident_attributes.get("name", "N/A")
            url = incident_attributes.get("url", "N/A")
            http_method = incident_attributes.get("http_method", "N/A")
            cause = incident_attributes.get("cause", "N/A")
            started_at = incident_attributes.get("started_at", "N/A")
            acknowledged_at = incident_attributes.get("acknowledged_at", "N/A")
            acknowledged_by = incident_attributes.get("acknowledged_by", "N/A")
            resolved_at = incident_attributes.get("resolved_at", "N/A")
            resolved_by = incident_attributes.get("resolved_by", "N/A")

            response_url = incident_attributes.get("response_url", "N/A")

            output += f"""
            Incident ID: {incident_id}
            Type: {incident_type}
            Name: {name}
            URL: {url}
            HTTP Method: {http_method}
            Cause: {cause}
            Started At: {started_at}
            Acknowledged At: {acknowledged_at}
            Acknowledged By: {acknowledged_by}
            Resolved At: {resolved_at}
            Resolved By: {resolved_by}
            Response URL: {response_url}
            """

            print(output)

        return output.strip()
    def parse_monitor_sla(self):
        try:
            data = self.json_data.get("data", {})
            attributes = data.get("attributes", {})

            monitor_sla = {
                "id": data.get("id", "N/A"),
                "type": data.get("type", "N/A"),
                "availability": attributes.get("availability", "N/A"),
                "total_downtime": attributes.get("total_downtime", "N/A"),
                "number_of_incidents": attributes.get("number_of_incidents", "N/A"),
                "longest_incident": attributes.get("longest_incident", "N/A"),
                "average_incident": attributes.get("average_incident", "N/A"),
            }

            print("Parsed Monitor SLA:")
            for key, value in monitor_sla.items():
                print(f"{key}: {value}")


        except Exception as e:
            print(f"Error parsing Monitor SLA JSON: {e}")
