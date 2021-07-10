import requests

from const import OPEN_WEATHER_API_BASE
from secrets import (
    HOME_LATITUDE,
    HOME_LONGITUDE,
    OPEN_WEATHER_API_KEY,
)

response = requests.get(
    url=OPEN_WEATHER_API_BASE,
    params={
        'lat': HOME_LATITUDE,
        'lon': HOME_LONGITUDE,
        'appid': OPEN_WEATHER_API_KEY,
    }
)
print(response.status_code)
print(response.json())
