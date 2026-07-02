import requests

api_key = "87a8c232e98289e9b300ff041eb611c9"

while True:
    location = input("Enter location: ").lower()

    weather_data = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}"
    ).json()

    if weather_data['cod'] == '404':
        print("Invalid location!")
        continue
    break

print(weather_data)
    
description = weather_data['weather'][0]['description']
temperature = round(weather_data['main']['temp'])
feels_like = round(weather_data['main']['feels_like'])
high = round(weather_data['main']['temp_max'])
low = round(weather_data['main']['temp_min'])


print(f"The weather in {location.capitalize()} is {temperature} °C with {description}.")
print(f"It feels like {feels_like} °C.")
print(f"Today's high is {high} °C and today's low is {low} °C.")
