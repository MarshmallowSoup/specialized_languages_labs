from dotenv import load_dotenv
from handlers.apihandler import APIHandler
import os

# Load environment variables from .env
load_dotenv()

# Get values from environment variables
endpoint = os.getenv("ENDPOINT")
api_key = os.getenv("API_KEY")

# Check if required variables are present
if endpoint is None or api_key is None:
    raise ValueError("Please set values for ENDPOINT and API_KEY in the .env file.")

# Initialize APIHandler with endpoint and set API key
apihandler = APIHandler(endpoint)
apihandler.set_api_key(api_key)

# Fetch data using APIHandler
print(apihandler.fetch_data("monitors"))