# 🌍 Countries API Data

 a project i made to practice working with APIs. you type in a country and it tells you the capital and the current weather there.

## what it does

- looks up a country using the **REST Countries API**
- gets the capital city
- checks the weather for that city using **OpenWeatherMap**
- shows it all in a streamlit web app

## what i used

- **Python** (3.x)
- **Streamlit** - for the web UI
- **Requests** - to talk to the APIs
- **python-dotenv** - for hiding API keys

the APIs:

| API | what for |
|-----|----------|
| [REST Countries](https://restcountries.com/) | country info (name, flag, capital) |
| [OpenWeatherMap](https://openweathermap.org/) | weather in the capital city |

## how to run it

1. clone this repo
2. install:
   ```bash
   pip install -r requirements.txt
   ```
3. make a `.env` file in the root folder and add your keys:
   ```
   COUNTRY_API_KEY = your_countries_api_key_here
   WEATHER_API_KEY = your_weather_api_key_here
   ```
4. run it:
   ```bash
   streamlit run app.py
   ```

## things i learned

- how to call APIs with `requests`
- handling errors (timeouts, bad connections, etc.)
- using `dotenv` to keep API keys safe
- building a simple UI with streamlit
- parsing JSON responses and pulling out the data i need
