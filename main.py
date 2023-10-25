# Name: Patrick Liu
# Student Number: 101142730

import datetime as dt
import requests
import sys

request_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = open('API_KEY', 'r').read()

with open('output.txt', 'w') as f:
    for x in range(1, len(sys.argv)):

        city = sys.argv[x]
        url = request_url + "appid=" + api_key + "&q=" + city
        response = requests.get(url).json()

        location = response['name']
        temperature = response['main']['temp']
        pressure = response['main']['pressure']
        humidity = response['main']['humidity']
        wind_speed = response['wind']['speed']
        wind_direction = response['wind']['deg']
        sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
        sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
        weather_description = response['weather'][0]['description']

        f.write(location + "\n" + str(temperature) + "\n" + str(pressure) + "\n" + str(humidity) + "\n" +
                str(wind_speed) + "\n" + str(wind_direction) + "\n" + str(sunrise_time) + "\n" +
                str(sunset_time) + "\n" + weather_description + "\n\n")

        # For Visualization
        # f.write("Location: " + location + "\n" +
        #         "Temperature in Kelvin: " + str(temperature) + "\n" +
        #         "Pressure: " + str(pressure) + "\n" +
        #         "Humidity: " + str(humidity) + "\n" +
        #         "Wind Speed: " + str(wind_speed) + "\n" +
        #         "Wind Direction: " + str(wind_direction) + "\n" +
        #         "Sunrise Time: " + str(sunrise_time) + "\n" +
        #         "Sunset Time: " + str(sunset_time) + "\n" +
        #         "Weather Description: " + weather_description + "\n\n")

f.close()

