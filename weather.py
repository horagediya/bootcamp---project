import requests
# import os
from datetime import datetime

s1 = open("file.txt", "w")

api_key = '94928bcd402abce1ddd14006aa8e8456'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

# create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

s1.write("\n-------------------------------------------------------------")
s1.write(str("\nWeather Stats for - {}  || {}".format(location.upper(), date_time)))
s1.write("\n-------------------------------------------------------------")

s1.write(str("\nCurrent temperature is: {:.2f} deg C".format(temp_city)))
s1.write(str("\nCurrent weather desc  :" + weather_desc))
s1.write(str("\nCurrent Humidity      :"))
s1.write(str( hmdt))
s1.write('%')
s1.write(str("\nCurrent wind speed    :"))
s1.write(str( wind_spd))
s1.write('kmph')
s1.close()
