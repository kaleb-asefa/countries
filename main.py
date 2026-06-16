import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout

from dotenv import load_dotenv
import os

load_dotenv()

COUNTRY_API_KEY = os.getenv("COUNTRY_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


def country_request(country_name):
  params = {'q': country_name}
  try:
    response = requests.get(
      'https://api.restcountries.com/countries/v5',
      headers={'Authorization': f'Bearer {COUNTRY_API_KEY}'}, params=params
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
  
def get_country_coordinates(data):
  if isinstance(data, str):
    return None
  else:
    country_coordinates = data["data"]["objects"][0]["coordinates"]
    return country_coordinates

def get_city_coordinates(data):
  if isinstance(data, str):
    return None
  else:
    city_coordinates = data["data"]["objects"][0]["capitals"][0]['coordinates']
    return city_coordinates
  
def weather_request(city_coordinates):
  params = {'lat': city_coordinates['lat'],
            'lon': city_coordinates['lng'],
            'appid': WEATHER_API_KEY}
  try:
    response = requests.get(
      'https://api.openweathermap.org/data/4.0/onecall/current', params=params
      )
    response.raise_for_status()

    city = response.json()
    return city

  except HTTPError as http_err:
    return f"HTTP error occurred: {http_err}"

  except ConnectionError as conn_err:
    return f"Connection error occurred: {conn_err}"

  except Timeout as timeout_err:
    return f"Timeout error occurred: {timeout_err}"


