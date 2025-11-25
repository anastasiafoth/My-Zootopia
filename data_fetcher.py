import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

URL = "https://api.api-ninjas.com/v1/animals?name="

def load_data_from_api(user_input):
    headers = {
        "X-Api-Key": API_KEY
    }

    url = URL + user_input
    res = requests.get(url, headers=headers)
    return res.json()