import requests

def get_location():
    try:
        response = requests.get("http://ip-api.com/json/")
        data = response.json()
        if data["status"] == "success":
            city = data["city"]
            lat = data["lat"]
            lon = data["lon"]
            return city, lat, lon
        else:
            return "Guwahati", 26.1445, 91.7362
    except:
        return "Guwahati", 26.1445, 91.7362
