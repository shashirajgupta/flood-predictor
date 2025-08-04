import requests

# Replace with your actual key
API_KEY = "c106825ae145200ef3d090b3b8dd2417"
from get_location import get_location


def get_weather1(city):
   try:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url).json()

    if res.get("cod") != 200:
            raise ValueError(res.get("message", "Invalid input or city not found"))

    rainfall = res.get("rain", {}).get("1h", 0)
    temperature = res["main"]["temp"]
    humidity = res["main"]["humidity"]
    water_level = estimate_water_level(rainfall)  # simple simulated logic
     
    return {
        "success": True,
        "city": city,
        "rainfall": float(rainfall),
        "temperature": float(temperature),
        "humidity": float(humidity),
        "water_level": float(water_level)    
    }
   except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def get_weather():
    city, lat, lon = get_location()
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    # Extract relevant data
    rainfall = data.get("rain", {}).get("1h", 0) or 0
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    water_level = estimate_water_level(rainfall)  # simple simulated logic

    return {
        "city": city,
        "rainfall": float(rainfall),
        "temperature": float(temperature),
        "humidity": float(humidity),
        "water_level": float(water_level)
    }

def estimate_water_level(rainfall):
    # Fake logic for now, can be improved
    base = 2.0  # base water level
    return base + (rainfall * 0.1)
