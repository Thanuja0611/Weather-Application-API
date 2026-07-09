import requests
from config import API_KEY, BASE_URL


def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            return {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "condition": data["weather"][0]["description"].title()
            }
        else:
            return {"error": data.get("message", "Unable to fetch weather.")}

    except requests.exceptions.RequestException:
        return {"error": "Network Error! Please check your internet connection."}