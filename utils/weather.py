import requests


def get_weather_data():

    latitude = 13.3611
    longitude = 100.9847

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current=temperature_2m,"
        "relative_humidity_2m,"
        "precipitation,"
        "wind_speed_10m"
    )

    try:

        response = requests.get(
            url,
            timeout=10
        )

        data = response.json()

        current = data["current"]

        return {
            "temperature":
                current["temperature_2m"],

            "humidity":
                current["relative_humidity_2m"],

            "rain":
                current["precipitation"],

            "wind":
                current["wind_speed_10m"]
        }

    except:

        return None
