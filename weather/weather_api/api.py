import requests

API_KEY = 'f252d4ad337c7343054c883f19b61051'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
languages = [
    'sq', 'af', 'ar', 'az', 'eu', 'be', 'bg', 'ca', 'zh_cn', 'zh_tw',
    'hr', 'cz', 'da', 'nl', 'en', 'fi', 'fr', 'gl', 'de', 'el',
    'he', 'hi', 'hu', 'is', 'id', 'it', 'ja', 'kr', 'ku', 'la',
    'lt', 'mk', 'no', 'fa', 'pl', 'pt', 'pt_br', 'ro', 'ru',
    'sr', 'sk', 'sl', 'sp', 'sv', 'th', 'tr', 'ua', 'vi', 'zu',
]

def get_weather_data(city, language='en'):
    url = f'{BASE_URL}?q={city}&appid={API_KEY}&lang={language}'
    response = requests.get(url)
    print(response.json())
    if response.status_code == 200:
        return response.json()  # retorna os dados em formato JSON
    else:
        return None


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32