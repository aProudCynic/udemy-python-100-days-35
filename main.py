import requests

from const import (
    OPEN_WEATHER_API_BASE,
    OPEN_WEATHER_EXCLUDED_DATA,
    MIN_WEATHER_CODE_TO_NOT_INDICATE_PRECIPITATION,
    LENGTH_OF_HOURS_TO_EXAMINE,
    HOUR_OF_NOTIFICATION,
)
from secrets import (
    HOME_LATITUDE,
    HOME_LONGITUDE,
    OPEN_WEATHER_API_KEY,
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN, TWILIO_TEST_PHONE_NUMBER,
    TWILIO_MESSAGING_SERVICE_SID,
)
from twilio.rest import Client


def fetch_weather_data():
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
    return response.json()


def umbrella_is_needed(hourly_data):
    for hour in range(HOUR_OF_NOTIFICATION, HOUR_OF_NOTIFICATION + LENGTH_OF_HOURS_TO_EXAMINE):
        examined_hourly_data = hourly_data[hour]
        weather_data = examined_hourly_data['weather']
        for weather_details in weather_data:
            if int(weather_details['id']) < MIN_WEATHER_CODE_TO_NOT_INDICATE_PRECIPITATION:
                return True
    return False


def send_warning_sms():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        to=TWILIO_TEST_PHONE_NUMBER,
        messaging_service_sid=TWILIO_MESSAGING_SERVICE_SID,
        body='Bring an umbrella',
    )


response_content = fetch_weather_data()
hourly_data = response_content['hourly']
if umbrella_is_needed(hourly_data):
    send_warning_sms()
