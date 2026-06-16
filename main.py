import requests
import json

from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

params = {'q':'ethi'}

response = requests.get(
  'https://api.restcountries.com/countries/v5',
  headers={'Authorization': f'Bearer {API_KEY}'}, params=params
)
data = response.json()
print(json.dumps(data, indent=2))
print(response.status_code)
