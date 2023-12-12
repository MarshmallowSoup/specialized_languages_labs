from dotenv import load_dotenv
from handlers import APIHandler, Menu, Options
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
menu = Menu(endpoint, api_key=api_key)

menu.run_menu()
