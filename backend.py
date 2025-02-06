import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise ValueError("API Key not found! Set OPENWEATHER_API_KEY in environment variables.")

BASE_URL = "http://api.openweathermap.org/data/2.5/"


def fetch_weather_data(endpoint, params):
    """Helper function to fetch weather data from OpenWeather API."""
    try:
        params["appid"] = API_KEY
        params["units"] = "metric"
        response = requests.get(BASE_URL + endpoint, params=params)
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"API request error: {e}")
        return None


def get_current_weather(place):
    """Fetches current weather for a given city."""
    data = fetch_weather_data("weather", {"q": place})
    if not data or "main" not in data:
        return None
    return {
        "location": data.get("name"),
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "weather": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"]
    }


def get_forecast_data(place, forecast_days=1):
    """Fetches weather forecast for a given city and number of days."""
    data = fetch_weather_data("forecast", {"q": place})
    if not data or "list" not in data:
        return None
    nr_values = 8 * forecast_days  # 8 forecasts per day (3-hour intervals)
    return data["list"][:nr_values]
