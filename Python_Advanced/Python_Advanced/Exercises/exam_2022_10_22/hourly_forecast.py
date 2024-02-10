def forecast(*weather_info):
    weather_dict = {city: weather for city, weather in weather_info}

    sorted_weather = sorted(weather_dict.items(), key=lambda x: x[0])

    sunny, cloudy, rainy = '', '', ''
    for city, weather in sorted_weather:
        if weather == 'Sunny':
            sunny += f'{city} - {weather}\n'
        elif weather == 'Cloudy':
            cloudy += f'{city} - {weather}\n'
        else:
            rainy += f'{city} - {weather}\n'

    return sunny + cloudy + rainy



print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
