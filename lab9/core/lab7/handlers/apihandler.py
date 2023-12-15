import requests

class APIHandler:
    def __init__(self, api_url, api_key=None):
        self.api_url = api_url
        self.api_key = api_key

    def set_api_key(self, api_key):
        self.api_key = api_key

    def fetch_data(self, endpoint, params=None):
        try:
            headers = {'Authorization': f'Bearer {self.api_key}'} if self.api_key else None
            response = requests.get(f'{self.api_url}/{endpoint}', params=params, headers=headers)
            response.raise_for_status()  # Raise an error for non-200 status codes
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
            return None
        
    def post_data(self, endpoint, data=None):
        try:
            headers = {'Authorization': f'Bearer {self.api_key}'} if self.api_key else None
            response = requests.post(f'{self.api_url}/{endpoint}', json=data, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error posting data: {e}")
            return None
        
    def patch_data(self, endpoint, data=None):
        try:
            headers = {'Authorization': f'Bearer {self.api_key}'} if self.api_key else None
            response = requests.patch(f'{self.api_url}/{endpoint}', json=data, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error patching data: {e}")
            return None

    def delete_data(self, endpoint):
        try:
            headers = {'Authorization': f'Bearer {self.api_key}'} if self.api_key else None
            response = requests.delete(f'{self.api_url}/{endpoint}', headers=headers)
            response.raise_for_status()
            return "Data deleted successfully"
        except requests.RequestException as e:
            print(f"Error deleting data: {e}")
            return None
