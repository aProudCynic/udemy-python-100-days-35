import requests

from const import (
    OPEN_WEATHER_API_BASE,
    OPEN_WEATHER_EXCLUDED_DATA,
)
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
        'exclude': OPEN_WEATHER_EXCLUDED_DATA,
        'appid': OPEN_WEATHER_API_KEY,
    }
)
response.raise_for_status()
print(response.content)
