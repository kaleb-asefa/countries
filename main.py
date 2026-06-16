import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout

from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")


def country_request(country_name):
  params = {'q': country_name}
  try:
    response = requests.get(
      'https://api.restcountries.com/countries/v5',
      headers={'Authorization': f'Bearer {API_KEY}'}, params=params
      )
    response.raise_for_status()

    data = response.json()

    if not data['data']['objects']:
      return f'No data found for country: {country_name}'
    
    else:
      return data

  except HTTPError as http_err:
    return f"HTTP error occurred: {http_err}"

  except ConnectionError as conn_err:
    return f"Connection error occurred: {conn_err}"

  except Timeout as timeout_err:
    return f"Timeout error occurred: {timeout_err}"


