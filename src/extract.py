import requests
from src.utils import retry

@retry(max_attempts=3, delay=2)
def fetch_data() -> dict:
    url = "https://api.open-meteo.com/v1/forecast"

    parameters = {
        "latitude": 49.6116,
        "longitude": 6.1319,
        "hourly": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "precipitation,"
            "wind_speed_10m"
        ),
        "timezone": "Europe/Luxembourg",
        "forecast_days": 2,
    }

    response = requests.get(
        url,
        params=parameters,
        timeout=10,
    )

    response.raise_for_status()

    return response.json()