BASE_URL= "https://api.open-meteo.com/v1/forecast"
CITY= {
    "name":"shimla",
    "latitude":31.10,
    "longitude":77.17
}
def build_weather_url():
    "open meteo api url"
    latitude=CITY["latitude"]
    longitude=CITY["longitude"]
    url=(
    f"{BASE_URL}"
    f"?latitude={latitude}"
    f"&longitude={longitude}"
    f"&current=temperature_2m,relative_humidity_2m,"
    f"wind_speed_10m,pressure_msl"
)
    return url

import requests
def fetch_weather_data():

    print("1. Building URL")

    url = build_weather_url()

    print(url)

    print("2. Calling Weather API...")

    response = requests.get(url)

    print("3. Weather API Responded")

    response.raise_for_status()

    print("4. Returning JSON")

    return response.json()

## create weather event function
from datetime import datetime
def create_weather_event(weather_data):
    current=weather_data["current"]
    event={
    "city":CITY["name"],
    "temperature_c":current["temperature_2m"],
    "humidity_percent":current["relative_humidity_2m"],
    "wind_speed_kmh":current["wind_speed_10m"],
    "pressure_hpa":current["pressure_msl"],
    "event_time":current["time"],
    "producer_timestamp":datetime.now().isoformat()
}
    return event

def get_weather_event():
    weather_data=fetch_weather_data()
    weather_event=create_weather_event(weather_data)
    return weather_event