import requests

api_key = 'YOU KEY HERE'


def temperatura_city(cidade):
    weather_data = requests.get(f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={cidade}&aqi=no")
    temp = weather_data.json()['current']['temp_c']

    return f'A temperatura em {cidade}, é de: {temp} graus'

