from .apihandler import APIHandler
from dataprocess import JSONParser, DataSaver
from datetime import datetime, timedelta


class Options:
    def __init__(self, api_url, api_key):
        self.running = True
        self.api_handler = APIHandler(api_key, api_url)
        self.operation_history = []

    def list_all_monitors(self):
        endpoint = "api/v2/monitors"
        self.handle_data_fetching(endpoint, JSONParser.parse_monitor_data)

        

    def get_monitor_availability_summary(self):
        monitor_id = input("Enter the monitor ID: ")
        endpoint = f"api/v2/monitors/{monitor_id}/sla"
        self.handle_data_fetching(endpoint, JSONParser.parse_monitor_sla)

    def list_incidents(self):
        five_days_ago = (datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d")
        endpoint = f"api/v2/incidents?from={five_days_ago}"
        self.handle_data_fetching(endpoint, JSONParser.parse_incidents)

    def list_incident_timeline_events(self):
        incident_id = input("Enter the incident ID: ")
        endpoint = f"api/v2/incidents/{incident_id}/timeline"
        self.handle_data_fetching(endpoint, JSONParser.parse_timeline_items)

    def should_save_data(self):
        save = input("Do you want to save data in file?(y/n): ")
        return save.lower() == 'y'

    def save_data(self, data):
        saver = DataSaver(data)
        saver.save_data()

    def handle_data_fetching(self, endpoint, parse_method):
        data = self.api_handler.fetch_data(endpoint=endpoint)
        json_data = JSONParser(data)
        parse_method(json_data)

        self.operation_history.append({
            "endpoint": endpoint,
            "operation": parse_method.__name__,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        if self.should_save_data():
            self.save_data(json_data)

    def track_operation_history(self):
        print("Operation History:")
        for operation in self.operation_history:
            print(f"{operation['timestamp']} - {operation['operation']} - {operation['endpoint']}")
