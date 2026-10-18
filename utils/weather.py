import requests


def get_weather_data():

    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=13.69"
        "&longitude=100.08"
        "&current=temperature_2m,relative_humidity_2m,precipitation"
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
                current["precipitation"]
        }

    except:

        return None
