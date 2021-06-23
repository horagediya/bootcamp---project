import requests
# import os
from datetime import datetime

txt_file = open("file.txt", "w")

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

txt_file.write("\n-------------------------------------------------------------")
txt_file.write(str("\nWeather Stats for - {}  || {}".format(location.upper(), date_time)))
txt_file.write("\n-------------------------------------------------------------")

txt_file.write(str("\nCurrent temperature is: {:.2f} deg C".format(temp_city)))
txt_file.write(str("\nCurrent weather desc  :" +weather_desc))
txt_file.write(str("\nCurrent Humidity      :"))
txt_file.write(str( hmdt))
txt_file.write('%')
txt_file.write(str("\nCurrent wind speed    :"))
txt_file.write(str( wind_spd))
txt_file.write('kmph')
txt_file.close()
