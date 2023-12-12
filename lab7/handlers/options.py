from .apihandler import APIHandler
from dataprocess import JSONParser, DataSaver


class Options:
    def __init__(self,api_url, api_key):
        self.running = True
        self.api_handler = APIHandler(api_key, api_url)

    def list_all_monitors(self):
        endpoint = "api/v2/monitors" 
        monitors = self.api_handler.fetch_data(endpoint=endpoint)
        data = JSONParser(monitors)
        data.parse_and_display()
        save = input("Do ypu want to save data in file?(y/n): ")
        if save == 'y':
            saver = DataSaver(data)
            saver.save_data()
            return 0
        else:
            return 0


    def get_monitor_availability_summary(self):
        # Implement the logic to get a monitor's availability summary
        monitor_id = input("Enter the monitor ID: ")
        print(f"Getting availability summary for monitor {monitor_id}...")
        endpoint = f"api/v2/monitors/{monitor_id}/sla" 
        monitors = self.api_handler.fetch_data(endpoint=endpoint)
        data = JSONParser(monitors)
        data.parse_and_display()
        save = input("Do ypu want to save data in file?(y/n): ")
        if save == 'y':
            saver = DataSaver(data)
            saver.save_data()
            return 0
        else:
            return 0

    def list_all_incidents(self):
        endpoint = f"api/v2/incidents" 
        monitors = self.api_handler.fetch_data(endpoint=endpoint)
        data = JSONParser(monitors)
        data.parse_and_display()
        save = input("Do ypu want to save data in file?(y/n): ")
        if save == 'y':
            saver = DataSaver(data)
            saver.save_data()
            return 0
        else:
            return 0

    def list_incident_timeline_events(self):
        # Implement the logic to list incident timeline events
        incident_id = input("Enter the incident ID: ")
        print(f"Listing timeline events for incident {incident_id}...")
        endpoint = f"api/v2/incidents/{incident_id}/timeline" 
        monitors = self.api_handler.fetch_data(endpoint=endpoint)
        data = JSONParser(monitors)
        data.parse_and_display()
        save = input("Do ypu want to save data in file?(y/n): ")
        if save == 'y':
            saver = DataSaver(data)
            saver.save_data()
            return 0
        else:
            return 0